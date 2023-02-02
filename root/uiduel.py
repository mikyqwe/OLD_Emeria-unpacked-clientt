###################################################################
# title_name		: Duel System Advanced
# date_created		: 2016.09.10
# filename			: uiDuel.py
# author			: VegaS
# version			: 0.2.0
#
import ui
import wndMgr
import chat
import player as ch
import constInfo as pvp
import uiGuild as uiPvP
import uiCommon as message
import playerSettingModule as face
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import net as commandServer
import app

def CalculateTimeLeft(iTime):
	A, B = divmod(iTime, 60)
	C, A = divmod(A, 60)
	return "%02d:%02d" % (A, B)	

mCheck = 0

FACE_IMAGE_DICT = {
	face.RACE_WARRIOR_M	: "icon/face/warrior_m.tga",
	face.RACE_WARRIOR_W	: "icon/face/warrior_w.tga",
	face.RACE_ASSASSIN_M	: "icon/face/assassin_m.tga",
	face.RACE_ASSASSIN_W	: "icon/face/assassin_w.tga",
	face.RACE_SURA_M		: "icon/face/sura_m.tga",
	face.RACE_SURA_W		: "icon/face/sura_w.tga",
	face.RACE_SHAMAN_M	: "icon/face/shaman_m.tga",
	face.RACE_SHAMAN_W	: "icon/face/shaman_w.tga",
	#face.RACE_WOLFMAN_M	: "icon/face/wolfman_m.tga"
}

BINARY_DUEL_GET_ = {
	"selected"  : {
		0 : 0,
		1 : 0,
		2 : 0,
		3 : 0,
		4 : 0,
		5 : 0,
		6 : 0,
		7 : 0,
	},
	"amount"  : {
		0 : 0
	}
}

class WindowEquipmentBlock(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)

		self.SetSize(250, 100)
		self.SetTitleName(localeInfo.DUEL_TITLENAME)
		self.SetCloseEvent(ui.__mem_func__(self.Close))
		self.SetCenterPosition()
		self.AddFlag('movable')
		self.SetTop()

		self.btns = []

		self.Add(localeInfo.DUEL_EQUIP_BLOCK, self.Enable)
		self.Add(localeInfo.DUEL_EQUIP_UNBLOCK, self.Disable)	

	def Add(self, text, event):
		height = len(self.btns) * 26

		button = ui.Button()
		button.SetParent(self)
		button.SetPosition(33, 35 + height)
		button.SetUpVisual("d:/ymir work/ui/public/XLarge_Button_01.sub")
		button.SetOverVisual("d:/ymir work/ui/public/XLarge_Button_02.sub")
		button.SetDownVisual("d:/ymir work/ui/public/XLarge_Button_03.sub")
		button.SetText(text)
		button.SetEvent(event)
		button.Show()
		
		self.btns.append(button)

	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)

	def Destroy(self):
		self.Hide()

		for obj in self.btns:
			obj.Hide()
			obj = None
		del self.btns[:]
		self.btns = None

	def Close(self):
		self.Hide()

	def Open(self):
		self.Show()

	def Enable(self):
		commandServer.SendChatPacket("/pvp_block_equipment BLOCK")
		
	def Disable(self):
		commandServer.SendChatPacket("/pvp_block_equipment UNBLOCK")

class WindowLiveInformations(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/pvp_advanced_informations.py")
		getObject = self.GetChild

		self.wndBoard = getObject("Board")
		self.name = self.GetChild("NameCharacterValue")
		self.level = self.GetChild("LevelCharacterValue")
		self.face = getObject("CharacterIcon")
		self.MoneyText = getObject("Money")

		width = self.GetWidth()	
		x = min(0 + width/2, wndMgr.GetScreenWidth() - width/2) - width/2
		y = wndMgr.GetScreenHeight() - 305
		box_x = x+10
		text_x = x + 67
		color = "|cFFff5148"

		self.checkBoxTable	=	{
									0	:	[uiPvP.CheckBox2(self, box_x, y+65, lambda arg = 0: self.SetType(arg)), 0, self.SetText(text_x, y+65, color + localeInfo.DUEL_BLOCK_CHANGE_ITEM)],
									1	:	[uiPvP.CheckBox2(self, box_x, y+65+20, lambda arg = 1: self.SetType(arg)), 0, self.SetText(text_x, y+65+20, color + localeInfo.DUEL_BLOCK_BUFF)],
									2	:	[uiPvP.CheckBox2(self, box_x, y+65+20+20, lambda arg = 2: self.SetType(arg)), 0, self.SetText(text_x, y+65+20+20, color + localeInfo.DUEL_BLOCK_POTION_RED)],
									3	:	[uiPvP.CheckBox2(self, box_x, y+65+20+20+20, lambda arg = 3: self.SetType(arg)), 0, self.SetText(text_x, y+65+20+20+20, color + localeInfo.DUEL_BLOCK_HORSE_MOUNT)],
									4	:	[uiPvP.CheckBox2(self, box_x+155, y+65, lambda arg = 4: self.SetType(arg)), 0, self.SetText(text_x+155, y+65, color + localeInfo.DUEL_BLOCK_PET)],
									5	:	[uiPvP.CheckBox2(self, box_x+155, y+65+20, lambda arg = 5: self.SetType(arg)), 0, self.SetText(text_x+155, y+65+20, color + localeInfo.DUEL_BLOCK_POLY)],
									6	:	[uiPvP.CheckBox2(self, box_x+155, y+65+20+20, lambda arg = 6: self.SetType(arg)), 0, self.SetText(text_x+155, y+65+20+20, color + localeInfo.DUEL_BLOCK_PARTY)],
									7	:	[uiPvP.CheckBox2(self, box_x+155, y+65+20+20+20, lambda arg = 7: self.SetType(arg)), 0, self.SetText(text_x+155, y+65+20+20+20, color + localeInfo.DUEL_BLOCK_EXCHANGE)]
								}

		self.wndBoard.SetPosition(x + 5, y)

	def SetText(self, x, y, text):
		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetPosition(x, y)
		self.textLine.SetText(text)
		self.textLine.Show()

		return self.textLine

	def ShowInformations(self, value):	
		self.name.SetText((str(value[0])))
		self.level.SetText((str(value[1])))
		self.face.LoadImage(FACE_IMAGE_DICT[int(value[2])])

		for i in xrange(8):
			self.checkBoxTable[i][0].SetCheck((int(value[i + 3])))

		self.MoneyText.SetText(localeInfo.NumberToMoneyString(str(value[11])))
		self.Show()

class Initializate(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.Name = ""
		self.Guild = ""
		self.Level = 0
		self.PlayTime = 0
		self.VID = 0
		self.acceptButton = 0
		self.declineButton = 0
		self.HP = 0
		self.SP = 0	
		self.Race = 0

		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/pvp_advanced.py")
		getObject = self.GetChild

		self.board = getObject("Board")
		self.board.SetCloseEvent(self.Close)
		self.acceptButton = getObject("AcceptButton")
		self.declineButton = getObject("DenyButton")

		self.name = self.GetChild("NameCharacterValue")
		#self.guild = self.GetChild("GuildCharacterValue")
		self.level = self.GetChild("LevelCharacterValue")
		#self.playtime = self.GetChild("PlayTimeCharacterValue")
		self.hp = self.GetChild("ValueHP")
		#self.sp = self.GetChild("ValueMP")
		self.face = getObject("CharacterIcon")
		self.percent_hp = getObject("percent_hp")
		#self.percent_sp = getObject("percent_sp")
		
		self.textLineTime = ui.TextLine()
		self.textLineTime.SetParent(self.board)
		self.textLineTime.SetPosition(408, 9)
		self.textLineTime.SetPackedFontColor(0xffdcf600)
		self.textLineTime.Hide()

		self.MoneyText = getObject("Money")
		self.MoneySlot = getObject("Money_Slot")
		self.MoneySlot.SetEvent(ui.__mem_func__(self.GetSlotMoney))
		self.MoneyText.Hide()
		self.MoneySlot.Hide()

		self.checkBoxTable	=	{
									0	:	[uiPvP.CheckBox2(self, 490, 50, lambda arg = 0: self.SetType(arg)), 0, self.SetText(377, 50, localeInfo.DUEL_BLOCK_CHANGE_ITEM)],
									1	:	[uiPvP.CheckBox2(self, 490, 50+25, lambda arg = 1: self.SetType(arg)), 0, self.SetText(377, 50+25, localeInfo.DUEL_BLOCK_BUFF)],
									2	:	[uiPvP.CheckBox2(self, 490, 50+25+25, lambda arg = 2: self.SetType(arg)), 0, self.SetText(377, 50+25+25, localeInfo.DUEL_BLOCK_POTION_RED)],
									3	:	[uiPvP.CheckBox2(self, 490, 50+25+25+25, lambda arg = 3: self.SetType(arg)), 0, self.SetText(377, 50+25+25+25, localeInfo.DUEL_BLOCK_HORSE_MOUNT)],
									4	:	[uiPvP.CheckBox2(self, 490, 50+25+25+25+25, lambda arg = 4: self.SetType(arg)), 0, self.SetText(377, 50+25+25+25+25, localeInfo.DUEL_BLOCK_PET)],
									5	:	[uiPvP.CheckBox2(self, 490, 50+25+25+25+25+25, lambda arg = 5: self.SetType(arg)), 0, self.SetText(377, 50+25+25+25+25+25, localeInfo.DUEL_BLOCK_POLY)],
									6	:	[uiPvP.CheckBox2(self, 490, 50+25+25+25+25+25+25, lambda arg = 6: self.SetType(arg)), 0, self.SetText(377, 50+25+25+25+25+25+25, localeInfo.DUEL_BLOCK_PARTY)],
									7	:	[uiPvP.CheckBox2(self, 490, 50+25+25+25+25+25+25+25, lambda arg = 7: self.SetType(arg)), 0, self.SetText(377, 50+25+25+25+25+25+25+25, localeInfo.DUEL_BLOCK_EXCHANGE)]
								}

		if self.acceptButton:
			self.acceptButton.SetEvent(ui.__mem_func__(self.ApplyRequest))

		if self.declineButton:
			self.declineButton.SetEvent(ui.__mem_func__(self.Close))

		self.percent_hp.SetPercentage(100, 100)
		#self.percent_sp.SetPercentage(100, 100)
		self.SetCenterPosition()

	def OpenDialog(self, VID, Name, Guild, Level, Race, PlayTime, HP, SP):

		self.VID   = int(VID)
		self.Name  = Name
		self.Guild  = Guild
		self.Level = str(Level)
		self.Race  = int(Race)
		self.PlayTime  = int(PlayTime)
		self.HP  = str(HP)
		self.SP  = str(SP)

		self.SetTitle(localeInfo.DUEL_TARGET_NAME + Name)
		self.name.SetText(Name)
		#self.guild.SetText(self.Guild)
		self.level.SetText(self.Level)
		#self.playtime.SetText(localeInfo.FormatTime(self.PlayTime))
		self.hp.SetText(self.HP)
		#self.sp.SetText(self.SP)
		self.face.LoadImage(FACE_IMAGE_DICT[self.Race])

		self.Show()

	def Selected(self, value):
		for i in xrange(8):
			self.checkBoxTable[i][0].SetCheck((int(value[i])))		
		
		self.MoneyText.SetText(localeInfo.NumberToMoneyString(str(value[8])))

		global mCheck
		mCheck = 1
		
		self.textLineTime.Show()
		self.leftTime = app.GetGlobalTimeStamp() + 30

	def SetType(self, arg):
		global mCheck
		if mCheck == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DUEL_VICTIM_ERROR)
			return
		else:
			for index in xrange(len(BINARY_DUEL_GET_["selected"])):
				if arg == index and mCheck != 1:
					if BINARY_DUEL_GET_["selected"][arg] == 1:
						self.checkBoxTable[arg][0].SetCheck(0)
						BINARY_DUEL_GET_["selected"][arg] = 0
					else:
						self.checkBoxTable[arg][0].SetCheck(1)
						BINARY_DUEL_GET_["selected"][arg] = 1

	def ApplyRequest(self):
		global mCheck
		if mCheck == 1:
			commandServer.SendChatPacket("/pvp %d accept" % (self.VID))
		else:
			commandServer.SendChatPacket("/pvp %d %d %d %d %d %d %d %d %d %d" % ((self.VID), (int(BINARY_DUEL_GET_["selected"][0])), (int(BINARY_DUEL_GET_["selected"][1])), (int(BINARY_DUEL_GET_["selected"][2])), (int(BINARY_DUEL_GET_["selected"][3])), (int(BINARY_DUEL_GET_["selected"][4])), (int(BINARY_DUEL_GET_["selected"][5])), (int(BINARY_DUEL_GET_["selected"][6])), (int(BINARY_DUEL_GET_["selected"][7])), (int(BINARY_DUEL_GET_["amount"][0]))))				

		self.Remove()
		pvp.DUEL_IS_SHOW_EQUIP = 1

	def Remove(self):
		global mCheck
		mCheck = 0

		for index in xrange(len(BINARY_DUEL_GET_["selected"])):
			self.checkBoxTable[index][0].SetCheck(0)
			BINARY_DUEL_GET_["selected"][index] = 0
			BINARY_DUEL_GET_["amount"][0] = 0

		self.Hide()
		self.MoneyText.SetText("")

	def SetText(self, x, y, text):
		self.textLine = ui.TextLine()
		self.textLine.SetParent(self)
		self.textLine.SetPosition(x, y)
		self.textLine.SetText(text)
		self.textLine.Show()

		return self.textLine

	def SetTitle(self, name):
		self.board.SetTitleName(name)

	def Close(self):
		commandServer.SendChatPacket("/decline_pvp %d" % (self.VID))

		self.Remove()
		pvp.DUEL_IS_SHOW_EQUIP = 1

	def GetSlotMoney(self):
		global mCheck
		if mCheck == 1:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DUEL_VICTIM_ERROR)
			return
		else:
			self.inputDialog = message.Duel_InputMoneyBet()
			self.inputDialog.SetMaxLength(9)
			self.inputDialog.SetAcceptEvent(lambda arg = TRUE: self.SetMoney())
			self.inputDialog.SetCancelEvent(ui.__mem_func__(self.Cancel))
			self.inputDialog.SetAcceptText(localeInfo.DUEL_MONEY_ADD)
			self.inputDialog.SetCancelText(localeInfo.DUEL_MONEY_CANCEL)
			self.inputDialog.SetTitle(localeInfo.DUEL_MONEY_TITLE)
			self.inputDialog.SetDescription(localeInfo.DUEL_MONEY_CURRENT + localeInfo.NumberToMoneyString(str(ch.GetElk())))
			self.inputDialog.Open()

	def SetMoney(self):

		if not self.inputDialog:
			return True

		updateMoney = self.inputDialog.GetText()
		currentMoney = ch.GetElk()

		if not updateMoney:
			return True

		if not updateMoney.isdigit():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DUEL_MONEY_ERROR_1)
			return True

		if int(updateMoney) <= 0:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DUEL_MONEY_ERROR_2)
			return True

		if len(updateMoney) < 0:
			return True

		if updateMoney < 0:
			return True

		global mCheck
		if updateMoney.isdigit() and mCheck != 1:
			if int(updateMoney) <= int(currentMoney):
				self.MoneyText.SetText(localeInfo.NumberToMoneyString(str(updateMoney)))
				BINARY_DUEL_GET_["amount"][0] = (int(updateMoney))
				self.inputDialog.Hide()
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DUEL_MONEY_ERROR_3)
				return True

	def Cancel(self):
		self.inputDialog.Hide()
		
	def SetTime(self, iLeft):
		leftTime = iLeft - app.GetGlobalTimeStamp()
		
		if leftTime <= 0:
			leftTime = 0
			self.Close()

		self.textLineTime.SetText("Time remaining: [%s]" % (CalculateTimeLeft(leftTime)))

	def OnUpdate(self):
		global mCheck
		if mCheck == 1:
			self.SetTime(int(self.leftTime))