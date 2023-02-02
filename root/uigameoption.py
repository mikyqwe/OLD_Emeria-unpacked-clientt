import ui
import snd
import systemSetting
import net
import chat
import app
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import constInfo
import chrmgr
import player
import uiPrivateShopBuilder # ±èÁØÈ£
import interfaceModule # ±èÁØÈ£
import uiScriptLocale
if app.ENABLE_MELEY_LAIR_DUNGEON:
	import background

blockMode = 0
viewChatMode = 0

MOBILE = FALSE

if localeInfo.IsYMIR():
	MOBILE = TRUE


class OptionDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
		self.__Load()
		self.RefreshViewChat()
		self.RefreshAlwaysShowName()
		self.RefreshShowDamage()
		self.RefreshShowSalesText()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print " -------------------------------------- DELETE GAME OPTION DIALOG"

	def __Initialize(self):
		self.titleBar = 0
		self.nameColorModeButtonList = []
		self.viewTargetBoardButtonList = []
		self.pvpModeButtonDict = {}
		self.blockButtonList = []
		self.viewChatButtonList = []
		self.alwaysShowNameButtonList = []
		self.showDamageButtonList = []
		self.showsalesTextButtonList = []
		if app.__BL_HIDE_EFFECT__:
			self.BLEffectGroupList = []
		self.renderTarget = []
		

	def Destroy(self):
		self.ClearDictionary()

		self.__Initialize()
		print " -------------------------------------- DESTROY GAME OPTION DIALOG"
	
	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("OptionDialog.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			GetObject = self.GetChild
			self.titleBar = GetObject("titlebar")
			self.nameColorModeButtonList.append(GetObject("name_color_normal"))
			self.nameColorModeButtonList.append(GetObject("name_color_empire"))
			self.viewTargetBoardButtonList.append(GetObject("target_board_no_view"))
			self.viewTargetBoardButtonList.append(GetObject("target_board_view"))
			self.pvpModeButtonDict[player.PK_MODE_PEACE] = GetObject("pvp_peace")
			self.pvpModeButtonDict[player.PK_MODE_REVENGE] = GetObject("pvp_revenge")
			self.pvpModeButtonDict[player.PK_MODE_GUILD] = GetObject("pvp_guild")
			self.pvpModeButtonDict[player.PK_MODE_FREE] = GetObject("pvp_free")
			self.blockButtonList.append(GetObject("block_exchange_button"))
			self.blockButtonList.append(GetObject("block_party_button"))
			self.blockButtonList.append(GetObject("block_guild_button"))
			self.blockButtonList.append(GetObject("block_whisper_button"))
			self.blockButtonList.append(GetObject("block_friend_button"))
			self.blockButtonList.append(GetObject("block_party_request_button"))
			self.viewChatButtonList.append(GetObject("view_chat_on_button"))
			self.viewChatButtonList.append(GetObject("view_chat_off_button"))
			self.alwaysShowNameButtonList.append(GetObject("always_show_name_on_button"))
			self.alwaysShowNameButtonList.append(GetObject("always_show_name_off_button"))
			self.showDamageButtonList.append(GetObject("show_damage_on_button"))
			self.showDamageButtonList.append(GetObject("show_damage_off_button"))
			self.showsalesTextButtonList.append(GetObject("salestext_on_button"))
			self.showsalesTextButtonList.append(GetObject("salestext_off_button"))
			if app.__BL_HIDE_EFFECT__:			
				for BLEffectNames in ('BUFF_EFFECT', 'SKILL_EFFECT'):
					self.BLEffectGroupList.append(GetObject(BLEffectNames))

			self.renderTarget.append(GetObject("RenderTarget_on_off"))
			self.ctrlShopNamesRange = GetObject("salestext_range_controller")

			global MOBILE
			if MOBILE:
				self.inputMobileButton = GetObject("input_mobile_button")
				self.deleteMobileButton = GetObject("delete_mobile_button")


		except:
			import exception
			exception.Abort("OptionDialog.__Load_BindObject")

	def __Load(self):
		global MOBILE
		if MOBILE:
			self.__Load_LoadScript("uiscript/gameoptiondialog_formobile.py")
		else:
			self.__Load_LoadScript("uiscript/gameoptiondialog.py")

		self.__Load_BindObject()

		self.SetCenterPosition()

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

		self.nameColorModeButtonList[0].SAFE_SetEvent(self.__OnClickNameColorModeNormalButton)
		self.nameColorModeButtonList[1].SAFE_SetEvent(self.__OnClickNameColorModeEmpireButton)

		self.viewTargetBoardButtonList[0].SAFE_SetEvent(self.__OnClickTargetBoardViewButton)
		self.viewTargetBoardButtonList[1].SAFE_SetEvent(self.__OnClickTargetBoardNoViewButton)

		self.pvpModeButtonDict[player.PK_MODE_PEACE].SAFE_SetEvent(self.__OnClickPvPModePeaceButton)
		self.pvpModeButtonDict[player.PK_MODE_REVENGE].SAFE_SetEvent(self.__OnClickPvPModeRevengeButton)
		self.pvpModeButtonDict[player.PK_MODE_GUILD].SAFE_SetEvent(self.__OnClickPvPModeGuildButton)
		self.pvpModeButtonDict[player.PK_MODE_FREE].SAFE_SetEvent(self.__OnClickPvPModeFreeButton)
		if app.__BL_HIDE_EFFECT__:
			for (Index, Button) in enumerate(self.BLEffectGroupList):
				Button.SetToggleDownEvent(lambda arg=Index: self.__OnClickBLEffectButton(arg))
				Button.SetToggleUpEvent(lambda arg=Index: self.__OnClickBLEffectButton(arg))
			self.__RefreshBLEffectButton()

		self.blockButtonList[0].SetToggleUpEvent(self.__OnClickBlockExchangeButton)
		self.blockButtonList[1].SetToggleUpEvent(self.__OnClickBlockPartyButton)
		self.blockButtonList[2].SetToggleUpEvent(self.__OnClickBlockGuildButton)
		self.blockButtonList[3].SetToggleUpEvent(self.__OnClickBlockWhisperButton)
		self.blockButtonList[4].SetToggleUpEvent(self.__OnClickBlockFriendButton)
		self.blockButtonList[5].SetToggleUpEvent(self.__OnClickBlockPartyRequest)

		self.blockButtonList[0].SetToggleDownEvent(self.__OnClickBlockExchangeButton)
		self.blockButtonList[1].SetToggleDownEvent(self.__OnClickBlockPartyButton)
		self.blockButtonList[2].SetToggleDownEvent(self.__OnClickBlockGuildButton)
		self.blockButtonList[3].SetToggleDownEvent(self.__OnClickBlockWhisperButton)
		self.blockButtonList[4].SetToggleDownEvent(self.__OnClickBlockFriendButton)
		self.blockButtonList[5].SetToggleDownEvent(self.__OnClickBlockPartyRequest)

		self.viewChatButtonList[0].SAFE_SetEvent(self.__OnClickViewChatOnButton)
		self.viewChatButtonList[1].SAFE_SetEvent(self.__OnClickViewChatOffButton)

		self.alwaysShowNameButtonList[0].SAFE_SetEvent(self.__OnClickAlwaysShowNameOnButton)
		self.alwaysShowNameButtonList[1].SAFE_SetEvent(self.__OnClickAlwaysShowNameOffButton)

		self.showDamageButtonList[0].SAFE_SetEvent(self.__OnClickShowDamageOnButton)
		self.showDamageButtonList[1].SAFE_SetEvent(self.__OnClickShowDamageOffButton)
		
		self.showsalesTextButtonList[0].SAFE_SetEvent(self.__OnClickSalesTextOnButton)
		self.showsalesTextButtonList[1].SAFE_SetEvent(self.__OnClickSalesTextOffButton)	

		self.renderTarget[0].SetToggleUpEvent(self.__OnClickRenderTargetOnButton)
		self.renderTarget[0].SetToggleDownEvent(self.__OnClickRenderTargetOffButton)
		
		self.__ClickRadioButton(self.nameColorModeButtonList, constInfo.GET_CHRNAME_COLOR_INDEX())
		self.__ClickRadioButton(self.viewTargetBoardButtonList, constInfo.GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD())
		self.__SetPeacePKMode()

		self.ctrlShopNamesRange.SetSliderPos(float(uiPrivateShopBuilder.GetShopNamesRange()))
		self.ctrlShopNamesRange.SetEvent(ui.__mem_func__(self.OnChangeShopNamesRange))
				
		self.UpdateRenderSystem()

		self.stoneScaleTextLine = ui.TextLine()
		self.stoneScaleTextLine.SetParent(self)
		self.stoneScaleTextLine.SetPosition(30, 340 + 2)
		self.stoneScaleTextLine.SetText("Stone scale")
		self.stoneScaleTextLine.Show()

		self.stoneScaleSlider = ui.SliderBar()
		self.stoneScaleSlider.SetParent(self)
		self.stoneScaleSlider.SetPosition(110, 340)
		self.stoneScaleSlider.SetSliderPos(float(systemSetting.GetStoneScale()) / 2.0)
		self.stoneScaleSlider.SetEvent(ui.__mem_func__(self.OnChangeStoneScale))
		self.stoneScaleSlider.Show()
		
		if app.ENABLE_DROP_EFFECT_OPTION:
			dropEffectTextLine = ui.TextLine()
			dropEffectTextLine.SetParent(self)
			dropEffectTextLine.SetPosition(30, 365 + 2)
			dropEffectTextLine.SetText("Drop Effect")
			dropEffectTextLine.Show()
			self.dropEffectTextLine = dropEffectTextLine
		
			dropEffectOn = ui.RadioButton()
			dropEffectOn.SetParent(self)
			dropEffectOn.SetPosition(90, 365)
			dropEffectOn.SetUpVisual("d:/ymir work/ui/public/Middle_Button_01.sub")
			dropEffectOn.SetOverVisual("d:/ymir work/ui/public/Middle_Button_02.sub")
			dropEffectOn.SetDownVisual("d:/ymir work/ui/public/Middle_Button_03.sub")
			dropEffectOn.SetText(uiScriptLocale.OPTION_VIEW_CHAT_ON)
			dropEffectOn.Show()
			self.dropEffectOn = dropEffectOn

			dropEffectOff = ui.RadioButton()
			dropEffectOff.SetParent(self)
			dropEffectOff.SetPosition(155, 365)
			dropEffectOff.SetUpVisual("d:/ymir work/ui/public/Middle_Button_01.sub")
			dropEffectOff.SetOverVisual("d:/ymir work/ui/public/Middle_Button_02.sub")
			dropEffectOff.SetDownVisual("d:/ymir work/ui/public/Middle_Button_03.sub")
			dropEffectOff.SetText(uiScriptLocale.OPTION_VIEW_CHAT_OFF)
			dropEffectOff.Show()
			self.dropEffectOff = dropEffectOff
			
			self.dropEffectButtonList = []
			self.dropEffectButtonList.append(self.dropEffectOn)
			self.dropEffectButtonList.append(self.dropEffectOff)
			self.dropEffectButtonList[0].SAFE_SetEvent(self.OnClickShowDropEffectButton)
			self.dropEffectButtonList[1].SAFE_SetEvent(self.OnClickHideDropEffectButton)		
			self.RefreshDropEffectButtons()
	
		#global MOBILE
		if MOBILE:
			self.inputMobileButton.SetEvent(ui.__mem_func__(self.__OnChangeMobilePhoneNumber))
			self.deleteMobileButton.SetEvent(ui.__mem_func__(self.__OnDeleteMobilePhoneNumber))

	if app.ENABLE_DROP_EFFECT_OPTION:	
		def OnClickShowDropEffectButton(self):
			systemSetting.HideDropEffect(False)
			self.RefreshDropEffectButtons()

		def OnClickHideDropEffectButton(self):
			systemSetting.HideDropEffect(True)
			self.RefreshDropEffectButtons()
			
		def RefreshDropEffectButtons(self):
			if systemSetting.IsHideDropEffect():
				self.dropEffectButtonList[1].Down()
				self.dropEffectButtonList[0].SetUp()
			else:
				self.dropEffectButtonList[1].SetUp()
				self.dropEffectButtonList[0].Down()
			
	def MinMax(self, min, value, max):
		temp = min
		if min > value:
			temp = min
		else:
			temp = value
			
		if max < temp:
			return max
		else:
			return temp
			
	def OnChangeStoneScale(self):
		value = self.MinMax(0.5, self.stoneScaleSlider.GetSliderPos() * 2, 2.0)
		systemSetting.SetStoneScale(value)
		
	def OnChangeShopNamesRange(self):
		pos = self.ctrlShopNamesRange.GetSliderPos()
		uiPrivateShopBuilder.SetShopNamesRange(pos)
		if systemSetting.IsShowSalesText():
			uiPrivateShopBuilder.UpdateADBoard()

	def __ClickRadioButton(self, buttonList, buttonIndex):
		try:
			selButton=buttonList[buttonIndex]
		except IndexError:
			return

		for eachButton in buttonList:
			eachButton.SetUp()

		selButton.Down()
		
	def UpdateRenderSystem(self):
		if constInfo.DISABLE_MODEL_PREVIEW == 1:
			self.renderTarget[0].Down()
		else:
			self.renderTarget[0].SetUp()

			
	def __OnClickRenderTargetOnButton(self):
		constInfo.DISABLE_MODEL_PREVIEW = 0
		self.UpdateRenderSystem()
		with open('render_target.cfg', 'w') as f:
			f.write('0')

	def __OnClickRenderTargetOffButton(self):
		constInfo.DISABLE_MODEL_PREVIEW = 1
		self.UpdateRenderSystem()		
		with open('render_target.cfg', 'w') as f:
			f.write('1')

	def __SetNameColorMode(self, index):
		constInfo.SET_CHRNAME_COLOR_INDEX(index)
		self.__ClickRadioButton(self.nameColorModeButtonList, index)

	def __SetTargetBoardViewMode(self, flag):
		constInfo.SET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD(flag)
		self.__ClickRadioButton(self.viewTargetBoardButtonList, flag)

	def __OnClickNameColorModeNormalButton(self):
		self.__SetNameColorMode(0)

	def __OnClickNameColorModeEmpireButton(self):
		self.__SetNameColorMode(1)

	def __OnClickTargetBoardViewButton(self):
		self.__SetTargetBoardViewMode(0)

	def __OnClickTargetBoardNoViewButton(self):
		self.__SetTargetBoardViewMode(1)

	def __OnClickCameraModeShortButton(self):
		self.__SetCameraMode(0)

	def __OnClickCameraModeLongButton(self):
		self.__SetCameraMode(1)

	def __OnClickFogModeLevel0Button(self):
		self.__SetFogLevel(0)

	def __OnClickFogModeLevel1Button(self):
		self.__SetFogLevel(1)

	def __OnClickFogModeLevel2Button(self):
		self.__SetFogLevel(2)

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
	def __OnClickBlockPartyRequest(self):
		self.RefreshBlock()
		global blockMode
		net.SendChatPacket("/setblockmode " + str(blockMode ^ player.BLOCK_PARTY_REQUEST))

	def __OnClickViewChatOnButton(self):
		global viewChatMode
		viewChatMode = 1
		systemSetting.SetViewChatFlag(viewChatMode)
		self.RefreshViewChat()
	def __OnClickViewChatOffButton(self):
		global viewChatMode
		viewChatMode = 0
		systemSetting.SetViewChatFlag(viewChatMode)
		self.RefreshViewChat()

	def __OnClickAlwaysShowNameOnButton(self):
		systemSetting.SetAlwaysShowNameFlag(TRUE)
		self.RefreshAlwaysShowName()

	def __OnClickAlwaysShowNameOffButton(self):
		systemSetting.SetAlwaysShowNameFlag(FALSE)
		self.RefreshAlwaysShowName()

	def __OnClickShowDamageOnButton(self):
		systemSetting.SetShowDamageFlag(TRUE)
		self.RefreshShowDamage()

	def __OnClickShowDamageOffButton(self):
		systemSetting.SetShowDamageFlag(FALSE)
		self.RefreshShowDamage()
		
	def __OnClickSalesTextOnButton(self):
		systemSetting.SetShowSalesTextFlag(TRUE)
		self.RefreshShowSalesText()
		uiPrivateShopBuilder.UpdateADBoard()
		
	def __OnClickSalesTextOffButton(self):
		systemSetting.SetShowSalesTextFlag(FALSE)
		self.RefreshShowSalesText()		
		
	def __CheckPvPProtectedLevelPlayer(self):	
		if player.GetStatus(player.LEVEL)<constInfo.PVPMODE_PROTECTED_LEVEL:
			self.__SetPeacePKMode()
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_PROTECT % (constInfo.PVPMODE_PROTECTED_LEVEL))
			return 1

		return 0

	def __SetPKMode(self, mode):
		for btn in self.pvpModeButtonDict.values():
			btn.SetUp()
		if self.pvpModeButtonDict.has_key(mode):
			self.pvpModeButtonDict[mode].Down()

	def __SetPeacePKMode(self):
		self.__SetPKMode(player.PK_MODE_PEACE)
	if app.__BL_HIDE_EFFECT__:
		def __OnClickBLEffectButton(self, Index):
			systemSetting.SetBLEffectOption(Index, not systemSetting.GetBLEffectOption(Index))
			self.__RefreshBLEffectButton()
		
		def __RefreshBLEffectButton(self):
			for (Index, Button) in enumerate(self.BLEffectGroupList):
				if systemSetting.GetBLEffectOption(Index):
					Button.SetUp()
				else:
					Button.Down()

	def __RefreshPVPButtonList(self):
		self.__SetPKMode(player.GetPKMode())

	if app.ENABLE_MELEY_LAIR_DUNGEON:
		def setMeleyMap(self):
			mapName = background.GetCurrentMapName()
			if mapName == "metin2_map_n_flame_dragon":
				if player.GetGuildID() != 0 and player.GetPKMode() != player.PK_MODE_GUILD:
					for btn in self.pvpModeButtonDict.values():
						btn.SetUp()
					
					net.SendChatPacket("/pkmode 4", chat.CHAT_TYPE_TALKING)
					self.pvpModeButtonDict[player.PK_MODE_GUILD].Down()

		def isMeleyMap(self, button):
			mapName = background.GetCurrentMapName()
			if mapName == "metin2_map_n_flame_dragon":
				if self.pvpModeButtonDict[button]:
					self.pvpModeButtonDict[button].SetUp()
				
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CANNOT_CHANGE_FIGHT_MODE)
				return 1
			
			return 0

	def __OnClickPvPModePeaceButton(self):
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			if self.isMeleyMap(player.PK_MODE_PEACE):
				return
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 0", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeRevengeButton(self):
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			if self.isMeleyMap(player.PK_MODE_REVENGE):
				return
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 1", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeFreeButton(self):
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			if self.isMeleyMap(player.PK_MODE_FREE):
				return
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 2", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def __OnClickPvPModeGuildButton(self):
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			if self.isMeleyMap(player.PK_MODE_GUILD):
				return
		if self.__CheckPvPProtectedLevelPlayer():
			return

		self.__RefreshPVPButtonList()

		if 0 == player.GetGuildID():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_CANNOT_SET_GUILD_MODE)
			return

		if constInfo.PVPMODE_ENABLE:
			net.SendChatPacket("/pkmode 4", chat.CHAT_TYPE_TALKING)
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.OPTION_PVPMODE_NOT_SUPPORT)

	def OnChangePKMode(self):
		self.__RefreshPVPButtonList()

	def __OnChangeMobilePhoneNumber(self):
		global MOBILE
		if not MOBILE:
			return

		import uiCommon
		inputDialog = uiCommon.InputDialog()
		inputDialog.SetTitle(localeInfo.MESSENGER_INPUT_MOBILE_PHONE_NUMBER_TITLE)
		inputDialog.SetMaxLength(13)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OnInputMobilePhoneNumber))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseInputDialog))
		inputDialog.Open()
		self.inputDialog = inputDialog

	def __OnDeleteMobilePhoneNumber(self):
		global MOBILE
		if not MOBILE:
			return

		import uiCommon
		questionDialog = uiCommon.QuestionDialog()
		questionDialog.SetText(localeInfo.MESSENGER_DO_YOU_DELETE_PHONE_NUMBER)
		questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDeleteMobile))
		questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		questionDialog.Open()
		self.questionDialog = questionDialog

	def OnInputMobilePhoneNumber(self):
		global MOBILE
		if not MOBILE:
			return

		text = self.inputDialog.GetText()

		if not text:
			return

		text.replace('-', '')
		net.SendChatPacket("/mobile " + text)
		self.OnCloseInputDialog()
		return TRUE

	def OnInputMobileAuthorityCode(self):
		global MOBILE
		if not MOBILE:
			return

		text = self.inputDialog.GetText()
		net.SendChatPacket("/mobile_auth " + text)
		self.OnCloseInputDialog()
		return TRUE

	def OnDeleteMobile(self):
		global MOBILE
		if not MOBILE:
			return

		net.SendChatPacket("/mobile")
		self.OnCloseQuestionDialog()
		return TRUE

	def OnCloseInputDialog(self):
		self.inputDialog.Close()
		self.inputDialog = None
		return TRUE

	def OnCloseQuestionDialog(self):
		self.questionDialog.Close()
		self.questionDialog = None
		return TRUE

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def RefreshMobile(self):
		global MOBILE
		if not MOBILE:
			return

		if player.HasMobilePhoneNumber():
			self.inputMobileButton.Hide()
			self.deleteMobileButton.Show()
		else:
			self.inputMobileButton.Show()
			self.deleteMobileButton.Hide()

	def OnMobileAuthority(self):
		global MOBILE
		if not MOBILE:
			return

		import uiCommon
		inputDialog = uiCommon.InputDialogWithDescription()
		inputDialog.SetTitle(localeInfo.MESSENGER_INPUT_MOBILE_AUTHORITY_TITLE)
		inputDialog.SetDescription(localeInfo.MESSENGER_INPUT_MOBILE_AUTHORITY_DESCRIPTION)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OnInputMobileAuthorityCode))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseInputDialog))
		inputDialog.SetMaxLength(4)
		inputDialog.SetBoardWidth(310)
		inputDialog.Open()
		self.inputDialog = inputDialog

	def RefreshBlock(self):
		global blockMode
		for i in xrange(len(self.blockButtonList)):
			if 0 != (blockMode & (1 << i)):
				self.blockButtonList[i].Down()
			else:
				self.blockButtonList[i].SetUp()

	def RefreshViewChat(self):
		if systemSetting.IsViewChat():
			self.viewChatButtonList[0].Down()
			self.viewChatButtonList[1].SetUp()
		else:
			self.viewChatButtonList[0].SetUp()
			self.viewChatButtonList[1].Down()

	def RefreshAlwaysShowName(self):
		if systemSetting.IsAlwaysShowName():
			self.alwaysShowNameButtonList[0].Down()
			self.alwaysShowNameButtonList[1].SetUp()
		else:
			self.alwaysShowNameButtonList[0].SetUp()
			self.alwaysShowNameButtonList[1].Down()

	def RefreshShowDamage(self):
		if systemSetting.IsShowDamage():
			self.showDamageButtonList[0].Down()
			self.showDamageButtonList[1].SetUp()
		else:
			self.showDamageButtonList[0].SetUp()
			self.showDamageButtonList[1].Down()
			
	def RefreshShowSalesText(self):
		if systemSetting.IsShowSalesText():
			self.showsalesTextButtonList[0].Down()
			self.showsalesTextButtonList[1].SetUp()
		else:
			self.showsalesTextButtonList[0].SetUp()
			self.showsalesTextButtonList[1].Down()

	def OnBlockMode(self, mode):
		global blockMode
		blockMode = mode
		self.RefreshBlock()

	def Show(self):
		self.RefreshMobile()
		self.RefreshBlock()
		ui.ScriptWindow.Show(self)
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			self.setMeleyMap()

	def Close(self):
		self.Hide()
