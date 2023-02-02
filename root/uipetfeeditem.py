import os
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
import localeInfo
import constInfo
import ime
import wndMgr
import uiToolTip

class PetFeedWindow(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.arryfeed = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
		self.LoadWindow()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		ui.ScriptWindow.Show(self)

			
	def Close(self):
		for x in range(len(self.arryfeed)):
			self.arryfeed[x] = -1
			self.petslot.ClearSlot(x)
			self.petslot.RefreshSlot()
		self.Hide()
		constInfo.FEEDWINDOWITEM = 0
		constInfo.FEEDWINDOWITEMCLOSED = 1
	
	def Destroy(self):
		self.Hide()
		
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/PetFeedWindowItem.py")
		except:
			import exception
			exception.Abort("PetFeedWindow.LoadWindow.LoadObject")
			
		try:
			self.tooltipItem = uiToolTip.ItemToolTip()
			self.tooltipItem.Hide()
			
			self.petfeed = self.GetChild("board")
			self.closebtn = self.GetChild("PetFeed_TitleBar")
			self.petslot = self.GetChild("FeedItemSlot")
			self.feedbtn = self.GetChild("FeedButton")
			
			##PetSlot
			
			self.petslot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptySlot))
			self.petslot.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
			self.petslot.SetUnselectItemSlotEvent(ui.__mem_func__(self.UseItemSlot))
			self.petslot.SetUseSlotEvent(ui.__mem_func__(self.UseItemSlot))
			
			self.petslot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			self.petslot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
			
			##Event secondari
			
			self.feedbtn.SetEvent(ui.__mem_func__(self.SendPetItem))
			self.closebtn.SetCloseEvent(self.Close)
			
			
		except:
			import exception
			exception.Abort("PetFeedWindow.LoadWindow.BindObject")
	
	def SelectEmptySlot(self, selectedSlotPos):	
			
		if mouseModule.mouseController.isAttached():

			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			attachedItemCount = mouseModule.mouseController.GetAttachedItemCount()
			attachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()
			selectedItemVNum = player.GetItemIndex(player.INVENTORY, attachedSlotPos)
		
			if selectedItemVNum >= 77760 and selectedItemVNum <= 77763:
				if not attachedSlotPos in self.arryfeed:
					itemCount = player.GetItemCount(attachedSlotPos)
					attachedCount = mouseModule.mouseController.GetAttachedItemCount()
					self.arryfeed[selectedSlotPos] = attachedSlotPos
					self.petslot.SetItemSlot(selectedSlotPos, attachedItemIndex, attachedItemCount)
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "You can only put pet food in these slots")

			mouseModule.mouseController.DeattachObject()
	
	def SelectItemSlot(self, itemSlotIndex):
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "Select"+str(itemSlotIndex))
		self.arryfeed[itemSlotIndex] = -1
		self.petslot.ClearSlot(itemSlotIndex)
		self.petslot.RefreshSlot()
	
	def UseItemSlot(self, slotIndex):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "Select"+str(slotIndex))
	
	def OverOutItem(self):
		self.petslot.SetUsableItem(False)
		if None != self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def OverInItem(self, overSlotPos):
		if None != self.tooltipItem:
			slot_pos = self.arryfeed[overSlotPos]
			self.ShowToolTip(slot_pos)

	def ShowToolTip(self, slotIndex):
		if None != self.tooltipItem:
			self.tooltipItem.SetInventoryItem(slotIndex)

	def SendPetItem(self):
		for i in range(len(self.arryfeed)):
			if self.arryfeed[i] != -1:
				net.SendChatPacket("/cubepetadd a %d %d" % (i, self.arryfeed[i]))
		net.SendChatPacket("/feedcubepet %d" % (constInfo.FEEDWINDOWITEM))
		# for x in range(len(self.arryfeed)):
			# self.arryfeed[x] = -1
			# self.petslot.ClearSlot(x)
			# self.petslot.RefreshSlot()

	def OnUpdate(self):
		for x in range(len(self.arryfeed)):
			if self.arryfeed[x] != -1:
				selectedItemVNum = player.GetItemIndex(player.INVENTORY, self.arryfeed[x])
				itemCount = player.GetItemCount(self.arryfeed[x])
				self.petslot.SetItemSlot(x, selectedItemVNum, itemCount)