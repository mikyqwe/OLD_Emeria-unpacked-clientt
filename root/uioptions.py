import player
import exchange
import net
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import event
import chat
import item
import constInfo
import playerSettingModule
import ui
import mouseModule
import uiPickMoney
import wndMgr
import uiToolTip
import uiScriptLocale
import systemSetting
import uiPrivateShopBuilder
import background
import chat
import snd
import uiSelectMusic
import musicInfo
import uitooltipGold
import apollo_interface


OnTest1 = 0
movement = 0
movement1 = 0
movement2 = 0
movement3 = 0
movement4 = 0
active = 0

MUSIC_FILENAME_MAX_LEN = 25
blockMode = 0
viewChatMode = 0

DayMode = 1
ShowMode = 1

class OptionWindow(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded_1= 0
		self.LoadWindow()
		self.__Initialize()
		self.tilingMode = 0
		self.musicListDlg = 0

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.RefreshBlock()
		self.RefreshOptiones()
		self.RefreshTextures()
		ui.ScriptWindow.Show(self)

	def Destroy(self):
		global OnTest1
		OnTest1 = 0

	def __Initialize(self):
		return

	def LoadWindow(self):
		if self.isLoaded_1 == 1:
			return

		self.isLoaded_1 = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "apollo_scripts/OptionWindow.py")
		except:
			import exception
			exception.Abort("OptionWindow.LoadWindow.LoadObject")


		try:
			self.Board = self.GetChild("board")
			self.Options_Input = self.GetChild("Options_Input")
			self.Options_Page = self.GetChild("Options_Page")
			self.TitleName = self.GetChild("TitleName")
			self.TitleBar = self.GetChild("Options_TitleBar")
			self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close))

			self.ButtonCollapse = self.GetChild("ButtonCollapse")
			self.ButtonCollapse.SetEvent(lambda : self.InputFunctiones(1))
			self.ButtonExpande = self.GetChild("ButtonExpande")
			self.ButtonExpande.SetEvent(lambda : self.InputFunctiones(2))
			self.ButtonExpande.Hide()
			self.Board_Caracter_Function()

			## Page Status 1
			self.Player_Status = self.GetChild("Player_Status")
			self.Player_Status.Show()
			self.Player_Status_1 = self.GetChild("Player_Status_1")
			self.Player_Status_1.Show()
			self.Player_Status_2 = self.GetChild("Player_Status_2")
			self.Player_Status_2.Show()
			self.Player_Status_Function()

			## Page Status 2
			self.Player_Block_Status = self.GetChild("Player_Block_Status")
			self.Player_Block_Status.Hide()
			self.Player_Block_Function()
			## Page Status 3
			self.Player_Grafics = self.GetChild("Player_Grafics")
			self.Player_Grafics_1 = self.GetChild("Player_Grafics_1")
			self.Player_Grafics_2 = self.GetChild("Player_Grafics_2")
			self.Player_Grafics_3 = self.GetChild("Player_Grafics_3")
			self.Player_Grafics_Function()
			self.Player_Grafics.Hide()

			## Page Status 4
			self.Player_Sound = self.GetChild("Player_Sound")
			self.Player_Sound.Hide()
			self.Player_Sound_Function()

		except:
			import exception
			exception.Abort("OptionWindow.LoadWindow.BindObject")

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
		inf_sec_1 =[
		[[1,2,apollo_interface.PAGE_TEXT_OPTIONS_1]],
		[[1,34,apollo_interface.PAGE_TEXT_OPTIONS_2]],
		[[1,34+34,apollo_interface.PAGE_TEXT_OPTIONS_3]],
		[[1,34+34+34,apollo_interface.PAGE_TEXT_OPTIONS_4]]
		]
		for d in inf_sec_1:
			self.BoardSlot[number_title_c_f] = ui.BoardSlot()
			self.BoardSlot[number_title_c_f].SetParent(self.Options_Input)
			self.BoardSlot[number_title_c_f].SetPosition(d[0][0]+6,d[0][1])
			self.BoardSlot[number_title_c_f].MakeTitleBar(150-110)
			self.BoardSlot[number_title_c_f].Show()

			self.BoardSlots_Image[number_title_c_f] = ui.ImageBox()
			self.BoardSlots_Image[number_title_c_f].SetParent(self.BoardSlot[number_title_c_f])
			self.BoardSlots_Image[number_title_c_f].SetPosition(1,0)
			self.BoardSlots_Image[number_title_c_f].LoadImage(apollo_interface.PATCH_COMMON+"/list_item_menu/arrow_bg.png")
			self.BoardSlots_Image[number_title_c_f].Show()

			self.BoardSlots_Button[number_title_c_f] = ui.RadioButton()
			self.BoardSlots_Button[number_title_c_f].SetParent(self.BoardSlots_Image[number_title_c_f])
			self.BoardSlots_Button[number_title_c_f].SetPosition(7,7)
			self.BoardSlots_Button[number_title_c_f].SetUpVisual(apollo_interface.PATCH_COMMON+"/list_item_menu/arrow_empty.png")
			self.BoardSlots_Button[number_title_c_f].SetOverVisual(apollo_interface.PATCH_COMMON+"/list_item_menu/arrow_filled.png")
			self.BoardSlots_Button[number_title_c_f].SetDownVisual(apollo_interface.PATCH_COMMON+"/list_item_menu/arrow_filled.png")
			self.BoardSlots_Button[number_title_c_f].Show()

			self.BoardSlots_Text[number_title_c_f] = ui.TextLine()
			self.BoardSlots_Text[number_title_c_f].SetParent(self.Options_Input)
			self.BoardSlots_Text[number_title_c_f].SetPosition(d[0][0]+40+4,d[0][1]+8)
			self.BoardSlots_Text[number_title_c_f].SetText(d[0][2])
			self.BoardSlots_Text[number_title_c_f].SetPackedFontColor(0xff6c5654)
			self.BoardSlots_Text[number_title_c_f].Hide()

			number_title_c_f += 1

		self.BoardSlots = (
			self.BoardSlots_Button[0],
			self.BoardSlots_Button[1],
			self.BoardSlots_Button[2],
			self.BoardSlots_Button[3],
			
		)
		self.BoardSlots_1 = (
			self.BoardSlots_Text[0],
			self.BoardSlots_Text[1],
			self.BoardSlots_Text[2],
			self.BoardSlots_Text[3],
			
		)

		self.BoardSlots_Button[0].SetEvent((lambda : self.EventsPage(0)))
		self.BoardSlots_Button[0].Down()
		self.BoardSlots_Text[0].SetPackedFontColor(0xffe6d0a2)
		self.BoardSlots_Button[1].SetEvent((lambda : self.EventsPage(1)))
		self.BoardSlots_Button[2].SetEvent((lambda : self.EventsPage(2)))
		self.BoardSlots_Button[3].SetEvent((lambda : self.EventsPage(3)))

	def EventsPage(self,number):
		for btn in self.BoardSlots:
			btn.SetUp()
			for ex in self.BoardSlots_1:
				ex.SetPackedFontColor(0xff6c5654)
		self.BoardSlots[number].Down()
		self.BoardSlots_1[number].SetPackedFontColor(0xffe6d0a2)

		if number == 0:
			self.Player_Block_Status.Hide()
			self.Player_Status.Show()
			self.Player_Grafics.Hide()
			self.Player_Sound.Hide()
			
		if number == 1:
			self.Player_Grafics.Hide()
			self.Player_Block_Status.Show()
			self.Player_Status.Hide()
			self.Player_Sound.Hide()
			
		if number == 2:
			self.Player_Block_Status.Hide()
			self.Player_Status.Hide()
			self.Player_Grafics.Show()
			self.Player_Sound.Hide()
			
		if number == 3:
			self.Player_Sound.Show()
			self.Player_Block_Status.Hide()
			self.Player_Status.Hide()
			self.Player_Grafics.Hide()
			

	def Player_Status_Function(self):
		self.Button_Status ={}
		self.Button_Status_Pvp_Text ={}
		self.Button_Block = {}
		self.Button_Status_Block_Text ={}
		var_1 = 0
		var_2 = 0
		inf_sec_1 =[
		[[40,80,uiScriptLocale.OPTION_PVPMODE_PEACE]],
		[[40+80,80,uiScriptLocale.OPTION_PVPMODE_REVENGE]],
		[[40+80+80,80,uiScriptLocale.OPTION_PVPMODE_GUILD]],
		[[40+80+80+80,80,uiScriptLocale.OPTION_PVPMODE_FREE]]
		]
		inf_sec_2 =[
		[[40,60,uiScriptLocale.OPTION_BLOCK_EXCHANGE]],
		[[40+75+50,60,uiScriptLocale.OPTION_BLOCK_PARTY]],
		[[40,60+30,uiScriptLocale.OPTION_BLOCK_GUILD]],
		[[40+75+50,60+30,uiScriptLocale.OPTION_BLOCK_WHISPER]],
		[[40,60+30+30,uiScriptLocale.OPTION_BLOCK_FRIEND]],
		[[40,60+30+30+30,uiScriptLocale.OPTION_BLOCK_PARTY_REQUEST]]


		]
		for c in inf_sec_1:
			self.Button_Status[var_2] = ui.RadioButton()
			self.Button_Status[var_2].SetParent(self.Player_Status_1)
			self.Button_Status[var_2].SetPosition(c[0][0],c[0][1])
			self.Button_Status[var_2].SetUpVisual(apollo_interface.PATCH_BRADIO+"/empty_03_active.png")
			self.Button_Status[var_2].SetOverVisual(apollo_interface.PATCH_BRADIO+"/filled_03_active.png")
			self.Button_Status[var_2].SetDownVisual(apollo_interface.PATCH_BRADIO+"/filled_03_active.png")
			self.Button_Status[var_2].Show()

			self.Button_Status_Pvp_Text[var_2] = ui.TextLine()
			self.Button_Status_Pvp_Text[var_2].SetParent(self.Button_Status[var_2])
			self.Button_Status_Pvp_Text[var_2].SetPosition(30,2)
			self.Button_Status_Pvp_Text[var_2].SetText(c[0][2])
			self.Button_Status_Pvp_Text[var_2].SetPackedFontColor(apollo_interface.COLOR_NORMAL)
			self.Button_Status_Pvp_Text[var_2].Show()

			var_2 +=1

		self.BoardSlots_2 = (
			self.Button_Status[0],
			self.Button_Status[1],
			self.Button_Status[2],
			self.Button_Status[3],
		)
		self.BoardSlots_2_1 = (
			self.Button_Status_Pvp_Text[0],
			self.Button_Status_Pvp_Text[1],
			self.Button_Status_Pvp_Text[2],
			self.Button_Status_Pvp_Text[3],
		)

		self.BoardSlots_2[0].SetEvent((lambda : self.OpenEvents(0,0)))
		self.BoardSlots_2[0].Down()
		self.BoardSlots_2_1[0].SetPackedFontColor(apollo_interface.COLOR_HOVER)
		self.__OnClickPvPModePeaceButton()
		self.BoardSlots_2[1].SetEvent((lambda : self.OpenEvents(1,0)))
		self.BoardSlots_2[2].SetEvent((lambda : self.OpenEvents(2,0)))
		self.BoardSlots_2[3].SetEvent((lambda : self.OpenEvents(3,0)))

		for e in inf_sec_2:
			self.Button_Block[var_1] = ui.ToggleButton()
			self.Button_Block[var_1].SetParent(self.Player_Status_2)
			self.Button_Block[var_1].SetPosition(e[0][0],e[0][1])
			self.Button_Block[var_1].SetUpVisual(apollo_interface.PATCH_BRADIO+"/empty_03_active.png")
			self.Button_Block[var_1].SetOverVisual(apollo_interface.PATCH_BRADIO+"/filled_01_normal.png")
			self.Button_Block[var_1].SetDownVisual(apollo_interface.PATCH_BRADIO+"/filled_01_normal.png")
			self.Button_Block[var_1].Show()

			self.Button_Status_Block_Text[var_1] = ui.TextLine()
			self.Button_Status_Block_Text[var_1].SetParent(self.Button_Block[var_1])
			self.Button_Status_Block_Text[var_1].SetPosition(30,0)
			self.Button_Status_Block_Text[var_1].SetText(e[0][2])
			self.Button_Status_Block_Text[var_1].SetPackedFontColor(apollo_interface.COLOR_NORMAL)
			self.Button_Status_Block_Text[var_1].Show()

			var_1 +=1

		self.BoardSlots_3 = (
			self.Button_Block[0],
			self.Button_Block[1],
			self.Button_Block[2],
			self.Button_Block[3],
			self.Button_Block[4],
			self.Button_Block[5],
		)

		self.BoardSlots_3_1 = (
			self.Button_Status_Block_Text[0],
			self.Button_Status_Block_Text[1],
			self.Button_Status_Block_Text[2],
			self.Button_Status_Block_Text[3],
			self.Button_Status_Block_Text[4],
			self.Button_Status_Block_Text[5],
		)


		self.blockButtonList = []
		self.blockButtonList.append(self.Button_Block[0])
		self.blockButtonList.append(self.Button_Block[1])
		self.blockButtonList.append(self.Button_Block[2])
		self.blockButtonList.append(self.Button_Block[3])
		self.blockButtonList.append(self.Button_Block[4])
		#self.blockButtonList.append(self.Button_Block[5])

		self.blockButtonList[0].SetToggleUpEvent(self.__OnClickBlockExchangeButton)
		self.blockButtonList[1].SetToggleUpEvent(self.__OnClickBlockPartyButton)
		self.blockButtonList[2].SetToggleUpEvent(self.__OnClickBlockGuildButton)
		self.blockButtonList[3].SetToggleUpEvent(self.__OnClickBlockWhisperButton)
		self.blockButtonList[4].SetToggleUpEvent(self.__OnClickBlockFriendButton)
		self.blockButtonList[0].SetToggleDownEvent(self.__OnClickBlockExchangeButton)
		self.blockButtonList[1].SetToggleDownEvent(self.__OnClickBlockPartyButton)
		self.blockButtonList[2].SetToggleDownEvent(self.__OnClickBlockGuildButton)
		self.blockButtonList[3].SetToggleDownEvent(self.__OnClickBlockWhisperButton)
		self.blockButtonList[4].SetToggleDownEvent(self.__OnClickBlockFriendButton)

	def Player_Block_Function(self):
		self.Button_V ={}
		self.Button_V_Text_2 ={}
		self.Button_V_Text_3 ={}
		self.Button_V_Text_4 ={}
		self.Button_V_1 = {}
		number_title_d = 0
		info_d_f =[
		[[40+100,60,uiScriptLocale.OPTION_NAME_COLOR],[uiScriptLocale.OPTION_NAME_COLOR_NORMAL,uiScriptLocale.OPTION_NAME_COLOR_EMPIRE]],
		[[40+100,60+35,uiScriptLocale.OPTION_TARGET_BOARD],[uiScriptLocale.OPTION_TARGET_BOARD_NO_VIEW,uiScriptLocale.OPTION_TARGET_BOARD_VIEW]],
		[[40+100,60+35+35,uiScriptLocale.OPTION_VIEW_CHAT],[uiScriptLocale.OPTION_VIEW_CHAT_ON,uiScriptLocale.OPTION_VIEW_CHAT_OFF]],
		[[40+100,60+35+35+35,uiScriptLocale.OPTION_ALWAYS_SHOW_NAME],[uiScriptLocale.OPTION_ALWAYS_SHOW_NAME_ON,uiScriptLocale.OPTION_ALWAYS_SHOW_NAME_OFF]],
		[[40+100,60+35+35+35+35,uiScriptLocale.OPTION_EFFECT],[uiScriptLocale.OPTION_VIEW_CHAT_ON,uiScriptLocale.OPTION_VIEW_CHAT_OFF]],
		[[40+100,60+35+35+35+35+35,uiScriptLocale.OPTION_SALESTEXT],[uiScriptLocale.OPTION_SALESTEXT_VIEW_ON,uiScriptLocale.OPTION_SALESTEXT_VIEW_OFF]]

		]

		for x in info_d_f:
			self.Button_V[number_title_d] = ui.RadioButton()
			self.Button_V[number_title_d].SetParent(self.Player_Block_Status)
			self.Button_V[number_title_d].SetPosition(x[0][0],x[0][1])
			self.Button_V[number_title_d].SetUpVisual(apollo_interface.PATCH_CHECK+"empty_03_active.png")
			self.Button_V[number_title_d].SetOverVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_V[number_title_d].SetDownVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_V[number_title_d].Show()

			self.Button_V_Text_3[number_title_d] = ui.TextLine()
			self.Button_V_Text_3[number_title_d].SetParent(self.Button_V[number_title_d])
			self.Button_V_Text_3[number_title_d].SetPosition(30,3)
			self.Button_V_Text_3[number_title_d].SetText(x[1][0])
			self.Button_V_Text_3[number_title_d].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			self.Button_V_Text_3[number_title_d].Show()

			self.Button_V_1[number_title_d] = ui.RadioButton()
			self.Button_V_1[number_title_d].SetParent(self.Player_Block_Status)
			self.Button_V_1[number_title_d].SetPosition(x[0][0]+100,x[0][1])
			self.Button_V_1[number_title_d].SetUpVisual(apollo_interface.PATCH_CHECK+"empty_03_active.png")
			self.Button_V_1[number_title_d].SetOverVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_V_1[number_title_d].SetDownVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_V_1[number_title_d].Show()

			self.Button_V_Text_4[number_title_d] = ui.TextLine()
			self.Button_V_Text_4[number_title_d].SetParent(self.Button_V_1[number_title_d])
			self.Button_V_Text_4[number_title_d].SetPosition(30,3)
			self.Button_V_Text_4[number_title_d].SetText(x[1][1])
			self.Button_V_Text_4[number_title_d].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			self.Button_V_Text_4[number_title_d].Show()

			self.Button_V_Text_2[number_title_d] = ui.TextLine()
			self.Button_V_Text_2[number_title_d].SetParent(self.Button_V[number_title_d])
			self.Button_V_Text_2[number_title_d].SetPosition(-x[0][0]+40,3)
			self.Button_V_Text_2[number_title_d].SetText(x[0][2]+":")
			self.Button_V_Text_2[number_title_d].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			self.Button_V_Text_2[number_title_d].Show()

			number_title_d +=1

		self.BoardSlots_5 = (
			self.Button_V[0],
			self.Button_V_1[0],
		)
		self.BoardSlots_6 = (
			self.Button_V[1],
			self.Button_V_1[1],
		)
		self.BoardSlots_7 = (
			self.Button_V[2],
			self.Button_V_1[2],
		)
		self.BoardSlots_8 = (
			self.Button_V[3],
			self.Button_V_1[3],
		)
		self.BoardSlots_9 = (
			self.Button_V[4],
			self.Button_V_1[4],
		)

		self.BoardSlots_10 = (
			self.Button_V[5],
			self.Button_V_1[5],
		)

		self.BoardSlots_5[0].SetEvent((lambda : self.OpenEvents1(0,0)))
		self.BoardSlots_5[1].SetEvent((lambda : self.OpenEvents1(0,1)))

		self.BoardSlots_6[0].SetEvent((lambda : self.OpenEvents1(1,0)))
		self.BoardSlots_6[1].SetEvent((lambda : self.OpenEvents1(1,1)))

		self.BoardSlots_7[0].SetEvent((lambda : self.OpenEvents1(2,0)))
		self.BoardSlots_7[1].SetEvent((lambda : self.OpenEvents1(2,1)))

		self.BoardSlots_8[0].SetEvent((lambda : self.OpenEvents1(3,0)))
		self.BoardSlots_8[1].SetEvent((lambda : self.OpenEvents1(3,1)))


		self.BoardSlots_9[0].SetEvent((lambda : self.OpenEvents1(4,0)))
		self.BoardSlots_9[1].SetEvent((lambda : self.OpenEvents1(4,1)))

		self.BoardSlots_10[0].SetEvent((lambda : self.OpenEvents1(5,0)))
		self.BoardSlots_10[1].SetEvent((lambda : self.OpenEvents1(5,1)))

		self.__ClickRadioButton(self.BoardSlots_5, constInfo.GET_CHRNAME_COLOR_INDEX())
		self.__ClickRadioButton(self.BoardSlots_6, constInfo.GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD())

		self.TextColor(0,constInfo.GET_CHRNAME_COLOR_INDEX())
		self.TextColor(1,constInfo.GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD())

	def Player_Grafics_Function(self):
		lineStep = 70
		lineStep1 = 70
		self.button_viz_1 = []
		self.button_viz_11 = []
		self.button_viz_12 =[]
		self.apollo_13 = {}
		self.apollo_14 = {}
		self.apollo_15 = {}
		for i in xrange(2):
			inverseLineIndex = 2 - i - 1
			yPos = 28 + inverseLineIndex*lineStep
			self.Button_Viz = ui.RadioButton()
			self.Button_Viz.SetParent(self.Player_Grafics_1)
			self.Button_Viz.SetPosition(yPos+90,50)
			self.Button_Viz.SetUpVisual(apollo_interface.PATCH_CHECK+"empty_03_active.png")
			self.Button_Viz.SetOverVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_Viz.SetDownVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_Viz.Show()
			self.apollo_13[inverseLineIndex] = self.Button_Viz
			self.button_viz_1.append(self.Button_Viz)


		number_title_v = 0
		number_title_v_1 = 0
		number_title_v_2 = 0
		number_title_v_3 = 0
		number_title_v_4 = 0
		self.Button_Viz_Text ={}
		self.Button_Viz_1_Text ={}
		self.Button_Viz_2_Text = {}
		self.Button_Viz_3 = {}
		self.Button_Viz_4 ={}
		info_d_v =[
		[[30,50+2],[uiScriptLocale.OPTION_TILING+":"]],
		[[30+95+20,50+2],[uiScriptLocale.OPTION_TILING_CPU]],
		[[30+95+70+20,50+2],[uiScriptLocale.OPTION_TILING_GPU]]
		]
		info_d_1 =[

		[[30,19],[uiScriptLocale.OPTION_FOG+":"]],
		[[30+95+20,19],[uiScriptLocale.OPTION_FOG_DENSE]],
		[[30+95+70+20,19],[uiScriptLocale.OPTION_FOG_MIDDLE]],
		[[30+95+70+70+20,19],[uiScriptLocale.OPTION_FOG_LIGHT]],

		[[30,50+2],[uiScriptLocale.OPTION_CAMERA_DISTANCE+":"]],
		[[30+95+20,50+2],[uiScriptLocale.OPTION_CAMERA_DISTANCE_SHORT]],
		[[30+95+70+20,50+2],[uiScriptLocale.OPTION_CAMERA_DISTANCE_LONG]]

		]

		info_d_2 =[

		[[30,19],[apollo_interface.SHOW_NIGHT_TXT]],
		[[30+95+20,19],[apollo_interface.ON]],
		[[30+95+70+20,19],[apollo_interface.OFF]],

		[[30,50+2],[apollo_interface.SHOW_SNOW_TXT]],
		[[30+95+20,50+2],[apollo_interface.ON]],
		[[30+95+70+20,50+2],[apollo_interface.OFF]],

		[[30,50+2+30],[apollo_interface.SHOW_SNOW_TXT]],
		[[30+95+20,50+2+30],[apollo_interface.ON]],
		[[30+95+70+20,50+2+30],[apollo_interface.OFF]]

		]

		info_d_4 =[

		[[98,15]],
		[[98,19+29]],
		[[98,19+29+29]]

		]

		for v1 in info_d_v:
			self.Button_Viz_Text[number_title_v] = ui.TextLine()
			self.Button_Viz_Text[number_title_v].SetParent(self.Player_Grafics_1)
			self.Button_Viz_Text[number_title_v].SetPosition(v1[0][0],v1[0][1])
			self.Button_Viz_Text[number_title_v].SetText(v1[1][0])
			self.Button_Viz_Text[number_title_v].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			self.Button_Viz_Text[number_title_v].Show()
			number_title_v +=1

		for i in xrange(3):
			inverseLineIndex1 = 2 - i - 1
			inverseLineIndex1_1 = 3 - i - 1
			yPos1 = 28 + inverseLineIndex1*lineStep1
			self.Button_Viz_1_1 = ui.RadioButton()
			self.Button_Viz_1_1.SetParent(self.Player_Grafics_2)
			self.Button_Viz_1_1.SetPosition(yPos1+140+20,15)
			self.Button_Viz_1_1.SetUpVisual(apollo_interface.PATCH_CHECK+"empty_03_active.png")
			self.Button_Viz_1_1.SetOverVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_Viz_1_1.SetDownVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_Viz_1_1.Show()
			self.apollo_14[inverseLineIndex1_1] = self.Button_Viz_1_1
			self.button_viz_11.append(self.Button_Viz_1_1)

		for v2 in info_d_1:
			self.Button_Viz_1_Text[number_title_v_1] = ui.TextLine()
			self.Button_Viz_1_Text[number_title_v_1].SetParent(self.Player_Grafics_2)
			self.Button_Viz_1_Text[number_title_v_1].SetPosition(v2[0][0],v2[0][1])
			self.Button_Viz_1_Text[number_title_v_1].SetText(v2[1][0])
			self.Button_Viz_1_Text[number_title_v_1].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			self.Button_Viz_1_Text[number_title_v_1].Show()
			number_title_v_1 +=1

		for i in xrange(2):
			inverseLineIndex1 = 2 - i - 1
			yPos2 = 28 + inverseLineIndex1*lineStep
			self.Button_Viz_1_2 = ui.RadioButton()
			self.Button_Viz_1_2.SetParent(self.Player_Grafics_2)
			self.Button_Viz_1_2.SetPosition(yPos2+70+20,50)
			self.Button_Viz_1_2.SetUpVisual(apollo_interface.PATCH_CHECK+"empty_03_active.png")
			self.Button_Viz_1_2.SetOverVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_Viz_1_2.SetDownVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_Viz_1_2.Show()
			self.apollo_15[inverseLineIndex1] = self.Button_Viz_1_2
			self.button_viz_12.append(self.Button_Viz_1_2)

		for v3 in info_d_2:
			self.Button_Viz_2_Text[number_title_v_2] = ui.TextLine()
			self.Button_Viz_2_Text[number_title_v_2].SetParent(self.Player_Grafics_3)
			self.Button_Viz_2_Text[number_title_v_2].SetPosition(v3[0][0],v3[0][1])
			self.Button_Viz_2_Text[number_title_v_2].SetText(v3[1][0])
			self.Button_Viz_2_Text[number_title_v_2].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			self.Button_Viz_2_Text[number_title_v_2].Show()
			number_title_v_2 +=1

		for v4 in info_d_4:
			self.Button_Viz_3[number_title_v_3] = ui.RadioButton()
			self.Button_Viz_3[number_title_v_3].SetParent(self.Player_Grafics_3)
			self.Button_Viz_3[number_title_v_3].SetPosition(v4[0][0]+20,v4[0][1])
			self.Button_Viz_3[number_title_v_3].SetUpVisual(apollo_interface.PATCH_CHECK+"empty_03_active.png")
			self.Button_Viz_3[number_title_v_3].SetOverVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_Viz_3[number_title_v_3].SetDownVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_Viz_3[number_title_v_3].Show()
			number_title_v_3 +=1

		for v5 in info_d_4:
			self.Button_Viz_4[number_title_v_4] = ui.RadioButton()
			self.Button_Viz_4[number_title_v_4].SetParent(self.Player_Grafics_3)
			self.Button_Viz_4[number_title_v_4].SetPosition(v5[0][0]+70+20,v5[0][1])
			self.Button_Viz_4[number_title_v_4].SetUpVisual(apollo_interface.PATCH_CHECK+"empty_03_active.png")
			self.Button_Viz_4[number_title_v_4].SetOverVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_Viz_4[number_title_v_4].SetDownVisual(apollo_interface.PATCH_CHECK+"filled_01_normal.png")
			self.Button_Viz_4[number_title_v_4].Show()
			number_title_v_4 +=1


		self.BoardTexture_1 = (
			self.apollo_13[0],
			self.apollo_13[1],
		)
		self.BoardTexture_2 = (
			self.apollo_14[0],
			self.apollo_14[1],
			self.apollo_14[2],
		)
		self.BoardTexture_3 = (
			self.apollo_15[0],
			self.apollo_15[1],
		)
		self.BoardTexture_4 = (
			self.Button_Viz_3[0],
			self.Button_Viz_4[0],
		)
		self.BoardTexture_5 = (
			self.Button_Viz_3[1],
			self.Button_Viz_4[1],
		)
		self.BoardTexture_6 = (
			self.Button_Viz_3[2],
			self.Button_Viz_4[2],
		)

		self.BoardTexture_6[0].Hide()
		self.BoardTexture_6[1].Hide()
		self.Button_Viz_2_Text[6].Hide()
		self.Button_Viz_2_Text[7].Hide()
		self.Button_Viz_2_Text[8].Hide()

		self.BoardTexture_1[0].SetEvent((lambda : self.OpenEvents2(0,0)))
		self.BoardTexture_1[1].SetEvent((lambda : self.OpenEvents2(0,1)))

		self.BoardTexture_2[0].SetEvent((lambda : self.OpenEvents2(1,0)))
		self.BoardTexture_2[1].SetEvent((lambda : self.OpenEvents2(1,1)))
		self.BoardTexture_2[2].SetEvent((lambda : self.OpenEvents2(1,2)))

		self.BoardTexture_3[0].SetEvent((lambda : self.OpenEvents2(2,0)))
		self.BoardTexture_3[1].SetEvent((lambda : self.OpenEvents2(2,1)))

		self.BoardTexture_4[0].SetEvent((lambda : self.OpenEvents2(3,0)))
		self.BoardTexture_4[1].SetEvent((lambda : self.OpenEvents2(3,1)))

		self.BoardTexture_5[0].SetEvent((lambda : self.OpenEvents2(4,0)))
		self.BoardTexture_5[1].SetEvent((lambda : self.OpenEvents2(4,1)))


		self.__ClickRadioButton(self.BoardTexture_2, constInfo.GET_FOG_LEVEL_INDEX())
		self.__ClickRadioButton(self.BoardTexture_3, constInfo.GET_CAMERA_MAX_DISTANCE_INDEX())
		self.__ClickRadioButton(self.BoardTexture_4, DayMode)
		self.__ClickRadioButton(self.BoardTexture_5, ShowMode)

		self.TextColor2(constInfo.GET_FOG_LEVEL_INDEX()+1,constInfo.GET_FOG_LEVEL_INDEX(),1)
		self.TextColor2(constInfo.GET_CAMERA_MAX_DISTANCE_INDEX()+5,constInfo.GET_CAMERA_MAX_DISTANCE_INDEX(),2)
		self.TextColor2(DayMode+1,DayMode,3)
		self.TextColor2(ShowMode+4,ShowMode,4)

	def Player_Sound_Function(self):
		self.slider_effect = ui.SliderBar()
		self.slider_effect.SetParent(self.Player_Sound)
		self.slider_effect.SetPosition(160,60)
		self.slider_effect.SetEvent((lambda : self.OnChangeSoundVolume(0)))
		self.slider_effect.SetSliderPos(float(systemSetting.GetMusicVolume()))
		self.slider_effect.Show()

		self.slider_music = ui.SliderBar()
		self.slider_music.SetParent(self.Player_Sound)
		self.slider_music.SetPosition(160,60+40)
		self.slider_music.SetEvent((lambda : self.OnChangeSoundVolume(1)))
		self.slider_music.SetSliderPos(float(systemSetting.GetSoundVolume()) / 5.0)
		self.slider_music.Show()

		self.slide_slot = {}
		self.textapollo = {}
		self.textapollo_title = {}
		number_title_s = 0
		slider_info = [
		[[98,34+20],[50],[apollo_interface.MUSIC]],
		[[98,34+60],[50],[apollo_interface.SOUND]],
		[[98,34+40+60],[140],[apollo_interface.MUSIC_TITLE_TEXT]]

		]
		for i in slider_info:

			self.textapollo_title[number_title_s] = ui.TextLine()
			self.textapollo_title[number_title_s].SetParent(self.Player_Sound)
			self.textapollo_title[number_title_s].SetPosition(14,i[0][1]+8)
			self.textapollo_title[number_title_s].SetText(i[2][0])
			self.textapollo_title[number_title_s].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			self.textapollo_title[number_title_s].Show()

			self.slide_slot[number_title_s] = ui.InputNew()
			self.slide_slot[number_title_s].SetParent(self.Player_Sound)
			self.slide_slot[number_title_s].SetPosition(i[0][0],i[0][1])
			self.slide_slot[number_title_s].MakeTitleBar(i[1][0])
			self.slide_slot[number_title_s].Show()

			self.textapollo[number_title_s] = ui.TextLine()
			self.textapollo[number_title_s].SetParent(self.slide_slot[number_title_s])
			self.textapollo[number_title_s].SetPosition(14,8)
			self.textapollo[number_title_s].SetText("0/5")
			self.textapollo[number_title_s].SetPackedFontColor(apollo_interface.COLOR_TEXT2)
			self.textapollo[number_title_s].Show()


			number_title_s +=1

		self.PorcentajeSound(self.slider_effect.GetSliderPos(),0)
		self.PorcentajeSound(self.slider_music.GetSliderPos(),1)

		if musicInfo.fieldMusic==musicInfo.METIN2THEMA:
			self.textapollo[2].SetText(uiSelectMusic.DEFAULT_THEMA)
		else:
			self.textapollo[2].SetText(musicInfo.fieldMusic[:MUSIC_FILENAME_MAX_LEN])

		self.slide_button = ui.Button()
		self.slide_button.SetParent(self.Player_Sound)
		self.slide_button.SetPosition(242,34+60+42)
		self.slide_button.SetUpVisual("%s/costume/btn_option_on.png" % apollo_interface.PATCH_COMMON)
		self.slide_button.SetOverVisual("%s/costume/btn_option_ds.png" % apollo_interface.PATCH_COMMON)
		self.slide_button.SetDownVisual("%s/costume/btn_option_dn.png" % apollo_interface.PATCH_COMMON)
		self.slide_button.SetText(apollo_interface.CHANGE_MUSIC_BUTTON_TEXT)
		self.slide_button.SAFE_SetEvent(self.__OnClickChangeMusicButton)
		self.slide_button.Show()

	def OpenEvents(self,index,board):
		if board == 0:
			for btn in self.BoardSlots_2:
				btn.SetUp()
				for ex in self.BoardSlots_2_1:
					ex.SetPackedFontColor(apollo_interface.COLOR_NORMAL)
			self.BoardSlots_2[index].Down()
			self.BoardSlots_2_1[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
			if index == 0:
				self.__OnClickPvPModePeaceButton()
			if index == 1:
				self.__OnClickPvPModeRevengeButton()
			if index == 2:
				self.__OnClickPvPModeGuildButton()
			if index == 3:
				self.__OnClickPvPModeFreeButton()
		if board == 1:
			if index == 0:
				self.__OnClickBlockExchangeButton()
			if index == 1:
				self.__OnClickBlockPartyButton()
			if index == 2:
				self.__OnClickBlockGuildButton()
			if index == 3:
				self.__OnClickBlockWhisperButton()
			if index == 4:
				self.__OnClickBlockFriendButton()
			if index == 5:
				self.__OnClickBlockPartyRequest()

	def OpenEvents1(self,index,arg):
		if index == 0:
			self.__SetNameColorMode(arg)
		if index == 1:
			self.__SetTargetBoardViewMode(arg)
		if index == 2:
			self.__OnClickViewChatOnButton(arg)
		if index == 3:
			self.__OnClickAlwaysShowName(arg)
		if index == 4:
			self.__OnClickShowDamage(arg)
		if index == 5:
			self.__OnClickSalesTextOnButton(arg)

		self.TextColor(index,arg)

	def OpenEvents2(self,index,arg):
		if index == 0:
			self.__OnClickTilingModeCPUButton(arg)
		if index == 1:
			self.__SetFogLevel(arg)
		if index == 2:
			self.__SetCameraMode(arg)
		if index ==3:
			self.__DayMode(arg)
		if index == 4:
			self.__SnowMode(arg)

	def OnUpdate(self):
		global OnTest1
		global movement
		global movement1
		global movement2
		global movement3
		global movement4

		speed_movem = 3
		if OnTest1 == 1:
			if movement >= 0 and movement <= 143-(143-110):
				movement += speed_movem
				self.Options_Input.SetSize(143-95+movement,323)
			elif movement >= 143:
				OnTest1 = 0
				movement = 0
				movement1 = 0
				movement2 = 0
				movement3 = 0
				movement4 = 0

			if movement2 >= 0 and movement2 <= 541-(541-110):
				movement2 +=speed_movem
				self.SetSize(541-108+movement2,402)
				self.Options_Page.SetSize(541-115+movement2,400)
				self.Board.SetSize(541-103+movement2,370)
				self.TitleName.SetParent(self)
				self.TitleName.SetPosition(+20,-184)
				self.TitleName.SetText(apollo_interface.OPTION_TITLE)
				self.TitleName.SetHorizontalAlignCenter()
			else:
				for i in xrange(0,4):
					self.BoardSlots_Text[i].Show()

			if movement1 >= 0 and movement1 <= 441-56-(441-110-56):
				movement1 +=speed_movem
				self.TitleBar.SetWidth(541-110-15+movement1)
				self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close))

			if movement3 >= 0 and movement3 <= 150-(150-110):
				movement3 +=speed_movem
				for a in xrange(0,4):
					self.BoardSlot[a].MakeTitleBar(150-110+movement3)
					self.BoardSlots_Image[a].Show()
					self.BoardSlots_Image[a].SetTop()

			if movement4 >= 0 and movement4 <= 370-(257):
				movement4 +=speed_movem
				self.ButtonExpande.SetParent(self)
				self.ButtonExpande.SetPosition(347+movement4,12)
				self.ButtonExpande.Show()

		elif OnTest1 == 2:
			if movement >= 0 and movement <= 143-109-(-143):
				movement +=speed_movem
				self.Options_Input.SetSize(143-movement,323)
			if movement >= 109:
				OnTest1 = 0

			if movement1 >= 0 and movement1 <= 541-110-56-(-441-56):
				movement1 +=speed_movem
				self.TitleBar.SetWidth(541-20-movement1)
				self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close))

			if movement2 >= 0 and movement2 <= 541-110-(-441):
				movement2 +=speed_movem
				self.SetSize(541-movement2,400)
				self.Options_Page.SetSize(541-movement2,400)
				self.Board.SetSize(545-movement2,370)
				self.TitleName.SetParent(self)
				self.TitleName.SetPosition(20,-183)
				self.TitleName.SetText(apollo_interface.OPTION_TITLE)
				self.TitleName.SetHorizontalAlignCenter()
				for i in xrange(0,4):
					self.BoardSlots_Text[i].Hide()


			if movement3 >= 0 and movement3 <= 150-110-(-150):
				movement3 +=speed_movem
				for a in xrange(0,4):
					self.BoardSlot[a].MakeTitleBar(150-movement3)
					self.BoardSlots_Image[a].Show()
					self.BoardSlots_Image[a].SetTop()

			if movement4 >= 0 and movement4 <= 260-(-370):
				movement4 +=speed_movem
				self.ButtonCollapse.SetParent(self)
				self.ButtonCollapse.SetPosition(455-movement4,12)
				self.ButtonCollapse.Show()

		if self.isLoaded_1 == 1:
			return

	def TextColor(self,index,arg):
		if arg == 0:
			self.Button_V_Text_3[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
			self.Button_V_Text_4[index].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
		else:
			self.Button_V_Text_4[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
			self.Button_V_Text_3[index].SetPackedFontColor(apollo_interface.COLOR_TEXT1)

	def TextColor2(self,index,arg,board):
		if board == 0:
			if arg == 0:
				self.Button_Viz_Text[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
				self.Button_Viz_Text[2].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			else:
				self.Button_Viz_Text[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
				self.Button_Viz_Text[1].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
		if board == 1:
			if arg == 0:
				self.Button_Viz_1_Text[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
				self.Button_Viz_1_Text[2].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
				self.Button_Viz_1_Text[3].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			elif arg ==1:
				self.Button_Viz_1_Text[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
				self.Button_Viz_1_Text[1].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
				self.Button_Viz_1_Text[3].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			else:
				self.Button_Viz_1_Text[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
				self.Button_Viz_1_Text[2].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
				self.Button_Viz_1_Text[1].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
		if board == 2:
			if arg == 0:
				self.Button_Viz_1_Text[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
				self.Button_Viz_1_Text[6].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			elif arg ==1:
				self.Button_Viz_1_Text[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
				self.Button_Viz_1_Text[5].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
		if board ==3:
			if arg == 0:
				self.Button_Viz_2_Text[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
				self.Button_Viz_2_Text[2].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			else:
				self.Button_Viz_2_Text[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
				self.Button_Viz_2_Text[1].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
		if board ==4:
			if arg == 0:
				self.Button_Viz_2_Text[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
				self.Button_Viz_2_Text[5].SetPackedFontColor(apollo_interface.COLOR_TEXT1)
			else:
				self.Button_Viz_2_Text[index].SetPackedFontColor(apollo_interface.COLOR_HOVER)
				self.Button_Viz_2_Text[4].SetPackedFontColor(apollo_interface.COLOR_TEXT1)

	def OnChangeSoundVolume(self,index):
		if index == 0:
			pos = self.slider_effect.GetSliderPos()
			snd.SetMusicVolume(pos * net.GetFieldMusicVolume())
			systemSetting.SetMusicVolume(pos)
		else:
			pos = self.slider_music.GetSliderPos()
			snd.SetSoundVolumef(pos)
			systemSetting.SetSoundVolumef(pos)
		self.PorcentajeSound(pos,index)

	def PorcentajeSound(self,pos,index):
		if pos == 0.0:
			self.textapollo[index].SetText("0/5")
		elif pos > 0.0 and pos <= 0.2:
			self.textapollo[index].SetText("1/5")
		elif pos >= 0.3 and pos <= 0.4:
			self.textapollo[index].SetText("2/5")
		elif pos >= 0.5 and pos <= 0.6:
			self.textapollo[index].SetText("3/5")
		elif pos >= 0.7 and pos <= 0.8:
			self.textapollo[index].SetText("4/5")
		elif pos >= 0.9:
			self.textapollo[index].SetText("5/5")

	def __OnClickChangeMusicButton(self):
		if not self.musicListDlg:

			self.musicListDlg=uiSelectMusic.FileListDialog()
			self.musicListDlg.SAFE_SetSelectEvent(self.__OnChangeMusic)

		self.musicListDlg.Open()

	def __OnChangeMusic(self, fileName):
		self.textapollo[2].SetText(fileName[:MUSIC_FILENAME_MAX_LEN])

		if musicInfo.fieldMusic != "":
			snd.FadeOutMusic("BGM/"+ musicInfo.fieldMusic)

		if fileName==uiSelectMusic.DEFAULT_THEMA:
			musicInfo.fieldMusic=musicInfo.METIN2THEMA
		else:
			musicInfo.fieldMusic=fileName

		musicInfo.SaveLastPlayFieldMusic()

		if musicInfo.fieldMusic != "":
			snd.FadeInMusic("BGM/" + musicInfo.fieldMusic)

	def __OnClickTilingModeCPUButton(self,index):
		self.__NotifyChatLine(localeInfo.SYSTEM_OPTION_TILING_EXIT)
		self.TextColor2(index+1,index,0)
		if 0 == index:
			background.EnableSoftwareTiling(1)
		else:
			background.EnableSoftwareTiling(0)

		self.tilingMode = index
		net.Exipngme()

		self.__ClickRadioButton(self.BoardTexture_1, index)

	def __SetFogLevel(self, index):
		constInfo.SET_FOG_LEVEL_INDEX(index)
		self.__ClickRadioButton(self.BoardTexture_2, index)

		self.TextColor2(index+1,index,1)

	def __SetCameraMode(self, index):
		constInfo.SET_CAMERA_MAX_DISTANCE_INDEX(index)
		self.__ClickRadioButton(self.BoardTexture_3, index)

		self.TextColor2(index+5,index,2)

	def __DayMode(self, index):
		if 0 == index:
			background.RegisterEnvironmentData(1, apollo_interface.DAY)
			background.SetEnvironmentData(1)
		else:
			background.RegisterEnvironmentData(1, apollo_interface.NIGHT)
			background.SetEnvironmentData(0)

		DayMode = index
		self.TextColor2(index+1,index,3)
		self.__ClickRadioButton(self.BoardTexture_4, index)

	def __SnowMode(self, index):
		if index == 0:
			background.EnableSnow(1)
			constInfo.ShowMode = 0
		else:
			background.EnableSnow(0)
			constInfo.ShowMode = 1

		self.TextColor2(index+4,index,4)
		self.__ClickRadioButton(self.BoardTexture_5, index)

	def __NotifyChatLine(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, text)

	def __SetNameColorMode(self, index):
		constInfo.SET_CHRNAME_COLOR_INDEX(index)
		self.__ClickRadioButton(self.BoardSlots_5, index)

	def __SetTargetBoardViewMode(self, flag):
		constInfo.SET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD(flag)
		self.__ClickRadioButton(self.BoardSlots_6, flag)

	def __OnClickViewChatOnButton(self, flag):
		global viewChatMode
		if flag == 0:
			viewChatMode = 1
			systemSetting.SetViewChatFlag(viewChatMode)
		else:
			viewChatMode = 0
			systemSetting.SetViewChatFlag(viewChatMode)

		self.__ClickRadioButton(self.BoardSlots_7, flag)

	def __OnClickAlwaysShowName(self, index):
		if index == 0:
			systemSetting.SetAlwaysShowNameFlag(TRUE)
		else:
			systemSetting.SetAlwaysShowNameFlag(FALSE)

		self.__ClickRadioButton(self.BoardSlots_8, index)

	def __OnClickShowDamage(self, index):
		if index == 0:
			systemSetting.SetShowDamageFlag(TRUE)
		else:
			systemSetting.SetShowDamageFlag(FALSE)

		self.__ClickRadioButton(self.BoardSlots_9, index)

	def __OnClickSalesTextOnButton(self, index):
		if index == 0:
			systemSetting.SetShowSalesTextFlag(TRUE)
			uiPrivateShopBuilder.UpdateADBoard()
		else:
			systemSetting.SetShowSalesTextFlag(FALSE)

		self.__ClickRadioButton(self.BoardSlots_10, index)

	def __ClickRadioButton(self, buttonList, buttonIndex):
		selButton=buttonList[buttonIndex]
		for eachButton in buttonList:
			eachButton.SetUp()

		selButton.Down()

	def RefreshTextures(self):
		if background.IsSoftwareTiling():
			self.__ClickRadioButton(self.BoardTexture_1, 0)
			self.TextColor2(1,0,0)
		else:
			self.__ClickRadioButton(self.BoardTexture_1, 1)
			self.TextColor2(2,1,0)

	def RefreshOptiones(self):
		if systemSetting.IsAlwaysShowName():
			self.BoardSlots_8[0].Down()
			self.BoardSlots_8[1].SetUp()
			self.TextColor(3,0)
		else:
			self.BoardSlots_8[0].SetUp()
			self.BoardSlots_8[1].Down()
			self.TextColor(3,1)

		if systemSetting.IsShowDamage():
			self.BoardSlots_9[0].Down()
			self.BoardSlots_9[1].SetUp()
			self.TextColor(4,0)
		else:
			self.BoardSlots_9[0].SetUp()
			self.BoardSlots_9[1].Down()
			self.TextColor(4,1)

		if systemSetting.IsShowSalesText():
			self.BoardSlots_10[0].Down()
			self.BoardSlots_10[1].SetUp()
			self.TextColor(5,0)
		else:
			self.BoardSlots_10[0].SetUp()
			self.BoardSlots_10[1].Down()
			self.TextColor(5,1)

		if systemSetting.IsViewChat():
			self.BoardSlots_7[0].Down()
			self.BoardSlots_7[1].SetUp()
			self.TextColor(2,0)
		else:
			self.BoardSlots_7[0].SetUp()
			self.BoardSlots_7[1].Down()
			self.TextColor(2,1)

	def __OnClickBlockExchangeButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_EXCHANGE))

	def __OnClickBlockPartyButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_PARTY))

	def __OnClickBlockGuildButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_GUILD))

	def __OnClickBlockWhisperButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_WHISPER))

	def __OnClickBlockFriendButton(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_FRIEND))

	def RefreshBlock(self):
		global blockMode
		for i in xrange(len(self.blockButtonList)):
			if 0 != (blockMode & (1 << i)):
				self.blockButtonList[i].Down()
			else:
				self.blockButtonList[i].SetUp()

	def OnBlockMode(self, mode):
		global blockMode
		blockMode = mode
		self.RefreshBlock()


	def __OnClickPvPModePeaceButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 0", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeRevengeButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 1", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeGuildButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return


		if 0 == player.GetGuildID():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_CANNOT_SET_GUILD_MODE)
			return

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 4", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeFreeButton(self):
		if self.__CheckPvPProtectedLevelPlayer():
			return

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 2", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __CheckPvPProtectedLevelPlayer(self):
		if player.GetStatus(player.LEVEL)<constInfo.PVPMODE_PROTECTED_LEVEL:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_PROTECT % (constInfo.PVPMODE_PROTECTED_LEVEL))
			return 1


	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def Close(self):
		self.Hide()
