import ui
import player
import mouseModule
import net
import app
import snd
import item
import player
import chat
import grp
import uiScriptLocale
import uiRefine
import uiAttachMetin
import uiPickMoney
import uiCommon
import uiPrivateShopBuilder # 개인상점 열동안 ItemMove 방지
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import exchange
import constInfo
import ime
import wndMgr
import apollo_interface
import shop

if app.ENABLE_RENDER_TARGET_SYSTEM:
	import renderTargetExtension

ITEM_MALL_BUTTON_ENABLE = TRUE

if app.ENABLE_SASH_SYSTEM:
	import sash

if app.ENABLE_CHANGELOOK_SYSTEM:
	import changelook

if app.ENABLE_SORT_INVEN:
	import uiToolTip
	
ITEM_FLAG_APPLICABLE = 1 << 14

class CostumeWindow(ui.ScriptWindow):

	TITLE_HOVER_LIST = [uiScriptLocale.COSTUME_WINDOW_TITLE, uiScriptLocale.SHINING_WINDOW_TITLE, "Skill Costume", uiScriptLocale.CHANGE_COSTUME, uiScriptLocale.CHANGE_SHINING ]

	def __init__(self, wndInventory):
		import exception
		
		if not app.ENABLE_COSTUME_SYSTEM:			
			exception.Abort("What do you do?")
			return

		if not wndInventory:
			exception.Abort("wndInventory parameter must be set to InventoryWindow")
			return						
			 	 
		ui.ScriptWindow.__init__(self)
	
		self.isLoaded = 0
		self.page = 0
		self.wndInventory = wndInventory;
		if app.ENABLE_HIDE_COSTUME_SYSTEM:
			self.visibleButtonList = []

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()
		self.RefreshCostumeSlot()

		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "apollo_scripts/CostumeWindow.py")
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.LoadObject")

		try:
			wndEquip = self.GetChild("CostumeSlot")
			if app.ENABLE_HIDE_COSTUME_SYSTEM:
				self.visibleButtonList.append(self.GetChild("BodyToolTipButton"))
				self.visibleButtonList.append(self.GetChild("HairToolTipButton"))
				if app.ENABLE_SASH_SYSTEM:
					self.visibleButtonList.append(self.GetChild("SashToolTipButton"))
				if app.ENABLE_COSTUME_WEAPON_SYSTEM:
					self.visibleButtonList.append(self.GetChild("WeaponToolTipButton"))
			wndShining = self.GetChild("ShiningSlot")
			changeButton = self.GetChild("ChangeButton")
			costumePage = self.GetChild("Costume_Page")
			shiningPage = self.GetChild("Shining_Page")
			wndSkillCostume = self.GetChild("SkillSlot")
			skillPage = self.GetChild("Skill_Page")
			board = self.GetChild("board")
			
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.BindObject")

		wndEquip.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
		wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
		wndEquip.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndEquip.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
		wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))

		wndShining.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
		wndShining.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
		wndShining.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndShining.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndShining.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
		wndShining.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))

		if app.ENABLE_SKILL_COSTUME_SYSTEM:
			wndSkillCostume.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
			wndSkillCostume.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
			wndSkillCostume.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
			wndSkillCostume.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
			wndSkillCostume.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
			wndSkillCostume.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))
			
		if app.ENABLE_HIDE_COSTUME_SYSTEM:
			self.visibleButtonList[0].SetToggleUpEvent(ui.__mem_func__(self.VisibleCostume), 1, 0)
			self.visibleButtonList[1].SetToggleUpEvent(ui.__mem_func__(self.VisibleCostume), 2, 0)
			if app.ENABLE_SASH_SYSTEM:
				self.visibleButtonList[2].SetToggleUpEvent(ui.__mem_func__(self.VisibleCostume), 3, 0)
			if app.ENABLE_COSTUME_WEAPON_SYSTEM:
				self.visibleButtonList[3].SetToggleUpEvent(ui.__mem_func__(self.VisibleCostume), 4, 0)

			self.visibleButtonList[0].SetToggleDownEvent(ui.__mem_func__(self.VisibleCostume), 1, 1)
			self.visibleButtonList[1].SetToggleDownEvent(ui.__mem_func__(self.VisibleCostume), 2, 1)
			if app.ENABLE_SASH_SYSTEM:
				self.visibleButtonList[2].SetToggleDownEvent(ui.__mem_func__(self.VisibleCostume), 3, 1)
			if app.ENABLE_COSTUME_WEAPON_SYSTEM:
				self.visibleButtonList[3].SetToggleDownEvent(ui.__mem_func__(self.VisibleCostume), 4, 1)
			
		self.board = board
		self.board.SetCloseEvent(ui.__mem_func__(self.Close))

		self.changeButton = changeButton
		self.changeButton.SetEvent(ui.__mem_func__(self.ClickChangeButton))

		self.wndEquip = wndEquip
		self.wndShining = wndShining
		self.costumePage = costumePage
		self.costumePage.Show()
		self.shiningPage = shiningPage
		self.shiningPage.Hide()
		if app.ENABLE_SKILL_COSTUME_SYSTEM:
			self.wndSkillCostume = wndSkillCostume
			self.skillPage = skillPage
			self.skillPage.Hide()
		
	def ClickChangeButton(self):
		self.page += 1
		if self.page == 3:
			self.page = 0
			
		if self.page == 0:
			self.shiningPage.Hide()
			self.skillPage.Hide()
			self.costumePage.Show()
		elif self.page == 1:
			self.shiningPage.Show()
			self.skillPage.Hide()
			self.costumePage.Hide()
		elif self.page == 2:
			self.shiningPage.Hide()
			self.skillPage.Show()
			self.costumePage.Hide()	
		#if self.page:
		#	self.shiningPage.Hide()
		#	self.costumePage.Show()
		#else:
		#	self.costumePage.Hide()
		#	self.shiningPage.Show()
		#
		#self.changeButton.SetToolTipText(self.TITLE_HOVER_LIST[self.page+2])
		#self.page ^= True
		
		self.board.SetTitleName(self.TITLE_HOVER_LIST[self.page])
		self.RefreshCostumeSlot()


	def RefreshCostumeSlot(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.wndEquip.SetItemSlot
		
		for i in xrange(item.COSTUME_SLOT_COUNT):
			slotNumber = item.COSTUME_SLOT_START + i
			self.wndEquip.SetItemSlot(slotNumber, getItemVNum(slotNumber), 0)
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = player.GetItemTransmutation(slotNumber)
				if itemTransmutedVnum:
					self.wndEquip.DisableCoverButton(slotNumber)
				else:
					self.wndEquip.EnableCoverButton(slotNumber)

		for i in xrange(item.SHINING_SLOT_COUNT):
			slotNumber = item.SHINING_SLOT_START + i
			self.wndShining.SetItemSlot(slotNumber, getItemVNum(slotNumber), 0)
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = player.GetItemTransmutation(slotNumber)
				if itemTransmutedVnum:
					self.wndEquip.DisableCoverButton(slotNumber)
				else:
					self.wndEquip.EnableCoverButton(slotNumber)

		if app.ENABLE_NEW_EQUIPMENT_SYSTEM:
			for i in xrange(player.NEW_EQUIPMENT_SLOT_COUNT):
				slotNumber = player.NEW_EQUIPMENT_SLOT_START + i
				itemCount = getItemCount(slotNumber)
				if itemCount <= 1:
					itemCount = 0
				setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)

		if app.ENABLE_SKILL_COSTUME_SYSTEM:
			for i in xrange(item.SKILL_COSTUME_SLOT_COUNT):
				slotNumber = item.SKILL_COSTUME_SLOT_START + i
				self.wndSkillCostume.SetItemSlot(slotNumber, getItemVNum(slotNumber), 0)
	
		self.wndEquip.RefreshSlot()
		self.wndShining.RefreshSlot()
		self.wndSkillCostume.RefreshSlot()
		
	if app.ENABLE_HIDE_COSTUME_SYSTEM:
		def RefreshVisibleCostume(self):
			body = constInfo.HIDDEN_BODY_COSTUME
			hair = constInfo.HIDDEN_HAIR_COSTUME
			if app.ENABLE_SASH_SYSTEM:
				sash = constInfo.HIDDEN_SASH_COSTUME
			if app.ENABLE_COSTUME_WEAPON_SYSTEM:
				weapon = constInfo.HIDDEN_WEAPON_COSTUME

			if body == 1:
				self.visibleButtonList[0].SetToolTipText(localeInfo.SHOW_COSTUME)
				self.visibleButtonList[0].Down()
			else:
				self.visibleButtonList[0].SetToolTipText(localeInfo.HIDE_COSTUME)
				self.visibleButtonList[0].SetUp()

			if hair == 1:
				self.visibleButtonList[1].SetToolTipText(localeInfo.SHOW_COSTUME)
				self.visibleButtonList[1].Down()
			else:
				self.visibleButtonList[1].SetToolTipText(localeInfo.HIDE_COSTUME)
				self.visibleButtonList[1].SetUp()

			if app.ENABLE_SASH_SYSTEM:
				if sash == 1:
					self.visibleButtonList[2].SetToolTipText(localeInfo.SHOW_COSTUME)
					self.visibleButtonList[2].Down()
				else:
					self.visibleButtonList[2].SetToolTipText(localeInfo.HIDE_COSTUME)
					self.visibleButtonList[2].SetUp()

			if app.ENABLE_COSTUME_WEAPON_SYSTEM:
				if weapon == 1:
					self.visibleButtonList[3].SetToolTipText(localeInfo.SHOW_COSTUME)
					self.visibleButtonList[3].Down()
				else:
					self.visibleButtonList[3].SetToolTipText(localeInfo.HIDE_COSTUME)
					self.visibleButtonList[3].SetUp()

		def VisibleCostume(self, part, hidden):
			net.SendChatPacket("/hide_costume %d %d" % (part, hidden))
		
class BeltInventoryWindow(ui.ScriptWindow):

	def __init__(self, wndInventory):
		import exception

		if not app.ENABLE_NEW_EQUIPMENT_SYSTEM:
			exception.Abort("What do you do?")
			return

		if not wndInventory:
			exception.Abort("wndInventory parameter must be set to InventoryWindow")
			return

		ui.ScriptWindow.__init__(self)

		self.isLoaded = 0
		self.wndInventory = wndInventory;

		self.wndBeltInventoryLayer = None
		self.wndBeltInventorySlot = None
		self.expandBtn = None
		self.minBtn = None

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self, openBeltSlot = False):
		self.__LoadWindow()
		self.RefreshSlot()

		ui.ScriptWindow.Show(self)

		if openBeltSlot:
			self.OpenInventory()
		else:
			self.CloseInventory()

	def Close(self):
		self.Hide()

	def IsOpeningInventory(self):
		return self.wndBeltInventoryLayer.IsShow()

	def OpenInventory(self):
		self.wndBeltInventoryLayer.Show()
		self.expandBtn.Hide()

		self.AdjustPositionAndSize()

	def CloseInventory(self):
		self.wndBeltInventoryLayer.Hide()
		self.expandBtn.Show()

		self.AdjustPositionAndSize()

	## ?? ???? ??? ???? BASE ??? ??, ??.. ?? ?????? ?? ??? ??? ??..
	def GetBasePosition(self):
		x, y = self.wndInventory.GetGlobalPosition()
		if app.ENABLE_SPECIAL_INVENTORY:
			return x - 155, y + 380
		else:
			return x - 155, y + 265

	def AdjustPositionAndSize(self):
		bx, by = self.GetBasePosition()

		if self.IsOpeningInventory():
			self.SetPosition(bx, by)
			self.SetSize(self.ORIGINAL_WIDTH, self.GetHeight())

		else:
			self.SetPosition(bx + 146, by);
			self.SetSize(10, self.GetHeight())

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "apollo_scripts/BeltInventoryWindow.py")
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.LoadObject")

		try:
			self.ORIGINAL_WIDTH = self.GetWidth()
			wndBeltInventorySlot = self.GetChild("BeltInventorySlot")
			self.wndBeltInventoryLayer = self.GetChild("BeltInventoryLayer")
			self.expandBtn = self.GetChild("ExpandBtn")
			self.minBtn = self.GetChild("MinimizeBtn")

			self.expandBtn.SetEvent(ui.__mem_func__(self.OpenInventory))
			self.minBtn.SetEvent(ui.__mem_func__(self.CloseInventory))

			for i in xrange(item.BELT_INVENTORY_SLOT_COUNT):
				slotNumber = item.BELT_INVENTORY_SLOT_START + i
				wndBeltInventorySlot.SetCoverButton(slotNumber,	"d:/ymir work/ui/game/quest/slot_button_01.sub",\
												"d:/ymir work/ui/game/quest/slot_button_01.sub",\
												"d:/ymir work/ui/game/quest/slot_button_01.sub",\
												apollo_interface.PATCH_COMMON+"/slot_rectangle/slot_unavailable.png", FALSE, FALSE)

		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.BindObject")

		## Equipment
		wndBeltInventorySlot.SetOverInItemEvent(ui.__mem_func__(self.wndInventory.OverInItem))
		wndBeltInventorySlot.SetOverOutItemEvent(ui.__mem_func__(self.wndInventory.OverOutItem))
		wndBeltInventorySlot.SetUnselectItemSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndBeltInventorySlot.SetUseSlotEvent(ui.__mem_func__(self.wndInventory.UseItemSlot))
		wndBeltInventorySlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.wndInventory.SelectEmptySlot))
		wndBeltInventorySlot.SetSelectItemSlotEvent(ui.__mem_func__(self.wndInventory.SelectItemSlot))

		self.wndBeltInventorySlot = wndBeltInventorySlot

	def RefreshSlot(self):
		getItemVNum=player.GetItemIndex

		for i in xrange(item.BELT_INVENTORY_SLOT_COUNT):
			slotNumber = item.BELT_INVENTORY_SLOT_START + i
			self.wndBeltInventorySlot.SetItemSlot(slotNumber, getItemVNum(slotNumber), player.GetItemCount(slotNumber))
			self.wndBeltInventorySlot.SetAlwaysRenderCoverButton(slotNumber, True)

			avail = "0"

			if player.IsAvailableBeltInventoryCell(slotNumber):
				self.wndBeltInventorySlot.EnableCoverButton(slotNumber)
			else:
				self.wndBeltInventorySlot.DisableCoverButton(slotNumber)

		self.wndBeltInventorySlot.RefreshSlot()

		
class InventoryWindow(ui.ScriptWindow):
	liHighlightedItems = []
	USE_TYPE_TUPLE = ("USE_CLEAN_SOCKET", "USE_CHANGE_ATTRIBUTE", "USE_ADD_ATTRIBUTE", "USE_ADD_ATTRIBUTE2", "USE_ADD_ACCESSORY_SOCKET", "USE_PUT_INTO_ACCESSORY_SOCKET", "USE_PUT_INTO_BELT_SOCKET", "USE_PUT_INTO_RING_SOCKET")
	if app.ENABLE_COSTUME_EXTENDED_RECHARGE:
		USE_TYPE_LIST = list(USE_TYPE_TUPLE)
		USE_TYPE_LIST.append("USE_TIME_CHARGE_PER")
		USE_TYPE_LIST.append("USE_TIME_CHARGE_FIX")
		USE_TYPE_TUPLE = tuple(USE_TYPE_LIST)
	if app.ENABLE_NEW_ADDON_SWITCHER:
		USE_TYPE_TUPLE += ("USE_CHANGE_SPECIAL_FKS_ATTRIBUTE", "USE_CHANGE_SPECIAL_DSS_ATTRIBUTE", )

	questionDialog = None
	tooltipItem = None
	wndCostume = None
	wndBelt = None
	dlgPickMoney = None
	
	interface = None
	if app.WJ_ENABLE_TRADABLE_ICON:
		bindWnds = []
		
	if app.ENABLE_SPECIAL_INVENTORY:
		wndInventoryTypeTab = None
		inventoryTypeIndex = 0

	sellingSlotNumber = -1
	isLoaded = 0
	isOpenedCostumeWindowWhenClosingInventory = 0		# 인벤토리 닫을 때 코스츔이 열려있었는지 여부-_-; 네이밍 ㅈㅅ
	isOpenedBeltWindowWhenClosingInventory = 0		# 인벤토리 닫을 때 벨트 인벤토리가 열려있었는지 여부-_-; 네이밍 ㅈㅅ

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.inventoryTypeTabDict = None
		self.inventoryTypeButtonDict = None
		self.isOpenedBeltWindowWhenClosingInventory = 0		# 인벤토리 닫을 때 벨트 인벤토리가 열려있었는지 여부-_-; 네이밍 ㅈㅅ

		self.__LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()

		ui.ScriptWindow.Show(self)

		# 인벤토리를 닫을 때 코스츔이 열려있었다면 인벤토리를 열 때 코스츔도 같이 열도록 함.
		if self.isOpenedCostumeWindowWhenClosingInventory and self.wndCostume:
			self.wndCostume.Show() 

		# 인벤토리를 닫을 때 벨트 인벤토리가 열려있었다면 같이 열도록 함.
		if self.wndBelt:
			self.wndBelt.Show(self.isOpenedBeltWindowWhenClosingInventory)

		if app.ENABLE_SPECIAL_INVENTORY and self.wndInventoryTypeTab:
			self.wndInventoryTypeTab.Show()

	def BindInterfaceClass(self, interface):
		self.interface = interface
		
	if app.WJ_ENABLE_TRADABLE_ICON:
		def BindWindow(self, wnd):
			self.bindWnds.append(wnd)

	def __LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()

			pyScrLoader.LoadScriptFile(self, "apollo_scripts/inventory.py")
		except:
			import exception
			exception.Abort("InventoryWindow.LoadWindow.LoadObject")

		try:
			self.genderEquip = self.GetChild("Gender_Equipment")
			wndItem = self.GetChild("ItemSlot")
			wndEquip = self.GetChild("EquipmentSlot")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.wndMoney = self.GetChild("Money")
			self.wndMoneySlot = self.GetChild("Money_Slot")
			self.mallButton = self.GetChild2("MallButton")
			self.DSSButton = self.GetChild2("DSSButton")
			self.costumeButton = self.GetChild2("CostumeButton")
			
			self.inventoryTab = []
			self.inventoryTab.append(self.GetChild("Inventory_Tab_01"))
			self.inventoryTab.append(self.GetChild("Inventory_Tab_02"))
			self.inventoryTab.append(self.GetChild("Inventory_Tab_03"))
			self.inventoryTab.append(self.GetChild("Inventory_Tab_04"))
			
			self.textColor1 = self.GetChild("Inventory_Tab_01_Print")
			self.textColor2 = self.GetChild("Inventory_Tab_02_Print")
			self.textColor3 = self.GetChild("Inventory_Tab_03_Print")
			self.textColor4 = self.GetChild("Inventory_Tab_04_Print")
			
			self.equipmentTab = []
			self.equipmentTab.append(self.GetChild("Equipment_Tab_01"))
			self.equipmentTab.append(self.GetChild("Equipment_Tab_02"))

			if app.ENABLE_SORT_INVEN:
				self.yenilebutton = self.GetChild2("YenileButton")
				self.yenilebutton.SetEvent(ui.__mem_func__(self.ClickYenileButton))
				self.tooltipI = uiToolTip.ToolTip()
				self.tooltipI.Hide()
				self.tooltipInfo = [self.tooltipI]*4
				self.InformationText = [localeInfo.YENILE_BUTTON_TITLE,
										localeInfo.YENILE_BUTTON,
										localeInfo.YENILE_BUTTON2,
										localeInfo.YENILE_BUTTON3
				]
				for i in xrange(len(self.tooltipInfo)):
					self.tooltipInfo[i].SetFollow(True)
					self.tooltipInfo[i].AlignHorizonalCenter()
					if i == 0:
						self.tooltipInfo[i].AppendTextLine(self.InformationText[i], 0xffffff00)
					else:
						self.tooltipInfo[i].AppendTextLine(self.InformationText[i])
					self.tooltipInfo[i].Hide()
					
			if self.costumeButton and not app.ENABLE_COSTUME_SYSTEM:
				self.costumeButton.Hide()
				self.costumeButton.Destroy()
				self.costumeButton = 0

			# Belt Inventory Window
			self.wndBelt = None
			
			if app.ENABLE_NEW_EQUIPMENT_SYSTEM:
				self.wndBelt = BeltInventoryWindow(self)
				
			
		except:
			import exception
			exception.Abort("InventoryWindow.LoadWindow.BindObject")
		
		race = net.GetMainActorRace()
		try:
			genderImage = apollo_interface.EQUIPEMENT_GENDER[race]
			try:
				self.genderEquip.LoadImage(genderImage)
			except:
				print ("Face.RefreshCharacter(race=%d, genderImage=%s)" % (race,genderImage))
				self.genderEquip.Hide()
		except KeyError:
			self.genderEquip.Hide()
		
		## Item
		wndItem.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndItem.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndItem.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndItem.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndItem.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		## Equipment
		wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
		wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		wndEquip.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndEquip.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
		wndEquip.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		## PickMoneyDialog
		dlgPickMoney = uiPickMoney.PickMoneyDialog()
		dlgPickMoney.LoadDialog()
		dlgPickMoney.Hide()

		## RefineDialog
		self.refineDialog = uiRefine.RefineDialog()
		self.refineDialog.Hide()

		## AttachMetinDialog
		if app.WJ_ENABLE_TRADABLE_ICON:  
			self.attachMetinDialog = uiAttachMetin.AttachMetinDialog(self)
			self.BindWindow(self.attachMetinDialog)
		else:
			self.attachMetinDialog = uiAttachMetin.AttachMetinDialog()
		self.attachMetinDialog.Hide()

		if app.ENABLE_SPECIAL_INVENTORY:
			self.inventoryTypeTabDict = {
				0 : self.GetChild("Inventory_Type_01"),
				1 : self.GetChild("Inventory_Type_02"),
				2 : self.GetChild("Inventory_Type_03"),
				3 : self.GetChild("Inventory_Type_04"),
			}

			self.inventoryTypeButtonDict = {
				0 : self.GetChild("Inventory_Type_Button_01"),
				1 : self.GetChild("Inventory_Type_Button_02"),
				2 : self.GetChild("Inventory_Type_Button_03"),
				3 : self.GetChild("Inventory_Type_Button_04")
			}
			
			self.inventorySafeTypePageIndex = {
				0 : 0,
				1 : 0,
				2 : 0,
				3 : 0,
			}

			for (type, tabButton) in self.inventoryTypeButtonDict.items():
				tabButton.SetEvent(ui.__mem_func__(self.__OnClickTabTypeButton), type)

		## MoneySlot
		self.wndMoneySlot.SetEvent(ui.__mem_func__(self.OpenPickMoneyDialog))

		self.inventoryTab[0].SetEvent(lambda arg=0: self.SetInventoryPage(arg))
		self.inventoryTab[1].SetEvent(lambda arg=1: self.SetInventoryPage(arg))
		self.inventoryTab[2].SetEvent(lambda arg=2: self.SetInventoryPage(arg))
		self.inventoryTab[3].SetEvent(lambda arg=3: self.SetInventoryPage(arg))
		self.inventoryTab[0].Down()
		self.inventoryPageIndex = 0

		self.equipmentTab[0].SetEvent(lambda arg=0: self.SetEquipmentPage(arg))
		self.equipmentTab[1].SetEvent(lambda arg=1: self.SetEquipmentPage(arg))
		self.equipmentTab[0].Down()
		self.equipmentTab[0].Hide()
		self.equipmentTab[1].Hide()
	
		self.wndItem = wndItem
		self.wndEquip = wndEquip
		self.dlgPickMoney = dlgPickMoney

		# MallButton
		if self.mallButton:
			self.mallButton.SetEvent(ui.__mem_func__(self.ClickMallButton))

		if self.DSSButton:
			#self.DSSButton.Hide()
			self.DSSButton.SetEvent(ui.__mem_func__(self.ClickDSSButton)) 
		
		# Costume Button
		if self.costumeButton:
			self.costumeButton.SetEvent(ui.__mem_func__(self.ClickCostumeButton))

		self.wndCostume = None
		self.interface = None
		
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.bindWnds = []

 		#####
		if app.ENABLE_SASH_SYSTEM:
			self.listAttachedSashs = []
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.listAttachedCl = []
		## Refresh
		self.SetInventoryPage(0)
		self.SetInventoryType(0)
		self.SetEquipmentPage(0)
		self.RefreshItemSlot()
		self.RefreshStatus()
			
	if app.ENABLE_INVENTORY_SORT:
		def OnSortInventory(self):
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.INVENTORY_SORT_QUESTION)
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.AcceptSortInventory))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.CancelSortInventory))
			self.questionDialog.Open()
			self.questionDialog.inventoryTypeIndex = self.inventoryTypeIndex

		def CancelSortInventory(self):
			self.OnCloseQuestionDialog()

		def AcceptSortInventory(self):
			if uiPrivateShopBuilder.IsBuildingPrivateShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
				return
			
			if self.questionDialog:
				if self.questionDialog.inventoryTypeIndex == player.INVENTORY_TYPE_INVENTORY:
					net.SendChatPacket("/sort_inventory")
				else:
					net.SendChatPacket("/sort_special_inventory %i" % (self.questionDialog.inventoryTypeIndex-1))
	
				self.questionDialog.Close()

			self.questionDialog = None

	def Destroy(self):
		self.ClearDictionary()

		self.dlgPickMoney.Destroy()
		self.dlgPickMoney = 0

		self.refineDialog.Destroy()
		self.refineDialog = 0

		self.attachMetinDialog.Destroy()
		self.attachMetinDialog = 0

		self.tooltipItem = None
		self.wndItem = 0
		self.wndEquip = 0
		self.wndShining = 0
		if app.ENABLE_SKILL_COSTUME_SYSTEM:
			self.wndSkillCostume = 0
		self.dlgPickMoney = 0
		self.wndMoney = 0
		self.wndMoneySlot = 0
		self.questionDialog = None
		self.mallButton = None
		self.DSSButton = None
		self.interface = None

		if self.wndCostume:
			self.wndCostume.Destroy()
			self.wndCostume = 0
			
		if self.wndBelt:
			self.wndBelt.Destroy()
			self.wndBelt = None
			
		if app.ENABLE_SPECIAL_INVENTORY and self.wndInventoryTypeTab:
			self.inventoryTypeIndex = 0
			self.wndInventoryTypeTab.Destroy()
			self.wndInventoryTypeTab = None

		self.inventoryTab = []
		self.equipmentTab = []

	def Hide(self):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			self.OnCloseQuestionDialog()
			return
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()

		if self.wndCostume:
			self.isOpenedCostumeWindowWhenClosingInventory = self.wndCostume.IsShow()			# 인벤토리 창이 닫힐 때 코스츔이 열려 있었는가?
			self.wndCostume.Close()
 
		if self.wndBelt:
			self.isOpenedBeltWindowWhenClosingInventory = self.wndBelt.IsOpeningInventory()		# 인벤토리 창이 닫힐 때 벨트 인벤토리도 열려 있었는가?
			print "Is Opening Belt Inven?? ", self.isOpenedBeltWindowWhenClosingInventory
			self.wndBelt.Close()
  
		if self.dlgPickMoney:
			self.dlgPickMoney.Close()
		
		if app.ENABLE_SPECIAL_INVENTORY and self.wndInventoryTypeTab:
			self.wndInventoryTypeTab.Hide()

		wndMgr.Hide(self.hWnd)
		
	
	def Close(self):
		self.Hide()

	def OnUpdate(self):
		if app.ENABLE_SORT_INVEN and self.tooltipInfo:
			for i in xrange(len(self.tooltipInfo)):
				if self.yenilebutton.IsIn():
					self.tooltipInfo[i].Show()
				else:
					self.tooltipInfo[i].Hide()
					
	if app.ENABLE_SORT_INVEN:
		def ClickYenileButton(self):
			if uiPrivateShopBuilder.IsBuildingPrivateShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
				return
				
			if app.IsPressed(app.DIK_LALT):
				net.SortInven(2, self.inventoryTypeIndex)
			elif app.IsPressed(app.DIK_LCONTROL):
				net.SortInven(3, self.inventoryTypeIndex)
			else:
				net.SortInven(1, self.inventoryTypeIndex)
				
#	def SetInventoryPage(self, page):
#		self.inventoryTab[self.inventoryPageIndex].SetUp()
#		self.inventoryPageIndex = page
#		self.RefreshBagSlotWindow()

	# def SetInventoryPage(self, page):
		# self.inventoryTab[self.inventoryPageIndex].SetUp()
		# self.inventoryPageIndex = page
		# self.inventoryTab[self.inventoryPageIndex].Down()
		# self.RefreshBagSlotWindow()
	
	def SetInventoryPage(self, page):
		self.inventoryTab[self.inventoryPageIndex].SetUp()
		self.inventoryPageIndex = page
		self.inventoryTab[self.inventoryPageIndex].Down()

		self.inventorySafeTypePageIndex[self.inventoryTypeIndex] = page

		if app.ENABLE_SPECIAL_INVENTORY:	
			if self.inventoryTypeIndex == player.INVENTORY_TYPE_INVENTORY:
				self.RefreshBagSlotWindow()
			else:
				self.RefreshSpecialInventory()
		else:
			self.RefreshBagSlotWindow()
		
		if page == 0:
			self.textColor1.SetPackedFontColor(0xffF8D090)
			self.textColor2.SetPackedFontColor(0xffA08784)
			self.textColor3.SetPackedFontColor(0xffA08784)
			self.textColor4.SetPackedFontColor(0xffA08784)
			
		elif page == 1:
			self.textColor2.SetPackedFontColor(0xffF8D090)
			self.textColor1.SetPackedFontColor(0xffA08784)
			self.textColor3.SetPackedFontColor(0xffA08784)
			self.textColor4.SetPackedFontColor(0xffA08784)
			
		elif page == 2:
			self.textColor3.SetPackedFontColor(0xffF8D090)
			self.textColor1.SetPackedFontColor(0xffA08784)
			self.textColor2.SetPackedFontColor(0xffA08784)
			self.textColor4.SetPackedFontColor(0xffA08784)
			

		elif page == 3:
			self.textColor4.SetPackedFontColor(0xffF8D090)
			self.textColor3.SetPackedFontColor(0xffA08784)
			self.textColor1.SetPackedFontColor(0xffA08784)
			self.textColor2.SetPackedFontColor(0xffA08784)
			
	
	if app.ENABLE_SPECIAL_INVENTORY:
		def __OnClickTabTypeButton(self, type):
			self.SetInventoryType(type)

		def SetInventoryType(self, type):
			self.inventoryTab[self.inventoryPageIndex].SetUp()
			self.inventoryPageIndex = self.inventorySafeTypePageIndex[int(type)]
			self.inventoryTab[self.inventoryPageIndex].Down()
			self.inventoryTypeIndex = int(type)
			
			for (tabKey, tabButton) in self.inventoryTypeButtonDict.items():
				if type!=tabKey:
					tabButton.SetUp()

			for tabValue in self.inventoryTypeTabDict.itervalues():
				tabValue.Hide()

			self.inventoryTypeTabDict[type].Show()

			if self.inventoryTypeIndex == player.INVENTORY_TYPE_INVENTORY:
				self.RefreshBagSlotWindow()
			else:
				self.RefreshSpecialInventory()

		def GetInventoryType(self):
			return self.inventoryTypeIndex
				
		def __SpecialInventoryLocalSlotPosToGlobalSlotPos(self, local):

			if player.IsEquipmentSlot(local) or player.IsCostumeSlot(local):
				return local

			start = player.SPECIAL_INVENTORY_SLOT_START
			slotCountPerType = (player.SPECIAL_INVENTORY_PAGE_SIZE * player.INVENTORY_PAGE_COUNT)
			slotStartForType = start + slotCountPerType * (self.inventoryTypeIndex-1)
			slotPageStart = slotStartForType + (player.SPECIAL_INVENTORY_PAGE_SIZE * self.inventoryPageIndex)

			return slotPageStart + local
			
			
		def RefreshSpecialInventory(self):
			for i in xrange(player.SPECIAL_INVENTORY_PAGE_SIZE):
				slotNumber = self.__SpecialInventoryLocalSlotPosToGlobalSlotPos(i)
				
				itemCount = player.GetItemCount(slotNumber)
				if 0 == itemCount:
					self.wndItem.ClearSlot(i)
					continue
				elif 1 == itemCount:
					itemCount = 0
					
				itemVnum = player.GetItemIndex(slotNumber)

				if itemVnum == 0 and slotNumber in self.liHighlightedItems:
					self.liHighlightedItems.remove(slotNumber)

				#self.wndItem.DeactivateSlot(slotNumber)
				self.wndItem.DeactivateSlot(i)
				self.wndItem.SetItemSlot(i, itemVnum, itemCount)

			self.__RefreshHighlights()

			self.wndItem.RefreshSlot()

			if app.WJ_ENABLE_TRADABLE_ICON:
				map(lambda wnd:wnd.RefreshLockedSlot(), self.bindWnds)
				self.RefreshMarkSlots()
	
	def SetEquipmentPage(self, page):
		self.equipmentPageIndex = page
		self.equipmentTab[1-page].SetUp()
		self.RefreshEquipSlotWindow()

	def ClickMallButton(self):
		#print "click_mall_button"
		#net.SendChatPacket("/click_mall")
		import event
		event.QuestButtonClick(constInfo.QID_MALL)

	# DSSButton
	def ClickDSSButton(self):
		print "click_dss_button"
		self.interface.ToggleDragonSoulWindow()

	def ClickCostumeButton(self):
		print "Click Costume Button"
		if self.wndCostume:
			if self.wndCostume.IsShow(): 
				self.wndCostume.Hide()
			else:
				self.wndCostume.Show()
		else:
			self.wndCostume = CostumeWindow(self)
			self.wndCostume.Show()

	def OpenPickMoneyDialog(self):

		if mouseModule.mouseController.isAttached():

			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			if player.SLOT_TYPE_SAFEBOX == mouseModule.mouseController.GetAttachedType():

				if player.ITEM_MONEY == mouseModule.mouseController.GetAttachedItemIndex():
					net.SendSafeboxWithdrawMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

			mouseModule.mouseController.DeattachObject()

		else:
			curMoney = player.GetElk()

			if curMoney <= 0:
				return

			self.dlgPickMoney.SetTitleName(localeInfo.PICK_MONEY_TITLE)
			self.dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickMoney))
			self.dlgPickMoney.Open(curMoney)
			self.dlgPickMoney.SetMax(7) # 인벤토리 990000 제한 버그 수정

	def OnPickMoney(self, money):
		mouseModule.mouseController.AttachMoney(self, player.SLOT_TYPE_INVENTORY, money)

	def OnPickItem(self, count):
		itemSlotIndex = self.dlgPickMoney.itemGlobalSlotIndex
		selectedItemVNum = player.GetItemIndex(itemSlotIndex)
		mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, count)

	def __InventoryLocalSlotPosToGlobalSlotPos(self, local):
		if player.IsEquipmentSlot(local) or player.IsCostumeSlot(local) or (app.ENABLE_NEW_EQUIPMENT_SYSTEM and player.IsBeltInventorySlot(local)):
			return local

		return self.inventoryPageIndex*player.INVENTORY_PAGE_SIZE + local

	def GetInventoryPageIndex(self):
		return self.inventoryPageIndex

	if app.WJ_ENABLE_TRADABLE_ICON:
		def RefreshMarkSlots(self, localIndex=None):
			if not self.interface:
				return

			onTopWnd = self.interface.GetOnTopWindow()
			if localIndex:
				if app.ENABLE_SPECIAL_INVENTORY:
					if self.inventoryTypeIndex == player.INVENTORY_TYPE_INVENTORY:
						slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(localIndex)
					else:
						slotNumber = self.__SpecialInventoryLocalSlotPosToGlobalSlotPos(localIndex)
				else:
					slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(localIndex)
					
				if onTopWnd == player.ON_TOP_WND_NONE:
					self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif onTopWnd == player.ON_TOP_WND_SHOP:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SELL):
						self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif onTopWnd == player.ON_TOP_WND_EXCHANGE:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_GIVE):
						self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif onTopWnd == player.ON_TOP_WND_PRIVATE_SHOP:
					if player.IsAntiFlagBySlot(slotNumber, item.ITEM_ANTIFLAG_MYSHOP):
						self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				elif onTopWnd == player.ON_TOP_WND_SAFEBOX:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SAFEBOX):
						self.wndItem.SetUnusableSlotOnTopWnd(localIndex)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(localIndex)

				return

			for i in xrange(player.INVENTORY_PAGE_SIZE):
				if app.ENABLE_SPECIAL_INVENTORY:
					if self.inventoryTypeIndex == player.INVENTORY_TYPE_INVENTORY:
						slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)
					else:
						slotNumber = self.__SpecialInventoryLocalSlotPosToGlobalSlotPos(i)
				else:
					slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)	
						
				if onTopWnd == player.ON_TOP_WND_NONE:
					self.wndItem.SetUsableSlotOnTopWnd(i)

				elif onTopWnd == player.ON_TOP_WND_SHOP:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SELL):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

				elif onTopWnd == player.ON_TOP_WND_EXCHANGE:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_GIVE):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

				elif onTopWnd == player.ON_TOP_WND_PRIVATE_SHOP:
					if player.IsAntiFlagBySlot(slotNumber, item.ITEM_ANTIFLAG_MYSHOP):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

				elif onTopWnd == player.ON_TOP_WND_SAFEBOX:
					if player.IsAntiFlagBySlot(slotNumber, item.ANTIFLAG_SAFEBOX):
						self.wndItem.SetUnusableSlotOnTopWnd(i)
					else:
						self.wndItem.SetUsableSlotOnTopWnd(i)

	def RefreshBagSlotWindow(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.wndItem.SetItemSlot

		for i in xrange(player.INVENTORY_PAGE_SIZE):
			slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)			
			
			itemCount = getItemCount(slotNumber)
			# itemCount == 0이면 소켓을 비운다.
			if 0 == itemCount:
				self.wndItem.ClearSlot(i)
				continue
			elif 1 == itemCount:
				itemCount = 0
				
			itemVnum = getItemVNum(slotNumber)
			setItemVNum(i, itemVnum, itemCount)
			if itemVnum == 0 and slotNumber in self.liHighlightedItems:				
				self.liHightlightedItems.remove(slotNumber)
				
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = player.GetItemTransmutation(slotNumber)
				if itemTransmutedVnum:
					self.wndItem.DisableCoverButton(i)
				else:
					self.wndItem.EnableCoverButton(i)
			
			## 자동물약 (HP: #72723 ~ #72726, SP: #72727 ~ #72730) 특수처리 - 아이템인데도 슬롯에 활성화/비활성화 표시를 위한 작업임 - [hyo]
			
			if constInfo.IS_AUTO_POTION(itemVnum):
				# metinSocket - [0] : 활성화 여부, [1] : 사용한 양, [2] : 최대 용량
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]

				if slotNumber >= player.INVENTORY_PAGE_SIZE * self.inventoryPageIndex:
					slotNumber -= player.INVENTORY_PAGE_SIZE * self.inventoryPageIndex
					
				isActivated = 0 != metinSocket[0]
				
				if isActivated:
					potionType = 0;
					if constInfo.IS_AUTO_POTION_HP(itemVnum):
						potionType = player.AUTO_POTION_TYPE_HP
					elif constInfo.IS_AUTO_POTION_SP(itemVnum):
						potionType = player.AUTO_POTION_TYPE_SP						
					
					usedAmount = int(metinSocket[1])
					totalAmount = int(metinSocket[2])					
					player.SetAutoPotionInfo(potionType, isActivated, (totalAmount - usedAmount), totalAmount, self.__InventoryLocalSlotPosToGlobalSlotPos(i))

					self.wndItem.ActivateSlot(slotNumber)
				else:
					self.wndItem.DeactivateSlot(slotNumber)
			
			# ##########################################################################################
			# starting app.ENABLE_NEW_PET_SYSTEM
			elif constInfo.IS_PET_ITEM(itemVnum):
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
				isActivated = 0 != metinSocket[0]
				if isActivated:
					self.wndItem.ActivateSlot(i)
				else:
					self.wndItem.DeactivateSlot(i)
			# ending app.ENABLE_NEW_PET_SYSTEM
			# ##########################################################################################

			elif app.ENABLE_EXTENDED_BLEND_AFFECT and constInfo.IS_BLEND_POTION(itemVnum) or constInfo.IS_EXTENDED_BLEND_POTION(itemVnum):
				metinSocket = [player.GetItemMetinSocket(slotNumber, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]

				if slotNumber >= player.INVENTORY_PAGE_SIZE * self.inventoryPageIndex:
					slotNumber -= player.INVENTORY_PAGE_SIZE * self.inventoryPageIndex

				isActivated = 0 != metinSocket[3]

				if constInfo.IS_EXTENDED_BLEND_POTION(itemVnum):
					r, g, b = (150.00 / 255.0), (80.00 / 255.0), (255.00 / 255.0) # rgb(150, 80, 255)
				else:
					r, g, b = (255.00 / 255.0), (255.00 / 255.0), (0.00 / 255.0) # rgb(255, 255, 0)

				if isActivated:
					self.wndItem.ActivateSlot(slotNumber, r, g, b, 1.0)
				else:
					self.wndItem.DeactivateSlot(slotNumber)

				self.wndItem.DisableCoverButton(i)
			else:
				slotClNumberChecked = False

				for q in xrange(changelook.WINDOW_MAX_MATERIALS):
					(isHere, iCell) = changelook.GetAttachedItem(q)
					if isHere:
						if iCell == slotNumber:
							self.wndItem.ActivateSlot(i, (238.00 / 255.0), (11.00 / 255.0), (11.00 / 255.0), 1.0)
							if not slotNumber in self.listAttachedCl:
								self.listAttachedCl.append(slotNumber)
							
							slotClNumberChecked = True
					else:
						if slotNumber in self.listAttachedCl and not slotClNumberChecked:
							self.wndItem.DeactivateSlot(i)
							self.listAttachedCl.remove(slotNumber)
					
				slotNumberChecked = False
				
				if app.ENABLE_SASH_SYSTEM:
					for j in xrange(sash.WINDOW_MAX_MATERIALS):
						(isHere, iCell) = sash.GetAttachedItem(j)
						if isHere:
							if iCell == slotNumber:
								self.wndItem.ActivateSlot(i, (36.00 / 255.0), (222.00 / 255.0), (3.00 / 255.0), 1.0)
								if not slotNumber in self.listAttachedSashs:
									self.listAttachedSashs.append(slotNumber)
								
								slotNumberChecked = True
						else:
							if slotNumber in self.listAttachedSashs and not slotNumberChecked:
								self.wndItem.DeactivateSlot(i)
								self.listAttachedSashs.remove(slotNumber)

				if not slotClNumberChecked and not slotNumberChecked:
					self.wndItem.DeactivateSlot(i)
	
			if app.ENABLE_PICKUP_FILTER and app.ENABLE_AUTO_PICKUP:
				if item.ITEM_TYPE_USE == item.GetItemType() and item.USE_AUTO_PICKUP == item.GetItemSubType():
					metinSocket = player.GetItemMetinSocket(slotNumber, 0)
					if slotNumber >= player.INVENTORY_PAGE_SIZE * self.inventoryPageIndex:
						slotNumber -= player.INVENTORY_PAGE_SIZE * self.inventoryPageIndex
					
					if metinSocket:
						self.wndItem.ActivateSlot(i)
					else:
						self.wndItem.DeactivateSlot(i)	
						
			if app.WJ_ENABLE_TRADABLE_ICON:
				self.RefreshMarkSlots(i)
				
		self.__RefreshHighlights()
		self.wndItem.RefreshSlot()

		if self.wndBelt:
			self.wndBelt.RefreshSlot()
		if app.WJ_ENABLE_TRADABLE_ICON:
			map(lambda wnd:wnd.RefreshLockedSlot(), self.bindWnds)

	def HighlightSlot(self, slot):
		if not slot in self.liHighlightedItems:
			self.liHighlightedItems.append(slot)
	
	def __RefreshHighlights(self):
		for i in xrange(player.INVENTORY_PAGE_SIZE):
			if app.ENABLE_SPECIAL_INVENTORY:
				if self.inventoryTypeIndex == player.INVENTORY_TYPE_INVENTORY:
					slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)
				else:
					slotNumber = self.__SpecialInventoryLocalSlotPosToGlobalSlotPos(i)
			else:
				slotNumber = self.__InventoryLocalSlotPosToGlobalSlotPos(i)

			if slotNumber in self.liHighlightedItems:
				self.wndItem.ActivateSlot(i)

	def RefreshEquipSlotWindow(self):
		getItemVNum=player.GetItemIndex
		getItemCount=player.GetItemCount
		setItemVNum=self.wndEquip.SetItemSlot
		for i in xrange(player.EQUIPMENT_PAGE_COUNT):
			slotNumber = player.EQUIPMENT_SLOT_START + i
			itemCount = getItemCount(slotNumber)
			if itemCount <= 1:
				itemCount = 0
			setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)
			if app.ENABLE_CHANGELOOK_SYSTEM:
				itemTransmutedVnum = player.GetItemTransmutation(slotNumber)
				if itemTransmutedVnum:
					self.wndEquip.DisableCoverButton(slotNumber)
				else:
					self.wndEquip.EnableCoverButton(slotNumber)
		
		if app.ENABLE_NEW_EQUIPMENT_SYSTEM:
			for i in xrange(player.NEW_EQUIPMENT_SLOT_COUNT):
				slotNumber = player.NEW_EQUIPMENT_SLOT_START + i
				itemCount = getItemCount(slotNumber)
				if itemCount <= 1:
					itemCount = 0
				setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)
				print "ENABLE_NEW_EQUIPMENT_SYSTEM", slotNumber, itemCount, getItemVNum(slotNumber)
				if app.ENABLE_CHANGELOOK_SYSTEM:
					itemTransmutedVnum = player.GetItemTransmutation(slotNumber)
					if itemTransmutedVnum:
						self.wndEquip.DisableCoverButton(slotNumber)
					else:
						self.wndEquip.EnableCoverButton(slotNumber)
		
		slotNumber = item.EQUIPMENT_PET
		itemCount = getItemCount(slotNumber)
		if itemCount <= 1:
			itemCount = 0
		setItemVNum(slotNumber, getItemVNum(slotNumber), itemCount)
		print "ENABLE_NEW_EQUIPMENT_SYSTEM", slotNumber, itemCount, getItemVNum(slotNumber)
		if app.ENABLE_CHANGELOOK_SYSTEM:
			itemTransmutedVnum = player.GetItemTransmutation(slotNumber)
			if itemTransmutedVnum:
				self.wndEquip.DisableCoverButton(slotNumber)
			else:
				self.wndEquip.EnableCoverButton(slotNumber)
		
		self.wndEquip.RefreshSlot()
		
		if self.wndCostume:
			self.wndCostume.RefreshCostumeSlot()
			
		if app.ENABLE_SHOW_CHEST_DROP and self.interface and self.interface.dlgChestDrop and self.interface.dlgChestDrop.IsShow():
			self.interface.dlgChestDrop.RefreshInvItemSlot()

	def RefreshItemSlot(self):
		self.RefreshEquipSlotWindow()
		if app.ENABLE_SPECIAL_INVENTORY:
			if self.inventoryTypeIndex == player.INVENTORY_TYPE_INVENTORY:
				self.RefreshBagSlotWindow()
			else:
				self.RefreshSpecialInventory()	
		else:
			self.RefreshBagSlotWindow()

	def RefreshStatus(self):
		money = player.GetElk()
		self.wndMoney.SetText(localeInfo.NumberToMoneyString(money))

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def SellItem(self):
		if self.sellingSlotitemIndex == player.GetItemIndex(self.sellingSlotNumber):
			if self.sellingSlotitemCount == player.GetItemCount(self.sellingSlotNumber):
				## 용혼석도 팔리게 하는 기능 추가하면서 인자 type 추가
				net.SendShopSellPacketNew(self.sellingSlotNumber, self.questionDialog.count, player.INVENTORY)
				snd.PlaySound("sound/ui/money.wav")
		self.OnCloseQuestionDialog()

	def OnDetachMetinFromItem(self):
		if None == self.questionDialog:
			return
			
		#net.SendItemUseToItemPacket(self.questionDialog.sourcePos, self.questionDialog.targetPos)		
		self.__SendUseItemToItemPacket(self.questionDialog.sourcePos, self.questionDialog.targetPos)
		self.OnCloseQuestionDialog()

	def OnCloseQuestionDialog(self):
		if not self.questionDialog:
			return
		
		self.questionDialog.Close()
		self.questionDialog = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)

	## Slot Event
	def SelectEmptySlot(self, selectedSlotPos):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return

		if app.ENABLE_SPECIAL_INVENTORY:
			if self.inventoryTypeIndex == player.INVENTORY_TYPE_INVENTORY:
				selectedSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(selectedSlotPos)
			else:
				selectedSlotPos = self.__SpecialInventoryLocalSlotPosToGlobalSlotPos(selectedSlotPos)
		else:
			selectedSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(selectedSlotPos)

		if mouseModule.mouseController.isAttached():

			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()
			attachedCount = mouseModule.mouseController.GetAttachedItemCount()

			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				itemCount = player.GetItemCount(attachedSlotPos)
				self.__SendMoveItemPacket(attachedSlotPos, selectedSlotPos, attachedCount)

				if item.IsRefineScroll(attachedItemIndex):
					self.wndItem.SetUseMode(FALSE)
					
			elif app.ENABLE_SWITCHBOT and player.SLOT_TYPE_SWITCHBOT == attachedSlotType:
				net.SendItemMovePacket(player.SWITCHBOT, attachedSlotPos, player.INVENTORY, selectedSlotPos, attachedCount)

			elif player.SLOT_TYPE_PRIVATE_SHOP == attachedSlotType:
				mouseModule.mouseController.RunCallBack("INVENTORY")

			elif player.SLOT_TYPE_SHOP == attachedSlotType:
				net.SendShopBuyPacket(attachedSlotPos)

			elif player.SLOT_TYPE_SAFEBOX == attachedSlotType:

				if player.ITEM_MONEY == attachedItemIndex:
					net.SendSafeboxWithdrawMoneyPacket(mouseModule.mouseController.GetAttachedItemCount())
					snd.PlaySound("sound/ui/money.wav")

				else:
					net.SendSafeboxCheckoutPacket(attachedSlotPos, selectedSlotPos)

			elif player.SLOT_TYPE_MALL == attachedSlotType:
				net.SendMallCheckoutPacket(attachedSlotPos, selectedSlotPos)

			mouseModule.mouseController.DeattachObject()

	def SelectItemSlot(self, itemSlotIndex):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS() == 1:
			return

		if app.ENABLE_SPECIAL_INVENTORY:
			if self.inventoryTypeIndex == player.INVENTORY_TYPE_INVENTORY:
				itemSlotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(itemSlotIndex)
			else:
				itemSlotIndex = self.__SpecialInventoryLocalSlotPosToGlobalSlotPos(itemSlotIndex)
		else:
			itemSlotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(itemSlotIndex)

		if mouseModule.mouseController.isAttached():
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemVID = mouseModule.mouseController.GetAttachedItemIndex()

			if player.SLOT_TYPE_INVENTORY == attachedSlotType:
				self.__DropSrcItemToDestItemInInventory(attachedItemVID, attachedSlotPos, itemSlotIndex)

			mouseModule.mouseController.DeattachObject()

		else:

			curCursorNum = app.GetCursor()
			if app.SELL == curCursorNum:
				self.__SellItem(itemSlotIndex)
				
			elif app.BUY == curCursorNum:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_BUY_INFO)

			elif shop.IsOpen() and app.IsPressed(app.DIK_LCONTROL):
				if not player.IsEquipmentSlot(itemSlotIndex):
					if shop.IsOpen():
						if not shop.IsPrivateShop():
							net.SendShopSellPacketNew(itemSlotIndex, player.GetItemCount(itemSlotIndex), player.INVENTORY)
			
			elif app.IsPressed(app.DIK_LALT):
				link = player.GetItemLink(itemSlotIndex)
				ime.PasteString(link)

			elif app.IsPressed(app.DIK_LSHIFT):
				itemCount = player.GetItemCount(itemSlotIndex)
				
				if itemCount > 1:
					self.dlgPickMoney.SetTitleName(localeInfo.PICK_ITEM_TITLE)
					self.dlgPickMoney.SetAcceptEvent(ui.__mem_func__(self.OnPickItem))
					self.dlgPickMoney.Open(itemCount)
					self.dlgPickMoney.itemGlobalSlotIndex = itemSlotIndex
				#else:
					#selectedItemVNum = player.GetItemIndex(itemSlotIndex)
					#mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum)

			elif app.IsPressed(app.DIK_LCONTROL):
				itemIndex = player.GetItemIndex(itemSlotIndex)

				if True == item.CanAddToQuickSlotItem(itemIndex):
					if self.inventoryTypeIndex == player.INVENTORY_TYPE_INVENTORY:
						player.RequestAddToEmptyLocalQuickSlot(player.INVENTORY_TYPE_INVENTORY, itemSlotIndex)
					elif self.inventoryTypeIndex == player.INVENTORY_TYPE_SKILLBOOK:
						player.RequestAddToEmptyLocalQuickSlot(player.INVENTORY_TYPE_SKILLBOOK, itemSlotIndex)
					elif self.inventoryTypeIndex == player.INVENTORY_TYPE_STONE:
						player.RequestAddToEmptyLocalQuickSlot(player.INVENTORY_TYPE_STONE, itemSlotIndex)
					elif self.inventoryTypeIndex == player.INVENTORY_TYPE_MATERIAL:
						player.RequestAddToEmptyLocalQuickSlot(player.INVENTORY_TYPE_MATERIAL, itemSlotIndex)
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.QUICKSLOT_REGISTER_DISABLE_ITEM)

			else:
				selectedItemVNum = player.GetItemIndex(itemSlotIndex)
				itemCount = player.GetItemCount(itemSlotIndex)
				mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_INVENTORY, itemSlotIndex, selectedItemVNum, itemCount)
				
				if self.__IsUsableItemToItem(selectedItemVNum, itemSlotIndex):				
					self.wndItem.SetUseMode(True)
				else:					
					self.wndItem.SetUseMode(False)

				snd.PlaySound("sound/ui/pick.wav")
				
	if app.ENABLE_NEW_PET_SYSTEM:
		def UseProteinOrTransportBox(self):
			self.__SendUseItemToItemPacket(self.questionDialog.src, self.questionDialog.dst)
			self.OnCloseQuestionDialog()

	def __DropSrcItemToDestItemInInventory(self, srcItemVID, srcItemSlotPos, dstItemSlotPos):
		if player.GetItemIndex(srcItemSlotPos) in [71084, 71085, 76013, 76014, 71051, 71052]:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)
			return
			
		if srcItemSlotPos == dstItemSlotPos:
			return
		
		if item.IsRefineScroll(srcItemVID):
			self.RefineItem(srcItemSlotPos, dstItemSlotPos)
			self.wndItem.SetUseMode(FALSE)

		elif item.IsMetin(srcItemVID):
			self.AttachMetinToItem(srcItemSlotPos, dstItemSlotPos)

		elif item.IsDetachScroll(srcItemVID):
			self.DetachMetinFromItem(srcItemSlotPos, dstItemSlotPos)

		elif item.IsKey(srcItemVID):
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)			

		elif (player.GetItemFlags(srcItemSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)

		elif item.GetUseType(srcItemVID) in self.USE_TYPE_TUPLE:
			self.__SendUseItemToItemPacket(srcItemSlotPos, dstItemSlotPos)			

		# ##########################################################################################
		# starting app.ENABLE_NEW_PET_SYSTEM
		elif srcItemVID == 55008 and player.GetItemIndex(dstItemSlotPos) >= 55701 and player.GetItemIndex(dstItemSlotPos) <= 55799:
			import uiPetIncubator
			self.petinc = uiPetIncubator.PetSystemRenewName(player.GetItemIndex(dstItemSlotPos), dstItemSlotPos, srcItemSlotPos)
			self.petinc.Show()
			self.petinc.SetTop()

		elif srcItemVID >= 55701 and srcItemVID <= 55799 and player.GetItemIndex(dstItemSlotPos) == 55002:
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText("Do you want to add this pet to the transport box?")
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.UseProteinOrTransportBox))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.src = srcItemSlotPos
			self.questionDialog.dst = dstItemSlotPos
			
		elif srcItemVID == 55002 and player.GetItemIndex(dstItemSlotPos) == 55002:
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText("Do you want to add this pet to a new transport box?")
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.UseProteinOrTransportBox))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.src = srcItemSlotPos
			self.questionDialog.dst = dstItemSlotPos
			
		elif srcItemVID == 55001 and player.GetItemIndex(dstItemSlotPos) >= 55701 and player.GetItemIndex(dstItemSlotPos) <= 55799:
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText("Do you want to feed it to your pet?")
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.UseProteinOrTransportBox))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.src = srcItemSlotPos
			self.questionDialog.dst = dstItemSlotPos
		# ending app.ENABLE_NEW_PET_SYSTEM
		# ##########################################################################################
		else:
			#snd.PlaySound("sound/ui/drop.wav")

			## 이동시킨 곳이 장착 슬롯일 경우 아이템을 사용해서 장착 시킨다 - [levites]
			if player.IsEquipmentSlot(dstItemSlotPos):

				## 들고 있는 아이템이 장비일때만
				if item.IsEquipmentVID(srcItemVID):
					self.__UseItem(srcItemSlotPos)

			else:
				self.__SendMoveItemPacket(srcItemSlotPos, dstItemSlotPos, 0)
				#net.SendItemMovePacket(srcItemSlotPos, dstItemSlotPos, 0)

	def __SellItem(self, itemSlotPos):
		if not player.IsEquipmentSlot(itemSlotPos):
			self.sellingSlotNumber = itemSlotPos
			itemIndex = player.GetItemIndex(itemSlotPos)
			itemCount = player.GetItemCount(itemSlotPos)
			
			
			self.sellingSlotitemIndex = itemIndex
			self.sellingSlotitemCount = itemCount

			item.SelectItem(itemIndex)
			## 안티 플레그 검사 빠져서 추가
			## 20140220
			if item.IsAntiFlag(item.ANTIFLAG_SELL):
				popup = uiCommon.PopupDialog()
				popup.SetText(localeInfo.SHOP_CANNOT_SELL_ITEM)
				popup.SetAcceptEvent(self.__OnClosePopupDialog)
				popup.Open()
				self.popup = popup
				return

			itemPrice = item.GetISellItemPrice()

			if item.Is1GoldItem():
				itemPrice = itemCount / itemPrice / 1
			else:
				itemPrice = itemPrice * itemCount / 1

			item.GetItemName(itemIndex)
			itemName = item.GetItemName()

			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.DO_YOU_SELL_ITEM(itemName, itemCount, itemPrice))
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.SellItem))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
			self.questionDialog.Open()
			self.questionDialog.count = itemCount
		
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)

	def __OnClosePopupDialog(self):
		self.pop = None

	def RefineItem(self, scrollSlotPos, targetSlotPos):

		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)

		if player.REFINE_OK != player.CanRefine(scrollIndex, targetSlotPos):
			return
					
		if app.ENABLE_REFINE_RENEWAL:
			constInfo.AUTO_REFINE_TYPE = 1
			constInfo.AUTO_REFINE_DATA["ITEM"][0] = scrollSlotPos
			constInfo.AUTO_REFINE_DATA["ITEM"][1] = targetSlotPos

		###########################################################
		self.__SendUseItemToItemPacket(scrollSlotPos, targetSlotPos)
		#net.SendItemUseToItemPacket(scrollSlotPos, targetSlotPos)
		return
		###########################################################

		###########################################################
		#net.SendRequestRefineInfoPacket(targetSlotPos)
		#return
		###########################################################

		result = player.CanRefine(scrollIndex, targetSlotPos)

		if player.REFINE_ALREADY_MAX_SOCKET_COUNT == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_MORE_SOCKET)

		elif player.REFINE_NEED_MORE_GOOD_SCROLL == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NEED_BETTER_SCROLL)

		elif player.REFINE_CANT_MAKE_SOCKET_ITEM == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_SOCKET_DISABLE_ITEM)

		elif player.REFINE_NOT_NEXT_GRADE_ITEM == result:
			#snd.PlaySound("sound/ui/jaeryun_fail.wav")
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_UPGRADE_DISABLE_ITEM)

		elif player.REFINE_CANT_REFINE_METIN_TO_EQUIPMENT == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_EQUIP_ITEM)

		if player.REFINE_OK != result:
			return

		self.refineDialog.Open(scrollSlotPos, targetSlotPos)

	def DetachMetinFromItem(self, scrollSlotPos, targetSlotPos):
		scrollIndex = player.GetItemIndex(scrollSlotPos)
		targetIndex = player.GetItemIndex(targetSlotPos)
		if app.ENABLE_SASH_SYSTEM:
			if not player.CanDetach(scrollIndex, targetSlotPos):
				item.SelectItem(scrollIndex)
				if item.GetValue(0) == sash.CLEAN_ATTR_VALUE0:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SASH_FAILURE_CLEAN)
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_METIN_INSEPARABLE_ITEM)
				
				return
		else:
			if not player.CanDetach(scrollIndex, targetSlotPos):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_METIN_INSEPARABLE_ITEM)
				return

		if app.ENABLE_CHANGELOOK_SYSTEM:
			if not player.CanDetach(scrollIndex, targetSlotPos):
				item.SelectItem(scrollIndex)
				if item.GetValue(0) == changelook.CLEAN_ATTR_VALUE0:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CHANGE_LOOK_FAILURE_CLEAN)
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_METIN_INSEPARABLE_ITEM)
				
				return
		else:
			if not player.CanDetach(scrollIndex, targetSlotPos):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_METIN_INSEPARABLE_ITEM)
				return

		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText(localeInfo.REFINE_DO_YOU_SEPARATE_METIN)
		if app.ENABLE_SASH_SYSTEM:
			item.SelectItem(targetIndex)
			if item.GetItemType() == item.ITEM_TYPE_COSTUME and item.GetItemSubType() == item.COSTUME_TYPE_SASH:
				item.SelectItem(scrollIndex)
				if item.GetValue(0) == sash.CLEAN_ATTR_VALUE0:
					self.questionDialog.SetText(localeInfo.SASH_DO_YOU_CLEAN)

		if app.ENABLE_CHANGELOOK_SYSTEM:
			item.SelectItem(targetIndex)
			if item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR or item.GetItemType() == item.ITEM_TYPE_COSTUME:
				item.SelectItem(scrollIndex)
				if item.GetValue(0) == changelook.CLEAN_ATTR_VALUE0:
					self.questionDialog.SetText(localeInfo.CHANGE_LOOK_DO_YOU_CLEAN)

		self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.OnDetachMetinFromItem))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnCloseQuestionDialog))
		self.questionDialog.Open()
		self.questionDialog.sourcePos = scrollSlotPos
		self.questionDialog.targetPos = targetSlotPos

	def AttachMetinToItem(self, metinSlotPos, targetSlotPos):
		metinIndex = player.GetItemIndex(metinSlotPos)
			
		targetIndex = player.GetItemIndex(targetSlotPos)

		item.SelectItem(metinIndex)
		itemName = item.GetItemName()

		result = player.CanAttachMetin(metinIndex, targetSlotPos)

		if player.ATTACH_METIN_NOT_MATCHABLE_ITEM == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_CAN_NOT_ATTACH(itemName))

		if player.ATTACH_METIN_NO_MATCHABLE_SOCKET == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_SOCKET(itemName))

		elif player.ATTACH_METIN_NOT_EXIST_GOLD_SOCKET == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_NO_GOLD_SOCKET(itemName))

		elif player.ATTACH_METIN_CANT_ATTACH_TO_EQUIPMENT == result:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.REFINE_FAILURE_EQUIP_ITEM)

		if player.ATTACH_METIN_OK != result:
			return

		self.attachMetinDialog.Open(metinSlotPos, targetSlotPos)


		
	def OverOutItem(self):
		self.wndItem.SetUsableItem(FALSE)
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()
			
	def OverInItem(self, overSlotPos):
		if app.ENABLE_SPECIAL_INVENTORY:
			if self.inventoryTypeIndex == player.INVENTORY_TYPE_INVENTORY:
				overSlotPosGlobal = self.__InventoryLocalSlotPosToGlobalSlotPos(overSlotPos)
			else:
				overSlotPosGlobal = self.__SpecialInventoryLocalSlotPosToGlobalSlotPos(overSlotPos)
		else:
			overSlotPosGlobal = self.__InventoryLocalSlotPosToGlobalSlotPos(overSlotPos)	
		self.wndItem.SetUsableItem(False)
		
		if overSlotPosGlobal in self.liHighlightedItems:
			self.liHighlightedItems.remove(overSlotPosGlobal)
			self.wndItem.DeactivateSlot(overSlotPos)
		
		if mouseModule.mouseController.isAttached():
			attachedItemType = mouseModule.mouseController.GetAttachedType()

			if player.SLOT_TYPE_INVENTORY == attachedItemType:
				
				attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
				attachedItemVNum = mouseModule.mouseController.GetAttachedItemIndex()
				
				if self.__CanUseSrcItemToDstItem(attachedItemVNum, attachedSlotPos, overSlotPosGlobal):
					self.wndItem.SetUsableItem(True)
					self.ShowToolTip(overSlotPosGlobal)
					return
		
		self.ShowToolTip(overSlotPosGlobal)
	'''
	def OverInItem(self, overSlotPos):
		overSlotPos = self.__InventoryLocalSlotPosToGlobalSlotPos(overSlotPos)
		self.wndItem.SetUsableItem(False)

		if mouseModule.mouseController.isAttached():
			attachedItemType = mouseModule.mouseController.GetAttachedType()
			if app.ENABLE_SPECIAL_STORAGE:
				if player.SLOT_TYPE_INVENTORY == attachedItemType or player.SLOT_TYPE_STONE_INVENTORY == attachedItemType:
					attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
					attachedItemVNum = mouseModule.mouseController.GetAttachedItemIndex()

					if self.__CanUseSrcItemToDstItem(attachedItemVNum, attachedSlotPos, overSlotPos):
						self.wndItem.SetUsableItem(True)
						self.wndItem.SetUseMode(True)
						self.ShowToolTip(overSlotPos)
						return
			else:
				if player.SLOT_TYPE_INVENTORY == attachedItemType:

					attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
					attachedItemVNum = mouseModule.mouseController.GetAttachedItemIndex()
					
					if self.__CanUseSrcItemToDstItem(attachedItemVNum, attachedSlotPos, overSlotPos):
						self.wndItem.SetUsableItem(True)
						self.ShowToolTip(overSlotPos)
						return
				
		self.ShowToolTip(overSlotPos)
	'''
		
	def __IsUsableItemToItem(self, srcItemVNum, srcSlotPos):
		if srcItemVNum >= 55701 and srcItemVNum <= 55705:
			return True
		
		if srcItemVNum == 55001:
			return True
			
		if item.IsRefineScroll(srcItemVNum):
			return TRUE
		elif item.IsMetin(srcItemVNum):
			return TRUE
		elif item.IsDetachScroll(srcItemVNum):
			return TRUE
		elif item.IsKey(srcItemVNum):
			return TRUE
		elif (player.GetItemFlags(srcSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			return TRUE
		# ###############################################################
		# starting app.ENABLE_NEW_PET_SYSTEM
		
		elif srcItemVNum >= 55701 and srcItemVNum <= 55799 or srcItemVNum == 55001 or srcItemVNum == 55002 or srcItemVNum == 55008:
			return True
		
		# ending app.ENABLE_NEW_PET_SYSTEM
		# ###############################################################
		else:
			if item.GetUseType(srcItemVNum) in self.USE_TYPE_TUPLE:
				return TRUE
			
		return FALSE

	def __CanUseSrcItemToDstItem(self, srcItemVNum, srcSlotPos, dstSlotPos):
		"대상 아이템에 사용할 수 있는가?"
		if player.GetItemIndex(srcSlotPos) in [71084, 71085, 76013, 76014, 71051, 71052]:
			if self.__CanChangeItemAttrList(dstSlotPos):
				return TRUE
		
		if srcSlotPos == dstSlotPos:
			return FALSE
				
		if srcItemVNum >= 55701 and  srcItemVNum <= 55705 and player.GetItemIndex(dstSlotPos) == 55036:			
			return True		
		
		if srcItemVNum == 55001 and player.GetItemIndex(dstSlotPos) >= 55701 and player.GetItemIndex(dstSlotPos) <= 55705:			
			return True
		
		if srcItemVNum == 71084:
			if self.__CanChangeItemAttrList(dstSlotPos):
				return TRUE

		if item.IsRefineScroll(srcItemVNum):
			if player.REFINE_OK == player.CanRefine(srcItemVNum, dstSlotPos):
				return TRUE
		elif item.IsMetin(srcItemVNum):
			if player.ATTACH_METIN_OK == player.CanAttachMetin(srcItemVNum, dstSlotPos):
				return TRUE
		elif item.IsDetachScroll(srcItemVNum):
			if player.DETACH_METIN_OK == player.CanDetach(srcItemVNum, dstSlotPos):
				return TRUE
		elif item.IsKey(srcItemVNum):
			if player.CanUnlock(srcItemVNum, dstSlotPos):
				return TRUE

		elif (player.GetItemFlags(srcSlotPos) & ITEM_FLAG_APPLICABLE) == ITEM_FLAG_APPLICABLE:
			return TRUE

		# ###############################################################
		# starting app.ENABLE_NEW_PET_SYSTEM
		elif srcItemVNum >= 55701 and srcItemVNum <= 55799 and player.GetItemIndex(dstSlotPos) == 55002:			
			return True	

		elif srcItemVNum == 55002 and player.GetItemIndex(dstSlotPos) == 55002:			
			return True		
		
		elif srcItemVNum == 55001 and player.GetItemIndex(dstSlotPos) >= 55701 and player.GetItemIndex(dstSlotPos) <= 55799:			
			return True
			
		elif srcItemVNum == 55008 and player.GetItemIndex(dstSlotPos) >= 55701 and player.GetItemIndex(dstSlotPos) <= 55799:			
			return True
		# ending app.ENABLE_NEW_PET_SYSTEM
		# ###############################################################
		else:
			useType=item.GetUseType(srcItemVNum)

			if "USE_CLEAN_SOCKET" == useType:
				if self.__CanCleanBrokenMetinStone(dstSlotPos):
					return TRUE
			elif "USE_CHANGE_ATTRIBUTE" == useType:
				if self.__CanChangeItemAttrList(dstSlotPos):
					return TRUE
			elif "USE_ADD_ATTRIBUTE" == useType:
				if self.__CanAddItemAttr(dstSlotPos):
					return TRUE
			elif "USE_ADD_ATTRIBUTE2" == useType:
				if self.__CanAddItemAttr(dstSlotPos):
					return TRUE
			elif "USE_ADD_ACCESSORY_SOCKET" == useType:
				if self.__CanAddAccessorySocket(dstSlotPos):
					return TRUE
			elif "USE_PUT_INTO_ACCESSORY_SOCKET" == useType:								
				if self.__CanPutAccessorySocket(dstSlotPos, srcItemVNum):
					return TRUE;
			elif "USE_PUT_INTO_BELT_SOCKET" == useType:								
				dstItemVNum = player.GetItemIndex(dstSlotPos)
				print "USE_PUT_INTO_BELT_SOCKET", srcItemVNum, dstItemVNum

				item.SelectItem(dstItemVNum)
		
				if item.ITEM_TYPE_BELT == item.GetItemType():
					return TRUE
					
			elif app.ENABLE_NEW_ADDON_SWITCHER and "USE_CHANGE_SPECIAL_FKS_ATTRIBUTE" == useType or "USE_CHANGE_SPECIAL_DSS_ATTRIBUTE" == useType:
				if self.__CanChangeSpecialAddonItemAttrList(dstSlotPos):
					return True
					
			elif app.ENABLE_COSTUME_EXTENDED_RECHARGE:
				if "USE_TIME_CHARGE_PER" == useType:
					if self.__CanExtendTime(dstSlotPos):
						return True
				elif "USE_TIME_CHARGE_FIX" == useType:
					if self.__CanExtendTime(dstSlotPos):
						return True
				else:
					pass

		return FALSE

	def __CanCleanBrokenMetinStone(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return FALSE

		item.SelectItem(dstItemVNum)
		
		if item.ITEM_TYPE_WEAPON != item.GetItemType():
			return FALSE

		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemMetinSocket(dstSlotPos, i) == constInfo.ERROR_METIN_STONE:
				return TRUE

		return FALSE

	def __CanChangeItemAttrList(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return FALSE

		item.SelectItem(dstItemVNum)
		
		if not item.GetItemType() in (item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR):	 
			return FALSE

		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemAttribute(dstSlotPos, i) != 0:
				return TRUE

		return FALSE

	def __CanPutAccessorySocket(self, dstSlotPos, mtrlVnum):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return FALSE

		item.SelectItem(dstItemVNum)

		if item.GetItemType() != item.ITEM_TYPE_ARMOR:
			return FALSE

		if not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
			return FALSE

		curCount = player.GetItemMetinSocket(dstSlotPos, 0)
		maxCount = player.GetItemMetinSocket(dstSlotPos, 1)

		if mtrlVnum != constInfo.GET_ACCESSORY_MATERIAL_VNUM(dstItemVNum, item.GetItemSubType()):
			return FALSE
		
		if curCount>=maxCount:
			return FALSE

		return TRUE

	def __CanAddAccessorySocket(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return FALSE

		item.SelectItem(dstItemVNum)

		if item.GetItemType() != item.ITEM_TYPE_ARMOR:
			return FALSE

		if not item.GetItemSubType() in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):
			return FALSE

		curCount = player.GetItemMetinSocket(dstSlotPos, 0)
		maxCount = player.GetItemMetinSocket(dstSlotPos, 1)
		
		ACCESSORY_SOCKET_MAX_SIZE = 3
		if maxCount >= ACCESSORY_SOCKET_MAX_SIZE:
			return FALSE

		return TRUE

	def __CanAddItemAttr(self, dstSlotPos):
		dstItemVNum = player.GetItemIndex(dstSlotPos)
		if dstItemVNum == 0:
			return FALSE

		item.SelectItem(dstItemVNum)
		
		if not item.GetItemType() in (item.ITEM_TYPE_WEAPON, item.ITEM_TYPE_ARMOR):	 
			return FALSE
			
		attrCount = 0
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			if player.GetItemAttribute(dstSlotPos, i) != 0:
				attrCount += 1

		if attrCount<4:
			return TRUE
								
		return FALSE
		
	if app.ENABLE_COSTUME_EXTENDED_RECHARGE:
		def __CanExtendTime(self, dstSlotPos):
			dstItemVNum = player.GetItemIndex(dstSlotPos)
			if dstItemVNum == 0:
				return False

			item.SelectItem(dstItemVNum)

			if item.GetItemType() != item.ITEM_TYPE_COSTUME:
				return False

			if app.ENABLE_SASH_SYSTEM:
				if item.GetItemSubType() == item.COSTUME_TYPE_SASH:
					return False

			metinSlot = [player.GetItemMetinSocket(dstSlotPos, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
			leftSec = max(0, metinSlot[0] - app.GetGlobalTimeStamp())

			if leftSec >= item.MIN_INFINITE_DURATION:
				return False

			return True

	def ShowToolTip(self, slotIndex):
		if None != self.tooltipItem:
			self.tooltipItem.SetInventoryItem(slotIndex)
			if self.interface.dlgExchange.IsShow():
				self.tooltipItem.AppendTradeableInformation()

	def OnTop(self):
		if None != self.tooltipItem:
			self.tooltipItem.SetTop()
		if app.WJ_ENABLE_TRADABLE_ICON:
			map(lambda wnd:wnd.RefreshLockedSlot(), self.bindWnds)
			self.RefreshMarkSlots()
			
	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def UseItemSlot(self, slotIndex):
		if constInfo.GET_ITEM_QUESTION_DIALOG_STATUS():
			return

		if app.ENABLE_SPECIAL_INVENTORY:
			if self.inventoryTypeIndex == player.INVENTORY_TYPE_INVENTORY:		
				slotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(slotIndex)
			else:
				slotIndex = self.__SpecialInventoryLocalSlotPosToGlobalSlotPos(slotIndex)
		else:
			slotIndex = self.__InventoryLocalSlotPosToGlobalSlotPos(slotIndex)

		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			if self.wndDragonSoulRefine.IsShow():
				self.wndDragonSoulRefine.AutoSetItem((player.INVENTORY, slotIndex), 1)
				return

		if app.ENABLE_SASH_SYSTEM:
			if self.isShowSashWindow():
				sash.Add(player.INVENTORY, slotIndex, 255)
				return

		if app.ENABLE_CHANGELOOK_SYSTEM:
			if self.isShowChangeLookWindow():
				changelook.Add(player.INVENTORY, slotIndex, 255)
				return

		if app.IsPressed(app.DIK_LCONTROL):	
			itemVnum = player.GetItemIndex(slotIndex)
			item.SelectItem(itemVnum)
			
			if app.ENABLE_PICKUP_FILTER and app.ENABLE_AUTO_PICKUP and item.USE_AUTO_PICKUP == item.GetItemSubType():
				import uiitempickupfilter
				self.wndItemPickupFilter = uiitempickupfilter.OpenItemPickupFilterDialog()
				self.wndItemPickupFilter.Open(slotIndex, player.GetItemMetinSocket(slotIndex, 1))
				return	
				
		if self.interface.dlgExchange.IsShow() and (app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)):
			item.SelectItem(player.GetItemIndex(slotIndex))
			emptyExchangeSlots = self.GetExchangeEmptyItemPos(item.GetItemSize()[1])
			if emptyExchangeSlots == -1:
				return
			if item.IsAntiFlag(item.ANTIFLAG_GIVE):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.EXCHANGE_CANNOT_GIVE)
				return
			net.SendExchangeItemAddPacket(player.SLOT_TYPE_INVENTORY, slotIndex, emptyExchangeSlots[0])
			
		elif self.interface.dlgShop.IsShow() and (app.IsPressed(app.DIK_LCONTROL) or app.IsPressed(app.DIK_RCONTROL)):
			item.SelectItem(player.GetItemIndex(slotIndex))
			if item.IsAntiFlag(item.ANTIFLAG_SELL):
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.SHOP_CANNOT_SELL_ITEM)
				return
			net.SendShopSellPacketNew(slotIndex, 0, player.SLOT_TYPE_INVENTORY)
		else:
			self.__UseItem(slotIndex)
			mouseModule.mouseController.DeattachObject()
			self.OverOutItem()
			
	def GetExchangeEmptyItemPos(self, itemHeight):
		inventorySize = exchange.EXCHANGE_ITEM_MAX_NUM
		inventoryWidth = 6
		GetBlockedSlots = lambda slot, size: [slot+(round*inventoryWidth) for round in xrange(size)] 
		blockedSlots = [element for sublist in [GetBlockedSlots(slot, item.GetItemSize(item.SelectItem(exchange.GetItemVnumFromSelf(slot)))[1]) for slot in xrange(inventorySize) if exchange.GetItemVnumFromSelf(slot) != 0] for element in sublist] 
		freeSlots = [slot for slot in xrange(inventorySize) if not slot in blockedSlots and not True in [e in blockedSlots for e in [slot+(round*inventoryWidth) for round in xrange(itemHeight)]]] 
		return [freeSlots, -1][len(freeSlots) == 0]
		
	def __UseItem(self, slotIndex):
		ItemVNum = player.GetItemIndex(slotIndex)
		item.SelectItem(ItemVNum)
		if item.IsFlag(item.ITEM_FLAG_CONFIRM_WHEN_USE):
			self.questionDialog = uiCommon.QuestionDialog()
			self.questionDialog.SetText(localeInfo.INVENTORY_REALLY_USE_ITEM)
			self.questionDialog.SetAcceptEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnAccept))
			self.questionDialog.SetCancelEvent(ui.__mem_func__(self.__UseItemQuestionDialog_OnCancel))
			self.questionDialog.Open()
			self.questionDialog.slotIndex = slotIndex
			constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
		
		elif app.ENABLE_RENDER_TARGET_SYSTEM and app.IsPressed(app.DIK_LSHIFT):
			itemTransmutedVnum = player.GetItemTransmutation(slotIndex)
			if itemTransmutedVnum:
				self.tooltipItem.ModelPreviewFull(itemTransmutedVnum)
			else:
				self.tooltipItem.ModelPreviewFull(ItemVNum)
		
		elif app.ENABLE_SHOW_CHEST_DROP and player.GetItemTypeBySlot(slotIndex) == item.ITEM_TYPE_GIFTBOX:
			if self.interface:
				if self.interface.dlgChestDrop:
					if not self.interface.dlgChestDrop.IsShow():
						self.interface.dlgChestDrop.Open(slotIndex)
						net.SendChestDropInfo(slotIndex)
		else:
			if app.ENABLE_RENDER_TARGET_SYSTEM:
				wndTargetRender = renderTargetExtension.RenderTarget.Get()
				if wndTargetRender.IsShow():
					wndTargetRender.DisplayUser(player.GetRace(), True)
			if item.GetItemType() == 23 or ItemVNum == 27987:
				if app.IsPressed(app.DIK_LCONTROL):
					for i in xrange(player.GetItemCount(slotIndex)):
						self.__SendUseItemPacket(slotIndex)
				else:
					self.__SendUseItemPacket(slotIndex)
			else:
				self.__SendUseItemPacket(slotIndex)
			#net.SendItemUsePacket(slotIndex)	

	def __UseItemQuestionDialog_OnCancel(self):
		self.OnCloseQuestionDialog()

	def __UseItemQuestionDialog_OnAccept(self):
		self.__SendUseItemPacket(self.questionDialog.slotIndex)
		self.OnCloseQuestionDialog()		

	def __SendUseItemToItemPacket(self, srcSlotPos, dstSlotPos):
		# 개인상점 열고 있는 동안 아이템 사용 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemUseToItemPacket(srcSlotPos, dstSlotPos)

	def __SendUseItemPacket(self, slotPos):
		# 개인상점 열고 있는 동안 아이템 사용 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.USE_ITEM_FAILURE_PRIVATE_SHOP)
			return
			
		itemb = player.GetItemIndex(slotPos)
		if app.LWT_BUFF_UPDATE:	
			if constInfo.IS_BUFFI(itemb) and player.GetStatus(player.LEVEL) < 5:
				popup = uiCommon.PopupDialog()
				popup.SetText(translate.buffilevel)
				popup.SetAcceptEvent(self.__OnClosePopupDialog)
				popup.Open()
				self.popup = popup
				return
		if int(itemb) == 92015:
			self.sorusoruyoz = uiCommon.QuestionDialog2()
			self.sorusoruyoz.SetText1(translate.buffip)
			self.sorusoruyoz.SetText2(translate.buffipsor)
			self.sorusoruyoz.SetAcceptEvent(lambda arg=TRUE: self.sorgula(slotPos))
			self.sorusoruyoz.SetCancelEvent(lambda arg=FALSE: self.kkkd(2))
			self.sorusoruyoz.Open()
			return
		net.SendItemUsePacket(slotPos)
	def kkkd(self, l):
		self.sorusoruyoz.Close()
	def sorgula(self, pos):
		self.sorusoruyoz.Close()
		net.SendItemUsePacket(pos)
	
	def __SendMoveItemPacket(self, srcSlotPos, dstSlotPos, srcItemCount):
		# 개인상점 열고 있는 동안 아이템 사용 방지
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.MOVE_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemMovePacket(srcSlotPos, dstSlotPos, srcItemCount)
	
	def SetDragonSoulRefineWindow(self, wndDragonSoulRefine):
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoulRefine = wndDragonSoulRefine

	if app.ENABLE_CHANGELOOK_SYSTEM:
		def SetChangeLookWindow(self, wndChangeLook):
			self.wndChangeLook = wndChangeLook

		def isShowChangeLookWindow(self):
			if self.wndChangeLook:
				if self.wndChangeLook.IsShow():
					return 1
			
			return 0

	if app.ENABLE_SASH_SYSTEM:
		def SetSashWindow(self, wndSashCombine, wndSashAbsorption):
			self.wndSashCombine = wndSashCombine
			self.wndSashAbsorption = wndSashAbsorption

		def isShowSashWindow(self):
			if self.wndSashCombine:
				if self.wndSashCombine.IsShow():
					return 1

			if self.wndSashAbsorption:
				if self.wndSashAbsorption.IsShow():
					return 1
			
			return 0

	def OnMoveWindow(self, x, y):
#		print "Inventory Global Pos : ", self.GetGlobalPosition()
		if self.wndBelt:
#			print "Belt Global Pos : ", self.wndBelt.GetGlobalPosition()
			self.wndBelt.AdjustPositionAndSize()
						
		if app.ENABLE_SPECIAL_INVENTORY and self.wndInventoryTypeTab:
			self.wndInventoryTypeTab.AdjustPosition()
			
	if app.ENABLE_HIDE_COSTUME_SYSTEM:
		def RefreshVisibleCostume(self):
			if self.wndCostume:
				self.wndCostume.RefreshVisibleCostume()
			else:
				self.wndCostume = CostumeWindow(self)
				self.wndCostume.RefreshVisibleCostume()

	if app.ENABLE_NEW_ADDON_SWITCHER:
		def __CanChangeSpecialAddonItemAttrList(self, dstSlotPos):
			dstItemVNum = player.GetItemIndex(dstSlotPos)
			if dstItemVNum == 0:
				return False

			item.SelectItem(dstItemVNum)
			if item.ITEM_TYPE_WEAPON != item.GetItemType():
				return False

			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				if player.GetItemAttribute(dstSlotPos, i) != 0:
					return True

			return False
			