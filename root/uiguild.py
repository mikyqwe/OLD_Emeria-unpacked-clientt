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
import guild
import uiScriptLocale
import app
import uiUploadMark
import grpText
import skill
import uiCommon
import grp
from _weakref import proxy
import background
import miniMap
import chr
import apollo_interface
import uitooltipGold

def unsigned32(n):
	return n & 0xFFFFFFFFL


OnTest1 = 0
movement = 0
movement1 = 0
movement2 = 0
movement3 = 0
movement4 = 0
active = 0

GRADE_ADD_MEMBER_AUTHORITY = 1
GRADE_REMOVE_MEMBER_AUTHORITY = 2
GRADE_NOTICE_AUTHORITY = 3
GRADE_SKILL_AUTHORITY = 4


def unsigned32(n):
	return n & 0xFFFFFFFFL

def NumberToMoneyString(n):
	return localeInfo.NumberToMoneyString(n)

MATERIAL_STONE_INDEX = 0
MATERIAL_LOG_INDEX = 1
MATERIAL_PLYWOOD_INDEX = 2

MATERIAL_STONE_ID = 90010
MATERIAL_LOG_ID = 90011
MATERIAL_PLYWOOD_ID = 90012

BUILDING_DATA_LIST = []


def GetGVGKey(srcGuildID, dstGuildID):
	minID = min(srcGuildID, dstGuildID)
	maxID = max(srcGuildID, dstGuildID)
	return minID*1000 + maxID

class EditableTextSlot(ui.ComboBox_New):
	def __init__(self, parent, x, y):
		ui.ComboBox_New.__init__(self)
		self.SetParent(parent)
		self.SetPosition(x+13, y-6)
		self.SetSize(48, 30)
		self.SizeInput(88)

		self.mouseReflector = MouseReflector(self)
		self.mouseReflector.SetSize(self.GetWidth(), self.GetHeight())

		self.Enable = TRUE
		self.textLine = ui.MakeTextLine(self)
		self.event = lambda *arg: None
		self.arg = 0
		self.Show()

		self.mouseReflector.UpdateRect()

	def __del__(self):
		ui.ComboBox_New.__del__(self)

	def SetText(self, text):
		self.textLine.SetText(text)
		self.textLine.SetPackedFontColor(0xffA07970)

	def SetEvent(self, event, arg):
		self.event = event
		self.arg = arg

	def Disable(self):
		self.Enable = FALSE

	def OnMouseOverIn(self):
		if not self.Enable:
			return
		self.mouseReflector.Show()

	def OnMouseOverOut(self):
		if not self.Enable:
			return
		self.mouseReflector.Hide()

	def OnMouseLeftButtonDown(self):
		if not self.Enable:
			return
		self.mouseReflector.Down()

	def OnMouseLeftButtonUp(self):
		if not self.Enable:
			return

		self.mouseReflector.Up()
		self.event(self.arg)

class MouseReflector(ui.Window):
	def __init__(self, parent):
		ui.Window.__init__(self)
		self.SetParent(parent)
		self.AddFlag("not_pick")
		self.width = self.height = 0
		self.isDown = FALSE

	def Down(self):
		self.isDown = TRUE

	def Up(self):
		self.isDown = FALSE

	def OnRender(self):

		if self.isDown:
			grp.SetColor(ui.WHITE_COLOR)
		else:
			grp.SetColor(ui.HALF_WHITE_COLOR)

		x, y = self.GetGlobalPosition()
		grp.RenderBar(x+2, y+2, self.GetWidth()-4, self.GetHeight()-4)
		
class CheckBox2(ui.ImageBox):
	def __init__(self, parent, x, y, event, filename = "d:/ymir work/ui/public/Parameter_Slot_01.sub"):
		ui.ImageBox.__init__(self)
		self.SetParent(parent)
		self.SetPosition(x, y)
		self.LoadImage(filename)

		self.mouseReflector = MouseReflector(self)
		self.mouseReflector.SetSize(self.GetWidth(), self.GetHeight())

		image = ui.MakeImageBox(self, "d:/ymir work/ui/public/check_image.sub", 0, 0)
		image.AddFlag("not_pick")
		image.SetWindowHorizontalAlignCenter()
		image.SetWindowVerticalAlignCenter()
		image.Hide()
		self.Enable = TRUE
		self.image = image
		self.event = event
		self.Show()

		self.mouseReflector.UpdateRect()

	def __del__(self):
		ui.ImageBox.__del__(self)

	def SetCheck(self, flag):
		if flag:
			self.image.Show()
		else:
			self.image.Hide()

	def Disable(self):
		self.Enable = FALSE

	def OnMouseOverIn(self):
		if not self.Enable:
			return
		self.mouseReflector.Show()

	def OnMouseOverOut(self):
		if not self.Enable:
			return
		self.mouseReflector.Hide()

	def OnMouseLeftButtonDown(self):
		if not self.Enable:
			return
		self.mouseReflector.Down()

	def OnMouseLeftButtonUp(self):
		if not self.Enable:
			return
		self.mouseReflector.Up()
		self.event()		

class CheckBox(ui.Window):
	def __init__(self, parent, x, y, filename = "d:/ymir work/ui/public/Parameter_Slot_01.sub"):
		ui.Window.__init__(self)
		self.SetParent(parent)
		self.SetPosition(x-4, y-6)
		self.SetSize(52,32)
		# self.LoadImage(filename)

		self.mouseReflector = MouseReflector(self)
		self.mouseReflector.SetSize(self.GetWidth(), self.GetHeight())

		image = ui.MakeImageBox(self, apollo_interface.PATCH_SPECIAL_1 + "/ok.tga", 0, 0)  #change rute
		image.AddFlag("not_pick")
		image.SetWindowHorizontalAlignCenter()
		image.SetWindowVerticalAlignCenter()
		image.Hide()
		self.Enable = TRUE
		self.image = image
		self.Show()

		self.mouseReflector.UpdateRect()
		self.event = None

	def __del__(self):
		ui.Window.__del__(self)

	def SetCheck(self, flag):
		if flag:
			self.image.Show()
		else:
			self.image.Hide()

	def EventApollo(self,event):
		self.event = event

	def Disable(self):
		self.Enable = FALSE

	def OnMouseOverIn(self):
		if not self.Enable:
			return
		self.mouseReflector.Show()

	def OnMouseOverOut(self):
		if not self.Enable:
			return
		self.mouseReflector.Hide()

	def OnMouseLeftButtonDown(self):
		if not self.Enable:
			return
		self.mouseReflector.Down()

	def OnMouseLeftButtonUp(self):
		if not self.Enable:
			return
		self.mouseReflector.Up()
		self.event()

class ChangeGradeNameDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

	def Open(self):
		self.gradeNameSlot.SetText("")
		self.gradeNameSlot.SetFocus()
		xMouse, yMouse = wndMgr.GetMousePosition()
		self.SetPosition(xMouse - self.GetWidth()/2, yMouse + 50)
		self.SetTop()
		self.Show()
	def Close(self):
		self.gradeNameSlot.KillFocus()
		self.Hide()
		return TRUE

	def SetGradeNumber(self, gradeNumber):
		self.gradeNumber = gradeNumber

	def GetGradeNumber(self):
		return self.gradeNumber
	def GetGradeName(self):
		return self.gradeNameSlot.GetText()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

class DeclareGuildWarDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.type=0
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self):
		self.inputValue.SetFocus()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputSlot = None
		self.inputValue = None
		self.Hide()

	def __CreateDialog(self):

		try:
			pyScrLoader = ui.PythonScriptLoader()

			if localeInfo.IsVIETNAM() :
				pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "declareguildwardialog.py")
			else:
				pyScrLoader.LoadScriptFile(self, "uiscript/declareguildwardialog.py")

		except:
			import exception
			exception.Abort("DeclareGuildWarWindow.__CreateDialog - LoadScript")

		try:
			getObject = self.GetChild
			self.board = getObject("Board")

			self.typeButtonList=[]
			#self.typeButtonList.append(getObject("NormalButton"))
			self.typeButtonList.append(getObject("WarpButton"))
			#self.typeButtonList.append(getObject("CTFButton"))

			self.acceptButton = getObject("AcceptButton")
			self.cancelButton = getObject("CancelButton")
			self.inputSlot = getObject("InputSlot")
			self.inputValue = getObject("InputValue")

			gameType=getObject("GameType")

		except:
			import exception
			exception.Abort("DeclareGuildWarWindow.__CreateDialog - BindObject")

		if constInfo.GUILD_WAR_TYPE_SELECT_ENABLE==0:
			gameType.Hide()

		#self.typeButtonList[0].SAFE_SetEvent(self.__OnClickTypeButtonNormal)
		self.typeButtonList[0].SAFE_SetEvent(self.__OnClickTypeButtonWarp)
		#self.typeButtonList[2].SAFE_SetEvent(self.__OnClickTypeButtonCTF)

		#self.typeButtonList[0].SetToolTipWindow(self.__CreateGameTypeToolTip(localeInfo.GUILDWAR_NORMAL_TITLE, localeInfo.GUILDWAR_NORMAL_DESCLIST))
		self.typeButtonList[0].SetToolTipWindow(self.__CreateGameTypeToolTip(localeInfo.GUILDWAR_WARP_TITLE, localeInfo.GUILDWAR_WARP_DESCLIST))
		#self.typeButtonList[2].SetToolTipWindow(self.__CreateGameTypeToolTip(localeInfo.GUILDWAR_CTF_TITLE, localeInfo.GUILDWAR_CTF_DESCLIST))

		self.__ClickRadioButton(self.typeButtonList, 0)

		self.SetAcceptEvent(ui.__mem_func__(self.__OnOK))
		self.SetCancelEvent(ui.__mem_func__(self.__OnCancel))

	def __OnOK(self):
		text = self.GetText()
		type = self.GetType()

		if ""==text:
			return

		net.SendChatPacket("/war %s 1" % (text))
		self.Close()

		return 1

	def __OnCancel(self):
		self.Close()
		return 1

	def __OnClickTypeButtonNormal(self):
		self.__ClickTypeRadioButton(0)

	def __OnClickTypeButtonWarp(self):
		self.__ClickTypeRadioButton(1)

	def __OnClickTypeButtonCTF(self):
		self.__ClickTypeRadioButton(2)

	def __ClickTypeRadioButton(self, type):
		self.__ClickRadioButton(self.typeButtonList, type)
		self.type=type

	def __ClickRadioButton(self, buttonList, buttonIndex):
		try:
			selButton=buttonList[buttonIndex]
		except IndexError:
			return

		for eachButton in buttonList:
			eachButton.SetUp()

		selButton.Down()

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetNumberMode(self):
		self.inputValue.SetNumberMode()

	def SetSecretMode(self):
		self.inputValue.SetSecret()

	def SetFocus(self):
		self.inputValue.SetFocus()

	def SetMaxLength(self, length):
		width = length * 6 + 10
		self.inputValue.SetMax(length)
		self.SetSlotWidth(width)
		self.SetBoardWidth(max(width + 50, 160))

	def SetSlotWidth(self, width):
		self.inputSlot.SetSize(width, self.inputSlot.GetHeight())
		self.inputValue.SetSize(width, self.inputValue.GetHeight())

	def SetBoardWidth(self, width):
		self.board.SetSize(max(width + 50, 160), self.GetHeight())
		self.SetSize(max(width + 50, 160), self.GetHeight())
		self.UpdateRect()

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.OnIMEReturn = event

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		self.inputValue.OnPressEscapeKey = event

	def GetType(self):
		return self.type

	def GetText(self):
		return self.inputValue.GetText()

	def __CreateGameTypeToolTip(self, title, descList):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetTitle(title)
		toolTip.AppendSpace(5)

		for desc in descList:
			toolTip.AutoAppendTextLine(desc)

		toolTip.AlignHorizonalCenter()
		return toolTip
		
class AcceptGuildWarDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.type=0
		self.__CreateDialog()

	def __del__(self):
		print "---------------------------------------------------------------------------- DELETE AcceptGuildWarDialog"
		ui.ScriptWindow.__del__(self)

	def Open(self, guildName, warType):
		self.guildName=guildName
		self.warType=warType
		self.__ClickSelectedTypeRadioButton()
		self.inputValue.SetText(guildName)
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def GetGuildName(self):
		return self.guildName

	def Close(self):
		self.ClearDictionary()
		self.board = None
		self.acceptButton = None
		self.cancelButton = None
		self.inputSlot = None
		self.inputValue = None
		self.Hide()

	def __ClickSelectedTypeRadioButton(self):
		self.__ClickTypeRadioButton(self.warType)

	def __CreateDialog(self):

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/acceptguildwardialog.py")
		except:
			import exception
			exception.Abort("DeclareGuildWarWindow.__CreateDialog - LoadScript")

		try:
			getObject = self.GetChild
			self.board = getObject("Board")

			self.typeButtonList=[]
			#self.typeButtonList.append(getObject("NormalButton"))
			self.typeButtonList.append(getObject("WarpButton"))
			#self.typeButtonList.append(getObject("CTFButton"))

			self.acceptButton = getObject("AcceptButton")
			self.cancelButton = getObject("CancelButton")
			self.inputSlot = getObject("InputSlot")
			self.inputValue = getObject("InputValue")

			gameType=getObject("GameType")

		except:
			import exception
			exception.Abort("DeclareGuildWarWindow.__CreateDialog - BindObject")

		if constInfo.GUILD_WAR_TYPE_SELECT_ENABLE==0:
			gameType.Hide()

		#self.typeButtonList[0].SAFE_SetEvent(self.__OnClickTypeButtonNormal)
		self.typeButtonList[0].SAFE_SetEvent(self.__OnClickTypeButtonWarp)
		#self.typeButtonList[2].SAFE_SetEvent(self.__OnClickTypeButtonCTF)

		#self.typeButtonList[0].SetToolTipWindow(self.__CreateGameTypeToolTip(localeInfo.GUILDWAR_NORMAL_TITLE, localeInfo.GUILDWAR_NORMAL_DESCLIST))
		self.typeButtonList[0].SetToolTipWindow(self.__CreateGameTypeToolTip(localeInfo.GUILDWAR_WARP_TITLE, localeInfo.GUILDWAR_WARP_DESCLIST))
		#self.typeButtonList[2].SetToolTipWindow(self.__CreateGameTypeToolTip(localeInfo.GUILDWAR_CTF_TITLE, localeInfo.GUILDWAR_CTF_DESCLIST))

		self.__ClickRadioButton(self.typeButtonList, 0)

	def __OnClickTypeButtonNormal(self):
		self.__ClickSelectedTypeRadioButton()

	def __OnClickTypeButtonWarp(self):
		self.__ClickSelectedTypeRadioButton()

	def __OnClickTypeButtonCTF(self):
		self.__ClickSelectedTypeRadioButton()

	def __ClickTypeRadioButton(self, type):
		self.__ClickRadioButton(self.typeButtonList, type)
		self.type=type

	def __ClickRadioButton(self, buttonList, buttonIndex):
		try:
			selButton=buttonList[buttonIndex]
		except IndexError:
			return

		for eachButton in buttonList:
			eachButton.SetUp()

		selButton.Down()

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def SetNumberMode(self):
		self.inputValue.SetNumberMode()

	def SetSecretMode(self):
		self.inputValue.SetSecret()

	def SetFocus(self):
		self.inputValue.SetFocus()

	def SetMaxLength(self, length):
		width = length * 6 + 10
		self.inputValue.SetMax(length)
		self.SetSlotWidth(width)
		self.SetBoardWidth(max(width + 50, 160))

	def SetSlotWidth(self, width):
		self.inputSlot.SetSize(width, self.inputSlot.GetHeight())
		self.inputValue.SetSize(width, self.inputValue.GetHeight())

	def SetBoardWidth(self, width):
		self.board.SetSize(max(width + 50, 160), self.GetHeight())
		self.SetSize(max(width + 50, 160), self.GetHeight())
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.SetAcceptEvent(ui.__mem_func__(event))

	def SAFE_SetCancelEvent(self, event):
		self.SetCancelEvent(ui.__mem_func__(event))

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)
		self.inputValue.OnIMEReturn = event

	def SetCancelEvent(self, event):
		self.board.SetCloseEvent(event)
		self.cancelButton.SetEvent(event)
		self.inputValue.OnPressEscapeKey = event

	def GetType(self):
		return self.type

	def GetText(self):
		return self.inputValue.GetText()

	def __CreateGameTypeToolTip(self, title, descList):
		toolTip = uiToolTip.ToolTip()
		toolTip.SetTitle(title)
		toolTip.AppendSpace(5)

		for desc in descList:
			toolTip.AutoAppendTextLine(desc)

		toolTip.AlignHorizonalCenter()
		return toolTip



class GuildWarScoreBoard(ui.ThinBoard):

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.Initialize()

	def __del__(self):
		ui.ThinBoard.__del__(self)

	def Initialize(self):
		self.allyGuildID = 0
		self.enemyGuildID = 0
		self.allyDataDict = {}
		self.enemyDataDict = {}

	def Open(self, allyGuildID, enemyGuildID):

		self.allyGuildID = allyGuildID
		self.enemyGuildID = enemyGuildID

		self.SetPosition(10, wndMgr.GetScreenHeight() - 175)

		mark = ui.MarkBox()
		mark.SetParent(self)
		mark.SetIndex(allyGuildID)
		mark.SetPosition(10, 10 + 18*0)
		mark.Show()
		scoreText = ui.TextLine()
		scoreText.SetParent(self)
		scoreText.SetPosition(30, 10 + 18*0)
		scoreText.SetHorizontalAlignLeft()
		scoreText.Show()
		self.allyDataDict["NAME"] = guild.GetGuildName(allyGuildID)
		self.allyDataDict["SCORE"] = 0
		self.allyDataDict["MEMBER_COUNT"] = -1
		self.allyDataDict["MARK"] = mark
		self.allyDataDict["TEXT"] = scoreText

		mark = ui.MarkBox()
		mark.SetParent(self)
		mark.SetIndex(enemyGuildID)
		mark.SetPosition(10, 10 + 18*1)
		mark.Show()
		scoreText = ui.TextLine()
		scoreText.SetParent(self)
		scoreText.SetPosition(30, 10 + 18*1)
		scoreText.SetHorizontalAlignLeft()
		scoreText.Show()
		self.enemyDataDict["NAME"] = guild.GetGuildName(enemyGuildID)
		self.enemyDataDict["SCORE"] = 0
		self.enemyDataDict["MEMBER_COUNT"] = -1
		self.enemyDataDict["MARK"] = mark
		self.enemyDataDict["TEXT"] = scoreText

		self.__RefreshName()
		self.Show()

	def __GetDataDict(self, ID):
		if self.allyGuildID == ID:
			return self.allyDataDict
		if self.enemyGuildID == ID:
			return self.enemyDataDict

		return None

	def SetScore(self, gainGuildID, opponetGuildID, point):
		dataDict = self.__GetDataDict(gainGuildID)
		if not dataDict:
			return
		dataDict["SCORE"] = point
		self.__RefreshName()

	def UpdateMemberCount(self, guildID1, memberCount1, guildID2, memberCount2):
		dataDict1 = self.__GetDataDict(guildID1)
		dataDict2 = self.__GetDataDict(guildID2)
		if dataDict1:
			dataDict1["MEMBER_COUNT"] = memberCount1
		if dataDict2:
			dataDict2["MEMBER_COUNT"] = memberCount2
		self.__RefreshName()

	def __RefreshName(self):
		nameMaxLen = max(len(self.allyDataDict["NAME"]), len(self.enemyDataDict["NAME"]))

		if -1 == self.allyDataDict["MEMBER_COUNT"] or -1 == self.enemyDataDict["MEMBER_COUNT"]:
			self.SetSize(30+nameMaxLen*6+8*5, 50)
			self.allyDataDict["TEXT"].SetText("%s %d" % (self.allyDataDict["NAME"], self.allyDataDict["SCORE"]))
			self.enemyDataDict["TEXT"].SetText("%s %d" % (self.enemyDataDict["NAME"], self.enemyDataDict["SCORE"]))

		else:
			self.SetSize(30+nameMaxLen*6+8*5+15, 50)
			self.allyDataDict["TEXT"].SetText("%s(%d) %d" % (self.allyDataDict["NAME"], self.allyDataDict["MEMBER_COUNT"], self.allyDataDict["SCORE"]))
			self.enemyDataDict["TEXT"].SetText("%s(%d) %d" % (self.enemyDataDict["NAME"], self.enemyDataDict["MEMBER_COUNT"], self.enemyDataDict["SCORE"]))


class GuildWindow(ui.ScriptWindow):

	GUILD_SKILL_PASSIVE_SLOT = 0
	GUILD_SKILL_ACTIVE_SLOT = 1
	GUILD_SKILL_AFFECT_SLOT = 2
	MEMBER_LINE_COUNT = 8

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded_1= 0
		self.isLoaded = 0
		self.__Initialize()
		self.memberLinePos1 = 0
		self.offerDialog = None
		self.markSelectDialog = None
		self.popupDialog = None
		self.apollo1 = None
		self.apollo = None
		self.apollo2 = None
		self.apollo3 = None
		self.apollo4 = None
		self.apollo_11 =None
		self.apollo_12 =None
		self.apollo_13 = None
		self.apollo_15 = None
		self.apollo_17 = None
		self.apollo_18 = None
		self.apollo_19 = None
		self.apollo_20 = None
		self.apollo_21 = None
		self.apollo_22 = None
		self.apollo_23 = None
		self.apollo_24 = None
		self.apollo_31 = None
		self.apollo_30 = None
		# self.changeGradeNameDialog = None
		self.tooltipSkill = None
		self.popupDialog = None
		self.memberLinePos = 0
		self.memberLinePos1 = 0
		if self.isLoaded==0:
			self.isLoaded=1
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.LoadWindow()
		ui.ScriptWindow.Show(self)

	def Destroy(self):
		global OnTest1
		OnTest1 = 0

	def __Initialize(self):
		return

	def LoadWindow(self):

		self.isLoaded_1 = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "apollo_scripts/GuildWindow.py")
		except:
			import exception
			exception.Abort("GuildWindow.LoadWindow.LoadObject")


		try:

			self.changeGradeNameDialog = ChangeGradeNameDialog()
			pyScrLoader.LoadScriptFile(self.changeGradeNameDialog, "apollo_scripts/changegradenamedialog.py")

			self.Board = self.GetChild("board")
			self.Guild_Input = self.GetChild("Guild_Input")
			self.Guild_Page = self.GetChild("Guild_Page")
			self.TitleName = self.GetChild("TitleName")
			self.TitleBar = self.GetChild("Guild_TitleBar")
			self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close))

			self.ButtonCollapse = self.GetChild("ButtonCollapse")
			self.ButtonCollapse.SetEvent(lambda : self.InputFunctiones(1))
			self.ButtonExpande = self.GetChild("ButtonExpande")
			self.ButtonExpande.SetEvent(lambda : self.InputFunctiones(2))
			self.ButtonExpande.Hide()
			self.Board_Caracter_Function()

			## Page Status 1
			self.Guild_Status = self.GetChild("Guild_Status")
			self.Guild_Status.Show()
			self.Guild_Status_Function()

			## Page Status 2
			self.Guild_Chat = self.GetChild("Guild_Chat")
			self.Guild_Chat.Hide()
			self.Guild_Chat_Function()
			## Page Status 3
			self.Guild_Members = self.GetChild("Guild_Members")
			self.Guild_Members_1 = self.GetChild("Guild_Members_1")
			self.Guild_Members_2 = self.GetChild("Guild_Members_2")
			self.Guild_Members_Function()
			self.Guild_Members.Hide()

			## Page Status 4
			self.Guild_Skills = self.GetChild("Guild_Skills")
			self.Guild_Skills.Hide()
			self.Guild_Skills_Function()

			##Page Status 5
			self.Guild_Authority = self.GetChild("Guild_Authority")
			self.Guild_Authority_1 = self.GetChild("Guild_Authority_1")
			self.Guild_Authority_2 = self.GetChild("Guild_Authority_2")
			self.Guild_Authority.Hide()
			self.Guild_Authority_Function()

			## ChangeGradeName
			self.changeGradeNameDialog.GetChild("AcceptButton").SetEvent(ui.__mem_func__(self.OnChangeGradeName))
			self.changeGradeNameDialog.GetChild("CancelButton").SetEvent(ui.__mem_func__(self.changeGradeNameDialog.Hide))
			self.changeGradeNameDialog.GetChild("Board").SetCloseEvent(ui.__mem_func__(self.changeGradeNameDialog.Hide))
			self.changeGradeNameDialog.gradeNameSlot = self.changeGradeNameDialog.GetChild("GradeNameValue")
			self.changeGradeNameDialog.gradeNameSlot.OnIMEReturn = ui.__mem_func__(self.OnChangeGradeName)
			self.changeGradeNameDialog.gradeNameSlot.OnPressEscapeKey = ui.__mem_func__(self.changeGradeNameDialog.Close)


		except:
			import exception
			exception.Abort("GuildWindow.LoadWindow.BindObject")

		# self.RefreshGuildBoardPage()
		self.RefreshGuildMemberPage()
		self.RefreshGuildSkillPage()
		self.RefreshGuildGradePage()
		self.OnRefreshComments()

		self.markSelectDialog=uiUploadMark.MarkSelectDialog()
		self.markSelectDialog.SAFE_SetSelectEvent(self.__OnSelectMark)

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
		[[1,6,apollo_interface.PAGE_TEXT_GUILD_1]],
		[[1,40,apollo_interface.PAGE_TEXT_GUILD_2]],
		[[1,34+40,apollo_interface.PAGE_TEXT_GUILD_3]],
		[[1,34+34+40,apollo_interface.PAGE_TEXT_GUILD_4]],
		[[1,34+34+34+40,apollo_interface.PAGE_TEXT_GUILD_5]]
		]
		for d in inf_sec_1:
			self.BoardSlot[number_title_c_f] = ui.BoardSlot()
			self.BoardSlot[number_title_c_f].SetParent(self.Guild_Input)
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
			self.BoardSlots_Text[number_title_c_f].SetParent(self.Guild_Input)
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
			self.BoardSlots_Button[4],
		)
		self.BoardSlots_1 = (
			self.BoardSlots_Text[0],
			self.BoardSlots_Text[1],
			self.BoardSlots_Text[2],
			self.BoardSlots_Text[3],
			self.BoardSlots_Text[4],
		)

		self.BoardSlots_Button[0].SetEvent((lambda : self.EventsPage(0)))
		self.BoardSlots_Button[0].Down()
		self.BoardSlots_Text[0].SetPackedFontColor(0xffe6d0a2)
		self.BoardSlots_Button[1].SetEvent((lambda : self.EventsPage(1)))
		self.BoardSlots_Button[2].SetEvent((lambda : self.EventsPage(2)))
		self.BoardSlots_Button[3].SetEvent((lambda : self.EventsPage(3)))
		self.BoardSlots_Button[4].SetEvent((lambda : self.EventsPage(4)))

	def EventsPage(self,number):
		for btn in self.BoardSlots:
			btn.SetUp()
			for ex in self.BoardSlots_1:
				ex.SetPackedFontColor(0xff6c5654)
		self.BoardSlots[number].Down()
		self.BoardSlots_1[number].SetPackedFontColor(0xffe6d0a2)

		if number == 0:
			self.Guild_Chat.Hide()
			self.Guild_Status.Show()
			self.Guild_Members.Hide()
			self.Guild_Skills.Hide()
			self.Guild_Authority.Hide()
		if number == 1:
			self.Guild_Members.Hide()
			self.Guild_Chat.Show()
			self.Guild_Status.Hide()
			self.Guild_Skills.Hide()
			self.Guild_Authority.Hide()
			self.RefreshGuildBoardPage()
		if number == 2:
			self.Guild_Chat.Hide()
			self.Guild_Status.Hide()
			self.Guild_Members.Show()
			self.Guild_Skills.Hide()
			self.Guild_Authority.Hide()

		if number == 3:
			self.Guild_Skills.Show()
			self.Guild_Chat.Hide()
			self.Guild_Status.Hide()
			self.Guild_Members.Hide()
			self.Guild_Authority.Hide()


		if number == 4:
			self.Guild_Authority.Show()
			self.Guild_Skills.Hide()
			self.Guild_Chat.Hide()
			self.Guild_Status.Hide()
			self.Guild_Members.Hide()

	def Guild_Status_Function(self):
		#-1
		self.mark = self.GetChild("LargeGuildMark")
		self.mark_change = self.GetChild("GuildMark")
		self.mark_change.SetEvent(lambda : self.__OnClickSelectGuildMarkButton())

		self.guild_level = self.GetChild("GuildLevelValue")
		self.guild_name = self.GetChild("GuildNameValue")
		self.guild_leader = self.GetChild("GuildMasterNameValue")
		self.level_percent = self.GetChild("PercentExp")
		self.curr_exp = self.GetChild("CurrentExperienceValue")
		self.exp_img = self.GetChild("ExpImgFull")
		#-2
		self.guild_members = self.GetChild("GuildMemberCountValue")
		self.guild_members_level = self.GetChild("GuildMemberLevelAverageValue")
		self.guild_members_level = self.GetChild("GuildMemberLevelAverageValue")

		self.guild_donate_exp = self.GetChild("OfferButton")
		self.guild_donate_exp.SetEvent(lambda : self.__OnClickOfferButton())

		self.guild_declare_war = self.GetChild("DeclareWarButton")
		self.guild_declare_war.SetEvent(lambda : self.__OnClickDeclareWarButton())

		self.offerDialog = uiPickMoney.PickMoneyDialog()
		self.offerDialog.LoadDialog()
		self.offerDialog.SetMax(9)
		self.offerDialog.SetTitleName(localeInfo.GUILD_OFFER_EXP)
		self.offerDialog.SetAcceptEvent(ui.__mem_func__(self.OnOffer))

	def Guild_Chat_Function(self):
		self.scrollbar = ui.ScrollBarNewDesign()
		self.scrollbar.SetParent(self.GetChild("Comment_section"))
		self.scrollbar.SetPosition(342,14)
		self.scrollbar.SetScrollBarSize(210)
		self.scrollbar.SetScrollEvent(self.__OnScroll)
		self.scrollbar.Show()

		self.commentSlot = ui.SpecialEditLine()
		self.commentSlot.SetParent(self.GetChild("Type_section"))
		self.commentSlot.SetPosition(18,25)
		self.commentSlot.SetSize(121,25)
		self.commentSlot.SetMax(35)
		self.commentSlot.OnIMEReturn = ui.__mem_func__(self.OnPostComment)
		self.commentSlot.SetIMEFlag(0)
		self.commentSlot.SetPlaceHolderText(apollo_interface.TEXT_TYPE_MESSEGE)
		self.commentSlot.SetPlaceHolderTextColor(0xffa07970)
		self.commentSlot.Show()

		self.objPos = 0
		self.scrollbar.SetPos(0)
		self.RefreshGuildBoardPage()


	def Guild_Skills_Function(self):
		self.skillPoints = self.GetChild("Skill_Plus_Value")
		self.energy = self.GetChild("Dragon_God_Power_Value")
		self.energyBar = self.GetChild("EnergyFull")
		self.donate_energy = self.GetChild("DonateEnergyButton")
		self.donate_energy.SetEvent(lambda : self.__OnOpenHealGSPBoard())



		self.backSlot = ui.GridSlotWindow()
		self.backSlot.SetParent(self.GetChild("Guild_Skills"))
		self.backSlot.SetPosition(30-25,80)
		self.backSlot.ArrangeSlot(210, 6, 1, 40, 40,3,0)
		self.backSlot.SetSlotBaseImage( apollo_interface.PATCH_COMMON+"/slot_ellipse/slot.png" ,1.0,1.0,1.0,1.0)
		self.backSlot.SetWindowHorizontalAlignCenter()
		self.backSlot.Show()

		self.activeSlot = ui.GridSlotWindow()
		self.activeSlot.SetParent(self.GetChild("Guild_Skills"))
		self.activeSlot.SetPosition(34-25,84)
		self.activeSlot.ArrangeSlot(210, 6, 1, 40, 40,3,0)
		self.activeSlot.SetSlotBaseImage("d:/ymir work/ui/slot.tga",1.0,1.0,1.0,1.0)
		self.activeSlot.SetWindowHorizontalAlignCenter()
		self.activeSlot.Show()

		self.activeSlot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
		self.activeSlot.SetOverInItemEvent(lambda slotNumber, type=self.GUILD_SKILL_ACTIVE_SLOT: self.OverInItem(slotNumber, type))
		self.activeSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.activeSlot.SetSelectItemSlotEvent(lambda slotNumber, type=self.GUILD_SKILL_ACTIVE_SLOT: self.OnPickUpGuildSkill(slotNumber, type))
		self.activeSlot.SetUnselectItemSlotEvent(lambda slotNumber, type=self.GUILD_SKILL_ACTIVE_SLOT: self.OnUseGuildSkill(slotNumber, type))
		self.activeSlot.SetPressedSlotButtonEvent(lambda slotNumber, type=self.GUILD_SKILL_ACTIVE_SLOT: self.OnUpGuildSkill(slotNumber, type))
		self.activeSlot.AppendSlotButton(apollo_interface.PATCH_BUTTONS+"/plus_01_normal.png",\
										apollo_interface.PATCH_BUTTONS+"/plus_02_hover.png",\
										apollo_interface.PATCH_BUTTONS+"/plus_03_active.png")


		## Active
		for i in xrange(len(playerSettingModule.ACTIVE_GUILD_SKILL_INDEX_LIST)):

			slotIndex = self.activeSlot.GetStartIndex()+i
			skillIndex = playerSettingModule.ACTIVE_GUILD_SKILL_INDEX_LIST[i]

			self.activeSlot.SetSkillSlot(slotIndex, skillIndex, 0)
			self.activeSlot.SetCoverButton(slotIndex)
			self.activeSlot.RefreshSlot()
			guild.SetSkillIndex(slotIndex, len(playerSettingModule.PASSIVE_GUILD_SKILL_INDEX_LIST)+i)


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
				self.Guild_Input.SetSize(143-95+movement,323)
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
				self.Guild_Page.SetSize(541-115+movement2,400)
				self.Board.SetSize(541-103+movement2,370)
				self.TitleName.SetParent(self)
				self.TitleName.SetPosition(+20,-184)
				self.TitleName.SetText(apollo_interface.GUILD_TITLE)
				self.TitleName.SetHorizontalAlignCenter()
			else:
				for i in xrange(0,5):
					self.BoardSlots_Text[i].Show()

			if movement1 >= 0 and movement1 <= 441-56-(441-110-56):
				movement1 +=speed_movem
				self.TitleBar.SetWidth(541-110-15+movement1)
				self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close))

			if movement3 >= 0 and movement3 <= 150-(150-110):
				movement3 +=speed_movem
				for a in xrange(0,5):
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
				self.Guild_Input.SetSize(143-movement,323)
			if movement >= 109:
				OnTest1 = 0

			if movement1 >= 0 and movement1 <= 541-110-56-(-441-56):
				movement1 +=speed_movem
				self.TitleBar.SetWidth(541-20-movement1)
				self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close))

			if movement2 >= 0 and movement2 <= 541-110-(-441):
				movement2 +=speed_movem
				self.SetSize(541-movement2,400)
				self.Guild_Page.SetSize(541-movement2,400)
				self.Board.SetSize(545-movement2,370)
				self.TitleName.SetParent(self)
				self.TitleName.SetPosition(20,-183)
				self.TitleName.SetText(apollo_interface.GUILD_TITLE)
				self.TitleName.SetHorizontalAlignCenter()
				for i in xrange(0,5):
					self.BoardSlots_Text[i].Hide()


			if movement3 >= 0 and movement3 <= 150-110-(-150):
				movement3 +=speed_movem
				for a in xrange(0,5):
					self.BoardSlot[a].MakeTitleBar(150-movement3)
					self.BoardSlots_Image[a].Show()
					self.BoardSlots_Image[a].SetTop()

			if movement4 >= 0 and movement4 <= 260-(-370):
				movement4 +=speed_movem
				self.ButtonCollapse.SetParent(self)
				self.ButtonCollapse.SetPosition(455-movement4,12)
				self.ButtonCollapse.Show()
		self.RefreshGuildInfoPage()

	def RefreshGuildInfoPage(self):
	#-1
		self.mark.SetIndex(net.GetGuildID())
		self.mark.SetScale(3.3)
		self.guild_level.SetText(str(guild.GetGuildLevel()))
		self.guild_name.SetText(guild.GetGuildName())
		self.guild_leader.SetText(guild.GetGuildMasterName())
		curExp, lastExp = guild.GetGuildExperience()
		curExp *= 100
		lastExp *= 100
		total = curExp + lastExp
		self.exp_img.SetPercentage(curExp,total)
		self.curr_exp.SetText("EXP:   "+str(curExp)+ "       " +apollo_interface.CHARACTER_FROM +"       "+str(total))
		self.level_percent.SetText("%s %.2f%%" % ("", float(curExp) / max(1, float(total)) * 100))
	#-1
	#-2
		curMemberCount, maxMemberCount = guild.GetGuildMemberCount()
		self.guild_members.SetText(str(curMemberCount)+" / "+str(maxMemberCount))
		self.guild_members_level.SetText(str(guild.GetGuildMemberLevelAverage()))
		#

	#Guild Info Func
	def __OnSelectMark(self, markFileName):
		ret = net.UploadMark("upload/"+markFileName)

		# MARK_BUG_FIX
		if net.ERROR_MARK_UPLOAD_NEED_RECONNECT == ret:
			chat.AppendChat(1,localeInfo.UPLOAD_MARK_UPLOAD_NEED_RECONNECT)
		return ret

	def __OnClickSelectGuildMarkButton(self):
		if guild.GetGuildLevel() < int(localeInfo.GUILD_MARK_MIN_LEVEL):
			chat.AppendChat(1,localeInfo.GUILD_MARK_NOT_ENOUGH_LEVEL)
		elif not guild.MainPlayerHasAuthority(guild.AUTH_NOTICE):
			chat.AppendChat(1,localeInfo.GUILD_NO_NOTICE_PERMISSION)
		else:
			self.markSelectDialog.Open()

	def __OnClickOfferButton(self):

		curEXP = unsigned32(player.GetStatus(player.EXP))

		if curEXP <= 100:
			chat.AppendChat(1,localeInfo.GUILD_SHORT_EXP)
			return

		self.offerDialog.Open(curEXP, 100)

	def OnOffer(self, exp):
		net.SendGuildOfferPacket(exp)

	def __OnClickDeclareWarButton(self):
		inputDialog = DeclareGuildWarDialog()
		inputDialog.Open()
		self.inputDialog = inputDialog

	def __GetGuildBoardCommentData(self, index):
		commentID, chrName, comment = guild.GetGuildBoardCommentData(index)
		if 0==commentID:
			if ""==chrName:
				chrName=localeInfo.UI_NONAME
			if ""==comment:
				comment=localeInfo.UI_NOCONTENTS

		return commentID, chrName, comment

	def OnPostComment(self):
		text = self.commentSlot.GetText()
		if not text:
			return FALSE
		if not guild.MainPlayerHasAuthority(guild.AUTH_NOTICE):
			chat.AppendChat(1,localeInfo.GUILD_NO_NOTICE_PERMISSION)
			return

		net.SendGuildPostCommentPacket(text[:50])
		self.commentSlot.SetText("")
		self.objPos = 0
		self.scrollbar.SetPos(0)
		self.RefreshGuildBoardPage()
		return TRUE

	def OnDeleteComment(self, index):
		commentID, chrName, comment = self.__GetGuildBoardCommentData(index)
		net.SendGuildDeleteCommentPacket(commentID)
		self.RefreshGuildBoardPage()

	def OnRefreshComments(self):
		net.SendGuildRefreshCommentsPacket(0)

	def __OnScroll(self):
		self.OnRefreshComments()
		self.objPos = self.scrollbar.GetPos() * (guild.GetGuildBoardCommentCount()-6)
		self.RefreshGuildBoardPage()

	###

	def Guild_Authority_Function(self):
		lineStep = 20
		lineStep1 = 30
		lineStep2 = 30
		self.apollo_31 = {}
		self.apollo_30 = []
		self.apollo_32 =[]

		self.Name_Title_Member_1 = {}
		number_title_r_1 = 0
		info_s41 =[
		[[30,8+5],[apollo_interface.NR_GRADE]],
		[[60+20,8+5],[apollo_interface.NAME_GRADE]],
		[[60+60+29,8+5],[apollo_interface.INVITE_TEXT]],
		[[65+60+40+33,8+5],[apollo_interface.DISMISS_TEXT]],
		[[65+60+40+40+48,8+5],[apollo_interface.WRITE_TEXT]],
		[[65+60+40+40+70+30,8+5],[apollo_interface.SKILL_TEXT]]
		]
		for e1 in info_s41:
			self.Name_Title_Member_1[number_title_r_1] = ui.TextLine()
			self.Name_Title_Member_1[number_title_r_1].SetParent(self.Guild_Authority_1)
			self.Name_Title_Member_1[number_title_r_1].SetPosition(e1[0][0],e1[0][1])
			self.Name_Title_Member_1[number_title_r_1].SetText(e1[1][0])
			self.Name_Title_Member_1[number_title_r_1].SetHorizontalAlignCenter()
			self.Name_Title_Member_1[number_title_r_1].SetPackedFontColor(0xffE6D0A2)
			self.Name_Title_Member_1[number_title_r_1].Show()
			number_title_r_1 +=1

		for i in xrange(self.MEMBER_LINE_COUNT):
			index = i+1

			inverseLineIndex = self.MEMBER_LINE_COUNT - i - 1
			yPos = 28 + inverseLineIndex*lineStep
			yPos1 = 28 + inverseLineIndex*lineStep1
			yPos2 = 25 + inverseLineIndex*lineStep2
			yPos3 = 15 + inverseLineIndex*lineStep2

			self.Decoration_Chat1 = ui.ImageBox()
			self.Decoration_Chat1.AddFlag("not_pick")
			self.Decoration_Chat1.SetParent(self.Guild_Authority_2)
			self.Decoration_Chat1.SetPosition(15,yPos1-10)
			self.Decoration_Chat1.LoadImage(apollo_interface.PATCH_GUILD + "/dialog_rank_slot.png")
			self.Decoration_Chat1.Show()

			gradeNumberSlot = ui.MakeTextLine(self.Decoration_Chat1)
			gradeNumberSlot.SetText(str(1+i))
			gradeNumberSlot.SetPosition(-142,0)
			gradeNumberSlot.SetPackedFontColor(0xffCAA76F)

			gradeNameSlot = EditableTextSlot(self.Guild_Authority_2, 28+5, yPos2)

			inviteAuthorityCheckBox = CheckBox(self.Guild_Authority_2, 124+5, yPos2)
			driveoutAuthorityCheckBox = CheckBox(self.Guild_Authority_2, 124+51+5, yPos2)
			noticeAuthorityCheckBox = CheckBox(self.Guild_Authority_2, 124+51+51+5, yPos2)
			skillAuthorityCheckBox = CheckBox(self.Guild_Authority_2, 124+51+51+51+5, yPos2)

			self.apollo_32.append(self.Decoration_Chat1)
			self.apollo_32.append(gradeNumberSlot)
			self.apollo_32.append(gradeNameSlot)
			self.apollo_32.append(inviteAuthorityCheckBox)
			self.apollo_32.append(driveoutAuthorityCheckBox)
			self.apollo_32.append(noticeAuthorityCheckBox)
			self.apollo_32.append(skillAuthorityCheckBox)


			self.Name_Title_Member5 = ui.TextLine()
			self.Name_Title_Member5.SetParent(self.Guild_Authority_2)
			self.Name_Title_Member5.SetPosition(55,yPos1-12)
			self.Name_Title_Member5.SetText("")
			self.Name_Title_Member5.SetHorizontalAlignCenter()
			self.Name_Title_Member5.SetPackedFontColor(0xffCAA76F)
			self.Name_Title_Member5.Hide()

			self.apollo_30.append(self.Name_Title_Member5)

			memberSlotList1 = []
			memberSlotList1.append(gradeNumberSlot)
			memberSlotList1.append(gradeNameSlot)
			memberSlotList1.append(inviteAuthorityCheckBox)
			memberSlotList1.append(driveoutAuthorityCheckBox)
			memberSlotList1.append(noticeAuthorityCheckBox)
			memberSlotList1.append(skillAuthorityCheckBox)
			self.apollo_31[inverseLineIndex] = memberSlotList1

		self.ScrollBar1 = ui.ScrollBarNewDesign()
		self.ScrollBar1.SetParent(self.Guild_Authority_2)
		self.ScrollBar1.SetPosition(342, 20)
		self.ScrollBar1.SetScrollBarSize(242)
		self.ScrollBar1.SetScrollStep(0.6)
		self.ScrollBar1.Show()

		self.ScrollBar1.SetScrollEvent(ui.__mem_func__(self.OnScrollMemberLine1))

	## Grade
	def OnOpenChangeGradeName(self, arg):
		self.changeGradeNameDialog.SetGradeNumber(arg)
		self.changeGradeNameDialog.Open()

	def Guild_Members_Function(self):
		self.Name_Title_Member = {}
		number_title_r = 0
		xPos = 15
		info_s4 =[
		[[xPos+55,8+5],[apollo_interface.NAME_TEXT]],
		[[xPos+60+60,8+5],[apollo_interface.RACE_TEXT]],
		[[xPos+60+60+40,8+5],[apollo_interface.LEVEL_TEXT]],
		[[xPos+65+60+40+40,8+5],[apollo_interface.INVEST_TEXT]],
		[[xPos+65+60+40+40+70,8+5],[apollo_interface.RANG_TEXT]]
		]
		for e in info_s4:
			self.Name_Title_Member[number_title_r] = ui.TextLine()
			self.Name_Title_Member[number_title_r].SetParent(self.Guild_Members_1)
			self.Name_Title_Member[number_title_r].SetPosition(e[0][0],e[0][1])
			self.Name_Title_Member[number_title_r].SetText(e[1][0])
			self.Name_Title_Member[number_title_r].SetHorizontalAlignCenter()
			self.Name_Title_Member[number_title_r].SetPackedFontColor(0xffE6D0A2)
			self.Name_Title_Member[number_title_r].Show()
			number_title_r +=1

		lineStep = 20
		lineStep1 = 30
		self.apollo_11 =[]
		self.apollo_12 = []
		self.apollo_13 = {}
		self.apollo_15 = []
		self.apollo_17 = []
		self.apollo_18 = []
		self.apollo_19 = []
		self.apollo_20 = []

		self.ScrollBar = ui.ScrollBar()
		self.ScrollBar.SetParent(self.Guild_Members_2)
		self.ScrollBar.SetPosition(332, 10)
		self.ScrollBar.SetScrollBarSize(242)
		self.ScrollBar.SetScrollStep(0.6)
		self.ScrollBar.Show()

		self.ScrollBar.SetScrollEvent(ui.__mem_func__(self.OnScrollMemberLine))

		self.objPos2 = 0
		curMemberCount, maxMemberCount = guild.GetGuildMemberCount()
		pos = self.objPos2
		if curMemberCount >= 5:
			self.obj_count2 = 5
		else:
			self.obj_count2 = curMemberCount
		z=0

		self.players, u = {}, 0
		self.namesAuthority,self.imgs,self.levels,self.inverts,self.pos = {},{},{},{},{}

		for i in xrange(self.obj_count2):
			realPos = pos+i

			self.players[i] = ui.ImageBox()
			self.players[i].SetParent(self.Guild_Members_2)
			self.players[i].SetPosition(25,20+u)
			self.players[i].LoadImage(apollo_interface.PATCH_GUILD + "/dialog_member_slot.png")
			self.players[i].Show()

			u+= 31

		for i in xrange(self.MEMBER_LINE_COUNT):

			inverseLineIndex = self.MEMBER_LINE_COUNT - i - 1
			yPos = 28+10 + inverseLineIndex*lineStep
			yPos1 = 28+14 + inverseLineIndex*lineStep1

			self.Box_Image = ui.ImageBox()
			self.Box_Image.SetParent(self.Guild_Members_2)
			self.Box_Image.SetPosition(10+94+xPos,yPos1-18)
			self.Box_Image.LoadImage("interface_emperorapollo/icons/faces/small/icon_mwarrior.png")
			self.Box_Image.Show()
			self.apollo_17.append(self.Box_Image)

			self.Level_Member = ui.TextLine()
			self.Level_Member.SetParent(self.Guild_Members_2)
			self.Level_Member.SetPosition(55+94+12+xPos,yPos1-12)
			self.Level_Member.SetText("")
			self.Level_Member.SetHorizontalAlignCenter()
			self.Level_Member.SetPackedFontColor(0xffA08784)
			self.Level_Member.Show()
			self.apollo_18.append(self.Level_Member)

			self.Invet_Member = ui.TextLine()
			self.Invet_Member.SetParent(self.Guild_Members_2)
			self.Invet_Member.SetPosition(55+94+12+42+xPos,yPos1-12)
			self.Invet_Member.SetText("")
			self.Invet_Member.SetHorizontalAlignCenter()
			self.Invet_Member.SetPackedFontColor(0xffA08784)
			self.Invet_Member.Show()
			self.apollo_19.append(self.Invet_Member)

			self.Slots_Grade = ui.ComboBox_New()
			self.Slots_Grade.SetParent(self.Guild_Members_2)
			self.Slots_Grade.SetPosition(55+94+12+66+xPos,yPos1-19)
			self.Slots_Grade.SetSize(61, 18)
			self.Slots_Grade.SetEvent(lambda gradeNumber, lineIndex=inverseLineIndex, argSelf=proxy(self): argSelf.OnChangeMemberGrade(lineIndex, gradeNumber))
			self.Slots_Grade.ShowButton(1)
			self.Slots_Grade.Show()

			self.apollo_20.append(self.Slots_Grade)


			self.Name_Title_Member1 = ui.TextLine()
			self.Name_Title_Member1.SetParent(self.Guild_Members_2)
			self.Name_Title_Member1.SetPosition(55+xPos,yPos1-12)
			self.Name_Title_Member1.SetText("")
			self.Name_Title_Member1.SetHorizontalAlignCenter()
			self.Name_Title_Member1.SetPackedFontColor(0xffCAA76F)
			self.Name_Title_Member1.Show()

			self.apollo_12.append(self.Name_Title_Member1)

			memberSlotList = []
			memberSlotList.append(self.Name_Title_Member1)
			memberSlotList.append(self.Box_Image)
			memberSlotList.append(self.Level_Member)
			memberSlotList.append(self.Invet_Member)
			memberSlotList.append(self.Slots_Grade)
			self.apollo_13[inverseLineIndex] = memberSlotList


	def RefreshGuildMemberPage(self):

		if self.isLoaded==0:
			return

		count = guild.GetMemberCount()
		if count > self.MEMBER_LINE_COUNT:
			self.ScrollBar.Show()
		else:
			self.ScrollBar.Hide()

		self.RefreshGuildMemberPageGradeComboBox()
		self.RefreshGuildMemberPageMemberList()

	def RefreshGuildGradePage(self):
		if self.isLoaded==0:
			return

		self.RefreshGuildMemberPageGradeComboBox()
		self.RefreshGuildMemberPageMemberList()
		self.RefreshGuildGradePageList()

	def OnScrollMemberLine(self):
		scrollBar = self.ScrollBar
		pos = scrollBar.GetPos()

		count = guild.GetMemberCount()
		newLinePos = int(float(count - self.MEMBER_LINE_COUNT) * pos)

		if newLinePos != self.memberLinePos:
			self.memberLinePos = newLinePos
			self.RefreshGuildMemberPageMemberList()

	def OnScrollMemberLine1(self):
		scrollBar = self.ScrollBar1
		pos = scrollBar.GetPos()

		count = 15
		newLinePos = int(float(count - self.MEMBER_LINE_COUNT) * pos)

		if newLinePos != self.memberLinePos1:
			self.memberLinePos1 = newLinePos
			self.RefreshGuildGradePageList()

	def RefreshGuildMemberPageMemberList(self):

		if self.isLoaded==0:
			return

		for line, slotList in self.apollo_13.items():

			gradeComboBox = slotList[4]
			gradeComboBox.Disable()


			if not guild.IsMember(line):
				slotList[0].SetText("")
				slotList[1].Hide()
				slotList[2].SetText("")
				slotList[3].SetText("")
				gradeComboBox.Hide()
				continue

			pid, name, grade, race, level, offer, general = self.GetMemberData(line)
			if pid < 0:
				continue

			guildExperienceSummary = guild.GetGuildExperienceSummary()

			offerPercentage = 0
			if guildExperienceSummary > 0:
				offerPercentage = int(float(offer) / float(guildExperienceSummary) * 100.0)

			faceImageName = apollo_interface.FACE_IMAGE_DICT_SMALL[race]
			slotList[0].SetText(name)
			slotList[1].LoadImage(faceImageName)
			slotList[2].SetText(str(level))
			slotList[3].SetText(str(offerPercentage) + "%")
			gradeComboBox.SetCurrentItem(guild.GetGradeName(grade))
			if 1 != grade:
				gradeComboBox.Enable()
				gradeComboBox.Show()

	def RefreshGuildGradePageList(self):
		if self.isLoaded==0:
			return

		for line, slotList1 in self.apollo_31.items():

			name12, authority = guild.GetGradeData(int(line)+self.memberLinePos1+1)

			slotList1[0].SetText(str(line+self.memberLinePos1+1))
			slotList1[1].SetEvent(ui.__mem_func__(self.OnOpenChangeGradeName), line+self.memberLinePos1+1)
			slotList1[1].SetText(name12)
			slotList1[2].EventApollo(lambda argSelf=proxy(self), argIndex=line+self.memberLinePos1+1, argAuthority=1<<0: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority)))
			slotList1[2].SetCheck(authority & guild.AUTH_ADD_MEMBER)
			slotList1[3].EventApollo(lambda argSelf=proxy(self), argIndex=line+self.memberLinePos1+1, argAuthority=1<<1: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority)))
			slotList1[3].SetCheck(authority & guild.AUTH_REMOVE_MEMBER)
			slotList1[4].EventApollo(lambda argSelf=proxy(self), argIndex=line+self.memberLinePos1+1, argAuthority=1<<2: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority)))
			slotList1[4].SetCheck(authority & guild.AUTH_NOTICE)
			slotList1[5].EventApollo(lambda argSelf=proxy(self), argIndex=line+self.memberLinePos1+1, argAuthority=1<<3: apply(argSelf.OnCheckAuthority, (argIndex,argAuthority)))
			slotList1[5].SetCheck(authority & guild.AUTH_SKILL)

	def GetMemberData(self, localPos):
		return guild.GetMemberData(localPos + self.memberLinePos)

	def GetGradeData(self, localPos):
		return guild.GetGradeData(int(localPos) + self.memberLinePos1+1)


	def OnChangeMemberGrade(self, lineIndex, gradeNumber):
		PID = guild.MemberIndexToPID(lineIndex + self.memberLinePos)
		net.SendGuildChangeMemberGradePacket(PID, gradeNumber)

	def RefreshGuildMemberPageGradeComboBox(self):

		if self.isLoaded==0:
			return

		self.CAN_CHANGE_GRADE_COUNT = 15 - 1
		for key, slotList in self.apollo_13.items():

			gradeComboBox = slotList[4]
			gradeComboBox.Disable()

			if not guild.IsMember(key):
				continue

			pid, name, grade, job, level, offer, general = self.GetMemberData(key)
			if pid < 0:
				continue

			gradeComboBox.ClearItem()
			for i in xrange(self.CAN_CHANGE_GRADE_COUNT):
				gradeComboBox.InsertItem(i+2, guild.GetGradeName(i+2))
			gradeComboBox.SetCurrentItem(guild.GetGradeName(grade))
			if 1 != grade:
				gradeComboBox.Enable()

	def CanOpen(self):
		return guild.IsGuildEnable()

	def Open(self):
		self.Show()
		self.SetTop()

		guildID = net.GetGuildID()
		self.largeMarkBox.SetIndex(guildID)
		self.largeMarkBox.SetScale(3)

	def OnChangeGradeName(self):
		self.changeGradeNameDialog.Hide()
		gradeNumber = self.changeGradeNameDialog.GetGradeNumber()
		gradeName = self.changeGradeNameDialog.GetGradeName()

		if len(gradeName) == 0:
			gradeName = localeInfo.GUILD_DEFAULT_GRADE

		net.SendGuildChangeGradeNamePacket(gradeNumber, gradeName)
		return TRUE

	def OnCheckAuthority(self, argIndex, argAuthority):
		name, authority = guild.GetGradeData(argIndex)
		net.SendGuildChangeGradeAuthorityPacket(argIndex, authority ^ argAuthority)

	def CanOpen(self):
		return guild.IsGuildEnable()

	def Open(self):
		self.Show()
		self.SetTop()

	def RefreshGuildBoardPage(self):
		self.commentImportantToolTip = uitooltipGold.ToolTip(130)
		net.SendGuildRefreshCommentsPacket(0)
		pos = self.objPos
		if guild.GetGuildBoardCommentCount() >= 6:
			self.obj_count = 6
			self.scrollbar.Show()
		else:
			self.obj_count = guild.GetGuildBoardCommentCount()
			self.scrollbar.Hide()

		self.delete,self.important, self.spaces,self.namesCommand,self.comments, u = {},{},{},{},{}, 0

		for i in xrange(self.obj_count):
			realPos = pos+i

			commentID, chrName, comment = self.__GetGuildBoardCommentData(realPos)
			if chrName == "Noname":
				break

			self.spaces[i] = ui.ImageBox()
			self.spaces[i].SetParent(self.GetChild("Comment_section"))
			self.spaces[i].SetPosition(20,20+u)
			self.spaces[i].LoadImage(apollo_interface.PATCH_GUILD + "/dialog_message_slot.png")
			self.spaces[i].Show()

			self.namesCommand[i] = ui.TextLine()
			self.namesCommand[i].SetParent(self.spaces[i])
			self.namesCommand[i].SetPosition(24,8)
			self.namesCommand[i].SetText(chrName)
			self.namesCommand[i].SetPackedFontColor(0xffcaa76f)
			self.namesCommand[i].Show()

			self.important[i] = ui.ImageBox()
			self.important[i].SetParent(self.spaces[i])
			self.important[i].SetPosition(87,8)
			self.important[i].LoadImage(apollo_interface.PATCH_SPECIAL_1 + "/dialog_message_importantmsg.png")

			self.comments[i] = ui.TextLine()
			self.comments[i].SetParent(self.spaces[i])
			self.comments[i].SetPosition(110,8)
			if "!" == comment[0]:
				self.comments[i].SetText(comment[1:])
				self.comments[i].SetPackedFontColor(0xffdb9b93)
				self.important[i].Show()
			else:
				self.comments[i].SetText(comment)
				self.comments[i].SetPackedFontColor(0xffa08784)

			self.comments[i].Show()

			masterName = guild.GetGuildMasterName()
			mainCharacterName = player.GetMainCharacterName()

			if mainCharacterName == chrName or (masterName == mainCharacterName):
				self.delete[i] = ui.Button()
				self.delete[i].SetParent(self.spaces[i])
				self.delete[i].SetPosition(305,7)
				self.delete[i].SetUpVisual(apollo_interface.PATCH_BUTTONS + "/close_mini_01_normal.png")
				self.delete[i].SetOverVisual(apollo_interface.PATCH_BUTTONS + "/close_mini_02_hover.png")
				self.delete[i].SetDownVisual(apollo_interface.PATCH_BUTTONS + "/close_mini_03_active.png")
				self.delete[i].SetEvent(lambda x = realPos: self.OnDeleteComment(x))
				self.delete[i].Show()

			u += 35

	def __ShowAlignmentToolTip(self):
		self.commentImportantToolTip.ShowToolTip()

	def __HideAlignmentToolTip(self):
		self.commentImportantToolTip.HideToolTip()

	#Skill Func
	def RefreshGuildSkillPage(self):

		if 0 != 0:
			return

		# page = self.pageDict["MUSIC"]

		curPoint, maxPoint = guild.GetDragonPowerPoint()
		maxPoint = max(maxPoint, 1)
		self.energy.SetText("|cffa08784"+apollo_interface.CHARACTER_PSTATUS+ "|cfff8d090 "  +str(curPoint) + " / " + str(maxPoint))

		percentage = ( (float(curPoint / max(1, float(maxPoint))) * 100))
		self.energyBar.SetPercentage(curPoint,maxPoint)

		skillPoint = guild.GetGuildSkillPoint()
		self.skillPoints.SetText("|cffa08784"+apollo_interface.CHARACTER_PSTATUS + "|cfff8d090 " +str(skillPoint))

		# page.passiveSlot.HideAllSlotButton()
		self.activeSlot.HideAllSlotButton()

		## Active
		for i in xrange(len(playerSettingModule.ACTIVE_GUILD_SKILL_INDEX_LIST)):

			slotIndex = self.activeSlot.GetStartIndex()+i
			skillIndex = playerSettingModule.ACTIVE_GUILD_SKILL_INDEX_LIST[i]
			skillLevel = guild.GetSkillLevel(slotIndex)
			skillMaxLevel = skill.GetSkillMaxLevel(skillIndex)

			self.activeSlot.SetSlotCount(slotIndex, skillLevel)

			if skillLevel <= 0:
				self.activeSlot.DisableCoverButton(slotIndex)
			else:
				self.activeSlot.EnableCoverButton(slotIndex)

			if skillPoint > 0:
				if skillLevel < skillMaxLevel:
					self.activeSlot.ShowSlotButton(slotIndex)

	def OnPickUpGuildSkill(self, skillSlotIndex, type):

		mouseController = mouseModule.mouseController

		if False == mouseController.isAttached():

			skillIndex = player.GetSkillIndex(skillSlotIndex)
			skillLevel = guild.GetSkillLevel(skillSlotIndex)

			if skill.CanUseSkill(skillIndex) and skillLevel > 0:

				if app.IsPressed(app.DIK_LCONTROL):

					player.RequestAddToEmptyLocalQuickSlot(player.SLOT_TYPE_SKILL, skillSlotIndex)
					return

				mouseController.AttachObject(self, player.SLOT_TYPE_SKILL, skillSlotIndex, skillIndex)

		else:
			mouseController.DeattachObject()

	def OnUseGuildSkill(self, slotNumber, type):
		skillIndex = player.GetSkillIndex(slotNumber)
		skillLevel = guild.GetSkillLevel(slotNumber)

		if skillLevel <= 0:
			return

		player.UseGuildSkill(slotNumber)

	def OnUpGuildSkill(self, slotNumber, type):
		skillIndex = player.GetSkillIndex(slotNumber)
		net.SendChatPacket("/gskillup " + str(skillIndex))
		
	def OnStartGuildWar(self, guildSelf, guildOpp):

		if self.isLoaded==0:
			return

		if guild.GetGuildID() != guildSelf:
			return

		guildName = guild.GetGuildName(guildOpp)
				
	def OnEndGuildWar(self, guildSelf, guildOpp):

		if self.isLoaded==0:
			return

		if guild.GetGuildID() != guildSelf:
			return

		guildName = guild.GetGuildName(guildOpp)

	def OnUseSkill(self, slotNumber, coolTime):

		if 0 != 0:
			return
		# self.activeSlot = ui.GridSlotWindow()
		if self.activeSlot.HasSlot(slotNumber):
			self.activeSlot.SetSlotCoolTime(slotNumber, coolTime)

	def OverInItem(self, slotNumber, type):

		if mouseModule.mouseController.isAttached():
			return

		if None != self.tooltipSkill:
			skillIndex = player.GetSkillIndex(slotNumber)
			skillLevel = guild.GetSkillLevel(slotNumber)

			self.tooltipSkill.SetSkill(skillIndex, skillLevel)

	def OverOutItem(self):
		self.tooltipSkill.HideToolTip()
		self.tooltip_in = 0

	def SetSkillToolTip(self, tooltipSkill):
		self.tooltipSkill = tooltipSkill

	def __OnOpenHealGSPBoard(self):

		curPoint, maxPoint = guild.GetDragonPowerPoint()

		if maxPoint - curPoint <= 0:
			chat.AppendChat(1,localeInfo.GUILD_CANNOT_HEAL_GSP_ANYMORE)
			return

		pickDialog = uiPickMoney.PickMoneyDialog()
		pickDialog.LoadDialog()
		pickDialog.SetMax(9)
		pickDialog.SetTitleName(localeInfo.GUILD_HEAL_GSP)
		pickDialog.SetAcceptEvent(ui.__mem_func__(self.__OnOpenHealGSPQuestionDialog))
		pickDialog.Open(maxPoint - curPoint, 1)
		self.pickDialog = pickDialog

	def DeleteGuild(self):
		self.RefreshGuildInfoPage()
		self.RefreshGuildBoardPage()
		self.RefreshGuildMemberPage()
		self.RefreshGuildSkillPage()
		self.RefreshGuildGradePage()
		self.Hide()

	def __OnOpenHealGSPQuestionDialog(self, healGSP):

		money = healGSP * constInfo.GUILD_MONEY_PER_GSP

		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.GUILD_DO_YOU_HEAL_GSP % (money, healGSP))
		questionDialog.SetAcceptEvent(ui.__mem_func__(self.__OnHealGSP))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.__OnCloseQuestionDialog))
		questionDialog.SetWidth(400)
		questionDialog.Open()
		questionDialog.healGSP = healGSP
		self.questionDialog = questionDialog

	def __OnHealGSP(self):
		net.SendGuildChargeGSPPacket(self.questionDialog.healGSP)
		self.__OnCloseQuestionDialog()

	def __OnCloseQuestionDialog(self):
		if self.questionDialog:
			self.questionDialog.Close()
		self.questionDialog = None

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def Close(self):
		self.Hide()


class BuildGuildBuildingWindow(ui.ScriptWindow):
	try:
		GUILD_CATEGORY_LIST = (
				("HEADQUARTER", localeInfo.GUILD_HEADQUARTER),
				("FACILITY", 	localeInfo.GUILD_FACILITY),
				("OBJECT", 	localeInfo.GUILD_OBJECT),
			)
	except:
		GUILD_CATEGORY_LIST = (
				("HEADQUARTER", "Main Building"),
				("FACILITY", "Facility"),
				("OBJECT", "Object"),
			)

	MODE_VIEW = 0
	MODE_POSITIONING = 1
	MODE_PREVIEW = 2

	BUILDING_ALPHA = 0.55

	ENABLE_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	DISABLE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)

	START_INSTANCE_INDEX = 123450
	#WALL_SET_INSTANCE = 14105

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()

		self.closeEvent = None
		self.popup = None
		self.mode = self.MODE_VIEW
		self.race = 0
		self.type = None
		self.x = 0
		self.y = 0
		self.z = 0
		self.rot_x = 0
		self.rot_y = 0
		self.rot_z = 0
		self.rot_x_limit = 0
		self.rot_y_limit = 0
		self.rot_z_limit = 0
		self.needMoney = 0
		self.needStoneCount = 0
		self.needLogCount = 0
		self.needPlywoodCount = 0

		#self.index = 0
		self.indexList = []
		self.raceList = []
		self.posList = []
		self.rotList = []

		index = 0
		for category in self.GUILD_CATEGORY_LIST:
			self.categoryList.InsertItem(index, category[1])
			index += 1

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadWindow(self):

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/buildguildbuildingwindow.py")
		except:
			import exception
			exception.Abort("DeclareGuildWarWindow.__CreateDialog - LoadScript")

		try:
			getObject = self.GetChild

			self.board = getObject("Board")
			self.categoryList = getObject("CategoryList")
			self.buildingList = getObject("BuildingList")
			self.listScrollBar = getObject("ListScrollBar")
			self.positionButton = getObject("PositionButton")
			self.previewButton = getObject("PreviewButton")
			self.posValueX = getObject("BuildingPositionXValue")
			self.posValueY = getObject("BuildingPositionYValue")
			self.ctrlRotationX = getObject("BuildingRotationX")
			self.ctrlRotationY = getObject("BuildingRotationY")
			self.ctrlRotationZ = getObject("BuildingRotationZ")
			self.buildingPriceValue = getObject("BuildingPriceValue")
			self.buildingMaterialStoneValue = getObject("BuildingMaterialStoneValue")
			self.buildingMaterialLogValue = getObject("BuildingMaterialLogValue")
			self.buildingMaterialPlywoodValue = getObject("BuildingMaterialPlywoodValue")

			self.positionButton.SetEvent(ui.__mem_func__(self.__OnSelectPositioningMode))
			self.previewButton.SetToggleDownEvent(ui.__mem_func__(self.__OnEnterPreviewMode))
			self.previewButton.SetToggleUpEvent(ui.__mem_func__(self.__OnLeavePreviewMode))
			self.ctrlRotationX.SetEvent(ui.__mem_func__(self.__OnChangeRotation))
			self.ctrlRotationY.SetEvent(ui.__mem_func__(self.__OnChangeRotation))
			self.ctrlRotationZ.SetEvent(ui.__mem_func__(self.__OnChangeRotation))
			self.listScrollBar.SetScrollEvent(ui.__mem_func__(self.__OnScrollBuildingList))

			getObject("CategoryList").SetEvent(ui.__mem_func__(self.__OnSelectCategory))
			getObject("BuildingList").SetEvent(ui.__mem_func__(self.__OnSelectBuilding))
			getObject("AcceptButton").SetEvent(ui.__mem_func__(self.Build))
			getObject("CancelButton").SetEvent(ui.__mem_func__(self.Close))
			self.board.SetCloseEvent(ui.__mem_func__(self.Close))

		except:
			import exception
			exception.Abort("BuildGuildBuildingWindow.__LoadWindow - BindObject")

	def __CreateWallBlock(self, race, x, y, rot=0.0 ):
		idx = self.START_INSTANCE_INDEX + len(self.indexList)
		self.indexList.append(idx)
		self.raceList.append(race)
		self.posList.append((x, y))
		self.rotList.append(rot)
		chr.CreateInstance(idx)
		chr.SelectInstance(idx)
		chr.SetVirtualID(idx)
		chr.SetInstanceType(chr.INSTANCE_TYPE_OBJECT)

		chr.SetRace(race)
		chr.SetArmor(0)
		chr.Refresh()
		chr.SetLoopMotion(chr.MOTION_WAIT)
		chr.SetBlendRenderMode(idx, self.BUILDING_ALPHA)
		chr.SetRotationAll(0.0, 0.0, rot)

		self.ctrlRotationX.SetSliderPos(0.5)
		self.ctrlRotationY.SetSliderPos(0.5)
		self.ctrlRotationZ.SetSliderPos(0.5)

	def __GetObjectSize(self, race):
		idx = self.START_INSTANCE_INDEX + 1000
		chr.CreateInstance(idx)
		chr.SelectInstance(idx)
		chr.SetVirtualID(idx)
		chr.SetInstanceType(chr.INSTANCE_TYPE_OBJECT)

		chr.SetRace(race)
		chr.SetArmor(0)
		chr.Refresh()
		chr.SetLoopMotion(chr.MOTION_WAIT)
		sx, sy, ex, ey = chr.GetBoundBoxOnlyXY(idx)
		chr.DeleteInstance(idx)
		return sx, sy, ex, ey

	def __GetBuildInPosition(self):

		zList = []
		zList.append( background.GetHeight(self.x+self.sxPos, self.y+self.syPos) )
		zList.append( background.GetHeight(self.x+self.sxPos, self.y+self.eyPos) )
		zList.append( background.GetHeight(self.x+self.exPos, self.y+self.syPos) )
		zList.append( background.GetHeight(self.x+self.exPos, self.y+self.eyPos) )
		zList.append( background.GetHeight(self.x+(self.exPos+self.sxPos)/2, self.y+(self.eyPos+self.syPos)/2) )
		zList.sort()
		return zList[3]

	def __CreateBuildInInstance(self,race):

		self.__DeleteInstance()

		object_base = race - race%10

		door_minX, door_minY, door_maxX, door_maxY = self.__GetObjectSize(object_base+4)
		corner_minX, corner_minY, corner_maxX, corner_maxY = self.__GetObjectSize(object_base+1)
		line_minX, line_minY, line_maxX, line_maxY = self.__GetObjectSize(object_base+2)
		line_width = line_maxX - line_minX
		line_width_half = line_width / 2

		X_SIZE_STEP = 2 * 2
		Y_SIZE_STEP = 8
		sxPos = door_maxX - corner_minX + (line_width_half*X_SIZE_STEP)
		exPos = -sxPos
		syPos = 0
		eyPos = -(corner_maxY*2 + line_width*Y_SIZE_STEP)

		self.sxPos = sxPos
		self.syPos = syPos
		self.exPos = exPos
		self.eyPos = eyPos

		z = self.__GetBuildInPosition()

		## Door
		self.__CreateWallBlock(object_base+4, 0.0, syPos)

		## Corner
		self.__CreateWallBlock(object_base+1, sxPos, syPos)
		self.__CreateWallBlock(object_base+1, exPos, syPos, 270.0)
		self.__CreateWallBlock(object_base+1, sxPos, eyPos, 90.0)
		self.__CreateWallBlock(object_base+1, exPos, eyPos,180.0 )

		## Line
		lineBlock = object_base+2
		line_startX = -door_maxX - line_minX - (line_width_half*X_SIZE_STEP)
		self.__CreateWallBlock(lineBlock, line_startX, eyPos)
		self.__CreateWallBlock(lineBlock, line_startX+line_width*1, eyPos)
		self.__CreateWallBlock(lineBlock, line_startX+line_width*2, eyPos)
		self.__CreateWallBlock(lineBlock, line_startX+line_width*3, eyPos)
		for i in xrange(X_SIZE_STEP):
			self.__CreateWallBlock(lineBlock, line_startX+line_width*(3+i+1), eyPos)
		for i in xrange(X_SIZE_STEP/2):
			self.__CreateWallBlock(lineBlock, door_minX - line_maxX - line_width*i, syPos)
			self.__CreateWallBlock(lineBlock, door_maxX - line_minX + line_width*i, syPos)
		for i in xrange(Y_SIZE_STEP):
			self.__CreateWallBlock(lineBlock, sxPos, line_minX + corner_minX - line_width*i, 90.0)
			self.__CreateWallBlock(lineBlock, exPos, line_minX + corner_minX - line_width*i, 90.0)

		self.SetBuildingPosition(int(self.x), int(self.y), self.__GetBuildInPosition())

	def __DeleteInstance(self):
		if not self.indexList:
			return

		for index in self.indexList:
			chr.DeleteInstance(index)

		self.indexList = []
		self.raceList = []
		self.posList = []
		self.rotList = []

	def __CreateInstance(self, race):

		self.__DeleteInstance()

		self.race = race

		idx = self.START_INSTANCE_INDEX
		self.indexList.append(idx)
		self.posList.append((0, 0))
		self.rotList.append(0)

		chr.CreateInstance(idx)
		chr.SelectInstance(idx)
		chr.SetVirtualID(idx)
		chr.SetInstanceType(chr.INSTANCE_TYPE_OBJECT)

		chr.SetRace(race)
		chr.SetArmor(0)
		chr.Refresh()
		chr.SetLoopMotion(chr.MOTION_WAIT)
		chr.SetBlendRenderMode(idx, self.BUILDING_ALPHA)

		self.SetBuildingPosition(int(self.x), int(self.y), 0)
		self.ctrlRotationX.SetSliderPos(0.5)
		self.ctrlRotationY.SetSliderPos(0.5)
		self.ctrlRotationZ.SetSliderPos(0.5)

	def Build(self):

		if not self.__IsEnoughMoney():
			self.__PopupDialog(localeInfo.GUILD_NOT_ENOUGH_MONEY)
			return
		if not self.__IsEnoughMaterialStone():
			self.__PopupDialog(localeInfo.GUILD_NOT_ENOUGH_MATERIAL)
			return
		if not self.__IsEnoughMaterialLog():
			self.__PopupDialog(localeInfo.GUILD_NOT_ENOUGH_MATERIAL)
			return
		if not self.__IsEnoughMaterialPlywood():
			self.__PopupDialog(localeInfo.GUILD_NOT_ENOUGH_MATERIAL)
			return

		## /build c vnum x y x_rot y_rot z_rot
		## /build d vnum
		if "BUILDIN" == self.type:
			for i in xrange(len(self.raceList)):
				race = self.raceList[i]
				xPos, yPos = self.posList[i]
				rot = self.rotList[i]
				net.SendChatPacket("/build c %d %d %d %d %d %d" % (race, int(self.x+xPos), int(self.y+yPos), self.rot_x, self.rot_y, rot))
		else:
			net.SendChatPacket("/build c %d %d %d %d %d %d" % (self.race, int(self.x), int(self.y), self.rot_x, self.rot_y, self.rot_z))

		self.Close()

	def Open(self):
		x, y, z = player.GetMainCharacterPosition()
		app.SetCameraSetting(int(x), int(-y), int(z), 3000, 0, 30)

		background.VisibleGuildArea()

		self.x = x
		self.y = y
		self.z = z
		self.categoryList.SelectItem(0)
		self.buildingList.SelectItem(0)
		self.SetTop()
		self.Show()
		self.__DisablePCBlocker()

		import debugInfo
		if debugInfo.IsDebugMode():
			self.categoryList.SelectItem(2)
			self.buildingList.SelectItem(0)

	def Close(self):

		self.__DeleteInstance()

		background.DisableGuildArea()

		self.Hide()
		self.__OnClosePopupDialog()
		self.__EnablePCBlocker()
		self.__UnlockCameraMoving()
		if self.closeEvent:
			self.closeEvent()

	def Destory(self):
		self.Close()

		self.ClearDictionary()
		self.board = None
		self.categoryList = None
		self.buildingList = None
		self.listScrollBar = None
		self.positionButton = None
		self.previewButton = None
		self.posValueX = None
		self.posValueY = None
		self.ctrlRotationX = None
		self.ctrlRotationY = None
		self.ctrlRotationZ = None
		self.buildingPriceValue = None
		self.buildingMaterialStoneValue = None
		self.buildingMaterialLogValue = None
		self.buildingMaterialPlywoodValue = None
		self.closeEvent = None

	def SetCloseEvent(self, event):
		self.closeEvent = event

	def __PopupDialog(self, text):
		popup = uiCommon.PopupDialog()
		popup.SetText(text)
		popup.SetAcceptEvent(self.__OnClosePopupDialog)
		popup.Open()
		self.popup = popup

	def __OnClosePopupDialog(self):
		self.popup = None

	def __EnablePCBlocker(self):
		## PC Blocker A3~~~~ ~O~U. (Ao~~~O~~)
		chr.SetInstanceType(chr.INSTANCE_TYPE_BUILDING)

		for idx in self.indexList:
			chr.SetBlendRenderMode(idx, 1.0)

	def __DisablePCBlocker(self):
		## PC Blocker A3~~~~ 2~~U. (3EAo~~~O~~)
		chr.SetInstanceType(chr.INSTANCE_TYPE_OBJECT)

		for idx in self.indexList:
			chr.SetBlendRenderMode(idx, self.BUILDING_ALPHA)

	def __OnSelectPositioningMode(self):
		if self.MODE_PREVIEW == self.mode:
			self.positionButton.SetUp()
			return

		self.mode = self.MODE_POSITIONING
		self.Hide()

	def __OnEnterPreviewMode(self):

		if self.MODE_POSITIONING == self.mode:
			self.previewButton.SetUp()
			return

		self.mode = self.MODE_PREVIEW
		self.positionButton.SetUp()
		self.__UnlockCameraMoving()
		self.__EnablePCBlocker()

	def __OnLeavePreviewMode(self):
		self.__RestoreViewMode()

	def __RestoreViewMode(self):
		self.__DisablePCBlocker()
		self.__LockCameraMoving()
		self.mode = self.MODE_VIEW
		self.positionButton.SetUp()
		self.previewButton.SetUp()

	def __IsEnoughMoney(self):

		if app.IsEnableTestServerFlag():
			return TRUE

		curMoney = player.GetMoney()
		if curMoney < self.needMoney:
			return FALSE
		return TRUE

	def __IsEnoughMaterialStone(self):

		if app.IsEnableTestServerFlag():
			return TRUE

		curStoneCount = player.GetItemCountByVnum(MATERIAL_STONE_ID)
		if curStoneCount < self.needStoneCount:
			return FALSE
		return TRUE

	def __IsEnoughMaterialLog(self):

		if app.IsEnableTestServerFlag():
			return TRUE

		curLogCount = player.GetItemCountByVnum(MATERIAL_LOG_ID)
		if curLogCount < self.needLogCount:
			return FALSE
		return TRUE

	def __IsEnoughMaterialPlywood(self):

		if app.IsEnableTestServerFlag():
			return TRUE

		curPlywoodCount = player.GetItemCountByVnum(MATERIAL_PLYWOOD_ID)
		if curPlywoodCount < self.needPlywoodCount:
			return FALSE
		return TRUE

	def __OnSelectCategory(self):
		self.listScrollBar.SetPos(0.0)
		self.__RefreshItem()

	def __SetBuildingData(self, data):
		self.buildingPriceValue.SetText(NumberToMoneyString(data["PRICE"]))

		self.needMoney = int(data["PRICE"])

		materialList = data["MATERIAL"]
		self.needStoneCount = int(materialList[MATERIAL_STONE_INDEX])
		self.needLogCount = int(materialList[MATERIAL_LOG_INDEX])
		self.needPlywoodCount = int(materialList[MATERIAL_PLYWOOD_INDEX])

		self.buildingMaterialStoneValue.SetText(materialList[MATERIAL_STONE_INDEX] + localeInfo.THING_COUNT)
		self.buildingMaterialLogValue.SetText(materialList[MATERIAL_LOG_INDEX] + localeInfo.THING_COUNT)
		self.buildingMaterialPlywoodValue.SetText(materialList[MATERIAL_PLYWOOD_INDEX] + localeInfo.THING_COUNT)

		if self.__IsEnoughMoney():
			self.buildingPriceValue.SetPackedFontColor(self.ENABLE_COLOR)
		else:
			self.buildingPriceValue.SetPackedFontColor(self.DISABLE_COLOR)

		if self.__IsEnoughMaterialStone():
			self.buildingMaterialStoneValue.SetPackedFontColor(self.ENABLE_COLOR)
		else:
			self.buildingMaterialStoneValue.SetPackedFontColor(self.DISABLE_COLOR)

		if self.__IsEnoughMaterialLog():
			self.buildingMaterialLogValue.SetPackedFontColor(self.ENABLE_COLOR)
		else:
			self.buildingMaterialLogValue.SetPackedFontColor(self.DISABLE_COLOR)

		if self.__IsEnoughMaterialPlywood():
			self.buildingMaterialPlywoodValue.SetPackedFontColor(self.ENABLE_COLOR)
		else:
			self.buildingMaterialPlywoodValue.SetPackedFontColor(self.DISABLE_COLOR)

		self.rot_x_limit = data["X_ROT_LIMIT"]
		self.rot_y_limit = data["Y_ROT_LIMIT"]
		self.rot_z_limit = data["Z_ROT_LIMIT"]
		self.ctrlRotationX.Enable()
		self.ctrlRotationY.Enable()
		self.ctrlRotationZ.Enable()
		if 0 == self.rot_x_limit:
			self.ctrlRotationX.Disable()
		if 0 == self.rot_y_limit:
			self.ctrlRotationY.Disable()
		if 0 == self.rot_z_limit:
			self.ctrlRotationZ.Disable()

	def __OnSelectBuilding(self):
		buildingIndex = self.buildingList.GetSelectedItem()
		if buildingIndex >= len(BUILDING_DATA_LIST):
			return

		categoryIndex = self.categoryList.GetSelectedItem()
		if categoryIndex >= len(self.GUILD_CATEGORY_LIST):
			return
		selectedType = self.GUILD_CATEGORY_LIST[categoryIndex][0]

		index = 0
		for data in BUILDING_DATA_LIST:
			type = data["TYPE"]
			vnum = data["VNUM"]
			if selectedType != type:
				continue

			if index == buildingIndex:
				self.type = type
				if "BUILDIN" == self.type:
					self.__CreateBuildInInstance(vnum)
				else:
					self.__CreateInstance(vnum)

				self.__SetBuildingData(data)

			index += 1

	def __OnScrollBuildingList(self):
		viewItemCount = self.buildingList.GetViewItemCount()
		itemCount = self.buildingList.GetItemCount()
		pos = self.listScrollBar.GetPos() * (itemCount-viewItemCount)
		self.buildingList.SetBasePos(int(pos))

	def __OnChangeRotation(self):
		self.rot_x = self.ctrlRotationX.GetSliderPos() * self.rot_x_limit - self.rot_x_limit/2
		self.rot_y = self.ctrlRotationY.GetSliderPos() * self.rot_y_limit - self.rot_y_limit/2
		self.rot_z = (self.ctrlRotationZ.GetSliderPos() * 360 + 180) % 360
		if "BUILDIN" == self.type:
			chr.SetRotationAll(self.rot_x, self.rot_y, self.rot_z)
		else:
			chr.SetRotationAll(self.rot_x, self.rot_y, self.rot_z)

	def __LockCameraMoving(self):
		app.SetCameraSetting(int(self.x), int(-self.y), int(self.z), 3000, 0, 30)

	def __UnlockCameraMoving(self):
		app.SetDefaultCamera()

	def __RefreshItem(self):

		self.buildingList.ClearItem()

		categoryIndex = self.categoryList.GetSelectedItem()
		if categoryIndex >= len(self.GUILD_CATEGORY_LIST):
			return
		selectedType = self.GUILD_CATEGORY_LIST[categoryIndex][0]

		index = 0
		for data in BUILDING_DATA_LIST:
			if selectedType != data["TYPE"]:
				continue

			if data["SHOW"]:
				self.buildingList.InsertItem(index, data["LOCAL_NAME"])

			index += 1

		self.buildingList.SelectItem(0)

		if self.buildingList.GetItemCount() < self.buildingList.GetViewItemCount():
			self.buildingList.SetSize(120, self.buildingList.GetHeight())
			self.buildingList.LocateItem()
			self.listScrollBar.Hide()
		else:
			self.buildingList.SetSize(105, self.buildingList.GetHeight())
			self.buildingList.LocateItem()
			self.listScrollBar.Show()
			

	def SettleCurrentPosition(self):
		guildID = miniMap.GetGuildAreaID(self.x, self.y)

		import debugInfo
		if debugInfo.IsDebugMode():
			guildID = player.GetGuildID()

		if guildID != player.GetGuildID():
			return

		self.__RestoreViewMode()
		self.__LockCameraMoving()
		self.Show()

	def SetBuildingPosition(self, x, y, z):
		self.x = x
		self.y = y
		self.posValueX.SetText(str(int(x)))
		self.posValueY.SetText(str(int(y)))

		for i in xrange(len(self.indexList)):
			idx = self.indexList[i]
			xPos, yPos = self.posList[i]

			chr.SelectInstance(idx)
			if 0 != z:
				self.z = z
				chr.SetPixelPosition(int(x+xPos), int(y+yPos), int(z))
			else:
				chr.SetPixelPosition(int(x+xPos), int(y+yPos))

	def IsPositioningMode(self):
		if self.MODE_POSITIONING == self.mode:
			return TRUE
		return FALSE

	def IsPreviewMode(self):
		if self.MODE_PREVIEW == self.mode:
			return TRUE
		return FALSE

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
