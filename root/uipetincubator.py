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


class PetSystemIncubator(ui.ScriptWindow):
	
	def __init__(self, type, pet, cost):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()
		self.LoadPetIncubatorImg(type, pet, cost)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
	
	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/PetHatchingWindow.py")
		except:
			import exception
			exception.Abort("PetHatchingWindow.LoadWindow.LoadObject")
			
		try:
			self.board = self.GetChild("board")
			self.boardtitle = self.GetChild("PetHatching_TitleBar")
			self.boardtitlename = self.GetChild("TitleName")
			
			self.petimg = self.GetChild("HatchingItemSlot")
			self.costText = self.GetChild("HatchingMoney")
			self.petname = self.GetChild("pet_name")
			self.HatchingButton = self.GetChild("HatchingButton")
			
			self.boardtitlename.SetText(uiScriptLocale.PET_HATCHING_WINDOW_TITLE)
			self.petname.SetText("")
			self.petname.SetFocus()
			
			
			#Event
			self.boardtitle.SetCloseEvent(ui.__mem_func__(self.Close))
			self.HatchingButton.SetEvent(ui.__mem_func__(self.RequestHatching))
			
			
		except:
			import exception
			exception.Abort("PetHatchingWindow.LoadWindow.BindObject")
			
	def LoadPetIncubatorImg(self, type, pet, cost):
		self.petimg.SetItemSlot(0, (int(pet)), 0)
		self.petimg.SetAlwaysRenderCoverButton(0, TRUE)
		self.costText.SetText(uiScriptLocale.GUILD_BUILDING_PRICE+": "+str(localeInfo.NumberToMoneyString(int(cost))))
		
		#self.petimg.SetSlotBaseImage("icon/item/"+petarryimg[new_pet], 0, 0, 0, 0)
		
	def RequestHatching(self):
		if self.petname.GetText() == "" or len(self.petname.GetText()) < 4:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "The name for the pet is invalid.")
			return

		import chr
		chr.RequestPetName(self.petname.GetText())
		self.Close()


class PetSystemRenewName(ui.ScriptWindow):
	def __init__(self, petItemVnum, petitem, scrollitem):
		ui.ScriptWindow.__init__(self)
		self.__LoadWindow()
		self.petItem = petitem
		self.scrollItem = scrollitem
		self.LoadPetIncubatorImg(petItemVnum)

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		ui.ScriptWindow.Show(self)

	def Close(self):
		self.Hide()
		self.petItem = -1
		self.scrollItem = -1
	
	def __LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/PetHatchingWindow.py")
		except:
			import exception
			exception.Abort("PetHatchingWindow.LoadWindow.LoadObject")
			
		try:
			self.board = self.GetChild("board")
			self.boardtitle = self.GetChild("PetHatching_TitleBar")
			self.boardtitlename = self.GetChild("TitleName")
			
			self.petimg = self.GetChild("HatchingItemSlot")
			self.costText = self.GetChild("HatchingMoney")
			self.petname = self.GetChild("pet_name")
			self.HatchingButton = self.GetChild("HatchingButton")
			
			self.HatchingButton.SetText(uiScriptLocale.PET_NAME_CHANGE_WINDOW_TITLE)
			self.boardtitlename.SetText(uiScriptLocale.PET_NAME_CHANGE_WINDOW_TITLE)
			
			self.petname.SetText("")
			self.petname.SetFocus()
			
			#Event
			self.boardtitle.SetCloseEvent(ui.__mem_func__(self.Close))
			self.HatchingButton.SetEvent(ui.__mem_func__(self.RequestHatching))
			
			
		except:
			import exception
			exception.Abort("PetHatchingWindow.LoadWindow.BindObject")
			
	def LoadPetIncubatorImg(self, petItemVnum):
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "[Pet-Incubator] "+petarryname[int(new_pet)]+".")
		self.petimg.SetItemSlot(0, (int(petItemVnum)), 0)
		self.petimg.SetAlwaysRenderCoverButton(0, TRUE)
		#self.costText.SetText(uiScriptLocale.GUILD_BUILDING_PRICE+": "+str(localeInfo.NumberToMoneyString(int(cost))))
		
		#self.petimg.SetSlotBaseImage("icon/item/"+petarryimg[new_pet], 0, 0, 0, 0)
		
	def RequestHatching(self):
		if self.petname.GetText() == "" or len(self.petname.GetText()) < 4:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "The name for the pet is invalid.")
			return

		import chr
		chr.RenewPetName(self.petname.GetText(), self.petItem, self.scrollItem)
		self.Close()
