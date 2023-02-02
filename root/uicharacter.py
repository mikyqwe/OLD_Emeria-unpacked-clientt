import ui
import net
import item
import skill
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import wndMgr
import player
import constInfo
import mouseModule
import uiScriptLocale
import app
import playerSettingModule
import chr
import uiToolTip
import emotion
import quest
import dbg
import game
import uitooltipGold
import snd
import apollo_interface
import uiCommon
if app.ENABLE_SKILL_COLOR_SYSTEM:
	import uiSkillColor

OnTest1 = 0
movement = 0
movement1 = 0
movement2 = 0
movement3 = 0
movement4 = 0
active = 0
SHOW_ONLY_ACTIVE_SKILL = FALSE
if localeInfo.IsYMIR():
	SHOW_LIMIT_SUPPORT_SKILL_LIST = [121, 122, 123, 124, 126, 127, 129, 128, 131, 137, 138, 139, 140,141,142]
	if not localeInfo.IsCHEONMA():
		HIDE_SUPPORT_SKILL_POINT = TRUE
		SHOW_LIMIT_SUPPORT_SKILL_LIST = [121, 122, 123, 124, 126, 127, 129, 128, 131, 137, 138, 139, 140,141,142]
if localeInfo.IsJAPAN() or   (localeInfo.IsEUROPE() and app.GetLocalePath() != "locale/ca") and (localeInfo.IsEUROPE() and app.GetLocalePath() != "locale/br"):
	HIDE_SUPPORT_SKILL_POINT = TRUE
	SHOW_LIMIT_SUPPORT_SKILL_LIST = [121, 122, 123, 124, 126, 127, 129, 128, 131, 137, 138, 139, 140]
else:
	HIDE_SUPPORT_SKILL_POINT = TRUE
HIDE_SUPPORT_SKILL_POINT = TRUE

number_on = 5
isLoaded = 0

def unsigned32(n):
	return n & 0xFFFFFFFFL

class CharacterWindow(ui.ScriptWindow):
	SKILL_GROUP_NAME_DICT = {
		playerSettingModule.JOB_WARRIOR	: { 1 : localeInfo.SKILL_GROUP_WARRIOR_1,	2 : localeInfo.SKILL_GROUP_WARRIOR_2, },
		playerSettingModule.JOB_ASSASSIN	: { 1 : localeInfo.SKILL_GROUP_ASSASSIN_1,	2 : localeInfo.SKILL_GROUP_ASSASSIN_2, },
		playerSettingModule.JOB_SURA		: { 1 : localeInfo.SKILL_GROUP_SURA_1,		2 : localeInfo.SKILL_GROUP_SURA_2, },
		playerSettingModule.JOB_SHAMAN		: { 1 : localeInfo.SKILL_GROUP_SHAMAN_1,	2 : localeInfo.SKILL_GROUP_SHAMAN_2, },
	}

	EMPIRE_NAME = {
		net.EMPIRE_A : localeInfo.EMPIRE_A,
		net.EMPIRE_B : localeInfo.EMPIRE_B,
		net.EMPIRE_C : localeInfo.EMPIRE_C
	}

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded_1 = 0
		self.guildNameValue = None
		self.toolTipSkill = 0
		self.emotionToolTip = None
		self.faceImage = None
		self.Procent = None
		self.skillPageDict = None
		self.questNameList = None
		self.questLastTimeList = None
		self.questLastCountList = None
		self.slots_button_skills = {}
		self.ACTIVE_PAGE_SLOT_COUNT = 8
		self.SUPPORT_PAGE_SLOT_COUNT = 12
		self.questShowingStartIndex = 0
		self.PAGE_SLOT_COUNT = 12
		self.curSelectedSkillGroup = 0
		self.PAGE_HORSE = 2
		self.canUseHorseSkill = -1
		self.BoardSlots = ()
		self.skillGroupButton = ()
		if app.ENABLE_SKILL_COLOR_SYSTEM:
			self.skillColorWnd = None
			self.skillColorButton = []
			
		self.statusPlusCommandDict={
			"HTH" : "/stat ht",
			"INT" : "/stat iq",
			"STR" : "/stat st",
			"DEX" : "/stat dx",
		}
		
		self.statusPlusCommandDictNew={
			"HTH" : "ht",
			"INT" : "iq",
			"STR" : "st",
			"DEX" : "dx",
		}
		
		self.skillPageStatDict = {
			"SUPPORT"	: player.SKILL_SUPPORT,
			"ACTIVE"	: player.SKILL_ACTIVE,
			"HORSE"		: player.SKILL_HORSE,
		}
		self.LoadWindow()
		self.__Initialize()

		self.ref = WaitingDialog()
		self.ref.Open(0.1)
		self.ref.SAFE_SetTimeOverEvent(self.Refreshing)


	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		global OnTest1
		OnTest1 = 0

	def __Initialize(self):
		return

	def LoadWindow(self):
		self.toolTipAlignment = uitooltipGold.ToolTip(130)
		if self.isLoaded_1 == 1:
			return

		self.isLoaded_1 = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "apollo_scripts/characterwindow.py")
		except:
			import exception
			exception.Abort("CharacterWindow.LoadWindow.LoadObject")


		try:
			self.Board = self.GetChild("board")
			self.Caracter_Input = self.GetChild("Caracter_Input")
			self.Character_Page = self.GetChild("Character_Page")
			self.TitleName = self.GetChild("TitleName")
			self.TitleBar = self.GetChild("Character_TitleBar")

			self.characterNameValue = self.GetChild("Character_Name")
			self.levelValue = self.GetChild("Level_Value")
			self.EXP = self.GetChild("Exp_Value")
			self.EXP_REST = self.GetChild("RestExp_Value")
			self.nameSlot = self.GetChild("NameSlot")
			self.guildNameValue = self.GetChild("Guild_Name")
			self.faceImage = self.GetChild("Face_Image")
			self.Procent = self.GetChild("Procent")
			self.exp_slot = self.GetChild("Exp_Full")


			self.ButtonCollapse = self.GetChild("ButtonCollapse")
			self.ButtonCollapse.SetEvent(lambda : self.InputFunctiones(1))
			self.ButtonCollapse.Hide()
			self.ButtonExpande = self.GetChild("ButtonExpande")
			self.ButtonExpande.SetEvent(lambda : self.InputFunctiones(2))
			self.ButtonExpande.Hide()
			self.Board_Caracter_Function()

			## Page Status 1
			self.FirstPage = 1

			self.Board_Status_0 = self.GetChild("Board_Status_0")
			self.Board_Status_1 = self.GetChild("Board_Status_1")
			self.Board_Status_Function()
			self.Board_Status_1.Hide()
			self.Board_Status_0.Hide()
			if self.FirstPage == 1:
				self.Board_Status_1.Show()
				self.Board_Status_0.Show()

			## Page Status 2
			self.Board_Caracteristics = self.GetChild("Board_Caracteristics")
			self.Board_Caracteristics_Function()
			self.Board_Caracteristics.Hide()

			## Page Status 3
			self.Board_Bonus_Function()

			## Page Status 4
			self.Board_Skills = self.GetChild("Board_Abilities")
			self.Board_Skills.Hide()
			self.Board_Skills_Function()

			##Page Status 5
			self.Board_Emotion = self.GetChild("Board_Emotion")
			self.Board_Emotion.Hide()
			self.Board_Emotion_Function()

			## Page Status 6
			self.Board_Quest = self.GetChild("Board_Quest")
			self.Board_Quest.Hide()
			self.Board_Quest_Function()


			self.__BindEvent()
			self.SetSize(441, 396)
			self.Board.SetSize(441, 396)
			self.SetEmpireAndGuild(net.GetEmpireID())
			self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		except:
			import exception
			exception.Abort("CharacterWindow.LoadWindow.BindObject")

	def Board_Quest_Function(self):
		self.slots_quest = ui.GridSlotWindow()
		self.slots_quest.SetParent(self.Board_Quest)
		self.slots_quest.SetPosition(9+8,39)
		self.slots_quest.ArrangeSlot(0,1,5,46,20,0,28)
		self.slots_quest.Show()

		self.ScrollBarQuest = ui.ScrollBarNewDesign()
		self.ScrollBarQuest.SetParent(self.Board_Quest)
		self.ScrollBarQuest.SetPosition(250, 40)
		self.ScrollBarQuest.SetScrollBarSize(220)
		self.ScrollBarQuest.SetScrollStep(0.6)
		self.ScrollBarQuest.SetScrollEvent(ui.__mem_func__(self.OnQuestScroll))
		self.ScrollBarQuest.Show()

		for i in xrange(quest.QUEST_MAX_NUM):
			self.slots_quest.HideSlotBaseImage(i)

		self.Slot_Quest_Name ={}
		self.Slot_Quest_Time ={}
		self.Slot_Quest_Count ={}
		number_title_e = 0
		quest_text = [
		[[9+8+70,39]],
		[[9+8+70,39+39+10]],
		[[9+8+70,39+39+10+39+4]],
		[[9+8+70,39+39+10+39+10+39+4]],
		[[9+8+70,39+39+10+39+10+39+10+39+4]]
		]

		for a in quest_text:
			self.Slot_Quest_Name[number_title_e] = ui.TextLine()
			self.Slot_Quest_Name[number_title_e].SetParent(self.Board_Quest)
			self.Slot_Quest_Name[number_title_e].SetPosition(a[0][0],a[0][1])
			self.Slot_Quest_Name[number_title_e].SetText(apollo_interface.TEXT_QUEST_1)
			self.Slot_Quest_Name[number_title_e].SetPackedFontColor(0xff81663A)
			self.Slot_Quest_Name[number_title_e].Show()

			self.Slot_Quest_Time[number_title_e] = ui.TextLine()
			self.Slot_Quest_Time[number_title_e].SetParent(self.Board_Quest)
			self.Slot_Quest_Time[number_title_e].SetPosition(a[0][0],a[0][1]+10)
			self.Slot_Quest_Time[number_title_e].SetText(apollo_interface.TEXT_QUEST_2)
			self.Slot_Quest_Time[number_title_e].SetPackedFontColor(0xff5C5351)
			self.Slot_Quest_Time[number_title_e].Show()

			self.Slot_Quest_Count[number_title_e] = ui.TextLine()
			self.Slot_Quest_Count[number_title_e].SetParent(self.Board_Quest)
			self.Slot_Quest_Count[number_title_e].SetPosition(a[0][0],a[0][1]+20)
			self.Slot_Quest_Count[number_title_e].SetText(apollo_interface.TEXT_QUEST_3)
			self.Slot_Quest_Count[number_title_e].SetPackedFontColor(0xff5C5351)
			self.Slot_Quest_Count[number_title_e].Show()

			number_title_e +=1

		self.questNameList = []
		self.questLastTimeList = []
		self.questLastCountList =[]
		self.questShowingStartIndex = 0
		for i in xrange(quest.QUEST_MAX_NUM):
			self.questNameList.append(self.Slot_Quest_Name[i])
			self.questLastTimeList.append(self.Slot_Quest_Time[i])
			self.questLastCountList.append(self.Slot_Quest_Count[i])

	def Board_Emotion_Function(self):
		slot_etc = [
		[[1,1+3+4,83,40,40]],
		[[21,1+40+1+3+4,83,40,40]],
		[[41,1+40+40+1+1+3+4,83,40,40]],

		#[[3,1+3+4,1+40+1+82,40,40]],
		#[[23,1+40+1+3+4,1+40+1+82,40,40]],
		#[[43,1+40+40+1+1+3+4,1+40+1+82,40,40]],
		#
		#[[2,1+130,83,40,40]],
		#[[22,1+130+40+1,83,40,40]],
		#[[42,1+130+40+40+1+1,83,40,40]],
		#
		#[[4,1+130,1+40+1+83,40,40]],
		#[[24,1+130+40+1,1+40+1+83,40,40]],
		#[[44,1+130+40+40+1+1,1+40+1+83,40,40]],

		]
		slots_1 =[
		[[1,1+3+4,83,40,40]],
		[[21,1+40+1+3+4,83,40,40]],
		[[41,1+40+40+1+1+3+4,83,40,40]],

		[[3,1+3+4,1+40+1+82,40,40]],
		[[23,1+40+1+3+4,1+40+1+82,40,40]],
		[[43,1+40+40+1+1+3+4,1+40+1+82,40,40]],

		[[5,1+3+4,1+40+1+40+1+82,40,40]],
		[[25,1+40+1+3+4,1+40+1+40+1+82,40,40]],
		[[45,1+40+40+1+1+3+4,1+40+1+40+1+82,40,40]],

		[[2,1+130,83,40,40]],
		[[22,1+130+40+1,83,40,40]],
		[[42,1+130+40+40+1+1,83,40,40]],

		[[4,1+130,1+40+1+83,40,40]],
		[[24,1+130+40+1,1+40+1+83,40,40]],
		[[44,1+130+40+40+1+1,1+40+1+83,40,40]],

		[[6,1+130,1+40+1+40+1+83,40,40]],
		[[26,1+130+40+1,1+40+1+40+1+83,40,40]],
		[[46,1+130+40+40+1+1,1+40+1+40+1+83,40,40]]
		]

		number_title_e = 0
		self.Slot_Image_Emotion ={}
		self.Slot_Image_Emotion_2 ={}
		for a in slots_1:
			self.Slot_Image_Emotion[number_title_e] = ui.ImageBox()
			self.Slot_Image_Emotion[number_title_e].SetParent(self.Board_Emotion)
			self.Slot_Image_Emotion[number_title_e].SetPosition(a[0][1]+5,a[0][2]-48)
			self.Slot_Image_Emotion[number_title_e].LoadImage(apollo_interface.PATCH_COMMON+"/slot_ellipse/slot.png")
			self.Slot_Image_Emotion[number_title_e].Show()
			number_title_e +=1

		for a in slot_etc:
			self.Slot_Image_Emotion_2[number_title_e] = ui.ImageBox()
			self.Slot_Image_Emotion_2[number_title_e].SetParent(self.Board_Emotion)
			self.Slot_Image_Emotion_2[number_title_e].SetPosition(a[0][1]+5,a[0][2]+105)
			self.Slot_Image_Emotion_2[number_title_e].LoadImage(apollo_interface.PATCH_COMMON+"/slot_ellipse/slot.png")
			self.Slot_Image_Emotion_2[number_title_e].Show()
			number_title_e +=1
			
		self.itemslot4 = ui.GridSlotWindow()
		self.itemslot4.SetParent(self.Board_Emotion)
		self.itemslot4.SetPosition(9+8,39)
		self.itemslot4.ArrangeSlot(1,6,3,36,37,5,4)
		self.itemslot4.Show()

		self.itemslot5 = ui.GridSlotWindow()
		self.itemslot5.SetParent(self.Board_Emotion)
		self.itemslot5.SetPosition(9+8,39+150+3)
		self.itemslot5.ArrangeSlot(51,3,1,36,37,5,4)
		self.itemslot5.Show()
		
		if app.ENABLE_NEW_EMOTION_SYSTEM:
			slot_3 = [
				[[1,1+3+4,83,40,40]],
				[[21,1+40+1+3+4,83,40,40]],
				[[41,1+40+40+1+1+3+4,83,40,40]],

				[[3,1+3+4,1+40+1+82,40,40]],
				[[23,1+40+1+3+4,1+40+1+82,40,40]],
				[[43,1+40+40+1+1+3+4,1+40+1+82,40,40]],

				[[5,1+3+4,1+40+1+40+1+82,40,40]],
				[[25,1+40+1+3+4,1+40+1+40+1+82,40,40]],
				[[45,1+40+40+1+1+3+4,1+40+1+40+1+82,40,40]],

				[[2,1+130,83,40,40]],
				[[22,1+130+40+1,83,40,40]],
				[[42,1+130+40+40+1+1,83,40,40]],

				[[4,1+130,1+40+1+83,40,40]],
				[[24,1+130+40+1,1+40+1+83,40,40]],
				[[44,1+130+40+40+1+1,1+40+1+83,40,40]],
			]
			
			number_title_e = 0
			self.Slot_Image_Emotion_3 ={}
			for a in slot_3:
				self.Slot_Image_Emotion_3[number_title_e] = ui.ImageBox()
				self.Slot_Image_Emotion_3[number_title_e].SetParent(self.Board_Emotion)
				self.Slot_Image_Emotion_3[number_title_e].SetPosition(a[0][1]+5,a[0][2]+173) # Slot Emotionen verschieben wegen Kreis machen
				self.Slot_Image_Emotion_3[number_title_e].LoadImage(apollo_interface.PATCH_COMMON+"/slot_ellipse/slot.png")
				self.Slot_Image_Emotion_3[number_title_e].Show()
				number_title_e +=1
			
			self.specialEmotionSlot = ui.GridSlotWindow()
			self.specialEmotionSlot.SetParent(self.Board_Emotion)
			self.specialEmotionSlot.SetPosition(17, 260)
			self.specialEmotionSlot.ArrangeSlot(60,6,3,36,37,5,4)
			self.specialEmotionSlot.Show()
		
		self.__SetEmotionSlot()

	def __SetEmotionSlot(self):

		if app.ENABLE_NEW_EMOTION_SYSTEM:	
			slots_new = (self.itemslot4, self.itemslot5, self.specialEmotionSlot)
		else:
			slots_new = (self.itemslot4, self.itemslot5)	
			
		for slot in slots_new:
			self.emotionToolTip = uiToolTip.ToolTip()

			slot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
			slot.SetSelectItemSlotEvent(ui.__mem_func__(self.__SelectEmotion))
			slot.SetUnselectItemSlotEvent(ui.__mem_func__(self.__ClickEmotionSlot))
			slot.SetUseSlotEvent(ui.__mem_func__(self.__ClickEmotionSlot))
			slot.SetOverInItemEvent(ui.__mem_func__(self.__OverInEmotion))
			slot.SetOverOutItemEvent(ui.__mem_func__(self.__OverOutEmotion))
			slot.AppendSlotButton("d:/ymir work/ui/game/windows/btn_plus_up.sub",\
											"d:/ymir work/ui/game/windows/btn_plus_over.sub",\
											"d:/ymir work/ui/game/windows/btn_plus_down.sub")

		for slotIdx, datadict in emotion.EMOTION_DICT.items():
			emotionIdx = slotIdx

			slot = self.itemslot4

			if slotIdx > 50:
				slot = self.itemslot5

			if app.ENABLE_NEW_EMOTION_SYSTEM:	
				if slotIdx >= 60:
					slot = self.specialEmotionSlot
					
			slot.SetEmotionSlot(slotIdx, emotionIdx)
			slot.SetCoverButton(slotIdx)

	def __SelectEmotion(self, slotIndex):
		if not slotIndex in emotion.EMOTION_DICT:
			return

		if app.IsPressed(app.DIK_LCONTROL):
			player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_EMOTION, slotIndex)
			return
			
		mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_EMOTION, slotIndex, slotIndex)

	def __ClickEmotionSlot(self, slotIndex):
		print "click emotion"
		if not slotIndex in emotion.EMOTION_DICT:
			return

		print "check acting"
		if player.IsActingEmotion():
			return

		command = emotion.EMOTION_DICT[slotIndex]["command"]
		print "command", command

		if app.ENABLE_NEW_EMOTION_SYSTEM:
			if (slotIndex > 50 and slotIndex < 60) or slotIndex > 70:
				vid = player.GetTargetVID()

				if 0 == vid or vid == player.GetMainCharacterIndex() or chr.IsNPC(vid) or chr.IsEnemy(vid):
					import chat
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EMOTION_CHOOSE_ONE)
					return

				command += " " + chr.GetNameByVID(vid)
		else:
			if slotIndex > 50:
				vid = player.GetTargetVID()

				if 0 == vid or vid == player.GetMainCharacterIndex() or chr.IsNPC(vid) or chr.IsEnemy(vid):
					import chat
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EMOTION_CHOOSE_ONE)
					return

				command += " " + chr.GetNameByVID(vid)

		print "send_command", command
		net.SendChatPacket(command)


	def Board_Skills_Function(self):
		slot_etc = [
		[[1,1+3+4,83,40,40]],
		[[21,1+40+1+3+4,83,40,40]],
		[[41,1+40+40+1+1+3+4,83,40,40]],

		[[3,1+3+4,1+40+1+82,40,40]],
		[[23,1+40+1+3+4,1+40+1+82,40,40]],
		[[43,1+40+40+1+1+3+4,1+40+1+82,40,40]],

		[[2,1+130,83,40,40]],
		[[22,1+130+40+1,83,40,40]],
		[[42,1+130+40+40+1+1,83,40,40]],

		[[4,1+130,1+40+1+83,40,40]],
		[[24,1+130+40+1,1+40+1+83,40,40]],
		[[44,1+130+40+40+1+1,1+40+1+83,40,40]],

		]
		slots_1 =[
		[[1,1+3,1,40,40]],
		[[21,1+40+1+3,1,40,40]],
		[[41,1+40+40+1+1+3,1,40,40]],

		[[3,1+3,1+40+1,40,40]],
		[[23,1+40+1+3,1+40+1,40,40]],
		[[43,1+40+40+1+1+3,1+40+1,40,40]],

		[[5,1+3,1+40+1+40+1,40,40]],
		[[25,1+40+1+3,1+40+1+40+1,40,40]],
		[[45,1+40+40+1+1+3,1+40+1+40+1,40,40]]



		]
		slots_2 =[
		[[2,1+130+3,1,40,40]],
		[[22,1+130+40+1+3,1,40,40]],
		[[42,1+130+40+40+1+1+3,1,40,40]],

		[[4,1+130+3,1+40+1,40,40]],
		[[24,1+130+40+1+3,1+40+1,40,40]],
		[[44,1+130+40+40+1+1+3,1+40+1,40,40]],

		[[6,1+130+3,1+40+1+40+1,40,40]],
		[[26,1+130+40+1+3,1+40+1+40+1,40,40]],
		[[46,1+130+40+40+1+1+3,1+40+1+40+1,40,40]]
		]

		self.Slot_Image ={}
		self.Slot_Image_1 ={}
		self.Slot_Image_2 = {}
		self.S_Slot_Button_2 ={}
		number_title_s_2 = 0
		for a in slots_1:
			self.Slot_Image[number_title_s_2] = ui.ImageBox()
			self.Slot_Image[number_title_s_2].SetParent(self.Board_Skills)
			self.Slot_Image[number_title_s_2].SetPosition(a[0][1]+5,a[0][2]+35)
			self.Slot_Image[number_title_s_2].LoadImage(apollo_interface.PATCH_COMMON+"/slot_ellipse/slot.png")
			self.Slot_Image[number_title_s_2].Show()
			number_title_s_2 +=1

		for e in slots_2:
			self.Slot_Image_1[number_title_s_2] = ui.ImageBox()
			self.Slot_Image_1[number_title_s_2].SetParent(self.Board_Skills)
			self.Slot_Image_1[number_title_s_2].SetPosition(e[0][1]+5,e[0][2]+35)
			self.Slot_Image_1[number_title_s_2].LoadImage(apollo_interface.PATCH_COMMON+"/slot_ellipse/slot.png")
			self.Slot_Image_1[number_title_s_2].Show()
			number_title_s_2 +=1


		self.itemslot1 = ui.SlotWindow()
		self.itemslot1.SetParent(self.Board_Skills)
		self.itemslot1.SetSize(400,200)
		self.itemslot1.SetPosition(9, 39)
		self.itemslot1.Show()


		for s in slots_1:
			self.itemslot1.AppendSlot(s[0][0], s[0][1], s[0][2], s[0][3],s[0][4])
		for s_1 in slots_2:
			self.itemslot1.AppendSlot(s_1[0][0], s_1[0][1], s_1[0][2], s_1[0][3],s_1[0][4])

		for a in slot_etc:
			self.Slot_Image_2[number_title_s_2] = ui.ImageBox()
			self.Slot_Image_2[number_title_s_2].SetParent(self.Board_Skills)
			self.Slot_Image_2[number_title_s_2].SetPosition(a[0][1]+5,a[0][2]+105)
			self.Slot_Image_2[number_title_s_2].LoadImage(apollo_interface.PATCH_COMMON+"/slot_ellipse/slot.png")
			self.Slot_Image_2[number_title_s_2].Show()
			number_title_s_2 +=1

		self.slots_button_skills = {}
		self.slot_skill_name = {}
		number_title_e = 0
		slot_etc_1 =[
		[[30,7],[apollo_interface.SKILL_BUTTON_1]],
		[[2+225,7],[apollo_interface.SKILL_BUTTON_2]]
		]

		for ed in slot_etc_1:
			self.slots_button_skills[number_title_e] = ui.RadioButton()
			self.slots_button_skills[number_title_e].SetParent(self.Board_Skills)
			self.slots_button_skills[number_title_e].SetPosition(ed[0][0],ed[0][1])
			self.slots_button_skills[number_title_e].SetUpVisual(apollo_interface.PATCH_BUTTONS+"/titlebar_%d_normal.png" % number_title_e)
			self.slots_button_skills[number_title_e].SetOverVisual(apollo_interface.PATCH_BUTTONS+"/titlebar_%d_hover.png" % number_title_e)
			self.slots_button_skills[number_title_e].SetDownVisual(apollo_interface.PATCH_BUTTONS+"/titlebar_%d_active.png" % number_title_e)
			# self.slots_button_skills[number_title_e].SetText(ed[1][0])
			self.slots_button_skills[number_title_e].Show()

			self.slot_skill_name[number_title_e] = ui.TextLine()
			self.slot_skill_name[number_title_e].SetParent(self.Board_Skills)
			self.slot_skill_name[number_title_e].SetPosition(70/2+95,8)
			self.slot_skill_name[number_title_e].SetText(ed[1][0])
			self.slot_skill_name[number_title_e].SetHorizontalAlignCenter()
			self.slot_skill_name[number_title_e].SetPackedFontColor(0xffcaa76f)

			number_title_e +=1

		self.itemslot2 = ui.GridSlotWindow()
		self.itemslot2.SetParent(self.Board_Skills)
		self.itemslot2.SetPosition(9+8,39+150+3)
		self.itemslot2.ArrangeSlot(101,6,2,36,37,5,4)
		self.itemslot2.Show()

		self.status_abilities = ui.TextLine()
		self.status_abilities.SetParent(self.Board_Skills)
		self.status_abilities.SetPosition(160/2+95,8)
		self.status_abilities.SetText("|cffa07970| |cfff8d0900 |cffa07970|") #|cffa08784%s|cffcaa76f +%s|cffa08784 f8d090
		#self.status_abilities.SetPackedFontColor(0xffa07970)
		self.status_abilities.SetHorizontalAlignCenter()
		self.status_abilities.Show()


		self.skillPageDict = {
			"ACTIVE" : self.itemslot1,
			"SUPPORT" : self.itemslot2,
			"HORSE" : self.itemslot1,
		}
		self.skillGroupButton = (
			self.slots_button_skills[0],
			self.slots_button_skills[1],
		)


	def Board_Bonus_Function(self):
		self.Board_Bonus ={}
		self.Board_Bonus_Slot ={}
		self.Board_Bonus_Image ={}
		self.Board_Bonus_Expander ={}
		self.Board_Bonus_Title ={}
		self.Board_Bonus_Search ={}
		number_title_b = 0
		info_b =[
		[[8,113],[apollo_interface.OFENSIVE_BONUSES]],
		[[8,45+113],[apollo_interface.DEFENSIVE_BONUSES]],
		[[8,45+49-4+113],[apollo_interface.OTHER_BONUSES]]
		]
		for e in info_b:
			self.Board_Bonus[number_title_b] = ui.NewBoard()
			self.Board_Bonus[number_title_b].SetParent(self)
			self.Board_Bonus[number_title_b].SetPosition(e[0][0],e[0][1])
			self.Board_Bonus[number_title_b].SetSize(272,34-5)
			self.Board_Bonus[number_title_b].Hide()

			self.Board_Bonus_Image[number_title_b] = ui.ImageBox()
			self.Board_Bonus_Image[number_title_b].SetParent(self.Board_Bonus[number_title_b])
			self.Board_Bonus_Image[number_title_b].SetPosition(6,5)
			self.Board_Bonus_Image[number_title_b].LoadImage(apollo_interface.PATCH_SPECIAL + "/character/line.png")
			self.Board_Bonus_Image[number_title_b].Show()

			self.Board_Bonus_Expander[number_title_b] = ui.Button()
			self.Board_Bonus_Expander[number_title_b].SetParent(self.Board_Bonus_Image[number_title_b])
			self.Board_Bonus_Expander[number_title_b].SetPosition(6,5)
			self.Board_Bonus_Expander[number_title_b].SetUpVisual(apollo_interface.PATCH_SPECIAL + "/character/boni_search_01_normal.png")
			self.Board_Bonus_Expander[number_title_b].SetOverVisual(apollo_interface.PATCH_SPECIAL + "/character/boni_search_02_hover.png")
			self.Board_Bonus_Expander[number_title_b].SetDownVisual(apollo_interface.PATCH_SPECIAL + "/character/boni_search_03_active.png")
			self.Board_Bonus_Expander[number_title_b].Show()

			self.Board_Bonus_Title[number_title_b] = ui.TextLine()
			self.Board_Bonus_Title[number_title_b].SetParent(self.Board_Bonus_Image[number_title_b])
			self.Board_Bonus_Title[number_title_b].SetPosition(48,12)
			self.Board_Bonus_Title[number_title_b].SetText(e[1][0])
			self.Board_Bonus_Title[number_title_b].SetPackedFontColor(0xffe6d0a2)
			self.Board_Bonus_Title[number_title_b].Show()

			number_title_b += 1

		self.Board_Bonus_s = ui.NewBoard()
		self.Board_Bonus_s.SetParent(self.Board_Bonus[0])
		self.Board_Bonus_s.SetPosition(0,135)
		self.Board_Bonus_s.SetSize(272,136)
		self.Board_Bonus_s.Show()

		self.Board_Bonus_Expander[0].SetEvent(lambda : self.Expander_Bonus_Functiones(0)) # 0-2 =1 , 1-1 =2 ,2 = 3
		self.Board_Bonus_Expander[1].SetEvent(lambda : self.Expander_Bonus_Functiones(1)) # 0-2 =1 , 1-1 =2 ,2 = 3
		self.Board_Bonus_Expander[2].SetEvent(lambda : self.Expander_Bonus_Functiones(2)) # 0-2 =1 , 1-1 =2 ,2 = 3

	def Expander_Bonus_Functiones(self,number):
		global active
		self.ContentBonus(number,active)
		if number == 0:
			if active == 0:
				self.Board_Bonus[number].SetSize(272,20+165)
				self.Board_Bonus[1].SetPosition(8,223-38+113)
				self.Board_Bonus[2].SetPosition(8,256-27+113)
				self.Board_Bonus_s.Hide()
				active = 1
			else:
				self.Board_Bonus[number].SetSize(272,34)
				self.Board_Bonus[1].SetSize(272,25-5)
				self.Board_Bonus[1].SetPosition(8,10+37-2+113)
				self.Board_Bonus[2].SetSize(272,34-5)
				self.Board_Bonus[2].SetPosition(8,20+37+37-4+113)
				self.Board_Bonus_s.Show()
				active = 0

		if number == 1:
			if active == 0:
				self.Board_Bonus[number].SetSize(272,20+165)
				self.Board_Bonus[2].SetPosition(8,257-27+113)
				self.Board_Bonus_s.Hide()
				active = 1
			else:
				self.Board_Bonus[number].SetSize(272,34-5)
				self.Board_Bonus[number].SetPosition(8,12+37-4+113)
				self.Board_Bonus[0].SetSize(272,34-5)
				self.Board_Bonus[2].SetSize(272,34-5)
				self.Board_Bonus[2].SetPosition(8,20+37+37-4+113)
				self.Board_Bonus_s.Show()
				active = 0
		if number == 2:
			if active == 0:
				self.Board_Bonus[number].SetSize(272,20+165)
				self.Board_Bonus[2].SetPosition(8,20+37+37-4+113)
				self.Board_Bonus_s.Hide()
				active = 1
			else:
				self.Board_Bonus[number].SetSize(272,34-5)
				self.Board_Bonus[number].SetPosition(8,12+37-4+113)
				self.Board_Bonus[0].SetSize(272,34-5)
				self.Board_Bonus[2].SetSize(272,34-5)
				self.Board_Bonus[2].SetPosition(8,20+37+37-4+113)
				self.Board_Bonus_s.Show()
				active = 0

	def ContentBonus(self,number,activacion):
		global isLoaded
		self.fileListBox = ui.ListBoxEx()
		self.fileListBox.SetParent(self.Board_Bonus[number])
		self.fileListBox.SetPosition(15, 45)
		# self.fileListBox.RemoveBonus()
		self.fileListBox.SetViewItemCount(7)
		self.fileListBox.Show()

		self.ScrollBar = ui.ScrollBarNewDesign()
		self.ScrollBar.SetParent(self.Board_Bonus[number])
		self.ScrollBar.SetPosition(250, 45)
		self.ScrollBar.SetScrollBarSize(137)
		self.ScrollBar.SetScrollStep(0.6)
		#self.ScrollBar.Show()

		self.fileListBox.SetScrollBar(self.ScrollBar)
		self.ContenidoBonus(number)
		self.ContenidoBonus1()


		if activacion == 0:
			isLoaded = 1
			self.fileListBox.Show()
			self.ScrollBar.Show()
		else:
			isLoaded = 0
			self.fileListBox.Hide()
			self.ScrollBar.Hide()

	def ContenidoBonus(self,number):
		global number_on
		number_on = number

	def InputFunctiones(self,number):
		global movement
		global movement1
		global movement2
		global movement3
		global movement4
		global OnTest1
		movement = 0
		movement1 = 0
		movement2 = 0
		movement3 = 0
		movement4 = 0
		if number == 1:
			OnTest1 = number
			self.ButtonCollapse.Hide()
		else:
			OnTest1 = number
			self.ButtonExpande.Hide()

	def Board_Caracter_Function(self):
		self.BoardSlot = {}
		self.BoardSlots_Image = {}
		self.BoardSlots_Button={}
		self.BoardSlots_Text ={}
		number_title_c_f = 0
		info_c_f =[
		[[1,2,apollo_interface.PAGE_TEXT_1]],
		[[1,34,apollo_interface.PAGE_TEXT_2]],
		[[1,34+34,apollo_interface.PAGE_TEXT_3]],
		[[1,34+34+34,apollo_interface.PAGE_TEXT_4]],
		[[1,34+34+34+34,apollo_interface.PAGE_TEXT_5]],
		[[1,34+34+34+34+34,apollo_interface.PAGE_TEXT_7]]
		]
		for d in info_c_f:
			self.BoardSlot[number_title_c_f] = ui.BoardSlot()
			self.BoardSlot[number_title_c_f].SetParent(self.Caracter_Input)
			self.BoardSlot[number_title_c_f].SetPosition(d[0][0]+6,d[0][1])
			self.BoardSlot[number_title_c_f].MakeTitleBar(150-110)
			self.BoardSlot[number_title_c_f].Show()

			self.BoardSlots_Image[number_title_c_f] = ui.ImageBox()
			self.BoardSlots_Image[number_title_c_f].SetParent(self.BoardSlot[number_title_c_f])
			self.BoardSlots_Image[number_title_c_f].SetPosition(1,0)
			self.BoardSlots_Image[number_title_c_f].LoadImage(apollo_interface.PATCH_COMMON+"/list_item_menu/arrow_bg.png")
			self.BoardSlots_Image[number_title_c_f].Show()
			self.BoardSlots_Image[number_title_c_f].SetTop()

			self.BoardSlots_Button[number_title_c_f] = ui.RadioButton()
			self.BoardSlots_Button[number_title_c_f].SetParent(self.BoardSlots_Image[number_title_c_f])
			self.BoardSlots_Button[number_title_c_f].SetPosition(7,7)
			self.BoardSlots_Button[number_title_c_f].SetUpVisual(apollo_interface.PATCH_COMMON+"/list_item_menu/arrow_empty.png")
			self.BoardSlots_Button[number_title_c_f].SetOverVisual(apollo_interface.PATCH_COMMON+"/list_item_menu/arrow_filled.png")
			self.BoardSlots_Button[number_title_c_f].SetDownVisual(apollo_interface.PATCH_COMMON+"/list_item_menu/arrow_filled.png")
			self.BoardSlots_Button[number_title_c_f].Show()

			self.BoardSlots_Text[number_title_c_f] = ui.TextLine()
			self.BoardSlots_Text[number_title_c_f].SetParent(self.Caracter_Input)
			self.BoardSlots_Text[number_title_c_f].SetPosition(d[0][0]+40+4,d[0][1]+8)
			self.BoardSlots_Text[number_title_c_f].SetText(d[0][2])
			self.BoardSlots_Text[number_title_c_f].SetPackedFontColor(0xff6c5654)
			self.BoardSlots_Text[number_title_c_f].Show()

			number_title_c_f += 1

		self.BoardSlots = (
			self.BoardSlots_Button[0],
			self.BoardSlots_Button[1],
			self.BoardSlots_Button[2],
			self.BoardSlots_Button[3],
			self.BoardSlots_Button[4],
			self.BoardSlots_Button[5],
			
		)
		self.BoardSlots_1 = (
			self.BoardSlots_Text[0],
			self.BoardSlots_Text[1],
			self.BoardSlots_Text[2],
			self.BoardSlots_Text[3],
			self.BoardSlots_Text[4],
			self.BoardSlots_Text[5],
			
		)


		self.BoardSlots_Button[0].SetEvent((lambda : self.OpenEvents(0)))
		self.BoardSlots_Button[0].Down()
		self.BoardSlots_Text[0].SetPackedFontColor(0xffe6d0a2)
		self.BoardSlots_Button[1].SetEvent((lambda : self.OpenEvents(1)))
		self.BoardSlots_Button[2].SetEvent((lambda : self.OpenEvents(2)))
		self.BoardSlots_Button[3].SetEvent((lambda : self.OpenEvents(3)))
		self.BoardSlots_Button[4].SetEvent((lambda : self.OpenEvents(4)))
		self.BoardSlots_Button[5].SetEvent((lambda : self.OpenEvents(5)))

	def OpenEvents(self,number):
		for btn in self.BoardSlots:
			btn.SetUp()
			for ex in self.BoardSlots_1:
				ex.SetPackedFontColor(0xff6c5654)
		self.BoardSlots[number].Down()
		self.BoardSlots_1[number].SetPackedFontColor(0xffe6d0a2)

		if app.ENABLE_NEW_EMOTION_SYSTEM:
			if number != 4:
				self.SetSize(441, 396)
				self.Board.SetSize(441, 396)
				self.Caracter_Input.SetSize(143,350)

				
		if number == 0:
			if self.Board_Status_1.IsShow() and self.Board_Status_0.IsShow():
				return
			else:
				self.Board_Status_1.Show()
				self.Board_Status_0.Show()
			self.Board_Caracteristics.Hide()
			self.Board_Bonus[0].Hide()
			self.Board_Bonus[1].Hide()
			self.Board_Bonus[2].Hide()
			self.Board_Skills.Hide()
			self.Board_Emotion.Hide()
			self.Board_Quest.Hide()
			
		if number == 1:
			self.Board_Caracteristics.Show()
			self.Board_Status_1.Hide()
			self.Board_Status_0.Hide()
			self.Board_Bonus[0].Hide()
			self.Board_Bonus[1].Hide()
			self.Board_Bonus[2].Hide()
			self.Board_Skills.Hide()
			self.Board_Emotion.Hide()
			self.Board_Quest.Hide()
			

		if number == 2:
			self.Board_Bonus[0].Show()
			self.Board_Bonus[1].Show()
			self.Board_Bonus[2].Show()
			self.Board_Status_1.Hide()
			self.Board_Status_0.Hide()
			self.Board_Caracteristics.Hide()
			self.Board_Skills.Hide()
			self.Board_Emotion.Hide()
			self.Board_Quest.Hide()
			
		if number == 3:
			self.Board_Skills.Show()
			self.Board_Bonus[0].Hide()
			self.Board_Bonus[1].Hide()
			self.Board_Bonus[2].Hide()
			self.Board_Status_1.Hide()
			self.Board_Status_0.Hide()
			self.Board_Caracteristics.Hide()
			self.Board_Emotion.Hide()
			self.Board_Quest.Hide()
			

		if number == 4:
			if app.ENABLE_NEW_EMOTION_SYSTEM:
				self.SetSize(441, 396 + 110)
				self.Board.SetSize(441, 396 + 110)
				self.Board_Emotion.SetSize(271, 273 + 110)
				self.Caracter_Input.SetSize(143,458)
			
			self.Board_Emotion.Show()
			
			self.Board_Skills.Hide()
			self.Board_Bonus[0].Hide()
			self.Board_Bonus[1].Hide()
			self.Board_Bonus[2].Hide()
			self.Board_Status_1.Hide()
			self.Board_Status_0.Hide()
			self.Board_Caracteristics.Hide()
			self.Board_Quest.Hide()
		
		if number == 5:
			self.Board_Quest.Show()
			self.Board_Emotion.Hide()
			self.Board_Skills.Hide()
			self.Board_Bonus[0].Hide()
			self.Board_Bonus[1].Hide()
			self.Board_Bonus[2].Hide()
			self.Board_Status_1.Hide()
			self.Board_Status_0.Hide()
			self.Board_Caracteristics.Hide()
		
	def Board_Status_Function(self):
		self.S_Title = {}
		self.S_Title_1 = {}
		self.S_Slot = {}
		self.S_Slot_1 = {}
		self.S_Slot_Number = {}
		self.S_Slot_Number_1 = {}
		self.S_Slot_Button_1 = {}
		number_title_s = 0
		number_title_s_1 = 0

		info_s =[
		[[45,45],	[apollo_interface.NAME_HP]],
		[[45,45+30],[apollo_interface.NAME_SP]]
		]
		info_s_1 =[
		[[45,40],	[apollo_interface.NAME_VIT]],
		[[45,40+30],	[apollo_interface.NAME_INT]],
		[[45,40+30+30],	[apollo_interface.NAME_STR]],
		[[45,40+30+30+30],[apollo_interface.NAME_DEX]]
		]

		self.Status_Plus_Value = ui.TextLine()
		self.Status_Plus_Value.SetParent(self.Board_Status_1)
		self.Status_Plus_Value.SetPosition(271/2+52,8)
		self.Status_Plus_Value.SetText("220")
		self.Status_Plus_Value.SetPackedFontColor(0xfff8d090)
		self.Status_Plus_Value.Show()

		for b in info_s:
			self.S_Title[number_title_s] = ui.TextLine()
			self.S_Title[number_title_s].SetParent(self.Board_Status_0)
			self.S_Title[number_title_s].SetPosition(b[0][0],b[0][1])
			self.S_Title[number_title_s].SetText(b[1][0])
			self.S_Title[number_title_s].SetPackedFontColor(0xffa08784)
			self.S_Title[number_title_s].Show()

			self.S_Slot[number_title_s] = ui.InputNew()
			self.S_Slot[number_title_s].SetParent(self.Board_Status_0)
			self.S_Slot[number_title_s].SetPosition(b[0][0]+100,b[0][1]-5)
			self.S_Slot[number_title_s].MakeTitleBar(90)
			self.S_Slot[number_title_s].Show()

			self.S_Slot_Number[number_title_s] = ui.TextLine()
			self.S_Slot_Number[number_title_s].SetParent(self.S_Slot[number_title_s])
			self.S_Slot_Number[number_title_s].SetPosition(46-5,7)
			self.S_Slot_Number[number_title_s].SetText("90000/90000")
			self.S_Slot_Number[number_title_s].SetHorizontalAlignCenter()
			self.S_Slot_Number[number_title_s].SetPackedFontColor(0xffa07970)
			self.S_Slot_Number[number_title_s].Show()
			number_title_s +=1

		for c in info_s_1:
			self.S_Title_1[number_title_s_1] = ui.TextLine()
			self.S_Title_1[number_title_s_1].SetParent(self.Board_Status_1)
			self.S_Title_1[number_title_s_1].SetPosition(c[0][0],c[0][1])
			self.S_Title_1[number_title_s_1].SetText(c[1][0])
			self.S_Title_1[number_title_s_1].SetPackedFontColor(0xffa08784)
			self.S_Title_1[number_title_s_1].Show()

			self.S_Slot_1[number_title_s_1] = ui.InputNew()
			self.S_Slot_1[number_title_s_1].SetParent(self.Board_Status_1)
			self.S_Slot_1[number_title_s_1].SetPosition(c[0][0]+100,c[0][1]-8)
			self.S_Slot_1[number_title_s_1].MakeTitleBar(50)
			self.S_Slot_1[number_title_s_1].Show()

			self.S_Slot_Number_1[number_title_s_1] = ui.TextLine()
			self.S_Slot_Number_1[number_title_s_1].SetParent(self.S_Slot_1[number_title_s_1])
			self.S_Slot_Number_1[number_title_s_1].SetPosition(17,7)
			self.S_Slot_Number_1[number_title_s_1].SetText("0")
			self.S_Slot_Number_1[number_title_s_1].SetHorizontalAlignCenter()
			self.S_Slot_Number_1[number_title_s_1].SetPackedFontColor(0xffa07970)
			self.S_Slot_Number_1[number_title_s_1].Show()

			self.S_Slot_Button_1[number_title_s_1] = ui.Button()
			self.S_Slot_Button_1[number_title_s_1].SetParent(self.Board_Status_1)
			self.S_Slot_Button_1[number_title_s_1].SetPosition(c[0][0]+80+70,c[0][1]-4)
			self.S_Slot_Button_1[number_title_s_1].SetUpVisual(apollo_interface.PATCH_BUTTONS+"/plus_01_normal.png")
			self.S_Slot_Button_1[number_title_s_1].SetOverVisual(apollo_interface.PATCH_BUTTONS+"/plus_02_hover.png")
			self.S_Slot_Button_1[number_title_s_1].SetDownVisual(apollo_interface.PATCH_BUTTONS+"/plus_03_active.png")
			self.S_Slot_Button_1[number_title_s_1].Show()

			number_title_s_1 +=1

		self.statusPlusButtonDict = {
			"HTH"		: self.S_Slot_Button_1[0],
			"INT"		: self.S_Slot_Button_1[1],
			"STR"		: self.S_Slot_Button_1[2],
			"DEX"		: self.S_Slot_Button_1[3],
			}

	def Board_Caracteristics_Function(self):
		self.C_Title = {}
		self.C_Slot = {}
		self.C_Slot_Number ={}
		self.C_Slot_Value ={}
		number_title_c = 0
		info_c=[
		[[30,45+10-18], [apollo_interface.PG2_BONUS_1]],
		[[30,45+10+30-18], [apollo_interface.PG2_BONUS_2]],
		[[30,45+10+30+30-18], [apollo_interface.PG2_BONUS_3]],
		[[30,45+10+30+30+30-18], [apollo_interface.PG2_BONUS_4]],
		[[30,45+10+30+30+30+30-18], [apollo_interface.PG2_BONUS_5]],
		[[30,45+10+30+30+30+30+30-18], [apollo_interface.PG2_BONUS_6]],
		[[30,45+10+30+30+30+30+30+30-18], [apollo_interface.PG2_BONUS_7]],
		[[30,45+10+30+30+30+30+30+30+30-18], [apollo_interface.PG2_BONUS_8]]
		]
		for a in info_c:
			self.C_Title[number_title_c] = ui.TextLine()
			self.C_Title[number_title_c].SetParent(self.Board_Caracteristics)
			self.C_Title[number_title_c].SetPosition(a[0][0],a[0][1])
			self.C_Title[number_title_c].SetText(a[1][0]+":")
			self.C_Title[number_title_c].SetPackedFontColor(0xffa08784)
			self.C_Title[number_title_c].Show()

			self.C_Slot[number_title_c] = ui.InputNew()
			self.C_Slot[number_title_c].SetParent(self.Board_Caracteristics)
			self.C_Slot[number_title_c].SetPosition(a[0][0]+115,a[0][1]-5)
			self.C_Slot[number_title_c].MakeTitleBar(50+8)
			self.C_Slot[number_title_c].Show()

			self.C_Slot_Number[number_title_c] = ui.TextLine()
			self.C_Slot_Number[number_title_c].SetParent(self.C_Slot[number_title_c])
			self.C_Slot_Number[number_title_c].SetPosition(23,8)
			self.C_Slot_Number[number_title_c].SetText("0")
			self.C_Slot_Number[number_title_c].SetHorizontalAlignCenter()
			self.C_Slot_Number[number_title_c].SetPackedFontColor(0xffa07970)
			self.C_Slot_Number[number_title_c].Show()

			self.C_Slot_Value[number_title_c] = ui.TextLine()
			self.C_Slot_Value[number_title_c].SetParent(self.Board_Caracteristics)
			self.C_Slot_Value[number_title_c].SetPosition(a[0][0]+200,a[0][1])
			self.C_Slot_Value[number_title_c].SetText("(|cffa08784%s|cffcaa76f +%s|cffa08784)"%(0,0))
			self.C_Slot_Value[number_title_c].SetHorizontalAlignCenter()
			self.C_Slot_Value[number_title_c].SetPackedFontColor(0xffa08784)
			self.C_Slot_Value[number_title_c].Show()

			number_title_c +=1


	#def Update(self):
	#	global OnTest1
	#	global movement
	#	global movement1
	#	global movement2
	#	global movement3
	#	global movement4
	#
	#	self.RefreshStatus()
	#	self.Refreshing()
	#	self.RefreshQuest()
	#	self.SetEmpireAndGuild(net.GetEmpireID())
	#
	#	speed_movem = 3
	#	if OnTest1 == 1:
	#		if movement >= 0 and movement <= 143-(143-110):
	#			movement += speed_movem
	#			self.Caracter_Input.SetSize(143-95+movement,350)
	#		elif movement >= 143:
	#			OnTest1 = 0
	#			movement = 0
	#			movement1 = 0
	#			movement2 = 0
	#			movement3 = 0
	#			movement4 = 0
	#
	#		if movement2 >= 0 and movement2 <= 441-(441-110):
	#			movement2 +=speed_movem
	#			self.SetSize(441-108+movement2,402)
	#			self.Character_Page.SetSize(441-110+movement2,400)
	#			self.Board.SetSize(441-103+movement2,396)
	#			self.TitleName.SetParent(self)
	#			self.TitleName.SetPosition(+20,-184)
	#			self.TitleName.SetText(uiScriptLocale.CHARACTER_MAIN)
	#			self.TitleName.SetHorizontalAlignCenter()
	#		else:
	#			for i in xrange(0,6):
	#				self.BoardSlots_Text[i].Show()
	#
	#		if movement1 >= 0 and movement1 <= 441-56-(441-110-56):
	#			movement1 +=speed_movem
	#			self.TitleBar.SetWidth(441-110-56+movement1)
	#			self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close))
	#
	#		if movement3 >= 0 and movement3 <= 150-(150-110):
	#			movement3 +=speed_movem
	#			for a in xrange(0,6):
	#				self.BoardSlot[a].MakeTitleBar(150-110+movement3)
	#				self.BoardSlots_Image[a].Show()
	#				self.BoardSlots_Image[a].SetTop()
	#
	#		if movement4 >= 0 and movement4 <= 370-(257):
	#			movement4 +=speed_movem
	#			self.ButtonExpande.SetParent(self)
	#			self.ButtonExpande.SetPosition(257+movement4,12)
	#			self.ButtonExpande.Show()
	#
	#	elif OnTest1 == 2:
	#		if movement >= 0 and movement <= 143-109-(-143):
	#			movement +=speed_movem
	#			self.Caracter_Input.SetSize(143-movement,350)
	#		if movement >= 109:
	#			OnTest1 = 0
	#
	#		if movement1 >= 0 and movement1 <= 441-110-56-(-441-56):
	#			movement1 +=speed_movem
	#			self.TitleBar.SetWidth(441-56-movement1)
	#			self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close))
	#
	#		if movement2 >= 0 and movement2 <= 441-110-(-441):
	#			movement2 +=speed_movem
	#			self.SetSize(441-movement2,400)
	#			self.Character_Page.SetSize(441-movement2,400)
	#			self.Board.SetSize(445-movement2,396)
	#			self.TitleName.SetParent(self)
	#			self.TitleName.SetPosition(20,-183)
	#			self.TitleName.SetText(uiScriptLocale.CHARACTER_MAIN)
	#			self.TitleName.SetHorizontalAlignCenter()
	#			for i in xrange(0,6):
	#				self.BoardSlots_Text[i].Hide()
	#
	#
	#		if movement3 >= 0 and movement3 <= 150-110-(-150):
	#			movement3 +=speed_movem
	#			for a in xrange(0,6):
	#				self.BoardSlot[a].MakeTitleBar(150-movement3)
	#				self.BoardSlots_Image[a].Show()
	#				self.BoardSlots_Image[a].SetTop()
	#
	#		if movement4 >= 0 and movement4 <= 260-(-370):
	#			movement4 +=speed_movem
	#			self.ButtonCollapse.SetParent(self)
	#			self.ButtonCollapse.SetPosition(370-movement4,12)
	#			self.ButtonCollapse.Show()
	#
	#	if self.isLoaded_1 == 1:
	#		return

	def SetSkillToolTip(self, toolTipSkill):
		self.toolTipSkill = toolTipSkill

	def RefreshQuest(self):

		if self.isLoaded_1==0:
			return

		questCount = quest.GetQuestCount()
		questRange = range(quest.QUEST_MAX_NUM)

		for i in questRange[:questCount]:
			(questName, questIcon, questCounterName, questCounterValue) = quest.GetQuestData(self.questShowingStartIndex+i)
			# start colored scrolls
			if questName[0] == '*':
				questName = questName[1:]
			elif questName[0] == '&':
				questName = questName[1:]
			elif questName[0] == '~':
				questName = questName[1:]
			elif questName[0] == '+':
				questName = questName[1:]
			# end colored scrolls
			self.questNameList[i].SetText(questName)
			self.questNameList[i].Show()
			self.questLastCountList[i].Show()
			self.questLastTimeList[i].Show()

			if len(questCounterName) > 0:
				self.questLastCountList[i].SetText("%s : %d" % (questCounterName, questCounterValue))
			else:
				self.questLastCountList[i].SetText("")

			if questCount >= 5:
				self.ScrollBarQuest.Show()
			else:
				self.ScrollBarQuest.Hide()


			self.slots_quest.SetSlot(i, i, 1, 1, questIcon)

		for i in questRange[questCount:]:
			self.questNameList[i].Hide()
			self.questLastCountList[i].Hide()
			self.questLastTimeList[i].Hide()
			self.slots_quest.ClearSlot(i)
			self.slots_quest.HideSlotBaseImage(i)

		self.__UpdateQuestClock()

	def __UpdateQuestClock(self):
			# QUEST_LIMIT_COUNT_BUG_FIX
		for i in xrange(min(quest.GetQuestCount(), quest.QUEST_MAX_NUM)):
		# END_OF_QUEST_LIMIT_COUNT_BUG_FIX
			(lastName, lastTime) = quest.GetQuestLastTime(i)
			clockText = localeInfo.QUEST_UNLIMITED_TIME
			if len(lastName) > 0:

				if lastTime <= 0:
					clockText = localeInfo.QUEST_TIMEOVER

				else:
					questLastMinute = lastTime / 60
					questLastSecond = lastTime % 60

					clockText = lastName + " : "

					if questLastMinute > 0:
						clockText += str(questLastMinute) + localeInfo.QUEST_MIN
						if questLastSecond > 0:
							clockText += " "

					if questLastSecond > 0:
						clockText += str(questLastSecond) + localeInfo.QUEST_SEC

			self.questLastTimeList[i].SetText(clockText)

	def OnUpdate(self):
		self.RefreshAlignment()
		self.RefreshStatus()
		self.Refreshing()
		self.RefreshQuest()
		self.SetEmpireAndGuild(net.GetEmpireID())
		self.__UpdateQuestClock()
		if app.ENABLE_SKILL_COLOR_SYSTEM:
			if self.skillColorWnd:
				self.__UpdateSkillColorPosition()
				
	def SetExperience(self, curPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		if maxPoint > 0:
			self.exp_slot.SetPercentage(curPoint, maxPoint)

	def Refreshing(self):
		curPoint = unsigned32(player.GetStatus(player.EXP))
		maxPoint = unsigned32(player.GetStatus(player.NEXT_EXP))

		curPoint = min(curPoint, maxPoint)
		curPoint = max(curPoint, 0)
		maxPoint = max(maxPoint, 0)

		self.EXP.SetText("EXP:"+str(curPoint))
		self.EXP_REST.SetText("from" + "    " + str(maxPoint))
		self.Procent.SetText("%s %.2f%%" % ("", float(curPoint) / max(1, float(maxPoint)) * 100))

		#---------------------------
		self.SetExperience(curPoint, maxPoint)

	def SetEmpireAndGuild (self, id):
		guildName = player.GetGuildName()
		if not guildName:
			self.guildNameValue.SetText(self.EMPIRE_NAME.get(id, ""))
			if id == 0:
				self.guildNameValue.SetPackedFontColor(0xffc944316)
			elif id == 2:
				self.guildNameValue.SetPackedFontColor(0xffe5ad4d)
			else:
				self.guildNameValue.SetPackedFontColor(0xff467ddd)
		else:
			self.guildNameValue.SetText(guildName)
			self.guildNameValue.SetPackedFontColor(0xffa07970)

	def RefreshStatus(self):
		if self.isLoaded_1==0:
			return
		try:
			characterName = player.GetName()
			self.characterNameValue.SetText(characterName)
			self.levelValue.SetText(str(player.GetStatus(player.LEVEL)))

			self.S_Slot_Number[0].SetText(str(player.GetStatus(player.HP)) + '/' + str(player.GetStatus(player.MAX_HP)))
			self.S_Slot_Number[1].SetText(str(player.GetStatus(player.SP)) + '/' + str(player.GetStatus(player.MAX_SP)))

			self.Status_Plus_Value.SetText(str(player.GetStatus(player.STAT)))

			self.SetEmpireAndGuild(net.GetEmpireID())
			self.RefreshAlignment()

			statusPlusPoint=player.GetStatus(player.STAT)
			if statusPlusPoint > 0:
				self.S_Slot_Button_1[0].Show()
				self.S_Slot_Button_1[1].Show()
				self.S_Slot_Button_1[2].Show()
				self.S_Slot_Button_1[3].Show()
			else:
				self.S_Slot_Button_1[0].Hide()
				self.S_Slot_Button_1[1].Hide()
				self.S_Slot_Button_1[2].Hide()
				self.S_Slot_Button_1[3].Hide()

			self.S_Slot_Number_1[0].SetText(str(player.GetStatus(player.HT)))
			self.S_Slot_Number_1[1].SetText(str(player.GetStatus(player.IQ)))
			self.S_Slot_Number_1[2].SetText(str(player.GetStatus(player.ST)))
			self.S_Slot_Number_1[3].SetText(str(player.GetStatus(player.DX)))

			minAtk=player.GetStatus(player.ATT_MIN)
			maxAtk=player.GetStatus(player.ATT_MAX)
			atkBonus=player.GetStatus(player.ATT_BONUS)
			attackerBonus=player.GetStatus(player.ATTACKER_BONUS)

			self.C_Slot_Number[0].SetText(str(player.GetStatus(player.MOVING_SPEED)))
			self.C_Slot_Number[1].SetText(str(player.GetStatus(player.ATT_SPEED)))
			self.C_Slot_Number[2].SetText(str(player.GetStatus(player.CASTING_SPEED)))
			self.C_Slot_Number[4].SetText(str(player.GetStatus(player.MAG_DEF)))
			self.C_Slot_Number[5].SetText(str(player.GetStatus(player.EVADE_RATE)))

			minAtk=player.GetStatus(player.ATT_MIN)
			maxAtk=player.GetStatus(player.ATT_MAX)
			atkBonus=player.GetStatus(player.ATT_BONUS)
			attackerBonus=player.GetStatus(player.ATTACKER_BONUS)

			if minAtk==maxAtk:
				self.C_Slot_Number[6].SetText("%d" % (minAtk+atkBonus+attackerBonus))
			else:
				self.C_Slot_Number[6].SetText("%d-%d" % (minAtk+atkBonus+attackerBonus, maxAtk+atkBonus+attackerBonus))

			minMagAtk=player.GetStatus(player.MAG_ATT)+player.GetStatus(player.MIN_MAGIC_WEP)
			maxMagAtk=player.GetStatus(player.MAG_ATT)+player.GetStatus(player.MAX_MAGIC_WEP)

			if minMagAtk==maxMagAtk:
				self.C_Slot_Number[3].SetText("%d" % (minMagAtk))
			else:
				self.C_Slot_Number[3].SetText("%d-%d" % (minMagAtk, maxMagAtk))

			defValue=player.GetStatus(player.DEF_GRADE)
			if constInfo.ADD_DEF_BONUS_ENABLE:
				defValue+=player.GetStatus(player.DEF_BONUS)
			self.C_Slot_Number[7].SetText("%d" % (defValue))


			Test_Poits = [player.GetStatus(player.MOVING_SPEED),player.GetStatus(player.ATT_SPEED),player.GetStatus(player.CASTING_SPEED),
			minMagAtk,player.GetStatus(player.MAG_DEF),player.GetStatus(player.EVADE_RATE),minAtk+atkBonus+attackerBonus,defValue]

			race = net.GetMainActorRace()
			group = net.GetMainActorSkillGroup()
			empire = net.GetMainActorEmpire()

			job = chr.RaceToJob(race)
			if job == 0:
				Test_Poits_2= [100,100,100,8,5,3,10,5]
			if job == 1:
				Test_Poits_2= [100,100,100,8,5,5,8,4]
			if job == 2:
				Test_Poits_2= [100,100,100,12,7,3,9,4]
			if job == 3:
				Test_Poits_2= [100,100,100,14,8,3,7,5]
			if job == 4:
				Test_Poits_2= [100,100,100,8,5,5,8,4]

			for i in xrange(0,8):
				if Test_Poits[i] == Test_Poits_2[i]:
					self.C_Slot_Value[i].SetText("(|cffa08784%s|cffcaa76f +%s|cffa08784)"%(Test_Poits_2[i],0))
				if Test_Poits[i] > Test_Poits_2[i]:
					self.C_Slot_Value[i].SetText("(|cffa08784%s|cffcaa76f %s|cffa08784)"%(100,str(Test_Poits_2[i]-Test_Poits[i]).replace("-","+")))
				if Test_Poits[i] < Test_Poits_2[i]:
					self.C_Slot_Value[i].SetText("(|cffa08784%s|cffcaa76f -%s|cffa08784)"%(100,str(Test_Poits_2[i]-Test_Poits[i])))

		except:
			import exception
			exception.Abort("CharacterWindow.RefreshStatus")

		try:
			faceImageName = apollo_interface.FACE_IMAGE_DICT[race]
			try:
				self.faceImage.LoadImage(faceImageName)
			except:
				print "CharacterWindow.RefreshCharacter(race=%d, faceImageName=%s)" % (race, faceImageName)
				self.faceImage.Hide()

		except KeyError:
			self.faceImage.Hide()

	def RefreshAlignment(self):
		# import apollo_interface
		COLOR_NORMAL = 0xffa08784
		if TRUE == self.nameSlot.IsIn():
			point, grade = player.GetAlignmentData()

			import colorInfo
			COLOR_DICT = {	0 : colorInfo.TITLE_RGB_GOOD_4,
							1 : colorInfo.TITLE_RGB_GOOD_3,
							2 : colorInfo.TITLE_RGB_GOOD_2,
							3 : colorInfo.TITLE_RGB_GOOD_1,
							4 : colorInfo.TITLE_RGB_NORMAL,
							5 : colorInfo.TITLE_RGB_EVIL_1,
							6 : colorInfo.TITLE_RGB_EVIL_2,
							7 : colorInfo.TITLE_RGB_EVIL_3,
							8 : colorInfo.TITLE_RGB_EVIL_4, }
			colorList = COLOR_DICT.get(grade, colorInfo.TITLE_RGB_NORMAL)
			gradeColor = ui.GenerateColor(colorList[0], colorList[1], colorList[2])

			self.toolTipAlignment.ClearToolTip()
			self.toolTipAlignment.AutoAppendTextLine(localeInfo.TITLE_NAME_LIST[grade], gradeColor)
			self.toolTipAlignment.AutoAppendTextLine(localeInfo.ALIGNMENT_NAME + str(point), COLOR_NORMAL)
			self.toolTipAlignment.AlignHorizonalCenter()
			self.toolTipAlignment.ShowToolTip()
		else:
			self.toolTipAlignment.HideToolTip()

	def ContenidoBonus1(self):
		global isLoaded
		global number_on
		if number_on == 0:
			var = 0
			for i in apollo_interface.Offensive_bonuse:
				self.fileListBox.AppendItem(Item("|cffa08784 %s |cffcaa76f %s%s "% (i+":",player.GetStatus(apollo_interface.Offensive_bonuse_Val[var]),"%" ))) #"|cffa08784"+str(i))
				var += 1

		if number_on == 1:
			var = 0
			for i in apollo_interface.Defensive_bonuse:
				self.fileListBox.AppendItem(Item("|cffa08784 %s |cffcaa76f %s%s "% (i+":",player.GetStatus(apollo_interface.Defensive_bonuse_Val[var]),"%" ))) #"|cffa08784"+str(i))
				var += 1

		if number_on == 2:
			var = 0
			for i in apollo_interface.Other_bonuses:
				self.fileListBox.AppendItem(Item("|cffa08784 %s |cffcaa76f %s%s "% (i+":",player.GetStatus(apollo_interface.Other_bonuses_Val[var]),"%" ))) #"|cffa08784"+str(i))
				var += 1

	def __BindEvent(self):
		for i in xrange(len(self.skillGroupButton)):
			self.skillGroupButton[i].SetEvent(lambda arg=i: self.__SelectSkillGroup(arg))

		for (statusPlusKey, statusPlusButton) in self.statusPlusButtonDict.items():
			statusPlusButton.SAFE_SetEvent(self.__OnClickStatusPlusButton, statusPlusKey)

		self.slots_quest.SetSelectItemSlotEvent(ui.__mem_func__(self.__SelectQuest))

		race = net.GetMainActorRace()
		group = net.GetMainActorSkillGroup()
		empire = net.GetMainActorEmpire()


		self.__SetSkillGroupName(race, group)

	def __SetSkillGroupName(self, race, group):

		job = chr.RaceToJob(race)

		if not self.SKILL_GROUP_NAME_DICT.has_key(job):
			return

		nameList = self.SKILL_GROUP_NAME_DICT[job]

		if 0 == group:
			self.slot_skill_name[0].SetText(nameList[1])
			self.slot_skill_name[1].SetText(nameList[2])
			self.slot_skill_name[0].Show()
			self.slot_skill_name[1].Hide()
			self.slots_button_skills[0].Show()
			self.slots_button_skills[1].Show()

		else:

			if self.__CanUseHorseSkill():
				self.slot_skill_name[0].SetText(nameList.get(group, "Noname"))
				self.slot_skill_name[1].SetText(localeInfo.SKILL_GROUP_HORSE)
				self.slot_skill_name[0].Show()
				self.slot_skill_name[1].Show()
				self.slots_button_skills[0].Show()
				self.slots_button_skills[1].Show()


			else:
				self.slots_button_skills[0].Hide()
				self.slots_button_skills[1].Hide()
				#self.__SelectSkillGroup(0)
			self.slot_skill_name[0].SetText(nameList[1])
			self.slot_skill_name[1].SetText(nameList[2])
			self.slot_skill_name[0].Hide()
			self.slot_skill_name[1].Show()

	def __CanUseHorseSkill(self):

		slotIndex = player.GetSkillSlotIndex(player.SKILL_INDEX_RIDING)

		if not slotIndex:
			return FALSE

		grade = player.GetSkillGrade(slotIndex)
		level = player.GetSkillLevel(slotIndex)
		if level < 0:
			level *= -1
		if grade >= 1 and level >= 1:
			return TRUE

		return FALSE

	## Quest
	def __SelectQuest(self, slotIndex):
		questIndex = quest.GetQuestIndex(self.questShowingStartIndex+slotIndex)

		import event
		event.QuestButtonClick(-2147483648 + questIndex)


	if constInfo.ENABLE_FAST_STATUS_POUNTS:	
		def ChooseCountPlusStat(self, statusKey):
			inputDialog = uiCommon.InputDialog()
			inputDialog.SetTitle("Status Points")
			inputDialog.SetMaxLength(2)
			inputDialog.SetNumberMode()
			inputDialog.SetFocus()
			inputDialog.SetAcceptEvent(lambda arg1=statusKey: self.ChooseCountPlusStatConfirm(arg1))
			inputDialog.SetCancelEvent(self.ChooseCountPlusStatHide)
			inputDialog.Open()
			self.inputDialog = inputDialog
			
		def ChooseCountPlusStatHide(self):
			self.inputDialog.Hide()
			
		def ChooseCountPlusStatConfirm(self, statusKey):
			self.ChooseCountPlusStatHide()
			statusPlusCommand=self.statusPlusCommandDictNew[statusKey]
			try:
				count = int(self.inputDialog.GetText())
				if count <= 0:
					return
				net.SendChatPacket("/stat %s %s" % (str(statusPlusCommand), str(count)))

			except ValueError:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "value error.")

		def __OnClickStatusPlusButton(self, statusKey):
			try:
				statusPlusPoint=player.GetStatus(player.STAT)
				if statusPlusPoint >= 10:
					self.ChooseCountPlusStat(statusKey)
				else:
					statusPlusCommand=self.statusPlusCommandDict[statusKey]
					net.SendChatPacket(statusPlusCommand)

			except KeyError, msg:
				dbg.TraceError("CharacterWindow.__OnClickStatusPlusButton KeyError: %s", msg)
	else:		
		def __OnClickStatusPlusButton(self, statusKey):
			try:
				statusPlusCommand=self.statusPlusCommandDict[statusKey]
				net.SendChatPacket(statusPlusCommand)
			except KeyError, msg:
				dbg.TraceError("CharacterWindow.__OnClickStatusPlusButton KeyError: %s", msg)

	def __SetSkillSlotData(self, race, group, empire=0):

		## SkillIndex
		# net.RegisterSkills(race, group, empire)

		## Event
		self.__SetSkillSlotEvent()

		## Refresh
		self.RefreshSkill()

	## Skill Process
	def __RefreshSkillPage(self, name, slotCount):
		global SHOW_LIMIT_SUPPORT_SKILL_LIST

		skillPage = self.skillPageDict[name]

		startSlotIndex = skillPage.GetStartIndex()
		if "ACTIVE" == name:
			if self.PAGE_HORSE == self.curSelectedSkillGroup:
				startSlotIndex += slotCount

		getSkillType=skill.GetSkillType
		getSkillIndex=player.GetSkillIndex
		getSkillGrade=player.GetSkillGrade
		getSkillLevel=player.GetSkillLevel
		getSkillLevelUpPoint=skill.GetSkillLevelUpPoint
		getSkillMaxLevel=skill.GetSkillMaxLevel
		for i in xrange(slotCount+1):

			slotIndex = i + startSlotIndex
			skillIndex = getSkillIndex(slotIndex)

			for j in xrange(skill.SKILL_GRADE_COUNT):
				skillPage.ClearSlot(self.__GetRealSkillSlot(j, i))

			if 0 == skillIndex:
				continue

			skillGrade = getSkillGrade(slotIndex)
			skillLevel = getSkillLevel(slotIndex)
			skillType = getSkillType(skillIndex)


			if player.SKILL_INDEX_RIDING == skillIndex:
				if 1 == skillGrade:
					skillLevel += 19
				elif 2 == skillGrade:
					skillLevel += 29
				elif 3 == skillGrade:
					skillLevel = 40

				skillPage.SetSkillSlotNew(slotIndex, skillIndex, max(skillLevel-1, 0), skillLevel)
				skillPage.SetSlotCount(slotIndex, skillLevel)

				## ACTIVE
			elif skill.SKILL_TYPE_ACTIVE == skillType:
				for j in xrange(skill.SKILL_GRADE_COUNT):
					realSlotIndex = self.__GetRealSkillSlot(j, slotIndex)
					skillPage.SetSkillSlotNew(realSlotIndex, skillIndex, j, skillLevel)
					skillPage.SetCoverButton(realSlotIndex)

					if (skillGrade == skill.SKILL_GRADE_COUNT) and j == (skill.SKILL_GRADE_COUNT-1):
						skillPage.SetSlotCountNew(realSlotIndex, skillGrade, skillLevel)
					elif (not self.__CanUseSkillNow()) or (skillGrade != j):
						skillPage.SetSlotCount(realSlotIndex, 0)
						skillPage.DisableCoverButton(realSlotIndex)
					else:
						skillPage.SetSlotCountNew(realSlotIndex, skillGrade, skillLevel)


			else:
				if not SHOW_LIMIT_SUPPORT_SKILL_LIST or skillIndex in SHOW_LIMIT_SUPPORT_SKILL_LIST:
					realSlotIndex = self.__GetETCSkillRealSlotIndex(slotIndex)
					skillPage.SetSkillSlot(realSlotIndex, skillIndex, skillLevel)
					skillPage.SetSlotCountNew(realSlotIndex, skillGrade, skillLevel)

					if skill.CanUseSkill(skillIndex):
						skillPage.SetCoverButton(realSlotIndex)

			skillPage.RefreshSlot()

		if app.ENABLE_SKILL_COLOR_SYSTEM:
			if "ACTIVE" == name:
				if self.PAGE_HORSE != self.curSelectedSkillGroup:
					self.__CreateSkillColorButton(skillPage)
				else:
					self.skillColorButton = []

	def RefreshSkill(self):

		if self.isLoaded_1==0:
			return

		if self.__IsChangedHorseRidingSkillLevel():
			self.RefreshCharacter()
			return

		activeStatPoint = player.GetStatus(player.SKILL_ACTIVE)
		self.status_abilities.SetText("|cffa07970| |cfff8d090%s |cffa07970|"%activeStatPoint) #|cffa08784%s|cffcaa76f +%s|cffa08784 f8d090


		global SHOW_ONLY_ACTIVE_SKILL
		if SHOW_ONLY_ACTIVE_SKILL:
			self.__RefreshSkillPage("ACTIVE", self.ACTIVE_PAGE_SLOT_COUNT)
		else:
			self.__RefreshSkillPage("ACTIVE", self.ACTIVE_PAGE_SLOT_COUNT)
			self.__RefreshSkillPage("SUPPORT", self.SUPPORT_PAGE_SLOT_COUNT)

		self.RefreshSkillPlusButtonList()

	def __ShowAlignmentToolTip(self):
		self.toolTipAlignment.ShowToolTip()

	def __HideAlignmentToolTip(self):
		self.toolTipAlignment.HideToolTip()

	def RefreshCharacter(self):
		## GroupName
		race = net.GetMainActorRace()
		group = net.GetMainActorSkillGroup()
		empire = net.GetMainActorEmpire()

		self.__SetSkillGroupName(race, group)
		
		## Skill
		if 0 == group:
			self.__SelectSkillGroup(0)

		else:
			self.__SetSkillSlotData(race, group, empire)

			if self.__CanUseHorseSkill():
				self.__SelectSkillGroup(0)

	def __CanUseHorseSkill(self):

		slotIndex = player.GetSkillSlotIndex(player.SKILL_INDEX_RIDING)

		if not slotIndex:
			return FALSE

		grade = player.GetSkillGrade(slotIndex)
		level = player.GetSkillLevel(slotIndex)
		if level < 0:
			level *= -1
		if grade >= 1 and level >= 1:
			return TRUE

		return FALSE
	def __IsChangedHorseRidingSkillLevel(self):
		ret = FALSE

		if -1 == self.canUseHorseSkill:
			self.canUseHorseSkill = self.__CanUseHorseSkill()

		if self.canUseHorseSkill != self.__CanUseHorseSkill():
			ret = TRUE

		self.canUseHorseSkill = self.__CanUseHorseSkill()
		return ret


	def __SelectSkillGroup(self, index):
		for btn in self.skillGroupButton:
			btn.SetUp()
		self.skillGroupButton[index].Down()
		self.slot_skill_name[index].Show()

		if 0 == index:
			# index = net.GetMainActorSkillGroup()-1
			self.slot_skill_name[0].Show()
			self.slot_skill_name[1].Hide()
		elif 1 == index:
			# index = self.PAGE_HORSE
			self.slot_skill_name[0].Hide()
			self.slot_skill_name[1].Show()


		if self.__CanUseHorseSkill():
			if 0 == index:
				index = net.GetMainActorSkillGroup()-1
			elif 1 == index:
				index = self.PAGE_HORSE

		self.curSelectedSkillGroup = index
		self.__SetSkillSlotData(net.GetMainActorRace(), index+1, net.GetMainActorEmpire())

	def __SetSkillSlotEvent(self):
		for skillPageValue in self.skillPageDict.itervalues():
			skillPageValue.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
			skillPageValue.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectSkill))
			skillPageValue.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
			skillPageValue.SetUnselectItemSlotEvent(ui.__mem_func__(self.ClickSkillSlot))
			skillPageValue.SetUseSlotEvent(ui.__mem_func__(self.ClickSkillSlot))
			skillPageValue.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			skillPageValue.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			skillPageValue.SetPressedSlotButtonEvent(ui.__mem_func__(self.OnPressedSlotButton))
			skillPageValue.AppendSlotButton(apollo_interface.PATCH_BUTTONS+"/plus_01_normal.png",\
											apollo_interface.PATCH_BUTTONS+"/plus_02_hover.png",\
											apollo_interface.PATCH_BUTTONS+"/plus_03_active.png")
	def SelectSkill(self, skillSlotIndex):

		mouseController = mouseModule.mouseController

		if FALSE == mouseController.isAttached():

			srcSlotIndex = self.__RealSkillSlotToSourceSlot(skillSlotIndex)
			selectedSkillIndex = player.GetSkillIndex(srcSlotIndex)

			if skill.CanUseSkill(selectedSkillIndex):

				if app.IsPressed(app.DIK_LCONTROL):

					player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_SKILL, srcSlotIndex)
					return

				mouseController.AttachObject(self, player.SLOT_TYPE_SKILL, srcSlotIndex, selectedSkillIndex)

		else:

			mouseController.DeattachObject()

	def SelectEmptySlot(self, SlotIndex):
		mouseModule.mouseController.DeattachObject()

	## ToolTip
	def OverInItem(self, slotNumber):

		if mouseModule.mouseController.isAttached():
			return

		if 0 == self.toolTipSkill:
			return

		srcSlotIndex = self.__RealSkillSlotToSourceSlot(slotNumber)
		skillIndex = player.GetSkillIndex(srcSlotIndex)
		skillLevel = player.GetSkillLevel(srcSlotIndex)
		skillGrade = player.GetSkillGrade(srcSlotIndex)
		skillType = skill.GetSkillType(skillIndex)

		## ACTIVE
		if skill.SKILL_TYPE_ACTIVE == skillType:
			overInSkillGrade = self.__GetSkillGradeFromSlot(slotNumber)

			if overInSkillGrade == skill.SKILL_GRADE_COUNT-1 and skillGrade == skill.SKILL_GRADE_COUNT:
				self.toolTipSkill.SetSkillNew(srcSlotIndex, skillIndex, skillGrade, skillLevel)
			elif overInSkillGrade == skillGrade:
				self.toolTipSkill.SetSkillNew(srcSlotIndex, skillIndex, overInSkillGrade, skillLevel)
			else:
				self.toolTipSkill.SetSkillOnlyName(srcSlotIndex, skillIndex, overInSkillGrade)

		else:
			self.toolTipSkill.SetSkillNew(srcSlotIndex, skillIndex, skillGrade, skillLevel)

	def OverOutItem(self):
		if 0 != self.toolTipSkill:
			self.toolTipSkill.HideToolTip()

	def ActEmotion(self, emotionIndex):
		self.__ClickEmotionSlot(emotionIndex)

	def __OverInEmotion(self, slotIndex):
		if self.emotionToolTip:
			if not slotIndex in emotion.EMOTION_DICT:
				return

			self.emotionToolTip.ClearToolTip()
			self.emotionToolTip.SetTitle(emotion.EMOTION_DICT[slotIndex]["name"])
			self.emotionToolTip.AlignHorizonalCenter()
			self.emotionToolTip.ShowToolTip()

	def __OverOutEmotion(self):
		if self.emotionToolTip:
			self.emotionToolTip.HideToolTip()

	def OnPressedSlotButton(self, slotNumber):
		srcSlotIndex = self.__RealSkillSlotToSourceSlot(slotNumber)

		skillIndex = player.GetSkillIndex(srcSlotIndex)
		curLevel = player.GetSkillLevel(srcSlotIndex)
		maxLevel = skill.GetSkillMaxLevel(skillIndex)

		net.SendChatPacket("/skillup " + str(skillIndex))

	def ClickSkillSlot(self, slotIndex):

		srcSlotIndex = self.__RealSkillSlotToSourceSlot(slotIndex)
		skillIndex = player.GetSkillIndex(srcSlotIndex)
		skillType = skill.GetSkillType(skillIndex)

		if not self.__CanUseSkillNow():
			if skill.SKILL_TYPE_ACTIVE == skillType:
				return

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				if skill.CanUseSkill(skillIndex):
					player.ClickSkillSlot(srcSlotIndex)
					return

		mouseModule.mouseController.DeattachObject()


	def OnUseSkill(self, slotIndex, coolTime):

		skillIndex = player.GetSkillIndex(slotIndex)
		skillType = skill.GetSkillType(skillIndex)
		skillGrade = player.GetSkillGrade(slotIndex)

		## ACTIVE
		if skill.SKILL_TYPE_ACTIVE == skillType:
			skillGrade = player.GetSkillGrade(slotIndex)
			slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)
		## ETC
		else:
			slotIndex = self.__GetETCSkillRealSlotIndex(slotIndex)

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				slotWindow.SetSlotCoolTime(slotIndex, coolTime)
				return
				
	def OnActivateSkill(self, slotIndex):
		skillGrade = player.GetSkillGrade(slotIndex)
		slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)
		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				if app.ENABLE_CHANGELOOK_SYSTEM:
					slotWindow.ActivateSlotOld(slotIndex)
				else:
					slotWindow.ActivateSlot(slotIndex)
				
				return

	def OnDeactivateSkill(self, slotIndex):
		skillGrade = player.GetSkillGrade(slotIndex)
		slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)
		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				if app.ENABLE_CHANGELOOK_SYSTEM:
					slotWindow.DeactivateSlotOld(slotIndex)
				else:
					slotWindow.DeactivateSlot(slotIndex)
				
				return
	'''
	def OnActivateSkill(self, slotIndex):

		skillGrade = player.GetSkillGrade(slotIndex)
		slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				slotWindow.ActivateSlot(slotIndex)
				return

	def OnDeactivateSkill(self, slotIndex):

		skillGrade = player.GetSkillGrade(slotIndex)
		slotIndex = self.__GetRealSkillSlot(skillGrade, slotIndex)

		for slotWindow in self.skillPageDict.values():
			if slotWindow.HasSlot(slotIndex):
				slotWindow.DeactivateSlot(slotIndex)
				return
	'''
	def __GetRealSkillSlot(self, skillGrade, skillSlot):
		return skillSlot + min(skill.SKILL_GRADE_COUNT-1, skillGrade)*skill.SKILL_GRADE_STEP_COUNT

	if app.ENABLE_SKILL_COLOR_SYSTEM:
		def __CreateSkillColorButton(self, parent):
			self.skillColorButton = []

			xPos, yPos = 0, 0
			for idx in xrange(self.PAGE_SLOT_COUNT):
				skillSlot = idx
				if skillSlot < 6:
					if (skillSlot % 2) == 0:
						xPos = 80
						yPos = 4 + (skillSlot / 2 * 36)
					else:
						xPos = 205
						yPos = 4 + (skillSlot / 2 * 36)

					skillIndex = player.GetSkillIndex(skillSlot + 1)
					skillMaxGrade = 3

					if len(self.skillColorButton) == skillSlot:
						self.skillColorButton.append([])
						self.skillColorButton[skillSlot] = ui.Button()
						self.skillColorButton[skillSlot].SetParent(parent)
						self.skillColorButton[skillSlot].SetUpVisual("d:/ymir work/ui/skillcolor/skill_color_button_default.tga")
						self.skillColorButton[skillSlot].SetOverVisual("d:/ymir work/ui/skillcolor/skill_color_button_over.tga")
						self.skillColorButton[skillSlot].SetDownVisual("d:/ymir work/ui/skillcolor/skill_color_button_down.tga")
						self.skillColorButton[skillSlot].SetPosition(xPos, yPos)
						self.skillColorButton[skillSlot].SetEvent(lambda arg = skillSlot, arg2 = skillIndex: self.__OnPressSkillColorButton(arg, arg2))
						if player.GetSkillGrade(skillSlot + 1) >= skillMaxGrade:
							self.skillColorButton[skillSlot].Show()
						else:
							self.skillColorButton[skillSlot].Hide()
					else:
						self.skillColorButton[skillSlot].SetPosition(xPos, yPos)

		def __UpdateSkillColorPosition(self):
			x, y = self.GetGlobalPosition()
			self.skillColorWnd.SetPosition(x + 440, y)

		def __OnPressSkillColorButton(self, skillSlot, skillIndex):
			self.skillColorWnd = uiSkillColor.SkillColorWindow(skillSlot, skillIndex)
			if self.skillColorWnd and not self.skillColorWnd.IsShow():
				self.skillColorWnd.Show()

				"""
				if app.ENABLE_DETAILS_UI:
					if self.chDetailsWnd and self.chDetailsWnd.IsShow():
						self.chDetailsWnd.Hide()
						self.__InitCharacterDetailsUIButton()
				"""


	def RefreshSkillPlusButtonList(self):

		if self.isLoaded_1==0:
			return


		if not self.__CanUseSkillNow():
			return

		try:
			if self.PAGE_HORSE == self.curSelectedSkillGroup:
				self.__RefreshSkillPlusButton("HORSE")
			else:
				self.__RefreshSkillPlusButton("ACTIVE")

			self.__RefreshSkillPlusButton("SUPPORT")

		except:
			import exception
			exception.Abort("CharacterWindow.RefreshSkillPlusButtonList.BindObject")


	def CanShowPlusButton(self, skillIndex, skillLevel, curStatPoint):
		if 0 == skillIndex:
			return FALSE


		if not skill.CanLevelUpSkill(skillIndex, skillLevel):
			return FALSE

		return TRUE

	def __RefreshSkillPlusButton(self, name):
		global HIDE_SUPPORT_SKILL_POINT
		if HIDE_SUPPORT_SKILL_POINT and "SUPPORT" == name:
			return

		slotWindow = self.skillPageDict[name]
		slotWindow.HideAllSlotButton()

		slotStatType = self.skillPageStatDict[name]
		if 0 == slotStatType:
			return

		statPoint = player.GetStatus(slotStatType)
		startSlotIndex = slotWindow.GetStartIndex()
		if "HORSE" == name:
			startSlotIndex += self.ACTIVE_PAGE_SLOT_COUNT

		if statPoint > 0:
			for i in xrange(self.PAGE_SLOT_COUNT):
				slotIndex = i + startSlotIndex
				skillIndex = player.GetSkillIndex(slotIndex)
				skillGrade = player.GetSkillGrade(slotIndex)
				skillLevel = player.GetSkillLevel(slotIndex)

				if skillIndex == 0:
					continue
				if skillGrade != 0:
					continue

				if name == "HORSE":
					if player.GetStatus(player.LEVEL) >= skill.GetSkillLevelLimit(skillIndex):
						if skillLevel < 20:
							slotWindow.ShowSlotButton(self.__GetETCSkillRealSlotIndex(slotIndex))

				else:
					if "SUPPORT" == name:
						if not SHOW_LIMIT_SUPPORT_SKILL_LIST or skillIndex in SHOW_LIMIT_SUPPORT_SKILL_LIST:
							if self.CanShowPlusButton(skillIndex, skillLevel, statPoint):
								slotWindow.ShowSlotButton(slotIndex)
					else:
						if self.CanShowPlusButton(skillIndex, skillLevel, statPoint):
							slotWindow.ShowSlotButton(slotIndex)

	def __GetSkillGradeFromSlot(self, skillSlot):
		return int(skillSlot / skill.SKILL_GRADE_STEP_COUNT)

	def __GetETCSkillRealSlotIndex(self, skillSlot):
		if skillSlot > 100:
			return skillSlot
		return skillSlot % self.ACTIVE_PAGE_SLOT_COUNT

	def __RealSkillSlotToSourceSlot(self, realSkillSlot):
		if realSkillSlot > 100:
			return realSkillSlot
		if self.PAGE_HORSE == self.curSelectedSkillGroup:
			return realSkillSlot + self.ACTIVE_PAGE_SLOT_COUNT
		return realSkillSlot % skill.SKILL_GRADE_STEP_COUNT

	def __CanUseSkillNow(self):
		if 0 == net.GetMainActorSkillGroup():
			return FALSE

		return TRUE

	def OnQuestScroll(self):
		questCount = quest.GetQuestCount()
		scrollLineCount = max(0, questCount - quest.QUEST_MAX_NUM)
		startIndex = int(scrollLineCount * self.ScrollBarQuest.GetPos())

		if startIndex != self.questShowingStartIndex:
			self.questShowingStartIndex = startIndex
			self.RefreshQuest()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def Close(self):
		if 0 != self.toolTipSkill:
			self.toolTipSkill.HideToolTip()
		if app.ENABLE_SKILL_COLOR_SYSTEM:
			if self.skillColorWnd and self.skillColorWnd.IsShow():
				self.skillColorWnd.Hide()
		self.Hide()

class WaitingDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self, waitTime):
		import time
		curTime = time.clock()
		self.endTime = curTime + waitTime

		self.Show()

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)

	def OnUpdate(self):
		import time
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			return

	def OnPressExitKey(self):
		self.Close()
		return TRUE

class Item(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=fileName
		self.textLine=self.__CreateTextLine(fileName[:70])

	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)

	def GetText(self):
		return self.text

	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 0, 0)

	def __CreateTextLine(self, fileName):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)
		textLine.SetText(fileName)
		textLine.Show()
		return textLine
