import app
import ui
import os
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import uiScriptLocale

FILE_NAME_LEN = 20 
DEFAULT_THEMA = localeInfo.MUSIC_METIN2_DEFAULT_THEMA

class Item(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=fileName
		self.textLine=self.__CreateTextLine(fileName[:FILE_NAME_LEN])

	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)

	def GetText(self):
		return self.text

	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 6*len(self.textLine.GetText()) + 4, height)

	def IsEmpty(self):
		if len(self.itemList)==0:
			return 1

		return 0

	def __CreateTextLine(self, fileName):
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(0, 0)

		textLine.SetText(fileName)
		textLine.Show()
		return textLine

class PopupDialog(ui.ScriptWindow):
	def __init__(self, parent):
		print "PopupDialog::PopupDialog()"
		ui.ScriptWindow.__init__(self)

		self.__Load()
		self.__Bind()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print "PopupDialog::~PopupDialog()"

	def __Load(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PopupDialog.py")
		except:
			import exception
			exception.Abort("PopupDialog.__Load")

	def __Bind(self):
		try:
			self.textLine=self.GetChild("message")
			self.okButton=self.GetChild("accept")
		except:
			import exception
			exception.Abort("PopupDialog.__Bind")

		self.okButton.SAFE_SetEvent(self.__OnOK)

	def Open(self, msg):
		self.textLine.SetText(msg)
		self.SetCenterPosition()
		self.Show()
		self.SetTop()

	def __OnOK(self):
		self.Hide()

class FileListDialog(ui.ScriptWindow):
	def __init__(self):
		print "FileListDialog::FileListDialog()"
		ui.ScriptWindow.__init__(self)

		self.isLoaded=0
		self.selectEvent=None
		self.languageListBox=None

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		print "FileListDialog::~FileListDialog()"

	def Show(self):
		if self.isLoaded == 0:
			self.isLoaded = 1
			self.__Load()

		ui.ScriptWindow.Show(self)

	def Open(self):
		self.Show()

		self.SetCenterPosition()
		self.SetTop()

		if self.languageListBox.IsEmpty():
			self.__PopupMessage("No non-default language available")

	def Close(self):
		self.popupDialog.Hide()
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def SAFE_SetSelectEvent(self, event):
		self.selectEvent = ui.__mem_func__(event)

	def __CreateLanguageListBox(self):
		languageListBox = ui.ListBoxEx()
		languageListBox.SetParent(self)
		
		if localeInfo.IsARABIC():
			languageListBox.SetPosition(self.GetWidth() - languageListBox.GetWidth() - 10, 50)
		else:
			languageListBox.SetPosition(15, 50)

		languageListBox.Show()
		return languageListBox

	def __Load(self):
		self.popupDialog = PopupDialog(self)

		if localeInfo.IsARABIC():
			self.__Load_LoadScript(uiScriptLocale.LOCALE_UISCRIPT_PATH + "MusicListWindow.py")
		else:
			self.__Load_LoadScript("UIScript/MusicListWindow.py")

		self.__Load_BindObject()

		self.refreshButton.SAFE_SetEvent(self.__OnRefresh)
		self.cancelButton.SAFE_SetEvent(self.__OnCancel)
		self.okButton.SAFE_SetEvent(self.__OnOK)
		self.board.SetCloseEvent(ui.__mem_func__(self.__OnCancel))
		self.board.SetTitleName("Language Select")
		self.UpdateRect()

		self.__RefreshLangList()

	def __Load_LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("LanguageListBox.__Load")

	def __Load_BindObject(self):
		try:
			self.languageListBox=self.__CreateLanguageListBox()
			self.languageListBox.SetScrollBar(self.GetChild("ScrollBar"))

			self.board=self.GetChild("board")
			self.okButton=self.GetChild("ok")
			self.cancelButton=self.GetChild("cancel")
			self.refreshButton=self.GetChild("refresh")

			self.popupText = self.popupDialog.GetChild("message")

		except:
			import exception
			exception.Abort("LanguageListBox.__Bind")

	def __PopupMessage(self, msg):
		self.popupDialog.Open(msg)

	def __OnOK(self):
		selItem = self.languageListBox.GetSelectedItem()
		if selItem:
			if self.selectEvent:
				self.selectEvent(selItem.GetText())

			#self.Hide()
		else:
			self.__PopupMessage("No language selected!")

	def __OnCancel(self):
		self.Hide()

	def __OnRefresh(self):
		self.__RefreshLangList()

	def __RefreshLangList(self):
		self.__ClearLanguageList()
		self.__AppendLanguage("de")
		self.__AppendLanguageList()

	def __ClearLanguageList(self):
		self.languageListBox.RemoveAllItems()

	def WalkDir(self, top):
		join, isdir = os.path.join, os.path.isdir

		try:
			# Note that listdir and error are globals in this module due
			# to earlier import-*.
			names = os.listdir(top)
		except:
			return None

		dirs = []
		for name in names:
			if isdir(join(top, name)):
				dirs.append(name)
				
		return dirs
			
	def __AppendLanguageList(self):
			self.__AppendLanguage("de")
			self.__AppendLanguage("en")
			self.__AppendLanguage("ro")
			self.__AppendLanguage("pl")
			self.__AppendLanguage("cz")
			self.__AppendLanguage("hu")
			self.__AppendLanguage("tr")
			self.__AppendLanguage("es")
			self.__AppendLanguage("pt")
			self.__AppendLanguage("it")

	def __ReplaceCodeWitName(self, code):
		langCodeReplace = {
			"de"		:	localeInfo.LANG_DEFAULT,
			"en"		:	localeInfo.LANG_ENGLISH,
			"tr"		:	localeInfo.LANG_TURKEY,
			"ro"		:	localeInfo.LANG_ROMANIAN,
			"pl"		:	localeInfo.LANG_POLISH,
			"hu"		:	localeInfo.LANG_HUNGARIAN,
			"es"		:	localeInfo.LANG_SPANISH,
			"cz"		:	localeInfo.LANG_CZECH,
			"pt"		:	localeInfo.LANG_PORTUGUESE,
			"it"		:	localeInfo.LANG_ITALIAN,
		}
		try:
			return langCodeReplace[code]
		except:
			return code
	
	def __AppendLanguage(self, folderName):
		self.languageListBox.AppendItem(Item(self.__ReplaceCodeWitName(folderName)))


