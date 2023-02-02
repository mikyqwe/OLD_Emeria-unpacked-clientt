import ui
import wndMgr
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import app
import net
import dbg
import player
import chat
import snd
import grp
import multifarmblock

class MouseReflector(ui.Window):
	def __init__(self, parent):
		ui.Window.__init__(self)
		self.SetParent(parent)
		self.AddFlag("not_pick")
		self.width = self.height = 0
		self.isDown = FALSE

	def Down(self):
		self.isDown = TRUE

	def Up(self):
		self.isDown = FALSE

	def OnRender(self):

		if self.isDown:
			grp.SetColor(ui.WHITE_COLOR)
		else:
			grp.SetColor(ui.HALF_WHITE_COLOR)

		x, y = self.GetGlobalPosition()
		grp.RenderBar(x+2, y+2, self.GetWidth()-4, self.GetHeight()-4)

class CheckBox(ui.ImageBox):
	def __init__(self, parent, x, y, event, filename = "d:/ymir work/ui/public/Parameter_Slot_01.sub"):
		ui.ImageBox.__init__(self)
		self.SetParent(parent)
		self.SetPosition(x, y)
		self.LoadImage(filename)

		self.mouseReflector = MouseReflector(self)
		self.mouseReflector.SetSize(self.GetWidth(), self.GetHeight())

		image = ui.MakeImageBox(self, "d:/ymir work/ui/public/check_image.sub", 0, 0)
		image.AddFlag("not_pick")
		image.SetWindowHorizontalAlignCenter()
		image.SetWindowVerticalAlignCenter()
		image.Hide()
		self.Enable = TRUE
		self.image = image
		self.event = event
		self.Show()

		self.mouseReflector.UpdateRect()

	def __del__(self):
		ui.ImageBox.__del__(self)

	def SetCheck(self, flag):
		if flag:
			self.image.Show()
		else:
			self.image.Hide()
			
	def IsChecked(self):
		return self.image.IsShow()

	def Disable(self):
		self.Enable = FALSE

	def OnMouseOverIn(self):
		if not self.Enable:
			return
		self.mouseReflector.Show()

	def OnMouseOverOut(self):
		if not self.Enable:
			return
		self.mouseReflector.Hide()

	def OnMouseLeftButtonDown(self):
		if not self.Enable:
			return
		self.mouseReflector.Down()

	def OnMouseLeftButtonUp(self):
		if not self.Enable:
			return
		self.mouseReflector.Up()
		self.event()

class LogEntry(ui.ImageBox):
	def __init__(self):
		ui.ImageBox.__init__(self)
		self.LoadImage("multi_farmblock/log_line.png")
		self.Show()
		
		self.UserTextLine = ui.TextLine()
		self.UserTextLine.SetParent(self)
		self.UserTextLine.SetPosition(183/2, 3)
		self.UserTextLine.SetHorizontalAlignCenter()
		self.UserTextLine.SetText("")
		self.UserTextLine.Show()
		self.name = ""
		
		self.StateCheckBox = CheckBox(self, 190, 2, self.ToggleState, "d:/ymir work/ui/public/Parameter_Slot_02.sub")
	
	def ToggleState(self):
		multifarmblock.ToggleState(self.name)
	
	def SetData(self, name, state):
		self.name = name
		self.UserTextLine.SetText(name)
		self.StateCheckBox.SetCheck(state==0)
		
class MainWindow(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.SetSize(310, 300)
		self.AddFlag("movable")
		self.SetTitleName("Multi-Farmblock")
		self.SetCenterPosition()
		
		self.LogEntries = []
		
		self.LoadLogs()
		
		for i in range(10):
			Entry = LogEntry()
			Entry.SetParent(self.LogBG)
			Entry.SetPosition(1, 24+i*22)
			self.LogEntries.append(Entry)
		
	def Open(self):
		self.OnScroll()
		self.Show()

	def LoadLogs(self):
		self.LogBG = ui.ImageBox()
		self.LogBG.SetParent(self)
		self.LogBG.SetPosition(10, 40)
		self.LogBG.LoadImage("multi_farmblock/log_bg.png")
		self.LogBG.Show()
		
		self.UserHeadLine = ui.TextLine()
		self.UserHeadLine.SetParent(self)
		self.UserHeadLine.SetPosition(85, 42)
		self.UserHeadLine.SetText("Account")
		self.UserHeadLine.Show()
		
		self.DateHeadLine = ui.TextLine()
		self.DateHeadLine.SetParent(self)
		self.DateHeadLine.SetPosition(220, 42)
		self.DateHeadLine.SetText("State")
		self.DateHeadLine.Show()
		
		self.ScrollBar = ui.ScrollBarNewDesign()
		self.ScrollBar.SetParent(self)
		self.ScrollBar.SetPosition(285, 40)
		self.ScrollBar.SetScrollBarSize(253)
		self.ScrollBar.Show()
		self.ScrollBar.SetScrollStep(0.3)
		self.ScrollBar.SetScrollEvent(ui.__mem_func__(self.OnScroll))
		
	def Close(self):
		self.Hide()
		
	def Destroy(self):
		self.Close()
	
	def OnScroll(self):
		for log in self.LogEntries:
			log.Hide()
		
		entrys = multifarmblock.GetEntries()
		count = len(entrys)
		
		if count == 0:
			return
		
		scrollLineCount = max(0, count - 10)
		startIdx = int(scrollLineCount * self.ScrollBar.GetPos())
		
		found = 0
		y = 0
		while found < 10:
			i = startIdx+y
			
			if count <= i:
				break
				
			self.LogEntries[found].SetData(entrys[i][0], entrys[i][1])
			self.LogEntries[found].Show()
			found += 1
			y += 1
