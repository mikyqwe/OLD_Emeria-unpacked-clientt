import app
import ui
import grp
import net
import guild
import messenger
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import constInfo
import uiToolTip
import uiGameOption

import dbg
import wndMgr
import uiCommon
import apollo_interface
from _weakref import proxy
import apollo_interface

if app.ENABLE_RENEW_MESSENGER_WHISPER:
	import uiContact, player, ime

FRIEND = 0
GUILD = 1
TEAM = 2 

class MessengerItem(ui.Window):

	def __init__(self, getParentEvent):
		ui.Window.__init__(self)

		self.SetParent(getParentEvent())
		self.AddFlag("float")


		self.HideGrp = 0

		self.name = ""



		self.img = ui.ImageBox()
		self.img.AddFlag("not_pick")
		self.img.SetParent(self)
		self.img.SetPosition(-15,-10)
		self.img.Show()

		self.image = ui.ImageBox()
		self.image.AddFlag("not_pick")
		self.image.SetParent(self)
		self.image.SetPosition(0,5)
		self.image.Show()

		self.imgPref = ui.ImageBox()
		self.imgPref.AddFlag("not_pick")
		self.imgPref.SetParent(self)
		self.imgPref.SetPosition(-10,2)
		self.imgPref.SetTop()
		self.imgPref.Show()

		self.imageGrup = ui.ImageBox()
		self.imageGrup.AddFlag("not_pick")
		self.imageGrup.SetParent(self)
		self.imageGrup.SetPosition(-10,1)
		self.imageGrup.SetTop()
		self.imageGrup.Show()

		self.text = ui.TextLine()
		self.text.SetParent(self)
		self.text.SetPosition(20, 7)
		self.text.Show()

		self.text1 = ui.TextLine()
		self.text1.SetParent(self)
		self.text1.SetPosition(25, 7)
		self.text1.SetPackedFontColor(apollo_interface.COLOR_HOVER)
		self.text1.Show()

		self.selectedimg = ui.ImageBox()
		self.selectedimg.SetParent(self)
		self.selectedimg.SetPosition(-12, 6)
		self.selectedimg.LoadImage(apollo_interface.PATCH_COMMON + "/list_item/selected_fill.png")
		self.lovePoint = -1
		self.lovePointToolTip = None

		self.isSelected = FALSE

		self.getParentEvent = getParentEvent

	def SetLast(self):
		self.imgPref.LoadImage(apollo_interface.PATCH_SPECIAL + "/friendlist/icon_prefix_last.png")

	def SetName(self, name):
		self.name = name
		if name:
			self.text.SetText(name)
			self.SetSize(20 + 6*len(name) + 4, 16)

			if localeInfo.IsARABIC():
				self.text.SetPosition(20 + 6*len(name) + 4, 2)

	def SetName2(self, name):
		self.name = name
		if name:
			self.text1.SetText(name)
			self.SetSize(20 + 6*len(name) + 4, 16)

			if localeInfo.IsARABIC():
				self.text.SetPosition(20 + 6*len(name) + 4, 2)

	def SetLovePoint(self, lovePoint):
		self.lovePoint = lovePoint

	def Select(self, type=1):
		self.isSelected = TRUE
		self.HideGrp = 0
		if type != 0:
			self.selectedimg.Show()
			self.HideGrp = 1

	def UnSelect(self):
		self.isSelected = FALSE
		self.selectedimg.Hide()

	def GetName(self):
		return self.name

	def GetStepWidth(self):
		return 0

	# Whisper
	def CanWhisper(self):
		return FALSE

	def IsOnline(self):
		return FALSE

	def IsMobile(self):
		return FALSE

	def OnWhisper(self):
		pass

	def OnMobileMessage(self):
		pass

	# Remove
	def CanRemove(self):
		return FALSE

	def OnRemove(self):
		return FALSE

	# Warp
	def CanWarp(self):
		return FALSE

	def OnWarp(self):
		pass

	def OnMouseOverIn(self):
		if -1 != self.lovePoint:
			if not self.lovePointToolTip:
				self.lovePointToolTip = uiToolTip.ToolTip(100)
				self.lovePointToolTip.SetTitle(self.name)
				self.lovePointToolTip.AppendTextLine(localeInfo.AFF_LOVE_POINT % (self.lovePoint))
				self.lovePointToolTip.ResizeToolTip()
			self.lovePointToolTip.ShowToolTip()

	def OnMouseOverOut(self):
		if self.lovePointToolTip:
			self.lovePointToolTip.HideToolTip()

	def OnMouseLeftButtonDown(self):
		self.getParentEvent().OnSelectItem(self)

	def OnMouseLeftButtonDoubleClick(self):
		self.getParentEvent().OnDoubleClickItem(self)


class MessengerMemberItem(MessengerItem):

	STATE_OFFLINE = 0
	STATE_ONLINE = 1
	STATE_MOBILE = 2

	IMAGE_FILE_NAME = {	"ONLINE" : apollo_interface.PATCH_SPECIAL_1 + "/online.png",
						"OFFLINE" : apollo_interface.PATCH_SPECIAL_1 + "/offline.png",
						"MOBILE" : apollo_interface.PATCH_SPECIAL_1 + "/offline.png", }

	def __init__(self, getParentEvent):
		MessengerItem.__init__(self, getParentEvent)
		self.key = None
		self.state = self.STATE_OFFLINE
		self.mobileFlag = FALSE
		self.Offline()

	def GetStepWidth(self):
		return 15


	def SetKey(self, key):
		self.key = key

	def IsSameKey(self, key):
		return self.key == key

	def IsOnline(self):
		if self.STATE_ONLINE == self.state:
			return TRUE

		return FALSE

	def IsMobile(self):
		if self.STATE_MOBILE == self.state:
			return TRUE

		return FALSE

	def Online(self):
		self.imgPref.LoadImage("%s/friendlist/icon_prefix_last2.png" % apollo_interface.PATCH_SPECIAL)
		self.image.LoadImage(self.IMAGE_FILE_NAME["ONLINE"])
		self.text.SetPackedFontColor(0xffa08784)
		self.state = self.STATE_ONLINE

	def Offline(self):
		if self.mobileFlag:
			self.image.LoadImage(self.IMAGE_FILE_NAME["MOBILE"])
			self.state = self.STATE_MOBILE

		else:
			self.image.LoadImage(self.IMAGE_FILE_NAME["OFFLINE"])
			self.state = self.STATE_OFFLINE
			self.text.SetPackedFontColor(0xff757170)
		self.imgPref.LoadImage("%s/friendlist/icon_prefix_last2.png" % apollo_interface.PATCH_SPECIAL)


	def SetMobile(self, flag):
		self.mobileFlag = flag

		if not self.IsOnline():
			self.Offline()

	def CanWhisper(self):
		if self.IsOnline():
			return TRUE

		return FALSE

	def OnWhisper(self):
		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.getParentEvent().whisperButtonEvent(self.GetName())
		else:
			if self.IsOnline():
				self.getParentEvent().whisperButtonEvent(self.GetName())

	def OnMobileMessage(self):
		if not uiGameOption.MOBILE:
			return

		if not self.IsMobile():
			return

		self.getParentEvent().SendMobileMessage(self.GetName())

	def Select(self):
		MessengerItem.Select(self)

class MessengerGroupItem(MessengerItem):

	IMAGE_FILE_NAME = {	"OPEN" : apollo_interface.PATCH_COMMON + "/scrollbar/btn_down_01_normal.png",

						"CLOSE" : apollo_interface.PATCH_COMMON + "/scrollbar/btn_up_03_active.png", }

	def __init__(self, getParentEvent):
		self.isOpen = FALSE
		self.memberList = []

		self.count = 0
		MessengerItem.__init__(self, getParentEvent)

	def AppendMember(self, member, key, name):
		member.SetKey(key)
		# member.SetName2(name)
		self.memberList.append(member)
		return member

	def RemoveMember(self, item):
		for i in xrange(len(self.memberList)):
			if item == self.memberList[i]:
				del self.memberList[i]
				return

	def ClearMember(self):
		self.memberList = []

	def FindMember(self, key):
		list = filter(lambda argMember, argKey=key: argMember.IsSameKey(argKey), self.memberList)
		if list:
			return list[0]

		return None

	def GetLoginMemberList(self):
		return filter(MessengerMemberItem.IsOnline, self.memberList)

	def GetLogoutMemberList(self):
		return filter(lambda arg: not arg.IsOnline(), self.memberList)

		
	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def GetAllMembersList(self):
			return self.memberList
	
	def IsOpen(self):
		return self.isOpen

	def Open(self):
		self.imageGrup.LoadImage("%s/friendlist/expand.png" % apollo_interface.PATCH_SPECIAL)
		self.isOpen = TRUE

	def Close(self):
		self.imageGrup.LoadImage("%s/friendlist/minimize.png" % apollo_interface.PATCH_SPECIAL)
		self.isOpen = FALSE

		map(ui.Window.Hide, self.memberList)

	def Select(self):

		if self.IsOpen():
			self.Close()
		else:
			self.Open()


		MessengerItem.Select(self, 0)
		self.getParentEvent().OnRefreshList()

class MessengerFriendItem(MessengerMemberItem):

	def __init__(self, getParentEvent):
		MessengerMemberItem.__init__(self, getParentEvent)

	def CanRemove(self):
		return TRUE

	def OnRemove(self):
		messenger.RemoveFriend(self.key)
		net.SendMessengerRemovePacket(self.key, self.name)
		return TRUE

class MessengerTeamItem(MessengerMemberItem):

	def __init__(self, getParentEvent):
		MessengerMemberItem.__init__(self, getParentEvent)

	def CanRemove(self):
		return TRUE

	def OnRemove(self):
		messenger.RemoveFriend(self.key)
		return TRUE


		
class MessengerGuildItem(MessengerMemberItem):

	def __init__(self, getParentEvent):
		MessengerMemberItem.__init__(self, getParentEvent)

	def CanWarp(self):
		if not self.IsOnline():
			return FALSE
		return TRUE

	def OnWarp(self):
		net.SendGuildUseSkillPacket(155, self.key)

	def CanRemove(self):
		for i in xrange(guild.ENEMY_GUILD_SLOT_MAX_COUNT):
			if guild.GetEnemyGuildName(i) != "":
				return FALSE

		if guild.MainPlayerHasAuthority(guild.AUTH_REMOVE_MEMBER):
			if guild.IsMemberByName(self.name):
				return TRUE

		return FALSE

	def OnRemove(self):
		net.SendGuildRemoveMemberPacket(self.key)
		return TRUE

class MessengerFriendGroup(MessengerGroupItem):

	def __init__(self, getParentEvent):
		MessengerGroupItem.__init__(self, getParentEvent)
		self.SetName2(localeInfo.MESSENGER_FRIEND)

	def AppendMember(self, key, name):
		item = MessengerFriendItem(self.getParentEvent)
		return MessengerGroupItem.AppendMember(self, item, key, name)

class MessengerTeamGroup(MessengerGroupItem):

	def __init__(self, getParentEvent):
		MessengerGroupItem.__init__(self, getParentEvent)
		self.SetName2("Teamler")

	def AppendMember(self, key, name):
		item = MessengerFriendItem(self.getParentEvent)
		return MessengerGroupItem.AppendMember(self, item, key, name)

	
class MessengerGuildGroup(MessengerGroupItem):

	def __init__(self, getParentEvent):
		MessengerGroupItem.__init__(self, getParentEvent)
		self.SetName2(localeInfo.MESSENGER_GUILD)
		self.AddFlag("float")

	def AppendMember(self, key, name):
		item = MessengerGuildItem(self.getParentEvent)
		return MessengerGroupItem.AppendMember(self, item, key, name)

class MessengerFamilyGroup(MessengerGroupItem):

	def __init__(self, getParentEvent):
		MessengerGroupItem.__init__(self, getParentEvent)
		self.SetName(localeInfo.MESSENGER_FAMILY)
		self.AddFlag("float")

		self.lover = None

	def AppendMember(self, key, name):
		item = MessengerGuildItem(self.getParentEvent)
		self.lover = item
		return MessengerGroupItem.AppendMember(self, item, key, name)

	def GetLover(self):
		return self.lover

###################################################################################################
###################################################################################################
###################################################################################################

class MessengerWindow(ui.ScriptWindow):

	START_POSITION = 40

	class ResizeButton(ui.DragButton):

		def OnMouseOverIn(self):
			app.SetCursor(app.VSIZE)

		def OnMouseOverOut(self):
			app.SetCursor(app.NORMAL)

	def __init__(self):
		ui.ScriptWindow.__init__(self, "TOP_MOST")
		messenger.SetMessengerHandler(self)

		self.board = None
		self.groupList = []
		self.imgList = []
		self.showingItemList = []
		self.selectedItem = None
		self.whisperButtonEvent = lambda *arg: None
		self.familyGroup = None

		self.guildButtonEvent = None

		self.showingPageSize = 0
		self.startLine = 0
		self.hasMobilePhoneNumber = TRUE

		self.isLoaded = 0
		
		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.LISTBOX_ADD_POS_Y = 17.5
			self.BOARD_WIDTH = 190
			self.BOARD_HEIGHT = 130
			self.membersOnline = None
			self.membersOffline = None
			self.MEMBER_ONLINE_LIST = []
			self.MEMBER_OFFLINE_LIST = []
			self.count = 0		
			self.selected = 0
			self.searchMemberNameList = []
			self.searchMemberResult = []
			self.SEARCH_MEMBER_LIST = {}
			
			self.settingsProfileWnd = uiContact.SettingsProfileWindow()

		self.__AddGroup()
		messenger.RefreshGuildMember()


	def Show(self):
		if self.isLoaded==0:
			self.isLoaded=1

			self.__LoadWindow()
			self.OnRefreshList()
			# self.OnResizeDialog()

		ui.ScriptWindow.Show(self)

	def __LoadWindow(self):

		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "apollo_scripts/MessengerWindow.py")

		try:
			self.board = self.GetChild("board")
			self.scrollBar = self.GetChild("ScrollBar")
			self.whisperButton = self.GetChild("WhisperButton")
			self.mobileButton = self.GetChild("MobileButton")
			self.removeButton = self.GetChild("RemoveButton")
			self.addFriendButton = self.GetChild("AddFriendButton")
			self.guildButton = self.GetChild("GuildButton")
			
			if app.ENABLE_RENEW_MESSENGER_WHISPER:
				self.Messenger_Profile_Settings_Button = self.GetChild("Messenger_Profile_Settings_Button")
				self.Messenger_Profile_Contacts_Online_Value = self.GetChild("Messenger_Profile_Contacts_Online_Value")
				self.Messenger_Profile_Contacts_Offline_Value = self.GetChild("Messenger_Profile_Contacts_Offline_Value")
				self.Messenger_Profile_Board = self.GetChild("Messenger_Profile_Board")
				self.Messenger_Profile_Input_Search_Result_ListBox = self.GetChild("Messenger_Profile_Input_Search_Result_ListBox")
				self.Messenger_Profile_Input_Search_Result_Bar = self.GetChild("Messenger_Profile_Input_Search_Result_Bar")
				self.Messenger_Profile_Input_Search_Value = self.GetChild("Messenger_Profile_Input_Search_Value")
		except:
			import exception
			exception.Abort("MessengerWindow.__LoadWindow.__Bind")
			
		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			##for obj in [self.scrollBar, self.whisperButton, self.mobileButton, self.removeButton, self.addFriendButton, self.guildButton]:
			##	obj.SetParent(self.board)
				
			self.Messenger_Profile_Settings_Button.SetEvent(ui.__mem_func__(self.OnPressProfileSettings))

		self.board.SetCloseEvent(ui.__mem_func__(self.Close))
		self.scrollBar.SetScrollEvent(ui.__mem_func__(self.OnScroll))
		self.whisperButton.SetEvent(ui.__mem_func__(self.OnPressWhisperButton))
		self.mobileButton.SetEvent(ui.__mem_func__(self.OnPressMobileButton))
		self.removeButton.SetEvent(ui.__mem_func__(self.OnPressRemoveButton))
		self.addFriendButton.SetEvent(ui.__mem_func__(self.OnPressAddFriendButton))
		self.guildButton.SetEvent(ui.__mem_func__(self.OnPressGuildButton))


		self.mobileButton.Hide()
		width = self.GetWidth()
		height = self.GetHeight()
		# self.addFriendButton.SetPosition(-60, 36)
		# self.whisperButton.SetPosition(-20, 36)
		# self.removeButton.SetPosition(20, 36)
		# self.guildButton.SetPosition(60, 36)

		self.whisperButton.Disable()
		self.mobileButton.Disable()
		self.removeButton.Disable()

		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.Messenger_Profile_Input_Search_Value.SetEscapeEvent(self.Close)
			self.Messenger_Profile_Input_Search_Value.OnIMEUpdate = ui.__mem_func__(self.OnUpdateSearchSlot)
			self.Messenger_Profile_Input_Search_Result_ListBox.SetEvent(self.OnClick)
			self.SetBackgroundListBox(False)
			
			uiContact.RefreshMainProfileData()

		for list in self.groupList:
			list.SetTop()

	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def OnPressProfileSettings(self):
			if self.settingsProfileWnd.IsShow():
				self.settingsProfileWnd.Close()
			else:
				self.settingsProfileWnd.Open()
				
		def OnClick(self, key, name):
			self.Messenger_Profile_Input_Search_Value.SetText(name)
			self.Messenger_Profile_Input_Search_Value.SetFocus()

			player.OpenWhisperBySearchName(str(name))
			ime.SetCursorPosition(len(name) + 1)
			
			self.SetBackgroundListBox(False)
			self.Messenger_Profile_Input_Search_Result_ListBox.ClearItem()
			self.count = 0
			
		def GetMembersCounter(self):
			self.MEMBER_ONLINE_LIST = []
			self.MEMBER_OFFLINE_LIST = []

			for group in self.groupList:
				loginMemberList = group.GetLoginMemberList()
				logoutMemberList = group.GetLogoutMemberList()

				if loginMemberList or logoutMemberList:
					for k, member in enumerate(loginMemberList):
						if not uiContact.swapcaseDictionary(self.MEMBER_ONLINE_LIST, member.GetName()):
							continue
						self.MEMBER_ONLINE_LIST.append(member.GetName())

					for member in logoutMemberList:
						if not uiContact.swapcaseDictionary(self.MEMBER_OFFLINE_LIST, member.GetName()):
							continue
						self.MEMBER_OFFLINE_LIST.append(member.GetName())
					
			if self.Messenger_Profile_Contacts_Online_Value and self.Messenger_Profile_Contacts_Offline_Value:
				self.Messenger_Profile_Contacts_Online_Value.SetText(localeInfo.CONTACT_MEMBERS_ONLINE % (len(self.MEMBER_ONLINE_LIST)))
				self.Messenger_Profile_Contacts_Offline_Value.SetText(localeInfo.CONTACT_MEMBERS_OFFLINE % (len(self.MEMBER_OFFLINE_LIST)))
				
		def AppendMemberList(self):
			for group in self.groupList:
				memberList = group.GetAllMembersList()
				if memberList:
					for key, member in enumerate(memberList):
						if not uiContact.swapcaseDictionary(self.SEARCH_MEMBER_LIST, member.GetName()):
							continue
						self.SEARCH_MEMBER_LIST.update({key : member.GetName()})

		def SetBackgroundListBox(self, flag):
			for wnd in [self.Messenger_Profile_Input_Search_Result_ListBox, self.Messenger_Profile_Input_Search_Result_Bar]:
				if not flag:
					wnd.Hide()
					self.Messenger_Profile_Board.SetSize(self.BOARD_WIDTH, self.BOARD_HEIGHT)
				else:
					wnd.Show()
					
		def UpdateSizeListBox(self):
			iRows = self.Messenger_Profile_Input_Search_Result_ListBox.GetItemCount()
			iList = [self.Messenger_Profile_Input_Search_Result_ListBox, self.Messenger_Profile_Input_Search_Result_Bar]
			[wnd.SetSize(self.BOARD_HEIGHT, self.LISTBOX_ADD_POS_Y * iRows) for wnd in iList]
			self.Messenger_Profile_Board.SetSize(self.BOARD_WIDTH, self.BOARD_HEIGHT + (self.LISTBOX_ADD_POS_Y * iRows))

		def SetStatusListBox(self, flag):
			if not flag:
				self.SetBackgroundListBox(False)

			self.searchMemberNameList, self.searchMemberResult, self.count = [], [], 0
			self.Messenger_Profile_Input_Search_Result_ListBox.ClearItem()
					
		def OnUpdateSearchSlot(self):
			ui.EditLine.OnIMEUpdate(self.Messenger_Profile_Input_Search_Value)
			textLine = str(self.Messenger_Profile_Input_Search_Value.GetText())
			
			if len(textLine) <= 1:
				self.SetStatusListBox(False)
				return

			self.SetStatusListBox(True)

			for key, member in self.SEARCH_MEMBER_LIST.iteritems():
				if len(member) >= len(textLine) and member[:len(textLine)].lower() == textLine.lower(): self.searchMemberResult.append(key)

			for i in xrange(len(self.searchMemberResult)):
				if self.count >= 8:
					break

				self.Messenger_Profile_Input_Search_Result_ListBox.InsertItem(i, self.SEARCH_MEMBER_LIST[self.searchMemberResult[i]])
				self.searchMemberNameList.append(self.searchMemberResult[i])
				self.count += 1

			self.SetBackgroundListBox(True)
			self.UpdateSizeListBox()

			if not len(self.searchMemberNameList):
				self.SetStatusListBox(False)
				return

	def __del__(self):
		messenger.SetMessengerHandler(None)
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.membersOnline = None
			self.membersOffline = None
		self.board = None
		self.scrollBar = None
		# self.resizeButton = None
		self.friendNameBoard = None
		self.questionDialog = None
		self.popupDialog = None
		self.inputDialog = None
		self.familyGroup = None

		self.whisperButton = None
		self.mobileButton = None
		self.removeButton = None

	def OnCloseQuestionDialog(self):
		self.questionDialog.Close()
		self.questionDialog = None
		return TRUE

	def Close(self):
		self.questionDialog = None
		self.Hide()

	def SetSize(self, width, height):
		ui.ScriptWindow.SetSize(self, width, height)
		if self.board:
			self.board.SetSize(width, height)

	def __LocateMember(self):

		if self.isLoaded==0:
			return

		if (self.showingPageSize/20)-1 >= len(self.showingItemList):
			self.scrollBar.Hide()
			self.startLine = 0
		else:
			self.scrollBar.Show()


		yPos = self.START_POSITION
		heightLimit = self.GetHeight() - (self.START_POSITION + 13)-20

		map(ui.Window.Hide, self.showingItemList)


		for item in self.showingItemList[self.startLine:]:
			item.SetPosition(20 + item.GetStepWidth(), yPos)
			item.SetTop()
			item.Show()

			yPos += 25
			if yPos > heightLimit:
				break

	def __AddGroup(self):
		member = MessengerFriendGroup(ui.__mem_func__(self.GetSelf))
		member.Open()
		member.Show()
		self.groupList.append(member)

		member = MessengerGuildGroup(ui.__mem_func__(self.GetSelf))
		member.Open()
		member.Show()
		self.groupList.append(member)
		
		member = MessengerTeamGroup(ui.__mem_func__(self.GetSelf))
		member.Open()
		member.Show()
		self.TeamGroup = member
		self.groupList.append(member) 
		
	def __AddFamilyGroup(self):
		member = MessengerFamilyGroup(ui.__mem_func__(self.GetSelf))
		member.Open()
		member.Show()

		self.familyGroup = member

	def ClearGuildMember(self):
		self.groupList[GUILD].ClearMember()

	def SetWhisperButtonEvent(self, event):
		self.whisperButtonEvent=event

	def SetGuildButtonEvent(self, event):
		self.guildButtonEvent=event

	def SendMobileMessage(self, name):
		if not uiGameOption.MOBILE:
			return

		if not self.hasMobilePhoneNumber:
			questionDialog = uiCommon.QuestionDialog2()
			questionDialog.SetText1(localeInfo.MESSENGER_INPUT_MOBILE_PHONE_NUMBER_1)
			questionDialog.SetText2(localeInfo.MESSENGER_INPUT_MOBILE_PHONE_NUMBER_2)
			questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnAcceptInputMobilePhoneNumber))
			questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCancelInputMobilePhoneNumber))
			questionDialog.SetWidth(400)
			questionDialog.Open()
			self.questionDialog = questionDialog
			return

		## Input Sending Mobile Message
		inputDialog = uiCommon.InputDialog()
		inputDialog.SetTitle(localeInfo.MESSENGER_SEND_MOBILE_MESSAGE_TITLE)
		inputDialog.SetMaxLength(50)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OnInputMobileMessage))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseInputDialog))
		inputDialog.name = name
		inputDialog.Open()
		self.inputDialog = inputDialog

	def OnAcceptInputMobilePhoneNumber(self):
		if not uiGameOption.MOBILE:
			return

		## Input Mobile Phone Number
		inputDialog = uiCommon.InputDialog()
		inputDialog.SetTitle(localeInfo.MESSENGER_INPUT_MOBILE_PHONE_NUMBER_TITLE)
		inputDialog.SetMaxLength(13)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OnInputMobilePhoneNumber))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseInputDialog))
		inputDialog.Open()
		self.inputDialog = inputDialog
		self.OnCancelInputMobilePhoneNumber()

	def OnCancelInputMobilePhoneNumber(self):
		if not uiGameOption.MOBILE:
			return
		self.questionDialog.Close()
		self.questionDialog = None
		return TRUE

	def OnInputMobilePhoneNumber(self):
		if not uiGameOption.MOBILE:
			return

		text = self.inputDialog.GetText()

		if not text:
			return

		text.replace('-', '')
		net.SendChatPacket("/mobile " + text)
		self.OnCloseInputDialog()
		return TRUE

	def OnInputMobileMessage(self):
		if not uiGameOption.MOBILE:
			return

		text = self.inputDialog.GetText()

		if not text:
			return

		net.SendMobileMessagePacket(self.inputDialog.name, text)
		self.OnCloseInputDialog()
		return TRUE

	def OnCloseInputDialog(self):
		self.inputDialog.Close()
		self.inputDialog = None
		return TRUE

	def OnPressGuildButton(self):
		self.guildButtonEvent()

	def OnPressAddFriendButton(self):
		friendNameBoard = uiCommon.InputDialog()
		friendNameBoard.SetTitle(localeInfo.MESSENGER_ADD_FRIEND)
		friendNameBoard.SetAcceptEvent(ui.__mem_func__(self.OnAddFriend))
		friendNameBoard.SetCancelEvent(ui.__mem_func__(self.OnCancelAddFriend))
		friendNameBoard.SetMaxLength(32)
		friendNameBoard.Open()
		self.friendNameBoard = friendNameBoard

	def OnAddFriend(self):
		text = self.friendNameBoard.GetText()
		if text:
			net.SendMessengerAddByNamePacket(text)
		self.friendNameBoard.Close()
		self.friendNameBoard = None
		return TRUE

	def OnCancelAddFriend(self):
		self.friendNameBoard.Close()
		self.friendNameBoard = None
		return TRUE

	def OnPressWhisperButton(self):
		if self.selectedItem:
			self.selectedItem.OnWhisper()

	def OnPressMobileButton(self):
		if self.selectedItem:
			self.selectedItem.OnMobileMessage()

	def OnPressRemoveButton(self):
		if self.selectedItem:
			if self.selectedItem.CanRemove():
				self.questionDialog = uiCommon.QuestionDialog()
				self.questionDialog.SetText(localeInfo.MESSENGER_DO_YOU_DELETE)
				self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnRemove))
				self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
				self.questionDialog.Open()

	def OnRemove(self):
		if self.selectedItem:
			if self.selectedItem.CanRemove():
				map(lambda arg, argDeletingItem=self.selectedItem: arg.RemoveMember(argDeletingItem), self.groupList)
				self.selectedItem.OnRemove()
				self.selectedItem.UnSelect()
				self.selectedItem = None
				self.OnRefreshList()

		self.OnCloseQuestionDialog()

	def OnScroll(self):
		scrollLineCount = len(self.showingItemList) - (self.showingPageSize/20)
		startLine = int(scrollLineCount * self.scrollBar.GetPos())

		if startLine != self.startLine:
			self.startLine = startLine
			self.__LocateMember()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	## CallBack
	def OnSelectItem(self, item):

		if self.selectedItem:
			if item != self.selectedItem:
				self.selectedItem.UnSelect()

		self.selectedItem = item

		if self.selectedItem:
			self.selectedItem.Select()

			if self.selectedItem.CanWhisper():
				self.whisperButton.Enable()
			else:
				self.whisperButton.Disable()

			if self.selectedItem.IsMobile():
				self.mobileButton.Enable()
			else:
				self.mobileButton.Disable()

			if self.selectedItem.CanRemove():
				self.removeButton.Enable()
			else:
				self.removeButton.Disable()

	def OnDoubleClickItem(self, item):

		if not self.selectedItem:
			return

		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.OnPressWhisperButton()
			if self.selectedItem.IsMobile():
				self.OnPressMobileButton()
		else:
			if self.selectedItem.IsOnline():
				self.OnPressWhisperButton()

			elif self.selectedItem.IsMobile():
				self.OnPressMobileButton()

	def GetSelf(self):
		return self

	def OnRefreshList(self):
		self.showingItemList = []

		if self.familyGroup:
			self.showingItemList.append(self.familyGroup)
			if self.familyGroup.GetLover():
				self.showingItemList.append(self.familyGroup.GetLover())

		for group in self.groupList:

			self.showingItemList.append(group)

			if group.IsOpen():

				loginMemberList = group.GetLoginMemberList()
				logoutMemberList = group.GetLogoutMemberList()

				if loginMemberList or logoutMemberList:
					for member in loginMemberList:
						self.showingItemList.append(member)
					for member in logoutMemberList:
						self.showingItemList.append(member)

				else:
					item = MessengerItem(ui.__mem_func__(self.GetSelf))
					item.SetName(localeInfo.MESSENGER_EMPTY_LIST)
					self.showingItemList.append(item)

		self.__LocateMember()
		if app.ENABLE_RENEW_MESSENGER_WHISPER:
			self.AppendMemberList()

	def RefreshMessenger(self):
		self.OnRefreshList()

	## EventHandler
	def __AddList(self, groupIndex, key, name):
		group = self.groupList[groupIndex]
		member = group.FindMember(key)
		if not member:
			member = group.AppendMember(key, name)
			self.OnSelectItem(None)
		return member

	def OnRemoveList(self, groupIndex, key):
		group = self.groupList[groupIndex]
		group.RemoveMember(group.FindMember(key))
		self.OnRefreshList()

	def OnRemoveAllList(self, groupIndex):
		group = self.groupList[groupIndex]
		group.ClearMember()
		self.OnRefreshList()

	def OnLogin(self, groupIndex, key, name=None):
		if not name:
			name = key
		group = self.groupList[groupIndex]
		member = self.__AddList(groupIndex, key, name)
		member.SetName(name)
		member.Online()
		self.OnRefreshList()
		
	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def OnUpdate(self):
			self.GetMembersCounter()

	def OnLogout(self, groupIndex, key, name=None):
		group = self.groupList[groupIndex]
		member = self.__AddList(groupIndex, key, name)
		if not name:
			name = key
		member.SetName(name)
		member.Offline()
		self.OnRefreshList()

	def OnMobile(self, groupIndex, key, mobileFlag):
		group = self.groupList[groupIndex]
		member = group.FindMember(key)
		if not member:
			return
		member.SetMobile(mobileFlag)
		self.OnRefreshList()

	def OnAddLover(self, name, lovePoint):
		if not self.familyGroup:
			self.__AddFamilyGroup()

		member = self.familyGroup.AppendMember(0, name)

		member.SetName(name)
		member.SetLovePoint(lovePoint)
		member.Offline()
		self.OnRefreshList()

	def OnUpdateLovePoint(self, lovePoint):
		if not self.familyGroup:
			return

		lover = self.familyGroup.GetLover()
		if not lover:
			return

		lover.SetLovePoint(lovePoint)

	def OnLoginLover(self):
		if not self.familyGroup:
			return

		lover = self.familyGroup.GetLover()
		if not lover:
			return

		lover.Online()

	def OnLogoutLover(self):
		if not self.familyGroup:
			return

		lover = self.familyGroup.GetLover()
		if not lover:
			return

		lover.Offline()

	def ClearLoverInfo(self):
		if not self.familyGroup:
			return

		self.familyGroup.ClearMember()
		self.familyGroup = None
		self.OnRefreshList()

