import ui
import item
import constInfo
import app
import net
import chat
import player
import localeInfo
from uiToolTip import ItemToolTip
import apollo_interface

WIDTH = 340
HEIGHT = 470

OZUT_STATUS = True
UNUTKANLIK_STATUS = True
CALLBACK_MISSION = True

ROOT = "d:/ymir work/ui/game/bio/"

YENILEME_NOTU = 70028

bio_data = [
	# level, item, count, time, lucky, stone, afftype1, affvalue1, afftype2, affvalue2, afftype3, affvalue3 , afftype4, affvalue4, isChoose
	[ 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0], #empty
	[ 30, 30006, 10, 900 * 60, 60, 30220, item.APPLY_ATTBONUS_MONSTER, 5,0,0,0,0,0,0,0, 71035, 70022], #Ork disi
	[ 40, 30047, 15, 900 * 60, 60, 30221, item.APPLY_MAX_HP, 800,0,0,0,0,0,0,0, 71035, 70022], #Seytan hatirasi
	[ 50, 30015, 15, 900 * 60, 60, 30222, item.APPLY_ATTBONUS_HUMAN, 5,0,0,0,0,0,0,0, 71035, 70022], #Lanet kitabi
	[ 60, 30050, 20, 900 * 60, 60, 30223, item.APPLY_ATT_GRADE_BONUS, 50,0,0,0,0,0,0,0, 71035, 70022], #Buz topu
	[ 70, 30165, 25, 900 * 60, 60, 30224, item.APPLY_ATTBONUS_MONSTER, 8,0,0,0,0,0,0,0, 71035, 70022], #Zelkova
	[ 80, 30166, 30, 900 * 60, 60, 30225, item.APPLY_ATT_SPEED, 10,item.APPLY_ATT_GRADE_BONUS,10,0,0,0,0,0, 71035, 70022], #Tugyis
	[ 85, 30167, 40, 900 * 60, 60, 30226, item.APPLY_RESIST_WARRIOR, 10,item.APPLY_RESIST_ASSASSIN,10,item.APPLY_RESIST_SURA,10,item.APPLY_RESIST_SHAMAN,10,0, 71035, 70022], #Kırmızı hayalet dal
	[ 90, 30168, 50, 900 * 60, 60, 30227, item.APPLY_ATTBONUS_WARRIOR, 10,item.APPLY_ATTBONUS_ASSASSIN,10,item.APPLY_ATTBONUS_SURA,10,item.APPLY_ATTBONUS_SHAMAN,10,0, 71035, 70022], #Kırmızı hayalet dal
	[ 92, 30251, 10, 900 * 60, 60, 0, item.APPLY_MAX_HP, 1000,item.APPLY_DEF_GRADE_BONUS,120,item.APPLY_ATT_GRADE_BONUS,50,0,0,1, 71035, 70022], #92 gorevi
	[ 94, 30252, 20, 900 * 60, 60, 30228, item.APPLY_MAX_HP, 1100,item.APPLY_DEF_GRADE_BONUS,140,item.APPLY_ATT_GRADE_BONUS,60,0,0,1, 71035, 70022], #92 gorevi
]

class BiologWindow(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.AddFlag("float")
		self.AddFlag("movable")
		self.SetWindowName("BiologWindow")
		self.SetTitleName(localeInfo.BIO_TITLE)
		self.SetSize(WIDTH,HEIGHT)
		self.SetCenterPosition()
		self.SetCloseEvent(ui.__mem_func__(self.Close))

		self.__Initialize()
		self.LoadWindow()

	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)

	def __Initialize(self):
		self.children = []
		self.missionIcon=None
		self.missionName=None
		self.statusText=None
		self.missionGiftText=None
		self.giftFirst=None
		self.giftSecond=None
		self.giftThird=None

		self.bioLevel = 0
		self.bioCount = 0
		self.bioTime = 0
		self.needUpdate = False

		self.unutkanlikIcon = None
		self.checkBoxUnutkanlik = None
		self.ozutIcon = None
		self.checkBoxOzut = None
		self.checkBoxCall = None

	def Destroy(self):
		self.__Initialize()
		ui.BoardWithTitleBar.Destroy(self)

	def LoadWindow(self):
		#blackBoard = ui.Board()
		#blackBoard.SetParent(self)
		#blackBoard.AddFlag("not_pick")
		#blackBoard.SetPosition(10,30+5)
		#blackBoard.SetSize(WIDTH-20,HEIGHT-50)
		#blackBoard.Show()
		#self.children.append(blackBoard)

		thinBoard = ui.ThinBoard()
		thinBoard.SetParent(self)
		thinBoard.AddFlag("not_pick")
		thinBoard.SetPosition(12+2,30+5+2)
		thinBoard.SetSize(WIDTH-20-4,HEIGHT-50-4)
		thinBoard.Show()
		self.children.append(thinBoard)

		blackBoardEx = ui.Board()
		blackBoardEx.SetParent(self)
		blackBoardEx.AddFlag("not_pick")
		blackBoardEx.SetPosition(12+2+5+5,30+5+2+10+15)
		blackBoardEx.SetSize(WIDTH-45,HEIGHT-90)
		blackBoardEx.Show()
		self.children.append(blackBoardEx)

		titleImage = ui.ImageBox()
		titleImage.SetParent(self)
		titleImage.AddFlag("not_pick")
		titleImage.LoadImage(ROOT+"title_bio.tga")
		titleImage.SetPosition(10+2+5,30+5+2+10)
		titleImage.Show()
		self.children.append(titleImage)

		titleImageExTitle = ui.ImageBox()
		titleImageExTitle.SetParent(self)
		titleImageExTitle.AddFlag("not_pick")
		titleImageExTitle.LoadImage(ROOT+"bio_gui.tga")
		titleImageExTitle.SetPosition(10+2+5+12,30+5+2+10+140+12)
		titleImageExTitle.Show()
		self.children.append(titleImageExTitle)

		titleImageBiologeTitle = ui.ImageBox()
		titleImageBiologeTitle.SetParent(self)
		titleImageBiologeTitle.AddFlag("not_pick")
		titleImageBiologeTitle.LoadImage(ROOT+"Biologe_render.png")
		titleImageBiologeTitle.SetPosition(18+2+5+12,30+5+2+10+140+140)
		titleImageBiologeTitle.Show()
		self.children.append(titleImageBiologeTitle)
		
		titleImageBiologe2Title = ui.ImageBox()
		titleImageBiologe2Title.SetParent(self)
		titleImageBiologe2Title.AddFlag("not_pick")
		titleImageBiologe2Title.LoadImage(ROOT+"Biologe_render2.png")
		titleImageBiologe2Title.SetPosition(230+2+5+12,30+5+2+10+140+140)
		titleImageBiologe2Title.Show()
		self.children.append(titleImageBiologe2Title)
		
		titleImageBiologeHintergrundTitle = ui.ImageBox()
		titleImageBiologeHintergrundTitle.SetParent(self)
		titleImageBiologeHintergrundTitle.AddFlag("not_pick")
		titleImageBiologeHintergrundTitle.LoadImage(ROOT+"bio_hintergrund.tga")
		titleImageBiologeHintergrundTitle.SetPosition(10+2+5+12,30+5+2+10+140-85)
		titleImageBiologeHintergrundTitle.Show()
		self.children.append(titleImageBiologeHintergrundTitle)

		titleImageEx = ui.ImageBox()
		titleImageEx.SetParent(self)
		titleImageEx.AddFlag("not_pick")
		titleImageEx.LoadImage(ROOT+"title_bio2.tga")
		#titleImageEx.SetPosition(13+2+5,30+5+2+10+140+60)
		titleImageEx.SetPosition(20+2+5,30+5+2+10+140+60)
		titleImageEx.Show()
		self.children.append(titleImageEx)

		#titleImageTitle = ui.ImageBox()
		#titleImageTitle.SetParent(self)
		#titleImageTitle.AddFlag("not_pick")
		#titleImageTitle.LoadImage(ROOT+"bio_gui_ex.tga")
		#titleImageTitle.SetPosition(10+2+5+12+10,30+5+2+10+30)
		#titleImageTitle.Show()
		#self.children.append(titleImageTitle)
		
		titleImageTitle = ui.ImageBox()
		titleImageTitle.SetParent(self)
		titleImageTitle.AddFlag("not_pick")
		titleImageTitle.LoadImage(ROOT+"slot_unavailable.png")
		titleImageTitle.SetPosition(15+2+5+12+10,30+5+2+10+58)
		titleImageTitle.Show()
		self.children.append(titleImageTitle)

		shopBtn = ui.Button()
		shopBtn.SetParent(self)
		shopBtn.SetUpVisual(ROOT+"new_shop_normal.png")
		shopBtn.SetOverVisual(ROOT+"new_shop_hover.png")
		shopBtn.SetDownVisual(ROOT+"new_shop_down.png")
		shopBtn.SAFE_SetEvent(self.OpenShop)
		shopBtn.SetPosition(10+2+5+12+10+215,30+5+2+10+30+32)
		shopBtn.Show()
		self.children.append(shopBtn)

		clickBtn = ui.Button()
		clickBtn.SetParent(self)
		clickBtn.SetUpVisual(ROOT+"bio_click_btn_0.tga")
		clickBtn.SetOverVisual(ROOT+"bio_click_btn_1.tga")
		clickBtn.SetDownVisual(ROOT+"bio_click_btn_2.tga")
		clickBtn.SetText(localeInfo.BIO_GIVE_MISSION)
		clickBtn.SAFE_SetEvent(self.GiveMission)
		clickBtn.SetPosition(-7+2+5+12+10+65,30+5+2+10+30+5+70)
		clickBtn.Show()
		self.children.append(clickBtn)

		self.unutkanlikIcon = ui.ImageBox()
		self.unutkanlikIcon.SetParent(self)
		self.unutkanlikIcon.SetPosition(10+2+5+12+10+160,30+5+2+10+30+30)
		
		self.unutkanlikIcon.SAFE_SetStringEvent("MOUSE_OVER_OUT",self.OverOutItem)
		self.unutkanlikIcon.Show()


		self.checkBoxUnutkanlik = ui.CheckBox()
		self.checkBoxUnutkanlik.SetParent(self)
		self.checkBoxUnutkanlik.SetPosition(10+2+5+12+10+140,30+5+2+10+30+38)
		self.checkBoxUnutkanlik.SetEvent(ui.__mem_func__(self.CheckBoxEvent), "ON_CHECK", "UNUTKANLIK",True)
		self.checkBoxUnutkanlik.SetEvent(ui.__mem_func__(self.CheckBoxEvent), "ON_UNCKECK","UNUTKANLIK", False)
		self.checkBoxUnutkanlik.SetCheckStatus(UNUTKANLIK_STATUS)
		self.checkBoxUnutkanlik.Show()

		self.ozutIcon = ui.ImageBox()
		self.ozutIcon.SetParent(self)
		self.ozutIcon.SetPosition(10+2+5+12+10+90,30+5+2+10+30+30)
		self.ozutIcon.SAFE_SetStringEvent("MOUSE_OVER_OUT",self.OverOutItem)
		self.ozutIcon.Show()

		self.checkBoxOzut = ui.CheckBox()
		self.checkBoxOzut.SetParent(self)
		self.checkBoxOzut.SetPosition(10+2+5+12+10+70,30+5+2+10+30+38)
		self.checkBoxOzut.SetEvent(ui.__mem_func__(self.CheckBoxEvent), "ON_CHECK", "OZUT",True)
		self.checkBoxOzut.SetEvent(ui.__mem_func__(self.CheckBoxEvent), "ON_UNCKECK","OZUT", False)
		self.checkBoxOzut.SetCheckStatus(OZUT_STATUS)
		self.checkBoxOzut.Show()

		self.missionIcon = ui.ImageBox()
		self.missionIcon.SetParent(self)
		#item.SelectItem(50300)
		#if item.GetIconImageFileName().find("gr2") == -1:
		#	self.missionIcon.LoadImage(item.GetIconImageFileName())
		#else:
		#	self.missionIcon.LoadImage("icon/item/27995.tga")
		#self.missionIcon.SAFE_SetStringEvent("MOUSE_OVER_IN",self.OverInItem,50300)
		self.missionIcon.SetPosition(10+2+5+12+10,30+5+2+10+30+10)
		self.missionIcon.SAFE_SetStringEvent("MOUSE_OVER_OUT",self.OverOutItem)
		self.missionIcon.Show()

		self.checkBoxCall = ui.CheckBox()
		self.checkBoxCall.SetParent(self)
		self.checkBoxCall.SetPosition(10+2+5+12+10+225,30+5+2+10+30+133)
		#self.checkBoxCall.SetPosition(10+2+5+12,30+5+2+10+140+12)
		self.checkBoxCall.SetEvent(ui.__mem_func__(self.CheckBoxEvent), "ON_CHECK", "CALL",True)
		self.checkBoxCall.SetEvent(ui.__mem_func__(self.CheckBoxEvent), "ON_UNCKECK","CALL", False)
		self.checkBoxCall.SetCheckStatus(CALLBACK_MISSION)
		self.checkBoxCall.Show()


		self.missionName = ui.TextLine()
		self.missionName.AddFlag("not_pick")
		self.missionName.SetParent(self)
		self.missionName.SetPosition(10+2+5+152,30+5+2+10+7)
		self.missionName.SetHorizontalAlignCenter()
		self.missionName.Show()

		self.statusText = ui.TextLine()
		self.statusText.AddFlag("not_pick")
		self.statusText.SetParent(self)
		self.statusText.SetPosition(12+2+5+12+115,30+5+2+10+140-38+63)
		self.statusText.SetText(localeInfo.BIO_CAN_GIVE_ITEM)
		self.statusText.SetHorizontalAlignCenter()
		self.statusText.Show()

		self.missionGiftText = ui.TextLine()
		self.missionGiftText.AddFlag("not_pick")
		self.missionGiftText.SetParent(self)
		self.missionGiftText.SetPosition(10+2+5+152,30+5+2+10+140+95)
		#self.missionGiftText.SetPosition(20+2+5,30+5+2+10+140+60)
		self.missionGiftText.SetText(self.GetAffectString(1,10))
		self.missionGiftText.SetHorizontalAlignCenter()
		self.missionGiftText.Show()

		giftText = ui.TextLine()
		giftText.AddFlag("not_pick")
		giftText.SetParent(self)
		giftText.SetPosition(10+2+5+152,30+5+2+10+140+65)
		giftText.SetText(localeInfo.BIO_GIFT)
		giftText.SetHorizontalAlignCenter()
		giftText.Show()
		self.children.append(giftText)

		self.giftFirst = ui.Button()
		self.giftFirst.SetParent(self)
		self.giftFirst.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.giftFirst.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.giftFirst.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.giftFirst.SetEvent(lambda x = 0: self.ClickGift(x))
		self.giftFirst.SetPosition(10+2+5+10+10,30+5+2+10+140+30+70)
		self.giftFirst.Hide()

		self.giftSecond = ui.Button()
		self.giftSecond.SetParent(self)
		self.giftSecond.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.giftSecond.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.giftSecond.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.giftSecond.SetEvent(lambda x = 1: self.ClickGift(x))
		self.giftSecond.SetPosition(10+2+5+10+90+10,30+5+2+10+140+30+70)
		self.giftSecond.Hide()

		self.giftThird = ui.Button()
		self.giftThird.SetParent(self)
		self.giftThird.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.giftThird.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.giftThird.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.giftThird.SetEvent(lambda x = 2: self.ClickGift(x))
		self.giftThird.SetPosition(10+2+5+10+90+90+10,30+5+2+10+140+30+70)
		self.giftThird.Hide()

	def CheckBoxEvent(self, name, type, flag):
		if type == "OZUT":
			OZUT_STATUS=flag
		elif type == "UNUTKANLIK":
			UNUTKANLIK_STATUS=flag
		elif type == "CALL":
			CALLBACK_MISSION=flag

	def OverOutItem(self):
		interface = constInfo.GetInterfaceInstance()
		if interface:
			if interface.tooltipItem:
				interface.tooltipItem.HideToolTip()

	def OverInItem(self, index):
		interface = constInfo.GetInterfaceInstance()
		if interface:
			if interface.tooltipItem:
				interface.tooltipItem.SetItemToolTip(index)
				interface.tooltipItem.ShowToolTip()

	def GetAffectString(self, affectType, affectValue):
		if not affectType:
			return "None"
		try:
			return ItemToolTip.AFFECT_DICT[affectType](affectValue)
		except TypeError:
			return "UNKNOWN_VALUE[{}] {}".format(affectType, affectValue)
		except KeyError:
			return "UNKNOWN_TYPE[{}] {}".format(affectType, affectValue)

	def isDifferentText(self, index):
		if index == 7:
			self.missionGiftText.SetText(localeInfo.BIO_ALL_DEFENSE_CHARACTER % 10)
			return True
		elif index == 8:
			self.missionGiftText.SetText(localeInfo.BIO_ALL_ATT_CHARACTER % 10)
			return True
		return False

	def LoadData(self, level, count, time):
		global bio_data
		if level == 0 or level > len(bio_data):
			self.LoadEmpty()
			return

		item.SelectItem(bio_data[level][1])

		self.missionName.SetText(item.GetItemName()+ "("+str(count)+"/"+str(bio_data[level][2])+")")

		if level != self.bioLevel:
			if item.GetIconImageFileName().find("gr2") == -1:
				self.missionIcon.LoadImage(item.GetIconImageFileName())
				self.missionIcon.SAFE_SetStringEvent("MOUSE_OVER_IN",self.OverInItem,bio_data[level][1])
				self.missionIcon.SetPosition(14+2+5+12+10,30+5+2+10+30+10+20)
				self.missionIcon.Show()
			else:
				self.missionIcon.Hide()

			item.SelectItem(bio_data[level][15])
			if item.GetIconImageFileName().find("gr2") == -1:
				self.ozutIcon.LoadImage(item.GetIconImageFileName())
				self.ozutIcon.SAFE_SetStringEvent("MOUSE_OVER_IN",self.OverInItem,bio_data[level][15])
				self.ozutIcon.Show()
				self.checkBoxOzut.Show()
			else:
				self.ozutIcon.Hide()
				self.checkBoxOzut.Hide()

			item.SelectItem(bio_data[level][16])
			if item.GetIconImageFileName().find("gr2") == -1:
				self.unutkanlikIcon.LoadImage(item.GetIconImageFileName())
				self.unutkanlikIcon.SAFE_SetStringEvent("MOUSE_OVER_IN",self.OverInItem,bio_data[level][16])
				self.unutkanlikIcon.Show()
				self.checkBoxUnutkanlik.Show()
			else:
				self.unutkanlikIcon.Hide()
				self.checkBoxUnutkanlik.Hide()

		self.bioLevel = level
		self.bioCount = count
		self.bioTime = time
		self.needUpdate = False

		if self.checkBoxCall.GetCheckStatus():
			if not self.IsShow():
				game = constInfo.GetGameInstance()
				if game != None:
					game.AddLoopEvent("bio",ui.__mem_func__(self.OnUpdate))

		if self.isDifferentText(level) == False:
			affText = ""
			if bio_data[level][6] != 0:
				affText += self.GetAffectString(bio_data[level][6],bio_data[level][7])+" , "
			if bio_data[level][8] != 0:
				affText += self.GetAffectString(bio_data[level][8],bio_data[level][9])+" , "
			if bio_data[level][10] != 0:
				affText += self.GetAffectString(bio_data[level][10],bio_data[level][11])+" , "
			if bio_data[level][12] != 0:
				affText += self.GetAffectString(bio_data[level][12],bio_data[level][13])+" , "
			self.missionGiftText.SetText(affText[:-2])
		self.missionGiftText.Show()

		self.giftFirst.Hide()
		self.giftSecond.Hide()
		self.giftThird.Hide()

	def LoadStone(self, level):
		global bio_data
		if level == 0 or level > len(bio_data):
			self.LoadEmpty()
			return

		item.SelectItem(bio_data[level][1])
		self.missionName.SetText(item.GetItemName()+ "("+str(bio_data[level][2])+"/"+str(bio_data[level][2])+")")

		item.SelectItem(bio_data[level][5])
		
		text = self.missionName.GetText()
		text += " - "+item.GetItemName()
		self.missionName.SetText(text)
		if item.GetIconImageFileName().find("gr2") == -1:
			self.missionIcon.LoadImage(item.GetIconImageFileName())
			self.missionIcon.SAFE_SetStringEvent("MOUSE_OVER_IN",self.OverInItem,bio_data[level][5])
			self.missionIcon.SetPosition(14+2+5+12+10,30+5+2+10+30+10+20)
			self.missionIcon.Show()
		else:
			self.missionIcon.Hide()

		self.bioLevel = level
		self.bioCount = 0
		self.bioTime = 0
		self.needUpdate = True

		if self.isDifferentText(level) == False:
			affText = ""
			if bio_data[level][6] != 0:
				affText += self.GetAffectString(bio_data[level][6],bio_data[level][7])+" , "
			if bio_data[level][8] != 0:
				affText += self.GetAffectString(bio_data[level][8],bio_data[level][9])+" , "
			if bio_data[level][10] != 0:
				affText += self.GetAffectString(bio_data[level][10],bio_data[level][11])+" , "
			if bio_data[level][12] != 0:
				affText += self.GetAffectString(bio_data[level][12],bio_data[level][13])+" , "
			self.missionGiftText.SetText(affText[:-2])
		self.missionGiftText.Show()

		self.unutkanlikIcon.Hide()
		self.checkBoxUnutkanlik.Hide()
		self.ozutIcon.Hide()
		self.checkBoxOzut.Hide()

		self.giftFirst.Hide()
		self.giftSecond.Hide()
		self.giftThird.Hide()

		self.statusText.SetText(localeInfo.BIO_FIND_STONE)

	def LoadGift(self, level):
		global bio_data
		if level == 0 or level > len(bio_data):
			self.LoadEmpty()
			return
		item.SelectItem(bio_data[level][1])
		self.missionName.SetText(item.GetItemName()+ "("+str(bio_data[level][2])+"/"+str(bio_data[level][2])+")")
		if bio_data[level][5] != 0:
			item.SelectItem(bio_data[level][5])
			if item.GetIconImageFileName().find("gr2") == -1:
				self.missionIcon.LoadImage(item.GetIconImageFileName())
				self.missionIcon.SAFE_SetStringEvent("MOUSE_OVER_IN",self.OverInItem,bio_data[level][5])
				self.missionIcon.SetPosition(14+2+5+12+10,30+5+2+10+30+10+20)
				self.missionIcon.Show()
			else:
				self.missionIcon.Hide()
		else:
			item.SelectItem(bio_data[level][1])
			if item.GetIconImageFileName().find("gr2") == -1:
				self.missionIcon.LoadImage(item.GetIconImageFileName())
				self.missionIcon.SAFE_SetStringEvent("MOUSE_OVER_IN",self.OverInItem,bio_data[level][1])
				self.missionIcon.SetPosition(14+2+5+12+10,30+5+2+10+30+10+20)
				self.missionIcon.Show()
			else:
				self.missionIcon.Hide()
		self.bioLevel = level
		self.bioCount = 0
		self.bioTime = 0
		self.needUpdate = True
		self.statusText.SetText(localeInfo.BIO_CHOOSE_GIFT)
		self.missionGiftText.Hide()
		self.unutkanlikIcon.Hide()
		self.checkBoxUnutkanlik.Hide()
		self.ozutIcon.Hide()
		self.checkBoxOzut.Hide()
		self.giftFirst.SetText(self.GetAffectString(bio_data[level][6],bio_data[level][7]))
		self.giftFirst.Show()
		self.giftSecond.SetText(self.GetAffectString(bio_data[level][8],bio_data[level][9]))
		self.giftSecond.Show()
		self.giftThird.SetText(self.GetAffectString(bio_data[level][10],bio_data[level][11]))
		self.giftThird.Show()

	def LoadEmpty(self):
		self.missionIcon.Hide()
		self.unutkanlikIcon.Hide()
		self.checkBoxUnutkanlik.Hide()
		self.ozutIcon.Hide()
		self.checkBoxOzut.Hide()
		self.missionName.SetText("-")
		self.missionGiftText.SetText("-")
		self.statusText.SetText(localeInfo.BIO_DONT_HAVE_MISSION)
		self.bioLevel = 0
		self.bioCount = 0
		self.bioTime = 0
		self.needUpdate = True
		self.giftFirst.Hide()
		self.giftSecond.Hide()
		self.giftThird.Hide()

	def OpenShop(self):
		net.SendChatPacket("/open_shop 107")

	def GiveMission(self):
		if self.bioLevel == 0:
			#chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.BIO_CANT_MISSION % 30)
			return
		elif player.GetStatus(player.LEVEL) < bio_data[self.bioLevel][0]:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.BIO_CANT_MISSION % bio_data[self.bioLevel][0])
			return
		net.SendChatPacket("/bio mission %d %d"%(self.checkBoxOzut.GetCheckStatus(),self.checkBoxUnutkanlik.GetCheckStatus()))

	def ClickGift(self, index):
		net.SendChatPacket("/bio gift %d"%index)

	def OnUpdate(self):
		if not self.needUpdate:
			if self.bioTime == 0:
				self.statusText.SetText(localeInfo.BIO_CAN_GIVE_ITEM)
				self.needUpdate = True
				return True

			time = self.bioTime-app.GetGlobalTimeStamp()
			if time <= 0:
				if not self.IsShow():
					game = constInfo.GetGameInstance()
					if game != None:
						game.BINARY_OnRecvBulkWhisper("[Biolog] - "+localeInfo.BIO_CAN_GIVE_ITEM)

				self.statusText.SetText(localeInfo.BIO_CAN_GIVE_ITEM)
				self.needUpdate = True
				return True
			else:
				text = "%02d:%02d:%02d"%(constInfo.minutetohour(time),constInfo.minutetominute(time),constInfo.minutetosecond(time))
				self.statusText.SetText(localeInfo.BIO_CANT_GIVE_ITEM %text)
				return False
		return True

	def Open(self):
		self.Show()
		self.SetCenterPosition()
		self.SetTop()

		game = constInfo.GetGameInstance()
		if game != None:
			game.RemoveLoopEvent("bio")

	def Close(self):
		self.Hide()

		if self.checkBoxCall.GetCheckStatus():
			if not self.IsShow():
				game = constInfo.GetGameInstance()
				if game != None:
					game.AddLoopEvent("bio",ui.__mem_func__(self.OnUpdate))

	def OnPressEscapeKey(self):
		self.Close()
