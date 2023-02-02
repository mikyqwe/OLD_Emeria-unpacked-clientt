import ui,dbg,app,net,os

class Dialog1(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(202, 206)
		self.Board.SetCenterPosition()
		self.Board.AddFlag('movable')
		self.Board.AddFlag('float')
		self.Board.SetTitleName('Multilanguage-System')
		self.Board.SetCloseEvent(self.Close)
		self.Board.Show()
		self.comp = Component()

		self.img1 = self.comp.ExpandedImage(self.Board , 163, 54, 'firewall/lenguaje_venta/en.tga')
		self.img2 = self.comp.ExpandedImage(self.Board , 163, 85, 'firewall/lenguaje_venta/es.tga')
		self.img3 = self.comp.ExpandedImage(self.Board , 163, 116, 'firewall/lenguaje_venta/pt.tga')
		self.img4 = self.comp.ExpandedImage(self.Board , 163, 148, 'firewall/lenguaje_venta/de.tga')
		self.base = self.comp.Button(self.Board, 'Englisch', '', 9, 49, self.base_func, 'firewall/lenguaje_venta/boton_base1.tga', 'firewall/lenguaje_venta/boton_base2.tga', 'firewall/lenguaje_venta/boton_base3.tga')
		self.base1 = self.comp.Button(self.Board, 'Spanisch', '', 9, 80, self.base1_func, 'firewall/lenguaje_venta/boton_base1.tga', 'firewall/lenguaje_venta/boton_base2.tga', 'firewall/lenguaje_venta/boton_base3.tga')
		self.base2 = self.comp.Button(self.Board, 'Portugisisch', '', 9, 112, self.base2_func, 'firewall/lenguaje_venta/boton_base1.tga', 'firewall/lenguaje_venta/boton_base2.tga', 'firewall/lenguaje_venta/boton_base3.tga')
		self.base3 = self.comp.Button(self.Board, 'Deutsch', '', 9, 142, self.base3_func, 'firewall/lenguaje_venta/boton_base1.tga', 'firewall/lenguaje_venta/boton_base2.tga', 'firewall/lenguaje_venta/boton_base3.tga')
		self.base.SetToolTipText('Client auf Englisch Uebersetzen')
		self.base1.SetToolTipText('Client auf Spanisch Uebersetzen')
		self.base2.SetToolTipText('Client auf Portugisisch Uebersetzen')
		self.base3.SetToolTipText('Client auf Deutsch Uebersetzen')
	
	def base_func(self):
		os.remove('lang/idioma.txt')
		file = open('lang/idioma.txt', 'a')
		file.write("Espain") #Pones el idioma ejemplo español
		file.close()
		net.SendChatPacket("/idioma_ingles")
		net.ExitApplication()
		os.system('start Elendos.exe')
	
	def base1_func(self):
		os.remove('lang/idioma.txt')
		file = open('lang/idioma.txt', 'a')
		file.write("Espain")#Pones el idioma ejemplo ingles
		file.close()
		net.SendChatPacket("/idioma_espanol")
		net.ExitApplication()
		os.system('start Elendos.exe')
	
	def base2_func(self):
		os.remove('lang/idioma.txt')
		file = open('lang/idioma.txt', 'a')
		file.write("Espain")#Pones el idioma ejemplo ingles
		file.close()
		net.SendChatPacket("/idioma_portuges")
		net.ExitApplication()
		os.system('start Elendos.exe')
	
	def base3_func(self):
		os.remove('lang/idioma.txt')
		file = open('lang/idioma.txt', 'a')
		file.write("Espain")#Pones el idioma ejemplo ingles
		file.close()
		net.SendChatPacket("/idioma_rumano")
		net.ExitApplication()
		os.system('start Elendos.exe')
	
	
	def Close(self):
		self.Board.Hide()
		
class Component:
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button

	def ToggleButton(self, parent, buttonName, tooltipText, x, y, funcUp, funcDown, UpVisual, OverVisual, DownVisual):
		button = ui.ToggleButton()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetToggleUpEvent(funcUp)
		button.SetToggleDownEvent(funcDown)
		return button

	def EditLine(self, parent, editlineText, x, y, width, heigh, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(1, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetText(editlineText)
		Value.Show()
		return SlotBar, Value

	def TextLine(self, parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Show()
		return textline

	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)

	def SliderBar(self, parent, sliderPos, func, x, y):
		Slider = ui.SliderBar()
		if parent != None:
			Slider.SetParent(parent)
		Slider.SetPosition(x, y)
		Slider.SetSliderPos(sliderPos / 100)
		Slider.Show()
		Slider.SetEvent(func)
		return Slider

	def ExpandedImage(self, parent, x, y, img):
		image = ui.ExpandedImageBox()
		if parent != None:
			image.SetParent(parent)
		image.SetPosition(x, y)
		image.LoadImage(img)
		image.Show()
		return image

	def ComboBox(self, parent, text, x, y, width):
		combo = ui.ComboBox()
		if parent != None:
			combo.SetParent(parent)
		combo.SetPosition(x, y)
		combo.SetSize(width, 15)
		combo.SetCurrentItem(text)
		combo.Show()
		return combo

	def ThinBoard(self, parent, moveable, x, y, width, heigh, center):
		thin = ui.ThinBoard()
		if parent != None:
			thin.SetParent(parent)
		if moveable == TRUE:
			thin.AddFlag('movable')
			thin.AddFlag('float')
		thin.SetSize(width, heigh)
		thin.SetPosition(x, y)
		if center == TRUE:
			thin.SetCenterPosition()
		thin.Show()
		return thin

	def Gauge(self, parent, width, color, x, y):
		gauge = ui.Gauge()
		if parent != None:
			gauge.SetParent(parent)
		gauge.SetPosition(x, y)
		gauge.MakeGauge(width, color)
		gauge.Show()
		return gauge

	def ListBoxEx(self, parent, x, y, width, heigh):
		bar = ui.Bar()
		if parent != None:
			bar.SetParent(parent)
		bar.SetPosition(x, y)
		bar.SetSize(width, heigh)
		bar.SetColor(0x77000000)
		bar.Show()
		ListBox=ui.ListBoxEx()
		ListBox.SetParent(bar)
		ListBox.SetPosition(0, 0)
		ListBox.SetSize(width, heigh)
		ListBox.Show()
		scroll = ui.ScrollBar()
		scroll.SetParent(ListBox)
		scroll.SetPosition(width-15, 0)
		scroll.SetScrollBarSize(heigh)
		scroll.Show()
		ListBox.SetScrollBar(scroll)
		return bar, ListBox
