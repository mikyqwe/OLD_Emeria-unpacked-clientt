import dbg
import player
import item
import net
import snd
import ui
import uiToolTip
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import app
import mouseModule

class AttachMetinDialog(ui.ScriptWindow):
	if app.WJ_ENABLE_TRADABLE_ICON:  
		def __init__(self, wndInventory):
			ui.ScriptWindow.__init__(self)
			self.__LoadScript()

			self.metinItemPos = 0
			self.targetItemPos = 0
			self.wndInventory = wndInventory
			if app.ENABLE_SPECIAL_INVENTORY:
				self.lockedItems = {i:(player.INVENTORY_TYPE_INVENTORY, -1,-1) for i in range(2)}
			else:
				self.lockedItems = {i:(-1,-1) for i in range(2)}
	else:
		def __init__(self):
			ui.ScriptWindow.__init__(self)
			self.__LoadScript()

			self.metinItemPos = 0
			self.targetItemPos = 0

	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/attachstonedialog.py")

		except:
			import exception
			exception.Abort("AttachStoneDialog.__LoadScript.LoadObject")

		try:
			self.board = self.GetChild("Board")
			self.titleBar = self.GetChild("TitleBar")
			self.metinImage = self.GetChild("MetinImage")
			self.GetChild("AcceptButton").SetEvent(ui.__mem_func__(self.Accept))
			self.GetChild("CancelButton").SetEvent(ui.__mem_func__(self.Close))
		except:
			import exception
			exception.Abort("AttachStoneDialog.__LoadScript.BindObject")

		oldToolTip = uiToolTip.ItemToolTip()
		oldToolTip.SetParent(self)
		oldToolTip.SetPosition(15, 38)
		oldToolTip.SetFollow(FALSE)
		oldToolTip.Show()
		self.oldToolTip = oldToolTip

		newToolTip = uiToolTip.ItemToolTip()
		newToolTip.SetParent(self)
		newToolTip.SetPosition(230 + 20, 38)
		newToolTip.SetFollow(FALSE)
		newToolTip.Show()
		self.newToolTip = newToolTip

		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
			
		self.ClearDictionary()
		self.board = 0
		self.titleBar = 0
		self.metinImage = 0
		self.toolTip = 0
		if app.WJ_ENABLE_TRADABLE_ICON:  
			self.wndInventory = 0

	def CanAttachMetin(self, slot, metin):
		if item.METIN_NORMAL == metin:
			if player.METIN_SOCKET_TYPE_SILVER == slot or player.METIN_SOCKET_TYPE_GOLD == slot:
				return TRUE

		elif item.METIN_GOLD == metin:
			if player.METIN_SOCKET_TYPE_GOLD == slot:
				return TRUE

	def Open(self, metinItemPos, targetItemPos):
		self.metinItemPos = metinItemPos
		self.targetItemPos = targetItemPos

		metinIndex = player.GetItemIndex(metinItemPos)
			
		itemIndex = player.GetItemIndex(targetItemPos)
		self.oldToolTip.ClearToolTip()
		self.newToolTip.ClearToolTip()

		item.SelectItem(metinIndex)

		## Metin Image
		try:
			self.metinImage.LoadImage(item.GetIconImageFileName())
		except:
			dbg.TraceError("AttachMetinDialog.Open.LoadImage - Failed to find item data")

		## Old Item ToolTip
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(targetItemPos, i))
		self.oldToolTip.AddItemData(itemIndex, metinSlot)

		## New Item ToolTip
		item.SelectItem(metinIndex)
		metinSubType = item.GetItemSubType()

		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(targetItemPos, i))
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			slotData = metinSlot[i]
			if self.CanAttachMetin(slotData, metinSubType):
				metinSlot[i] = metinIndex
				break
		self.newToolTip.AddItemData(itemIndex, metinSlot)

		self.UpdateDialog()
		self.SetTop()
		self.Show()
		if app.WJ_ENABLE_TRADABLE_ICON:  
			self.SetCantMouseEventSlot(0, self.metinItemPos)
			self.SetCantMouseEventSlot(1, self.targetItemPos)

	def UpdateDialog(self):
		newWidth = self.newToolTip.GetWidth() + 230 + 15 + 20
		newHeight = self.newToolTip.GetHeight() + 98

		if localeInfo.IsARABIC():
			self.board.SetPosition( newWidth, 0 )

			(x,y) = self.titleBar.GetLocalPosition()
			self.titleBar.SetPosition( newWidth - 15, y )

		self.board.SetSize(newWidth, newHeight)
		self.titleBar.SetWidth(newWidth-15)
		self.SetSize(newWidth, newHeight)

		(x, y) = self.GetLocalPosition()
		self.SetPosition(x, y)

	def Accept(self):
		net.SendItemUseToItemPacket(self.metinItemPos, self.targetItemPos)
		snd.PlaySound("sound/ui/metinstone_insert.wav")
		self.Close()

	def Close(self):
		if app.WJ_ENABLE_TRADABLE_ICON:  
			self.SetCanMouseEventSlot(0, self.metinItemPos)
			self.SetCanMouseEventSlot(1, self.targetItemPos)
		self.Hide()

	if app.WJ_ENABLE_TRADABLE_ICON:  
		def SetCanMouseEventSlot(self, what, slotIndex):
			if app.ENABLE_SPECIAL_INVENTORY:
				invenType = player.GetSpecialInventoryTypeByGlobalSlot(slotIndex)
				if invenType == player.INVENTORY_TYPE_INVENTORY:
					itemInvenPage = slotIndex / player.INVENTORY_PAGE_SIZE
					localSlotPos = slotIndex - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
				else:
					(specialSlotStart, specialSlotEnd) = player.GetSpecialInventoryRange(invenType)
					specialInventorySlot = slotIndex - specialSlotStart
					itemInvenPage = specialInventorySlot / player.INVENTORY_PAGE_SIZE
					localSlotPos = specialInventorySlot - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
					
				self.lockedItems[what] = (player.INVENTORY_TYPE_INVENTORY, -1, -1)

				if invenType == self.wndInventory.GetInventoryType() and itemInvenPage == self.wndInventory.GetInventoryPageIndex() and self.IsShow():
					self.wndInventory.wndItem.SetCanMouseEventSlot(localSlotPos)
			else:
				itemInvenPage = slotIndex / player.INVENTORY_PAGE_SIZE
				localSlotPos = slotIndex - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
				self.lockedItems[what] = (-1, -1)

				if itemInvenPage == self.wndInventory.GetInventoryPageIndex():
					self.wndInventory.wndItem.SetCanMouseEventSlot(localSlotPos)

		def SetCantMouseEventSlot(self, what, slotIndex):
			if app.ENABLE_SPECIAL_INVENTORY:
				invenType = player.GetSpecialInventoryTypeByGlobalSlot(slotIndex)
				if invenType == player.INVENTORY_TYPE_INVENTORY:
					itemInvenPage = slotIndex / player.INVENTORY_PAGE_SIZE
					localSlotPos = slotIndex - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
				else:
					(specialSlotStart, specialSlotEnd) = player.GetSpecialInventoryRange(invenType)
					specialInventorySlot = slotIndex - specialSlotStart
					itemInvenPage = specialInventorySlot / player.INVENTORY_PAGE_SIZE
					localSlotPos = specialInventorySlot - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
					
				self.lockedItems[what] = (invenType, itemInvenPage, localSlotPos)

				if invenType == self.wndInventory.GetInventoryType() and itemInvenPage == self.wndInventory.GetInventoryPageIndex() and self.IsShow():
					self.wndInventory.wndItem.SetCantMouseEventSlot(localSlotPos)
			else:
				itemInvenPage = slotIndex / player.INVENTORY_PAGE_SIZE
				localSlotPos = slotIndex - (itemInvenPage * player.INVENTORY_PAGE_SIZE)
				self.lockedItems[what] = (itemInvenPage, localSlotPos)

				if itemInvenPage == self.wndInventory.GetInventoryPageIndex():
					self.wndInventory.wndItem.SetCantMouseEventSlot(localSlotPos)

		def RefreshLockedSlot(self):
			if self.wndInventory:
				if app.ENABLE_SPECIAL_INVENTORY:
					for what, (invenType, itemInvenPage, itemSlotPos) in self.lockedItems.items():
						if self.wndInventory.GetInventoryType() == invenType and self.wndInventory.GetInventoryPageIndex() == itemInvenPage:
							self.wndInventory.wndItem.SetCantMouseEventSlot(itemSlotPos)
				else:
					for what, (itemInvenPage, itemSlotPos) in self.lockedItems.items():
						if self.wndInventory.GetInventoryPageIndex() == itemInvenPage:
							self.wndInventory.wndItem.SetCantMouseEventSlot(itemSlotPos)

				self.wndInventory.wndItem.RefreshSlot()