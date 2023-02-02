import os
import app
import dbg
import grp
import item
import background
import chr
import chrmgr
import player
import snd
import chat
import introLogin
import textTail
import snd
import net
import effect
import wndMgr
import fly
import systemSetting
import quest
import guild
import skill
import messenger
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import constInfo
import exchange
if app.ENABLE_RENEW_MESSENGER_WHISPER:
	import uiContact
import ime
import uisidebar
import event
if app.ENABLE_PVP_ADVANCED:
	import constInfo as pvp
	import uiCommon as message
	import uiduel
import ui
import uiCommon
import uiPhaseCurtain
import uiMapNameShower
import uiAffectShower
import uiPlayerGauge
import uiCharacter
import uiTarget
import uiSearchShop
import uiScriptLocale

# PRIVATE_SHOP_PRICE_LIST
import uiPrivateShopBuilder
# END_OF_PRIVATE_SHOP_PRICE_LIST

import mouseModule
import consoleModule
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import title_system
import playerSettingModule
import interfaceModule

import musicInfo
import debugInfo
import stringCommander
import time
import uiitemshop_v2
import uireward
from uiToolTip import ItemToolTip

if app.ENABLE_NEW_PET_SYSTEM:
	import uiPetsystem
	
from _weakref import proxy

import uitalenttree_v1
import talenttree

import uiRainSystem
import cfg
import uiSkyBoxChanger

if constInfo.ENABLE_PROMOTION_CODE_SYSTEM:
	import uipromotioncode	
# TEXTTAIL_LIVINGTIME_CONTROL
#if localeInfo.IsJAPAN():
#	app.SetTextTailLivingTime(8.0)
# END_OF_TEXTTAIL_LIVINGTIME_CONTROL

# SCREENSHOT_CWDSAVE
SCREENSHOT_CWDSAVE = FALSE
SCREENSHOT_DIR = None

if localeInfo.IsEUROPE():
	SCREENSHOT_CWDSAVE = TRUE

if localeInfo.IsCIBN10():
	SCREENSHOT_CWDSAVE = FALSE
	SCREENSHOT_DIR = "YT2W"

cameraDistance = 1550.0
cameraPitch = 27.0
cameraRotation = 0.0
cameraHeight = 100.0

testAlignment = 0

class GameWindow(ui.ScriptWindow):
	def __init__(self, stream):
		ui.ScriptWindow.__init__(self, "GAME")
		self.SetWindowName("game")
		net.SetPhaseWindow(net.PHASE_WINDOW_GAME, self)
		player.SetGameWindow(self)
		
		self.quickSlotPageIndex = 0
		self.lastPKModeSendedTime = 0
		self.pressNumber = None
		self.lastm2bob = 0

		self.guildWarQuestionDialog = None
		self.interface = None
		self.targetBoard = None
		self.console = None
		self.mapNameShower = None
		self.affectShower = None
		self.playerGauge = None
		self.wndPickupFilter = None
		self.loopList = []

		self.stream=stream
		self.interface = interfaceModule.Interface()
		constInfo.SetGameInstance(self)
		constInfo.SetInterfaceInstance(self.interface)
		if hasattr(app, "ENABLE_DUNGEON_COOL_TIME"):
			self.interface.SetGameInstance(self)
			interfaceModule.SetInstance(self.interface)
		self.interface.MakeInterface()
		self.interface.ShowDefaultWindows()

		self.curtain = uiPhaseCurtain.PhaseCurtain()
		self.curtain.speed = 0.03
		self.curtain.Hide()

		self.targetBoard = uiTarget.TargetBoard()
		self.targetBoard.SetWhisperEvent(ui.__mem_func__(self.interface.OpenWhisperDialog))
		self.targetBoard.Hide()
		
		if app.ENABLE_NEW_PET_SYSTEM:
			self.petInterface = uiPetsystem.PetSystemMain()
			self.petInterfaceMini = uiPetsystem.PetSystemMini()
		
		if app.ENABLE_TITLE_SYSTEM:
			import title_system
			self.wndTitleSystem = title_system.Title_System()
			
		self.console = consoleModule.ConsoleWindow()
		self.console.BindGameClass(self)
		self.console.SetConsoleSize(wndMgr.GetScreenWidth(), 200)
		self.console.Hide()

		self.mapNameShower = uiMapNameShower.MapNameShower()
		self.affectShower = uiAffectShower.AffectShower()
		
		if app.ENABLE_REBORN_SYSTEM:
			import uiReborn
			self.wndReborn = uiReborn.RebornClass()

		if constInfo.ENABLE_PROMOTION_CODE_SYSTEM:
			self.wndPromotioncode = uipromotioncode.PromotionCodeWindow()
		
		if app.ENABLE_PVP_ADVANCED:
			self.wndDuelGui = uiduel.Initializate()
			self.wndDuelLive = uiduel.WindowLiveInformations()
		
		import uimaintenance
		self.wndMaintenance = uimaintenance.MaintenanceClass()

		self.playerGauge = uiPlayerGauge.PlayerGauge(self)
		self.playerGauge.Hide()
		
		#wj 2014.1.2. ESC키를 누를 시 우선적으로 DropQuestionDialog를 끄도록 만들었다. 하지만 처음에 itemDropQuestionDialog가 선언되어 있지 않아 ERROR가 발생하여 init에서 선언과 동시에 초기화 시킴.
		self.itemDropQuestionDialog = None

		self.__SetQuickSlotMode()

		self.__ServerCommand_Build()
		self.__ProcessPreservedServerCommand()

		self.wndSkyboxWindow = uiSkyBoxChanger.SkyBoxChanger()
		
		self.sideBar = uisidebar.SideBar()
		self.sideBar.AddButton("Change Channel", self.__switch_channel)
		self.sideBar.AddButton("Titel - System", self.OpenTitleSystem)
		self.sideBar.AddButton("Skybox", self.OpenSkyboxWindow)
		self.sideBar.AddButton("Anti-EXP",self.__toggleAntiexp)
		self.sideBar.AddButton("Storage",self.__toggleStorage)
		self.sideBar.AddButton("Ingame Wiki",self.ToggleWikiWindow)
		self.sideBar.AddButton("Multifarmblock",self.OpenFarmBlock)
		self.sideBar.AddButton("PickupFilter",self.OpenPickupFilter)
		self.sideBar.AddButton("Prestige",self.SetReborn)
		self.sideBar.Show()
		
		## RAINING_SYSTEM
		#constInfo.ENVIRONMENT_CYCLE_ID = 0 # reset skybox id on every login
		#self.__MakeRain()
		## END_OF_RAINING_SYSTEM
		
		self.uiNewShopCreate = None
		self.uiNewShop = None
		self.uiSearchShop=uiSearchShop.ShopSearch()
		self.uiSearchShop.SetPosition(100,100)
		self.uiSearchShop.AddFlag('movable')
		self.uiSearchShop.AddFlag('float')
		self.uiSearchShop.Close()

		skybox_path = cfg.Get(cfg.SAVE_OPTION, "skybox_path", "0")
		if skybox_path and not skybox_path == "":
			background.RegisterEnvironmentData(1, skybox_path)
			background.SetEnvironmentData(1)
		else:
			background.SetEnvironmentData(0)	
			
	def __del__(self):
		player.SetGameWindow(0)
		net.ClearPhaseWindow(net.PHASE_WINDOW_GAME, self)
		ui.ScriptWindow.__del__(self)
		
	# def __wapi(self):
		# event.QuestButtonClick(81)
		
	def OpenSkyboxWindow(self):
		if self.wndSkyboxWindow.IsShow():
			self.wndSkyboxWindow.Hide()
		else:
			self.wndSkyboxWindow.Show()	
		
	def OpenPickupFilter(self):
		if not self.wndPickupFilter:
			import uiPickupFilter
			self.wndPickupFilter = uiPickupFilter.PickupFilterDialog()
		
		if self.wndPickupFilter.IsShow():
			self.wndPickupFilter.Hide()
		else:
			self.wndPickupFilter.Show()
			
	if app.INGAME_WIKI:
		def ToggleWikiWindow(self):
			if not self.wndWiki:
				return
			
			if self.wndWiki.IsShow():
				self.wndWiki.Hide()
			else:
				self.wndWiki.Show()
				self.wndWiki.SetTop()
		
		
	def __regi(self):
		event.QuestButtonClick(2)
			
			
	def OnClickSearch(self):
		if not self.uiSearchShop.IsShow():
			self.uiSearchShop.Show()
			self.uiSearchShop.SetCenterPosition()
		else:
			self.uiSearchShop.Hide()
		
	def Open(self):
		self.LoadingBar = uiitemshop_v2.LoadingBar()
		self.LoadingBar.Open()
		self.LoadingBar.SetPercent(100)
		app.SetFrameSkip(1)

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())

		self.quickSlotPageIndex = 0
		self.PickingCharacterIndex = -1
		self.PickingItemIndex = -1
		self.consoleEnable = FALSE
		self.isShowDebugInfo = FALSE
		self.ShowNameFlag = FALSE

		self.enableXMasBoom = FALSE
		self.startTimeXMasBoom = 0.0
		self.indexXMasBoom = 0

		global cameraDistance, cameraPitch, cameraRotation, cameraHeight

		app.SetCamera(cameraDistance, cameraPitch, cameraRotation, cameraHeight)

		constInfo.SET_DEFAULT_CAMERA_MAX_DISTANCE()
		constInfo.SET_DEFAULT_CHRNAME_COLOR()
		constInfo.SET_DEFAULT_FOG_LEVEL()
		constInfo.SET_DEFAULT_CONVERT_EMPIRE_LANGUAGE_ENABLE()
		constInfo.SET_DEFAULT_USE_ITEM_WEAPON_TABLE_ATTACK_BONUS()
		constInfo.SET_DEFAULT_USE_SKILL_EFFECT_ENABLE()

		# TWO_HANDED_WEAPON_ATTACK_SPEED_UP
		constInfo.SET_TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE()
		# END_OF_TWO_HANDED_WEAPON_ATTACK_SPEED_UP

		import event
		event.SetLeftTimeString(localeInfo.UI_LEFT_TIME)

		textTail.EnablePKTitle(constInfo.PVPMODE_ENABLE)

		if constInfo.PVPMODE_TEST_ENABLE:
			self.testPKMode = ui.TextLine()
			self.testPKMode.SetFontName(localeInfo.UI_DEF_FONT)
			self.testPKMode.SetPosition(0, 15)
			self.testPKMode.SetWindowHorizontalAlignCenter()
			self.testPKMode.SetHorizontalAlignCenter()
			self.testPKMode.SetFeather()
			self.testPKMode.SetOutline()
			self.testPKMode.Show()

			self.testAlignment = ui.TextLine()
			self.testAlignment.SetFontName(localeInfo.UI_DEF_FONT)
			self.testAlignment.SetPosition(0, 35)
			self.testAlignment.SetWindowHorizontalAlignCenter()
			self.testAlignment.SetHorizontalAlignCenter()
			self.testAlignment.SetFeather()
			self.testAlignment.SetOutline()
			self.testAlignment.Show()

		self.__BuildKeyDict()
		self.__BuildDebugInfo()

		# PRIVATE_SHOP_PRICE_LIST
		uiPrivateShopBuilder.Clear()
		# END_OF_PRIVATE_SHOP_PRICE_LIST

		# UNKNOWN_UPDATE
		exchange.InitTrading()
		# END_OF_UNKNOWN_UPDATE

		if debugInfo.IsDebugMode():
			self.ToggleDebugInfo()

		self.ToggleFPSInfo()

		## Sound
		snd.SetMusicVolume(systemSetting.GetMusicVolume()*net.GetFieldMusicVolume())
		snd.SetSoundVolume(systemSetting.GetSoundVolume())

		netFieldMusicFileName = net.GetFieldMusicFileName()
		if netFieldMusicFileName:
			snd.FadeInMusic("BGM/" + netFieldMusicFileName)
		elif musicInfo.fieldMusic != "":						
			snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

		self.__SetQuickSlotMode()
		self.__SelectQuickPage(self.quickSlotPageIndex)

		self.SetFocus()
		self.Show()
		app.ShowCursor()

		net.SendEnterGamePacket()

		# START_GAME_ERROR_EXIT
		try:
			self.StartGame()
		except:
			import exception
			exception.Abort("GameWindow.Open")
		# END_OF_START_GAME_ERROR_EXIT
		
		# NPC가 큐브시스템으로 만들 수 있는 아이템들의 목록을 캐싱
		# ex) cubeInformation[20383] = [ {"rewordVNUM": 72723, "rewordCount": 1, "materialInfo": "101,1&102,2", "price": 999 }, ... ]
		self.cubeInformation = {}
		self.currentCubeNPC = 0
		if app.INGAME_WIKI:
			import inGameWiki
			self.wndWiki = inGameWiki.InGameWiki()
			self.interface.dlgSystem.wikiWnd = proxy(self.wndWiki)

		import uiNewShop
		self.uiNewShop = uiNewShop.ShopDialog()
		self.uiNewShop.Close()
		self.uiNewShopCreate = uiNewShop.ShopDialogCreate()
		self.uiNewShopCreate.Hide()

	def Close(self):
		self.Hide()

		global cameraDistance, cameraPitch, cameraRotation, cameraHeight
		(cameraDistance, cameraPitch, cameraRotation, cameraHeight) = app.GetCamera()

		if musicInfo.fieldMusic != "":
			snd.FadeOutMusic("BGM/"+ musicInfo.fieldMusic)

		self.onPressKeyDict = None
		self.onClickKeyDict = None
		self.loopList = []

		chat.Close()
		snd.StopAllSound()
		grp.InitScreenEffect()
		chr.Destroy()
		textTail.Clear()
		quest.Clear()
		background.Destroy()
		guild.Destroy()
		messenger.Destroy()
		skill.ClearSkillData()
		wndMgr.Unlock()
		mouseModule.mouseController.DeattachObject()

		if self.guildWarQuestionDialog:
			self.guildWarQuestionDialog.Close()
			
		if self.uiSearchShop:
			self.uiSearchShop.Close()
			self.uiSearchShop=0

		self.guildNameBoard = None
		self.partyRequestQuestionDialog = None
		self.partyInviteQuestionDialog = None
		self.guildInviteQuestionDialog = None
		self.guildWarQuestionDialog = None
		self.messengerAddFriendQuestion = None
		if app.INGAME_WIKI:
			if self.wndWiki:
				self.wndWiki.Hide()
				self.wndWiki = None

		# UNKNOWN_UPDATE
		self.itemDropQuestionDialog = None
		# END_OF_UNKNOWN_UPDATE

		# QUEST_CONFIRM
		self.confirmDialog = None
		# END_OF_QUEST_CONFIRM

		self.PrintCoord = None
		self.FrameRate = None
		self.Pitch = None
		self.Splat = None
		self.TextureNum = None
		self.ObjectNum = None
		self.ViewDistance = None
		self.PrintMousePos = None

		self.ClearDictionary()
		if app.ENABLE_NEW_PET_SYSTEM:
			self.petInterface.Close()
			self.petInterfaceMini.Close()

		self.playerGauge = None
		self.mapNameShower = None
		self.affectShower = None

		if self.console:
			self.console.BindGameClass(0)
			self.console.Close()
			self.console=None
			
		if app.ENABLE_PVP_ADVANCED:
			if self.wndDuelLive.IsShow():
				self.wndDuelLive.Hide()
			
		if self.wndMaintenance.IsShow():
			self.wndMaintenance.Hide()
		
		if self.targetBoard:
			self.targetBoard.Destroy()
			self.targetBoard = None
			
		if app.ENABLE_REBORN_SYSTEM:			
			if self.wndReborn.IsShow():
				self.wndReborn.Hide()
			
		if app.ENABLE_TITLE_SYSTEM:			
			self.wndTitleSystem.Close()
			
		if self.interface:
			self.interface.HideAllWindows()
			self.interface.Close()
			self.interface=None
			
		if hasattr(app, "ENABLE_DUNGEON_COOL_TIME"):
			interfaceModule.SetInstance(None)

		player.ClearSkillDict()
		player.ResetCameraRotation()

		self.KillFocus()
		constInfo.SetInterfaceInstance(None)
		constInfo.SetGameInstance(None)
		app.HideCursor()

		self.uiNewShop.Hide()
		self.uiNewShopCreate.Hide()
		uiPrivateShopBuilder.Clear()
		
		self.sideBar.Destroy()
		self.sideBar = None
		print "---------------------------------------------------------------------------- CLOSE GAME WINDOW"

	def __BuildKeyDict(self):
		onPressKeyDict = {}

		##PressKey 는 누르고 있는 동안 계속 적용되는 키이다.
		
		## 숫자 단축키 퀵슬롯에 이용된다.(이후 숫자들도 퀵 슬롯용 예약)
		## F12 는 클라 디버그용 키이므로 쓰지 않는 게 좋다.
		onPressKeyDict[app.DIK_1]	= lambda : self.__PressNumKey(1)
		onPressKeyDict[app.DIK_2]	= lambda : self.__PressNumKey(2)
		onPressKeyDict[app.DIK_3]	= lambda : self.__PressNumKey(3)
		onPressKeyDict[app.DIK_4]	= lambda : self.__PressNumKey(4)
		onPressKeyDict[app.DIK_5]	= lambda : self.__PressNumKey(5)
		onPressKeyDict[app.DIK_6]	= lambda : self.__PressNumKey(6)
		onPressKeyDict[app.DIK_7]	= lambda : self.__PressNumKey(7)
		onPressKeyDict[app.DIK_8]	= lambda : self.__PressNumKey(8)
		onPressKeyDict[app.DIK_9]	= lambda : self.__PressNumKey(9)
		onPressKeyDict[app.DIK_F1]	= lambda : self.__PressQuickSlot(4)
		onPressKeyDict[app.DIK_F2]	= lambda : self.__PressQuickSlot(5)
		onPressKeyDict[app.DIK_F3]	= lambda : self.__PressQuickSlot(6)
		onPressKeyDict[app.DIK_F4]	= lambda : self.__PressQuickSlot(7)
		if app.ENABLE_WHEEL_OF_FORTUNE:
			onPressKeyDict[app.DIK_F12]	= lambda : net.SendChatPacket("/wheel_of_fortune open")
		onPressKeyDict[app.DIK_F5]	= lambda : self.__nopickInfo()
		if app.ENABLE_SWITCHBOT:
			onPressKeyDict[app.DIK_F6]	= lambda : self.interface.ToggleSwitchbotWindow()
		onPressKeyDict[app.DIK_F7]	= lambda : self.__OpenNewTestWindow()
		if app.ENABLE_EXTENDED_BATTLE_PASS:
			onPressKeyDict[app.DIK_F8] 		= lambda: self.interface.ToggleBattlePassExtended()
		if app.ENABLE_SHOP_SEARCH_SYSTEM:
			onPressKeyDict[app.DIK_F9] = lambda : self.interface.OpenPrivateShopSearch(1)
			onPressKeyDict[app.DIK_F10] = lambda : self.__ToggleTeleportPanel()
		onPressKeyDict[app.DIK_F11]	= lambda : self.OpenPromotionCodeSystem()		
			

		onPressKeyDict[app.DIK_LALT]		= lambda : self.ShowName()
		onPressKeyDict[app.DIK_LCONTROL]	= lambda : self.ShowMouseImage()
		onPressKeyDict[app.DIK_SYSRQ]		= lambda : self.SaveScreen()
		onPressKeyDict[app.DIK_SPACE]		= lambda : self.StartAttack()

		#캐릭터 이동키
		onPressKeyDict[app.DIK_UP]			= lambda : self.MoveUp()
		onPressKeyDict[app.DIK_DOWN]		= lambda : self.MoveDown()
		onPressKeyDict[app.DIK_LEFT]		= lambda : self.MoveLeft()
		onPressKeyDict[app.DIK_RIGHT]		= lambda : self.MoveRight()
		onPressKeyDict[app.DIK_W]			= lambda : self.MoveUp()
		onPressKeyDict[app.DIK_S]			= lambda : self.MoveDown()
		onPressKeyDict[app.DIK_A]			= lambda : self.MoveLeft()
		onPressKeyDict[app.DIK_D]			= lambda : self.MoveRight()

		onPressKeyDict[app.DIK_E]			= lambda: app.RotateCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_R]			= lambda: app.ZoomCamera(app.CAMERA_TO_NEGATIVE)
		#onPressKeyDict[app.DIK_F]			= lambda: app.ZoomCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_T]			= lambda: app.PitchCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_G]			= self.__PressGKey
		onPressKeyDict[app.DIK_Q]			= self.__PressQKey

		onPressKeyDict[app.DIK_NUMPAD9]		= lambda: app.MovieResetCamera()
		onPressKeyDict[app.DIK_NUMPAD4]		= lambda: app.MovieRotateCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_NUMPAD6]		= lambda: app.MovieRotateCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_PGUP]		= lambda: app.MovieZoomCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_PGDN]		= lambda: app.MovieZoomCamera(app.CAMERA_TO_POSITIVE)
		onPressKeyDict[app.DIK_NUMPAD8]		= lambda: app.MoviePitchCamera(app.CAMERA_TO_NEGATIVE)
		onPressKeyDict[app.DIK_NUMPAD2]		= lambda: app.MoviePitchCamera(app.CAMERA_TO_POSITIVE)
		if app.ENABLE_PICKUP_FILTER:
			onPressKeyDict[app.DIK_GRAVE]		= lambda : self.PickUpFilteredItem()
			onPressKeyDict[app.DIK_Z]			= lambda : self.PickUpFilteredItem()
		else:
			onPressKeyDict[app.DIK_GRAVE]		= lambda : self.PickUpItem()
			onPressKeyDict[app.DIK_Z]			= lambda : self.PickUpItem()
		onPressKeyDict[app.DIK_C]			= lambda state = 0: self.interface.ToggleCharacterWindow(state)
		onPressKeyDict[app.DIK_V]			= lambda state = 3: self.interface.ToggleCharacterWindow(state)
		onPressKeyDict[app.DIK_N]			= lambda state = 5: self.interface.ToggleCharacterWindow(state)
		onPressKeyDict[app.DIK_I]			= lambda : self.interface.ToggleInventoryWindow()
		onPressKeyDict[app.DIK_O]			= lambda : self.interface.ToggleDragonSoulWindowWithNoInfo()
		onPressKeyDict[app.DIK_M]			= lambda : self.interface.PressMKey()
		#onPressKeyDict[app.DIK_H]			= lambda : self.interface.OpenHelpWindow()
		onPressKeyDict[app.DIK_ADD]			= lambda : self.interface.MiniMapScaleUp()
		onPressKeyDict[app.DIK_SUBTRACT]	= lambda : self.interface.MiniMapScaleDown()
		onPressKeyDict[app.DIK_L]			= lambda : self.interface.ToggleChatLogWindow()
		onPressKeyDict[app.DIK_COMMA]		= lambda : self.ShowConsole()		# "`" key
		onPressKeyDict[app.DIK_LSHIFT]		= lambda : self.__SetQuickPageMode()

		onPressKeyDict[app.DIK_J]			= lambda : self.__PressJKey()
		onPressKeyDict[app.DIK_H]			= lambda : self.__PressHKey()
		onPressKeyDict[app.DIK_B]			= lambda : self.__PressBKey()
		onPressKeyDict[app.DIK_F]			= lambda : self.__PressFKey()
		if app.ENABLE_NEW_PET_SYSTEM:
			onPressKeyDict[app.DIK_P] 		= lambda: self.interface.TogglePetMain()

		# CUBE_TEST
		#onPressKeyDict[app.DIK_K]			= lambda : self.interface.OpenCubeWindow()
		# CUBE_TEST_END

		self.onPressKeyDict = onPressKeyDict

		onClickKeyDict = {}
		onClickKeyDict[app.DIK_UP] = lambda : self.StopUp()
		onClickKeyDict[app.DIK_DOWN] = lambda : self.StopDown()
		onClickKeyDict[app.DIK_LEFT] = lambda : self.StopLeft()
		onClickKeyDict[app.DIK_RIGHT] = lambda : self.StopRight()
		onClickKeyDict[app.DIK_SPACE] = lambda : self.EndAttack()

		onClickKeyDict[app.DIK_W] = lambda : self.StopUp()
		onClickKeyDict[app.DIK_S] = lambda : self.StopDown()
		onClickKeyDict[app.DIK_A] = lambda : self.StopLeft()
		onClickKeyDict[app.DIK_D] = lambda : self.StopRight()
		onClickKeyDict[app.DIK_Q] = lambda: app.RotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_E] = lambda: app.RotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_R] = lambda: app.ZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_F] = lambda: app.ZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_T] = lambda: app.PitchCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_G] = lambda: self.__ReleaseGKey()
		onClickKeyDict[app.DIK_NUMPAD4] = lambda: app.MovieRotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_NUMPAD6] = lambda: app.MovieRotateCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_PGUP] = lambda: app.MovieZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_PGDN] = lambda: app.MovieZoomCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_NUMPAD8] = lambda: app.MoviePitchCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_NUMPAD2] = lambda: app.MoviePitchCamera(app.CAMERA_STOP)
		onClickKeyDict[app.DIK_LALT] = lambda: self.HideName()
		onClickKeyDict[app.DIK_LCONTROL] = lambda: self.HideMouseImage()
		onClickKeyDict[app.DIK_LSHIFT] = lambda: self.__SetQuickSlotMode()

		#if constInfo.PVPMODE_ACCELKEY_ENABLE:
		#	onClickKeyDict[app.DIK_B] = lambda: self.ChangePKMode()

		self.onClickKeyDict=onClickKeyDict

	def __PressNumKey(self,num):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			
			if num >= 1 and num <= 9:
				if(chrmgr.IsPossibleEmoticon(-1)):				
					chrmgr.SetEmoticon(-1,int(num)-1)
					net.SendEmoticon(int(num)-1)
		else:
			if num >= 1 and num <= 4:
				self.pressNumber(num-1)

	def __ClickBKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			return
		else:
			if constInfo.PVPMODE_ACCELKEY_ENABLE:
				self.ChangePKMode()


	def	__PressJKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			if player.IsMountingHorse():
				net.SendChatPacket("/unmount")
			else:
				#net.SendChatPacket("/user_horse_ride")
				if not uiPrivateShopBuilder.IsBuildingPrivateShop():
					for i in xrange(player.INVENTORY_PAGE_SIZE):
						if player.GetItemIndex(i) in (71114, 71116, 71118, 71120):
							net.SendItemUsePacket(i)
							break
	def	__PressHKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			net.SendChatPacket("/user_horse_ride")
		else:
			self.interface.OpenHelpWindow()

	def	__PressBKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			net.SendChatPacket("/user_horse_back")
		else:
			state = 4
			self.interface.ToggleCharacterWindow(state)

	def	__PressFKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			net.SendChatPacket("/user_horse_feed")	
		else:
			app.ZoomCamera(app.CAMERA_TO_POSITIVE)

	def __PressGKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			if player.IsMountingHorse() == FALSE:
				if not uiPrivateShopBuilder.IsBuildingPrivateShop():
					for i in xrange(player.INVENTORY_PAGE_SIZE*4):
						if player.GetItemIndex(i) in (71114, 71115, 71116, 71117, 71118, 71119, 71120, 71121, 71124, 71125, 71126, 71127, 71128, 71131, 71132, 71133, 71134, 50268, 52011, 52026, 52042, 52056, 60126, 60127, 50271, 50272, 50273, 50274, 50275, 59398, 60130, 60131, 59434, 59435, 59436, 59437, 59439, 59440, 59441, 34296, 10030, 10031, 10032, 10033, 10034, 10035, 10036, 37100, 37101, 71161, 60133, 52071, 52031, 52041, 52051):
							net.SendItemUsePacket(i)
							return
			net.SendChatPacket("/ride")
		else:
			if self.ShowNameFlag:
				self.interface.ToggleGuildWindow()
			else:
				app.PitchCamera(app.CAMERA_TO_POSITIVE)

	def	__ReleaseGKey(self):
		app.PitchCamera(app.CAMERA_STOP)
		
	if app.ENABLE_TITLE_SYSTEM:	
		def OpenTitleSystem(self):		
			self.wndTitleSystem.OpenWindow()

	def __PressQKey(self):
		if app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL):
			if 0==interfaceModule.IsQBHide:
				interfaceModule.IsQBHide = 1
				self.interface.HideAllQuestButton()
			else:
				interfaceModule.IsQBHide = 0
				self.interface.ShowAllQuestButton()
		else:
			app.RotateCamera(app.CAMERA_TO_NEGATIVE)

	def __SetQuickSlotMode(self):
		self.pressNumber=ui.__mem_func__(self.__PressQuickSlot)

	def __SetQuickPageMode(self):
		self.pressNumber=ui.__mem_func__(self.__SelectQuickPage)

	def __PressQuickSlot(self, localSlotIndex):
		if localeInfo.IsARABIC():
			if 0 <= localSlotIndex and localSlotIndex < 4:
				player.RequestUseLocalQuickSlot(3-localSlotIndex)
			else:
				player.RequestUseLocalQuickSlot(11-localSlotIndex)
		else:
			player.RequestUseLocalQuickSlot(localSlotIndex)			

	def __SelectQuickPage(self, pageIndex):
		self.quickSlotPageIndex = pageIndex
		player.SetQuickPage(pageIndex)

	def ToggleFPSInfo(self):
		self.FrameRate.Show()

	def ToggleDebugInfo(self):
		self.isShowDebugInfo = not self.isShowDebugInfo

		if self.isShowDebugInfo:
			self.PrintCoord.Show()
			self.FrameRate.Show()
			self.Pitch.Show()
			self.Splat.Show()
			self.TextureNum.Show()
			self.ObjectNum.Show()
			self.ViewDistance.Show()
			self.PrintMousePos.Show()
		else:
			self.PrintCoord.Hide()
			self.FrameRate.Hide()
			self.Pitch.Hide()
			self.Splat.Hide()
			self.TextureNum.Hide()
			self.ObjectNum.Hide()
			self.ViewDistance.Hide()
			self.PrintMousePos.Hide()

	def __BuildFPSInfo(self):
		## Frame Rate
		self.FrameRate = ui.TextLine()
		self.FrameRate.SetFontName(localeInfo.UI_DEF_FONT)
		self.FrameRate.SetPosition(wndMgr.GetScreenWidth() - 200, 20)

	def __BuildDebugInfo(self):
		## Character Position Coordinate
		self.PrintCoord = ui.TextLine()
		self.PrintCoord.SetFontName(localeInfo.UI_DEF_FONT)
		self.PrintCoord.SetPosition(wndMgr.GetScreenWidth() - 270, 0)
		
		## Frame Rate
		self.FrameRate = ui.TextLine()
		self.FrameRate.SetFontName(localeInfo.UI_DEF_FONT)
		self.FrameRate.SetPosition(wndMgr.GetScreenWidth() - 270, 20)

		## Camera Pitch
		self.Pitch = ui.TextLine()
		self.Pitch.SetFontName(localeInfo.UI_DEF_FONT)
		self.Pitch.SetPosition(wndMgr.GetScreenWidth() - 270, 40)

		## Splat
		self.Splat = ui.TextLine()
		self.Splat.SetFontName(localeInfo.UI_DEF_FONT)
		self.Splat.SetPosition(wndMgr.GetScreenWidth() - 270, 60)
		
		##
		self.PrintMousePos = ui.TextLine()
		self.PrintMousePos.SetFontName(localeInfo.UI_DEF_FONT)
		self.PrintMousePos.SetPosition(wndMgr.GetScreenWidth() - 270, 80)

		# TextureNum
		self.TextureNum = ui.TextLine()
		self.TextureNum.SetFontName(localeInfo.UI_DEF_FONT)
		self.TextureNum.SetPosition(wndMgr.GetScreenWidth() - 270, 100)

		# 오브젝트 그리는 개수
		self.ObjectNum = ui.TextLine()
		self.ObjectNum.SetFontName(localeInfo.UI_DEF_FONT)
		self.ObjectNum.SetPosition(wndMgr.GetScreenWidth() - 270, 120)

		# 시야거리
		self.ViewDistance = ui.TextLine()
		self.ViewDistance.SetFontName(localeInfo.UI_DEF_FONT)
		self.ViewDistance.SetPosition(0, 0)

	def __NotifyError(self, msg):
		chat.AppendChat(chat.CHAT_TYPE_INFO, msg)

	def ChangePKMode(self):

		if not app.IsPressed(app.DIK_LCONTROL):
			return

		if player.GetStatus(player.LEVEL)<constInfo.PVPMODE_PROTECTED_LEVEL:
			self.__NotifyError(localeInfo.OPTION_PVPMODE_PROTECT % (constInfo.PVPMODE_PROTECTED_LEVEL))
			return

		curTime = app.GetTime()
		if curTime - self.lastPKModeSendedTime < constInfo.PVPMODE_ACCELKEY_DELAY:
			return

		self.lastPKModeSendedTime = curTime

		curPKMode = player.GetPKMode()
		nextPKMode = curPKMode + 1
		if nextPKMode == player.PK_MODE_PROTECT:
			if 0 == player.GetGuildID():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_CANNOT_SET_GUILD_MODE)
				nextPKMode = 0
			else:
				nextPKMode = player.PK_MODE_GUILD

		elif nextPKMode == player.PK_MODE_MAX_NUM:
			nextPKMode = 0

		net.SendChatPacket("/PKMode " + str(nextPKMode))
		print "/PKMode " + str(nextPKMode)

	def OnChangePKMode(self):

		self.interface.OnChangePKMode()

		try:
			self.__NotifyError(localeInfo.OPTION_PVPMODE_MESSAGE_DICT[player.GetPKMode()])
		except KeyError:
			print "UNKNOWN PVPMode[%d]" % (player.GetPKMode())

		if constInfo.PVPMODE_TEST_ENABLE:
			curPKMode = player.GetPKMode()
			alignment, grade = chr.testGetPKData()
			self.pkModeNameDict = { 0 : "PEACE", 1 : "REVENGE", 2 : "FREE", 3 : "PROTECT", }
			self.testPKMode.SetText("Current PK Mode : " + self.pkModeNameDict.get(curPKMode, "UNKNOWN"))
			self.testAlignment.SetText("Current Alignment : " + str(alignment) + " (" + localeInfo.TITLE_NAME_LIST[grade] + ")")

	###############################################################################################
	###############################################################################################
	## Game Callback Functions

	# Start
	def StartGame(self):
		self.RefreshInventory()
		self.RefreshEquipment()
		self.RefreshCharacter()
		self.RefreshSkill()

	# Refresh
	def CheckGameButton(self):
		if self.interface:
			self.interface.CheckGameButton()

	def RefreshAlignment(self):
		self.interface.RefreshAlignment()

	def RefreshStatus(self):
		self.CheckGameButton()

		if self.interface:
			self.interface.RefreshStatus()

		if self.playerGauge:
			self.playerGauge.RefreshGauge()

	def RefreshStamina(self):
		self.interface.RefreshStamina()

	def RefreshSkill(self):
		self.CheckGameButton()
		if self.interface:
			self.interface.RefreshSkill()

	def RefreshQuest(self):
		self.interface.RefreshQuest()

	def RefreshMessenger(self):
		self.interface.RefreshMessenger()

	def RefreshGuildInfoPage(self):
		self.interface.RefreshGuildInfoPage()

	def RefreshGuildBoardPage(self):
		self.interface.RefreshGuildBoardPage()

	def RefreshGuildMemberPage(self):
		self.interface.RefreshGuildMemberPage()

	def RefreshGuildMemberPageGradeComboBox(self):
		self.interface.RefreshGuildMemberPageGradeComboBox()

	def RefreshGuildSkillPage(self):
		self.interface.RefreshGuildSkillPage()

	def RefreshGuildGradePage(self):
		self.interface.RefreshGuildGradePage()

	def RefreshMobile(self):
		if self.interface:
			self.interface.RefreshMobile()

	def OnMobileAuthority(self):
		self.interface.OnMobileAuthority()

	def OnBlockMode(self, mode):
		self.interface.OnBlockMode(mode)
		
	if app.ENABLE_HIDE_COSTUME_SYSTEM:
		def SetBodyCostumeHidden(self, hidden):
			constInfo.HIDDEN_BODY_COSTUME = int(hidden)
			self.interface.RefreshVisibleCostume()

		def SetHairCostumeHidden(self, hidden):
			constInfo.HIDDEN_HAIR_COSTUME = int(hidden)
			self.interface.RefreshVisibleCostume()

		def SetSashCostumeHidden(self, hidden):
			if app.ENABLE_SASH_SYSTEM:
				constInfo.HIDDEN_SASH_COSTUME = int(hidden)
				self.interface.RefreshVisibleCostume()
			else:
				pass

		def SetWeaponCostumeHidden(self, hidden):
			if app.ENABLE_COSTUME_WEAPON_SYSTEM:
				constInfo.HIDDEN_WEAPON_COSTUME = int(hidden)
				self.interface.RefreshVisibleCostume()
			else:
				pass

	def OpenQuestWindow(self, skin, idx):
		if constInfo.INPUT_IGNORE:
			return
		self.interface.OpenQuestWindow(skin, idx)

	def AskGuildName(self):

		guildNameBoard = uiCommon.InputDialog()
		guildNameBoard.SetTitle(localeInfo.GUILD_NAME)
		guildNameBoard.SetAcceptEvent(ui.__mem_func__(self.ConfirmGuildName))
		guildNameBoard.SetCancelEvent(ui.__mem_func__(self.CancelGuildName))
		guildNameBoard.Open()

		self.guildNameBoard = guildNameBoard

	def ConfirmGuildName(self):
		guildName = self.guildNameBoard.GetText()
		if not guildName:
			return

		if net.IsInsultIn(guildName):
			self.PopupMessage(localeInfo.GUILD_CREATE_ERROR_INSULT_NAME)
			return

		net.SendAnswerMakeGuildPacket(guildName)
		self.guildNameBoard.Close()
		self.guildNameBoard = None
		return TRUE

	def CancelGuildName(self):
		self.guildNameBoard.Close()
		self.guildNameBoard = None
		return TRUE

	## Refine
	def PopupMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, 0, localeInfo.UI_OK)

	def OpenRefineDialog(self, targetItemPos, nextGradeItemVnum, cost, prob, type=0):
		self.interface.OpenRefineDialog(targetItemPos, nextGradeItemVnum, cost, prob, type)

	def AppendMaterialToRefineDialog(self, vnum, count):
		self.interface.AppendMaterialToRefineDialog(vnum, count)

	def RunUseSkillEvent(self, slotIndex, coolTime):
		self.interface.OnUseSkill(slotIndex, coolTime)

	def ClearAffects(self):
		self.affectShower.ClearAffects()

	def SetAffect(self, affect):
		self.affectShower.SetAffect(affect)

	def ResetAffect(self, affect):
		self.affectShower.ResetAffect(affect)

	# UNKNOWN_UPDATE
	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		self.affectShower.BINARY_NEW_AddAffect(type, pointIdx, value, duration)
		if chr.NEW_AFFECT_DRAGON_SOUL_DECK1 == type or chr.NEW_AFFECT_DRAGON_SOUL_DECK2 == type:
			self.interface.DragonSoulActivate(type - chr.NEW_AFFECT_DRAGON_SOUL_DECK1)
		elif chr.NEW_AFFECT_DRAGON_SOUL_QUALIFIED == type:
			self.BINARY_DragonSoulGiveQuilification()

	def BINARY_NEW_RemoveAffect(self, type, pointIdx):
		self.affectShower.BINARY_NEW_RemoveAffect(type, pointIdx)
		if chr.NEW_AFFECT_DRAGON_SOUL_DECK1 == type or chr.NEW_AFFECT_DRAGON_SOUL_DECK2 == type:
			self.interface.DragonSoulDeactivate()
	
 
 
	# END_OF_UNKNOWN_UPDATE

	def ActivateSkillSlot(self, slotIndex):
		if self.interface:
			self.interface.OnActivateSkill(slotIndex)

	def DeactivateSkillSlot(self, slotIndex):
		if self.interface:
			self.interface.OnDeactivateSkill(slotIndex)

	def RefreshEquipment(self):
		if self.interface:
			self.interface.RefreshInventory()

	def RefreshInventory(self):
		if self.interface:
			self.interface.RefreshInventory()

	def RefreshCharacter(self):
		if self.interface:
			self.interface.RefreshCharacter()

	def OnGameOver(self):
		self.CloseTargetBoard()
		self.OpenRestartDialog()

	def OpenRestartDialog(self):
		self.interface.OpenRestartDialog()

	def ChangeCurrentSkill(self, skillSlotNumber):
		self.interface.OnChangeCurrentSkill(skillSlotNumber)

	## TargetBoard
	def SetPCTargetBoard(self, vid, name):
		self.targetBoard.Open(vid, name)
		
		if app.IsPressed(app.DIK_LCONTROL):
			
			if not player.IsSameEmpire(vid):
				return

			if player.IsMainCharacterIndex(vid):
				return		
			elif chr.INSTANCE_TYPE_BUILDING == chr.GetInstanceType(vid):
				return

			self.interface.OpenWhisperDialog(name)
			

	def RefreshTargetBoardByVID(self, vid):
		self.targetBoard.RefreshByVID(vid)

	def RefreshTargetBoardByName(self, name):
		self.targetBoard.RefreshByName(name)
		
	def __RefreshTargetBoard(self):
		self.targetBoard.Refresh()
		
	if app.ENABLE_VIEW_TARGET_DECIMAL_HP:
		def SetHPTargetBoard(self, vid, hpPercentage, iMinHP, iMaxHP):
			if vid != self.targetBoard.GetTargetVID():
				self.targetBoard.ResetTargetBoard()
				self.targetBoard.SetEnemyVID(vid)
			
			self.targetBoard.SetHP(hpPercentage, iMinHP, iMaxHP)
			self.targetBoard.Show()
	else:
		def SetHPTargetBoard(self, vid, hpPercentage):
			if vid != self.targetBoard.GetTargetVID():
				self.targetBoard.ResetTargetBoard()
				self.targetBoard.SetEnemyVID(vid)
			
			self.targetBoard.SetHP(hpPercentage)
			self.targetBoard.Show()

	def CloseTargetBoardIfDifferent(self, vid):
		if vid != self.targetBoard.GetTargetVID():
			self.targetBoard.Close()

	def CloseTargetBoard(self):
		self.targetBoard.Close()

	## View Equipment
	def OpenEquipmentDialog(self, vid):
		if app.ENABLE_PVP_ADVANCED:
			pvp.DUEL_IS_SHOW_EQUIP = 0
			pvp.DUEL_SAVE_VID = (int(vid))

		self.interface.OpenEquipmentDialog(vid)

	def SetEquipmentDialogItem(self, vid, slotIndex, vnum, count):
		self.interface.SetEquipmentDialogItem(vid, slotIndex, vnum, count)

	def SetEquipmentDialogSocket(self, vid, slotIndex, socketIndex, value):
		self.interface.SetEquipmentDialogSocket(vid, slotIndex, socketIndex, value)

	def SetEquipmentDialogAttr(self, vid, slotIndex, attrIndex, type, value):
		self.interface.SetEquipmentDialogAttr(vid, slotIndex, attrIndex, type, value)
		
	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def BINARY_OpenWhisperBySearchName(self, name):
			self.interface.OpenWhisperDialog(name)

		def BINARY_Profile_OnRecvData(self, name, job, level, empire, guild, language, status, location, year, month, day):	
			self.interface.RecvWhisperProfile(name, job, level, empire, guild, language, status, location, year, month, day)
			if str(name) == str(player.GetMainCharacterName()):
				uiContact.PROFILE_DICT.update({"job":job,"status":status,"location":location,"year":year,"month":month,"day":day})
		
	if app.ENABLE_LANG_AND_EMPIRE_FLAG:
		def BINARY_SET_LANG_AND_EMPIRE_FLAG(self, name, language, empire):
			self.interface.SetInterfaceFlag(name, language, empire)

	# SHOW_LOCAL_MAP_NAME
	def ShowMapName(self, mapName, x, y):

		if self.mapNameShower:
			self.mapNameShower.ShowMapName(mapName, x, y)

		if self.interface:
			self.interface.SetMapName(mapName)
	# END_OF_SHOW_LOCAL_MAP_NAME	

	if app.ENABLE_EXTENDED_BATTLE_PASS:
		def BINARY_ExtOpenBattlePass(self):
			if self.interface:
				self.interface.ReciveOpenExtBattlePass()
			
		def BINARY_ExtBattlePassAddGeneralInfo(self, BattlePassType, BattlePassName, BattlePassID, battlePassStartTime, battlePassEndTime):
			if self.interface:
				self.interface.AddExtendedBattleGeneralInfo(BattlePassType, BattlePassName, BattlePassID, battlePassStartTime, battlePassEndTime)
				
		def BINARY_ExtBattlePassAddMission(self, battlepassType, battlepassID, missionIndex, missionType, missionInfo1, missionInfo2, missionInfo3):
			if self.interface:
				self.interface.AddExtendedBattlePassMission(battlepassType, battlepassID, missionIndex, missionType, missionInfo1, missionInfo2, missionInfo3)

		def BINARY_ExtBattlePassAddMissionReward(self, battlepassType, battlepassID, missionIndex, missionType, itemVnum, itemCount):
			if self.interface:
				self.interface.AddExtendedBattlePassMissionReward(battlepassType, battlepassID, missionIndex, missionType, itemVnum, itemCount)

		def BINARY_ExtBattlePassUpdate(self, battlepassType, missionIndex, missionType, newProgress):
			if self.interface:
				self.interface.UpdateExtendedBattlePassMission(battlepassType, missionIndex, missionType, newProgress)

		def BINARY_ExtBattlePassAddReward(self, battlepassType, battlepassID, itemVnum, itemCount):
			if self.interface:
				self.interface.AddExtendedBattlePassReward(battlepassType, battlepassID, itemVnum, itemCount)
		
		def BINARY_ExtBattlePassAddRanklistEntry(self, playername, battlepassType, battlepassID, startTime, endTime):
			if self.interface:
				self.interface.AddExtBattlePassRanklistEntry(playername, battlepassType, battlepassID, startTime, endTime)

	if app.ENABLE_ASLAN_LOTTERY:
		def BINARY_OpenLotteryWindow(self):
			self.interface.ToggleAslanLotteryWindow()
			
		def BINARY_LotterySetBaseData(self, lottoSlot, lottoNum, num1, num2, num3, num4):
			constInfo.lotto_number_infos[int(lottoSlot)]={"lotto_id" : int(lottoNum), "numbers" : [int(num1), int(num2), int(num3), int(num4)]}
		
		def BINARY_LotterySetLongLongValues(self, lottoSlot, jackpot, nextRefresh):
			if lottoSlot == 0:
				constInfo.lotto_next_refresh = nextRefresh + 1
				constInfo.lotto_jackpot = jackpot
			self.interface.RefreshLottoBasicInfo()

		def BINARY_LotterySetTicketData(self, tSlot, tID, num1, num2, num3, num4, lottoID, buytime, state, winnumbers, money):
			if int(tID) != 0:
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["ticket_id"] = int(tID)
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["ticket_numbers"] = [int(num1), int(num2), int(num3), int(num4)]
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["ticket_for_lottoid"] = int(lottoID)
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["ticket_buy_time"] = str(buytime)
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["ticket_state"] = int(state)
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["win_numbers"] = int(winnumbers)
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["ticket_win_money"] = long(money)
			else:
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["ticket_id"] = 0
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["ticket_numbers"] = [0, 0, 0, 0]
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["ticket_for_lottoid"] = 0
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["ticket_buy_time"] = ""
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["ticket_state"] = 0
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["win_numbers"] = 0
				constInfo.lotto_ticket_data["ticket_%s" % tSlot]["ticket_win_money"] = 0
			self.interface.RefreshLottoTicketInfo()

		def BINARY_LotterySetRanklistJackpotData(self, playername, lottoID, money, date):
			is_append = 0
			const_data = constInfo.lottery_ranklist_jackpot_data
			
			for i in xrange(len(const_data)):
				if const_data[i]["lottoID"] == lottoID:
					is_append = 1
					
			if is_append == 0:	
				const_data[len(const_data)]={"playername" : str(playername), "lottoID" : int(lottoID), "money" : long(money), "date" : str(date)}

		def BINARY_LotterySetRanklistMoneyData(self, playername, level, empire, money):
			is_append = 0
			const_data = constInfo.lottery_ranklist_money_data
			
			for i in xrange(len(const_data)):
				if const_data[i]["playername"] == playername:
					is_append = 1
	
			if is_append == 0:	
				const_data[len(const_data)]={"playername" : str(playername), "level" : int(level), "empire" : int(empire), "money" : long(money)}

	def BINARY_OpenAtlasWindow(self):
		self.interface.BINARY_OpenAtlasWindow()

	## Chat
	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def OnRecvWhisper(self, mode, name, line, job, level, empire, guild, language, status, location, year, month, day):
			if mode == chat.WHISPER_TYPE_GM:
				self.interface.RegisterGameMasterName(name)
			chat.AppendWhisper(mode, name, "%s %s" % (uiContact.GetWhisperSendedTime(), line))
			self.interface.RecvWhisper(name, job, level, empire, guild, language, status, location, year, month, day)
	else:
		def OnRecvWhisper(self, mode, name, line):
			if mode == chat.WHISPER_TYPE_GM:
				self.interface.RegisterGameMasterName(name)
			chat.AppendWhisper(mode, name, line)
			self.interface.RecvWhisper(name)

	def OnRecvWhisperSystemMessage(self, mode, name, line):
		chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, line)
		self.interface.RecvWhisper(name)

	def OnRecvWhisperError(self, mode, name, line):
		if localeInfo.WHISPER_ERROR.has_key(mode):
			chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, localeInfo.WHISPER_ERROR[mode](name))
		else:
			chat.AppendWhisper(chat.WHISPER_TYPE_SYSTEM, name, "Whisper Unknown Error(mode=%d, name=%s)" % (mode, name))
		self.interface.RecvWhisper(name)

	def RecvWhisper(self, name):
		self.interface.RecvWhisper(name)

	def OnPickMoney(self, money):
		if constInfo.pickInfo == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GAME_PICK_MONEY % (money))
		else:
			return

	def OnShopError(self, type):
		try:
			self.PopupMessage(localeInfo.SHOP_ERROR_DICT[type])
		except KeyError:
			self.PopupMessage(localeInfo.SHOP_ERROR_UNKNOWN % (type))

	def OnSafeBoxError(self):
		self.PopupMessage(localeInfo.SAFEBOX_ERROR)

	def OnFishingSuccess(self, isFish, fishName):
		chat.AppendChatWithDelay(chat.CHAT_TYPE_INFO, localeInfo.FISHING_SUCCESS(isFish, fishName), 2000)

	# ADD_FISHING_MESSAGE
	def OnFishingNotifyUnknown(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.FISHING_UNKNOWN)

	def OnFishingWrongPlace(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.FISHING_WRONG_PLACE)
	# END_OF_ADD_FISHING_MESSAGE

	def OnFishingNotify(self, isFish, fishName):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.FISHING_NOTIFY(isFish, fishName))

	def OnFishingFailure(self):
		chat.AppendChatWithDelay(chat.CHAT_TYPE_INFO, localeInfo.FISHING_FAILURE, 2000)

	def OnCannotPickItem(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GAME_CANNOT_PICK_ITEM)

	# MINING
	def OnCannotMining(self):
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GAME_CANNOT_MINING)
	# END_OF_MINING

	def OnCannotUseSkill(self, vid, type):
		if localeInfo.USE_SKILL_ERROR_TAIL_DICT.has_key(type):
			textTail.RegisterInfoTail(vid, localeInfo.USE_SKILL_ERROR_TAIL_DICT[type])

		if localeInfo.USE_SKILL_ERROR_CHAT_DICT.has_key(type):
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_SKILL_ERROR_CHAT_DICT[type])

	def	OnCannotShotError(self, vid, type):
		textTail.RegisterInfoTail(vid, localeInfo.SHOT_ERROR_TAIL_DICT.get(type, localeInfo.SHOT_ERROR_UNKNOWN % (type)))

	## PointReset
	def StartPointReset(self):
		self.interface.OpenPointResetDialog()

	## Shop
	def StartShop(self, vid):
		self.interface.OpenShopDialog(vid)

	def EndShop(self):
		self.interface.CloseShopDialog()

	def RefreshShop(self):
		self.interface.RefreshShopDialog()

	def SetShopSellingPrice(self, Price):
		pass

	## Exchange
	def StartExchange(self):
		self.interface.StartExchange()

	def EndExchange(self):
		self.interface.EndExchange()

	def RefreshExchange(self):
		self.interface.RefreshExchange()

	## Party
	def RecvPartyInviteQuestion(self, leaderVID, leaderName):
		partyInviteQuestionDialog = uiCommon.QuestionDialog()
		partyInviteQuestionDialog.SetText(leaderName + localeInfo.PARTY_DO_YOU_JOIN)
		partyInviteQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.AnswerPartyInvite(arg))
		partyInviteQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.AnswerPartyInvite(arg))
		partyInviteQuestionDialog.Open()
		partyInviteQuestionDialog.partyLeaderVID = leaderVID
		self.partyInviteQuestionDialog = partyInviteQuestionDialog

	def AnswerPartyInvite(self, answer):

		if not self.partyInviteQuestionDialog:
			return

		partyLeaderVID = self.partyInviteQuestionDialog.partyLeaderVID

		distance = player.GetCharacterDistance(partyLeaderVID)
		if distance < 0.0 or distance > 5000:
			answer = FALSE

		net.SendPartyInviteAnswerPacket(partyLeaderVID, answer)

		self.partyInviteQuestionDialog.Close()
		self.partyInviteQuestionDialog = None

	def AddPartyMember(self, pid, name):
		self.interface.AddPartyMember(pid, name)

	def UpdatePartyMemberInfo(self, pid):
		self.interface.UpdatePartyMemberInfo(pid)
		pass

	def RemovePartyMember(self, pid):
		self.interface.RemovePartyMember(pid)
		self.__RefreshTargetBoard()

	def LinkPartyMember(self, pid, vid):
		self.interface.LinkPartyMember(pid, vid)

	def UnlinkPartyMember(self, pid):
		self.interface.UnlinkPartyMember(pid)

	def UnlinkAllPartyMember(self):
		self.interface.UnlinkAllPartyMember()

	def ExitParty(self):
		self.interface.ExitParty()
		self.RefreshTargetBoardByVID(self.targetBoard.GetTargetVID())

	def ChangePartyParameter(self, distributionMode):
		self.interface.ChangePartyParameter(distributionMode)

	## Messenger
	def OnMessengerAddFriendQuestion(self, name):
		messengerAddFriendQuestion = uiCommon.QuestionDialog2()
		messengerAddFriendQuestion.SetText1(localeInfo.MESSENGER_DO_YOU_ACCEPT_ADD_FRIEND_1 % (name))
		messengerAddFriendQuestion.SetText2(localeInfo.MESSENGER_DO_YOU_ACCEPT_ADD_FRIEND_2)
		messengerAddFriendQuestion.SetAcceptEvent(ui.__mem_func__(self.OnAcceptAddFriend))
		messengerAddFriendQuestion.SetCancelEvent(ui.__mem_func__(self.OnDenyAddFriend))
		messengerAddFriendQuestion.Open()
		messengerAddFriendQuestion.name = name
		self.messengerAddFriendQuestion = messengerAddFriendQuestion

	def OnAcceptAddFriend(self):
		name = self.messengerAddFriendQuestion.name
		net.SendChatPacket("/messenger_auth y " + name)
		self.OnCloseAddFriendQuestionDialog()
		return TRUE

	def OnDenyAddFriend(self):
		name = self.messengerAddFriendQuestion.name
		net.SendChatPacket("/messenger_auth n " + name)
		self.OnCloseAddFriendQuestionDialog()
		return TRUE

	def OnCloseAddFriendQuestionDialog(self):
		self.messengerAddFriendQuestion.Close()
		self.messengerAddFriendQuestion = None
		return TRUE

	## SafeBox
	def OpenSafeboxWindow(self, size):
		self.interface.OpenSafeboxWindow(size)

	def RefreshSafebox(self):
		self.interface.RefreshSafebox()

	def RefreshSafeboxMoney(self):
		self.interface.RefreshSafeboxMoney()

	# ITEM_MALL
	def OpenMallWindow(self, size):
		self.interface.OpenMallWindow(size)

	def RefreshMall(self):
		self.interface.RefreshMall()
	# END_OF_ITEM_MALL

	## Guild
	def RecvGuildInviteQuestion(self, guildID, guildName):
		guildInviteQuestionDialog = uiCommon.QuestionDialog()
		guildInviteQuestionDialog.SetText(guildName + localeInfo.GUILD_DO_YOU_JOIN)
		guildInviteQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.AnswerGuildInvite(arg))
		guildInviteQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.AnswerGuildInvite(arg))
		guildInviteQuestionDialog.Open()
		guildInviteQuestionDialog.guildID = guildID
		self.guildInviteQuestionDialog = guildInviteQuestionDialog

	def AnswerGuildInvite(self, answer):

		if not self.guildInviteQuestionDialog:
			return

		guildLeaderVID = self.guildInviteQuestionDialog.guildID
		net.SendGuildInviteAnswerPacket(guildLeaderVID, answer)

		self.guildInviteQuestionDialog.Close()
		self.guildInviteQuestionDialog = None

	
	def DeleteGuild(self):
		self.interface.DeleteGuild()

	## Clock
	def ShowClock(self, second):
		self.interface.ShowClock(second)

	def HideClock(self):
		self.interface.HideClock()

	## Emotion
	def BINARY_ActEmotion(self, emotionIndex):
		if self.interface.wndCharacter:
			self.interface.wndCharacter.ActEmotion(emotionIndex)

	###############################################################################################
	###############################################################################################
	## Keyboard Functions

	def CheckFocus(self):
		if FALSE == self.IsFocus():
			if TRUE == self.interface.IsOpenChat():
				self.interface.ToggleChat()

			self.SetFocus()

	def SaveScreen(self):
		print "save screen"

		# SCREENSHOT_CWDSAVE
		if SCREENSHOT_CWDSAVE:
			if not os.path.exists(os.getcwd()+os.sep+"screenshot"):
				os.mkdir(os.getcwd()+os.sep+"screenshot")

			(succeeded, name) = grp.SaveScreenShotToPath(os.getcwd()+os.sep+"screenshot"+os.sep)
		elif SCREENSHOT_DIR:
			(succeeded, name) = grp.SaveScreenShot(SCREENSHOT_DIR)
		else:
			(succeeded, name) = grp.SaveScreenShot()
		# END_OF_SCREENSHOT_CWDSAVE

		if succeeded:
			pass
			"""
			chat.AppendChat(chat.CHAT_TYPE_INFO, name + localeInfo.SCREENSHOT_SAVE1)
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SCREENSHOT_SAVE2)
			"""
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SCREENSHOT_SAVE_FAILURE)

	def ShowConsole(self):
		if debugInfo.IsDebugMode() or TRUE == self.consoleEnable:
			player.EndKeyWalkingImmediately()
			self.console.OpenWindow()

	def ShowName(self):
		self.ShowNameFlag = TRUE
		self.playerGauge.EnableShowAlways()
		player.SetQuickPage(self.quickSlotPageIndex+1)

	# ADD_ALWAYS_SHOW_NAME
	def __IsShowName(self):

		if systemSetting.IsAlwaysShowName():
			return TRUE

		if self.ShowNameFlag:
			return TRUE

		return FALSE
	# END_OF_ADD_ALWAYS_SHOW_NAME
	
	def HideName(self):
		self.ShowNameFlag = FALSE
		self.playerGauge.DisableShowAlways()
		player.SetQuickPage(self.quickSlotPageIndex)

	def ShowMouseImage(self):
		self.interface.ShowMouseImage()

	def HideMouseImage(self):
		self.interface.HideMouseImage()

	def StartAttack(self):
		player.SetAttackKeyState(TRUE)
		
	if app.ENABLE_REBORN_SYSTEM:
		def SetReborn(self, app):
			import chat
			func_modul = str(app)
			#chat.AppendChat(chat.CHAT_TYPE_INFO, "vegas print number [%s]" % str(app))
			if func_modul == "arg1":
				self.wndReborn.OpenArgument("reborn_1")
			elif func_modul == "arg2":
				self.wndReborn.OpenArgument("reborn_2")
			elif func_modul == "arg3":
				self.wndReborn.OpenArgument("reborn_3")
			elif func_modul == "pro_1":
				self.wndReborn.OpenArgument("pro_1")
			elif func_modul == "pro_0":
				self.wndReborn.OpenArgument("pro_0")

	def EndAttack(self):
		player.SetAttackKeyState(FALSE)
		
	def BINARY_Update_Maintenance(self, iTime, iDuration, iReason):
		sTime = int(iTime)
		sDuration = int(iDuration)
		sReason = str(iReason)

		if sTime != 0 and sDuration != 0:
			self.wndMaintenance.OpenMaintenance(int(iTime), int(iDuration), str(iReason))
			

	def MoveUp(self):
		player.SetSingleDIKKeyState(app.DIK_UP, TRUE)

	def MoveDown(self):
		player.SetSingleDIKKeyState(app.DIK_DOWN, TRUE)

	def MoveLeft(self):
		player.SetSingleDIKKeyState(app.DIK_LEFT, TRUE)

	def MoveRight(self):
		player.SetSingleDIKKeyState(app.DIK_RIGHT, TRUE)

	def StopUp(self):
		player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

	def StopDown(self):
		player.SetSingleDIKKeyState(app.DIK_DOWN, FALSE)

	def StopLeft(self):
		player.SetSingleDIKKeyState(app.DIK_LEFT, FALSE)

	def StopRight(self):
		player.SetSingleDIKKeyState(app.DIK_RIGHT, FALSE)

	def PickUpItem(self):
		player.PickCloseItemVector()

	if app.ENABLE_PICKUP_FILTER:
		def PickUpFilteredItem(self):
			net.PickFilteredItem(int(cfg.Get(cfg.SAVE_OPTION, "pickup_filter_mode", "0")), int(cfg.Get(cfg.SAVE_OPTION, "pickup_filter_flag", "0")))

	###############################################################################################
	###############################################################################################
	## Event Handler

	def OnKeyDown(self, key):
		if self.interface.wndWeb and self.interface.wndWeb.IsShow():
			return

		if key == app.DIK_ESC:
			self.RequestDropItem(FALSE)
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

		try:
			self.onPressKeyDict[key]()
		except KeyError:
			pass
		except:
			raise

		return TRUE

	def OnKeyUp(self, key):
		try:
			if None == self.onClickKeyDict:
				self.__BuildKeyDict()
				return TRUE
				
			self.onClickKeyDict[key]()
		except KeyError:
			pass
		except:
			raise

		return TRUE

	def OnMouseLeftButtonDown(self):
		if self.interface.BUILD_OnMouseLeftButtonDown():
			return

		if mouseModule.mouseController.isAttached():
			self.CheckFocus()
		else:
			hyperlink = ui.GetHyperlink()
			if hyperlink:
				return
			else:
				self.CheckFocus()
				player.SetMouseState(player.MBT_LEFT, player.MBS_PRESS);

		return TRUE

	def OnMouseLeftButtonUp(self):

		if self.interface.BUILD_OnMouseLeftButtonUp():
			return

		if mouseModule.mouseController.isAttached():

			attachedType = mouseModule.mouseController.GetAttachedType()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()
			attachedItemSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()

			## QuickSlot
			if player.SLOT_TYPE_QUICK_SLOT == attachedType:
				player.RequestDeleteGlobalQuickSlot(attachedItemSlotPos)

			## Inventory
			elif player.SLOT_TYPE_INVENTORY == attachedType:

				if player.ITEM_MONEY == attachedItemIndex:
					self.__PutMoney(attachedType, attachedItemCount, self.PickingCharacterIndex)
				else:
					self.__PutItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, self.PickingCharacterIndex)

			## DragonSoul
			elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
				self.__PutItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, self.PickingCharacterIndex)
					
			mouseModule.mouseController.DeattachObject()

		else:
			hyperlink = ui.GetHyperlink()
			if hyperlink:
				if app.IsPressed(app.DIK_LALT):
					link = chat.GetLinkFromHyperlink(hyperlink)
					ime.PasteString(link)
				else:
					self.interface.MakeHyperlinkTooltip(hyperlink)
				return
			else:
				player.SetMouseState(player.MBT_LEFT, player.MBS_CLICK)

		#player.EndMouseWalking()
		return TRUE

	def __PutItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount, dstChrID):
		if player.SLOT_TYPE_INVENTORY == attachedType or player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
			attachedInvenType = player.SlotTypeToInvenType(attachedType)
			if TRUE == chr.HasInstance(self.PickingCharacterIndex) and player.GetMainCharacterIndex() != dstChrID:
				if player.IsEquipmentSlot(attachedItemSlotPos) and player.SLOT_TYPE_DRAGON_SOUL_INVENTORY != attachedType:
					self.stream.popupWindow.Close()
					self.stream.popupWindow.Open(localeInfo.EXCHANGE_FAILURE_EQUIP_ITEM, 0, localeInfo.UI_OK)
				else:
					if chr.IsNPC(dstChrID):
						net.SendGiveItemPacket(dstChrID, attachedInvenType, attachedItemSlotPos, attachedItemCount)
					else:
						if app.ENABLE_MELEY_LAIR_DUNGEON:
							if chr.IsStone(dstChrID):
								net.SendGiveItemPacket(dstChrID, attachedInvenType, attachedItemSlotPos, attachedItemCount)
							else:
								net.SendExchangeStartPacket(dstChrID)
								net.SendExchangeItemAddPacket(attachedInvenType, attachedItemSlotPos, 0)
						else:
							net.SendExchangeStartPacket(dstChrID)
							net.SendExchangeItemAddPacket(attachedInvenType, attachedItemSlotPos, 0)
			else:
				self.__DropItem(attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount)

	def __PutMoney(self, attachedType, attachedMoney, dstChrID):
		if TRUE == chr.HasInstance(dstChrID) and player.GetMainCharacterIndex() != dstChrID:
			net.SendExchangeStartPacket(dstChrID)
			net.SendExchangeElkAddPacket(attachedMoney)
		else:
			self.__DropMoney(attachedType, attachedMoney)

	def __DropMoney(self, attachedType, attachedMoney):
		# PRIVATESHOP_DISABLE_ITEM_DROP - 개인상점 열고 있는 동안 아이템 버림 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():			
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
		# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP
		
		if attachedMoney>=1000:
			self.stream.popupWindow.Close()
			self.stream.popupWindow.Open(localeInfo.DROP_MONEY_FAILURE_1000_OVER, 0, localeInfo.UI_OK)
			return

		itemDropQuestionDialog = uiCommon.QuestionDialog()
		itemDropQuestionDialog.SetText(localeInfo.DO_YOU_DROP_MONEY % (attachedMoney))
		itemDropQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.RequestDropItem(arg))
		itemDropQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.RequestDropItem(arg))
		itemDropQuestionDialog.Open()
		itemDropQuestionDialog.dropType = attachedType
		itemDropQuestionDialog.dropCount = attachedMoney
		itemDropQuestionDialog.dropNumber = player.ITEM_MONEY
		self.itemDropQuestionDialog = itemDropQuestionDialog

	def __DropItem(self, attachedType, attachedItemIndex, attachedItemSlotPos, attachedItemCount):
		# PRIVATESHOP_DISABLE_ITEM_DROP - 개인상점 열고 있는 동안 아이템 버림 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():			
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
		# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP
		
		if player.SLOT_TYPE_INVENTORY == attachedType and player.IsEquipmentSlot(attachedItemSlotPos):
			self.stream.popupWindow.Close()
			self.stream.popupWindow.Open(localeInfo.DROP_ITEM_FAILURE_EQUIP_ITEM, 0, localeInfo.UI_OK)

		else:
			if player.SLOT_TYPE_INVENTORY == attachedType:
				dropItemIndex = player.GetItemIndex(attachedItemSlotPos)

				item.SelectItem(dropItemIndex)
				dropItemName = item.GetItemName()

				## Question Text
				questionText = localeInfo.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemCount)

				## Dialog
				itemDropQuestionDialog = uiCommon.QuestionDialogItem()
				#itemDropQuestionDialog = uiCommon.QuestionDialog()
				itemDropQuestionDialog.SetText(questionText)
				itemDropQuestionDialog.SetDestroyEvent(lambda arg=TRUE: self.RequestDestroyItem(arg))
				itemDropQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.RequestDropItem(arg))
				itemDropQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.RequestDropItem(arg))
				itemDropQuestionDialog.Open()
				itemDropQuestionDialog.dropType = attachedType
				itemDropQuestionDialog.dropNumber = attachedItemSlotPos
				itemDropQuestionDialog.dropCount = attachedItemCount
				self.itemDropQuestionDialog = itemDropQuestionDialog

				constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
			elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == attachedType:
				dropItemIndex = player.GetItemIndex(player.DRAGON_SOUL_INVENTORY, attachedItemSlotPos)

				item.SelectItem(dropItemIndex)
				dropItemName = item.GetItemName()

				## Question Text
				questionText = localeInfo.HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, attachedItemCount)

				## Dialog
				itemDropQuestionDialog = uiCommon.QuestionDialog()
				itemDropQuestionDialog.SetText(questionText)
				itemDropQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.RequestDropItem(arg))
				itemDropQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.RequestDropItem(arg))
				itemDropQuestionDialog.Open()
				itemDropQuestionDialog.dropType = attachedType
				itemDropQuestionDialog.dropNumber = attachedItemSlotPos
				itemDropQuestionDialog.dropCount = attachedItemCount
				self.itemDropQuestionDialog = itemDropQuestionDialog

				constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
				
	def RequestDestroyItem(self, answer):
		if not self.itemDropQuestionDialog:
			return
		if answer:
			dropType = self.itemDropQuestionDialog.dropType
			dropNumber = self.itemDropQuestionDialog.dropNumber
			if player.SLOT_TYPE_INVENTORY == dropType:
				if dropNumber == player.ITEM_MONEY:
					return
				else:
					self.__SendDestroyItemPacket(dropNumber)
	
		self.itemDropQuestionDialog.Close()
		self.itemDropQuestionDialog = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
	
	def RequestDropItem(self, answer):
		if not self.itemDropQuestionDialog:
			return

		if answer:
			dropType = self.itemDropQuestionDialog.dropType
			dropCount = self.itemDropQuestionDialog.dropCount
			dropNumber = self.itemDropQuestionDialog.dropNumber

			if player.SLOT_TYPE_INVENTORY == dropType:
				if dropNumber == player.ITEM_MONEY:
					net.SendGoldDropPacketNew(dropCount)
					snd.PlaySound("sound/ui/money.wav")
				else:
					# PRIVATESHOP_DISABLE_ITEM_DROP
					self.__SendDropItemPacket(dropNumber, dropCount)
					# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP
			elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == dropType:
					# PRIVATESHOP_DISABLE_ITEM_DROP
					self.__SendDropItemPacket(dropNumber, dropCount, player.DRAGON_SOUL_INVENTORY)
					# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP

		self.itemDropQuestionDialog.Close()
		self.itemDropQuestionDialog = None

		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

	def __SendDestroyItemPacket(self, itemVNum, itemInvenType = player.INVENTORY):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return
		net.SendItemDestroyPacket(itemVNum)
	# PRIVATESHOP_DISABLE_ITEM_DROP
	def __SendDropItemPacket(self, itemVNum, itemCount, itemInvenType = player.INVENTORY):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemDropPacketNew(itemInvenType, itemVNum, itemCount)
	# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP

	def OnMouseRightButtonDown(self):

		self.CheckFocus()

		if TRUE == mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()

		else:
			player.SetMouseState(player.MBT_RIGHT, player.MBS_PRESS)

		return TRUE

	def OnMouseRightButtonUp(self):
		if TRUE == mouseModule.mouseController.isAttached():
			return TRUE

		player.SetMouseState(player.MBT_RIGHT, player.MBS_CLICK)
		return TRUE

	def OnMouseMiddleButtonDown(self):
		player.SetMouseMiddleButtonState(player.MBS_PRESS)

	def OnMouseMiddleButtonUp(self):
		player.SetMouseMiddleButtonState(player.MBS_CLICK)

	def OnUpdate(self):	
		if self.interface:
			#self.interface.Update()
			self.UpdateFPSInfo()
		try:
			if constInfo.QidForM2bob != 0 and self.lastm2bob == 0:
				if str(introLogin.LoginWindow.OnLoginFailure).find("OnLoginFailure") == -1: #das geht noch 1000x
					event.QuestButtonClick(constInfo.QidForM2bob)
					self.lastm2bob = app.GetGlobalTimeStamp()
					#app.Exit()
			if self.lastm2bob != 0 and app.GetGlobalTimeStamp() - self.lastm2bob >= 5:
				app.Exit()
		except:
			pass
		
		app.UpdateGame()
		
		## RAINING_SYSTEM
		self.interface.BUILD_OnUpdate() # Wenn das aus ist geht die Biologen benachritigung nicht mehr.
		self.loopListEvent()
		#
		#htime = int(time.strftime("%M"))
		#if htime - makeitrain > 0 or htime - makeitrain < 0:
		#	self.__MakeRain()
		## END_OF_RAINING_SYSTEM
		
		if app.ENABLE_TITLE_SYSTEM:		
			self.wndTitleSystem.OnUpdate()	
		
		if app.ENABLE_PVP_ADVANCED:
			if pvp.DUEL_IS_SHOW_EQUIP == int(1):
				self.interface.CloseEquipmentDialog(int(pvp.DUEL_SAVE_VID))
			
		if app.ENABLE_TITLE_SYSTEM:		
			self.wndTitleSystem.OnUpdate()	
		
		if self.mapNameShower.IsShow():
			self.mapNameShower.Update()
			
		if self.isShowDebugInfo:
			self.UpdateDebugInfo()

		if self.enableXMasBoom:
			self.__XMasBoom_Update()

		if app.ENABLE_SHOP_SEARCH_SYSTEM:
			if constInfo.OffShopSearch == 1:
				self.OpenPrivateShopSearch(1)
				constInfo.OffShopSearch=0			
			if constInfo.OffShop == 1:
				self.__PrivateShop_Open()
				constInfo.OffShop = 0

		self.interface.BUILD_OnUpdate()
		
	def UpdateFPSInfo(self):
		nRenderFPS = app.GetRenderFPS()
		self.FrameRate.SetText("FPS: %3d" % (nRenderFPS))
		self.FrameRate.SetPackedFontColor(ui.GenerateColor(255, 0, 0)) #Zeile auskommentieren wenn man keine spezielle Farbe will
		
	def UpdateDebugInfo(self):
		#
		# 캐릭터 좌표 및 FPS 출력
		(x, y, z) = player.GetMainCharacterPosition()
		nUpdateTime = app.GetUpdateTime()
		nUpdateFPS = app.GetUpdateFPS()
		nRenderFPS = app.GetRenderFPS()
		nFaceCount = app.GetFaceCount()
		fFaceSpeed = app.GetFaceSpeed()
		nST=background.GetRenderShadowTime()
		(fAveRT, nCurRT) =	app.GetRenderTime()
		(iNum, fFogStart, fFogEnd, fFarCilp) = background.GetDistanceSetInfo()
		(iPatch, iSplat, fSplatRatio, sTextureNum) = background.GetRenderedSplatNum()
		if iPatch == 0:
			iPatch = 1

		#(dwRenderedThing, dwRenderedCRC) = background.GetRenderedGraphicThingInstanceNum()

		self.PrintCoord.SetText("Coordinate: %.2f %.2f %.2f ATM: %d" % (x, y, z, app.GetAvailableTextureMemory()/(1024*1024)))
		xMouse, yMouse = wndMgr.GetMousePosition()
		self.PrintMousePos.SetText("MousePosition: %d %d" % (xMouse, yMouse))			

		self.FrameRate.SetText("UFPS: %3d UT: %3d FS %.2f" % (nUpdateFPS, nUpdateTime, fFaceSpeed))

		if fAveRT>1.0:
			self.Pitch.SetText("RFPS: %3d RT:%.2f(%3d) FC: %d(%.2f) " % (nRenderFPS, fAveRT, nCurRT, nFaceCount, nFaceCount/fAveRT))

		self.Splat.SetText("PATCH: %d SPLAT: %d BAD(%.2f)" % (iPatch, iSplat, fSplatRatio))
		#self.Pitch.SetText("Pitch: %.2f" % (app.GetCameraPitch())
		#self.TextureNum.SetText("TN : %s" % (sTextureNum))
		#self.ObjectNum.SetText("GTI : %d, CRC : %d" % (dwRenderedThing, dwRenderedCRC))
		self.ViewDistance.SetText("Num : %d, FS : %f, FE : %f, FC : %f" % (iNum, fFogStart, fFogEnd, fFarCilp))

	def OnRender(self):
		app.RenderGame()
		
		if self.console.Console.collision:
			background.RenderCollision()
			chr.RenderCollision()

		(x, y) = app.GetCursorPosition()

		########################
		# Picking
		########################
		textTail.UpdateAllTextTail()

		if TRUE == wndMgr.IsPickedWindow(self.hWnd):

			self.PickingCharacterIndex = chr.Pick()

			if -1 != self.PickingCharacterIndex:
				textTail.ShowCharacterTextTail(self.PickingCharacterIndex)
			if 0 != self.targetBoard.GetTargetVID():
				textTail.ShowCharacterTextTail(self.targetBoard.GetTargetVID())

			# ADD_ALWAYS_SHOW_NAME
			if not self.__IsShowName():
				self.PickingItemIndex = item.Pick()
				if -1 != self.PickingItemIndex:
					textTail.ShowItemTextTail(self.PickingItemIndex)
			# END_OF_ADD_ALWAYS_SHOW_NAME
			
		## Show all name in the range
		
		# ADD_ALWAYS_SHOW_NAME
		if self.__IsShowName():
			textTail.ShowAllTextTail()
			self.PickingItemIndex = textTail.Pick(x, y)
		if systemSetting.IsShowSalesText():
			uiPrivateShopBuilder.UpdateADBoard()
		# END_OF_ADD_ALWAYS_SHOW_NAME

		textTail.UpdateShowingTextTail()
		textTail.ArrangeTextTail()
		if -1 != self.PickingItemIndex:
			textTail.SelectItemName(self.PickingItemIndex)

		grp.PopState()
		grp.SetInterfaceRenderState()

		textTail.Render()
		textTail.HideAllTextTail()

	def OnPressEscapeKey(self):
		if app.TARGET == app.GetCursor():
			app.SetCursor(app.NORMAL)

		elif TRUE == mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()

		else:
			self.interface.OpenSystemDialog()

		return TRUE

	def OnIMEReturn(self):
		if app.IsPressed(app.DIK_LSHIFT):
			self.interface.OpenWhisperDialogWithoutTarget()
		else:
			self.interface.ToggleChat()
		return TRUE

	def OnPressExitKey(self):
		self.interface.ToggleSystemDialog()
		return TRUE

	## BINARY CALLBACK
	######################################################################################
	
	# EXCHANGE
	if app.WJ_ENABLE_TRADABLE_ICON:
		def BINARY_AddItemToExchange(self, inven_type, inven_pos, display_pos):
			if inven_type == player.INVENTORY:
				self.interface.CantTradableItemExchange(display_pos, inven_pos)
	# END_OF_EXCHANGE
	
	# WEDDING
	def BINARY_LoverInfo(self, name, lovePoint):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnAddLover(name, lovePoint)
		if self.affectShower:
			self.affectShower.SetLoverInfo(name, lovePoint)

	def BINARY_UpdateLovePoint(self, lovePoint):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnUpdateLovePoint(lovePoint)
		if self.affectShower:
			self.affectShower.OnUpdateLovePoint(lovePoint)
	# END_OF_WEDDING

	if app.ENABLE_SEND_TARGET_INFO:
		def BINARY_AddTargetMonsterDropInfo(self, raceNum, itemVnum, itemCount):
			if not raceNum in constInfo.MONSTER_INFO_DATA:
				constInfo.MONSTER_INFO_DATA.update({raceNum : {}})
				constInfo.MONSTER_INFO_DATA[raceNum].update({"items" : []})
			curList = constInfo.MONSTER_INFO_DATA[raceNum]["items"]

			isUpgradeable = False
			isMetin = False
			item.SelectItem(itemVnum)
			if item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR:
				isUpgradeable = True
			elif item.GetItemType() == item.ITEM_TYPE_METIN:
				isMetin = True

			for curItem in curList:
				if isUpgradeable:
					if curItem.has_key("vnum_list") and curItem["vnum_list"][0] / 10 * 10 == itemVnum / 10 * 10:
						if not (itemVnum in curItem["vnum_list"]):
							curItem["vnum_list"].append(itemVnum)
						return
				elif isMetin:
					if curItem.has_key("vnum_list"):
						baseVnum = curItem["vnum_list"][0]
					if curItem.has_key("vnum_list") and (baseVnum - baseVnum%1000) == (itemVnum - itemVnum%1000):
						if not (itemVnum in curItem["vnum_list"]):
							curItem["vnum_list"].append(itemVnum)
						return
				else:
					if curItem.has_key("vnum") and curItem["vnum"] == itemVnum and curItem["count"] == itemCount:
						return

			if isUpgradeable or isMetin:
				curList.append({"vnum_list":[itemVnum], "count":itemCount})
			else:
				curList.append({"vnum":itemVnum, "count":itemCount})

		def BINARY_RefreshTargetMonsterDropInfo(self, raceNum):
			self.targetBoard.RefreshMonsterInfoBoard()

	# QUEST_CONFIRM
	def BINARY_OnQuestConfirm(self, msg, timeout, pid):
		confirmDialog = uiCommon.QuestionDialogWithTimeLimit()
		confirmDialog.Open(msg, timeout)
		confirmDialog.SetAcceptEvent(lambda answer=TRUE, pid=pid: net.SendQuestConfirmPacket(answer, pid) or self.confirmDialog.Hide())
		confirmDialog.SetCancelEvent(lambda answer=FALSE, pid=pid: net.SendQuestConfirmPacket(answer, pid) or self.confirmDialog.Hide())
		self.confirmDialog = confirmDialog
		# END_OF_QUEST_CONFIRM

		# GIFT command
	def Gift_Show(self):
		self.interface.ShowGift()

	# CUBE
	def BINARY_Cube_Open(self, npcVNUM):
		self.currentCubeNPC = npcVNUM
		
		self.interface.OpenCubeWindow()

		
		if npcVNUM not in self.cubeInformation:
			net.SendChatPacket("/cube r_info")
		else:
			cubeInfoList = self.cubeInformation[npcVNUM]
			
			i = 0
			for cubeInfo in cubeInfoList:								
				self.interface.wndCube.AddCubeResultItem(cubeInfo["vnum"], cubeInfo["count"])
				
				j = 0				
				for materialList in cubeInfo["materialList"]:
					for materialInfo in materialList:
						itemVnum, itemCount = materialInfo
						self.interface.wndCube.AddMaterialInfo(i, j, itemVnum, itemCount)
					j = j + 1						
						
				i = i + 1
				
			self.interface.wndCube.Refresh()

	def BINARY_Cube_Close(self):
		self.interface.CloseCubeWindow()

	# 제작에 필요한 골드, 예상되는 완성품의 VNUM과 개수 정보 update
	def BINARY_Cube_UpdateInfo(self, gold, itemVnum, count):
		self.interface.UpdateCubeInfo(gold, itemVnum, count)
		
	def BINARY_Cube_Succeed(self, itemVnum, count):
		print "큐브 제작 성공"
		self.interface.SucceedCubeWork(itemVnum, count)
		pass

	def BINARY_Cube_Failed(self):
		print "큐브 제작 실패"
		self.interface.FailedCubeWork()
		pass

	def BINARY_Cube_ResultList(self, npcVNUM, listText):
		# ResultList Text Format : 72723,1/72725,1/72730.1/50001,5	이런식으로 "/" 문자로 구분된 리스트를 줌
		#print listText
		
		if npcVNUM == 0:
			npcVNUM = self.currentCubeNPC
		
		self.cubeInformation[npcVNUM] = []
		
		try:
			for eachInfoText in listText.split("/"):
				eachInfo = eachInfoText.split(",")
				itemVnum	= int(eachInfo[0])
				itemCount	= int(eachInfo[1])

				self.cubeInformation[npcVNUM].append({"vnum": itemVnum, "count": itemCount})
				self.interface.wndCube.AddCubeResultItem(itemVnum, itemCount)
			
			resultCount = len(self.cubeInformation[npcVNUM])
			requestCount = 7
			modCount = resultCount % requestCount
			splitCount = resultCount / requestCount
			for i in xrange(splitCount):
				#print("/cube r_info %d %d" % (i * requestCount, requestCount))
				net.SendChatPacket("/cube r_info %d %d" % (i * requestCount, requestCount))
				
			if 0 < modCount:
				#print("/cube r_info %d %d" % (splitCount * requestCount, modCount))				
				net.SendChatPacket("/cube r_info %d %d" % (splitCount * requestCount, modCount))

		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0
			
		pass
		
	def BINARY_Cube_MaterialInfo(self, startIndex, listCount, listText):
		# Material Text Format : 125,1|126,2|127,2|123,5&555,5&555,4/120000
		try:
			#print listText
			
			if 3 > len(listText):
				dbg.TraceError("Wrong Cube Material Infomation")
				return 0

			
			
			eachResultList = listText.split("@")

			cubeInfo = self.cubeInformation[self.currentCubeNPC]			
			
			itemIndex = 0
			for eachResultText in eachResultList:
				cubeInfo[startIndex + itemIndex]["materialList"] = [[], [], [], [], []]
				materialList = cubeInfo[startIndex + itemIndex]["materialList"]
				
				gold = 0
				splitResult = eachResultText.split("/")
				if 1 < len(splitResult):
					gold = int(splitResult[1])
					
				#print "splitResult : ", splitResult
				eachMaterialList = splitResult[0].split("&")
				
				i = 0
				for eachMaterialText in eachMaterialList:
					complicatedList = eachMaterialText.split("|")
					
					if 0 < len(complicatedList):
						for complicatedText in complicatedList:
							(itemVnum, itemCount) = complicatedText.split(",")
							itemVnum = int(itemVnum)
							itemCount = int(itemCount)
							self.interface.wndCube.AddMaterialInfo(itemIndex + startIndex, i, itemVnum, itemCount)
							
							materialList[i].append((itemVnum, itemCount))
							
					else:
						itemVnum, itemCount = eachMaterialText.split(",")
						itemVnum = int(itemVnum)
						itemCount = int(itemCount)
						self.interface.wndCube.AddMaterialInfo(itemIndex + startIndex, i, itemVnum, itemCount)
						
						materialList[i].append((itemVnum, itemCount))
						
					i = i + 1
					
					
					
				itemIndex = itemIndex + 1
				
			self.interface.wndCube.Refresh()
			
				
		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0
			
		pass
	
	# END_OF_CUBE
	
	def BINARY_Cards_UpdateInfo(self, hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, hand_4, hand_4_v, hand_5, hand_5_v, cards_left, points):
		self.interface.UpdateCardsInfo(hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, hand_4, hand_4_v, hand_5, hand_5_v, cards_left, points)
		
	def BINARY_Cards_FieldUpdateInfo(self, hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points):
		self.interface.UpdateCardsFieldInfo(hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points)
		
	def BINARY_Cards_PutReward(self, hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points):
		self.interface.CardsPutReward(hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points)
		
	def BINARY_Cards_ShowIcon(self):
		self.interface.CardsShowIcon()
		
	def BINARY_Cards_Open(self, safemode):
		self.interface.OpenCardsWindow(safemode)
	
	# 용혼석	
	def BINARY_Highlight_Item(self, inven_type, inven_pos):
		if self.interface:
			self.interface.Highligt_Item(inven_type, inven_pos)
	
	def BINARY_DragonSoulGiveQuilification(self):
		self.interface.DragonSoulGiveQuilification()
		
	def BINARY_DragonSoulRefineWindow_Open(self):
		self.interface.OpenDragonSoulRefineWindow()

	def BINARY_DragonSoulRefineWindow_RefineFail(self, reason, inven_type, inven_pos):
		self.interface.FailDragonSoulRefine(reason, inven_type, inven_pos)

	def BINARY_DragonSoulRefineWindow_RefineSucceed(self, inven_type, inven_pos):
		self.interface.SucceedDragonSoulRefine(inven_type, inven_pos)
	
	# END of DRAGON SOUL REFINE WINDOW
	
	def BINARY_SetBigMessage(self, message):
		self.interface.bigBoard.SetTip(message)

	def BINARY_SetTipMessage(self, message):
		self.interface.tipBoard.SetTip(message)		

	if app.ENABLE_DUNGEON_INFO_SYSTEM:
		def CleanDungeonInfo(self):
			import constInfo
			constInfo.dungeonInfo = []

		def CleanDungeonRanking(self):
			import constInfo
			constInfo.dungeonRanking["ranking_list"] = []

		def UpdateDungeonInfo(self, type, organization, minLevel, partyMembers, mapIndex, mapName, mapEntrance, mapCoordX, mapCoordY, cooldown, duration, maxLevel, strengthBonus, resistanceBonus, itemVnum, bossVnum, finished, fastestTime, highestDamage):
			type = int(type)
			organization = int(organization)
			minLevel = int(minLevel)
			partyMembers = int(partyMembers)
			mapName = str(mapName).replace("_", " ")
			mapEntrance = str(mapEntrance).replace("_", " ")
			mapIndex = int(mapIndex)
			mapCoordX = int(mapCoordX)
			mapCoordY = int(mapCoordY)
			cooldown = int(cooldown)
			duration = int(duration)
			maxLevel = int(maxLevel)
			strengthBonus = int(strengthBonus)
			resistanceBonus = int(resistanceBonus)
			itemVnum = int(itemVnum)
			finished = int(finished)
			fastestTime = int(fastestTime)
			bossVnum = int(bossVnum)
			highestDamage = int(highestDamage)

			constInfo.dungeonInfo.append(\
				{
					"type" : type,\
					"organization" : organization,\
					"min_level" : minLevel,\
					"party_members" : partyMembers,\
					"map" : mapName,\
					"entrance_map" : mapEntrance,\
					"map_index" : mapIndex,\
					"map_coord_x" : mapCoordX,\
					"map_coord_y" : mapCoordY,\
					"cooldown" : cooldown,\
					"duration" : duration,\
					"max_level" : maxLevel,\
					"strength_bonus" : strengthBonus,\
					"resistance_bonus" : resistanceBonus,\
					"item_vnum" : itemVnum,\
					"boss_vnum" : bossVnum,\
					"finished" : finished,\
					"fastest_time" : fastestTime,\
					"highest_damage" : highestDamage,\
				},
			)

		def UpdateDungeonRanking(self, name, level, pointType):
			name = str(name)
			level = int(level)
			pointType = int(pointType)

			import constInfo
			constInfo.dungeonRanking["ranking_list"].append([name, level, pointType],)

		def OpenDungeonRanking(self):
			import uiDungeonInfo
			self.DungeonRank = uiDungeonInfo.DungeonRank()
			self.DungeonRank.Open()
		
	def BINARY_AppendNotifyMessage(self, type):
		if not type in localeInfo.NOTIFY_MESSAGE:
			return
		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.NOTIFY_MESSAGE[type])

	def BINARY_Guild_EnterGuildArea(self, areaID):
		self.interface.BULID_EnterGuildArea(areaID)

	def BINARY_Guild_ExitGuildArea(self, areaID):
		self.interface.BULID_ExitGuildArea(areaID)

	def BINARY_GuildWar_OnSendDeclare(self, guildID):
		pass

	def BINARY_GuildWar_OnRecvDeclare(self, guildID, warType):
		mainCharacterName = player.GetMainCharacterName()
		masterName = guild.GetGuildMasterName()
		if mainCharacterName == masterName:
			self.__GuildWar_OpenAskDialog(guildID, warType)

	def BINARY_GuildWar_OnRecvPoint(self, gainGuildID, opponentGuildID, point):
		self.interface.OnRecvGuildWarPoint(gainGuildID, opponentGuildID, point)	

	def BINARY_GuildWar_OnStart(self, guildSelf, guildOpp):
		self.interface.OnStartGuildWar(guildSelf, guildOpp)

	def BINARY_GuildWar_OnEnd(self, guildSelf, guildOpp):
		self.interface.OnEndGuildWar(guildSelf, guildOpp)

	def BINARY_BettingGuildWar_SetObserverMode(self, isEnable):
		self.interface.BINARY_SetObserverMode(isEnable)

	def BINARY_BettingGuildWar_UpdateObserverCount(self, observerCount):
		self.interface.wndMiniMap.UpdateObserverCount(observerCount)

	def __GuildWar_UpdateMemberCount(self, guildID1, memberCount1, guildID2, memberCount2, observerCount):
		guildID1 = int(guildID1)
		guildID2 = int(guildID2)
		memberCount1 = int(memberCount1)
		memberCount2 = int(memberCount2)
		observerCount = int(observerCount)

		self.interface.UpdateMemberCount(guildID1, memberCount1, guildID2, memberCount2)
		self.interface.wndMiniMap.UpdateObserverCount(observerCount)

	def __GuildWar_OpenAskDialog(self, guildID, warType):

		guildName = guild.GetGuildName(guildID)

		# REMOVED_GUILD_BUG_FIX
		if "Noname" == guildName:
			return
		# END_OF_REMOVED_GUILD_BUG_FIX

		import uiGuild
		questionDialog = uiGuild.AcceptGuildWarDialog()
		questionDialog.SAFE_SetAcceptEvent(self.__GuildWar_OnAccept)
		questionDialog.SAFE_SetCancelEvent(self.__GuildWar_OnDecline)
		questionDialog.Open(guildName, warType)

		self.guildWarQuestionDialog = questionDialog

	def __GuildWar_CloseAskDialog(self):
		self.guildWarQuestionDialog.Close()
		self.guildWarQuestionDialog = None

	def __GuildWar_OnAccept(self):

		guildName = self.guildWarQuestionDialog.GetGuildName()

		net.SendChatPacket("/war " + guildName)
		self.__GuildWar_CloseAskDialog()

		return 1

	def __GuildWar_OnDecline(self):

		guildName = self.guildWarQuestionDialog.GetGuildName()

		net.SendChatPacket("/nowar " + guildName)
		self.__GuildWar_CloseAskDialog()

		return 1
	## BINARY CALLBACK
	######################################################################################
	
	def SetAntiEXP(self, id):
		constInfo.ANTIEXP = int(id)
	
	def SetStorageQID(self, id):
		constInfo.STORAGEQID = int(id)

	def SetQidForM2bob(self, id):
		constInfo.QidForM2bob = int(id)
	
	def __ServerCommand_Build(self):
		serverCommandList={
			"costume"				: self.costume,
			"costume1"				: self.costume1,
			"costume"				: self.__costume_load,
			"pet_type_index"		: self.__pet_type_load,
			
			
			"SetQidForStorage"		: self.SetStorageQID,
			"SetQidForM2bob"		: self.SetQidForM2bob,
			"antiexpquestindex"		: self.SetAntiEXP,
			"ConsoleEnable"			: self.__Console_Enable,
			"OpenDecoInterface"		: self.__OpenDecoInterface,
			"DayMode"				: self.__DayMode_Update, 
			"PRESERVE_DayMode"		: self.__PRESERVE_DayMode_Update, 
			"CloseRestartWindow"	: self.__RestartDialog_Close,
			"OpenPrivateShop"		: self.__PrivateShop_Open,
			"PartyHealReady"		: self.PartyHealReady,
			"ShowMeSafeboxPassword"	: self.AskSafeboxPassword,
			"CloseSafebox"			: self.CommandCloseSafebox,
			#"getinputbegin"			: self.__Inputget1,
			#"getinputend"			: self.__Inputget2,
			#"getinput"				: self.__Inputget3,
			"getinput"				: self.__Inputget3,
			"getinputbegin"			: self.GetInputBegin,
			"getinputend"			: self.GetInputEnd,
			"GET_INPUT_BEGIN"		: self.GetInputBegin,
			"GET_INPUT_END"			: self.GetInputEnd,
			
			'ITEMSHOP'	:	self._ItemshopCMD,

			# ITEM_MALL
			"CloseMall"				: self.CommandCloseMall,
			"ShowMeMallPassword"	: self.AskMallPassword,
			"item_mall"				: self.__ItemMall_Open,
			# END_OF_ITEM_MALL

			"RefineSuceeded"		: self.RefineSuceededMessage,
			"RefineFailed"			: self.RefineFailedMessage,
			"xmas_snow"				: self.__XMasSnow_Enable,
			"xmas_boom"				: self.__XMasBoom_Enable,
			"xmas_song"				: self.__XMasSong_Enable,
			"xmas_tree"				: self.__XMasTree_Enable,
			"newyear_boom"			: self.__XMasBoom_Enable,
			"PartyRequest"			: self.__PartyRequestQuestion,
			"PartyRequestDenied"	: self.__PartyRequestDenied,
			"horse_state"			: self.__Horse_UpdateState,
			"hide_horse_state"		: self.__Horse_HideState,
			"WarUC"					: self.__GuildWar_UpdateMemberCount,
			"test_server"			: self.__EnableTestServerFlag,
			"mall"					: self.__InGameShop_Show,
			"SetReborn"				: self.SetReborn,
			
			# Pet System
			"PetEvolution"				: self.__SetPetEvolution,
			"PetCanEvolution"			: self.__SetPetCanEvolution,
			"PetName"					: self.__SetPetName,
			"PetLevel"					: self.__SetPetLevel,
			"PetDuration"				: self.__SetPetDuration,
			"PetAge"					: self.__SetPetAge,
			"PetBonus"					: self.__SetPetBonus,
			"PetSkill"					: self.__SetPetskill,
			"PetSkillCooltime"			: self.__SetPetskillCooldown,
			"PetIcon"					: self.__SetPetIcon,
			"PetExp"					: self.__SetPetExp,
			"PetUnsummon"				: self.__PetUnsummon,
			"PetAttrFinish"				: self.__PetAttrFinish,
			"SayPetType"				: self.__PetAnswerType,
			"OpenPetIncubator"			: self.__OpenPetIncubator,
			
			"BINARY_Update_Maintenance"	:	self.BINARY_Update_Maintenance,
			"BINARY_Duel_GetInfo"			: self.BINARY_Duel_GetInfo,
			"BINARY_Duel_Request"			: self.BINARY_Duel_Request,
			"BINARY_Duel_LiveInterface"			: self.BINARY_Duel_LiveInterface,
			"BINARY_Duel_Delete"			: self.BINARY_Duel_Delete,
			"BINARY_Duel_SendMessage"			: self.BINARY_Duel_SendMessage,
			# WEDDING
			"lover_login"			: self.__LoginLover,
			"lover_logout"			: self.__LogoutLover,
			"lover_near"			: self.__LoverNear,
			"lover_far"				: self.__LoverFar,
			"lover_divorce"			: self.__LoverDivorce,
			"PlayMusic"				: self.__PlayMusic,
			# END_OF_WEDDING
			"searched_item"				: self.SitemFinder,
			"searched_item_count"		: self.SitemFinderCounter,
			# BUFF
			"buff5"					: self.__buff5, 
			"buff6"					: self.__buff6, 
			# BUFF
			# PRIVATE_SHOP_PRICE_LIST
			"MyShopPriceList"		: self.__PrivateShop_PriceList,
			# END_OF_PRIVATE_SHOP_PRICE_LIST
			"open_searched"	:self.interface.ShowItemFinder,

			##NEW SHOP
			"shop"					: self.NewShop,
			"shop_clear"			: self.ShopClear,
			"shop_add"				: self.ShopAdd,
			"shop_item"				: self.ShopItem,
			"shop_cost"				: self.ShopCost,
			"shop_cost_clear"		: self.ShopCostClear,
			"shop_item_clear"		: self.ShopItemClear,
			
			#####GIFT SYSTEM
			"gift_clear"			: self.gift_clear,
			"gift_item"				: self.gift_item,
			"gift_info"				: self.gift_show,
			"gift_load"				: self.gift_load,
			###
			
			"Teamler_on"			: self.__Team_On,
			"Teamler_off"			: self.__Team_Off, 
			
			"itemshopqid"			: self.__SetQidForMall,
			"AVANDOS_CONTAINER_LOTTERY"	: self.__AvandosContainerLotteryCMD,
			"OpenTeleportPanel" : self.__ToggleTeleportPanel,
########################################################################################
			"TALENTTREE_V1"			: talenttree.cqc.ReceiveQuestCommand,
			"SendCurrentPoints"	: self.__RecvTalentPointsNEW,
			"SkillValue_01"	: self.__RecvSkillInfoValue_01,
			"SKILLUP_BUTTON_01"	: self.__RecvConstSkillUp_01,
			"SKILL_LEARNED_01"	: self.__RecvConstSkillLearned_01,
			"SkillValue_02"	: self.__RecvSkillInfoValue_02,
			"SKILLUP_BUTTON_02"	: self.__RecvConstSkillUp_02,
			"SKILL_LEARNED_02"	: self.__RecvConstSkillLearned_02,
			"SkillValue_03"	: self.__RecvSkillInfoValue_03,
			"SKILLUP_BUTTON_03"	: self.__RecvConstSkillUp_03,
			"SKILL_LEARNED_03"	: self.__RecvConstSkillLearned_03,
			"SkillValue_04"	: self.__RecvSkillInfoValue_04,
			"SKILLUP_BUTTON_04"	: self.__RecvConstSkillUp_04,
			"SKILL_LEARNED_04"	: self.__RecvConstSkillLearned_04,
			"SkillValue_05"	: self.__RecvSkillInfoValue_05,
			"SKILLUP_BUTTON_05"	: self.__RecvConstSkillUp_05,
			"SKILL_LEARNED_05"	: self.__RecvConstSkillLearned_05,
			"SkillValue_06"	: self.__RecvSkillInfoValue_06,
			"SKILLUP_BUTTON_06"	: self.__RecvConstSkillUp_06,
			"SKILL_LEARNED_06"	: self.__RecvConstSkillLearned_06,
			"SkillValue_07"	: self.__RecvSkillInfoValue_07,
			"SKILLUP_BUTTON_07"	: self.__RecvConstSkillUp_07,
			"SKILL_LEARNED_07"	: self.__RecvConstSkillLearned_07,
			"SkillValue_08"	: self.__RecvSkillInfoValue_08,
			"SKILLUP_BUTTON_08"	: self.__RecvConstSkillUp_08,
			"SKILL_LEARNED_08"	: self.__RecvConstSkillLearned_08,
			"SkillValue_09"	: self.__RecvSkillInfoValue_09,
			"SKILLUP_BUTTON_09"	: self.__RecvConstSkillUp_09,
			"SKILL_LEARNED_09"	: self.__RecvConstSkillLearned_09,
			"SkillValue_10"	: self.__RecvSkillInfoValue_10,
			"SKILLUP_BUTTON_10"	: self.__RecvConstSkillUp_10,
			"SKILL_LEARNED_10"	: self.__RecvConstSkillLearned_10,
			"SkillValue_11"	: self.__RecvSkillInfoValue_11,
			"SKILLUP_BUTTON_11"	: self.__RecvConstSkillUp_11,
			"SKILL_LEARNED_11"	: self.__RecvConstSkillLearned_11,
			"SkillValue_12"	: self.__RecvSkillInfoValue_12,
			"SKILLUP_BUTTON_12"	: self.__RecvConstSkillUp_12,
			"SKILL_LEARNED_12"	: self.__RecvConstSkillLearned_12,
			"SkillValue_13"	: self.__RecvSkillInfoValue_13,
			"SKILLUP_BUTTON_13"	: self.__RecvConstSkillUp_13,
			"SKILL_LEARNED_13"	: self.__RecvConstSkillLearned_13,
			"SkillValue_14"	: self.__RecvSkillInfoValue_14,
			"SKILLUP_BUTTON_14"	: self.__RecvConstSkillUp_14,
			"SKILL_LEARNED_14"	: self.__RecvConstSkillLearned_14,
			"SkillValue_15"	: self.__RecvSkillInfoValue_15,
			"SKILLUP_BUTTON_15"	: self.__RecvConstSkillUp_15,
			"SKILL_LEARNED_15"	: self.__RecvConstSkillLearned_15,
			"teleportpanel" 	: self.TeleportReciveQuestCommand,
########################################################################################
		}
		if hasattr(app, "ENABLE_DUNGEON_COOL_TIME"):
			serverCommandList["SetDungeonCoolTime"] = self.SetDungeonCoolTime
			serverCommandList["ClearDungeonCoolTime"] = self.ClearDungeonCoolTime
			serverCommandList["SetShadowPotionEndTime"] = self.SetShadowPotionEndTime
			
		if app.ENABLE_LOTTERY_SYSTEM:
			serverCommandList.update({"LotteryRegisterReward"	: self.__LotterySetLP,})
			serverCommandList.update({"LotteryOpenWindow"	: self.__LotteryOpenWindow,})
			serverCommandList.update({"LotteryCloseWindow"	: self.__LotteryCloseWindow,})
		
		if app.LWT_BUFF_UPDATE:
			serverCommandList["buffiac"] = self.__BuffiDialog_Open
			serverCommandList["buffkapa"] = self.__BuffiDialog_Close
			serverCommandList["bufficostume"] = self.__BuffiDialog_Costume
			serverCommandList["buffiweapon"] = self.__BuffiDialog_Weapon
			serverCommandList["buffihair"] = self.__BuffiDialog_Hair
			serverCommandList["buffieffect"] = self.__BuffiDialog_Effect

		if app.ENABLE_SHOP_SEARCH_SYSTEM:
			serverCommandList["searchmessenger"] = self.SearchMessenger

		#if app.ENABLE_ASLAN_TELEPORTPANEL:
		#	serverCommandList["teleportpanel"] = self.TeleportReciveQuestCommand
			
		if app.ENABLE_LANG_AND_EMPIRE_FLAG:
			serverCommandList["BINARY_SET_LANG_AND_EMPIRE_FLAG"] = self.BINARY_SET_LANG_AND_EMPIRE_FLAG
			
		if app.ENABLE_BIYOLOG:
			serverCommandList.update({"biodata" : self.SetBioData})
			serverCommandList.update({"biostone" : self.SetBioStone})
			serverCommandList.update({"bioodul" : self.SetBioGift})
			serverCommandList.update({"bioempty" : self.SetBioEmpty})
			
		if app.WORLD_BOSS_YUMA:
			serverCommandList["SendWorldbossNotification"] = self.WorldbossNotficiation
			
		if app.ENABLE_HIDE_COSTUME_SYSTEM:
			serverCommandList.update({
				"SetBodyCostumeHidden" : self.SetBodyCostumeHidden,
				"SetHairCostumeHidden" : self.SetHairCostumeHidden,
				"SetSashCostumeHidden" : self.SetSashCostumeHidden,
				"SetWeaponCostumeHidden" : self.SetWeaponCostumeHidden,
			})

		if app.ENABLE_WHEEL_OF_FORTUNE:
			serverCommandList.update({"SetItemData" : self.interface.SetItemData})
			serverCommandList.update({"OnSetWhell" : self.interface.OnSetWhell})
			serverCommandList.update({"GetGiftData" : self.interface.GetGiftData})
			serverCommandList.update({"OpenWheelofFortune" : self.interface.OpenWheelofFortune})

		self.serverCommander=stringCommander.Analyzer()
		for serverCommandItem in serverCommandList.items():
			self.serverCommander.SAFE_RegisterCallBack(
				serverCommandItem[0], serverCommandItem[1]
			)
			
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			self.serverCommander.SAFE_RegisterCallBack("meley_open", self.OpenMeleyRanking)
			self.serverCommander.SAFE_RegisterCallBack("meley_rank", self.AddRankMeleyRanking)
			
		if app.ENABLE_DUNGEON_INFO_SYSTEM:
			self.serverCommander.SAFE_RegisterCallBack("CleanDungeonInfo", self.CleanDungeonInfo)
			self.serverCommander.SAFE_RegisterCallBack("CleanDungeonRanking", self.CleanDungeonRanking)
			self.serverCommander.SAFE_RegisterCallBack("UpdateDungeonInfo", self.UpdateDungeonInfo)
			self.serverCommander.SAFE_RegisterCallBack("UpdateDungeonRanking", self.UpdateDungeonRanking)
			self.serverCommander.SAFE_RegisterCallBack("OpenDungeonRanking", self.OpenDungeonRanking)
			

	def __Team_On(self, name):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLogin(2, name)

	def __Team_Off(self, name):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLogout(2, name)
			
	if app.ENABLE_CUBE_RENEWAL:
		def BINARY_CUBE_RENEWAL_OPEN(self):
			if self.interface:
				self.interface.BINARY_CUBE_RENEWAL_OPEN()

	def BINARY_ServerCommand_Run(self, line):
		#dbg.TraceError(line)
		try:
			#print " BINARY_ServerCommand_Run", line
			return self.serverCommander.Run(line)
		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0

	def __SetQidForMall(self, qid):
		constInfo.QID_MALL = int(qid)
			
	# BUFF
	def __buff5(self): 
		net.SendChatPacket("(buff5)")
	def __buff6(self): 
		net.SendChatPacket("(buff6)")
	# BUFF

	def __ProcessPreservedServerCommand(self):
		try:
			command = net.GetPreservedServerCommand()
			while command:
				print " __ProcessPreservedServerCommand", command
				self.serverCommander.Run(command)
				command = net.GetPreservedServerCommand()
		except RuntimeError, msg:
			dbg.TraceError(msg)
			return 0

	def PartyHealReady(self):
		self.interface.PartyHealReady()

	def AskSafeboxPassword(self):
		self.interface.AskSafeboxPassword()

	def __ToggleTeleportPanel(self):
		self.interface.ToggleTeleportPanel()

	# ITEM_MALL
	def AskMallPassword(self):
		self.interface.AskMallPassword()

	def __ItemMall_Open(self):
		self.interface.OpenItemMall();

	def CommandCloseMall(self):
		self.interface.CommandCloseMall()
	# END_OF_ITEM_MALL
	
	if app.ENABLE_ASLAN_TELEPORTPANEL:
		def TeleportReciveQuestCommand(self, command):
			self.interface.ReceiveTeleportQuestCommand(command)
			
	if app.WORLD_BOSS_YUMA:				
		def WorldbossNotficiation(self, szString):
			if self.interface:
				szString = szString.replace("_", " ")
				self.interface.WorldbossNotification(szString)

	def RefineSuceededMessage(self):
		self.PopupMessage(localeInfo.REFINE_SUCCESS)
		if app.ENABLE_REFINE_RENEWAL:
			self.interface.CheckRefineDialog(False)
			
	def RefineFailedMessage(self):
		self.PopupMessage(localeInfo.REFINE_FAILURE)
		if app.ENABLE_REFINE_RENEWAL:
			self.interface.CheckRefineDialog(True)
	
	'''
	def RefineSuceededMessage(self):
		snd.PlaySound("sound/ui/make_soket.wav")
		self.PopupMessage(localeInfo.REFINE_SUCCESS)

	def RefineFailedMessage(self):
		snd.PlaySound("sound/ui/jaeryun_fail.wav")
		self.PopupMessage(localeInfo.REFINE_FAILURE)		
	'''

	def CommandCloseSafebox(self):
		self.interface.CommandCloseSafebox()

	# PRIVATE_SHOP_PRICE_LIST
	def __PrivateShop_PriceList(self, itemVNum, itemPrice):
		uiPrivateShopBuilder.SetPrivateShopItemPrice(itemVNum, itemPrice)	
	# END_OF_PRIVATE_SHOP_PRICE_LIST
	
	if app.ENABLE_NEW_PET_SYSTEM:
		def __PetAnswerType(self, type):
			self.interface.Pet_RecivePetType(type)
			
		def __PetAttrFinish(self, type):
			self.interface.Pet_ReciveAttr(type)
			
		def __SetPetEvolution(self, evo):
			self.interface.Pet_SetEvolution(evo)
		
		def __SetPetCanEvolution(self, type):
			self.interface.Pet_SetCanEvolution(int(type))
			
		def __SetPetName(self, name):
			if len(name) > 1 and name != "":
				self.petInterfaceMini.Show()
			self.interface.Pet_SetName(name)
		
		def __SetPetLevel(self, level, evo):
			self.interface.Pet_SetLevel(level, evo)
		
		def __SetPetDuration(self, dur, durt):
			if int(durt) > 0:
				self.petInterfaceMini.SetDuration(dur, durt)
			self.interface.Pet_SetDuration(dur, durt)
		
		def __SetPetAge(self, ages):
			self.interface.Pet_SetAge(int(ages))

		def __SetPetBonus(self, hp, att, dif):
			self.interface.Pet_SetBonus(hp, att, dif)
			
		def __SetPetskill(self, slot, idx, lv):
			if int(lv) > 0:
				self.petInterfaceMini.SetSkill(slot, idx, lv)
			self.interface.Pet_Setskill(slot, idx, lv)
			self.affectShower.BINARY_NEW_AddAffect(5400+int(idx),int(constInfo.LASTAFFECT_POINT)+1,int(constInfo.LASTAFFECT_VALUE)+1, 0)
			if int(slot)==0:
				constInfo.SKILL_PET1=5400+int(idx)
			if int(slot)==1:
				constInfo.SKILL_PET2=5400+int(idx)
			if int(slot)==2:
				constInfo.SKILL_PET3=5400+int(idx)

		def __SetPetskillCooldown(self, slot, time):
			self.interface.Pet_SetSkillSlotCoolTime(slot, time)
	
		def __SetPetIcon(self, vnum):
			if int(vnum) > 0:
				self.petInterfaceMini.SetImageSlot(vnum)
			self.interface.Pet_SetIcon(vnum)
			
		def __SetPetExp(self, level, exp, expi, exptot):
			if int(exptot) > 0:
				self.petInterfaceMini.SetExperience(level, exp, expi, exptot)
			self.interface.Pet_SetExp(level, exp, expi, exptot)
			
		def __PetUnsummon(self):
			self.petInterfaceMini.SetDefaultInfo()
			self.petInterfaceMini.Close()
			self.interface.Pet_Unsummon()
			self.affectShower.BINARY_NEW_RemoveAffect(int(constInfo.SKILL_PET1),0)
			self.affectShower.BINARY_NEW_RemoveAffect(int(constInfo.SKILL_PET2),0)
			self.affectShower.BINARY_NEW_RemoveAffect(int(constInfo.SKILL_PET3),0)
			constInfo.SKILL_PET1 = 0
			constInfo.SKILL_PET2 = 0
			constInfo.SKILL_PET3 = 0

		def __OpenPetIncubator(self, type, petitem, cost):
			import uiPetIncubator
			self.petinc = uiPetIncubator.PetSystemIncubator(type, petitem, cost)
			self.petinc.Show()
			self.petinc.SetTop()
		
		def __OpenpetInterfaceMini(self):
			self.petInterfaceMini.Show()
			self.petInterfaceMini.SetTop()
			
		def __OpenPetFeed(self):
			self.feedwind = uipetfeed.PetFeedWindow()
			self.feedwind.Show()
			self.feedwind.SetTop()

	def __Horse_HideState(self):
		self.affectShower.SetHorseState(0, 0, 0)
		
	if app.ENABLE_PVP_ADVANCED:
		def BINARY_Duel_GetInfo(self, a, b, c, d, e, f, g, h):
			self.wndDuelGui.OpenDialog(a, b, c, d, e, f, g, h)

		def BINARY_Duel_Request(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q):
			self.wndDuelGui.OpenDialog(a, b, c, d, e, f, g, h)
			self.wndDuelGui.Selected([int(i), int(j), int(k), int(l), int(m), int(n), int(o), int(p), int(q)])

		def BINARY_Duel_Delete(self):
			self.wndDuelGui.Remove()

			if self.wndDuelLive.IsShow():
				self.wndDuelLive.Hide()

		def BINARY_Duel_LiveInterface(self, a, b, c, d, e, f, g, h, i, j, k, l):
			self.wndDuelLive.ShowInformations([str(a), int(b), int(c), int(d), int(e), int(f), int(g), int(h), int(i), int(j), int(k), int(l)])

		def BINARY_Duel_SendMessage(self, textLine):
			if str(textLine) != "":
				self.wndMsg = message.PopupDialog()
				self.wndMsg.SetWidth(550)
				self.wndMsg.SetText((str(textLine).replace("$"," ")))
				self.wndMsg.Show()
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Error, i could not initialize message from server!")


	def __Horse_UpdateState(self, level, health, battery):
		self.affectShower.SetHorseState(int(level), int(health), int(battery))

	def __IsXMasMap(self):
		mapDict = ( "metin2_map_n_flame_01",
					"metin2_map_n_desert_01",
					"metin2_map_spiderdungeon",
					"chamber_of_wisdom_dungeon",
					"plechito_pyramide_dungeon",
					"plechito_shadow_deviltower",
					"Elendos_pvp_beta",
					"metin2_map_deviltower1",
					"plechito_andun_catacombs", )

		if background.GetCurrentMapName() in mapDict:
			return FALSE

		return TRUE

	def __XMasSnow_Enable(self, mode):

		self.__XMasSong_Enable(mode)

		if "1"==mode:

			if not self.__IsXMasMap():
				return

			print "XMAS_SNOW ON"
			background.EnableSnow(1)

		else:
			print "XMAS_SNOW OFF"
			background.EnableSnow(0)

	def __XMasBoom_Enable(self, mode):
		if "1"==mode:

			if not self.__IsXMasMap():
				return

			print "XMAS_BOOM ON"
			self.__DayMode_Update("dark")
			self.enableXMasBoom = TRUE
			self.startTimeXMasBoom = app.GetTime()
		else:
			print "XMAS_BOOM OFF"
			self.__DayMode_Update("light")
			self.enableXMasBoom = FALSE

	def __XMasTree_Enable(self, grade):

		print "XMAS_TREE ", grade
		background.SetXMasTree(int(grade))

	def __XMasSong_Enable(self, mode):
		if "1"==mode:
			print "XMAS_SONG ON"

			XMAS_BGM = "xmas.mp3"

			if app.IsExistFile("BGM/" + XMAS_BGM)==1:
				if musicInfo.fieldMusic != "":
					snd.FadeOutMusic("BGM/" + musicInfo.fieldMusic)

				musicInfo.fieldMusic=XMAS_BGM
				snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

		else:
			print "XMAS_SONG OFF"

			if musicInfo.fieldMusic != "":
				snd.FadeOutMusic("BGM/" + musicInfo.fieldMusic)

			musicInfo.fieldMusic=musicInfo.METIN2THEMA
			snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

	def __RestartDialog_Close(self):
		self.interface.CloseRestartDialog()

	def __Console_Enable(self):
		constInfo.CONSOLE_ENABLE = TRUE
		self.consoleEnable = TRUE
		app.EnableSpecialCameraMode()
		ui.EnablePaste(TRUE)

	## PrivateShop
	def __PrivateShop_Open(self):
		#self.interface.OpenPrivateShopInputNameDialog()
		self.uiNewShop.Show()
		
	def __toggleAntiexp(self):
		event.QuestButtonClick(constInfo.ANTIEXP)
		
	def __toggleStorage(self):
		event.QuestButtonClick(constInfo.STORAGEQID)
		
	def __toggleItemFinder(self):
		self.interface.ShowItemFinder()

	def BINARY_PrivateShop_Appear(self, vid, text):
		if chr.GetInstanceType(vid) in [chr.INSTANCE_TYPE_PLAYER, chr.INSTANCE_TYPE_NPC]:
			self.interface.AppearPrivateShop(vid, text)

	def BINARY_PrivateShop_Disappear(self, vid):
		self.interface.DisappearPrivateShop(vid)

	## DayMode
	def __PRESERVE_DayMode_Update(self, mode):
		if "light"==mode:
			background.SetEnvironmentData(0)
		elif "dark"==mode:

			if not self.__IsXMasMap():
				return

			background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
			background.SetEnvironmentData(1)

	def __DayMode_Update(self, mode):
		if "light"==mode:
			self.curtain.SAFE_FadeOut(self.__DayMode_OnCompleteChangeToLight)
		elif "dark"==mode:

			if not self.__IsXMasMap():
				return

			self.curtain.SAFE_FadeOut(self.__DayMode_OnCompleteChangeToDark)

	def __DayMode_OnCompleteChangeToLight(self): #reinhardt fehler skybox auch wenn man maus kann man nicht mehr bewegen wenn self.curtain.FadeIn() aus ist
		#background.SetEnvironmentData(0)
		self.curtain.FadeIn()

	def __DayMode_OnCompleteChangeToDark(self):
		background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
		background.SetEnvironmentData(1)
		self.curtain.FadeIn()

	## XMasBoom
	def __XMasBoom_Update(self):

		self.BOOM_DATA_LIST = ( (2, 5), (5, 2), (7, 3), (10, 3), (20, 5) )
		if self.indexXMasBoom >= len(self.BOOM_DATA_LIST):
			return

		boomTime = self.BOOM_DATA_LIST[self.indexXMasBoom][0]
		boomCount = self.BOOM_DATA_LIST[self.indexXMasBoom][1]

		if app.GetTime() - self.startTimeXMasBoom > boomTime:

			self.indexXMasBoom += 1

			for i in xrange(boomCount):
				self.__XMasBoom_Boom()

	def __XMasBoom_Boom(self):
		x, y, z = player.GetMainCharacterPosition()
		randX = app.GetRandom(-150, 150)
		randY = app.GetRandom(-150, 150)

		snd.PlaySound3D(x+randX, -y+randY, z, "sound/common/etc/salute.mp3")

	def __PartyRequestQuestion(self, vid):
		vid = int(vid)
		partyRequestQuestionDialog = uiCommon.QuestionDialog()
		partyRequestQuestionDialog.SetText(chr.GetNameByVID(vid) + localeInfo.PARTY_DO_YOU_ACCEPT)
		partyRequestQuestionDialog.SetAcceptText(localeInfo.UI_ACCEPT)
		partyRequestQuestionDialog.SetCancelText(localeInfo.UI_DENY)
		partyRequestQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.__AnswerPartyRequest(arg))
		partyRequestQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.__AnswerPartyRequest(arg))
		partyRequestQuestionDialog.Open()
		partyRequestQuestionDialog.vid = vid
		self.partyRequestQuestionDialog = partyRequestQuestionDialog

	def __AnswerPartyRequest(self, answer):
		if not self.partyRequestQuestionDialog:
			return

		vid = self.partyRequestQuestionDialog.vid

		if answer:
			net.SendChatPacket("/party_request_accept " + str(vid))
		else:
			net.SendChatPacket("/party_request_deny " + str(vid))

		self.partyRequestQuestionDialog.Close()
		self.partyRequestQuestionDialog = None

	def __PartyRequestDenied(self):
		self.PopupMessage(localeInfo.PARTY_REQUEST_DENIED)

	def __EnableTestServerFlag(self):
		app.EnableTestServerFlag()

	def __InGameShop_Show(self, url):
		#if constInfo.IN_GAME_SHOP_ENABLE:
		#	self.openItemshop()
		self.interface.OpenWebWindow(url)
		
		
			
	def openItemshop(self):
		#import event
		#constInfo.ITEMSHOP["questCMD"] = 'LOAD#'+str(constInfo.ITEMSHOP['tableUpdate'])
		#event.QuestButtonClick(int(constInfo.ITEMSHOP["qid"]))
		#event.QuestButtonClick(constInfo.QID_MALL)
		net.SendChatPacket("/in_game_mall")

	# WEDDING
	def __LoginLover(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLoginLover()

	def __LogoutLover(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.OnLogoutLover()
		if self.affectShower:
			self.affectShower.HideLoverState()

	def __LoverNear(self):
		if self.affectShower:
			self.affectShower.ShowLoverState()

	def __LoverFar(self):
		if self.affectShower:
			self.affectShower.HideLoverState()

	def __LoverDivorce(self):
		if self.interface.wndMessenger:
			self.interface.wndMessenger.ClearLoverInfo()
		if self.affectShower:
			self.affectShower.ClearLoverState()

	def __PlayMusic(self, flag, filename):
		flag = int(flag)
		if flag:
			snd.FadeOutAllMusic()
			musicInfo.SaveLastPlayFieldMusic()
			snd.FadeInMusic("bgm/" + filename)
		else:
			snd.FadeOutAllMusic()
			musicInfo.LoadLastPlayFieldMusic()
			snd.FadeInMusic("bgm/" + musicInfo.fieldMusic)
			
	if app.ENABLE_MELEY_LAIR_DUNGEON:
		def OpenMeleyRanking(self):
			if self.interface:
				self.interface.OpenMeleyRanking()

		def AddRankMeleyRanking(self, data):
			if self.interface:
				line = int(data.split("#")[1])
				name = str(data.split("#")[2])
				members = int(data.split("#")[3])
				seconds = int(data.split("#")[4])
				minutes = seconds // 60
				seconds %= 60
				if seconds > 0:
					time = localeInfo.TIME_MIN_SEC % (minutes, seconds)
				else:
					time = localeInfo.TIME_MIN % (minutes)
				
				self.interface.RankMeleyRanking(line, name, members, time)

	if app.ENABLE_CHANGELOOK_SYSTEM:
		def ActChangeLook(self, iAct):
			if self.interface:
				self.interface.ActChangeLook(iAct)

		def AlertChangeLook(self):
			self.PopupMessage(localeInfo.CHANGE_LOOK_DEL_ITEM)

	if app.ENABLE_SASH_SYSTEM:
		def ActSash(self, iAct, bWindow):
			if self.interface:
				self.interface.ActSash(iAct, bWindow)

		def AlertSash(self, bWindow):
			snd.PlaySound("sound/ui/make_soket.wav")
			if bWindow:
				self.PopupMessage(localeInfo.SASH_DEL_SERVEITEM)
			else:
				self.PopupMessage(localeInfo.SASH_DEL_ABSORDITEM)

	# END_OF_WEDDING


	def __nopickInfo(self):
		if constInfo.pickInfo == 0:
			constInfo.pickInfo	= 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yang in Chat On!")
		elif constInfo.pickInfo	== 1:
			constInfo.pickInfo	= 0
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Yang in Chat Off!")

	def GetInputBegin(self):
		constInfo.INPUT_IGNORE = 1
		
	def GetInputEnd(self):
		constInfo.INPUT_IGNORE = 0
	def __Inputget1(self):
		constInfo.INPUT_IGNORE = 1 

	def __Inputget2(self):
		constInfo.INPUT_IGNORE = 0

	def __Inputget3(self): 
		net.SendQuestInputStringPacket("1")

	####SHOP SYSTEM#####
	def NewShop(self):
		if self.uiNewShop:
			self.uiNewShop.Show()
	
	def ShopClear(self):
		if self.uiNewShop:
			self.uiNewShop.HideAll()
		constInfo.MyShops=[]
	def ShopCostClear(self):
		constInfo.shop_cost=[]
	def ShopCost(self,id,time,time_val,price):
		constInfo.shop_cost.append({"id":int(id),"time":int(time),"time_val":int(time_val),"price":int(price)})
	def ShopAdd(self,shop_id,shop_vid,szSign,gold,count,sold,days,date_close):
		if self.uiNewShop:
			shop={
				"id":shop_id,
				"vid":shop_vid,
				"name":szSign.replace("\\"," ").replace("_","#"),
				"gold":gold,
				"sold":sold,
				"items":int(count)-int(sold),
				"days":days,
				"time":date_close
			}
			self.uiNewShop.Load(shop)
			constInfo.MyShops.append(shop)
	def ShopItemClear(self):
		if self.uiNewShop:
			self.uiNewShop.ClearItems()
	def ShopItem(self,data):
		d=data.split("#")
		id=d[0]
		vnum=d[1]
		count=d[2]
		slot=d[3]
		price=d[4]
		if app.ENABLE_CHANGELOOK_SYSTEM:
			transmutation=d[5]
			s=d[6]
			a=d[7]
		else:
			s=d[5]
			a=d[6]
		sockets=[]
		for key in s.split("|"):
			sockets.append(int(key))
	
		attrs=[]
		for key in a.split("|"):
			a=key.split(",")
			attrs.append([int(a[1]),int(a[0])])
		if self.uiNewShop:
			if app.ENABLE_CHANGELOOK_SYSTEM:
				self.uiNewShop.AddItem(slot,{"id":id,"vnum":vnum,"count":count,"price":price,"sockets":sockets,"attrs":attrs,"transmutation":transmutation})
			else:
				self.uiNewShop.AddItem(slot,{"id":id,"vnum":vnum,"count":count,"price":price,"sockets":sockets,"attrs":attrs})
		
	####GIFT SYSTEM#####
	def gift_clear(self):
		constInfo.gift_items={}
		self.interface.ClearGift()
	if app.ENABLE_CHANGELOOK_SYSTEM:
		def gift_item(self, id, vnum, count, pos, date_add, give, reason, szSockets, szAttrs, transmutation):
			sockets=[]
			for key in szSockets.split("|"):
				sockets.append(int(key))
			attrs=[]
			for key in szAttrs.split("|"):
				a=key.split(",")
				attrs.append([int(a[0]),int(a[1])])
			constInfo.gift_items[int(pos)]={"id":int(id),"vnum":int(vnum),"count":int(count),"pos":int(pos),"date_add":int(date_add),"reason":reason.replace("_"," "),"give":give.replace("_"," "),"sockets":sockets,"attrs":attrs,"transmutation":int(transmutation)}
	else:
		def gift_item(self, id, vnum, count, pos, date_add, give, reason, szSockets, szAttrs):
			sockets=[]
			for key in szSockets.split("|"):
				sockets.append(int(key))

			attrs=[]
			for key in szAttrs.split("|"):
				a=key.split(",")
				attrs.append([int(a[0]),int(a[1])])
			constInfo.gift_items[int(pos)]={"id":int(id),"vnum":int(vnum),"count":int(count),"pos":int(pos),"date_add":int(date_add),"reason":reason.replace("_"," "),"give":give.replace("_"," "),"sockets":sockets,"attrs":attrs}
	def gift_load(self):
		self.interface.wndGiftBox.Refresh()
	def gift_show(self,pages):
		self.interface.wndGiftBox.pageNum=int(pages)
		self.interface.OpenGift()

	def __OpenDecoInterface(self):
		self.interface.OpenOfflineShopDecoration()
		
	def _ItemshopCMD(self, command):
		cmd = command.split('/')

		if cmd[0] == 'QID': ## 1 argument
			constInfo.ITEMSHOP['qid'] = int(cmd[1])
		elif cmd[0] == 'QUESTCMD':
			net.SendQuestInputStringPacket(str(constInfo.ITEMSHOP['questCMD']))
			constInfo.ITEMSHOP['questCMD'] = 'NULL#'
		elif cmd[0] == 'UPDATETABLE_SET':
			constInfo.ITEMSHOP['tableUpdate'] = cmd[1]
		elif cmd[0] == 'CLEAR_ITEMS':
			constInfo.ITEMSHOP['items']['itemshop'] = {}
			constInfo.ITEMSHOP['items']['voteshop'] = {}
			constInfo.ITEMSHOP['items']['achievementshop'] = {}
			constInfo.ITEMSHOP['items']['startpage']['mostBought'] = []
			constInfo.ITEMSHOP['items']['startpage']['hotOffers'] = []
		## fill items
		elif cmd[0] == 'CREATE_CATEGORY': ## 2 arguments, shop, categoryID
			constInfo.ITEMSHOP['items'][cmd[1]][int(cmd[2])] = []
		elif cmd[0] == 'ADD_ITEM_IS': ## category, type, id, vnum, [socket], [attr], price, percent, time, runOut
			socket = cmd[5].split(",")
			attr = cmd[6].split(",")
			constInfo.ITEMSHOP['items']['itemshop'][int(cmd[1])].append([int(cmd[2]), int(cmd[3]), [int(cmd[4]),int(socket[0]),int(socket[1]),int(socket[2]), int(attr[0]),int(attr[1]),int(attr[2]),int(attr[3]),int(attr[4]),int(attr[5]),int(attr[6]),int(attr[7]),int(attr[8]),int(attr[9]),int(attr[10]),int(attr[11]),int(attr[12]),int(attr[13])], int(cmd[7]), int(cmd[8]), int(cmd[9]), int(cmd[10])])
		elif cmd[0] == 'ADD_ITEM_VS': ## category, type, id, vnum, [socket], [attr], price, percent, time, runOut
			socket = cmd[5].split(",")
			attr = cmd[6].split(",")
			constInfo.ITEMSHOP['items']['voteshop'][int(cmd[1])].append([int(cmd[2]), int(cmd[3]), [int(cmd[4]),int(socket[0]),int(socket[1]),int(socket[2]), int(attr[0]),int(attr[1]),int(attr[2]),int(attr[3]),int(attr[4]),int(attr[5]),int(attr[6]),int(attr[7]),int(attr[8]),int(attr[9]),int(attr[10]),int(attr[11]),int(attr[12]),int(attr[13])], int(cmd[7]), int(cmd[8]), int(cmd[9]), int(cmd[10])])
		elif cmd[0] == 'ADD_ITEM_AS': ## category, type, id, vnum, [socket], [attr], price, percent, time, runOut
			socket = cmd[5].split(",")
			attr = cmd[6].split(",")
			constInfo.ITEMSHOP['items']['achievementshop'][int(cmd[1])].append([int(cmd[2]), int(cmd[3]), [int(cmd[4]),int(socket[0]),int(socket[1]),int(socket[2]), int(attr[0]),int(attr[1]),int(attr[2]),int(attr[3]),int(attr[4]),int(attr[5]),int(attr[6]),int(attr[7]),int(attr[8]),int(attr[9]),int(attr[10]),int(attr[11]),int(attr[12]),int(attr[13])], int(cmd[7]), int(cmd[8]), int(cmd[9]), int(cmd[10])])
		elif cmd[0] == 'ADD_ITEM_MOSTBOUGHT': ## type, id, vnum, [socket], [attr], price, percent, time, runOut
			socket = cmd[4].split(",")
			attr = cmd[5].split(",")
			constInfo.ITEMSHOP['items']['startpage']['mostBought'].append([int(cmd[1]), int(cmd[2]), [int(cmd[3]),int(socket[0]),int(socket[1]),int(socket[2]), int(attr[0]),int(attr[1]),int(attr[2]),int(attr[3]),int(attr[4]),int(attr[5]),int(attr[6]),int(attr[7]),int(attr[8]),int(attr[9]),int(attr[10]),int(attr[11]),int(attr[12]),int(attr[13])], int(cmd[6]), int(cmd[7]), int(cmd[8]), int(cmd[9])])
		elif cmd[0] == 'ADD_ITEM_HOTOFFERS': ## type, id, vnum, [socket], [attr], price, percent, time, runOut
			socket = cmd[4].split(",")
			attr = cmd[5].split(",")
			constInfo.ITEMSHOP['items']['startpage']['hotOffers'].append([int(cmd[1]), int(cmd[2]), [int(cmd[3]),int(socket[0]),int(socket[1]),int(socket[2]), int(attr[0]),int(attr[1]),int(attr[2]),int(attr[3]),int(attr[4]),int(attr[5]),int(attr[6]),int(attr[7]),int(attr[8]),int(attr[9]),int(attr[10]),int(attr[11]),int(attr[12]),int(attr[13])], int(cmd[6]), int(cmd[7]), int(cmd[8]), int(cmd[9])])
		elif cmd[0] == 'SET_IS_COINS':
			self.interface.Itemshop_v2.SetItemshopCoins(int(cmd[1]))
		elif cmd[0] == 'SET_VS_COINS':
			self.interface.Itemshop_v2.SetVoteshopCoins(int(cmd[1]))
		elif cmd[0] == 'SET_AS_COINS':
			self.interface.Itemshop_v2.SetAchievementshopCoins(int(cmd[1]))
		elif cmd[0] == 'OPEN':
			self.interface.Itemshop_v2.Open(int(cmd[1]), int(cmd[2]),int(cmd[3]), cmd[4], cmd[5])
		elif cmd[0] == 'LOADING':
			self.LoadingBar.SetPercent(int(cmd[1]))
			
	def test(self):
		import uilenguaje
		self.fire = uilenguaje.Dialog1()
		self.fire.Show()
	

	if app.ENABLE_SHOW_CHEST_DROP:
		def BINARY_AddChestDropInfo(self, chestVnum, pageIndex, slotIndex, itemVnum, itemCount):
			if self.interface:
				self.interface.AddChestDropInfo(chestVnum, pageIndex, slotIndex, itemVnum, itemCount)
						
		def BINARY_RefreshChestDropInfo(self, chestVnum):
			if self.interface:
				self.interface.RefreshChestDropInfo(chestVnum)
				
	def __switch_channel(self):
		'''
		import uiChannel
		a = uiChannel.ChannelChanger()
		a.Show()
		'''
		import chchanger
		chchanger.ChannelBoard().Show()
		
	def __costume_load(self, value):
		constInfo.QUEST_INDEX_06 = int(value)
		
	def costume(self, qid):
		constInfo.costume = int(qid)
		
	def costume1(self, qid):
		constInfo.costume11 = int(qid)
		
	def __pet_type_load(self, value):
		constInfo.QUEST_INDEX_PET_TYPE = int(value)
		
	def SitemFinder(self, i, item, mob, i_vnum, count, prob, actives, mob_vnum):
		mob = str(mob).replace("_", " ")
		item = str(item).replace("_", " ")
		self.interface.AppendInfoFinder(int(i), str(mob), int(prob), int(actives), int(i_vnum), int(count), str(item))
		constInfo.finder_items[int(i)]={"iMobVnum":mob_vnum}

	def SitemFinderCounter(self, count):
		constInfo.finder_counts = int(count)
		
	if app.LWT_BUFF_UPDATE:
		def __BuffiDialog_Open(self):
			if self.interface:
				self.interface.OpenBuffiDialog()

		def __BuffiDialog_Close(self):
			if self.interface:
				self.interface.CloseBuffiDialog()

		def __BuffiDialog_Costume(self, itemVnum):
			if self.interface:
				self.interface.dlgBuffiSkill.SetBuffiKostum(itemVnum)

		def __BuffiDialog_Hair(self, itemVnum):
			if self.interface:
				self.interface.dlgBuffiSkill.SetBuffiSac(itemVnum)

		def __BuffiDialog_Weapon(self, itemVnum):
			if self.interface:
				self.interface.dlgBuffiSkill.SetBuffiSilah(itemVnum)

		def __BuffiDialog_Effect(self, itemVnum):
			if self.interface:
				self.interface.dlgBuffiSkill.SetBuffiKostumEfekt(itemVnum)
				
	def __AvandosContainerLotteryCMD(self, info):
		CMD = info.split("/")
		if CMD[0]=="index":
			constInfo.AVANDOS_CONTAINER_LOTTERY["index"] = int(CMD[1])
		elif CMD[0]=="input":
			net.SendQuestInputStringPacket(str(constInfo.AVANDOS_CONTAINER_LOTTERY["CMD"]))
		elif CMD[0]=="item_vnum_list":
			constInfo.AVANDOS_CONTAINER_LOTTERY["item_vnum_list"] = []
			constInfo.AVANDOS_CONTAINER_LOTTERY["item_vnum_list"].append(CMD[1].split("|"))
		elif CMD[0]=="item_rarity_list":
			constInfo.AVANDOS_CONTAINER_LOTTERY["item_rarity_list"] = []
			constInfo.AVANDOS_CONTAINER_LOTTERY["item_rarity_list"].append(CMD[1].split("|"))
			
	if app.ENABLE_LOTTERY_SYSTEM:
		def ToggleLotteryWindow(self):
			self.interface.ToggleLotteryWindow()
			
		def __LotteryOpenWindow(self):
			self.interface.OpenLotteryWindow()
			
		def __LotteryCloseWindow(self):
			self.interface.CloseLotteryWindow()
			
		def __LotterySetLP(self, lp):
			if self.interface:
				self.interface.InitRollLP(lp)
				
	# RAINING_SYSTEM
	def __MakeRain(self):
		global makeitrain
		makeitrain = int(time.strftime("%M"))
		wndRain = uiRainSystem.uiRainSystem()
		wndRain.LoadWindow()
		self.wndRain = wndRain
	# END_OF_RAINING_SYSTEM
				
	if app.ENABLE_SWITCHBOT:
		def RefreshSwitchbotWindow(self):
			self.interface.RefreshSwitchbotWindow()
			
		def RefreshSwitchbotItem(self, slot):
			self.interface.RefreshSwitchbotItem(slot)

	def __OpenNewTestWindow(self):
		self.interface.OpenNewTestWindow()

	def __RecvTalentPointsNEW(self, current_points):
		constInfo.CURRENT_POINTS = int(current_points)

	def __RecvConstSkillUp_01(self, value):
		constInfo.SKILLUP_BUTTON[0][0] = int(value)
	
	def __RecvSkillInfoValue_01(self, skill_01_points):
		constInfo.SKILL_POINTS[0][0] = int(skill_01_points)
	
	def __RecvConstSkillLearned_01(self, value):
		constInfo.SKILL_LEARNED[0][0] = int(value)

	def __RecvConstSkillUp_02(self, value):
		constInfo.SKILLUP_BUTTON[0][1] = int(value)
	
	def __RecvSkillInfoValue_02(self, skill_02_points):
		constInfo.SKILL_POINTS[0][1] = int(skill_02_points)
	
	def __RecvConstSkillLearned_02(self, value):
		constInfo.SKILL_LEARNED[0][1] = int(value)

	def __RecvConstSkillUp_03(self, value):
		constInfo.SKILLUP_BUTTON[0][2] = int(value)
	
	def __RecvSkillInfoValue_03(self, skill_03_points):
		constInfo.SKILL_POINTS[0][2] = int(skill_03_points)
	
	def __RecvConstSkillLearned_03(self, value):
		constInfo.SKILL_LEARNED[0][2] = int(value)

	def __RecvConstSkillUp_04(self, value):
		constInfo.SKILLUP_BUTTON[0][3] = int(value)
	
	def __RecvSkillInfoValue_04(self, skill_04_points):
		constInfo.SKILL_POINTS[0][3] = int(skill_04_points)
	
	def __RecvConstSkillLearned_04(self, value):
		constInfo.SKILL_LEARNED[0][3] = int(value)

	def __RecvConstSkillUp_05(self, value):
		constInfo.SKILLUP_BUTTON[0][4] = int(value)
	
	def __RecvSkillInfoValue_05(self, skill_05_points):
		constInfo.SKILL_POINTS[0][4] = int(skill_05_points)
	
	def __RecvConstSkillLearned_05(self, value):
		constInfo.SKILL_LEARNED[0][4] = int(value)

	def __RecvConstSkillUp_06(self, value):
		constInfo.SKILLUP_BUTTON[1][0] = int(value)
	
	def __RecvSkillInfoValue_06(self, skill_06_points):
		constInfo.SKILL_POINTS[1][0] = int(skill_06_points)
	
	def __RecvConstSkillLearned_06(self, value):
		constInfo.SKILL_LEARNED[1][0] = int(value)

	def __RecvConstSkillUp_07(self, value):
		constInfo.SKILLUP_BUTTON[1][1] = int(value)
	
	def __RecvSkillInfoValue_07(self, skill_07_points):
		constInfo.SKILL_POINTS[1][1] = int(skill_07_points)
	
	def __RecvConstSkillLearned_07(self, value):
		constInfo.SKILL_LEARNED[1][1] = int(value)

	def __RecvConstSkillUp_08(self, value):
		constInfo.SKILLUP_BUTTON[1][2] = int(value)
	
	def __RecvSkillInfoValue_08(self, skill_08_points):
		constInfo.SKILL_POINTS[1][2] = int(skill_08_points)
	
	def __RecvConstSkillLearned_08(self, value):
		constInfo.SKILL_LEARNED[1][2] = int(value)

	def __RecvConstSkillUp_09(self, value):
		constInfo.SKILLUP_BUTTON[1][3] = int(value)
	
	def __RecvSkillInfoValue_09(self, skill_09_points):
		constInfo.SKILL_POINTS[1][3] = int(skill_09_points)
	
	def __RecvConstSkillLearned_09(self, value):
		constInfo.SKILL_LEARNED[1][3] = int(value)

	def __RecvConstSkillUp_10(self, value):
		constInfo.SKILLUP_BUTTON[2][0] = int(value)
	
	def __RecvSkillInfoValue_10(self, skill_10_points):
		constInfo.SKILL_POINTS[2][0] = int(skill_10_points)
	
	def __RecvConstSkillLearned_10(self, value):
		constInfo.SKILL_LEARNED[2][0] = int(value)

	def __RecvConstSkillUp_11(self, value):
		constInfo.SKILLUP_BUTTON[2][1] = int(value)
	
	def __RecvSkillInfoValue_11(self, skill_11_points):
		constInfo.SKILL_POINTS[2][1] = int(skill_11_points)
	
	def __RecvConstSkillLearned_11(self, value):
		constInfo.SKILL_LEARNED[2][1] = int(value)

	def __RecvConstSkillUp_12(self, value):
		constInfo.SKILLUP_BUTTON[2][2] = int(value)
	
	def __RecvSkillInfoValue_12(self, skill_12_points):
		constInfo.SKILL_POINTS[2][2] = int(skill_12_points)
	
	def __RecvConstSkillLearned_12(self, value):
		constInfo.SKILL_LEARNED[2][2] = int(value)

	def __RecvConstSkillUp_13(self, value):
		constInfo.SKILLUP_BUTTON[3][0] = int(value)
	
	def __RecvSkillInfoValue_13(self, skill_13_points):
		constInfo.SKILL_POINTS[3][0] = int(skill_13_points)
	
	def __RecvConstSkillLearned_13(self, value):
		constInfo.SKILL_LEARNED[3][0] = int(value)

	def __RecvConstSkillUp_14(self, value):
		constInfo.SKILLUP_BUTTON[3][1] = int(value)
	
	def __RecvSkillInfoValue_14(self, skill_14_points):
		constInfo.SKILL_POINTS[3][1] = int(skill_14_points)
	
	def __RecvConstSkillLearned_14(self, value):
		constInfo.SKILL_LEARNED[3][1] = int(value)

	def __RecvConstSkillUp_15(self, value):
		constInfo.SKILLUP_BUTTON[4][0] = int(value)
	
	def __RecvSkillInfoValue_15(self, skill_15_points):
		constInfo.SKILL_POINTS[4][0] = int(skill_15_points)
	
	def __RecvConstSkillLearned_15(self, value):
		constInfo.SKILL_LEARNED[4][0] = int(value)

	if hasattr(app, "ENABLE_DUNGEON_COOL_TIME"):
		def GetAffectList(self):
			return self.affectShower.GetAffectList()

		def SetDungeonCoolTime(self, floor, cooltime):
			self.interface.OpenDungeonCoolTimeWindow(int(floor), int(cooltime))

		def SetShadowPotionEndTime(self, endTime):
			self.interface.SetShadowPotionEndTime(int(endTime))

		def ClearDungeonCoolTime(self):
			self.interface.ClearDungeonCoolTime()

	def OpenFarmBlock(self):
		self.interface.OpenFarmBlock()
		
	def BINARY_FARM_BLOCK_REFRESH_STATES(self):
		self.interface.wndFarmBlock.OnScroll()


	if app.ENABLE_BIYOLOG:
		def SetBioData(self, level, count, time):
			self.interface.wndBio.LoadData(int(level), int(count), int(time))
		def SetBioStone(self, level):
			self.interface.wndBio.LoadStone(int(level))
		def SetBioGift(self, level):
			self.interface.wndBio.LoadGift(int(level))
		def SetBioEmpty(self):
			self.interface.wndBio.LoadEmpty()

	def AddLoopEvent(self, name, event):
		for i in self.loopList:
			if i[0] == name:
				i[1] = event
				return # already have.
		list = [name,event]
		self.loopList.append(list)
	def RemoveLoopEvent(self, name):
		for i in xrange(len(self.loopList)):
			if self.loopList[i][0] == name:
				del self.loopList[i]
				return
	def loopListEvent(self):
		for i in xrange(len(self.loopList)):
			returnValue = self.loopList[i][1]()
			if returnValue == True:
				del self.loopList[i]
	
	def BINARY_OnRecvBulkWhisper(self, content):
		content = content.replace("$", " ")
		self.interface.RegisterGameMasterName("[SYSTEM]")
		chat.AppendWhisper(chat.WHISPER_TYPE_CHAT, "[SYSTEM]", content)
		self.interface.RecvWhisper("[SYSTEM]")
		
	if app.ENABLE_SHOP_SEARCH_SYSTEM:
		def OpenPrivateShopSearch(self, type):
			if self.interface:
				self.interface.OpenPrivateShopSearch(type)
				self.interface.RefreshShopSearch()

		def ClosePrivateShopSearch(self):
			if self.interface:
				self.interface.RefreshShopSearch()
				self.interface.ClosePrivateShopSearch()

		def RefreshShopSearch(self):
			self.interface.RefreshShopSearch()

		def BuyShopSearch(self):
			self.interface.RefreshShopSearch()
			self.PopupMessage(localeInfo.PRIVATESHOPSEARCH_BUY_SUCCESS)
		def SearchMessenger(self,name):
			self.interface.OpenWhisperDialog(name)

	if constInfo.ENABLE_PROMOTION_CODE_SYSTEM:	
		def OpenPromotionCodeSystem(self):
			if self.wndPromotioncode.IsShow():
				self.wndPromotioncode.Hide()
			else:	
				self.wndPromotioncode.Show()	