import ui
import grp
import player
import uiToolTip
import net
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import uiScriptLocale
import constInfo
import mouseModule
import chr
import chat
import playerSettingModule
import app
import dbg
import os
import apollo_interface
ROOT_PATH = apollo_interface.PATCH_SPECIAL + "/party/"

class PartyMemberInfoBoard(ui.ScriptWindow):

	MEMBER_BUTTON_NORMAL = 10
	MEMBER_BUTTON_WARP = 11
	MEMBER_BUTTON_KICK = 12

	MEMBER_OPTION_FILENAME = {	player.PARTY_STATE_LEADER : "btn_admin_%02d_%s.png",
								player.PARTY_STATE_ATTACKER : "btn_attacker_%02d_%s.png",
								player.PARTY_STATE_BERSERKER : "btn_berserk_%02d_%s.png",
								player.PARTY_STATE_TANKER : "btn_blocker_%02d_%s.png",
								player.PARTY_STATE_DEFENDER : "btn_defender_%02d_%s.png",
								player.PARTY_STATE_BUFFER : "btn_fighter_%02d_%s.png",
								player.PARTY_STATE_SKILL_MASTER : "btn_magican_%02d_%s.png",
								MEMBER_BUTTON_NORMAL : "btn_member_%02d_%s.png",
								MEMBER_BUTTON_KICK : "btn_kick_%02d_%s.png", }

	OPTION_NAME_DICT =	{	player.PARTY_STATE_ATTACKER : localeInfo.PARTY_SET_ATTACKER,
							player.PARTY_STATE_BERSERKER : localeInfo.PARTY_SET_BERSERKER,
							player.PARTY_STATE_TANKER : localeInfo.PARTY_SET_TANKER,
							player.PARTY_STATE_DEFENDER : localeInfo.PARTY_SET_DEFENDER,
							player.PARTY_STATE_BUFFER : localeInfo.PARTY_SET_BUFFER,
							player.PARTY_STATE_SKILL_MASTER : localeInfo.PARTY_SET_SKILL_MASTER, }

	PARTY_AFFECT_EXPERIENCE			= 0
	PARTY_AFFECT_ATTACKER			= 1
	PARTY_AFFECT_TANKER				= 2
	PARTY_AFFECT_BUFFER				= 3
	PARTY_AFFECT_SKILL_MASTER		= 4
	PARTY_AFFECT_BERSERKER			= 5
	PARTY_AFFECT_DEFENDER			= 6
	PARTY_AFFECT_MAX_NUM			= 7
	AFFECT_STRING_DICT = {			PARTY_AFFECT_EXPERIENCE : localeInfo.PARTY_BONUS_EXP,
									PARTY_AFFECT_ATTACKER : localeInfo.PARTY_BONUS_ATTACKER,
									PARTY_AFFECT_TANKER : localeInfo.PARTY_BONUS_TANKER,
									PARTY_AFFECT_BUFFER : localeInfo.PARTY_BONUS_BUFFER,
									PARTY_AFFECT_SKILL_MASTER : localeInfo.PARTY_BONUS_SKILL_MASTER,
									PARTY_AFFECT_BERSERKER : localeInfo.PARTY_BONUS_BERSERKER,
									PARTY_AFFECT_DEFENDER : localeInfo.PARTY_BONUS_DEFENDER,
								}

	ONLINE_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	OFFLINE_COLOR = grp.GenerateColor(0.5, 0.5, 0.5, 1.0)

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.selectedOption = -1
		self.optionButtons = {}
		self.optionButtonField = None

		self.affectValueDict = {}
		self.partyAffectImageList = []
		
		self.optionToolTip = uiToolTip.ToolTip()
		self.optionToolTip.HideToolTip()
		
		self.__CreateAffectToolTip()
		
		self.pid = 0
		self.vid = 0
		self.isShowOptionButton = False

		self.__LoadBoard()
		self.Show()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadBoard(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "apollo_scripts/new_partyscript.py")
		except:
			import exception
			exception.Abort("PartyMemberInfoBoard.__LoadBoard.LoadScript")

		try:
			self.main = {
				"optionBtn" : self.GetChild("option_button"),
				"optionTooltipImg" : self.GetChild("bonus_info_icon"),
				"faceImg" : self.GetChild("face_image"),
				"hpBar" : self.GetChild("hp_gauge"),
				"empty_face" : self.GetChild("Empty_Face"),
			}

			self.partyAffectImageList.append(self.GetChild("ExperienceImage"))
			self.partyAffectImageList.append(self.GetChild("AttackerImage"))
			self.partyAffectImageList.append(self.GetChild("DefenderImage"))
			self.partyAffectImageList.append(self.GetChild("BufferImage"))
			self.partyAffectImageList.append(self.GetChild("SkillMasterImage"))
			self.partyAffectImageList.append(self.GetChild("TimeBonusImage"))
			self.partyAffectImageList.append(self.GetChild("RegenBonus"))
			
			self.main["faceImg"].Hide()
		except:
			import exception
			exception.Abort("PartyMemberInfoBoard.__LoadBoard.BindObject")

		self.main["optionBtn"].SAFE_SetEvent(self.OnClickOptionButton)
		self.__SetAffectsMouseEvent()
		self.__HideAllAffects()

		try:
			# name window
			wndName = ui.Window()
			wndName.SetMouseLeftButtonDownEvent(ui.__mem_func__(self.OnMouseLeftButtonDown))
			wndName.SetSize(0, 23)
			wndName.SetParent(self)
			wndName.localX = 55
			wndName.localY = -7
			wndName.Show()
			self.wndName = wndName

			nameLeft = ui.ImageBox()
			nameLeft.AddFlag("not_pick")
			nameLeft.SetParent(wndName)
			nameLeft.LoadImage(ROOT_PATH + "member_label_name_left.png")
			nameLeft.Show()
			wndName.left = nameLeft

			nameCenter = ui.ExpandedImageBox()
			nameCenter.AddFlag("not_pick")
			nameCenter.SetParent(wndName)
			nameCenter.SetPosition(nameLeft.GetRight(), 0)
			nameCenter.LoadImage(ROOT_PATH + "member_label_name_center.png")
			nameCenter.Show()
			wndName.center = nameCenter

			nameRight = ui.ImageBox()
			nameRight.AddFlag("not_pick")
			nameRight.SetParent(wndName)
			nameRight.LoadImage(ROOT_PATH + "member_label_name_right.png")
			nameRight.SetPosition(nameRight.GetWidth(), 0)
			nameRight.SetWindowHorizontalAlignRight()
			nameRight.Show()
			wndName.right = nameRight

			nameText = ui.TextLine()
			nameText.SetParent(wndName)
			nameText.SetWindowHorizontalAlignCenter()
			nameText.SetHorizontalAlignCenter()
			nameText.SetWindowVerticalAlignCenter()
			nameText.SetVerticalAlignCenter()
			nameText.SetPosition(3, -1)
			nameText.Show()
			wndName.text = nameText
		except:
			import exception
			exception.Abort("PartyMemberInfoBoard.__LoadBoard.BuildObject")

		self.SetTop()

		self.__BuildOptionButtons()
	
	
	def __SetAffectsMouseEvent(self):
		for i in xrange(len(self.partyAffectImageList)):
			self.partyAffectImageList[i].OnMouseOverIn = lambda selfArg = self, index = i: selfArg.OnAffectOverIn(index)
		for i in xrange(len(self.partyAffectImageList)):
			self.partyAffectImageList[i].OnMouseOverOut = lambda selfArg = self, index = i: selfArg.OnAffectOverOut(index)

	def __HideAllAffects(self):
		for img in self.partyAffectImageList:
			img.Hide()
	
	def __CreateAffectToolTip(self):
		affectToolTip = uiToolTip.ToolTip(220)
		affectToolTip.Hide()
		self.affectToolTip = affectToolTip
	
	def OnAffectOverIn(self, index):

		if not self.AFFECT_STRING_DICT.has_key(index):
			return
		if not self.affectValueDict.has_key(index):
			return

		(x, y) = self.GetGlobalPosition()

		self.affectToolTip.ClearToolTip()
		self.affectToolTip.SetTitle(self.AFFECT_STRING_DICT[index](self.affectValueDict[index]))
		self.affectToolTip.SetToolTipPosition(x + index*12, y + 11)
		self.affectToolTip.ShowToolTip()

	def OnAffectOverOut(self, index):
		self.affectToolTip.HideToolTip()

	def SetPlayerID(self, pid):
		self.pid = pid

	def GetPlayerID(self):
		return self.pid

	def GetPlayerVID(self):
		return self.vid
	
	def SetCharacterPID(self, pid):
		self.pid = pid

	def SetCharacterVID(self, vid):
		self.vid = vid

	def GetCharacterPID(self):
		return self.pid

	def GetCharacterVID(self):
		return self.vid

	def __BuildOptionButtons(self):
		optionField = ui.Window()
		optionField.AddFlag("float")
		optionField.Hide()
		self.optionButtonField = optionField

		buttonIndexToName = ["normal", "hover", "active"]			

		for key, name in self.MEMBER_OPTION_FILENAME.items():
			if key == player.PARTY_STATE_LEADER:
				continue

			button = ui.Button()
			button.SetParent(optionField)
			button.AddFlag("float")
			button.SetUpVisual(ROOT_PATH + name % (1, buttonIndexToName[0]))
			button.SetOverVisual(ROOT_PATH + name % (2, buttonIndexToName[1]))
			button.SetDownVisual(ROOT_PATH + name % (3, buttonIndexToName[2]))
			button.Hide()
			self.optionButtons[key] = button

		for option, name in self.OPTION_NAME_DICT.items():
			button = self.optionButtons[option]
			button.SetToolTipText(name)
			button.SetEvent(ui.__mem_func__(self.OnSelectOption), option)

		self.optionButtons[self.MEMBER_BUTTON_NORMAL].SetEvent(ui.__mem_func__(self.OnSelectOption), -1)
		self.optionButtons[self.MEMBER_BUTTON_NORMAL].SetToolTipText(localeInfo.PARTY_SET_NORMAL)
		self.optionButtons[self.MEMBER_BUTTON_KICK].SetToolTipText(localeInfo.TARGET_BUTTON_EXCLUDE)
		self.optionButtons[self.MEMBER_BUTTON_KICK].SetEvent(ui.__mem_func__(self.OnKick))

	def __GetPartySkillLevel(self):
		slotIndex = player.GetSkillSlotIndex(player.SKILL_INDEX_TONGSOL)
		skillGrade = player.GetSkillGrade(slotIndex)
		skillLevel = player.GetSkillLevel(slotIndex)
		return skillLevel + skillGrade*20

	def __AppendOptionButton(self, x, y, option):
		if option == self.selectedOption:
			button = self.optionButtons[self.MEMBER_BUTTON_NORMAL]
		else:
			button = self.optionButtons[option]

		button.SetPosition(x, y)
		button.Show()

	def __ShowOptionButton(self):
		xPos_board = 142
		self.isShowOptionButton = TRUE

		(x, y) = self.main["optionBtn"].GetGlobalPosition()
		xPos = x + self.main["optionBtn"].GetWidth()

		self.optionButtonField.SetPosition(xPos_board, y - 2)
		
		xPos = 2
		y = 2

		skillLevel = self.__GetPartySkillLevel()

		## Tanker
		if skillLevel >= 10:
			self.__AppendOptionButton(xPos, y, player.PARTY_STATE_ATTACKER)
			xPos += 22

		## Attacker
		if skillLevel >= 20:
			self.__AppendOptionButton(xPos, y, player.PARTY_STATE_BERSERKER)
			xPos += 22

		## Tanker
		if skillLevel >= 20:
			self.__AppendOptionButton(xPos, y, player.PARTY_STATE_TANKER)
			xPos += 22

		## Buffer
		if skillLevel >= 25:
			self.__AppendOptionButton(xPos, y, player.PARTY_STATE_BUFFER)
			xPos += 22

		## Skill Master
		if skillLevel >= 35:
			self.__AppendOptionButton(xPos, y, player.PARTY_STATE_SKILL_MASTER)
			xPos += 22

		## Defender
		if skillLevel >= 40:
			self.__AppendOptionButton(xPos, y, player.PARTY_STATE_DEFENDER)
			xPos += 22

		## Kick
		if self.optionButtons.has_key(self.MEMBER_BUTTON_KICK):
			button = self.optionButtons[self.MEMBER_BUTTON_KICK]
			button.SetPosition(xPos, y)
			button.Show()
			xPos += 22

		self.optionButtonField.SetSize(xPos - 2, 44 + 2 * 2)
		self.optionButtonField.Show()

	def __HideOptionButton(self):
		self.isShowOptionButton = FALSE
		for button in self.optionButtons.values():
			button.Hide()
		self.optionButtonField.Hide()

	def SetCurrentOption(self, option):

		if self.selectedOption == option:
			return

		self.selectedOption = option
		self.main["optionBtn"].Show()

		name = self.MEMBER_OPTION_FILENAME[self.MEMBER_BUTTON_NORMAL]
		if self.MEMBER_OPTION_FILENAME.has_key(option):
			name = self.MEMBER_OPTION_FILENAME[option]

		buttonIndexToName = ["normal", "hover", "active"]	
		self.main["optionBtn"].SetUpVisual(ROOT_PATH + name % (1, buttonIndexToName[0]))
		self.main["optionBtn"].SetOverVisual(ROOT_PATH + name % (2, buttonIndexToName[1]))
		self.main["optionBtn"].SetDownVisual(ROOT_PATH + name % (3, buttonIndexToName[2]))

	def OnClickOptionButton(self):

		if player.IsPartyLeader(player.GetMainCharacterIndex()):
			if player.PARTY_STATE_LEADER != self.selectedOption:

				if self.isShowOptionButton:
					self.__HideOptionButton()
				else:
					self.__ShowOptionButton()

	def OnSelectOption(self, option):
		self.__HideOptionButton()

		if option <= 0:
			net.SendPartySetStatePacket(self.pid, self.selectedOption, FALSE)

		else:

			if self.selectedOption <= 0:
				net.SendPartySetStatePacket(self.pid, option, TRUE)

			else:
				net.SendPartySetStatePacket(self.pid, self.selectedOption, FALSE)
				net.SendPartySetStatePacket(self.pid, option, TRUE)

	def OnKick(self):
		self.__HideOptionButton()

		if not self.pid:
			return
		net.SendPartyRemovePacket(self.pid)	

	def SetName(self, name):
		wnd = self.wndName

		wnd.text.SetText(name)

		centerWidth = wnd.text.GetTextWidth() + 6
		newWidth = wnd.left.GetWidth() + wnd.right.GetWidth() + centerWidth
		wnd.SetSize(newWidth, wnd.GetHeight())

		wnd.center.SetRenderingRect(0.0, 0.0, float(centerWidth) - 1.0, 0.0)

	def SetCharacterHP(self, hpPercentage):
		hpPercentage = max(0, hpPercentage)
		self.main["hpBar"].SetPercentage(hpPercentage, 100)
	
	def SetRace(self, race):
		if race == 999:
			self.main["faceImg"].Hide()
			self.main["empty_face"].Show()
		else: 
			self.main["faceImg"].LoadImage(apollo_interface.FACE_IMAGE_DICT_MEDIUM[race])
			self.main["faceImg"].Show()
	
	def SetAffect(self, affectSlotIndex, affectValue):

		if affectSlotIndex >= len(self.partyAffectImageList):
			return

		if affectValue > 0:
			self.partyAffectImageList[affectSlotIndex].Show()
		else:
			self.partyAffectImageList[affectSlotIndex].Hide()

		self.affectValueDict[affectSlotIndex] = affectValue
	
	def SetOnline(self, vid):
		self.wndName.text.SetPackedFontColor(0xfff8d090)
		self.vid = vid
		self.main["hpBar"].Show()
		self.main["faceImg"].Show()

	def SetOffline(self):
		self.wndName.text.SetPackedFontColor(0xffa08784)
		self.vid = 0
		self.main["hpBar"].Hide()
		self.main["faceImg"].Hide()
		self.main["empty_face"].Show()
	
	def OnUpdate(self):
		x, y = self.GetGlobalPosition()

		self.wndName.SetPosition(x + self.wndName.localX,self.wndName.localY)

	def Destroy(self):
		self.optionToolTip.HideToolTip()
		self.ClearDictionary()
		self.Hide()

	def OnMouseLeftButtonDown(self):
		if self.GetPlayerVID():
			player.SetTarget(self.GetPlayerVID())
			player.OpenCharacterMenu(self.GetPlayerVID())

	def OnTop(self):
		if self.optionButtonField:
			self.optionButtonField.SetTop()

class PartyWindow(ui.Window):

	def __init__(self):
		ui.Window.__init__(self)

		self.distributionMode = 0
		self.isLeader = FALSE
		self.memberList = []
		self.mainMembersInfo = []

		self.__BuildWindow()

		self.SetPosition(0, 52)

	def __del__(self):
		ui.Window.__del__(self)

	def __BuildWindow(self):
		topImage = ui.ImageBox()
		topImage.SetParent(self)
		topImage.LoadImage(ROOT_PATH + "party_menu_bg.png")
		topImage.Show()
		self.topImage = topImage

		leaveButton = ui.Button()
		leaveButton.SetParent(topImage)
		leaveButton.SetPosition(5, 0)
		leaveButton.SetUpVisual(ROOT_PATH + "party_btn_leave_01_normal.png")
		leaveButton.SetOverVisual(ROOT_PATH + "party_btn_leave_02_hover.png")
		leaveButton.SetDownVisual(ROOT_PATH + "party_btn_leave_03_active.png")
		leaveButton.SetWindowVerticalAlignCenter()
		leaveButton.SetEvent(net.SendPartyExitPacket)
		leaveButton.Show()
		self.leaveButton = leaveButton

		partyExpEqualBorder = ui.ImageBox()
		partyExpEqualBorder.SetParent(topImage)
		partyExpEqualBorder.LoadImage(ROOT_PATH + "party_exp_radio_active.png")
		partyExpEqualBorder.SetPosition(leaveButton.GetRight() + 5, 0)
		partyExpEqualBorder.SetWindowVerticalAlignCenter()
		partyExpEqualBorder.Show()
		partyExpEqual = ui.RadioButton()
		partyExpEqual.SetParent(topImage)
		partyExpEqual.SetUpVisual(ROOT_PATH + "party_exp_radio_btn_equal_01_normal.png")
		partyExpEqual.SetOverVisual(ROOT_PATH + "party_exp_radio_btn_equal_02_hover.png")
		partyExpEqual.SetDownVisual(ROOT_PATH + "party_exp_radio_btn_equal_03_active.png")
		partyExpEqual.SetPosition(partyExpEqualBorder.GetLeft() + (partyExpEqualBorder.GetWidth() - partyExpEqual.GetWidth()) / 2, (topImage.GetHeight() - partyExpEqual.GetHeight()) / 2)
		partyExpEqual.SAFE_SetEvent(self.__OnSelectPartyButton, partyExpEqual, player.PARTY_EXP_DISTRIBUTION_PARITY)
		partyExpEqual.SetToolTipText(localeInfo.PARTY_EXP_DISTRIBUTION_MODE_PARITY)
		partyExpEqual.Show()
		partyExpEqual.border = partyExpEqualBorder
		self.partyExpEqual = partyExpEqual

		partyExpLevelBorder = ui.ImageBox()
		partyExpLevelBorder.SetParent(topImage)
		partyExpLevelBorder.LoadImage(ROOT_PATH + "party_exp_radio_active.png")
		partyExpLevelBorder.SetPosition(partyExpEqualBorder.GetRight(), 0)
		partyExpLevelBorder.SetWindowVerticalAlignCenter()
		partyExpLevelBorder.Show()
		partyExpLevel = ui.RadioButton()
		partyExpLevel.SetParent(topImage)
		partyExpLevel.SetUpVisual(ROOT_PATH + "party_exp_radio_btn_level_01_normal.png")
		partyExpLevel.SetOverVisual(ROOT_PATH + "party_exp_radio_btn_level_02_hover.png")
		partyExpLevel.SetDownVisual(ROOT_PATH + "party_exp_radio_btn_level_03_active.png")
		partyExpLevel.SetPosition(partyExpLevelBorder.GetLeft() + (partyExpLevelBorder.GetWidth() - partyExpLevel.GetWidth()) / 2, (topImage.GetHeight() - partyExpLevel.GetHeight()) / 2)
		partyExpLevel.SAFE_SetEvent(self.__OnSelectPartyButton, partyExpLevel, player.PARTY_EXP_NON_DISTRIBUTION)
		partyExpLevel.SetToolTipText(localeInfo.PARTY_EXP_DISTRIBUTION_MODE_LEVEL_TOOLTIP)
		partyExpLevel.Show()
		partyExpLevel.border = partyExpLevelBorder
		self.partyExpLevel = partyExpLevel

		partyMemberBG = ui.ExpandedImageBox()
		partyMemberBG.SetParent(self)
		partyMemberBG.SetPosition(0, topImage.GetBottom())
		partyMemberBG.LoadImage(ROOT_PATH + "party_bg.png")
		partyMemberBG.Show()
		self.partyMemberBG = partyMemberBG

		self.SetSize(topImage.GetWidth(), topImage.GetHeight())
		if self.distributionMode == player.PARTY_EXP_DISTRIBUTION_PARITY:
			self.__OnSelectPartyButton(partyExpEqual, self.distributionMode)
		else:
			self.__OnSelectPartyButton(partyExpLevel, self.distributionMode)

	def __OnSelectPartyButton(self, wndDown, distributionMode):
		self.partyExpEqual.SetUp()
		self.partyExpEqual.border.Hide()
		self.partyExpLevel.SetUp()
		self.partyExpLevel.border.Hide()

		wndDown.Down()
		wndDown.border.Show()

		if self.distributionMode != distributionMode:
			net.SendPartyParameterPacket(distributionMode)

	def OnSetPartyEXPType(self, distributionMode):
		self.distributionMode = distributionMode

		if player.PARTY_EXP_DISTRIBUTION_PARITY == distributionMode:
			self.__OnSelectPartyButton(self.partyExpEqual, distributionMode)
		else:
			self.__OnSelectPartyButton(self.partyExpLevel, distributionMode)

	def __ClearMemberList(self):
		self.memberList = {}

	def __GetMemberByPID(self, pid):
		for board in self.memberList:
			if board.GetPlayerID() == int(pid):
				return board

		return None

	def AddMember(self, pid, name):
		board = self.__GetMemberByPID(pid)

		if not board:
			board = PartyMemberInfoBoard()
			board.SetParent(self.partyMemberBG)
			board.SetPlayerID(int(pid))
			board.Show()

			self.memberList.append(board)
			self.__ArrangeMemberList()

		if not name:
			name = localeInfo.PARTY_MEMBER_OFFLINE

		# board.SetRace(race)
		board.SetName(name)
		board.SetOffline()

		self.Show()

	def RemoveMember(self, pid):
		board = self.__GetMemberByPID(pid)
		if None == board:
			return

		vid = board.GetPlayerVID()
		if 0 != vid and player.IsMainCharacterIndex(vid):
			self.ExitParty()
			player.ExitParty()

		else:
			board.Destroy()
			player.RemovePartyMember(pid)
			self.memberList.remove(board)
			self.__ArrangeMemberList()
	
	
	
	def UpdateMemberInfo(self, pid):
		board = self.__GetMemberByPID(pid)
		if None == board:
			return
		
		option = player.GetPartyMemberState(pid)
		hpPercentage = player.GetPartyMemberHPPercentage(pid)
		affectsList = player.GetPartyMemberAffects(pid)

		board.SetCurrentOption(option)
		board.SetCharacterHP(hpPercentage)

		for i in xrange(len(affectsList)):
			board.SetAffect(i, affectsList[i])
			
		vid_r = board.GetCharacterVID()
		myVid = player.GetMainCharacterIndex()
		if vid_r != None:
			chr.SelectInstance(int(vid_r))
			race = chr.GetRace()
			board.SetRace(race)
		else:
			race = 999
			board.SetRace(race)
			
		chr.SelectInstance(int(myVid))

		vid = board.GetPlayerVID()
		if 0 != vid:
			if player.IsMainCharacterIndex(vid):
				if player.PARTY_STATE_LEADER == player.GetPartyMemberState(pid):
					self.ShowLeaderButton()
				else:
					self.ShowMemberButton()

	def ShowLeaderButton(self): 
		self.isLeader = TRUE
		self.leaveButton.SetToolTipText(localeInfo.PARTY_BREAK_UP)
		self.partyExpEqual.Enable()
		self.partyExpLevel.Enable()

	def ShowMemberButton(self):
		self.isLeader = FALSE
		self.leaveButton.SetToolTipText(localeInfo.PARTY_LEAVE)
		self.partyExpEqual.Disable()
		self.partyExpLevel.Disable()

	def SetMemberOnline(self, pid, vid):
		board = self.__GetMemberByPID(pid)
		if not board:
			return
		
		board.SetOnline(vid)

	def SetMemberOffline(self, pid):
		board = self.__GetMemberByPID(pid)
		if not board:
			return

		board.SetOffline()

	def SetAllMemberOffline(self):
		for board in self.memberList:
			board.SetOffline()

	def ExitParty(self):
		self.isLeader = FALSE
		self.memberList = []
		self.Hide()

	def __ArrangeMemberList(self):
		count = 0
		newHeight = 0
		maxWidth = self.topImage.GetWidth()

		for board in self.memberList:
			board.SetPosition(3, 3 + count * (board.GetHeight() + 6))
			count += 1
			newHeight += board.GetHeight() + 6
			maxWidth = max(maxWidth, min(board.GetWidth(), self.partyMemberBG.GetWidth() - 3))

		self.partyMemberBG.SetRenderingRect(0.0, 0.0, 0.0, newHeight)
		self.partyMemberBG.SetSize(self.partyMemberBG.GetWidth(), newHeight)
		self.SetSize(maxWidth, newHeight + self.topImage.GetHeight())
