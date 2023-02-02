import ui
import constInfo
import chat
import time
import item
import uiWeb
import uiToolTip
import app
# import urllib
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import player

## add "editline.CanEdit()" in the ui.py

IS_BUY = FALSE ## Do not change

class Itemshop(ui.ScriptWindow):
	###########
	##Options##
	###########

	## Banner options
	bannerOptions = {
			'folder' : 'locale/de/ui/itemshop/banner/', ## folderpath to the banner images
			'time' : 5, ## time in seconds to change the banner automatically
			'timeToFade' : 0.04,
			'interval' : 0.05, 
			'banner_0' : 'banner_0',
			'banner_1' : 'banner_1',
		}

	## Buy coins; voting options
	link = {
		'buyCoins' : "https://web606163.fastpipe.io/auth/signin?ingame=1",
		'vote' : "",
		 }

	## Item/voteshop category options
	categorys = {
			'itemshop' : [
				['Ringe',1],
				['Pets',2],
				['PvP-Frisuren',3],
				['Premium-Titel-Tränke',4],
				['Waffen',5],
				['Rüstungen',6],
				['Sonstiges',7],
			],
			'voteshop' : [
				['Sonstiges',7],
				['Haustiere',8],
				['Reittiere',9],
				],
			'achievementshop' : [
				['Waffis',7],
				['Haustiereies',8],
				['Reittiereies',9],
				],
		}

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		

	def __LoadScript(self):
		try:
			self.__LoadVariables()
		except:
			import exception
			exception.Abort('test.__LoadScript.LoadVariables')
		## Load script
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, 'uiscript/itemshop_v2.py')
		except:
			import exception
			exception.Abort('test.__LoadScript.LoadObject')

		## Load gui
		try: 
			self.BindObjects()
		except:
			import exception
			exception.Abort('test.__LoadScript.BindObjects')
			
		## Load events
		try: 
			self.BindEvents()
		except:
			import exception
			exception.Abort('test.__LoadScript.BindEvents')
			
		self.isLoaded = TRUE

	## Load variables (DONT CHANGE)
	def __LoadVariables(self):
		self.bannerVar = {
				'fadeOut' : 0,
				'currentTime' : 0 ,
				'intervallEndTime' : 0,
				'currentAlphaValue' : 0,
				'currentImage' : 0,
				'lastSwitch' : time.clock() + self.bannerOptions['time'],
			}

		self.page = {
			   'curPage' : 'STARTPAGE',
			}
		self.arrows = {
				 'startpage' : {
						'mostBought' : 1,
						'hotOffers' : 1,
					},
				 'itemshop' : {
						'arrowOnSale' : 1,
						'arrowCategory' : 0,
					},
				 'voteshop' : {
						'arrowOnSale' : 1,
						'arrowCategory' : 0,
					},
				'achievementshop' : {
						'arrowOnSale' : 1,
						'arrowCategory' : 0,
					},
			 }

		self.category = {
					'itemshop' : 0,
					'voteshop' : 0,
					'achievementshop' : 0,
				}
		
	## Bind the objects in __LoadScript
	def BindObjects(self):
		self.board = self.GetChild('Board')
		self.elements = {
			'titlebar' : self.GetChild('titlebar'),
			'pages' : {
					'startpage' : self.GetChild('Startpage'),
					'itemshop' : self.GetChild('Itemshop'),
					'voteshop' : self.GetChild('Voteshop'),
					'achievementshop' : self.GetChild('Achievementshop'),
				},
			'windows' : {
					'startpage': {
						'banner' : self.GetChild('Banner'),
						'mostBought'  : self.GetChild('MostBought'),
						},

					## Itemshop start ##

					## Itemshop end ##
				},
			'buttons' : {

					'startpage': {   
						'startpage' : self.GetChild('btn_startpage'),
						'itemshop' : self.GetChild('btn_itemshop'),
						'voteshop' : self.GetChild('btn_voteshop'),
						'achievementshop' : self.GetChild('btn_achievementshop'),
						'banner_0' : self.GetChild('btn_banner_0'),
						'banner_1' : self.GetChild('btn_banner_1'),
						'buy_coins' : self.GetChild('btn_buy_coins'),
						'vote' : self.GetChild('btn_vote'),
						'mostBought_left' : self.GetChild('btn_mostBought_left'),
						'mostBought_right' : self.GetChild('btn_mostBought_right'),
						'hotOffers_up' : self.GetChild('btn_hotOffers_up'),
						'hotOffers_down' : self.GetChild('btn_hotOffers_down'),
					},

					'itemshop' : {
						'onSale_left' : self.GetChild('btn_IsOnSale_left'),
						'onSale_right' : self.GetChild('btn_IsOnSale_right'),
						'onSale_up' : self.GetChild('btn_IsCategory_up'),
						'onSale_down' : self.GetChild('btn_IsCategory_down'),
					},

					'voteshop' : {
						'onSale_left' : self.GetChild('btn_VsOnSale_left'),
						'onSale_right' : self.GetChild('btn_VsOnSale_right'),
						'onSale_up' : self.GetChild('btn_VsCategory_up'),
						'onSale_down' : self.GetChild('btn_VsCategory_down'),
					},
					
					'achievementshop' : {
						'onSale_left' : self.GetChild('btn_AsOnSale_left'),
						'onSale_right' : self.GetChild('btn_AsOnSale_right'),
						'onSale_up' : self.GetChild('btn_AsCategory_up'),
						'onSale_down' : self.GetChild('btn_AsCategory_down'),
					},
				},

			'textline' : {
					'menue' : {
						'itemshop_coins' : self.GetChild('tx_i_coins'),
						'voteshop_coins' : self.GetChild('tx_v_coins'),
						'achievementshop_coins' : self.GetChild('tx_a_coins'),
					},
					'box' : {
						'itemshop_coins' : self.GetChild('sb_i_coins'),
						'voteshop_coins' : self.GetChild('sb_v_coins'),
						'achievementshop_coins' : self.GetChild('sb_a_coins'),
					},
					'itemshop': {
						'page_nr' : self.GetChild('tx_IsOnSale_pageNr'),
					},
					'voteshop': {
						'page_nr' : self.GetChild('tx_VsOnSale_pageNr'),
					},
					'achievementshop': {
						'page_nr' : self.GetChild('tx_AsOnSale_pageNr'),
					},
				},
				
			'images' : {
					'startpage': {
						'banner' : self.GetChild('image_banner'),
						'fade_banner' : self.GetChild('image_fade_banner'),
					},
				},
			'itemBoxes' : {
				  'startpage' : {
						'mostBought': {
							'box_00' : ItemBox(),
							'box_01' : ItemBox(),
							'box_02' : ItemBox(),
						 },
						'hotOffers': {
							'box_00' : ItemBox(),
							'box_01' : ItemBox(),
						 },
					 },
					'itemshop' : {
						'box_00' : ItemBox(),
						'box_01' : ItemBox(),
						'box_02' : ItemBox(),
						'box_03' : ItemBox(),
						'box_04' : ItemBox(),
						'box_05' : ItemBox(),
						'box_06' : ItemBox(),
						'box_07' : ItemBox(),
						'box_08' : ItemBox(),
						'box_09' : ItemBox(),
						'box_010' : ItemBox(),
						'box_011' : ItemBox(),
					},
					'voteshop' : {
						'box_00' : ItemBox(),
						'box_01' : ItemBox(),
						'box_02' : ItemBox(),
						'box_03' : ItemBox(),
						'box_04' : ItemBox(),
						'box_05' : ItemBox(),
						'box_06' : ItemBox(),
						'box_07' : ItemBox(),
						'box_08' : ItemBox(),
						'box_09' : ItemBox(),
						'box_010' : ItemBox(),
						'box_011' : ItemBox(),
					},
					'achievementshop' : {
						'box_00' : ItemBox(),
						'box_01' : ItemBox(),
						'box_02' : ItemBox(),
						'box_03' : ItemBox(),
						'box_04' : ItemBox(),
						'box_05' : ItemBox(),
						'box_06' : ItemBox(),
						'box_07' : ItemBox(),
						'box_08' : ItemBox(),
						'box_09' : ItemBox(),
						'box_010' : ItemBox(),
						'box_011' : ItemBox(),
					},
				},
		}

		##Itemshop category buttons

		# for i in xrange(min(10, len(self.categorys['itemshop']))):
			# self.elements['buttons']['itemshop']['category_%d' % i] = self.CreateCategoryButton(self.elements['pages']['itemshop'], 44, 47+30*i,self.categorys['itemshop'][i][0], self.__OnClickItemshopCategory, self.categorys['itemshop'][i][1])
		
		# for i in xrange(min(10, len(self.categorys['voteshop']))):
			# self.elements['buttons']['voteshop']['category_%d' % i] = self.CreateCategoryButton(self.elements['pages']['voteshop'], 44, 47+30*i,self.categorys['voteshop'][i][0], self.__OnClickVoteshopCategory, self.categorys['voteshop'][i][1])
		
		self.ItemshopCategoryRefresh()
		self.VoteshopCategoryRefresh()
		self.AchievementshopCategoryRefresh()
		
		self.webWnd = uiWeb.WebWindow()
		self.webWnd.LoadWindow()
		self.webWnd.Hide()

		self.PopUp = PricePopUp()
		
	def SendSystemChat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "<System>: "+str(text))


	## Bind events to the objects in __LoadScript
	def BindEvents(self):
		self.elements['titlebar'].SetCloseEvent(ui.__mem_func__(self.__OnClickClose))
		# self.elements['buttons']['menue']['question'].SetEvent(self.__OnClickQuestion)
		self.elements['buttons']['startpage']['startpage'].SetEvent(self.ChangePage, 'STARTPAGE')
		self.elements['buttons']['startpage']['itemshop'].SetEvent(self.ChangePage, 'ITEMSHOP')
		self.elements['buttons']['startpage']['voteshop'].SetEvent(self.ChangePage, 'VOTESHOP')
		self.elements['buttons']['startpage']['achievementshop'].SetEvent(self.ChangePage, 'ACHIEVEMENTSHOP')
		self.elements['buttons']['startpage']['buy_coins'].SetEvent(self.__OnClickBuyCoins)
		self.elements['buttons']['startpage']['vote'].SetEvent(self.__OnClickVote)
		
		
		## Change Banner
		self.elements['buttons']['startpage']['banner_0'].SetToggleDownEvent(lambda arg = 0: self.__OnClickBannerBtn(arg))
		self.elements['buttons']['startpage']['banner_0'].SetToggleUpEvent(lambda arg = 0: self.__OnClickBannerBtn(arg))
		self.elements['buttons']['startpage']['banner_1'].SetToggleDownEvent(lambda arg = 1: self.__OnClickBannerBtn(arg))
		self.elements['buttons']['startpage']['banner_1'].SetToggleUpEvent(lambda arg = 1: self.__OnClickBannerBtn(arg))

		## Item boxes most bought
		self.elements['itemBoxes']['startpage']['mostBought']['box_00'].Open(self.elements['pages']['startpage'],91+8,389-100+8)
		self.elements['itemBoxes']['startpage']['mostBought']['box_01'].Open(self.elements['pages']['startpage'],235+8,389-100+8)
		self.elements['itemBoxes']['startpage']['mostBought']['box_02'].Open(self.elements['pages']['startpage'],382+8,389-100+8)

		## Item boxes hot offers
		self.elements['itemBoxes']['startpage']['hotOffers']['box_00'].Open(self.elements['pages']['startpage'],603,193-100)
		self.elements['itemBoxes']['startpage']['hotOffers']['box_01'].Open(self.elements['pages']['startpage'],603,307-100)

		## Item boxes itemshop
		self.elements['itemBoxes']['itemshop']['box_00'].Open(self.elements['pages']['itemshop'],259,126-100)
		self.elements['itemBoxes']['itemshop']['box_01'].Open(self.elements['pages']['itemshop'],405,126-100)
		self.elements['itemBoxes']['itemshop']['box_02'].Open(self.elements['pages']['itemshop'],551,126-100)
		self.elements['itemBoxes']['itemshop']['box_03'].Open(self.elements['pages']['itemshop'],259,216-100)
		self.elements['itemBoxes']['itemshop']['box_04'].Open(self.elements['pages']['itemshop'],405,216-100)
		self.elements['itemBoxes']['itemshop']['box_05'].Open(self.elements['pages']['itemshop'],551,216-100)
		self.elements['itemBoxes']['itemshop']['box_06'].Open(self.elements['pages']['itemshop'],259,306-100)
		self.elements['itemBoxes']['itemshop']['box_07'].Open(self.elements['pages']['itemshop'],405,306-100)
		self.elements['itemBoxes']['itemshop']['box_08'].Open(self.elements['pages']['itemshop'],551,306-100)
		self.elements['itemBoxes']['itemshop']['box_09'].Open(self.elements['pages']['itemshop'],259,396-100)
		self.elements['itemBoxes']['itemshop']['box_010'].Open(self.elements['pages']['itemshop'],405,396-100)
		self.elements['itemBoxes']['itemshop']['box_011'].Open(self.elements['pages']['itemshop'],551,396-100)

		## Item boxes voteshop
		self.elements['itemBoxes']['voteshop']['box_00'].Open(self.elements['pages']['voteshop'],259,126-100)
		self.elements['itemBoxes']['voteshop']['box_01'].Open(self.elements['pages']['voteshop'],405,126-100)
		self.elements['itemBoxes']['voteshop']['box_02'].Open(self.elements['pages']['voteshop'],551,126-100)
		self.elements['itemBoxes']['voteshop']['box_03'].Open(self.elements['pages']['voteshop'],259,216-100)
		self.elements['itemBoxes']['voteshop']['box_04'].Open(self.elements['pages']['voteshop'],405,216-100)
		self.elements['itemBoxes']['voteshop']['box_05'].Open(self.elements['pages']['voteshop'],551,216-100)
		self.elements['itemBoxes']['voteshop']['box_06'].Open(self.elements['pages']['voteshop'],259,306-100)
		self.elements['itemBoxes']['voteshop']['box_07'].Open(self.elements['pages']['voteshop'],405,306-100)
		self.elements['itemBoxes']['voteshop']['box_08'].Open(self.elements['pages']['voteshop'],551,306-100)
		self.elements['itemBoxes']['voteshop']['box_09'].Open(self.elements['pages']['voteshop'],259,396-100)
		self.elements['itemBoxes']['voteshop']['box_010'].Open(self.elements['pages']['voteshop'],405,396-100)
		self.elements['itemBoxes']['voteshop']['box_011'].Open(self.elements['pages']['voteshop'],551,396-100)
		
		## Item boxes achievementshop
		self.elements['itemBoxes']['achievementshop']['box_00'].Open(self.elements['pages']['achievementshop'],259,126-100)
		self.elements['itemBoxes']['achievementshop']['box_01'].Open(self.elements['pages']['achievementshop'],405,126-100)
		self.elements['itemBoxes']['achievementshop']['box_02'].Open(self.elements['pages']['achievementshop'],551,126-100)
		self.elements['itemBoxes']['achievementshop']['box_03'].Open(self.elements['pages']['achievementshop'],259,216-100)
		self.elements['itemBoxes']['achievementshop']['box_04'].Open(self.elements['pages']['achievementshop'],405,216-100)
		self.elements['itemBoxes']['achievementshop']['box_05'].Open(self.elements['pages']['achievementshop'],551,216-100)
		self.elements['itemBoxes']['achievementshop']['box_06'].Open(self.elements['pages']['achievementshop'],259,306-100)
		self.elements['itemBoxes']['achievementshop']['box_07'].Open(self.elements['pages']['achievementshop'],405,306-100)
		self.elements['itemBoxes']['achievementshop']['box_08'].Open(self.elements['pages']['achievementshop'],551,306-100)
		self.elements['itemBoxes']['achievementshop']['box_09'].Open(self.elements['pages']['achievementshop'],259,396-100)
		self.elements['itemBoxes']['achievementshop']['box_010'].Open(self.elements['pages']['achievementshop'],405,396-100)
		self.elements['itemBoxes']['achievementshop']['box_011'].Open(self.elements['pages']['achievementshop'],551,396-100)

		## Arrows Startpage
		self.elements['buttons']['startpage']['mostBought_left'].SetEvent(self.__OnClickArrow, 'MOSTBOUGHT_LEFT')
		self.elements['buttons']['startpage']['mostBought_right'].SetEvent(self.__OnClickArrow, 'MOSTBOUGHT_RIGHT')
		self.elements['buttons']['startpage']['hotOffers_up'].SetEvent(self.__OnClickArrow, 'HOTOFFERS_UP')
		self.elements['buttons']['startpage']['hotOffers_down'].SetEvent(self.__OnClickArrow, 'HOTOFFERS_DOWN')

		## Arrows Itemshop
		self.elements['buttons']['itemshop']['onSale_left'].SetEvent(self.__OnClickArrow, 'ITEMSHOP_ONSALE_LEFT')
		self.elements['buttons']['itemshop']['onSale_right'].SetEvent(self.__OnClickArrow, 'ITEMSHOP_ONSALE_RIGHT')
		self.elements['buttons']['itemshop']['onSale_up'].SetEvent(self.__OnClickArrow, 'ITEMSHOP_ONSALE_UP')
		self.elements['buttons']['itemshop']['onSale_down'].SetEvent(self.__OnClickArrow, 'ITEMSHOP_ONSALE_DOWN')
		
		## Arrows Voteshop
		self.elements['buttons']['voteshop']['onSale_left'].SetEvent(self.__OnClickArrow, 'VOTESHOP_ONSALE_LEFT')
		self.elements['buttons']['voteshop']['onSale_right'].SetEvent(self.__OnClickArrow, 'VOTESHOP_ONSALE_RIGHT')
		self.elements['buttons']['voteshop']['onSale_up'].SetEvent(self.__OnClickArrow, 'VOTESHOP_ONSALE_UP')
		self.elements['buttons']['voteshop']['onSale_down'].SetEvent(self.__OnClickArrow, 'VOTESHOP_ONSALE_DOWN')
		
		## Arrows Achievementshop
		self.elements['buttons']['achievementshop']['onSale_left'].SetEvent(self.__OnClickArrow, 'ACHIEVEMENTSHOP_ONSALE_LEFT')
		self.elements['buttons']['achievementshop']['onSale_right'].SetEvent(self.__OnClickArrow, 'ACHIEVEMENTSHOP_ONSALE_RIGHT')
		self.elements['buttons']['achievementshop']['onSale_up'].SetEvent(self.__OnClickArrow, 'ACHIEVEMENTSHOP_ONSALE_UP')
		self.elements['buttons']['achievementshop']['onSale_down'].SetEvent(self.__OnClickArrow, 'ACHIEVEMENTSHOP_ONSALE_DOWN')
		
		## Textlines
		self.elements['textline']['itemshop']['page_nr'].SetParent(self.elements['pages']['itemshop'])
		self.elements['textline']['voteshop']['page_nr'].SetParent(self.elements['pages']['voteshop'])
		self.elements['textline']['achievementshop']['page_nr'].SetParent(self.elements['pages']['achievementshop'])


	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	## Hide the Gui
	def Destroy(self):
		self.Hide()
		
	## Open the gui
	def Open(self, isCoins, vsCoins, asCoins, banner_0, banner_1):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		
		self.bannerOptions['banner_0'] = banner_0
		self.bannerOptions['banner_1'] = banner_1
		self.SetItemshopCoins(isCoins)
		self.SetVoteshopCoins(vsCoins)
		self.SetAchievementshopCoins(asCoins)
		self.page['curPage'] = 'STARTPAGE'
		self.ChangePage('STARTPAGE')
		self.ChangeBannerButton(0)
		self.SwitchBanner(0)
		
		self.elements['buttons']['startpage']['voteshop'].Hide()
		self.elements['buttons']['startpage']['achievementshop'].Hide()
		#self.elements['buttons']['startpage']['buy_coins'].Hide()
		#self.elements['buttons']['startpage']['vote'].Hide()
		self.elements['textline']['box']['voteshop_coins'].Hide()
		self.elements['textline']['box']['achievementshop_coins'].Hide()
		
		self.SetTop()
		self.Show()
		
	## Close the gui
	def Close(self):
		self.Hide()
		
	## Hide other pages and load the new Page
	def ChangePage(self, page):
		self.page['curPage'] = page

		if page == 'STARTPAGE':
			self.arrows['startpage']['mostBought'] = 1
			self.arrows['startpage']['hotOffers'] = 1
			
			self.HotOffersItemsRefresh()
			self.MostBoughtItemsRefresh()

			self.elements['pages']['itemshop'].Hide()
			self.elements['pages']['voteshop'].Hide()
			self.elements['pages']['achievementshop'].Hide()
			self.elements['pages']['startpage'].Show()
			
		elif page == 'ITEMSHOP':
			self.arrows['itemshop']['arrowOnSale'] = 1
			self.category['itemshop'] = self.categorys['itemshop'][0][1]
			self.arrows['itemshop']['arrowCategory'] = 0
			
			self.ItemshopCategoryRefresh()
			self.ItemshopItemsRefresh()

			self.elements['pages']['startpage'].Hide()
			self.elements['pages']['voteshop'].Hide()
			self.elements['pages']['achievementshop'].Hide()
			self.elements['pages']['itemshop'].Show()

		elif page == 'VOTESHOP':
			self.arrows['voteshop']['arrowOnSale'] = 1
			self.category['voteshop'] = self.categorys['voteshop'][0][1]
			self.arrows['voteshop']['arrowCategory'] = 0
			
			self.VoteshopCategoryRefresh()
			self.VoteshopItemsRefresh()

			self.elements['pages']['startpage'].Hide()
			self.elements['pages']['itemshop'].Hide()
			self.elements['pages']['achievementshop'].Hide()
			self.elements['pages']['voteshop'].Show()
		
		elif page == 'ACHIEVEMENTSHOP':
			self.arrows['achievementshop']['arrowOnSale'] = 1
			self.category['achievementshop'] = self.categorys['achievementshop'][0][1]
			self.arrows['achievementshop']['arrowCategory'] = 0
			
			self.AchievementshopCategoryRefresh()
			self.AchievementshopItemsRefresh()

			self.elements['pages']['startpage'].Hide()
			self.elements['pages']['itemshop'].Hide()
			self.elements['pages']['voteshop'].Hide()
			self.elements['pages']['achievementshop'].Show()

	def ChangeBannerButton(self, enable):
		if enable == 0:
			self.elements['buttons']['startpage']['banner_1'].SetUp()
			self.elements['buttons']['startpage']['banner_0'].Down()
		elif enable == 1:
			self.elements['buttons']['startpage']['banner_0'].SetUp()
			self.elements['buttons']['startpage']['banner_1'].Down()

	#########################
	## REFRESH ITEMS START ##
	#########################

	def HotOffersItemsRefresh(self):
		curPage = self.arrows['startpage']['hotOffers']
		## Hide Itemboxes
		for i in xrange(2):
			self.elements['itemBoxes']['startpage']['hotOffers']['box_0%d' % i].Hide()

		## Load hotOffers first itemboxes
		for i in xrange(min(2, len(constInfo.ITEMSHOP['items']['startpage']['hotOffers']) - curPage * 2 +2)):
			curItem = constInfo.ITEMSHOP['items']['startpage']['hotOffers'][i + (curPage - 1)*2]
			self.elements['itemBoxes']['startpage']['hotOffers']['box_0%d' % i].SetContent(curItem[0], curItem[1], curItem[2], curItem[3]) ## type, itemvnum, itemdetails, price
			self.elements['itemBoxes']['startpage']['hotOffers']['box_0%d' % i].SetPercent(curItem[4]) ## percent
			self.elements['itemBoxes']['startpage']['hotOffers']['box_0%d' % i].SetTime(curItem[5], curItem[6]) ## time , runOut
			self.elements['itemBoxes']['startpage']['hotOffers']['box_0%d' % i].Show()
		
		if curPage * 2 >= len(constInfo.ITEMSHOP['items']['startpage']['hotOffers']):
			self.elements['buttons']['startpage']['hotOffers_down'].Hide()
		else:
			self.elements['buttons']['startpage']['hotOffers_down'].Show()

		if curPage > 1:
			self.elements['buttons']['startpage']['hotOffers_up'].Show()
		else:
			self.elements['buttons']['startpage']['hotOffers_up'].Hide()

	def MostBoughtItemsRefresh(self):
		curPage = self.arrows['startpage']['mostBought']
		## Hide Itemboxes
		for i in xrange(3):
			self.elements['itemBoxes']['startpage']['mostBought']['box_0%d' % i].Hide()

		## Load mostBought first itemboxes
		for i in xrange(min(3, len(constInfo.ITEMSHOP['items']['startpage']['mostBought']) - curPage * 3 +3)):
			curItem = constInfo.ITEMSHOP['items']['startpage']['mostBought'][i + (curPage - 1)*3]
			self.elements['itemBoxes']['startpage']['mostBought']['box_0%d' % i].SetContent(curItem[0], curItem[1], curItem[2], curItem[3]) ## type, itemvnum, itemdetails, price
			self.elements['itemBoxes']['startpage']['mostBought']['box_0%d' % i].SetPercent(curItem[4]) ## percent
			self.elements['itemBoxes']['startpage']['mostBought']['box_0%d' % i].SetTime(curItem[5], curItem[6]) ## time , runOut
			self.elements['itemBoxes']['startpage']['mostBought']['box_0%d' % i].Show()
		
		if curPage * 3 >= len(constInfo.ITEMSHOP['items']['startpage']['mostBought']):
			self.elements['buttons']['startpage']['mostBought_right'].Hide()
		else:
			self.elements['buttons']['startpage']['mostBought_right'].Show()

		if curPage > 1:
			self.elements['buttons']['startpage']['mostBought_left'].Show()
		else:
			self.elements['buttons']['startpage']['mostBought_left'].Hide()

	def ItemshopItemsRefresh(self):
		curPage = self.arrows['itemshop']['arrowOnSale']
		## Hide Itemboxes
		for i in xrange(12):
			self.elements['itemBoxes']['itemshop']['box_0%d' % i].Hide()

		## Load mostBought first itemboxes
		try:
			for i in xrange(min(12, len(constInfo.ITEMSHOP['items']['itemshop'][self.category['itemshop']]) - curPage * 12 +12)):
				curItem = constInfo.ITEMSHOP['items']['itemshop'][self.category['itemshop']][i + (curPage - 1)*12]
				self.elements['itemBoxes']['itemshop']['box_0%d' % i].SetContent(curItem[0], curItem[1], curItem[2], curItem[3]) ## type, itemvnum, itemdetails, price
				self.elements['itemBoxes']['itemshop']['box_0%d' % i].SetPercent(curItem[4]) ## percent
				self.elements['itemBoxes']['itemshop']['box_0%d' % i].SetTime(curItem[5], curItem[6]) ## time , runOut
				self.elements['itemBoxes']['itemshop']['box_0%d' % i].Show()
		except:
			self.SendChat('Hier wurden keine Items gefunden, bitte patchen.')
			self.SendChat('Tritt der Fehler weiterhin auf, dann bitte einem GM melden, mit folgendem Fehler: [Error 001]')
			self.elements['buttons']['itemshop']['onSale_right'].Hide()
			self.elements['buttons']['itemshop']['onSale_left'].Hide()
			self.elements['textline']['itemshop']['page_nr'].Hide()
			return
			
		maxPage = self.RoundUp(float(len(constInfo.ITEMSHOP['items']['itemshop'][self.category['itemshop']]))/float(12))
		if maxPage > 1:
			self.elements['textline']['itemshop']['page_nr'].SetText(str(curPage) + ' / ' + str(maxPage))
			self.elements['textline']['itemshop']['page_nr'].Show()
		else:
			self.elements['textline']['itemshop']['page_nr'].Hide()
		
		if curPage * 12 >= len(constInfo.ITEMSHOP['items']['itemshop'][self.category['itemshop']]):
			self.elements['buttons']['itemshop']['onSale_right'].Hide()
		else:
			self.elements['buttons']['itemshop']['onSale_right'].Show()

		if curPage > 1:
			self.elements['buttons']['itemshop']['onSale_left'].Show()
		else:
			self.elements['buttons']['itemshop']['onSale_left'].Hide()

	def VoteshopItemsRefresh(self):
		curPage = self.arrows['voteshop']['arrowOnSale']
		## Hide Itemboxes 
		for i in xrange(12):
			self.elements['itemBoxes']['voteshop']['box_0%d' % i].Hide()

		## Load mostBought first itemboxes
		try:
			for i in xrange(min(12, len(constInfo.ITEMSHOP['items']['voteshop'][self.category['voteshop']]) - curPage * 12 +12)):
				curItem = constInfo.ITEMSHOP['items']['voteshop'][self.category['voteshop']][i + (curPage - 1)*12]
				self.elements['itemBoxes']['voteshop']['box_0%d' % i].SetContent(curItem[0], curItem[1], curItem[2], curItem[3]) ## type, itemvnum, itemdetails, price
				self.elements['itemBoxes']['voteshop']['box_0%d' % i].SetPercent(curItem[4]) ## percent
				self.elements['itemBoxes']['voteshop']['box_0%d' % i].SetTime(curItem[5], curItem[6]) ## time , runOut
				self.elements['itemBoxes']['voteshop']['box_0%d' % i].Show()
		except:
			self.SendChat('Hier wurden keine Items gefunden, bitte patchen.')
			self.SendChat('Tritt der Fehler weiterhin auf, dann bitte einem GM melden, mit folgendem Fehler: [Error 002]')
			self.elements['buttons']['voteshop']['onSale_right'].Hide()
			self.elements['buttons']['voteshop']['onSale_left'].Hide()
			self.elements['textline']['voteshop']['page_nr'].Hide()
			return
		
		maxPage = self.RoundUp(float(len(constInfo.ITEMSHOP['items']['voteshop'][self.category['voteshop']]))/float(12))
		if maxPage > 1:
			self.elements['textline']['voteshop']['page_nr'].SetText(str(curPage) + ' / ' + str(maxPage))
			self.elements['textline']['voteshop']['page_nr'].Show()
		else:
			self.elements['textline']['voteshop']['page_nr'].Hide()
			
		if curPage * 12 >= len(constInfo.ITEMSHOP['items']['voteshop'][self.category['voteshop']]):
			self.elements['buttons']['voteshop']['onSale_right'].Hide()
		else:
			self.elements['buttons']['voteshop']['onSale_right'].Show()

		if curPage > 1:
			self.elements['buttons']['voteshop']['onSale_left'].Show()
		else:
			self.elements['buttons']['voteshop']['onSale_left'].Hide()
			
	def AchievementshopItemsRefresh(self):
		curPage = self.arrows['achievementshop']['arrowOnSale']
		# self.SendSystemChat('curPage: '+str(curPage))
		## Hide Itemboxes 
		for i in xrange(12):
			self.elements['itemBoxes']['achievementshop']['box_0%d' % i].Hide()

		## Load mostBought first itemboxes
		try:
			for i in xrange(min(12, len(constInfo.ITEMSHOP['items']['achievementshop'][self.category['achievementshop']]) - curPage * 12 +12)):
				curItem = constInfo.ITEMSHOP['items']['achievementshop'][self.category['achievementshop']][i + (curPage - 1)*12]
				# self.SendSystemChat('curItem: '+ str(i)+ ' ' +str(curItem))
				self.elements['itemBoxes']['achievementshop']['box_0%d' % i].SetContent(curItem[0], curItem[1], curItem[2], curItem[3]) ## type, itemvnum, itemdetails, price
				self.elements['itemBoxes']['achievementshop']['box_0%d' % i].SetPercent(curItem[4]) ## percent
				self.elements['itemBoxes']['achievementshop']['box_0%d' % i].SetTime(curItem[5], curItem[6]) ## time , runOut
				self.elements['itemBoxes']['achievementshop']['box_0%d' % i].Show()
				# self.SendSystemChat('curItem: added' + str(i))
		except:
			self.SendChat('Hier wurden keine Items gefunden, bitte patchen.')
			self.SendChat('Tritt der Fehler weiterhin auf, dann bitte einem GM melden, mit folgendem Fehler: [Error 002]')
			self.elements['buttons']['achievementshop']['onSale_right'].Hide()
			self.elements['buttons']['achievementshop']['onSale_left'].Hide()
			self.elements['textline']['achievementshop']['page_nr'].Hide()
			return
		
		maxPage = self.RoundUp(float(len(constInfo.ITEMSHOP['items']['achievementshop'][self.category['achievementshop']]))/float(12))
		if maxPage > 1:
			self.elements['textline']['achievementshop']['page_nr'].SetText(str(curPage) + ' / ' + str(maxPage))
			self.elements['textline']['achievementshop']['page_nr'].Show()
		else:
			self.elements['textline']['achievementshop']['page_nr'].Hide()
			
		if curPage * 12 >= len(constInfo.ITEMSHOP['items']['achievementshop'][self.category['achievementshop']]):
			self.elements['buttons']['achievementshop']['onSale_right'].Hide()
		else:
			self.elements['buttons']['achievementshop']['onSale_right'].Show()

		if curPage > 1:
			self.elements['buttons']['achievementshop']['onSale_left'].Show()
		else:
			self.elements['buttons']['achievementshop']['onSale_left'].Hide()
	
	def ItemshopCategoryRefresh(self):
		try:
			for i in xrange(10):
				self.elements['buttons']['itemshop']['category_%d' % i].Hide()
		except:
			pass
		try:
			for i in xrange(min(10, len(self.categorys['itemshop']))):
				scrolledId = i + self.arrows['itemshop']['arrowCategory']
				self.elements['buttons']['itemshop']['category_%d' % i] = self.CreateCategoryButton(self.elements['pages']['itemshop'], 44, 47+30*i,self.categorys['itemshop'][scrolledId][0], self.__OnClickItemshopCategory, self.categorys['itemshop'][scrolledId][1])
				self.elements['buttons']['itemshop']['category_%d' % i].Show()
		except:
			pass
			
		if (len(self.categorys['itemshop']) > 10):
			if (self.arrows['itemshop']['arrowCategory'] <= 0):
				self.elements['buttons']['itemshop']['onSale_down'].Show()
				self.elements['buttons']['itemshop']['onSale_up'].Hide()
			elif (self.arrows['itemshop']['arrowCategory']+10 < len(self.categorys['itemshop'])):
				self.elements['buttons']['itemshop']['onSale_down'].Show()
				self.elements['buttons']['itemshop']['onSale_up'].Show()
			elif (self.arrows['itemshop']['arrowCategory']+10 >= len(self.categorys['itemshop'])):
				self.elements['buttons']['itemshop']['onSale_down'].Hide()
				self.elements['buttons']['itemshop']['onSale_up'].Show()
		else:
			self.elements['buttons']['itemshop']['onSale_down'].Hide()
			self.elements['buttons']['itemshop']['onSale_up'].Hide()
		
	def VoteshopCategoryRefresh(self):
		try:
			for i in xrange(10):
				self.elements['buttons']['voteshop']['category_%d' % i].Hide()
		except:
			pass
		try:
			for i in xrange(min(10, len(self.categorys['voteshop']))):
				scrolledId = i + self.arrows['voteshop']['arrowCategory']
				self.elements['buttons']['voteshop']['category_%d' % i] = self.CreateCategoryButton(self.elements['pages']['voteshop'], 44, 47+30*i,self.categorys['voteshop'][scrolledId][0], self.__OnClickVoteshopCategory, self.categorys['voteshop'][scrolledId][1])
				self.elements['buttons']['voteshop']['category_%d' % i].Show()
		except:
			pass
			
		if (len(self.categorys['voteshop']) > 10):
			if (self.arrows['voteshop']['arrowCategory'] <= 0):
				self.elements['buttons']['voteshop']['onSale_down'].Show()
				self.elements['buttons']['voteshop']['onSale_up'].Hide()
			elif (self.arrows['voteshop']['arrowCategory']+10 < len(self.categorys['voteshop'])):
				self.elements['buttons']['voteshop']['onSale_down'].Show()
				self.elements['buttons']['voteshop']['onSale_up'].Show()
			elif (self.arrows['voteshop']['arrowCategory']+10 >= len(self.categorys['voteshop'])):
				self.elements['buttons']['voteshop']['onSale_down'].Hide()
				self.elements['buttons']['voteshop']['onSale_up'].Show()
		else:
			self.elements['buttons']['voteshop']['onSale_down'].Hide()
			self.elements['buttons']['voteshop']['onSale_up'].Hide()
			
	def AchievementshopCategoryRefresh(self):
		try:
			for i in xrange(10):
				self.elements['buttons']['achievementshop']['category_%d' % i].Hide()
		except:
			pass
		try:
			for i in xrange(min(10, len(self.categorys['achievementshop']))):
				scrolledId = i + self.arrows['achievementshop']['arrowCategory']
				self.elements['buttons']['achievementshop']['category_%d' % i] = self.CreateCategoryButton(self.elements['pages']['achievementshop'], 44, 47+30*i,self.categorys['achievementshop'][scrolledId][0], self.__OnClickAchievementshopCategory, self.categorys['achievementshop'][scrolledId][1])
				self.elements['buttons']['achievementshop']['category_%d' % i].Show()
		except:
			pass
			
		if (len(self.categorys['achievementshop']) > 10):
			if (self.arrows['achievementshop']['arrowCategory'] <= 0):
				self.elements['buttons']['achievementshop']['onSale_down'].Show()
				self.elements['buttons']['achievementshop']['onSale_up'].Hide()
			elif (self.arrows['achievementshop']['arrowCategory']+10 < len(self.categorys['achievementshop'])):
				self.elements['buttons']['achievementshop']['onSale_down'].Show()
				self.elements['buttons']['achievementshop']['onSale_up'].Show()
			elif (self.arrows['achievementshop']['arrowCategory']+10 >= len(self.categorys['achievementshop'])):
				self.elements['buttons']['achievementshop']['onSale_down'].Hide()
				self.elements['buttons']['achievementshop']['onSale_up'].Show()
		else:
			self.elements['buttons']['achievementshop']['onSale_down'].Hide()
			self.elements['buttons']['achievementshop']['onSale_up'].Hide()
		
	#######################
	## REFRESH ITEMS END ##
	#######################

	#########################
	## OnClick Events START #
	#########################

	## Arrows (startpage [mostBought, hotOffers], itemshop, voteshop)
	def __OnClickArrow(self, arrow):
		if arrow == 'MOSTBOUGHT_LEFT':
			self.arrows['startpage']['mostBought'] -= 1
			self.MostBoughtItemsRefresh()
		elif arrow == 'MOSTBOUGHT_RIGHT':
			self.arrows['startpage']['mostBought'] += 1
			self.MostBoughtItemsRefresh()
		elif arrow == 'HOTOFFERS_UP':
			self.arrows['startpage']['hotOffers'] -= 1
			self.HotOffersItemsRefresh()
		elif arrow == 'HOTOFFERS_DOWN':
			self.arrows['startpage']['hotOffers'] += 1
			self.HotOffersItemsRefresh()
		elif arrow == 'ITEMSHOP_ONSALE_LEFT':
			self.arrows['itemshop']['arrowOnSale'] -= 1
			self.ItemshopItemsRefresh()
		elif arrow == 'ITEMSHOP_ONSALE_RIGHT':
			self.arrows['itemshop']['arrowOnSale'] += 1
			self.ItemshopItemsRefresh()
		elif arrow == 'VOTESHOP_ONSALE_LEFT':
			self.arrows['voteshop']['arrowOnSale'] -= 1
			self.VoteshopItemsRefresh()
		elif arrow == 'VOTESHOP_ONSALE_RIGHT':
			self.arrows['voteshop']['arrowOnSale'] += 1
			self.VoteshopItemsRefresh()
		elif arrow == 'VOTESHOP_ONSALE_UP':
			self.arrows['voteshop']['arrowCategory'] -= 1
			self.VoteshopCategoryRefresh()
		elif arrow == 'VOTESHOP_ONSALE_DOWN':
			self.arrows['voteshop']['arrowCategory'] += 1
			self.VoteshopCategoryRefresh()
		elif arrow == 'ITEMSHOP_ONSALE_UP':
			self.arrows['itemshop']['arrowCategory'] -= 1
			self.ItemshopCategoryRefresh()
		elif arrow == 'ITEMSHOP_ONSALE_DOWN':
			self.arrows['itemshop']['arrowCategory'] += 1
			self.ItemshopCategoryRefresh()
		elif arrow == 'ACHIEVEMENTSHOP_ONSALE_LEFT':
			self.arrows['achievementshop']['arrowOnSale'] -= 1
			self.AchievementshopItemsRefresh()
		elif arrow == 'ACHIEVEMENTSHOP_ONSALE_RIGHT':
			self.arrows['achievementshop']['arrowOnSale'] += 1
			self.AchievementshopItemsRefresh()
		elif arrow == 'ACHIEVEMENTSHOP_ONSALE_UP':
			self.arrows['achievementshop']['arrowCategory'] -= 1
			self.AchievementshopItemsRefresh()
		elif arrow == 'ACHIEVEMENTSHOP_ONSALE_DOWN':
			self.arrows['achievementshop']['arrowCategory'] += 1
			self.AchievementshopItemsRefresh()
		

	## Category Buttons

	def __OnClickItemshopCategory(self, arg):
		self.category['itemshop'] = arg
		self.arrows['itemshop']['arrowOnSale'] = 1
		self.ItemshopItemsRefresh()

	def __OnClickVoteshopCategory(self, arg):
		self.category['voteshop'] = arg
		self.arrows['voteshop']['arrowOnSale'] = 1
		self.VoteshopItemsRefresh()
		
	def __OnClickAchievementshopCategory(self, arg):
		self.category['achievementshop'] = arg
		self.arrows['achievementshop']['arrowOnSale'] = 1
		self.AchievementshopItemsRefresh()

	## Show the current market price of coins
	def __OnClickQuestion(self):
		if self.PopUp.IsShow():
			self.PopUp.Close()
		else:
			self.PopUp.Open()

	## Close gui
	def __OnClickClose(self):
		self.Close()

	## Switch the banner
	def __OnClickBannerBtn(self, arg):
		self.SwitchBanner(arg)

	## Open link to buy coins
	def __OnClickBuyCoins(self):
		self.webWnd.Open(self.link['buyCoins'])

	## Open link to vote
	def __OnClickVote(self):
		self.webWnd.Open(self.link['vote'])

	########################
	## OnClick Events END ##
	########################

	## Other functions [ConvertNumberToCoins, SetVoteshopCoins, SetItemshopCoins, CreateCategoryButton, SendChat, OnUpdate(BANNER,), SwitchBanner, SetAlpha]

	def ConvertNumberToCoins(self, coins, text):
		if coins <= 0 :
			return("0 %s" % text)

		return("%s %s" % ('.'.join([ i-3<0 and str(coins)[:i] or str(coins)[i-3:i] for i in range(len(str(coins))%3, len(str(coins))+1, 3) if i ]), text))

	def SetItemshopCoins(self, coins):
		self.elements['textline']['menue']['itemshop_coins'].SetText('%s' % self.ConvertNumberToCoins(coins, 'I-Coins'))

	def SetVoteshopCoins(self, coins):
		self.elements['textline']['menue']['voteshop_coins'].SetText('%s' % self.ConvertNumberToCoins(coins, 'V-Coins'))
		
	def SetAchievementshopCoins(self, coins):
		self.elements['textline']['menue']['achievementshop_coins'].SetText('%s' % self.ConvertNumberToCoins(coins, 'A-Coins'))

	def CreateCategoryButton(self, parent, x, y, text, func, arg):
		button = ui.Button()
		button.SetParent(parent)
		button.SetUpVisual("locale/de/ui/itemshop/btn_category_norm.sub")
		button.SetOverVisual("locale/de/ui/itemshop/btn_category_press.sub")
		button.SetDownVisual("locale/de/ui/itemshop/btn_category_hover.sub")
		button.SetText(text)
		button.SetEvent(ui.__mem_func__(func), arg)
		button.SetPosition(x, y)
		button.Show()
		return button


	def SendChat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, '<Shop>: '+str(text))

	def OnUpdate(self):
		## Banner UPDATE START

		if self.bannerVar['lastSwitch'] < time.clock():
			if self.bannerVar['currentImage'] == 1:
				self.SwitchBanner(0)
			else:
				self.SwitchBanner(1)

		## if image fade out activated, start fading out
		if self.bannerVar['fadeOut'] == 1:
			## get current time
			self.bannerVar['currentTime'] = time.clock()

			## if alpha value is bigger than zero, then check if it's time to change the alpha value - interval;
			## else deactivate fade out and hide the fade_banner and change the banner button 

			if self.bannerVar['currentAlphaValue'] > 0.0:
				if self.bannerVar['currentTime'] >= self.bannerVar['intervallEndTime']:
					newAlphaValue = self.bannerVar['currentAlphaValue'] 
					newAlphaValue -= self.bannerOptions['interval']
					self.SetAlpha(self.elements['images']['startpage']['fade_banner'], newAlphaValue)
					self.bannerVar['intervallEndTime'] = self.bannerVar['currentTime'] + self.bannerOptions['timeToFade']
			else:
				self.bannerVar['fadeOut'] = 0
				self.elements['images']['startpage']['fade_banner'].Hide()
		## Banner UPDATE END ## 
		
	## switch the banner with a fade out
	def SwitchBanner(self,newBanner):
		self.bannerVar['lastSwitch'] = time.clock() + self.bannerOptions['time'] + self.bannerOptions['timeToFade']/self.bannerOptions['interval']
		self.elements['images']['startpage']['fade_banner'].LoadImage(self.bannerOptions['folder'] + self.bannerOptions['banner_%d' % self.bannerVar['currentImage']] + '.jpg')
		self.elements['images']['startpage']['fade_banner'].Show()
		self.elements['images']['startpage']['banner'].LoadImage(self.bannerOptions['folder'] + self.bannerOptions['banner_%d' % newBanner]+ '.jpg')
		self.bannerVar['currentImage'] = newBanner
		self.SetAlpha(self.elements['images']['startpage']['fade_banner'], 1.0)
		self.bannerVar['fadeOut'] = 1
		self.bannerVar['intervallEndTime'] = self.bannerVar['currentTime'] + self.bannerOptions['timeToFade']
		self.ChangeBannerButton(newBanner)

	## set the alpha value of an image 'transparent'
	def SetAlpha(self, image, alpha):
		self.bannerVar['currentAlphaValue'] = alpha
		image.SetAlpha(alpha)
		
	def RoundUp(self, num):
		if (num + 1) != int(num+1):
			return int(num+1)
		else:
			return int(num)

		
	## Other functions end

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE

class ItemBox(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		self.time = None
		self.runOut = None
		self.price = None
		self.itemData = []
		self.lastTime = None
		
	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, 'uiscript/itemshop_v2_itembox.py')
		except:
			import exception
			exception.Abort('test.__LoadScript.LoadObject')

		try: 
			self.itemBox = self.GetChild('Background')
			self.timeBox = self.GetChild('TimeBox')
			self.countdown = self.GetChild('tx_countdown')
			self.percentBox = self.GetChild('PercentBox')
			self.tx_percent = self.GetChild('tx_percent')
			self.btn_buy = self.GetChild('btn_buy')
			self.itemName = self.GetChild('tx_itemName')
			self.itemPrice = self.GetChild('tx_itemPrice')
			self.amount = self.GetChild('ed_amount')
			self.amountBox = self.GetChild('sb_amount')
			self.icon = self.GetChild('icon_item')
			self.toolTip = uiToolTip.ItemToolTip()

			self.itemBuyQuestionDialog = ItemBuyDialog()
			
		except:
			import exception
			exception.Abort('test.__LoadScript.BindObject')

		try: 
			self.btn_buy.SetEvent(self.__OnClickBuy)
			self.amount.SetNumberMode()
			self.itemBuyQuestionDialog.SetAcceptEvent(lambda arg=TRUE: self.AnswerBuyItem(arg))
			self.itemBuyQuestionDialog.SetCancelEvent(lambda arg=FALSE: self.AnswerBuyItem(arg))

			self.icon.SAFE_SetStringEvent("MOUSE_OVER_IN",self.Icon_MouseOverIn)
			self.icon.SAFE_SetStringEvent("MOUSE_OVER_OUT",self.Icon_MouseOverOut)
		except:
			import exception
			exception.Abort('test.__LoadScript.BindEvent')

		self.isLoaded = TRUE

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Destroy(self):
		self.Hide()

	## Set the content of this box
	def SetContent(self, type, id, itemData, price):
		self.type = type
		self.itemData = itemData
		self.id = id ## id from mysql, used to identify the item from the table 
		self.price = price
		self.itemPrice.SetText('%d %s' % (price, (['I-Coins','V-Coins','A-Coins'])[type]))
		self.amount.SetText('1')

		item.SelectItem(itemData[0])
		if item.IsFlag(4) == 1:
			self.amountBox.Show()
		else:
			self.amountBox.Hide()

		self.itemName.SetText(item.GetItemName())

		## Load the image and scale the item if the slotsize is bigger than 1
		self.icon.LoadImage(str(item.GetIconImageFileName()))
		self.icon.SetScale(1, ([1, 0.6, 0.4])[item.GetItemSize()[1]-1])
		
		self.btn_buy.Enable()
		self.amount.KillFocus()
		self.amount.CanEdit(TRUE)
		self.timeBox.Hide()
		self.percentBox.Hide()

	def SetTime(self, time, runOut):
		if time == 0:
			self.timeBox.Hide()
			self.time = None
			return
		else:
			self.timeBox.Show()
			self.time = time
			self.runOut = runOut
			self.lastTime = 0

	def SetPercent(self, percent):
		if percent == 0:
			self.percentBox.Hide()
			return
		else:
			self.percentBox.LoadImage("locale/de/ui/itemshop/discount_percent_box.sub")
			self.percentBox.Show()
			
			self.itemPrice.SetText('%d %s' % (self.price-(self.price/100.00)*percent, (['I-Coins','V-Coins','A-Coins'])[self.type]))
			self.tx_percent.SetText(str(percent) + '%')
		
	## Set the parent to attach and the coordinates
	def Open(self,parent,x,y):
		if FALSE == self.isLoaded:
			self.__LoadScript()

		
		self.SetParent(parent)
		self.SetPosition(x,y)
		self.amount.SetText('1')
		self.btn_buy.Disable()
		self.amountBox.Hide()
		self.amount.CanEdit(FALSE)
		self.Show()

	def Icon_MouseOverIn(self):
		self.toolTip.ClearToolTip()
		item.SelectItem(self.itemData[0])
		attrSlot = [(self.itemData[4],self.itemData[5]),(self.itemData[6],self.itemData[7]),(self.itemData[8],self.itemData[9]),(self.itemData[10],self.itemData[11]),(self.itemData[12],self.itemData[13]),(self.itemData[14],self.itemData[15]),(self.itemData[16],self.itemData[17])]
		attrSlot += [(0,0) for i in range(player.ATTRIBUTE_SLOT_MAX_NUM-len(attrSlot))]
		
		## if item is real time (limit type) then calculate the time
		if item.GetLimit(0)[0] == 7:
			self.toolTip.AddItemData(self.itemData[0], [self.itemData[1] + app.GetGlobalTimeStamp(),self.itemData[2],self.itemData[3],0,0,0], attrSlot)
		else:
			self.toolTip.AddItemData(self.itemData[0], [self.itemData[1],self.itemData[2],self.itemData[3],0,0,0], attrSlot)

	def Icon_MouseOverOut(self):
		self.toolTip.Hide()

	def OnUpdate(self):
		amount = self.amount.GetText()
		if amount:
			## if the first character of amount is a 0 or its empty and not focused, then set the amount to 1
			if (amount != "" and amount[0] == '0') or (not self.amount.IsFocus() and amount == ""):
				self.amount.SetText('1')
			if int(amount) > 200:
				self.amount.SetText('200')

		## if time is set then calculate the time until end
		if self.time:
			remaining = self.time - app.GetGlobalTimeStamp()
			if self.lastTime < time.clock():
				if remaining <= 0:
					if self.runOut == 1:
						self.time = None
						self.countdown.SetText('Abgelaufen')
						self.btn_buy.Disable()
						self.amount.CanEdit(FALSE) ## new function in ui
					else:
						self.timeBox.Hide()
						self.percentBox.Hide()
						self.itemPrice.SetText('%d %s' % (self.price, (['I-Coins','V-Coins','A-Coins'])[self.type]))
					return

				self.lastTime = time.clock() + 1
				hoursRemaining = int(remaining) / 3600
				minutesRemaining = int(remaining % 3600) / 60
				secondsRemaining = int(remaining % 60)
				self.countdown.SetText('%dh %dm %ds' % (hoursRemaining, minutesRemaining, secondsRemaining))

	def __OnClickBuy(self):
		if self.amount.GetText() == '':
			self.amount.SetText('1')

		self.amount.KillFocus()
		amount = self.amount.GetText()
		price = int(amount) * int(self.itemPrice.GetText().split(' ')[0])

		if amount == '1':
			self.itemBuyQuestionDialog.SetText("Moechtest du %s für %d %s kaufen?" % (self.itemName.GetText(), price, (['I-Coins','V-Coins','A-Coins'])[self.type]))
		else:
			self.itemBuyQuestionDialog.SetText("Moechtest du %sx %s für %d %s kaufen?" % (amount, self.itemName.GetText(), price, (['I-Coins','V-Coins','A-Coins'])[self.type]))
		self.itemBuyQuestionDialog.Open()

	def AnswerBuyItem(self, arg):
		self.itemBuyQuestionDialog.Close()
		if arg == 1:
			# self.SendChat('BUY ID: %d AMOUNT: %s' % (self.id, self.amount.GetText()))
			import event
			constInfo.ITEMSHOP["questCMD"] = 'BUY#%d#%s' % (self.id, self.amount.GetText())
			event.QuestButtonClick(int(constInfo.ITEMSHOP["qid"]))
			## Send buy item : [type, id, amount]
		self.amount.SetText('1')
		
	def SendChat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, '<Shop>: '+str(text))



class ItemBuyDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def Open(self):
		global IS_BUY
		if IS_BUY == TRUE:
			return
		IS_BUY = TRUE
		self.SetCenterPosition()
		self.SetTop()
		self.Show()
		

	def Close(self):
		global IS_BUY
		IS_BUY = FALSE
		self.Hide()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.acceptButton.SAFE_SetEvent(event)

	def SAFE_SetCancelEvent(self, event):
		self.cancelButton.SAFE_SetEvent(event)

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE





class PricePopUp(ui.ScriptWindow):

	POPUPTXTLINK = "http://client.connect.ephyra2.info/shopprices.txt"

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		
	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/itemshop_popup.py")
		except:
			import exception
			exception.Abort("test.__LoadScript.LoadObject")

		try: 
			self.board = self.GetChild("ItemshopPopupBoard")
			self.closeBtn = self.GetChild("CloseButton")
			self.itemShopText = {
						"text_0" : self.GetChild("label_text_0"),
						"text_1" : self.GetChild("label_text_1"),
						"text_2" : self.GetChild("label_text_2"),
						"text_3" : self.GetChild("label_text_3"),
						}
			self.voteShopText = self.GetChild("label_text_4")
			self.slot = self.GetChild("ItemSlotPreview")

		except:
			import exception
			exception.Abort("test.__LoadScript.BindObject")
			
		self.closeBtn.SetEvent(ui.__mem_func__(self.Close))
		self.toolTip = uiToolTip.ItemToolTip()
		self.slot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.slot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		self.isLoaded = TRUE

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def Destroy(self):
		self.Close()
		
	def Open(self):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		self.SetTop()
		self.Show()
		self.BuildPage()

	def OverOutItem(self):
		self.toolTip.Hide()

	def OverInItem(self):
		self.toolTip.Show()
		self.toolTip.SetItemToolTip(self.vnum)

	def BuildPage(self):
		try:
			respons = str(urllib.urlopen(self.POPUPTXTLINK).read()) 
			self.txt = eval(respons)
			self.vnum = None
			count = None
			for i in range(4):
				if self.txt[i].find("[ITEMSHOP_TEXT_"+str(i)+"]") != -1:
					startIndex = self.txt[i].find("[ITEMSHOP_TEXT_"+str(i)+"]")+17
					endIndex = self.txt[i].find("[/ITEMSHOP_TEXT_"+str(i)+"]")
					self.itemShopText['text_'+str(i)].SetText(str((self.txt[i])[startIndex:endIndex]))
			if self.txt[4].find("[VOTESHOP_TEXT_0]") != -1:
				startIndex = self.txt[4].find("[VOTESHOP_TEXT_0]")+17
				endIndex = self.txt[4].find("[/VOTESHOP_TEXT_0]")
				self.voteShopText.SetText(str((self.txt[4])[startIndex:endIndex]))
			if self.txt[5].find("[VOTESHOP_ITEM_VNUM]") != -1:
				startIndex = self.txt[5].find("[VOTESHOP_ITEM_VNUM]")+20
				endIndex = self.txt[5].find("[/VOTESHOP_ITEM_VNUM]")
				self.vnum = int((self.txt[5])[startIndex:endIndex])

			if self.txt[6].find("[VOTESHOP_ITEM_COUNT]") != -1:
				startIndex = self.txt[6].find("[VOTESHOP_ITEM_COUNT]")+21
				endIndex = self.txt[6].find("[/VOTESHOP_ITEM_COUNT]")
				count = int((self.txt[6])[startIndex:endIndex])

			if self.vnum:
				self.slot.Show()
				self.slot.SetItemSlot(0, self.vnum, count)
				self.slot.RefreshSlot()
			else:
				self.slot.Hide()
		except:
			self.Hide()
	
	def SendSystemChat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "<System>: "+str(text))
		
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE
		
class LoadingBar(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		

	def __LoadScript(self):
		## Load gui
		try: 
			self.BindObjects()
		except:
			import exception
			exception.Abort('test.__LoadScript.BindObjects')
			
		## Load events
		try: 
			self.BindEvents()
		except:
			import exception
			exception.Abort('test.__LoadScript.BindEvents')
			
		self.isLoaded = TRUE
		
	## Bind the objects in __LoadScript
	def BindObjects(self):
		self.board = ui.ThinBoard()
		self.board.SetSize(260,30)
		self.board.SetCenterPosition()
		self.board.Show()

		self.progressBarActualFile = ui.AniImageBox()
		self.progressBarActualFile.SetParent(self.board)
		self.progressBarActualFile.AppendImage('locale\de\ui\itemshop\loadingBar.tga')
		self.progressBarActualFile.SetPosition(5, 8)
		self.progressBarActualFile.SetDelay(90)
		self.progressBarActualFile.SetPercentage(0, 100)
		self.progressBarActualFile.Show()

		self.lb_0 = ui.TextLine()
		self.lb_0.SetParent(self.board)
		self.lb_0.SetPosition(10,9)
		self.lb_0.SetText('Laden')
		self.lb_0.Show()

		self.lb_1 = ui.TextLine()
		self.lb_1.SetParent(self.board)
		self.lb_1.SetPosition(225,9)
		self.lb_1.SetText('0%')
		self.lb_1.Show()

	## Bind events to the objects in __LoadScript
	def BindEvents(self):
		pass
		#self.elements['buttons']['menue']['close'].SetEvent(self.__OnClickClose)

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	## Hide the Gui
	def Destroy(self):
		self.Hide()

	def SetPercent(self, percent):
		if percent >= 100:
			self.board.Hide()
		else:
			self.board.SetTop()
			self.board.Show()
			self.progressBarActualFile.SetPercentage(percent, 100)
			self.lb_1.SetText(str(percent) +'%')
		
	## Open the gui
	def Open(self):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		self.SetTop()
		self.Show()

	## Close the gui
	def Close(self):
		self.Hide()


