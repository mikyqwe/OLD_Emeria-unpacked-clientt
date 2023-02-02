import ui
import dbg
import app
import net
import item
import time
import chat

PATH = 'loterry/'
LEGEND_TEXT = ['Winner', 'Very rare hit!', 'Rare hit', 'Could have been better',
			   'Not so good', 'Trash']

ROLLCOUNT = 51
			   
# key : [vNum, type_border, count]
ITEMS = {
###	num	category	vnum	count
	0	:	[0,	41001,	5],
	1	:	[0,	41002,	25],
	2	:	[0,	41003,	5],
	3	:	[0,	41004,	10],
	4	:	[0,	41005,	10],
	5	:	[0,	41006,	10],
	6	:	[0,	41007,	10],
	7	:	[0,	41008,	25],
	8	:	[0,	41009,	25],
	9	:	[0,	41010,	25],
}

class LotteryWindow(ui.Window):
	_background = None
	_titleBackground = None
	_titleText = None
	_infoText_1 = None
	_infoText_2 = None
	_infoText_3 = None
	_randomButton = None
	_wasRandomText = None
	_wasRandom = None
	_toRandomText = None
	_toRandom = None
	_backgroundCards = None
	_rollLP = -1
	_cards = []
	_startLottery = FALSE
	_rolled = None
	_resumeButtonStatus = TRUE
	_autoLos = None
	_autoLosStatus = FALSE

	def __init__(self):
		ui.Window.__init__(self)
		self.legendInfo = []

	def __del__(self):
		ui.Window.__del__(self)
		self.Destroy()

	def LoadWindow(self):
		self.Board = ui.BoardWithTitleBar()	
		self.SetMainBoard()
		self.SetInterface()
		self.SetLegend()
		self.SetLottery()
		
	def SetMainBoard(self):
		self.Board.SetSize(798, 390)
		self.Board.SetCenterPosition()
		self.Board.AddFlag('movable')
		self.Board.AddFlag('float')
		self.Board.SetTitleName('System Loterie')
		self.Board.SetCloseEvent(self.Close)
		self.Board.Hide()

	def SetInterface(self):
		self.SetBackgroundCards(self.Board)
		self.SetCardsPreview()
		self.arrow = ui.ExpandedImageBox()
		self.arrow.SetParent(self.Board)
		self.arrow.SetPosition(394, 35)
		self.arrow.LoadImage(PATH + 'arrow.tga')
		self.arrow.Show()

	def SetLegend(self):
		self.Legend = Legend(self.Board)

	def SetLottery(self):
		self.SetBackground(self.Board)
		self.SetTitleBackground()
		self.SetTitleText()
		self.SetTextInfo()
		self.SetWasRandom()
		self.SetToRandom()
		self.SetRANDOMButton()
		self.SetRewardButton()
		self.SetResumeButton()

	def SetBackground(self, parent):
		self._background = ui.ExpandedImageBox()
		self._background.SetParent(parent)
		self._background.SetPosition(332, 205)
		self._background.LoadImage(PATH + 'lottery-bg.tga')
		self._background.Show()

	def SetTitleBackground(self):
		self._titleBackground = ui.ExpandedImageBox()
		self._titleBackground.SetParent(self._background)
		self._titleBackground.SetPosition(14, 13)
		self._titleBackground.LoadImage(PATH + 'lottery-title.tga')
		self._titleBackground.Show()

	def SetTitleText(self):
		self._titleText = ui.TextLine()
		self._titleText.SetParent(self._titleBackground)
		self._titleText.SetPosition(int(self._titleBackground.GetWidth() / 2), 0)
		self._titleText.SetText("Information")
		self._titleText.SetHorizontalAlignCenter()
		self._titleText.Show()

	def SetTextInfo(self):
		self._infoText_1 = ui.TextLine()
		self._infoText_1.SetParent(self._background)
		self._infoText_1.SetPosition(16, 33)
		self._infoText_1.SetText("Here you can try your luck and win great prizes")
		self._infoText_1.Show()

		self._infoText_2 = ui.TextLine()
		self._infoText_2.SetParent(self._background)
		self._infoText_2.SetPosition(16, 55)
		self._infoText_2.SetText("Press Play to start the lottery.")
		self._infoText_2.Show()
		
		self._infoText_3 = ui.TextLine()
		self._infoText_3.SetParent(self._background)
		self._infoText_3.SetPosition(16, 78)
		self._infoText_3.SetText("A lottery ticket is required for this.")
		self._infoText_3.Show()

	def SetWasRandom(self):
		self._wasRandomText = ui.TextLine()
		self._wasRandomText.SetParent(self._background)
		self._wasRandomText.SetPosition(22, 115)
		self._wasRandomText.SetText("Trials:")
		self._wasRandomText.Show()

		self._wasRandomSlotBar = ui.SlotBar()
		self._wasRandomSlotBar.SetParent(self._background)
		self._wasRandomSlotBar.SetSize(90, 20)
		self._wasRandomSlotBar.SetPosition(16, 135)
		self._wasRandomSlotBar.Show()
		self._wasRandom = ui.TextLine()
		self._wasRandom.SetParent(self._wasRandomSlotBar)
		self._wasRandom.SetSize(90, 20)
		self._wasRandom.SetPosition((self._wasRandomSlotBar.GetWidth()/2), 4)
		self._wasRandom.SetMax(5)
		self._wasRandom.SetLimitWidth(90)
		self._wasRandom.SetText('0')
		self._wasRandom.SetHorizontalAlignCenter()
		self._wasRandom.Show()

	def SetToRandom(self):
		self._toRandomText = ui.TextLine()
		self._toRandomText.SetParent(self._background)
		self._toRandomText.SetPosition(165, 115)
		self._toRandomText.SetText("Bet: ")
		self._toRandomText.Show()

		self._toRandomSlotBar = ui.SlotBar()
		self._toRandomSlotBar.SetParent(self._background)
		self._toRandomSlotBar.SetSize(90, 20)
		self._toRandomSlotBar.SetPosition(140, 135)
		self._toRandomSlotBar.Show()
		self._toRandom = ui.TextLine()
		self._toRandom.SetParent(self._toRandomSlotBar)
		self._toRandom.SetSize(90, 20)
		self._toRandom.SetPosition(int(self._toRandomSlotBar.GetWidth()/2) - 30, 4)
		self._toRandom.SetMax(5)
		self._toRandom.SetLimitWidth(90)
		self._toRandom.SetText('1')
		self._toRandom.Show()

	def SetRANDOMButton(self):
		self._startRandom = ui.Button()
		self._startRandom.SetParent(self._background)
		self._startRandom.SetPosition(350 - 50, 135)
		self._startRandom.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
		self._startRandom.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
		self._startRandom.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
		self._startRandom.SetText("Play")
		self._startRandom.SetEvent(self.RollComand)
		self._startRandom.Show()

	def SetBackgroundCards(self, parent):
		self._backgroundCards = ui.ExpandedImageBox()
		self._backgroundCards.SetParent(parent)
		self._backgroundCards.SetPosition(10, 30)
		self._backgroundCards.LoadImage(PATH + 'card-bg.tga')
		self._backgroundCards.Show()

	def SetRewardButton(self):
		self._rewardButton = ui.Button()
		self._rewardButton.SetParent(self._background)
		self._rewardButton.SetPosition(350, 105)
		self._rewardButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
		self._rewardButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
		self._rewardButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
		self._rewardButton.SetText('Receives the award')
		self._rewardButton.SetEvent(self.RewardItem)

	def RewardBtnToggle(self):
		if self._rewardButton.IsShow():
			self._rewardButton.Hide()
		else:
			self._rewardButton.Show()
		
	def SetResumeButton(self):
		self._resumeButton = ui.Button()
		self._resumeButton.SetParent(self._background)
		self._resumeButton.SetPosition(255, 105)
		self._resumeButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
		self._resumeButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
		self._resumeButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
		self._resumeButton.SetText('Stop')
		self._resumeButton.SetEvent(self.StopRoll)

	def RewardItem(self):
		pass
		#net.SendChatPacket("/lottery_withdraw_reward")
		#self._rewardButton.Hide()

	def StopRoll(self):
		if self._resumeButtonStatus:
			self._resumeButtonStatus = FALSE
			self._resumeButton.SetText('Replay')
			self._resumeButton.Disable()
		else:
			if int(self._toRandom.GetText()) > 0:
				self._resumeButton.SetText('Stop')
				self._resumeButtonStatus = TRUE
				self._resumeButton.Disable()
				self.RollComand()

	def SetCardsPreview(self):
		for x in xrange(7):
			item = ITEMS[app.GetRandom(0, len(ITEMS) - 1) ]
			self._cards.append(CardLottery(self._backgroundCards, x, item))  # (parent, index, itemVnum, border)

	def SetWasRandomAmount(self,amunt=1):
		self._wasRandom.SetText(str(int(self._wasRandom.GetText())+amunt))

	def SetToRandomAmount(self):
		#Take from inventory cash and calculate how many times u can roll
		pass

	def RollComand(self):
		net.SendChatPacket("/lottery_draw") # done
	
	def Roll(self, speed=1):
		if self.IsLp():
			self._startLottery = TRUE
			self._startRandom.Disable()
			self.InitRoll()
			self.SetWasRandomAmount()
			self.speed = 40
			self.deley = 0.001
			self.amountCards = len(self._cards)-2
			self.StartRoll()

	def IsLp(self):
		if self._rollLP == -1:
			return FALSE
		else:
			return TRUE

	def InitRollLP(self, lp):
		import chat
		chat.AppendChat(chat.CHAT_TYPE_INFO, str(lp))
		lp = int(lp)

		if ITEMS.has_key(lp):
			if lp != -1:
				self._rollLP = lp
				
		self.Roll()		

	def InitRoll(self):
		if self.IsLp():
			del self._cards[:]
			for x in xrange(ROLLCOUNT):
				self._cards.append(CardLottery(self._backgroundCards, x, ITEMS[app.GetRandom(0, len(ITEMS)-1)]))
			self._cards.append(CardLottery(self._backgroundCards, ROLLCOUNT, ITEMS[self._rollLP]))
			for x in xrange(5):
				self._cards.append(CardLottery(self._backgroundCards, x + ROLLCOUNT + 1, ITEMS[app.GetRandom(0, len(ITEMS)-1)]))

	def StartRoll(self):
		self.WarteSchleife = WaitingDialog()
		self.WarteSchleife.Open(float(self.deley))

		if self._cards[ROLLCOUNT].IsDrawn():
			for x in xrange(ROLLCOUNT - 1 + 6):
				self._cards[x].Roll(self.speed)

			if 400 < self._cards[int(self.amountCards * 0.1)]._positionX < 600:
				self.speed = 40
			if 400 < self._cards[int(self.amountCards * 0.8)]._positionX < 600:
				self.speed = 34
			if 400 < self._cards[int(self.amountCards * 0.85)]._positionX < 600:
				self.speed = 28
			if 400 < self._cards[int(self.amountCards * 0.86)]._positionX < 600:
				self.speed = 22
			if 400 < self._cards[int(self.amountCards * 0.865)]._positionX < 600:
				self.speed = 16
			if 400 < self._cards[int(self.amountCards * 0.875)]._positionX < 600:
				self.speed = 13
			if 400 < self._cards[int(self.amountCards * 0.88)]._positionX < 600:
				self.speed = 10
			if 400 < self._cards[int(self.amountCards * 0.905)]._positionX < 600:
				self.speed = 8
			if 400 < self._cards[int(self.amountCards * 0.92)]._positionX < 600:
				self.speed = 6
				self.deley = 0.01
			if 400 < self._cards[int(self.amountCards * 0.935)]._positionX < 600:
				self.speed = 5
			if 400 < self._cards[int(self.amountCards * 0.95)]._positionX < 600:
				self.speed = 4
			if 400 < self._cards[int(self.amountCards * 0.96)]._positionX < 600:
				self.speed = 3
			if 400 < self._cards[int(self.amountCards * 0.97)]._positionX < 600:
				self.speed = 2
			if 400 < self._cards[int(self.amountCards * 0.98)]._positionX < 600:
				self.speed = 2
				self.deley = 0.02
			if 400 < self._cards[int(self.amountCards * 0.99)]._positionX < 600:
				self.speed = 1

			self.WarteSchleife.SAFE_SetTimeOverEvent(self.StartRoll)
		else:
			self.ShowAward()

	def ShowAward(self):
		net.SendChatPacket("/lottery_withdraw_reward")
		self._rollLP = -1
		self._startRandom.Enable()
		self._resumeButton.Enable()
		if int(self._toRandom.GetText()) < 1:
			pass
		else:
			self._toRandom.SetText(str(int(self._toRandom.GetText()) - 1))
		if int(self._toRandom.GetText()) > 0:	
			if self._resumeButtonStatus:
				self._resumeButton.SetText('Stop')
				self._resumeButtonStatus = TRUE
				self._resumeButton.Show()
				self.RollComand()
		else:
			self._resumeButton.Hide()

	def Destroy(self):
		del self.Legend
		del self.arrow
		del self._background
		del self._titleBackground
		del self._titleText
		del self._infoText_1
		del self._infoText_2
		del self._infoText_3
		del self._wasRandomText
		del self._wasRandom
		del self._wasRandomSlotBar
		del self._toRandomSlotBar
		del self._toRandom
		del self._toRandomText
		del self._cards[:]
		del self._backgroundCards
		#del self._autoLosButton
		del self._rewardButton
		del self._resumeButton
		if self._autoLos is not None:
			del self._autoLos
		del self.Board

	def OpenWindow(self):
		if self.Board.IsShow():
			self.Board.Hide()
		else:
			self.Board.Show()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Close(self):
		if self.Board:
			self.Board.Hide()

	def Open(self):
		if self.Board:
			self.Board.Show()
			
class CardLottery:
	_background = None
	_item = None
	_border = None
	_count = None
	toolTip = None
	_index = None
	_itemVnum = None
	_typeBorder = None
	_positionX = None
	_winCard = FALSE
	_img = None
	
	def __init__(self, parent, index, item):
		self._index = index
		self._itemVnum = item[1]
		self._typeBorder = item[0]
		self._count = item[2]
		self._positionX = 40 + (self._index * 105)
		if self._index is ROLLCOUNT:
			self._winCard = TRUE
		self.SetBackground(parent)
		self.SetItem()
		self.SetBorder()

	def __del__(self):
		self.Destroy()

	def SetBackground(self, parent):
		self._background = ui.ExpandedImageBox()
		self._background.SetParent(parent)
		self._background.SetPosition(self._positionX, 28)
		self._background.LoadImage(PATH + 'card.tga')
		if self._positionX - 2 > 775:
			self._background.Hide()
		else:
			self._background.Show()

	def SetItem(self):
		self._item = ui.ExpandedImageBox()
		self._item.SetParent(self._background)
		item.SelectItem(self._itemVnum)
		try:
			self._img = item.GetIconImageFileName()
			self._item.LoadImage(self._img)
			if self._item.GetHeight() <= 32:
				self._item.SetPosition(int(self._background.GetWidth() / 2) - 16,
									   int(self._background.GetHeight() / 2) - 16)
			elif self._item.GetHeight() <= 64:
				self._item.SetPosition(int(self._background.GetWidth() / 2) - 16,
									   int(self._background.GetHeight() / 2) - 32)
			elif self._item.GetHeight() <= 96:
				self._item.SetPosition(int(self._background.GetWidth() / 2) - 16,
									   int(self._background.GetHeight() / 2) - 48)
		except:
			dbg.TraceError("No found item")
			self._item.LoadImage(PATH + '03150.tga')

		if self._positionX - 2 > 775:
			self._item.Hide()
		else:
			self._item.Show()

	def SetBorder(self):
		self._border = ui.ExpandedImageBox()
		self._border.SetParent(self._background)
		self._border.SetPosition(-2, -2)
		self._border.LoadImage(PATH + 'card-border-' + str(5-self._typeBorder + 1) + '.tga')
		if self._positionX - 2 > 775:
			self._border.Hide()
		else:
			self._border.Show()

		self._coutText = ui.TextLine()
		self._coutText.SetParent(self._item)
		self._coutText.SetPosition(int(self._item.GetWidth())-2,int(self._item.GetHeight())-2)
		self._coutText.SetText(str(self._count))
		self._coutText.SetFontName("Tahoma:11")
		if self._positionX - 2 > 775:
			self._coutText.Hide()
		else:
			if self._count == 1:
				self._coutText.Hide()
			else:
				self._coutText.Show()

	def IsDrawn(self):
		if self._winCard is TRUE and self._positionX > 360+((time.clock()%60)-30):
			return TRUE
		else:
			return FALSE
			
	def HideItems(self):
		self._border.Hide()
		self._background.Hide()
		self._item.Hide()

	def ShowItems(self):
		self._background.Show()
		self._item.Show()
		self._border.Show()

	def Roll(self, speed=1):
		if self._positionX - speed > -108:
			self._positionX = self._positionX - speed
			self._background.SetPosition(self._positionX, 28)
			if 695 < self._positionX < 776:
				Percent = float((776.0-self._positionX) / float(self._border.GetWidth())) - 1.0
				self._border.SetRenderingRect(0.0, 0.0,Percent, 0.0)
				self._background.SetRenderingRect(0.0, 0.0,Percent, 0.0)
				self._item.SetRenderingRect(0.0, 0.0,Percent, 0.0)
				self.ShowItems()
			if 300 < self._positionX <= 695:
				self._border.SetRenderingRect(0.0, 0.0, 0.0, 0.0)
				self._background.SetRenderingRect(0.0, 0.0, 0.0, 0.0)
				self._item.SetRenderingRect(0.0, 0.0, 0.0, 0.0)
			if 12 > self._positionX  and self._positionX >= -68:
				Percent = float(abs(self._positionX-12) / float(self._border.GetWidth()))
				self._border.SetRenderingRect(0.0-Percent,0.0, 0.0, 0.0)
				self._background.SetRenderingRect(0.0-Percent,0.0, 0.0, 0.0)
				self._item.SetRenderingRect(0.0-Percent-0.16,0.0, 0.0, 0.0)
				self.ShowItems()
			elif self._positionX < -68:
				self.HideItems()

	def Destroy(self):
		del self._index
		del self._count
		del self._border
		del self._item
		del self._background
		del self._typeBorder
		del self._itemVnum
		del self._img


class WaitingDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime

		self.Show()

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)

	def OnUpdate(self):
		import time
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			return

	def OnPressExitKey(self):
		self.Close()
		return TRUE


class Legend:
	_background = None
	_titleBackground = None
	_titleText = None
	_itemPrice = []

	def __init__(self, parent):
		self.SetBackground(parent)
		self.SetTitleBackground()
		self.SetTitleText()
		self.SetItemPrice()

	def SetBackground(self, parent):
		self._background = ui.ExpandedImageBox()
		self._background.SetParent(parent)
		self._background.SetPosition(10, 205)
		self._background.LoadImage(PATH + 'legend-bg.tga')
		self._background.Show()

	def SetTitleBackground(self):
		self._titleBackground = ui.ExpandedImageBox()
		self._titleBackground.SetParent(self._background)
		self._titleBackground.SetPosition(14, 13)
		self._titleBackground.LoadImage(PATH + 'legend-title.tga')
		self._titleBackground.Show()

	def SetTitleText(self):
		self._titleText = ui.TextLine()
		self._titleText.SetParent(self._titleBackground)
		self._titleText.SetPosition(int(self._titleBackground.GetWidth() / 2), 0)
		self._titleText.SetText("Legends")
		self._titleText.SetHorizontalAlignCenter()
		self._titleText.Show()

	def SetItemPrice(self):
		for x in xrange(len(LEGEND_TEXT)):
			self._itemPrice.append(LegendComponents(self._background, x))

	def __del__(self):
		self.Destroy()

	def Destroy(self):
		del self._background
		del self._titleBackground
		del self._titleText
		del self._itemPrice[:]


class LegendComponents:
	_board = None
	_index = 0
	_image = None
	_text = None

	def __init__(self, parent, index):
		self.Board = parent
		self.index = index
		self.AddImage()
		self.AddText()

	def AddImage(self):
		self.image = ui.ExpandedImageBox()
		self.image.SetParent(self.Board)
		self.image.SetPosition(28, 43 + self.index * 22)
		self.image.LoadImage(PATH + 'legend-border-' + str(self.index + 1) + '.tga')
		self.image.Show()

	def AddText(self):
		self.text = ui.TextLine()
		self.text.SetParent(self.Board)
		self.text.SetPosition(113, 36 + 22 * self.index)
		self.text.SetText(LEGEND_TEXT[self.index])
		self.text.Show()

	def __del__(self):
		self.Destroy()

	def Destroy(self):
		del self.Board
		del self.index
		del self.image
		del self.text
