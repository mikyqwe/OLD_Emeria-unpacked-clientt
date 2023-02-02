import ui
import item
import net
import constInfo
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import wndMgr
import app
import renderTarget
import grp
import chat 

class ItemFinder(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.name_item = ""
		self.tab = {}
		self.LoadWindow()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Show(self):
		self.marire = 0
		self.LoadWindow()
		self.ListBox=ui.ListBoxEx_dd()
		self.ListBox.SetParent(self.bg_finder)
		self.ListBox.SetPosition(70, 200)
		self.ListBox.SetSize(214, 275)
		self.ListBox.SetItemSize(185, 130)
		self.ListBox.SetItemStep(134)
		self.ListBox.SetViewItemCount(2)
		self.ListBox.SetScrollBar(self.ScrollBar)
		self.ListBox.SetParentbut(self.bg_finder)
		self.ListBox.Show()
		self.SetCenterPosition()
		self.ModelPreviewBoard.Hide()
		self.ModelPreview.Hide()
		ui.ScriptWindow.Show(self)
		
	def AppendInfo(self, index, name_monster, prob, activi, vnum, count, name_item):
		self.ListBox.SetButtons(index, name_monster,prob, activi, vnum, count, name_item)

	def LoadWindow(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "apollo_scripts/itemfinder.py")
		except:
			import exception
			exception.Abort("itemfinder.LoadWindow.LoadObject")
		try:
			self.titleBar = self.GetChild("TitleBar")
			self.board = self.GetChild("board")
			self.editline = self.GetChild("ItemNameValue")
			self.searchbutton = self.GetChild("search_button")
			self.clearbutton = self.GetChild("clear_button")
			self.ScrollBar = self.GetChild("ScrollBar")
			self.bg_finder = self.GetChild("bg_findere")
		except:
			import exception
			exception.Abort("itemfinder.__LoadWindow.BindObject")
	
		self.titleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.RENDER_TARGET_INDEX = 3

		self.ModelPreviewBoard = ui.ThinBoard()
		self.ModelPreviewBoard.SetParent(self)
		self.ModelPreviewBoard.SetSize(200+10, 230+30-12)
		self.ModelPreviewBoard.SetPosition(235, 120)
		self.ModelPreviewBoard.Show()

		self.ModelPreview = ui.RenderTarget()
		self.ModelPreview.SetParent(self.ModelPreviewBoard)
		self.ModelPreview.SetSize(200, 230)
		self.ModelPreview.SetPosition(5, 22-12)
		self.ModelPreview.SetRenderTarget(self.RENDER_TARGET_INDEX)
		self.ModelPreview.Show()
		
		self.searchbutton.SetEvent(ui.__mem_func__(self.OnSearch))
		self.clearbutton.SetEvent(ui.__mem_func__(self._StergeText))


	def Close(self):
		self.__ModelPreviewClose()
		self.Hide()

	def OnUpdate(self):
		if app.IsPressed(app.DIK_RETURN) and self.editline.IsFocus():
			self.OnSearch()
		if constInfo.finder_counts > 0:
			##self.ScrollBar.SetMiddleBarSize(float(2) / float(constInfo.finder_counts))
			self.ScrollBar.Show()
		else:
			self.ScrollBar.Hide()
		for i in range(constInfo.finder_counts):
			if self.ListBox.GetDown(i) == True:
				self.__ModelPreview(self.GetVnumPreview(i))
			
	def GetVnumPreview(self, i):
		try:
			return int(constInfo.finder_items[int(i)]["iMobVnum"])
		except KeyError:
			return 0
	
	def OnSearch(self):
		if self.editline.GetText() == None or self.editline.GetText() == "":
			return 
		constInfo.finder_counts = 0
		self.ScrollBar.SetPos(0.0)
		self.ListBox.RemoveAllItems()
		item_name = str(self.editline.GetText())
		item_name.replace(" ", "_")
		net.SendChatPacket("/cauta_drop %s" % (str(item_name.replace(" ", "_"))))

	def __ModelPreview(self, Vnum):
		self.ModelPreviewBoard.Show()
		self.ModelPreview.Show()
		renderTarget.SetBackground(self.RENDER_TARGET_INDEX, "d:/ymir work/ui/game/myshop_deco/model_view_bg.sub")
		renderTarget.SetVisibility(self.RENDER_TARGET_INDEX, True)
		renderTarget.SelectModel(self.RENDER_TARGET_INDEX, Vnum)

	def _StergeText(self):
		self.editline.SetText("")
	
	def __ModelPreviewClose(self):
		self.RENDER_TARGET_INDEX = 3

		if self.ModelPreviewBoard:
			self.ModelPreviewBoard.Hide()
			self.ModelPreview.Hide()

			self.ModelPreviewBoard = None
			self.ModelPreview = None

			renderTarget.SetVisibility(self.RENDER_TARGET_INDEX, False)

	def Destroy(self):
		self.ClearDictionary()
