import ui
import wndMgr
import grp
import item
import time
import uiToolTip

class Reward(ui.BoardStyle2):
	def __init__(self):
		ui.BoardStyle2.__init__(self)
			# self.__LoadMe()

	def __del__(self):
		ui.BoardStyle2.__del__(self)
		
	def Open(self, iRewardVnum, sAnimationDir):
		self.isLoaded = FALSE
		if FALSE == self.isLoaded:
			self.__LoadMe(iRewardVnum, sAnimationDir)
		self.boardAnimation.Enlarge()

	def Close(self):
		self.boardAnimation.Shrink()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnPressExitKey(self):
		self.Close()
		return True
		
	def __LoadMe(self, iRewardVnum, sAnimationDir):
		self.SetSize(300, 200)
		self.SetCenterPosition()
		self.AddFlag('movable')
		self.boardAnimation = BoardAnimation(self)
		
		thinBoard2 = ui.HorizontalSeparator()
		thinBoard2.SetParent(self)
		thinBoard2.SetWidth(280)
		thinBoard2.SetPosition(10, 65-10)
		thinBoard2.Show()
		self.thinBoard2 = thinBoard2
		
		
		thinBoard = ui.Input()
		thinBoard.SetParent(self)
		thinBoard.SetWidth(261)
		thinBoard.SetPosition(15, 70-22)
		thinBoard.Show()
		self.thinBoard = thinBoard
		
		if sAnimationDir <> "":
			self.rewardbackground = ui.AniImageBox()
			self.rewardbackground.SetParent(self)
			self.rewardbackground.AppendImage('reward/highlight/' + sAnimationDir + '/1.png')
			self.rewardbackground.AppendImage('reward/highlight/' + sAnimationDir + '/2.png')
			self.rewardbackground.AppendImage('reward/highlight/' + sAnimationDir + '/3.png')
			self.rewardbackground.AppendImage('reward/highlight/' + sAnimationDir + '/4.png')
			self.rewardbackground.AppendImage('reward/highlight/' + sAnimationDir + '/5.png')
			self.rewardbackground.AppendImage('reward/highlight/' + sAnimationDir + '/6.png')
			self.rewardbackground.AppendImage('reward/highlight/' + sAnimationDir + '/5.png')
			self.rewardbackground.AppendImage('reward/highlight/' + sAnimationDir + '/4.png')
			self.rewardbackground.AppendImage('reward/highlight/' + sAnimationDir + '/3.png')
			self.rewardbackground.AppendImage('reward/highlight/' + sAnimationDir + '/2.png')
			self.rewardbackground.SetPosition(110+15, 77+22)
			self.rewardbackground.SetDelay(3)
			# self.rewardbackground.SetPercentage(0, 100)
			# self.rewardbackground.LoadImage('Slotempty.png')
			self.rewardbackground.Show()
		
		# self.progressBarActualFile = ui.AniImageBox()
		# self.progressBarActualFile.SetParent(self.thinBoard2)
		# self.progressBarActualFile.AppendImage('locale\de\ui\itemshop\loadingBar.tga')
		# self.progressBarActualFile.SetPosition(5, 8)
		# self.progressBarActualFile.SetDelay(90)
		# self.progressBarActualFile.SetPercentage(0, 100)
		# self.progressBarActualFile.Show()
		
		# Close Button
		self.AcceptButton = ui.Button()
		self.AcceptButton.SetParent(self)
		self.AcceptButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AcceptButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AcceptButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AcceptButton.SetText("Schlieﬂen")
		self.AcceptButton.SetPosition(220, 160)
		self.AcceptButton.SetEvent(self.Close)
		self.AcceptButton.Show()
		
		# Reward Text
		textLine = ui.TextLine()
		textLine.SetParent(self)
		textLine.SetPosition(30, 49-22)
		textLine.SetFontColor( 1.0 ,  1.0 ,  0.2 )
		textLine.Show()
		self.textLine = textLine
		self.textLine.SetText("Du hast folgendes Item erhalten:")
		
		# Reward Text Item
		textLineReward = ui.TextLine()
		textLineReward.SetParent(self)
		textLineReward.SetPosition(195, 50-22)
		
		# Colors picked by: https://doc.instantreality.org/tools/color_calculator/
		if sAnimationDir == "blue":
			textLineReward.SetFontColor(0.5, 0.6, 1)
		elif sAnimationDir == "green":
			textLineReward.SetFontColor(0.435, 0.984, 0.525)
		elif sAnimationDir == "pink":
			textLineReward.SetFontColor(0.980, 0.435, 0.984)
		elif sAnimationDir == "red":
			textLineReward.SetFontColor(1, 0.235, 0.2)
		elif sAnimationDir == "gold":
			textLineReward.SetFontColor(0.996, 0.788, 0.003)
		else:
			textLineReward.SetFontColor(0.5, 0.6, 1)
		
		textLineReward.Show()
		self.textLineReward = textLineReward
		self.textLineReward.SetText("Schwert+9")
		
		# Reward Icon
		imageItem = ui.ImageBox()
		imageItem.SetParent(self)
		imageItem.SetPosition(0,22)
		imageItem.SetWindowVerticalAlignCenter()
		imageItem.SetWindowHorizontalAlignCenter()
		imageItem.Show()
		self.imageItem = imageItem
		
		
		self.toolTip = uiToolTip.ItemToolTip()
		self.toolTip.ClearToolTip()
		self.toolTip.Hide()
		
		self.imageItem.SAFE_SetStringEvent("MOUSE_OVER_IN" , self.ShowTip)
		self.imageItem.SAFE_SetStringEvent("MOUSE_OVER_OUT" , self.HideTip)
		
		
		self.iRewardVnum = iRewardVnum
		
		self.ShowReward()
		
		# self.isLoaded = True
		
	def ShowReward(self):
		item.SelectItem(self.iRewardVnum)
		self.textLineReward.SetText(item.GetItemName())
		try:
			self.imageItem.LoadImage(str(item.GetIconImageFileName()))
		except:
			import dbg
			dbg.TraceError("ShowReward.LoadImage")

	def ShowTip(self):
		self.toolTip.SetItemToolTip(self.iRewardVnum)
		self.toolTip.Show()
		
	def HideTip(self):
		self.toolTip.Hide()
		
class Animation(object):
	def __init__(self, element, mainElement, animateSteps = 20, animateTime = 2.05):
		self.element = element
		self.mainElement = mainElement
		self.animateTime = animateTime
		self.animateSteps = animateSteps

		self.animateEvent = None
		self.animateWidth = 0
		self.animateCurrentWidth = 0
		self.animateHeight = 0
		self.animateCurrentHeight = 0
		self.animateStartTime = 0
		self.animateEndEvent = None

	def Destroy(self):
		self.element = None

	def Enlarge(self, startWidth = 60, startHeight = 60, endEvent = None):
		self.animateWidth = self.mainElement.GetWidth()
		self.animateCurrentWidth = startWidth
		self.animateHeight = self.mainElement.GetHeight()
		self.animateCurrentHeight = startHeight
		self.animateStartTime = 0
		self.animateEndEvent = endEvent

		self.animateEvent = self.EnlargeEvent

		self.element.SetSize(0, 0)
		
		self.element.Show()

	def Shrink(self, endWidth = 300, endHeight = 200):
		self.animateWidth = endWidth
		self.animateCurrentWidth =  self.mainElement.GetWidth()
		self.animateHeight = endHeight
		self.animateCurrentHeight =  self.mainElement.GetHeight()
		self.animateStartTime = 0

		self.animateEvent = self.ShrinkEvent

		self.element.SetSize(self.mainElement.GetWidth(),  self.mainElement.GetHeight())
		self.element.Show()

	def EnlargeEvent(self):
		if self.animateCurrentWidth + self.animateSteps < self.animateWidth and self.animateCurrentHeight + self.animateSteps < self.animateHeight:
			self.animateCurrentWidth += self.animateSteps
			self.animateCurrentHeight += self.animateSteps

			x, y = self.mainElement.GetGlobalPosition()

			self.element.SetPosition(x + (self.animateWidth - self.animateCurrentWidth)/2, y + (self.animateHeight - self.animateCurrentHeight)/2)
			self.element.SetSize(self.animateCurrentWidth, self.animateCurrentHeight)
			
		else:
			self.animateEvent = None
			self.element.Hide()
			if self.animateEndEvent:
				self.animateEndEvent()

	def ShrinkEvent(self):
		if self.animateCurrentWidth - self.animateSteps > self.animateWidth and self.animateCurrentHeight - self.animateSteps > self.animateHeight:
			self.animateCurrentWidth -= self.animateSteps
			self.animateCurrentHeight -= self.animateSteps
			
			x, y = self.mainElement.GetGlobalPosition()

			self.element.SetPosition(x + ( self.mainElement.GetWidth() - self.animateCurrentWidth)/2, y + ( self.mainElement.GetHeight() - self.animateCurrentHeight)/2)
			self.element.SetSize(self.animateCurrentWidth, self.animateCurrentHeight)
		else:
			self.animateEvent = None
			self.element.Hide()

	def OnUpdate(self):
		if self.animateEvent:
			if self.animateStartTime < time.clock():
				self.animateStartTime = time.clock() + self.animateTime
				self.animateEvent()
					
class BoardAnimation(ui.Board):
	def __init__(self, mainBoardElement):
		ui.Board.__init__(self)
		self.mainBoardElement = mainBoardElement
		x, y = self.mainBoardElement.GetGlobalPosition()
		self.SetSize(self.mainBoardElement.GetWidth(), self.mainBoardElement.GetHeight())
		self.SetPosition(x,y)
		self.animation = Animation(self, mainBoardElement, animateSteps = 20, animateTime = 0.01)

	def __del__(self):
		ui.Board.__del__(self)

	def Enlarge(self):
		self.animation.Enlarge(endEvent = self.mainBoardElement.Show)

	def Shrink(self):
		self.mainBoardElement.Hide()
		self.animation.Shrink()

	def Destroy(self):
		self.mainBoardElement = None
		self.board = None

	def OnUpdate(self):
		self.animation.OnUpdate()
