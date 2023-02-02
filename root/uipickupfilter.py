import ui
import cfg
import localeInfo

class PickupFilterDialog(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.pickupModeButtonList = []
		self.pickupIgnoreButtonList = []
		self.LoadPickupFilterDialog()
		
	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)

	def LoadPickupFilterDialog(self):     
		self.SetSize(300, 200)
		self.Hide()
		self.AddFlag('movable')
		self.AddFlag("float")
		self.SetTitleName('Pickupfilter')
		self.SetCenterPosition()
		self.SetCloseEvent(self.Close)
		self.LoadGUI()
		
	def LoadGUI(self):		
		self.dropWindowNewBar = ui.HorizontalBar()
		self.dropWindowNewBar.SetParent(self)
		self.dropWindowNewBar.Create(self.GetWidth() - 30)
		self.dropWindowNewBar.SetPosition(15, 10 + 30)
		self.dropWindowNewBar.Show()
		
		self.dropWindowTextLinePickupMode = ui.TextLine()
		self.dropWindowTextLinePickupMode.SetParent(self.dropWindowNewBar)
		self.dropWindowTextLinePickupMode.SetPosition(0, 2)
		self.dropWindowTextLinePickupMode.SetWindowHorizontalAlignCenter()
		self.dropWindowTextLinePickupMode.SetHorizontalAlignCenter()
		self.dropWindowTextLinePickupMode.SetText(localeInfo.PICKUP_FILTER_MODE_LABEL)
		self.dropWindowTextLinePickupMode.Show()

		self.dropWindowRadioButtonPickupModeSingle = ui.RadioButton()
		self.dropWindowRadioButtonPickupModeSingle.SetParent(self)
		self.dropWindowRadioButtonPickupModeSingle.SetPosition(95 - 30, 27 + 30)
		self.dropWindowRadioButtonPickupModeSingle.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.dropWindowRadioButtonPickupModeSingle.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.dropWindowRadioButtonPickupModeSingle.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.dropWindowRadioButtonPickupModeSingle.SetText(localeInfo.PICKUP_FILTER_MODE_SINGLE_LABEL)
		self.dropWindowRadioButtonPickupModeSingle.Show()

		self.dropWindowRadioButtonPickupModeAll = ui.RadioButton()
		self.dropWindowRadioButtonPickupModeAll.SetParent(self)
		self.dropWindowRadioButtonPickupModeAll.SetPosition(195 - 30, 27 + 30)
		self.dropWindowRadioButtonPickupModeAll.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.dropWindowRadioButtonPickupModeAll.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.dropWindowRadioButtonPickupModeAll.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.dropWindowRadioButtonPickupModeAll.SetText(localeInfo.PICKUP_FILTER_MODE_ALL_LABEL)
		self.dropWindowRadioButtonPickupModeAll.Show()
		
		self.pickupModeButtonList.append(self.dropWindowRadioButtonPickupModeSingle)
		self.pickupModeButtonList.append(self.dropWindowRadioButtonPickupModeAll)
		
		self.dropWindowNewBar2 = ui.HorizontalBar()
		self.dropWindowNewBar2.SetParent(self)
		self.dropWindowNewBar2.Create(self.GetWidth() - 30)
		self.dropWindowNewBar2.SetPosition(15, 50 + 30)
		self.dropWindowNewBar2.Show()
		
		self.dropWindowTextLineDropsIgnore = ui.TextLine()
		self.dropWindowTextLineDropsIgnore.SetParent(self.dropWindowNewBar2)
		self.dropWindowTextLineDropsIgnore.SetPosition(0, 2)
		self.dropWindowTextLineDropsIgnore.SetWindowHorizontalAlignCenter()
		self.dropWindowTextLineDropsIgnore.SetHorizontalAlignCenter()
		self.dropWindowTextLineDropsIgnore.SetText(localeInfo.PICKUP_FILTER_IGNORE_LABEL)
		self.dropWindowTextLineDropsIgnore.Show()
		
		self.dropWindowToggleButtonDropsIgnoreWeapon = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreWeapon.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreWeapon.SetPosition(53 - 30, 75 + 30)
		self.dropWindowToggleButtonDropsIgnoreWeapon.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreWeapon.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreWeapon.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreWeapon.SetText(localeInfo.PICKUP_FILTER_IGNORE_WEAPON_LABEL)
		self.dropWindowToggleButtonDropsIgnoreWeapon.Show()
		
		self.dropWindowToggleButtonDropsIgnoreArmor = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreArmor.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreArmor.SetPosition(183 - 30, 75 + 30)
		self.dropWindowToggleButtonDropsIgnoreArmor.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreArmor.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreArmor.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreArmor.SetText(localeInfo.PICKUP_FILTER_IGNORE_ARMOR_LABEL)
		self.dropWindowToggleButtonDropsIgnoreArmor.Show()
		
		self.dropWindowToggleButtonDropsIgnoreHead = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreHead.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreHead.SetPosition(53 - 30, 100 + 30)
		self.dropWindowToggleButtonDropsIgnoreHead.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreHead.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreHead.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreHead.SetText(localeInfo.PICKUP_FILTER_IGNORE_HEAD_LABEL)
		self.dropWindowToggleButtonDropsIgnoreHead.Show()
		
		self.dropWindowToggleButtonDropsIgnoreShield = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreShield.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreShield.SetPosition(248 - 30, 100 + 30)
		self.dropWindowToggleButtonDropsIgnoreShield.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreShield.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreShield.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreShield.SetText(localeInfo.PICKUP_FILTER_IGNORE_SHIELD_LABEL)
		self.dropWindowToggleButtonDropsIgnoreShield.Show()
		
		self.dropWindowToggleButtonDropsIgnoreWrist = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreWrist.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreWrist.SetPosition(118 - 30, 75 + 30)
		self.dropWindowToggleButtonDropsIgnoreWrist.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreWrist.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreWrist.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreWrist.SetText(localeInfo.PICKUP_FILTER_IGNORE_WRIST_LABEL)
		self.dropWindowToggleButtonDropsIgnoreWrist.Show()
		
		self.dropWindowToggleButtonDropsIgnoreFoots = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreFoots.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreFoots.SetPosition(248 - 30, 75 + 30)
		self.dropWindowToggleButtonDropsIgnoreFoots.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreFoots.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreFoots.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreFoots.SetText(localeInfo.PICKUP_FILTER_IGNORE_FOOTS_LABEL)
		self.dropWindowToggleButtonDropsIgnoreFoots.Show()
		
		self.dropWindowToggleButtonDropsIgnoreNeck = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreNeck.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreNeck.SetPosition(118 - 30, 100 + 30)
		self.dropWindowToggleButtonDropsIgnoreNeck.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreNeck.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreNeck.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreNeck.SetText(localeInfo.PICKUP_FILTER_IGNORE_NECK_LABEL)
		self.dropWindowToggleButtonDropsIgnoreNeck.Show()
		
		self.dropWindowToggleButtonDropsIgnoreEar = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreEar.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreEar.SetPosition(183 - 30, 100 + 30)
		self.dropWindowToggleButtonDropsIgnoreEar.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreEar.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreEar.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreEar.SetText(localeInfo.PICKUP_FILTER_IGNORE_EAR_LABEL)
		self.dropWindowToggleButtonDropsIgnoreEar.Show()
		
		self.dropWindowToggleButtonDropsIgnoreEtc = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreEtc.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreEtc.SetPosition(148 - 30, 125 + 30)
		self.dropWindowToggleButtonDropsIgnoreEtc.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreEtc.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreEtc.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreEtc.SetText(localeInfo.PICKUP_FILTER_IGNORE_ETC_LABEL)
		self.dropWindowToggleButtonDropsIgnoreEtc.Show()

		self.pickupIgnoreButtonList.append(self.dropWindowToggleButtonDropsIgnoreWeapon)
		self.pickupIgnoreButtonList.append(self.dropWindowToggleButtonDropsIgnoreArmor)
		self.pickupIgnoreButtonList.append(self.dropWindowToggleButtonDropsIgnoreHead)
		self.pickupIgnoreButtonList.append(self.dropWindowToggleButtonDropsIgnoreShield)
		self.pickupIgnoreButtonList.append(self.dropWindowToggleButtonDropsIgnoreWrist)
		self.pickupIgnoreButtonList.append(self.dropWindowToggleButtonDropsIgnoreFoots)
		self.pickupIgnoreButtonList.append(self.dropWindowToggleButtonDropsIgnoreNeck)
		self.pickupIgnoreButtonList.append(self.dropWindowToggleButtonDropsIgnoreEar)
		self.pickupIgnoreButtonList.append(self.dropWindowToggleButtonDropsIgnoreEtc)

		for i in xrange(len(self.pickupModeButtonList)):
			self.pickupModeButtonList[i].SetEvent(lambda mode = i : self.OnClickPickupModeButton(mode))
				
		for i in xrange(len(self.pickupIgnoreButtonList)):
			self.pickupIgnoreButtonList[i].SetToggleUpEvent(lambda type = 1 << i, ignore = False : self.OnClickPickupIgnoreButton(type, ignore))
			self.pickupIgnoreButtonList[i].SetToggleDownEvent(lambda type = 1 << i, ignore = True : self.OnClickPickupIgnoreButton(type, ignore))
			
		self.RefreshPickUpModeButtons()
		self.RefreshPickupIgnoreButtons()	
		
	def OnClickPickupModeButton(self, mode):
		cfg.Set(cfg.SAVE_OPTION, "pickup_filter_mode", mode)
		self.RefreshPickUpModeButtons()
		
	def RefreshPickUpModeButtons(self):
		for button in self.pickupModeButtonList:
			button.SetUp()
		
		self.pickupModeButtonList[int(cfg.Get(cfg.SAVE_OPTION, "pickup_filter_mode", "0"))].Down()
		
	def OnClickPickupIgnoreButton(self, type, ignore):
		pickupFilterFlag = int(cfg.Get(cfg.SAVE_OPTION, "pickup_filter_flag", "0"))
		
		if ignore:
			cfg.Set(cfg.SAVE_OPTION, "pickup_filter_flag", pickupFilterFlag + type)
		else:
			cfg.Set(cfg.SAVE_OPTION, "pickup_filter_flag", pickupFilterFlag - type)
			
		self.RefreshPickupIgnoreButtons()
		
	def RefreshPickupIgnoreButtons(self):
		pickupFilterFlag = int(cfg.Get(cfg.SAVE_OPTION, "pickup_filter_flag", "0"))
		
		for i in xrange(len(self.pickupIgnoreButtonList)):
			flag = (1 << i)
			if pickupFilterFlag & flag:
				self.pickupIgnoreButtonList[i].Down()
			else:
				self.pickupIgnoreButtonList[i].SetUp()

	def Destroy(self):
		self.Hide()
		return TRUE
		
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
		
