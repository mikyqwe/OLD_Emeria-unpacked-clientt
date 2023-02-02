import net
import app
import ui
import uiOption
import uiachievementsystem

import uiSystemOption
import uiGameOption
import uiScriptLocale
import networkModule
import constInfo
import localeInfo as _localeInfo
if app.ENABLE_PATCHNOTE_WINDOW:
	import uiPatchnotes
localeInfo = _localeInfo.localeInfo()

SYSTEM_MENU_FOR_PORTAL = FALSE

###################################################################################################
## System
class SystemDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Initialize()
	
	def __Initialize(self):
		self.eventOpenHelpWindow = None
		self.systemOptionDlg = None
		self.gameOptionDlg = None
		
		
	def LoadDialog(self):	
		if SYSTEM_MENU_FOR_PORTAL:
			self.__LoadSystemMenu_ForPortal()
		else:
			self.__LoadSystemMenu_Default()
			
	def __LoadSystemMenu_Default(self):
		pyScrLoader = ui.PythonScriptLoader()
		if constInfo.IN_GAME_SHOP_ENABLE:
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "SystemDialog.py")
		else:
			pyScrLoader.LoadScriptFile(self, "uiscript/systemdialog.py")

		self.GetChild("system_option_button").SAFE_SetEvent(self.__ClickSystemOptionButton)
		self.GetChild("game_option_button").SAFE_SetEvent(self.__ClickGameOptionButton)
		self.GetChild("change_button").SAFE_SetEvent(self.__ClickChangeCharacterButton)
		self.GetChild("logout_button").SAFE_SetEvent(self.__ClickLogOutButton)
		self.GetChild("exit_button").SAFE_SetEvent(self.__ClickExitButton)
		self.GetChild("help_button").SAFE_SetEvent(self.__ClickHelpButton)
		self.GetChild("cancel_button").SAFE_SetEvent(self.Close)
		if app.ENABLE_PATCHNOTE_WINDOW:
			self.wndPatchnotes = uiPatchnotes.PatchNoteWindow()
			self.GetChild("patchnotes_button").SAFE_SetEvent(self.__ClickPatchnotesButton)
		# self.GetChild("achievement_button").SAFE_SetEvent(self.__ClickAchievementButton)
		self.GetChild("achievement_button").SAFE_SetEvent(self.__ClickAchievementButton)
		self.GetChild("achievement_button").SetText("Change channel")

		if constInfo.IN_GAME_SHOP_ENABLE:
			self.GetChild("mall_button").SAFE_SetEvent(self.__ClickInGameShopButton)
		

	def __LoadSystemMenu_ForPortal(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/systemdialog_forportal.py")

		self.GetChild("system_option_button").SAFE_SetEvent(self.__ClickSystemOptionButton)
		self.GetChild("game_option_button").SAFE_SetEvent(self.__ClickGameOptionButton)
		self.GetChild("change_button").SAFE_SetEvent(self.__ClickChangeCharacterButton)
		self.GetChild("exit_button").SAFE_SetEvent(self.__ClickExitButton)
		self.GetChild("help_button").SAFE_SetEvent(self.__ClickHelpButton)
		self.GetChild("cancel_button").SAFE_SetEvent(self.Close)
		# self.GetChild("achievement_button").SAFE_SetEvent(self.__ClickAchievementButton)
		

	def Destroy(self):
		self.ClearDictionary()
		
		if self.gameOptionDlg:
			self.gameOptionDlg.Destroy()
			
		if self.systemOptionDlg:
			self.systemOptionDlg.Destroy()
			
		self.__Initialize()

	def SetOpenHelpWindowEvent(self, event):
		self.eventOpenHelpWindow = event

	def OpenDialog(self):
		self.Show()

	def __ClickChangeCharacterButton(self):
		self.Close()

		net.ExitGame()
		
	if app.ENABLE_PATCHNOTE_WINDOW:
		def __ClickPatchnotesButton(self):
			self.Close()
			self.wndPatchnotes.Show()
			self.wndPatchnotes.SetTop()

	def __OnClosePopupDialog(self):
		self.popup = None		

	def __ClickLogOutButton(self):
		if SYSTEM_MENU_FOR_PORTAL: 
			if app.loggined:
				self.Close()
				net.ExitApplication()
			else:
				self.Close()
				net.LogOutGame()
		else:
			self.Close()
			net.LogOutGame()


	def __ClickExitButton(self):
		self.Close()
		app.Exit()
		
	def __ClickAchievementButton(self):
		self.Close()
		import chchanger
		chchanger.ChannelBoard().Show()
		
	def __ClickSystemOptionButton(self):
		self.Close()

		if not self.systemOptionDlg:
			self.systemOptionDlg = uiSystemOption.OptionDialog()

		self.systemOptionDlg.Show()

	def __ClickGameOptionButton(self):
		self.Close()

		if not self.gameOptionDlg:
			self.gameOptionDlg = uiGameOption.OptionDialog()

		self.gameOptionDlg.Show()

	
	def __ClickHelpButton(self):
		self.Close()

		if None != self.eventOpenHelpWindow:
			self.eventOpenHelpWindow()

	def __ClickInGameShopButton(self):
		self.Close()
		#import event
		#constInfo.ITEMSHOP["questCMD"] = 'LOAD#'+str(constInfo.ITEMSHOP['tableUpdate'])
		#event.QuestButtonClick(int(constInfo.ITEMSHOP["qid"]))
		net.SendChatPacket("/in_game_mall")

	def Close(self):
		self.Hide()
		return TRUE

	def RefreshMobile(self):
		if self.gameOptionDlg:
			self.gameOptionDlg.RefreshMobile()
		#self.optionDialog.RefreshMobile()

	def OnMobileAuthority(self):
		if self.gameOptionDlg:
			self.gameOptionDlg.OnMobileAuthority()
		#self.optionDialog.OnMobileAuthority()

	def OnBlockMode(self, mode):
		uiGameOption.blockMode = mode
		if self.gameOptionDlg:
			self.gameOptionDlg.OnBlockMode(mode)
		#self.optionDialog.OnBlockMode(mode)

	def OnChangePKMode(self):
		if self.gameOptionDlg:
			self.gameOptionDlg.OnChangePKMode()
		#self.optionDialog.OnChangePKMode()
	
	def OnPressExitKey(self):
		self.Close()
		return TRUE

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE



