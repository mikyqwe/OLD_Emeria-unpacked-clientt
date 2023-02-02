import ui
import net
import localeInfo

class OpenItemPickupFilterDialog(ui.BoardWithTitleBar):

	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.slotPos = 0
		self.pickupFilterFlag = 0
		self.pickupIgnoreButtonList = []
		self.LoadOpenItemPickupFilterDialog()
		
	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)
		
	def LoadOpenItemPickupFilterDialog(self):     
		self.SetTitleName(localeInfo.PICKUP_FILTER_TITLE)
		self.SetSize(300, 140)
		self.AddFlag('movable')
		self.AddFlag("float")
		self.SetCenterPosition()
		self.SetCloseEvent(self.Close)  
		
		self.dropWindowNewBar = ui.HorizontalBar()
		self.dropWindowNewBar.SetParent(self)
		self.dropWindowNewBar.Create(self.GetWidth() - 30)
		self.dropWindowNewBar.SetPosition(15, 30)
		self.dropWindowNewBar.Show()
		
		self.dropWindowTextLineDropsIgnore = ui.TextLine()
		self.dropWindowTextLineDropsIgnore.SetParent(self.dropWindowNewBar)
		self.dropWindowTextLineDropsIgnore.SetPosition(0, 2)
		self.dropWindowTextLineDropsIgnore.SetWindowHorizontalAlignCenter()
		self.dropWindowTextLineDropsIgnore.SetHorizontalAlignCenter()
		self.dropWindowTextLineDropsIgnore.SetText(localeInfo.PICKUP_FILTER_IGNORE_LABEL)
		self.dropWindowTextLineDropsIgnore.Show()
		
		self.dropWindowToggleButtonDropsIgnoreWeapon = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreWeapon.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreWeapon.SetPosition(25, 55)
		self.dropWindowToggleButtonDropsIgnoreWeapon.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreWeapon.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreWeapon.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreWeapon.SetText(localeInfo.PICKUP_FILTER_IGNORE_WEAPON_LABEL)
		self.dropWindowToggleButtonDropsIgnoreWeapon.Show()
		
		self.dropWindowToggleButtonDropsIgnoreArmor = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreArmor.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreArmor.SetPosition(155, 55)
		self.dropWindowToggleButtonDropsIgnoreArmor.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreArmor.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreArmor.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreArmor.SetText(localeInfo.PICKUP_FILTER_IGNORE_ARMOR_LABEL)
		self.dropWindowToggleButtonDropsIgnoreArmor.Show()
		
		self.dropWindowToggleButtonDropsIgnoreHead = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreHead.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreHead.SetPosition(25, 80)
		self.dropWindowToggleButtonDropsIgnoreHead.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreHead.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreHead.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreHead.SetText(localeInfo.PICKUP_FILTER_IGNORE_HEAD_LABEL)
		self.dropWindowToggleButtonDropsIgnoreHead.Show()
		
		self.dropWindowToggleButtonDropsIgnoreShield = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreShield.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreShield.SetPosition(220, 80)
		self.dropWindowToggleButtonDropsIgnoreShield.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreShield.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreShield.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreShield.SetText(localeInfo.PICKUP_FILTER_IGNORE_SHIELD_LABEL)
		self.dropWindowToggleButtonDropsIgnoreShield.Show()
		
		self.dropWindowToggleButtonDropsIgnoreWrist = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreWrist.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreWrist.SetPosition(90, 55)
		self.dropWindowToggleButtonDropsIgnoreWrist.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreWrist.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreWrist.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreWrist.SetText(localeInfo.PICKUP_FILTER_IGNORE_WRIST_LABEL)
		self.dropWindowToggleButtonDropsIgnoreWrist.Show()
		
		self.dropWindowToggleButtonDropsIgnoreFoots = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreFoots.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreFoots.SetPosition(220, 55)
		self.dropWindowToggleButtonDropsIgnoreFoots.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreFoots.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreFoots.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreFoots.SetText(localeInfo.PICKUP_FILTER_IGNORE_FOOTS_LABEL)
		self.dropWindowToggleButtonDropsIgnoreFoots.Show()
		
		self.dropWindowToggleButtonDropsIgnoreNeck = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreNeck.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreNeck.SetPosition(90, 80)
		self.dropWindowToggleButtonDropsIgnoreNeck.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreNeck.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreNeck.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreNeck.SetText(localeInfo.PICKUP_FILTER_IGNORE_NECK_LABEL)
		self.dropWindowToggleButtonDropsIgnoreNeck.Show()
		
		self.dropWindowToggleButtonDropsIgnoreEar = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreEar.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreEar.SetPosition(155, 80)
		self.dropWindowToggleButtonDropsIgnoreEar.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.dropWindowToggleButtonDropsIgnoreEar.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.dropWindowToggleButtonDropsIgnoreEar.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.dropWindowToggleButtonDropsIgnoreEar.SetText(localeInfo.PICKUP_FILTER_IGNORE_EAR_LABEL)
		self.dropWindowToggleButtonDropsIgnoreEar.Show()
		
		self.dropWindowToggleButtonDropsIgnoreEtc = ui.ToggleButton()
		self.dropWindowToggleButtonDropsIgnoreEtc.SetParent(self)
		self.dropWindowToggleButtonDropsIgnoreEtc.SetPosition(25, 105)
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

		for i in xrange(len(self.pickupIgnoreButtonList)):
			self.pickupIgnoreButtonList[i].SetToggleUpEvent(lambda type = 1 << i, ignore = False : self.OnClickPickupIgnoreButton(type, ignore))
			self.pickupIgnoreButtonList[i].SetToggleDownEvent(lambda type = 1 << i, ignore = True : self.OnClickPickupIgnoreButton(type, ignore))
		
		self.acceptButton = ui.Button()
		self.acceptButton.SetParent(self)
		self.acceptButton.SetPosition(125, 105)
		self.acceptButton.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.acceptButton.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.acceptButton.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.acceptButton.SetText("change")
		self.acceptButton.SetEvent(ui.__mem_func__(self.OnAccept))
		self.acceptButton.Show()
		
		self.Hide()
		
	def OnAccept(self):
		net.SendChatPacket("/change_item_pickup_filter %d %d" % (self.slotPos, self.pickupFilterFlag))
		self.Close()
		
	def OnClickPickupIgnoreButton(self, type, ignore):		
		if ignore:
			self.pickupFilterFlag += type
		else:
			self.pickupFilterFlag -= type
	
		self.RefreshPickupIgnoreButtons()
		
	def RefreshPickupIgnoreButtons(self):		
		for i in xrange(len(self.pickupIgnoreButtonList)):
			flag = (1 << i)
			if self.pickupFilterFlag & flag:
				self.pickupIgnoreButtonList[i].Down()
			else:
				self.pickupIgnoreButtonList[i].SetUp()
				
	def Open(self, slotPos, pickupFilterFlag):
		self.slotPos = slotPos
		self.pickupFilterFlag = pickupFilterFlag
		self.RefreshPickupIgnoreButtons()	
		
		self.Show()
		self.SetTop()
		
	def Destroy(self):
		self.Hide()
		return TRUE
		
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
		

