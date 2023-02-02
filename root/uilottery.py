#
#	Avandos Lottery
#		Copyright (C) Avandos Network. All rights reserved.
#		Developed 2020 by Avandos Network.
#
#
import ui
import dbg
import app
import net
import item
import time
import chat
import constInfo
import event
import random
import wndMgr
import grp
import uiToolTip
import uireward
import snd

PATH2 = 'interface_emperorapollo/common/horizontal_bar/'
PATH = 'loterry/'

# LOTTERY_ROLL_COUNT = 51 - 40
LOTTERY_ROLL_COUNT = 41
LOTTERY_CARDS_PREVIEW = 4

LOTTERY_ITEMS = {
	0	:	[0,	0, 0],
}


class LotteryWindow(ui.Window):
	
	_background = None
	_titleBackground = None
	_titleText = None
	_toRandom = None
	_backgroundCards = None
	_rollLP = -1
	_cards = []
	_startLottery = FALSE
	_rolled = None

	def __init__(self):
		ui.Window.__init__(self)

	def __del__(self):
		ui.Window.__del__(self)
		self.Destroy()
		
	def LoadWindow(self):
		self.Board = ui.BoardWithTitleBar()	
		self.SetMainBoard()
		self.SetInterface()
		# self.SetLegend()
		self.SetLottery()
		self.slots = {}
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()
		
	def SetMainBoard(self):
		self.Board.SetSize(498, 390)
		self.Board.SetCenterPosition()
		self.Board.AddFlag('movable')
		self.Board.AddFlag('float')
		self.Board.SetTitleName('Unlock Container')
		self.Board.SetCloseEvent(self.Close)
		self.Board.Hide()

	def SetInterface(self):
		self.SetBackgroundCards(self.Board)
		self.arrow = ui.AniImageBox()
		self.arrow.SetParent(self.Board)
		self.arrow.AppendImage(PATH + 'arrow.png')
		self.arrow.AppendImage(PATH + 'arrow2.png')
		self.arrow.AppendImage(PATH + 'arrow3.png')
		self.arrow.AppendImage(PATH + 'arrow4.png')
		self.arrow.AppendImage(PATH + 'arrow5.png')
		self.arrow.AppendImage(PATH + 'arrow6.png')
		self.arrow.AppendImage(PATH + 'arrow7.png')
		self.arrow.AppendImage(PATH + 'arrow6.png')
		self.arrow.AppendImage(PATH + 'arrow5.png')
		self.arrow.AppendImage(PATH + 'arrow4.png')
		self.arrow.AppendImage(PATH + 'arrow3.png')
		self.arrow.AppendImage(PATH + 'arrow2.png')
		self.arrow.SetPosition(240, 35)
		self.arrow.SetDelay(5)
		self.arrow.Show()
		
	def OverInItem(self, slot):
		self.tooltipItem.SetItemToolTip(self.aRarityPreviewItems[slot])
		
	def OverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	# def SetLegend(self):
		# self.Legend = Legend(self.Board)

	def SetLottery(self):
		self.SetBackground(self.Board)
		self.SetTitleBackground()
		self.SetTitleText()
		self.SetRarityItemPreview()

	def SetBackground(self, parent):
		self._background = ui.NewBoard()
		self._background.SetParent(parent)
		self._background.SetPosition(10, 205)
		self._background.SetSize(478, 175)
		self._background.Show()

	def SetTitleBackground(self):
		self._titleBackground = ui.ImageBox()
		self._titleBackground.SetParent(self._background)
		self._titleBackground.SetPosition(140, 13)
		self._titleBackground.LoadImage(PATH2 + 'center.png')
		self._titleBackground.Show()

	def SetTitleText(self):
		self._titleText = ui.TextLine()
		self._titleText.SetParent(self._titleBackground)
		self._titleText.SetPosition(int(self._titleBackground.GetWidth() / 2), 0)
		self._titleText.SetText("Mögliche Drops")
		self._titleText.SetHorizontalAlignCenter()
		self._titleText.Show()
		
		# Spin Button
		self.AcceptButton = ui.Button()
		self.AcceptButton.SetParent(self.Board)
		self.AcceptButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AcceptButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AcceptButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AcceptButton.SetText("Spin")
		self.AcceptButton.SetPosition(220, 350)
		self.AcceptButton.SetEvent(self.RequestSpin)
		self.AcceptButton.Show()
		
	def SetRarityItemPreview(self):
		
		# create grid slots
		self.previewItems = ui.GridSlotWindow()
		self.previewItems.SetParent(self._background)
		self.previewItems.SetPosition(70, 50)
		self.previewItems.ArrangeSlot(0,10,2,32,32,0,0)
		self.previewItems.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.previewItems.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))
		self.previewItems.SetSlotBaseImage("d:/ymir work/slot_lager/slot.tga",1.0,1.0,1.0,1.0)
		self.previewItems.RefreshSlot()
		self.previewItems.Show()
		
		# test preview items
		self.aRarityPreviewItems = [19, 29, 39] # TEST PREVIEW
		for i in range(len(self.aRarityPreviewItems)):
			self.previewItems.SetItemSlot(i,self.aRarityPreviewItems[i], 1)
		
	def SetBackgroundCards(self, parent):
		self._backgroundCards = ui.NewBoard()
		self._backgroundCards.SetParent(parent)
		self._backgroundCards.SetPosition(10, 35)
		self._backgroundCards.SetSize(478, 165)
		# self._backgroundCards.LoadImage(PATH + 'card-bg.tga')
		# self._backgroundCards.LoadImage(PATH + 'card-bg-small.tga')
		self._backgroundCards.Show()

	def SetCardsPreview(self):
		
		self._cards = []
		
		for x in xrange(LOTTERY_CARDS_PREVIEW):
			item = LOTTERY_ITEMS[app.GetRandom(0, len(LOTTERY_ITEMS) - 1) ]
			self._cards.append(CardLottery(self._backgroundCards, x, item))  # (parent, index, itemVnum, border)

	def RollComand(self):
		net.SendChatPacket("/lottery_draw") # done
	
	def Roll(self, speed=1):
		if self.IsLp():
			self._startLottery = TRUE
			self.InitRoll()
			self.speed = 25
			self.deley = 0.001
			self.amountCards = len(self._cards)-2
			self.StartRoll()

	def IsLp(self):
		if self._rollLP == -1:
			return FALSE
		else:
			return TRUE

	def InitRollLP(self, lp):
	
		#chat.AppendChat(chat.CHAT_TYPE_INFO, "[client init roll lp] " + str(lp))
		lp = int(lp)
		lp = lp -1 # required because array index begins from 0 while quest id sent from index 1.
		
		# self.InitLotteryItems()
		# self.SetPreviewItems()
		# self.SetCardsPreview()
		
		if lp in LOTTERY_ITEMS:
			if lp != -1:
				self._rollLP = lp
				
		snd.FadeOutMusic("sound/ui/lottery/background.mp3")
		snd.FadeInMusic("sound/ui/lottery/spin.mp3")
		
		self.Roll()

	def InitRoll(self):
		if self.IsLp():
			del self._cards[:]
			for x in xrange(LOTTERY_ROLL_COUNT):
				self._cards.append(CardLottery(self._backgroundCards, x, LOTTERY_ITEMS[app.GetRandom(0, len(LOTTERY_ITEMS)-1)]))
			self._cards.append(CardLottery(self._backgroundCards, LOTTERY_ROLL_COUNT, LOTTERY_ITEMS[self._rollLP]))
			for x in xrange(5):
				self._cards.append(CardLottery(self._backgroundCards, x + LOTTERY_ROLL_COUNT + 1, LOTTERY_ITEMS[app.GetRandom(0, len(LOTTERY_ITEMS)-1)]))

	def StartRoll(self):
		self.WarteSchleife = WaitingDialog()
		self.WarteSchleife.Open(float(self.deley))

		if self._cards[LOTTERY_ROLL_COUNT].IsDrawn():
			for x in xrange(LOTTERY_ROLL_COUNT - 1 + 6):
				self._cards[x].Roll(self.speed)

			if 400 < self._cards[int(self.amountCards * 0.2)]._positionX < 600:
				self.speed = 25
			if 400 < self._cards[int(self.amountCards * 0.5)]._positionX < 600:
				self.speed = 20
			if 400 < self._cards[int(self.amountCards * 0.6)]._positionX < 600:
				self.speed = 13
			if 400 < self._cards[int(self.amountCards * 0.8)]._positionX < 600:
				self.speed = 10
			if 400 < self._cards[int(self.amountCards * 0.905)]._positionX < 600:
				self.speed = 8
			if 400 < self._cards[int(self.amountCards * 0.92)]._positionX < 600:
				self.speed = 6
			# if 400 < self._cards[int(self.amountCards * 0.935)]._positionX < 600:
				# self.speed = 5
			if 400 < self._cards[int(self.amountCards * 0.95)]._positionX < 600:
				self.speed = 4
			# if 400 < self._cards[int(self.amountCards * 0.96)]._positionX < 600:
				# self.speed = 3
			if 400 < self._cards[int(self.amountCards * 0.97)]._positionX < 600:
				self.speed = 2
			# if 400 < self._cards[int(self.amountCards * 0.98)]._positionX < 600:
				# self.speed = 2
			if 400 < self._cards[int(self.amountCards * 0.99)]._positionX < 600:
				self.speed = 1

			self.WarteSchleife.SAFE_SetTimeOverEvent(self.StartRoll)
		else:
			self.ShowAward()

	def ShowAward(self):
		
		snd.FadeOutMusic("sound/ui/lottery/spin.mp3")
		snd.PlaySound("sound/ui/lottery/reward.mp3")
		
		constInfo.AVANDOS_CONTAINER_LOTTERY["CMD"] = "GIVE_REWARD"
		event.QuestButtonClick(constInfo.AVANDOS_CONTAINER_LOTTERY["index"])
		
		iItemRarity = int(LOTTERY_ITEMS[self._rollLP][2])
		aRarityColorNames = ["NONE", "blue", "green", "pink", "red", "gold"]
		
		wnd = uireward.Reward()
		wnd.Open(LOTTERY_ITEMS[self._rollLP][1], aRarityColorNames[iItemRarity])
		
		self._rollLP = -1
		self.Close()
		
	def RequestSpin(self):
		self.AcceptButton.Hide()
		constInfo.AVANDOS_CONTAINER_LOTTERY["CMD"] = "START_SPIN"
		event.QuestButtonClick(constInfo.AVANDOS_CONTAINER_LOTTERY["index"])

	def Destroy(self):
		del self.arrow
		del self._background
		del self._titleBackground
		del self._titleText
		del self._cards[:]
		del self._backgroundCards
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
			snd.FadeOutMusic("sound/ui/lottery/spin.mp3")
			snd.FadeOutMusic("sound/ui/lottery/background.mp3")

	def Open(self):
		
		if self.IsLp():
			return False
	
		if self.Board:
			
			self.InitLotteryItems()
			self.SetPreviewItems()
			self.SetCardsPreview()
			
			self.AcceptButton.Show()
			self.Board.Show()
			
			snd.FadeInMusic("sound/ui/lottery/background.mp3")
			
	def InitLotteryItems(self):
	
		global LOTTERY_ITEMS
		LOTTERY_ITEMS = {}
		
		###	num	category	vnum	count
		for i in xrange(len(constInfo.AVANDOS_CONTAINER_LOTTERY["item_vnum_list"])):
			for t in xrange(len(constInfo.AVANDOS_CONTAINER_LOTTERY["item_vnum_list"][i])):
				# chat.AppendChat(chat.CHAT_TYPE_INFO, constInfo.AVANDOS_CONTAINER_LOTTERY["item_vnum_list"][i][t] )
				iAppendItemVnum = constInfo.AVANDOS_CONTAINER_LOTTERY["item_vnum_list"][i][t]
				iAppendItemRarity = constInfo.AVANDOS_CONTAINER_LOTTERY["item_rarity_list"][i][t]
				LOTTERY_ITEMS[t] = {}
				LOTTERY_ITEMS[t][0] = 0
				LOTTERY_ITEMS[t][1] = int(iAppendItemVnum)
				LOTTERY_ITEMS[t][2] = iAppendItemRarity
				
	def SetPreviewItems(self):
	
		# clear slot items
		for item in range(len(self.aRarityPreviewItems)):
			self.previewItems.SetItemSlot(item, 0)
		
		# set slot items
		self.aRarityPreviewItems = []
		for item in LOTTERY_ITEMS:
			self.aRarityPreviewItems.append(LOTTERY_ITEMS[item][1])
			self.previewItems.SetItemSlot(item,self.aRarityPreviewItems[item], 1)

class CardLottery:
	_background = None
	_item = None
	_border = None
	_count = None
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
		if self._index is LOTTERY_ROLL_COUNT:
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
		self._background.LoadImage(PATH + 'card.png')
		if self._positionX - 2 > 475:
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

		if self._positionX - 2 > 475:
			self._item.Hide()
		else:
			self._item.Show()

	def SetBorder(self):
		self._border = ui.ExpandedImageBox()
		self._border.SetParent(self._background)
		self._border.SetPosition(-2, -2)
		self._border.LoadImage(PATH + 'card-border-' + str(5-self._typeBorder + 1) + '.tga')
		if self._positionX - 2 > 475:
			self._border.Hide()
		else:
			self._border.Show()

		self._coutText = ui.TextLine()
		self._coutText.SetParent(self._item)
		self._coutText.SetPosition(int(self._item.GetWidth())-2,int(self._item.GetHeight())-2)
		self._coutText.SetText(str(self._count))
		self._coutText.SetFontName("Tahoma:11")
		if self._positionX - 2 > 475:
			self._coutText.Hide()
		else:
			if self._count == 1:
				self._coutText.Hide()
			else:
				self._coutText.Show()

	def IsDrawn(self):
		if self._winCard is TRUE and self._positionX > 200+((time.clock()%60)-30):
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
			if 395 < self._positionX < 476:
				Percent = float((476.0-self._positionX) / float(self._border.GetWidth())) - 1.0
				self._border.SetRenderingRect(0.0, 0.0,Percent, 0.0)
				self._background.SetRenderingRect(0.0, 0.0,Percent, 0.0)
				self._item.SetRenderingRect(0.0, 0.0,Percent, 0.0)
				self.ShowItems()
			if 0 < self._positionX <= 395:
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
