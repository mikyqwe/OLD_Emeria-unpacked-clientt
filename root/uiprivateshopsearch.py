import app
import ui
import uiScriptLocale
import uiToolTip
import mouseModule
import constInfo
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import skill
import net
import player
import item
import privateShopSearch
import chr
import effect
import dbg
import background
import uiDropDown
from _weakref import proxy
from itertools import islice
import math
import chat
import uiMessenger
class PrivateShopSearchDialog(ui.ScriptWindow):

	class SearchResultItem(ui.Window):

		def __init__(self, parent, index):
			ui.Window.__init__(self)
			
			self.parent = parent
			
			self.isLoad = True
			self.isSelected = False

			self.index = index

			self.itemID = 0
			self.itemVnum = 0
			# if app.ENABLE_CHANGE_LOOK_SYSTEM:
				# self.lookvnum = 0
			self.shopVid = 0
			self.shopItemPos = 0
			self.metinSlot = 0
			self.attrSlot = 0
			self.effectID = 0
			self.priceInt = 0
			self.pricevnum = 0
			self.pricecount = 0
			self.imageName = None
			self.SetParent(parent)
			self.InitItem()

			
		def InitItem(self):
			startX = 0
			yPos = 1
			
			self.itemImage = ui.MakeImageBox(self, "d:/ymir work/ui/tab_01.tga", 0, yPos+2)
			self.itemImage.SAFE_SetStringEvent("MOUSE_OVER_IN",self.__OverInItem)
			self.itemImage.SAFE_SetStringEvent("MOUSE_OVER_OUT",self.__OverOutItem)
			self.itemImage.SAFE_SetStringEvent("MOUSE_LEFT_UP",self.__OnSelect)
			self.itemImage.SetTop()
			self.itemImage.Show()

			self.itemIcon2 = ui.CookiesScaleBox(self,item.GetIconImageFileName(),75,0,0.7,0.7)

			self.text = ui.TextLine()
			self.text.SetParent(self)
			self.text.SetPosition(startX+180, yPos+15)
			self.text.SetHorizontalAlignCenter()
			self.text.Show()
			
			self.seller = ui.TextLine()
			self.seller.SetParent(self)
			self.seller.SetPosition(startX+331, yPos+15)
			self.seller.SetHorizontalAlignCenter()
			self.seller.Show()
	
			self.message = ui.Button()
			self.message.SetParent(self)
			self.message.SetUpVisual("d:/ymir work/ui/privatesearch/mail_normal_closed.tga")
			self.message.SetOverVisual("d:/ymir work/ui/privatesearch/mail_normal_opend.tga")
			self.message.SetDownVisual("d:/ymir work/ui/privatesearch/mail_normal_closed.tga")
			self.message.SetEvent(ui.__mem_func__(self.__ClickName))
			self.message.SetPosition(startX+353, yPos+9)
			self.message.Show()

			self.count = ui.TextLine()
			self.count.SetParent(self)
			self.count.SetPosition(startX+431, yPos+15)
			self.count.SetHorizontalAlignCenter()
			self.count.Show()

			self.price = ui.TextLine()
			self.price.SetParent(self)
			self.price.SetPosition(startX+551, yPos+15)
			self.price.SetHorizontalAlignCenter()
			self.price.Show()
	
			self.buyButton_sub = ui.Button()
			self.buyButton_sub.SetParent(self)
			self.buyButton_sub.SetUpVisual("d:/ymir work/ui/privatesearch/money.tga")
			self.buyButton_sub.SetOverVisual("d:/ymir work/ui/privatesearch/money_02.tga")
			self.buyButton_sub.SetDownVisual("d:/ymir work/ui/privatesearch/money_03.tga")
			self.buyButton_sub.SetEvent(PrivateShopSearchDialog().BuySelectedItem)
			self.buyButton_sub.SetPosition(startX+637, yPos+9)
			self.buyButton_sub.Show()
	
			self.tooltipItem = uiToolTip.ItemToolTip()
			self.tooltipItem.Hide()
			
			self.SetSize(self.itemImage.GetWidth(), self.itemImage.GetHeight())
			
		def __OverOutItem(self):
			if not self.isSelected:
				self.itemImage.LoadImage("d:/ymir work/ui/tab_01.tga")		
			
			else:
				self.isSelected = False
				self.isLoad = True
				
			if None != self.tooltipItem:
				self.tooltipItem.HideToolTip()
			
		def __OverInItem(self):
			if not self.isSelected:
				self.itemImage.LoadImage("d:/ymir work/ui/tab_02.tga")
				self.isSelected = True
				self.isLoad = True
				self.parent.OnSearchResultItemSelect(self.index)
				
			if None == self.tooltipItem:
				return
			
			self.tooltipItem.ClearToolTip()
			self.tooltipItem.AppendItemIcon(self.GetIconImage())
			self.tooltipItem.AlignHorizonalCenter()
			# if app.ENABLE_CHANGE_LOOK_SYSTEM:
				# if(self.lookvnum > 0):
					# self.tooltipItem.AddItemData(self.itemVnum, self.metinSlot, self.attrSlot, 0, 0, player.GLASS, self.lookvnum)
				# else:
					# self.tooltipItem.AddItemData(self.itemVnum, self.metinSlot, self.attrSlot, 0, 0, 1)
			# else:	
			self.tooltipItem.AddItemData(self.itemVnum, self.metinSlot, self.attrSlot, 0, 0, 1)
				
			# if app.ENABLE_RENEWAL_SHOPEX:
				# PriceType = self.pricevnum
				# PriceCount = self.pricecount
				# if(PriceType > 1):
					# self.tooltipItem.AddSHOPEXItem(int(PriceType),int(self.priceInt),int(PriceCount))	
				# else:
			self.tooltipItem.AppendPrice(self.priceInt)
			self.tooltipItem.ShowToolTip()
					
		def __ClickName(self):
			net.SendChatPacket("/searchmessenger "+self.GetSeller())
				
		def SetItemName(self, name):
			self.text.SetText(name)

		def SetCount(self, count):
			self.count.SetText(count)
		
		def SetPrice(self, price):
			self.price.SetText(price)
			
		def SetPriceInt(self, price):
			self.priceInt = price
	
		def GetPriceInt(self):
			return self.priceInt
	
		def SetPriceVnum(self, price):		
			self.pricevnum = price	

		def SetPriceCount(self, count):		
			self.pricecount = count	
	
		def GetPriceVnum(self):		
			return self.pricevnum

		def GetPriceCount(self):		
			return self.pricecount
	
		def SetSeller(self, seller):
			self.seller.SetText(seller)
			
		def GetSeller(self):
			return self.seller.GetText()
			
		def SetIconImage(self, name):
			self.imageName = name
		
		def GetIconImage(self):
			return self.imageName
			
		def SetMetinSlot(self, metinSlot):
			self.metinSlot = metinSlot

		def SetAttrSlot(self, attrSLot):
			self.attrSlot = attrSLot
			
		def SetShopVid(self, vid):
			self.shopVid = vid

		def GetShopVid(self):
			return self.shopVid
			
		def SetItemVnum(self, vnum):
			self.itemVnum = vnum
			
		def GetShopItemVnum(self):
			return self.itemVnum	
	
		# if app.ENABLE_CHANGE_LOOK_SYSTEM:
			# def SetItemDwVnum(self, vnum):
				# self.lookvnum = vnum

		def GetShopItemPos(self):
			return self.shopItemPos
		
		def SetShopItemPos(self, itemPos):
			self.shopItemPos = itemPos

		def __OnSelect(self):
			self.parent.OnSearchResultItemSelect(self.index)

		def Select(self):
			self.isSelected = True
			self.isLoad = True

		def UnSelect(self):
			self.isSelected = False
			self.isLoad = True

		def OnUpdate(self):
			pass

		def OnRender(self):
			if self.isLoad:
				if self.isSelected:
					self.itemImage.LoadImage("d:/ymir work/ui/tab_02.tga")
				else:
					self.itemImage.LoadImage("d:/ymir work/ui/tab_01.tga")
				self.isLoad = False


	def __init__(self):
		ui.ScriptWindow.__init__(self)	

		self.selectedItemIndex = -1
		self.board = None
		self.minLevel = None
		self.maxLevel = None
		self.minRefine = None
		self.maxRefine = None
		self.minPrice = None
		self.maxPrice = None
		self.itemNameSearch = None
		self.filter = None
		self.boardFilter = None
		self.searchResultItems = []
		self.currentItemCat = item.ITEM_TYPE_WEAPON
		self.currentSubItemCat = item.WEAPON_SWORD
		self.currentJob = 0
		self.itemDataList = []
		self.listBoxCubeItemsLEN = 0
		self.arrayPos = 0
		self.boardfilterShow = False
		self.liste = []
		self.currentPage = 1
		self.pageCount = 1
		self.perPage = 9
		self.itemCount = 0
		self.all = 0
		self.LoadWindow()
		constInfo.OffShopSearch = 0
		self.tooltip = uiToolTip.ItemToolTip()
		self.tooltip.Hide()	
		
	def __del__(self):
		self.Destroy()
		ui.ScriptWindow.__del__(self)
					
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PrivateShopSearchDialog.py")
		except:
			import exception
			exception.Abort("PrivateShopSearchDialog.LoadDialog.LoadScript")

		try:
			GetObject=self.GetChild#warn das gleiche anzahl an zahlen ? 12 und da? 12hmm 
			self.board = GetObject("board")
			self.minLevel = GetObject("minLevelValue")
			self.maxLevel = GetObject("maxLevelValue")
			self.minRefine = GetObject("minrefineValue")
			self.maxRefine = GetObject("maxrefineValue")
			self.minPrice = GetObject("GoldminValue")
			self.maxPrice = GetObject("GoldmaxValue")
			self.itemNameSearch = GetObject("ItemNameValue")
			self.itemNameSearch.SAFE_SetReturnEvent(self.StartSearch)
			
			self.filter = GetObject("Filter")
			self.filter.SetEvent(ui.__mem_func__(self.OpenFilter))
			self.filter.Show()
			
			self.boardFilter =  GetObject("BoardFilter")
			self.boardFilter.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClickFilter))
			self.boardFilter.Hide()
			
			self.pageButtons = []
			self.pageButtons.append(GetObject("page1_button"))
			self.pageButtons.append(GetObject("page2_button"))
			self.pageButtons.append(GetObject("page3_button"))
			self.pageButtons.append(GetObject("page4_button"))
			self.pageButtons.append(GetObject("page5_button"))

			self.pageButtons[0].Show()
			self.pageButtons[1].Hide()
			self.pageButtons[2].Hide()
			self.pageButtons[3].Hide()
			self.pageButtons[4].Hide()
			self.pageButtons[0].Down()
			self.pageButtons[0].Disable()

			self.searchButton = GetObject("SearchButton")
			self.searchButton.SetEvent(ui.__mem_func__(self.StartSearch))

			self.buyButton = GetObject("BuyButton")
			self.buyButton.SetEvent(ui.__mem_func__(self.BuySelectedItem))
			self.buyButton.Hide()
			
			self.nextButton = GetObject("next_button")
			self.lastButton = GetObject("last_next_button")
			self.prevButton = GetObject("prev_button")
			self.firstButton = GetObject("first_prev_button")
			
			self.nextButton.SetEvent(ui.__mem_func__(self.NextPage))
			self.prevButton.SetEvent(ui.__mem_func__(self.PrevPage))
			self.firstButton.SetEvent(ui.__mem_func__(self.FirstPage))
			self.lastButton.SetEvent(ui.__mem_func__(self.LastPage))
			
			self.board.SetCloseEvent(ui.__mem_func__(self.__OnCloseButtonClick))
			

			listBoxCube = uiDropDown.DropdownTree()
			listBoxCube.SetParent(self)
			listBoxCube.SetPosition(15,35+40)
			listBoxCube.SetSize(100, 28)
			listBoxCube.SetItemSize(160, 28)
			listBoxCube.SetViewItemCount(12)
			listBoxCube.Show()
			self.listBoxCube = listBoxCube
			
			
			scrollBarListBoxCube = ui.ScrollBarShop()
			scrollBarListBoxCube.SetParent(self)
			#scrollBarListBoxCube.SetPosition(179,35+25)
			#scrollBarListBoxCube.SetScrollBarSize(-900)
			#scrollBarListBoxCube.Show()
			self.scrollBarListBoxCube = scrollBarListBoxCube
						
			self.listBoxCube.SetScrollBar(self.scrollBarListBoxCube)

			listBoxCubeItems = [
				{ 
					'item' : self.CreateNewMenuTab1(localeInfo.PRIVATESHOPSEARCH_ALL, lambda arg = ("1"): self.SetTextLineCubeNew(arg)), 
				},
				{ 
					'item' : self.CreateNewMenuTab2(localeInfo.PRIVATESHOPSEARCH_WEAPONS, None), 
					'children' : (
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_ONEHANDED, lambda arg = ("2 1"): self.SetTextLineCube(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_TWOHANDED, lambda arg = ("2 2"): self.SetTextLineCube(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_BELL, lambda arg = ("2 6"): self.SetTextLineCube(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_FAN, lambda arg = ("2 5"): self.SetTextLineCube(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_BOW, lambda arg = ("2 4"): self.SetTextLineCube(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_DAGGER, lambda arg = ("2 3"): self.SetTextLineCube(arg)),
						},
					)
				},
				{ 
					'item' : self.CreateNewMenuTab3(localeInfo.PRIVATESHOPSEARCH_ARMOR, None), 
					'children' : (
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.JOB_WARRIOR, lambda arg = ("3 1"): self.SetTextLineCube(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.JOB_ASSASSIN, lambda arg = ("3 2"): self.SetTextLineCube(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.JOB_SURA, lambda arg = ("3 3"): self.SetTextLineCube(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.JOB_SHAMAN, lambda arg = ("3 4"): self.SetTextLineCube(arg)),
						},
					)
				},
				{ 
					'item' : self.CreateNewMenuTab4(localeInfo.PRIVATESHOPSEARCH_JEWELRY, None), 
					'children' : (
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_WRIST, lambda arg = ("4 6"): self.SetTextLineCube(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_NECK, lambda arg = ("4 2"): self.SetTextLineCube(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_EAR, lambda arg = ("4 3"): self.SetTextLineCube(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_FOOTS, lambda arg = ("4 5"): self.SetTextLineCube(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_SHIELD, lambda arg = ("4 1"): self.SetTextLineCube(arg)),
						},
					)
				},
				{ 
					'item' : self.CreateNewMenuTab13(localeInfo.PRIVATESHOPSEARCH_HELMES,None), 
					'children' : (
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_HEAD_WARRIOR, lambda arg = ("12 1"): self.SetTextLineCubeNew(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_HEAD_NINJA, lambda arg = ("12 2"): self.SetTextLineCubeNew(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_HEAD_SURA, lambda arg = ("12 3"): self.SetTextLineCubeNew(arg)),
						},
						{
							'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_HEAD_SCHAMAN, lambda arg = ("12 4"): self.SetTextLineCubeNew(arg)),
						},
					)
				},
				{ 
					'item' : self.CreateNewMenuTab5(localeInfo.PRIVATESHOPSEARCH_COSTUMES,None), 
					'children' : (

							{
								'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_ARMOR_COSTUME, lambda arg = ("11 1"): self.SetTextLineCube(arg)),
							},
							{
								'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_HAIR_COSTUME, lambda arg = ("11 2"): self.SetTextLineCube(arg)),
							},
						)
				},
				{ 
					'item' : self.CreateNewMenuTab14(localeInfo.PRIVATESHOPSEARCH_WEAPON_SKINS,None), 
					'children' : (

							{
								'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_WEAPON_SKINS_WARRIOR, lambda arg = ("11 3"): self.SetTextLineCube(arg)),
							},
							{
								'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_WEAPON_SKINS_NINJA, lambda arg = ("11 4"): self.SetTextLineCube(arg)),
							},
							{
								'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_WEAPON_SKINS_SURA, lambda arg = ("11 5"): self.SetTextLineCube(arg)),
							},
							{
								'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_WEAPON_SKINS_SCHAMAN, lambda arg = ("11 6"): self.SetTextLineCube(arg)),
							},
						)
				},
				{ 
					'item' : self.CreateNewMenuTab6(localeInfo.PRIVATESHOPSEARCH_SKILLS, None), 
					'children' : (

							{
								'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_SKILLS_BOOK, lambda arg = ("9 1"): self.SetTextLineCube(arg)),
							},
							{
								'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_OTHER_BOOK, lambda arg = ("9 2"): self.SetTextLineCube(arg)),
							},
							{
								'item' : self.CreateCubeMenuTab3Item(localeInfo.PRIVATESHOPSEARCH_EDUCATION, lambda arg = ("9 3"): self.SetTextLineCube(arg)),
							},
						)
				},
				{ 
					'item' : self.CreateNewMenuTab8(localeInfo.PRIVATESHOPSEARCH_METIN, lambda arg = ("6 1"): self.SetTextLineCubeNew(arg)), 
				},
				{ 
					'item' : self.CreateNewMenuTab9(localeInfo.PRIVATESHOPSEARCH_MOUNTS, lambda arg = ("7"): self.SetTextLineCubeNew(arg)), 
				},
				{
					'item' : self.CreateNewMenuTab10(localeInfo.PRIVATESHOPSEARCH_PETS, lambda arg = ("8"): self.SetTextLineCubeNew(arg)),
				},
				{
					'item' : self.CreateNewMenuTab11(localeInfo.PRIVATESHOPSEARCH_UPPITEMS, lambda arg = ("5"): self.SetTextLineCubeNew(arg)),
				},		
			]

			self.listBoxCube.AppendItemList(listBoxCubeItems)
			self.listBoxCube.SetLEN(len(listBoxCubeItems))
			
		except:
			import exception
			exception.Abort("PrivateShopSearchDialog.LoadDialog.BindObject")

	def OnUpdate(self):
		if(constInfo.buyed == 1):
			constInfo.buyed  = 0
			self.BuySelectedItem()

		if(self.minPrice and str(self.minPrice.GetText()) != ""):
			if(long(self.minPrice.GetText())>999999999999999):
				self.minPrice.SetText('999999999999999')
				
		if(self.maxPrice and str(self.maxPrice.GetText()) != ""):
			if(long(self.maxPrice.GetText())>999999999999999):
				self.maxPrice.SetText('999999999999999')
				
	def SetTextLineCube(self, text):
		self.arrayPos = text
		self.RefreshRequest()
		
	def SetTextLineCubeNew(self, text):
		self.arrayPos = text
		self.RefreshRequest()
		
	def CreateCubeMenuTab1Item(self, text, event, offset = 0):
		listboxItem = uiDropDown.CubeMenuTab1(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem

	def CreateCubeMenuTab2Item(self, text, event, offset = 0):
		listboxItem = uiDropDown.CubeMenuTab2(text)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem

	def CreateCubeMenuTab3Item(self, text, event, offset = 0):
		listboxItem = uiDropDown.CubeMenuTab3(text)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem

	def CreateListItem(self, text, event, offset = 0):
		listboxItem = uiDropDown.ListItem(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem

	def CreateSubListItem(self, text, event, offset = 0):
		listboxItem = uiDropDown.SubListItem(text)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
	
	def CreateLastListItem(self, text, event, offset = 0):
		listboxItem = uiDropDown.LastListItem(text)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
	
	def CreateNewMenuTab1(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab1(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
	
	def CreateNewMenuTab2(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab2(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab3(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab3(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab4(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab4(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab5(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab5(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab6(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab6(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab7(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab7(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab8(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab8(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab9(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab9(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab10(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab10(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab11(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab11(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab12(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab12(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab13(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab12(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab14(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab12(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
		
	def CreateNewMenuTab15(self, text, event, offset = 0):
		listboxItem = uiDropDown.NewMenuTab12(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
				
	def Destroy(self):
		self.ClearDictionary()
		self.searchResultItems[:] = [] 
		self.titleBar = None
		constInfo.OffShopSearch = 0
		
	def Open(self, type):
		#if type == 0:
		#	self.buyButton.Hide()
		#else:
		#	self.buyButton.Show()
		self.RefreshMe()
		self.Show()
		constInfo.OffShopSearch = 1
		net.SendChatPacket("/checkresearch 1")
		self.SetCenterPosition()		
			
	def RefreshMe(self):
		background.DeletePrivateShopPos()
		self.itemDataList[:] = []
		self.searchResultItems[:] = []
		self.itemCount = privateShopSearch.GetItemCount()

		for x in xrange(privateShopSearch.GetItemCount()):
			vnum = privateShopSearch.GetSearchItemVnum(x)
			count = privateShopSearch.GetSearchItemCount(x)
			price = long(privateShopSearch.GetSearchItemPrice(x))
			price_vnum = int(privateShopSearch.GetSearchItemPriceVnum(x))
			pricecount = int(privateShopSearch.GetSearchItemPriceCount(x))
			vid = privateShopSearch.GetSearchItemShopVID(x)
			seller = privateShopSearch.GetName(x)#chr.GetNameByVID(x)
			seller = seller[:-5]
			itemPos = privateShopSearch.GetSearchItemPos(x)
			# if app.ENABLE_CHANGE_LOOK_SYSTEM:
				# lookvnum = privateShopSearch.GetSearchItemDwVnum(x)
			metinSlot = []
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlot.append(privateShopSearch.GetSearchItemMetinSocket(x, i))

			attrSlot = []
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				attrSlot.append(privateShopSearch.GetSearchItemAttribute(x, i))
			# if app.ENABLE_CHANGE_LOOK_SYSTEM:
				# self.itemDataList.append((vnum, count, price, seller, metinSlot, attrSlot, itemPos, vid, lookvnum,price_vnum,pricecount))
			# else:
			self.itemDataList.append((vnum, count, price, seller, metinSlot, attrSlot, itemPos, vid))
		
		
		self.pageCount = int(math.ceil(float(self.itemCount) / float(self.perPage)))
		self.currentPaginationPage = 1
		self.paginationPageCount = int(math.ceil(float(self.pageCount) / 5.0 ))
		
		self.FirstPage()
	
	def RefreshList(self):
		background.DeletePrivateShopPos()
		self.selectedItemIndex = -1
		self.RefreshPaginationButtons()
		self.searchResultItems[:] = []
				
		start = (self.currentPage - 1) * self.perPage
		end = ((self.currentPage - 1) * self.perPage) + self.perPage

		currentPageDict = self.itemDataList[start:end]
		basePos = 58
		for x, data in enumerate(currentPageDict):
			vnum = data[0]
			count = data[1]
			price = long(data[2])
			seller = data[3]
			metinSlot = data[4]
			attrSlot = data[5]
			itemPos = data[6]
			vid = data[7]
			# if app.ENABLE_CHANGE_LOOK_SYSTEM:
				# lookvnum = data[8]
			# price_vnum = data[8]
			# pricecount = data[8]
			item.SelectItem(vnum)
						
			resultItem = PrivateShopSearchDialog.SearchResultItem(self, x)
			resultItem.SetPosition(205, basePos)
			resultItem.SetItemVnum(vnum)
			resultItem.SetMetinSlot(metinSlot)
			resultItem.SetAttrSlot(attrSlot)
			if 50300 == vnum:
				skillIndex = metinSlot[0]
				skillName = skill.GetSkillName(skillIndex)
				itemName = skillName + " " + item.GetItemName()
				resultItem.SetItemName(itemName)			
			else:
				# if app.ENABLE_CHANGE_LOOK_SYSTEM:
					# if(lookvnum >1):
						# name = item.GetItemName()
						# item.SelectItem(lookvnum)
						# var=name+" ["+item.GetItemName()+"]"
						# resultItem.SetItemName(var)
						# item.SelectItem(vnum)
					# else:
						# resultItem.SetItemName(item.GetItemName())
				# else:
				resultItem.SetItemName(item.GetItemName())
	
			resultItem.SetIconImage(item.GetIconImageFileName())
			resultItem.SetSeller(seller)
			resultItem.SetCount(str(count))
			# if(price_vnum > 1):
				# item.SelectItem(price_vnum)
				# resultItem.SetPrice( str( str(item.GetItemName())+"(x"+str(pricecount)+")" ))
				# resultItem.SetPriceVnum(price_vnum)
				# resultItem.SetPriceInt(int(price))
				# resultItem.SetPriceCount(int(pricecount))
			# else:
			resultItem.SetPrice( str( str(localeInfo.NumberToMoneyString(long(price)))+" " ) )
			resultItem.SetPriceInt(long(price))
			resultItem.SetShopItemPos(itemPos)
			resultItem.SetShopVid(vid)
			# if app.ENABLE_CHANGE_LOOK_SYSTEM:
				# resultItem.SetItemDwVnum(lookvnum)
			resultItem.Show()
			self.searchResultItems.append(resultItem)

			basePos += 50
		
	def RefreshPaginationButtons(self):
		self.currentPaginationPage = int(math.ceil(float(self.currentPage) / 5.0 ))
		self.shownPages = min(self.pageCount - (5 * (self.currentPaginationPage - 1)), 5)

		for x in xrange(5):
			currentPage = (x + ((self.currentPaginationPage-1) * 5) + 1)
			self.pageButtons[x].SetUp()
			self.pageButtons[x].SetText("%d" % currentPage)
			self.pageButtons[x].SetEvent(lambda arg=currentPage: self.GotoPage(arg))
		
		map(ui.Button.Hide, self.pageButtons)
		map(ui.Button.Enable, self.pageButtons)
		
		for x in xrange(self.shownPages):
			self.pageButtons[x].Show()

		self.pageButtons[(self.currentPage - ((self.currentPaginationPage - 1) * 5)) - 1].Down()
		self.pageButtons[(self.currentPage - ((self.currentPaginationPage - 1) * 5)) - 1].Disable()
	
	def GotoPage(self, page):
		self.currentPage = page
		self.RefreshList()

	def FirstPage(self):
		self.currentPage = 1
		self.RefreshList()
		
	def LastPage(self):
		if len(self.itemDataList):
			self.currentPage = self.pageCount
			self.RefreshList()

	def NextPage(self):
		if self.currentPage < self.pageCount:
			self.currentPage += 1

		self.RefreshList()
			
	def PrevPage(self):
		if self.currentPage > 1:
			self.currentPage -= 1

		self.RefreshList()
	
	def RefreshRequest(self):
		self.StartSearch()
		self.RefreshList()

		
	def OpenFilter(self):
		if(self.boardfilterShow==False):
			privateShopSearch.ClearSearchItems()
			background.DeletePrivateShopPos()
			self.RefreshMe()
			self.boardFilter.Show()
			self.boardFilter.SetTop()
			self.boardfilterShow = True
		else:
			self.boardFilter.Hide()
			self.boardfilterShow = False

	def StartSearch(self):
		if(self.boardfilterShow==True):
			self.boardFilter.Hide()
			self.boardfilterShow = False
		privateShopSearch.ClearSearchItems()
		background.DeletePrivateShopPos()
		self.RefreshMe()
		Race = 0#
		ItemCat = 0#self.currentItemCat
		SubCat = 0#self.currentSubItemCat
		MinLevel = int(self.minLevel.GetText())
		MaxLevel = int(self.maxLevel.GetText())
		MinRefine = int(self.minRefine.GetText())
		MaxRefine = int(self.maxRefine.GetText())
		if(self.minPrice.GetText() != ""):
			MinGold = long(self.minPrice.GetText())
		else:
			return
		if(long(MinGold)>999999999999999):
			MinGold = 999999999999999
			self.minPrice.SetText('999999999999999')	
			# chat.AppendChat(1,"StartSearchmin %d" % MinGold)
		if(self.maxPrice.GetText() != ""):			
			MaxGold = long(self.maxPrice.GetText())
			# chat.AppendChat(1,"StartSearchmin %d" % MaxGold)
		else:
			return
		if(long(MaxGold)>999999999999999):
			MaxGold = 999999999999999
			self.maxPrice.SetText('999999999999999')#
		ItemName = self.itemNameSearch.GetText().replace(" ", "_")
		
		#Waffen-Kategorie
		if(self.arrayPos == "2 1"):#1Hand
			Race = 0
			ItemCat = 1
			SubCat = 0
		elif(self.arrayPos == "2 2"):#2Hand
			Race = 0
			ItemCat = 1
			SubCat = 3
		elif(self.arrayPos == "2 3"):#Dolche
			Race = 1
			ItemCat = 1
			SubCat = 1
		elif(self.arrayPos == "2 4"):#Bogen
			Race = 1
			ItemCat = 1
			SubCat = 2
		elif(self.arrayPos == "2 5"):#Fächer
			Race = 3
			ItemCat = 1
			SubCat = 5
		elif(self.arrayPos == "2 6"):#Glocke
			Race = 3
			ItemCat = 1
			SubCat = 4


		#Rüstung-Kategorie
		elif(self.arrayPos == "3 1"):#Krieger
			Race = 0
			ItemCat = 2
			SubCat = 0
		elif(self.arrayPos == "3 2"):#Ninja
			Race = 1
			ItemCat = 2
			SubCat = 0
		elif(self.arrayPos == "3 3"):#Sura
			Race = 2
			ItemCat = 2
			SubCat = 0
		elif(self.arrayPos == "3 4"):#Schamane
			Race = 3
			ItemCat = 2
			SubCat = 0

		#Schmuck-Kategorie
		elif(self.arrayPos == "4 1"):#Schild
			Race = 0
			ItemCat = 2
			SubCat = 2
		elif(self.arrayPos == "4 2"):#Halskette
			Race = 0
			ItemCat = 2
			SubCat = 5
		elif(self.arrayPos == "4 3"):#Ohrringe
			Race = 0
			ItemCat = 2
			SubCat = 6
		elif(self.arrayPos == "4 5"):#Schuhe
			Race = 0
			ItemCat = 2
			SubCat = 4
		elif(self.arrayPos == "4 6"):#Armbänder
			Race = 0
			ItemCat = 2
			SubCat = 3
			
			
		#Helme-Kategorie
		elif(self.arrayPos == "12 1"):#Helme Krieger
			Race = 0
			ItemCat = 2
			SubCat = 1
		elif(self.arrayPos == "12 2"):#Helme Ninja
			Race = 1
			ItemCat = 2
			SubCat = 1
		elif(self.arrayPos == "12 3"):#Helme Sura
			Race = 2
			ItemCat = 2
			SubCat = 1
		elif(self.arrayPos == "12 4"):#Helme Schamane
			Race = 3
			ItemCat = 2
			SubCat = 1



		#Upp-Items-Kategorie
		elif(self.arrayPos == "5"):#Upp-Items
			Race = 0
			ItemCat = 5
			SubCat = 0


		#Steine-Kategorie		
		elif(self.arrayPos == "6 1"):#Alle Steine
			Race = 0
			ItemCat = 10
			SubCat = 0



		#Mounts-Kategorie
		elif(self.arrayPos == "7"):
			Race = 0
			ItemCat = 28
			SubCat = 4


		#Pets-Kategorie
		elif(self.arrayPos == "8"):
			Race = 0
			ItemCat = 16
			SubCat = 4


		#Bücher-Kategorie
		elif(self.arrayPos == "9 1"):#Fertigkeitsbücher
			Race = 0
			ItemCat = 17
			SubCat = 0
		elif(self.arrayPos == "9 2"):#Andere Bücher
			Race = 0
			ItemCat = 3
			SubCat = 10
		elif(self.arrayPos == "9 3"):#Fortbildung
			Race = 0
			ItemCat = 18
			SubCat = 0


		#Tränke	
		elif(self.arrayPos == "10 1"):#autopot
			Race = 0
			ItemCat = 34
			SubCat = 0		
		elif(self.arrayPos == "10 2"):#other
			Race = 0
			ItemCat = 3
			SubCat = 0


		#Kostüm-Kategorie
		elif(self.arrayPos == "11 1"):#Rüstungs Kostüme
			Race = 0
			ItemCat = 28
			SubCat = 0		
		elif(self.arrayPos == "11 2"):#Haar Kostüme
			Race = True
			ItemCat = 28
			SubCat = 1


		#Waffen-Skins
		elif(self.arrayPos == "11 3"):#Waffenskin Krieger
			Race = 0
			ItemCat = 28
			SubCat = 3
		elif(self.arrayPos == "11 4"):#Waffenskin Ninja
			Race = 1
			ItemCat = 28
			SubCat = 3
		elif(self.arrayPos == "11 5"):#Waffenskin Sura
			Race = 2
			ItemCat = 28
			SubCat = 3
		elif(self.arrayPos == "11 6"):#Waffenskin Schamane
			Race = 3
			ItemCat = 28
			SubCat = 3

		#Skill-Kostüme
		elif(self.arrayPos == "13 1"):#Waffenkostüm Krieger
			Race = True
			ItemCat = 36
			SubCat = True
		elif(self.arrayPos == "13 2"):#Waffenkostüm Ninja
			Race = 1
			ItemCat = 36
			SubCat = 1 or 2 or 3 or 4
		elif(self.arrayPos == "13 3"):#Waffenkostüm Sura
			Race = 2
			ItemCat = 36
			SubCat = 1 or 2 or 3 or 4 or 5
		elif(self.arrayPos == "13 4"):#Waffenkostüm Schamane
			Race = 3
			ItemCat = 36
			SubCat = 1 or 2 or 3 or 4 or 5


		#Alles#
		elif(self.arrayPos == "1"):
			self.all = True

		if len(ItemName):
			net.SendPrivateShopSearchInfoSub(Race, ItemCat, SubCat, MinLevel, MaxLevel, MinRefine, MaxRefine, MinGold, MaxGold, ItemName)
			#chat.AppendChat(chat.CHAT_TYPE_INFO,"Yang %d : %d " % (MinGold,MaxGold ))
		elif self.all:
			net.SendPrivateShopSearchInfoAll(Race, ItemCat, SubCat, MinLevel, MaxLevel, MinRefine, MaxRefine, MinGold, MaxGold)
			#chat.AppendChat(chat.CHAT_TYPE_INFO,"Yang %d : %d " % (MinGold,MaxGold ))
		else:
			net.SendPrivateShopSearchInfo(Race, ItemCat, SubCat, MinLevel, MaxLevel, MinRefine, MaxRefine, MinGold, MaxGold)
			#chat.AppendChat(chat.CHAT_TYPE_INFO,"Yang %d : %d " % (MinGold,MaxGold ))
		self.all = False	
		self.Children.append(self.searchResultItems)
		
	def BuySelectedItem(self):
		if self.selectedItemIndex == -1:
			constInfo.buyed = 1
			return
		shopVid = self.searchResultItems[self.selectedItemIndex].GetShopVid()
		shopItemPos = self.searchResultItems[self.selectedItemIndex].GetShopItemPos()
		shopItemVnum = self.searchResultItems[self.selectedItemIndex].GetShopItemVnum()
		price_vnum = self.searchResultItems[self.selectedItemIndex].GetPriceVnum()
		price_count = self.searchResultItems[self.selectedItemIndex].GetPriceCount()
		price = self.searchResultItems[self.selectedItemIndex].GetPriceInt()
		
		import item, uiCommon

		slotPos = shopItemPos

		PriceCount = price_count
		
		# if(int(price_vnum) > 1):

			# item.SelectItem(shopItemVnum)
			# itemName = item.GetItemName()
			
			# item.SelectItem(price_vnum)
			# itemName2 = item.GetItemName()
			
			# targetItemPos = -1
			# targetItemCount = 0
			# if item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR:
				# for i in xrange(180):
					# if int(player.GetItemIndex(i)) == int(price_vnum) :
						# targetItemPos = i
						# targetItemCount = targetItemCount + int(player.GetItemCount(i))
						# self.liste.append(targetItemPos)
					
			# else:
				# Erst Inventar, dann die Lager
				# for i in xrange(player.INVENTORY_SLOT_COUNT):
					# if int(player.GetItemIndex(i)) == int(price_vnum) :
						# targetItemPos = i
						# targetItemCount = targetItemCount + int(player.GetItemCount(i))

				# if( item.GetItemType() == 5 and item.GetItemSubType() == 0 or item.GetItemType() == 14 or int(price_vnum) == 27987):#Upgrade
					# for i in xrange(player.SPECIAL_SLOT_COUNT):
						# if int(player.GetItemIndex(player.UPGRADE_INVENTORY,i)) == int(price_vnum) :
							# targetItemPos = i
							# targetItemCount = targetItemCount + int(player.GetItemCount(player.UPGRADE_INVENTORY,i))					
				# elif( (int(price_vnum) >= 50401 and int(price_vnum) <= 50511) or int(price_vnum) == 50300): #Bücher
					# for i in xrange(player.SPECIAL_SLOT_COUNT):
						# if int(player.GetItemIndex(player.BOOK_INVENTORY,i)) == int(price_vnum) :
							# targetItemPos = i
							# targetItemCount = targetItemCount + int(player.GetItemCount(player.BOOK_INVENTORY,i))
				
				# elif( item.GetItemType() == 10 ):#Steine
					# for i in xrange(player.SPECIAL_SLOT_COUNT):
						# if int(player.GetItemIndex(player.STONE_INVENTORY,i)) == int(price_vnum) :
							# targetItemPos = i
							# targetItemCount = targetItemCount + int(player.GetItemCount(player.STONE_INVENTORY,i))
				


			# if(targetItemPos < 0):
				# chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CANT_FIND_ITEM % (itemName2))
				# self.liste = []
				# return
				
			# print "targetItemCount ",targetItemCount,int(PriceCount)
			
			# if(targetItemCount < int(PriceCount)):		
				# chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CANT_FIND_ITEM_COUNT % (targetItemCount,PriceCount,itemName2))
				# self.liste = []
				# return
				
			# if item.GetItemType() == item.ITEM_TYPE_WEAPON or item.GetItemType() == item.ITEM_TYPE_ARMOR:				
				
				# itemBuyQuestionDialog = uiCommon.QuestionDialogTooltip()
				# itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_TRADE(itemName, PriceCount, itemName2, PriceCount))
				# itemBuyQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerBuyItem(arg))
				# itemBuyQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerBuyItem(arg))
				# vnum = price_vnum
				
				# for item123 in self.liste:	
					# attrSlot = []
					# for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
						# attrSlot.append(player.GetItemAttribute(item123, i))
					# metinSlot = []
					# for i in xrange(player.METIN_SOCKET_MAX_NUM):
						# metinSlot.append(player.GetItemMetinSocket(item123, i))	
						
					# itemBuyQuestionDialog.CreateTooltip(vnum,metinSlot,attrSlot)						

				# itemBuyQuestionDialog.Open(len(self.liste))
				# itemBuyQuestionDialog.pos = slotPos
				# self.itemBuyQuestionDialog = itemBuyQuestionDialog
				# self.liste = []
						
			# else:
				# itemBuyQuestionDialog = uiCommon.QuestionDialog()
				# itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_TRADE(itemName, PriceCount, itemName2, PriceCount))
				# itemBuyQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerBuyItem(arg))
				# itemBuyQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerBuyItem(arg))
				# itemBuyQuestionDialog.Open()
				# itemBuyQuestionDialog.pos = slotPos
				# self.itemBuyQuestionDialog = itemBuyQuestionDialog

			
		# else:#normal
		item.SelectItem(shopItemVnum)
		itemName = item.GetItemName()

		itemBuyQuestionDialog = uiCommon.QuestionDialog()
		itemBuyQuestionDialog.SetText(localeInfo.DO_YOU_BUY_ITEM(itemName, PriceCount, localeInfo.NumberToMoneyString(price)))
		itemBuyQuestionDialog.SetAcceptEvent(lambda arg=True: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.SetCancelEvent(lambda arg=False: self.AnswerBuyItem(arg))
		itemBuyQuestionDialog.Open()
		itemBuyQuestionDialog.pos = slotPos
		self.itemBuyQuestionDialog = itemBuyQuestionDialog		


	def AnswerBuyItem(self, flag):
		if flag:
			shopVid = self.searchResultItems[self.selectedItemIndex].GetShopVid()
			#shopItemPos = self.searchResultItems[self.selectedItemIndex].GetShopItemPos()
			pos = self.itemBuyQuestionDialog.pos

			net.SendPrivateShopSearchBuyItem(shopVid, pos)
			self.RefreshRequest()

		self.itemBuyQuestionDialog.Close()
		self.itemBuyQuestionDialog = None		

	
	def OnSearchResultItemSelect(self, index):
		map(PrivateShopSearchDialog.SearchResultItem.UnSelect,  self.searchResultItems)
		background.DeletePrivateShopPos()
		self.selectedItemIndex = index
		self.searchResultItems[self.selectedItemIndex].Select()
		shopVid = self.searchResultItems[self.selectedItemIndex].GetShopVid()
		shopItemPos = self.searchResultItems[self.selectedItemIndex].GetShopItemPos()

	def Close(self):
		background.DeletePrivateShopPos()
		map(PrivateShopSearchDialog.SearchResultItem.Hide, self.searchResultItems)
		constInfo.OffShopSearch = 0
		self.Hide()
		
	def SetItemToolTip(self, itemTooltip):
		self.tooltipItem = itemTooltip		

	def OverInItem(self, slotIndex):
		slotIndex = slotIndex
		self.wndItem.SetUsableItem(False)
		
	def OverOutItem(self):
		self.wndItem.SetUsableItem(False)
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()		

	def Clear(self):
		self.Refresh()

	def Refresh(self):
		pass

	def __OnCloseButtonClickFilter(self):
		self.boardFilter.Hide()

	def __OnCloseButtonClick(self):
		constInfo.OffShopSearch = 0
		net.SendChatPacket("/checkresearch 0")
		self.Hide()

	def OnPressEscapeKey(self):
		constInfo.OffShopSearch = 0
		net.SendChatPacket("/checkresearch 0")
		self.Close()

