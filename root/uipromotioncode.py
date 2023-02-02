import localeInfo
import constInfo
import net
import ui

class PromotionCodeWindow(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.LoadWindow()
		
	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)
			
	def LoadWindow(self):      
		self.SetSize(250, 100)
		for flag in ("movable", "float"):
			self.AddFlag(flag)
		self.SetTitleName("Promotion-Code")
		self.SetCenterPosition()
		self.SetCloseEvent(self.Close)
				
		self.LoadUI()
		self.Hide()
		
	def LoadUI(self):
		#EditLine/Slotbar
		self.slotBar = ui.SlotBar()
		self.slotBar.SetParent(self)
		self.slotBar.SetSize(125, 15)
		self.slotBar.SetPosition((self.GetWidth() - self.slotBar.GetWidth()) / 2, 40)
		self.slotBar.Show()
		
		self.editLine = ui.EditLine()
		self.editLine.SetParent(self.slotBar)
		self.editLine.SetSize(100, 15)
		self.editLine.SetMax(16)
		self.editLine.SetText("")
		self.editLine.SetPosition(1, 1)
		self.editLine.Show()	
			
		self.acceptButton = ui.Button()
		self.acceptButton.SetParent(self)
		self.acceptButton.SetUpVisual("d:/ymir work/promocode/promcode_button.png")
		self.acceptButton.SetOverVisual("d:/ymir work/promocode/promcode_button_hover.png")
		self.acceptButton.SetDownVisual("d:/ymir work/promocode/promcode_button_down.png")
		self.acceptButton.SetPosition((self.GetWidth() - self.acceptButton.GetWidth()) / 2, 65)
		self.acceptButton.SetEvent(ui.__mem_func__(self.Accept))	
		self.acceptButton.Show()

	def Accept(self):
		net.SendChatPacket("/use_promotion_code %s" % self.editLine.GetText())
		self.Close()
		
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True
		
