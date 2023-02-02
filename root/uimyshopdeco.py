import ui
import chat
import wndMgr
import net
import constInfo

class UiShopDeco(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadWindow()
		self.shop = 0
		self.decoration = 0
		self.npc=[30000,30002,30003,30004,30005,30006,30007,30008],
		self.ModuleEx()
		self.__Procces(0,"Default")

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "d:/ymir work/ui/myshopdecorationwindows.py")

		except:
			import exception
			exception.Abort("UiShopDeco.LoadWindow")

		try:
			
			self.name = self.GetChild("ModelName")
			self.cancel = self.GetChild("CancelButton")
			self.send = self.GetChild("CompleteButton")
			self.GetChild("MyShopTitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.send.SetEvent(self.__OkProcces)
			self.cancel.SetEvent(self.Close)

		except:
			import exception
			exception.Abort("UiShopDecoModules.LoadWindow")

	def ModuleEx(self):
		numb = 0
		self.buttons = {}
		self.buttons1 = {}
		self.button_x = [
		[[25,40,"Default"]],
		[[25,40+27,"1001 Nights"]],
		[[25,40+27+27,"BBQ King"]],
		[[25,40+27+27+27,"Treasure Hunter"]],
		[[25,40+27+27+27+27,"Frugal Flame"]],
		[[25,40+27+27+27+27+27,"Arms Dealer"]],
		[[25,40+27+27+27+27+27+27,"Armour Dealership"]],
		[[25,40+27+27+27+27+27+27+27,"Alchemist"]]
		]


		self.bg = ui.ExpandedImageBox()
		self.bg.SetParent(self)
		self.bg.SetPosition(194,65)
		self.bg.LoadImage("d:/ymir work/render_test/render_elendosfiles.tga")
		self.bg.Show()
			
		self.iconshop = ui.ImageBox()
		self.iconshop.SetParent(self.bg)
		self.iconshop.SetPosition(5,30)
		self.iconshop.LoadImage("d:/ymir work/images/30000.tga")
		self.iconshop.SetWindowHorizontalAlignCenter()
		self.iconshop.SetWindowVerticalAlignCenter()
		self.iconshop.Show()

		for ar in self.button_x:
			self.buttons[numb] = ui.RadioButton()
			self.buttons[numb].SetParent(self)
			self.buttons[numb].SetPosition(ar[0][0],ar[0][1])
			self.buttons[numb].SetUpVisual("d:/ymir work/offline_shop_deco_new/neuer_schop_button_normal.tga")
			self.buttons[numb].SetOverVisual("d:/ymir work/offline_shop_deco_new/neuer_schop_button_hover.tga")
			self.buttons[numb].SetDownVisual("d:/ymir work/offline_shop_deco_new/neuer_schop_button_down.tga")
			self.buttons[numb].SetText(ar[0][2])
			self.buttons[numb].SetEvent(self.__Procces,numb,ar[0][2])
			self.buttons[numb].Show()
			numb +=1

		self.npc_button = (
			self.buttons[0],
			self.buttons[1],
			self.buttons[2],
			self.buttons[3],
			self.buttons[4],
			self.buttons[5],
			self.buttons[6],
			self.buttons[7],
		)	

	def __Procces(self,index,name):
		for btn in self.npc_button:
			btn.SetUp()
		self.npc_button[index].Down()
		self.name.SetText(name)
		self.shop = index
		i_position = [[1,30],[5,30],[4,30],[2,30],[0,30],[-3,28],[2,30],[-1,30]]
		self.iconshop.LoadImage("d:/ymir work/images/"+str(self.npc[0][index])+".tga")
		self.iconshop.SetPosition(i_position[index][0],i_position[index][1])
		self.__ThinDecoration(0)

	def __ThinDecoration(self,index):
		t_board = [ui.ThinBoardNorm()]
		t_position = [[34,23]]
		self.thinboard = t_board[index]
		self.thinboard.SetParent(self.bg)
		self.thinboard.SetPosition(t_position[index][0],t_position[index][1])
		self.thinboard.SetSize(170)
		self.thinboard.Show()
		self.send.Show()

	def __OkProcces(self):	
		net.SendChatPacket("/shop_decoration %d" % (self.npc[0][self.shop]))
		wndMgr.Hide(self.hWnd)

	def OnPressEscapeKey(self):
		self.Close()
		return True
		
	def OnPressExitKey(self):
		self.Close()
		return True

	def Close(self):
		wndMgr.Hide(self.hWnd)	
