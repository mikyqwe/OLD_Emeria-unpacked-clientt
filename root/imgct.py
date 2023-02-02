import ui
import app
import wndMgr

class ImageCoolTimeTest(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.startTime = 0.
		self.CoolTime = 0.

		self.__LoadWindow()
		self.__LoadGUI()

	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)

	def __LoadWindow(self):
		self.SetSize(200, 220)
		self.SetCenterPosition()
		self.SetCloseEvent(self.Close)
		self.SetTitleName(" ~ Image CoolTime TEST ~ ")
		self.AddFlag('movable')
		self.AddFlag('float')

	def __LoadGUI(self):
		self.BGImage = ui.ImageBox()
		self.BGImage.SetParent(self)
		self.BGImage.AddFlag("not_pick")
		self.BGImage.SetPosition(40, 40)
		self.BGImage.LoadImage("d:/ymir work/ui/game/12zi/timer/bg_12zi_timer.sub")
		self.BGImage.Hide()
		# self.BGImage.Show()

		self.CoolTimeImage = ui.ExpandedImageBox()   ## Recommended for .sub images only
		# self.CoolTimeImage = ui.ImageBox()           ## For raw images only[dds, tga, jpg so on]
		self.CoolTimeImage.SetParent(self)
		self.CoolTimeImage.AddFlag("not_pick")
		self.CoolTimeImage.SetPosition(39, 39)
		self.CoolTimeImage.LoadImage("d:/ymir work/ui/game/12zi/timer/gauge_timer.sub")
		# self.CoolTimeImage.LoadImage("asd.tga")
		self.CoolTimeImage.Show()

		self.LeftTime = ui.TextLine()
		self.LeftTime.SetParent(self)
		self.LeftTime.SetDefaultFontName()
		self.LeftTime.SetPosition(70, 30)
		self.LeftTime.SetFeather()
		self.LeftTime.SetText("Time: 02:30")
		self.LeftTime.SetFontColor(0.6, 0.7, 1)
		self.LeftTime.SetOutline()
		self.LeftTime.Show()

		self.Button = ui.MakeButton(self, 70, 190, "", "d:/ymir work/ui/public/", "middle_button_01.sub", "middle_button_02.sub", "middle_button_03.sub")
		self.Button.SetEvent(ui.__mem_func__(self.Start))

	def Start(self):
		self.startTime = float(app.GetTime())
		self.CoolTime = 30.
		self.CoolTimeImage.SetCoolTime(self.CoolTime)
		self.CoolTimeImage.SetStartCoolTime(self.startTime)

	def Open(self):
		self.Show()

	def Close(self):
		self.Hide()
		return 1

	def OnPressEscapeKey(self):
		self.Close()
		return 1

	def OnUpdate(self):
		leftTime = max(0, self.startTime + self.CoolTime - app.GetTime() + 0.5)

		leftMin = int(leftTime/60)
		leftSecond = int(leftTime%60)

		self.LeftTime.SetText("Time: %02d:%02d" % (leftMin, leftSecond))

a=ImageCoolTimeTest()
a.Show()
