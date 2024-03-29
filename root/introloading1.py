import ui
import uiScriptLocale
import net
import app
import dbg
import player
import background
import wndMgr

import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import chrmgr
import colorInfo
import constInfo

import playerSettingModule
import stringCommander
import emotion

####################################
# ���� ������ ���� ��� �ε� �д�
####################################
import uiRefine
import uiToolTip
import uiAttachMetin
import uiPickMoney
import uiChat
import uiMessenger
import uiHelp
import uiWhisper
import uiPointReset
import uiShop
import uiExchange
import uiSystem
import uiOption
import uiRestart
####################################

class LoadingWindow(ui.ScriptWindow):
	def __init__(self, stream):
		print "NEW LOADING WINDOW -------------------------------------------------------------------------------"
		ui.Window.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_LOAD, self)

		self.stream=stream
		self.loadingImage=0
		self.loadingGage=0
		self.errMsg=0
		self.update=0
		self.playerX=0
		self.playerY=0
		self.loadStepList=[]

	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE LOADING WINDOW"
		net.SetPhaseWindow(net.PHASE_WINDOW_LOAD, 0)
		ui.Window.__del__(self)

	def Open(self):
		print "OPEN LOADING WINDOW -------------------------------------------------------------------------------"

		#app.HideCursor()

		try:
			pyScrLoader = ui.PythonScriptLoader()
			
			if localeInfo.IsYMIR() or localeInfo.IsWE_KOREA() or localeInfo.IsCANADA() or localeInfo.IsBRAZIL() or localeInfo.IsEUROPE():
				pyScrLoader.LoadScriptFile(self, "poccix_loading.py")
			else:			
				pyScrLoader.LoadScriptFile(self, "poccix_loading.py")
		except:
			import exception
			exception.Abort("LodingWindow.Open - LoadScriptFile Error")

		try:
			self.loadingGage=self.GetChild("img_gauge_full")
		except:
			import exception
			exception.Abort("LodingWindow.Open - LoadScriptFile Error")

		self.loadingGage.SetPercentage(2, 100)

		self.Show()

		chrSlot=self.stream.GetCharacterSlot()
		net.SendSelectCharacterPacket(chrSlot)

		app.SetFrameSkip(0)

	def Close(self):
		print "---------------------------------------------------------------------------- CLOSE LOADING WINDOW"

		app.SetFrameSkip(1)

		self.loadStepList=[]
		self.loadingImage=0
		self.loadingGage=0
		self.errMsg=0
		self.ClearDictionary()
		self.Hide()

	def OnPressEscapeKey(self):
		app.SetFrameSkip(1)
		self.stream.SetLoginPhase()
		return TRUE

	def __SetNext(self, next):
		if next:
			self.update=ui.__mem_func__(next)
		else:
			self.update=0

	def __SetProgress(self, p):
		if self.loadingGage:
			self.loadingGage.SetPercentage(2+98*p/100, 100)

	def DEBUG_LoadData(self, playerX, playerY):
		self.playerX=playerX
		self.playerY=playerY

		self.__RegisterSkill() ## �ε� �߰��� ���� �ϸ� ���� �߻�
		self.__RegisterTitleName()
		if app.ENABLE_REBORN_SYSTEM:		
			self.__RegisterTitleRebornName()	
		if app.ENABLE_TITLE_SYSTEM:	
			self.__RegisterTitlePrestigeName()	
		self.__RegisterColor()
		self.__InitData()
		self.__LoadMap()
		self.__LoadSound()
		self.__LoadEffect()
		self.__LoadWarrior()
		self.__LoadAssassin()
		self.__LoadSura()
		self.__LoadShaman()
		self.__LoadSkill()
		self.__LoadEnemy()
		self.__LoadNPC()
		self.__StartGame()

	def LoadData(self, playerX, playerY):
		self.playerX=playerX
		self.playerY=playerY

		self.__RegisterDungeonMapName()
		self.__RegisterSkill() ## �ε� �߰��� ���� �ϸ� ���� �߻�
		self.__RegisterTitleName()
		if app.ENABLE_REBORN_SYSTEM:		
			self.__RegisterTitleRebornName()	
		if app.ENABLE_TITLE_SYSTEM:	
			self.__RegisterTitlePrestigeName()	
		self.__RegisterColor()
		self.__RegisterEmotionIcon()

		self.loadStepList=[
			(0, ui.__mem_func__(self.__InitData)),
			(10, ui.__mem_func__(self.__LoadMap)),
			(30, ui.__mem_func__(self.__LoadSound)),
			(40, ui.__mem_func__(self.__LoadEffect)),
			(50, ui.__mem_func__(self.__LoadWarrior)),
			(60, ui.__mem_func__(self.__LoadAssassin)),
			(70, ui.__mem_func__(self.__LoadSura)),
			(80, ui.__mem_func__(self.__LoadShaman)),
			(90, ui.__mem_func__(self.__LoadSkill)),
			(93, ui.__mem_func__(self.__LoadEnemy)),
			(97, ui.__mem_func__(self.__LoadNPC)),

			# GUILD_BUILDING
			(98, ui.__mem_func__(self.__LoadGuildBuilding)),
			# END_OF_GUILD_BUILDING

			(100, ui.__mem_func__(self.__StartGame)),
		]

		self.__SetProgress(0)
		#self.__SetNext(self.__LoadMap)

	def OnUpdate(self):
		if len(self.loadStepList)>0:
			(progress, runFunc)=self.loadStepList[0]

			try:
				runFunc()
			except:	
				self.errMsg.Show()
				self.loadStepList=[]

				## �̰����� syserr.txt �� ������.

				import dbg
				dbg.TraceError(" !!! Failed to load game data : STEP [%d]" % (progress))

				#import shutil
				#import os
				#shutil.copyfile("syserr.txt", "errorlog.txt")
				#os.system("errorlog.exe")

				app.Exit()

				return

			self.loadStepList.pop(0)

			self.__SetProgress(progress)

	def __InitData(self):
		playerSettingModule.LoadGameData("INIT")

	def __RegisterDungeonMapName(self):
		background.RegisterDungeonMapName("metin2_map_spinnendungeon")
		background.RegisterDungeonMapName("metin2_map_monkeydungeon")
		background.RegisterDungeonMapName("metin2_map_monkeydungeon_02")
		background.RegisterDungeonMapName("metin2_map_monkeydungeon_03")
		background.RegisterDungeonMapName("metin2_map_daemonenturm")

	def __RegisterSkill(self):

		race = net.GetMainActorRace()
		group = net.GetMainActorSkillGroup()
		empire = net.GetMainActorEmpire()

		playerSettingModule.RegisterSkill(race, group, empire)

	def __RegisterTitleName(self):
		for i in xrange(len(localeInfo.TITLE_NAME_LIST)):
			chrmgr.RegisterTitleName(i, localeInfo.TITLE_NAME_LIST[i])
			
	if app.ENABLE_REBORN_SYSTEM:			
		def __RegisterTitleRebornName(self):
			for i in xrange(len(localeInfo.TITLEREBORN_NAME_LIST)):
				chrmgr.RegisterTitleRebornName(i, localeInfo.TITLEREBORN_NAME_LIST[i])	
			
	if app.ENABLE_TITLE_SYSTEM:			
		def __RegisterTitlePrestigeName(self):
			for i in xrange(len(localeInfo.TITLEPRESTIGE_NAME_LIST)):
				chrmgr.RegisterTitlePrestigeName(i, localeInfo.TITLEPRESTIGE_NAME_LIST[i])			

	def __RegisterColor(self):

		## Name
		NAME_COLOR_DICT = {
			chrmgr.NAMECOLOR_PC : colorInfo.CHR_NAME_RGB_PC,
			chrmgr.NAMECOLOR_NPC : colorInfo.CHR_NAME_RGB_NPC,
			chrmgr.NAMECOLOR_MOB : colorInfo.CHR_NAME_RGB_MOB,
			chrmgr.NAMECOLOR_PVP : colorInfo.CHR_NAME_RGB_PVP,
			chrmgr.NAMECOLOR_PK : colorInfo.CHR_NAME_RGB_PK,
			chrmgr.NAMECOLOR_PARTY : colorInfo.CHR_NAME_RGB_PARTY,
			chrmgr.NAMECOLOR_WARP : colorInfo.CHR_NAME_RGB_WARP,
			chrmgr.NAMECOLOR_WAYPOINT : colorInfo.CHR_NAME_RGB_WAYPOINT,
			chrmgr.NAMECOLOR_METIN : colorInfo.CHR_NAME_RGB_METIN,
			chrmgr.NAMECOLOR_SHOP : colorInfo.CHR_NAME_RGB_SHOP,

			chrmgr.NAMECOLOR_EMPIRE_MOB : colorInfo.CHR_NAME_RGB_EMPIRE_MOB,
			chrmgr.NAMECOLOR_EMPIRE_NPC : colorInfo.CHR_NAME_RGB_EMPIRE_NPC,
			chrmgr.NAMECOLOR_EMPIRE_PC+1 : colorInfo.CHR_NAME_RGB_EMPIRE_PC_A,
			chrmgr.NAMECOLOR_EMPIRE_PC+2 : colorInfo.CHR_NAME_RGB_EMPIRE_PC_B,
			chrmgr.NAMECOLOR_EMPIRE_PC+3 : colorInfo.CHR_NAME_RGB_EMPIRE_PC_C,
		}
		for name, rgb in NAME_COLOR_DICT.items():
			chrmgr.RegisterNameColor(name, rgb[0], rgb[1], rgb[2])

		## Title
		TITLE_COLOR_DICT = (	
								colorInfo.TITLE_RGB_GOOD_4,
								colorInfo.TITLE_RGB_GOOD_3,
								colorInfo.TITLE_RGB_GOOD_2,
								colorInfo.TITLE_RGB_GOOD_1,
								colorInfo.TITLE_RGB_NORMAL,
								colorInfo.TITLE_RGB_EVIL_1,
								colorInfo.TITLE_RGB_EVIL_2,
								colorInfo.TITLE_RGB_EVIL_3,
								colorInfo.TITLE_RGB_EVIL_4,	)
		count = 0
		for rgb in TITLE_COLOR_DICT:
			chrmgr.RegisterTitleColor(count, rgb[0], rgb[1], rgb[2])
			count += 1
			
		# NEW TITLE SYSTEM - VEGAS
		if app.ENABLE_REBORN_SYSTEM:
			TITLEREBORN_COLOR_DICT = (colorInfo.REBORN_COLOR_1,
									colorInfo.REBORN_COLOR_2,
									colorInfo.REBORN_COLOR_3,
									colorInfo.REBORN_COLOR_NONE,)
			count_reborn_vegas = 0
			for rgb in TITLEREBORN_COLOR_DICT:
				chrmgr.RegisterTitleRebornColor(count_reborn_vegas, rgb[0], rgb[1], rgb[2])
				count_reborn_vegas += 1
			
		if app.ENABLE_TITLE_SYSTEM:
			TITLEPRESTIGE_COLOR_DICT = ( colorInfo.TITLE_PRESTIGE_COLOR_1,
									colorInfo.TITLE_PRESTIGE_COLOR_2,
									colorInfo.TITLE_PRESTIGE_COLOR_3,
									colorInfo.TITLE_PRESTIGE_COLOR_4,		
									colorInfo.TITLE_PRESTIGE_COLOR_5,
									colorInfo.TITLE_PRESTIGE_COLOR_6,
									colorInfo.TITLE_PRESTIGE_COLOR_7,
									colorInfo.TITLE_PRESTIGE_COLOR_8,
									colorInfo.TITLE_PRESTIGE_COLOR_9,
									colorInfo.TITLE_PRESTIGE_COLOR_10,
									colorInfo.TITLE_PRESTIGE_COLOR_11,
									colorInfo.TITLE_PRESTIGE_COLOR_12,
									colorInfo.TITLE_PRESTIGE_COLOR_13,
									colorInfo.TITLE_PRESTIGE_COLOR_14,
									colorInfo.TITLE_PRESTIGE_COLOR_15,
									colorInfo.TITLE_PRESTIGE_COLOR_16,
									colorInfo.TITLE_PRESTIGE_COLOR_17,
									colorInfo.TITLE_PRESTIGE_COLOR_18,
									colorInfo.TITLE_PRESTIGE_COLOR_19,
									colorInfo.TITLE_PRESTIGE_COLOR_0,)
			count_prestige_vegas = 0
			for rgb in TITLEPRESTIGE_COLOR_DICT:
				chrmgr.RegisterTitlePrestigeColor(count_prestige_vegas, rgb[0], rgb[1], rgb[2])
				count_prestige_vegas += 1	

	def __RegisterEmotionIcon(self):
		emotion.RegisterEmotionIcons()

	def __LoadMap(self):
		net.Warp(self.playerX, self.playerY)

	def __LoadSound(self):
		playerSettingModule.LoadGameData("SOUND")

	def __LoadEffect(self):
		playerSettingModule.LoadGameData("EFFECT")

	def __LoadWarrior(self):
		playerSettingModule.LoadGameData("WARRIOR")

	def __LoadAssassin(self):
		playerSettingModule.LoadGameData("ASSASSIN")

	def __LoadSura(self):
		playerSettingModule.LoadGameData("SURA")

	def __LoadShaman(self):
		playerSettingModule.LoadGameData("SHAMAN")

	def __LoadSkill(self):
		playerSettingModule.LoadGameData("SKILL")

	def __LoadEnemy(self):
		playerSettingModule.LoadGameData("ENEMY")

	def __LoadNPC(self):
		playerSettingModule.LoadGameData("NPC")

	# GUILD_BUILDING
	def __LoadGuildBuilding(self):
		playerSettingModule.LoadGuildBuildingList(localeInfo.GUILD_BUILDING_LIST_TXT)
	# END_OF_GUILD_BUILDING

	def __StartGame(self):
		background.SetViewDistanceSet(background.DISTANCE0, 25600)
		"""
		background.SetViewDistanceSet(background.DISTANCE1, 19200)
		background.SetViewDistanceSet(background.DISTANCE2, 12800)
		background.SetViewDistanceSet(background.DISTANCE3, 9600)
		background.SetViewDistanceSet(background.DISTANCE4, 6400)
		"""
		background.SelectViewDistanceNum(background.DISTANCE0)

		app.SetGlobalCenterPosition(self.playerX, self.playerY)

		net.StartGame()
