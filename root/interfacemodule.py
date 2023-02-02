##
## Interface
##
import constInfo
import systemSetting
import wndMgr
import chat
import app
import net
import player
import uiTaskBar
import uiCharacter
import uiInventory
import uiDragonSoul
import uiChat
import uiMessenger
import guild
if app.LWT_BUFF_UPDATE:
	import uiBuffiSkill
if app.ENABLE_LOTTERY_SYSTEM:
	import uilottery
import snd
import ui
import uiHelp
import uiWhisper
import uiPointReset
import uiShop
import uiExchange
import uiSystem
import uiRestart
import uiToolTip
import uiMiniMap
import uiParty
import uiSafebox
import uiGuild
import uiQuest
import uiPrivateShopBuilder
import uiCommon
import uiRefine
import uiEquipmentDialog
import uiGameButton
import uiTip
import uiCube
import uiCards
import miniMap
import uimultifarmblock
import uiitemshop_v2
# ACCESSORY_REFINE_ADD_METIN_STONE
import uiselectitem
# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE
import uiScriptLocale
import uitalenttree_v1
import talenttree
import uiDungeonCoolTime
import event
import localeInfo as _localeInfo
import uimyshopdeco
import uiitemfinder
if app.ENABLE_RENDER_TARGET_SYSTEM:
	import renderTargetExtension

if app.ENABLE_WHEEL_OF_FORTUNE:
	import uiWheelofFortune
if app.ENABLE_NEW_PET_SYSTEM:
	import uiPetSystem
	
if app.ENABLE_ASLAN_TELEPORTPANEL:
	import uiTeleportPanel

if app.ENABLE_SWITCHBOT:
	import uiSwitchbot

if app.ENABLE_SASH_SYSTEM:
	import uisash
	
if app.ENABLE_CHANGELOOK_SYSTEM:
	import uichangelook

if app.ENABLE_SHOW_CHEST_DROP:
	import uiChestDrop
	
if app.ENABLE_MELEY_LAIR_DUNGEON:
	import uidragonlairranking

if app.ENABLE_ASLAN_LOTTERY:
	import uiLotteryAslan
	
if app.ENABLE_EXTENDED_BATTLE_PASS:
	import uiBattlePassExtended
	
if app.ENABLE_BIYOLOG:
	import uiBiyolog
if app.ENABLE_SHOP_SEARCH_SYSTEM:
	import uiPrivateShopSearch
	
if app.WORLD_BOSS_YUMA:
	import uiworldbosstext

localeInfo = _localeInfo.localeInfo()
IsQBHide = 0
class Interface(object):
	CHARACTER_STATUS_TAB = 1
	CHARACTER_SKILL_TAB = 2
	
	def __init__(self):
		systemSetting.SetInterfaceHandler(self)
		self.windowOpenPosition = 0
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.onTopWindow = player.ON_TOP_WND_NONE
		self.dlgWhisperWithoutTarget = None
		self.inputDialog = None
		self.offlineDecoration = None
		self.tipBoard = None
		self.bigBoard = None
		if app.ENABLE_WHEEL_OF_FORTUNE:
			self.wndWheelofFortune=None
		if app.ENABLE_LOTTERY_SYSTEM:
			self.lottery = None
		# ITEM_MALL
		self.mallPageDlg = None
		# END_OF_ITEM_MALL
		if app.ENABLE_CUBE_RENEWAL:
			self.wndCubeRenewal = None
		self.wndWeb = None
		self.wndTaskBar = None
		self.wndCharacter = None
		self.wndInventory = None
		self.wndExpandedTaskBar = None
		self.wndDragonSoul = None
		self.wndDragonSoulRefine = None
		self.wndChat = None
		self.wndMessenger = None
		self.wndMiniMap = None
		self.wndFarmBlock = None
		self.wndGuild = None
		self.wndGuildBuilding = None
		if app.ENABLE_NEW_PET_SYSTEM:
			self.wndPetMainWindow = None

		if app.ENABLE_RENDER_TARGET_SYSTEM:
			self.wndTargetRender = None

		if app.ENABLE_ASLAN_LOTTERY:
			self.wndLottery = None
		if hasattr(app, "ENABLE_DUNGEON_COOL_TIME"):
			self.wndDungeonCoolTime = None
		if app.ENABLE_SWITCHBOT:
			self.wndSwitchbot = None
		if app.ENABLE_SHOW_CHEST_DROP:
			self.dlgChestDrop = None
		if app.ENABLE_ASLAN_TELEPORTPANEL:
			self.wndTeleportPanel = None
		if app.ENABLE_EXTENDED_BATTLE_PASS:
			self.wndBattlePassExtended = None
			self.isFirstOpeningExtBattlePass = False

		self.listGMName = {}
		self.wndQuestWindow = {}
		self.wndQuestWindowNewKey = 0
		self.privateShopAdvertisementBoardDict = {}
		self.guildScoreBoardDict = {}
		self.equipmentDialogDict = {}
		if app.ENABLE_DUNGEON_INFO_SYSTEM:
			self.wndDungeonInfo = None
		if app.WORLD_BOSS_YUMA:
			self.WorldbossHwnd = {}
		event.SetInterfaceWindow(self)
		self.wndGiftBox = None

	def __del__(self):
		systemSetting.DestroyInterfaceHandler()
		event.SetInterfaceWindow(None)

	################################
	## Make Windows & Dialogs
	def __MakeUICurtain(self):
		wndUICurtain = ui.Bar("TOP_MOST")
		wndUICurtain.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		wndUICurtain.SetColor(0x77000000)
		wndUICurtain.Hide()
		self.wndUICurtain = wndUICurtain

	def __MakeMessengerWindow(self):
		self.wndMessenger = uiMessenger.MessengerWindow()

		from _weakref import proxy
		self.wndMessenger.SetWhisperButtonEvent(lambda n,i=proxy(self):i.OpenWhisperDialog(n))
		self.wndMessenger.SetGuildButtonEvent(ui.__mem_func__(self.ToggleGuildWindow))

	def __MakeGuildWindow(self):
		self.wndGuild = uiGuild.GuildWindow()
		
	if hasattr(app, "ENABLE_DUNGEON_COOL_TIME"):
		def __MakeDungeonCoolTime(self):
			self.wndDungeonCoolTime = uiDungeonCoolTime.DungeonCoolTimeWindow()
			self.wndDungeonCoolTime.Hide()

	def __MakeChatWindow(self):
		
		wndChat = uiChat.ChatWindow()
		
		wndChat.SetSize(wndChat.CHAT_WINDOW_WIDTH - 100, 0)
		wndChat.SetPosition(wndMgr.GetScreenWidth()/2 - wndChat.CHAT_WINDOW_WIDTH/2 + 1, wndMgr.GetScreenHeight() - wndChat.EDIT_LINE_HEIGHT - 50)
		wndChat.SetHeight(200)
		wndChat.Refresh()
		wndChat.Show()

		self.wndChat = wndChat
		self.wndChat.BindInterface(self)
		self.wndChat.SetSendWhisperEvent(ui.__mem_func__(self.OpenWhisperDialogWithoutTarget))
		self.wndChat.SetOpenChatLogEvent(ui.__mem_func__(self.ToggleChatLogWindow))

	def __OnClickGiftButton(self):
		if self.wndGameButton:
			if not self.wndGiftBox.IsShow():
				self.wndGiftBox.Open()
			else:
				self.wndGiftBox.Close()

	def ClearGift(self):
		if self.wndGameButton:
			self.wndGameButton.HideGiftButton()
		if self.wndGiftBox:
			self.wndGiftBox.Clear()
			self.wndGiftBox.Refresh()

	def __MakeTaskBar(self):
		wndTaskBar = uiTaskBar.TaskBar()
		wndTaskBar.LoadWindow()
		self.wndTaskBar = wndTaskBar
		self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_CHARACTER, ui.__mem_func__(self.ToggleCharacterWindowStatusPage))
		self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_INVENTORY, ui.__mem_func__(self.ToggleInventoryWindow))
		self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_MESSENGER, ui.__mem_func__(self.ToggleMessenger))
		self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_SYSTEM, ui.__mem_func__(self.ToggleSystemDialog))
		if uiTaskBar.TaskBar.IS_EXPANDED:
			self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_EXPAND, ui.__mem_func__(self.ToggleExpandedButton))
			self.wndExpandedTaskBar = uiTaskBar.ExpandedTaskBar()
			self.wndExpandedTaskBar.LoadWindow()
			self.wndExpandedTaskBar.SetToggleButtonEvent(uiTaskBar.ExpandedTaskBar.BUTTON_DRAGON_SOUL, ui.__mem_func__(self.ToggleDragonSoulWindow))
			#self.wndExpandedTaskBar.SetToggleButtonEvent(uiTaskBar.ExpandedTaskBar.BUTTON_PET_GUI, ui.__mem_func__(self.TogglePetMain))
		else:
			self.wndTaskBar.SetToggleButtonEvent(uiTaskBar.TaskBar.BUTTON_CHAT, ui.__mem_func__(self.ToggleChat))
		
		# self.wndEnergyBar = None
		# import app
		# if app.ENABLE_ENERGY_SYSTEM:
			# wndEnergyBar = uiTaskBar.EnergyBar()
			# wndEnergyBar.LoadWindow()
			# self.wndEnergyBar = wndEnergyBar
		import uiGift
		wndGiftBox=uiGift.GiftDialog()
		wndGiftBox.Hide()
		self.wndGiftBox=wndGiftBox

	def __MakeParty(self):
		wndParty = uiParty.PartyWindow()
		wndParty.Hide()
		self.wndParty = wndParty

	def __MakeGameButtonWindow(self):
		wndGameButton = uiGameButton.GameButtonWindow()
		wndGameButton.SetTop()
		wndGameButton.Show()
		wndGameButton.SetButtonEvent("STATUS", ui.__mem_func__(self.__OnClickStatusPlusButton))
		wndGameButton.SetButtonEvent("SKILL", ui.__mem_func__(self.__OnClickSkillPlusButton))
		wndGameButton.SetButtonEvent("QUEST", ui.__mem_func__(self.__OnClickQuestButton))
		wndGameButton.SetButtonEvent("HELP", ui.__mem_func__(self.__OnClickHelpButton))
		wndGameButton.SetButtonEvent("BUILD", ui.__mem_func__(self.__OnClickBuildButton))
		wndGameButton.SetButtonEvent("GIFT", ui.__mem_func__(self.__OnClickGiftButton))

		self.wndGameButton = wndGameButton

	def __IsChatOpen(self):
		return TRUE
		
	def __MakeWindows(self):
		wndCharacter = uiCharacter.CharacterWindow()
		wndInventory = uiInventory.InventoryWindow()
		wndInventory.BindInterfaceClass(self)
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			wndDragonSoul = uiDragonSoul.DragonSoulWindow()	
			wndDragonSoulRefine = uiDragonSoul.DragonSoulRefineWindow()
		else:
			wndDragonSoul = None
			wndDragonSoulRefine = None
 
		if app.ENABLE_NEW_PET_SYSTEM:
			self.wndPetMainWindow = uiPetSystem.PetSystemMain()
			self.wndPetMainWindow.BindInterface(self)
			
		wndMiniMap = uiMiniMap.MiniMap()
		wndSafebox = uiSafebox.SafeboxWindow()

		if app.WJ_ENABLE_TRADABLE_ICON:
			wndSafebox.BindInterface(self)
		
		# ITEM_MALL
		wndMall = uiSafebox.MallWindow()
		self.wndMall = wndMall
		# END_OF_ITEM_MALL

		wndChatLog = uiChat.ChatLogWindow()
		wndChatLog.BindInterface(self)
		
		self.wndCharacter = wndCharacter
		self.wndInventory = wndInventory
		self.wndDragonSoul = wndDragonSoul
		self.wndDragonSoulRefine = wndDragonSoulRefine
		self.wndMiniMap = wndMiniMap
		self.wndFarmBlock = uimultifarmblock.MainWindow()
		self.wndSafebox = wndSafebox
		if app.ENABLE_ASLAN_LOTTERY:
			self.wndLottery = uiLotteryAslan.LotteryWindow()
		self.wndChatLog = wndChatLog
		if app.ENABLE_SHOW_CHEST_DROP:
			self.dlgChestDrop = uiChestDrop.ChestDropWindow()
		
		if app.ENABLE_RENDER_TARGET_SYSTEM:
			self.wndTargetRender = renderTargetExtension.RenderTarget.Get()
			self.wndTargetRender.BindInterface(self)
			self.wndTargetRender.Hide()

		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.SetDragonSoulRefineWindow(self.wndDragonSoulRefine)
			self.wndDragonSoulRefine.SetInventoryWindows(self.wndInventory, self.wndDragonSoul)
			self.wndInventory.SetDragonSoulRefineWindow(self.wndDragonSoulRefine)
		if app.ENABLE_SWITCHBOT:
			self.wndSwitchbot = uiSwitchbot.SwitchbotWindow()
			
		if app.ENABLE_LOTTERY_SYSTEM:
			self.lottery = uilottery.LotteryWindow()
			self.lottery.LoadWindow()
			
		if app.ENABLE_ASLAN_TELEPORTPANEL:
			self.wndTeleportPanel = uiTeleportPanel.TeleportPanel()

	def __MakeDialogs(self):
		if app.ENABLE_DUNGEON_INFO_SYSTEM:
			import uiDungeonInfo
			self.wndDungeonInfo = uiDungeonInfo.DungeonInfo()
		self.Itemshop_v2 = uiitemshop_v2.Itemshop()
		self.dlgExchange = uiExchange.ExchangeDialog()
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.dlgExchange.BindInterface(self)
			self.dlgExchange.SetInven(self.wndInventory)
			self.wndInventory.BindWindow(self.dlgExchange)
		self.dlgExchange.LoadDialog()
		self.dlgExchange.SetCenterPosition()
		self.dlgExchange.Hide()

		if app.ENABLE_EXTENDED_BATTLE_PASS:
			self.wndBattlePassExtended = uiBattlePassExtended.BattlePassWindow()
			
		if app.LWT_BUFF_UPDATE:
			self.dlgBuffiSkill = uiBuffiSkill.BuffiSkillDialog()
			self.dlgBuffiSkill.LoadDialog()
			self.dlgBuffiSkill.SetCenterPosition()
			self.dlgBuffiSkill.Hide()

		self.dlgPointReset = uiPointReset.PointResetDialog()
		self.dlgPointReset.LoadDialog()
		self.dlgPointReset.Hide()

		self.dlgShop = uiShop.ShopDialog()
		if app.WJ_ENABLE_TRADABLE_ICON:
			self.dlgShop.BindInterface(self)
		self.dlgShop.LoadDialog()
		self.dlgShop.Hide()

		self.dlgRestart = uiRestart.RestartDialog()
		self.dlgRestart.LoadDialog()
		self.dlgRestart.Hide()

		self.dlgSystem = uiSystem.SystemDialog()
		self.dlgSystem.LoadDialog()
		self.dlgSystem.SetOpenHelpWindowEvent(ui.__mem_func__(self.OpenHelpWindow))

		self.dlgSystem.Hide()

		self.dlgPassword = uiSafebox.PasswordDialog()
		self.dlgPassword.Hide()

		self.hyperlinkItemTooltip = uiToolTip.HyperlinkItemToolTip()
		self.hyperlinkItemTooltip.Hide()

		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()

		self.tooltipSkill = uiToolTip.SkillToolTip()
		self.tooltipSkill.Hide()

		self.privateShopBuilder = uiPrivateShopBuilder.PrivateShopBuilder()
		self.privateShopBuilder.Hide()

		self.dlgRefineNew = uiRefine.RefineDialogNew()
		
		if app.ENABLE_RENDER_TARGET_SYSTEM:
			self.tooltipItem.BindInterface(self)

		if app.WJ_ENABLE_TRADABLE_ICON:
			self.dlgRefineNew.SetInven(self.wndInventory)
			self.wndInventory.BindWindow(self.dlgRefineNew)
		self.dlgRefineNew.Hide()

	def __MakeHelpWindow(self):
		self.wndHelp = uiHelp.HelpWindow()
		self.wndHelp.LoadDialog()
		self.wndHelp.SetCloseEvent(ui.__mem_func__(self.CloseHelpWindow))
		self.wndHelp.Hide()

	def __MakeTipBoard(self):
		self.tipBoard = uiTip.TipBoard()
		self.tipBoard.Hide()

		self.bigBoard = uiTip.BigBoard()
		self.bigBoard.Hide()
		
	if app.ENABLE_MELEY_LAIR_DUNGEON:
		def __MakeMeleyRanking(self):
			self.wndMeleyRanking = uidragonlairranking.Window()
			self.wndMeleyRanking.LoadWindow()
			self.wndMeleyRanking.Hide()
	def __MakeWebWindow(self):
		if constInfo.IN_GAME_SHOP_ENABLE:
			import uiWeb
			self.wndWeb = uiWeb.WebWindow()
			self.wndWeb.LoadWindow()
			self.wndWeb.Hide()

	if app.ENABLE_SHOP_SEARCH_SYSTEM:
		def __MakePrivateShopSearchWindow(self):
			self.wndPrivateShopSearch = uiPrivateShopSearch.PrivateShopSearchDialog()
			self.wndPrivateShopSearch.LoadWindow()
			self.wndPrivateShopSearch.Hide()

	if app.ENABLE_SASH_SYSTEM:
		def __MakeSashWindow(self):
			self.wndSashCombine = uisash.CombineWindow()
			self.wndSashCombine.LoadWindow()
			self.wndSashCombine.Hide()

			self.wndSashAbsorption = uisash.AbsorbWindow()
			self.wndSashAbsorption.LoadWindow()
			self.wndSashAbsorption.Hide()

			if self.wndInventory:
				self.wndInventory.SetSashWindow(self.wndSashCombine, self.wndSashAbsorption)

	if app.ENABLE_CHANGELOOK_SYSTEM:
		def __MakeChangeLookWindow(self):
			self.wndChangeLook = uichangelook.Window()
			self.wndChangeLook.LoadWindow()
			self.wndChangeLook.Hide()

			if self.wndInventory:
				self.wndInventory.SetChangeLookWindow(self.wndChangeLook)

	def __MakeCubeWindow(self):
		self.wndCube = uiCube.CubeWindow()
		self.wndCube.LoadWindow()
		self.wndCube.Hide()

	def __MakeCubeResultWindow(self):
		self.wndCubeResult = uiCube.CubeResultWindow()
		self.wndCubeResult.LoadWindow()
		self.wndCubeResult.Hide()
		
	def __MakeNewTestWindow(self):
		self.wndTalent = uitalenttree_v1.TalentTreeWindow()
		self.wndTalent.LoadWindow()
		self.wndTalent.Hide()
	def __MakeCardsInfoWindow(self):
		self.wndCardsInfo = uiCards.CardsInfoWindow()
		self.wndCardsInfo.LoadWindow()
		self.wndCardsInfo.Hide()
		
	def __MakeCardsWindow(self):
		self.wndCards = uiCards.CardsWindow()
		self.wndCards.LoadWindow()
		self.wndCards.Hide()
		
	def __MakeCardsIconWindow(self):
		self.wndCardsIcon = uiCards.IngameWindow()
		self.wndCardsIcon.LoadWindow()
		self.wndCardsIcon.Hide()
		
	def __MakeItemFinder(self):
		self.wndItemFinder = uiitemfinder.ItemFinder()
		self.wndItemFinder.LoadWindow()
		self.wndItemFinder.Hide()

	# ACCESSORY_REFINE_ADD_METIN_STONE
	def __MakeItemSelectWindow(self):
		self.wndItemSelect = uiselectitem.SelectItemWindow()
		self.wndItemSelect.Hide()
		
	# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE
	
	if app.ENABLE_CUBE_RENEWAL:
		def __MakeCubeRenewal(self):
			import uicuberenewal
			self.wndCubeRenewal = uicuberenewal.CubeRenewalWindows()
			self.wndCubeRenewal.Hide()
				
	def MakeInterface(self):
		self.__MakeMessengerWindow()
		self.__MakeGuildWindow()
		self.__MakeChatWindow()
		self.__MakeParty()
		self.__MakeWindows()
		self.__MakeDialogs()

		self.__MakeUICurtain()
		self.__MakeTaskBar()
		self.__MakeGameButtonWindow()
		self.__MakeHelpWindow()
		self.__MakeTipBoard()
		if app.ENABLE_BIYOLOG:
			self.MakeBioWindow()
		self.__MakeWebWindow()
		if app.ENABLE_CUBE_RENEWAL:
			self.__MakeCubeRenewal()
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			self.__MakeMeleyRanking()
		if app.ENABLE_SASH_SYSTEM:
			self.__MakeSashWindow()
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.__MakeChangeLookWindow()
		self.__MakeCubeWindow()
		self.__MakeCubeResultWindow()
		if app.ENABLE_SHOP_SEARCH_SYSTEM:
			self.__MakePrivateShopSearchWindow()
		if hasattr(app, "ENABLE_DUNGEON_COOL_TIME"):
			self.__MakeDungeonCoolTime()
		self.__MakeCardsInfoWindow()
		self.__MakeCardsWindow()
		self.__MakeCardsIconWindow()
		self.__MakeItemFinder()
		self.__MakeNewTestWindow()
		
		
		# ACCESSORY_REFINE_ADD_METIN_STONE
		self.__MakeItemSelectWindow()
		# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE

		self.questButtonList = []
		self.whisperButtonList = []
		self.whisperDialogDict = {}
		self.privateShopAdvertisementBoardDict = {}

		self.wndInventory.SetItemToolTip(self.tooltipItem)
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.SetItemToolTip(self.tooltipItem)
			self.wndDragonSoulRefine.SetItemToolTip(self.tooltipItem)
		self.wndSafebox.SetItemToolTip(self.tooltipItem)
		if app.ENABLE_SASH_SYSTEM:
			self.wndSashCombine.SetItemToolTip(self.tooltipItem)
			self.wndSashAbsorption.SetItemToolTip(self.tooltipItem)
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.wndChangeLook.SetItemToolTip(self.tooltipItem)
		self.wndCube.SetItemToolTip(self.tooltipItem)
		self.wndCubeResult.SetItemToolTip(self.tooltipItem)
		
		if app.ENABLE_SWITCHBOT:
			self.wndSwitchbot.SetItemToolTip(self.tooltipItem)
		if app.ENABLE_SHOP_SEARCH_SYSTEM:
			self.wndPrivateShopSearch.SetItemToolTip(self.tooltipItem)	
		# ITEM_MALL
		self.wndMall.SetItemToolTip(self.tooltipItem)
		# END_OF_ITEM_MALL

		self.wndCharacter.SetSkillToolTip(self.tooltipSkill)
		self.wndTaskBar.SetItemToolTip(self.tooltipItem)
		self.wndTaskBar.SetSkillToolTip(self.tooltipSkill)
		self.wndGuild.SetSkillToolTip(self.tooltipSkill)
		if app.LWT_BUFF_UPDATE:
			self.dlgBuffiSkill.SetSkillToolTip(self.tooltipSkill)
			self.dlgBuffiSkill.SetItemToolTip(self.tooltipItem)

		# ACCESSORY_REFINE_ADD_METIN_STONE
		self.wndItemSelect.SetItemToolTip(self.tooltipItem)
		# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE
		if app.ENABLE_SHOW_CHEST_DROP:
			self.dlgChestDrop.SetItemToolTip(self.tooltipItem)

		self.dlgShop.SetItemToolTip(self.tooltipItem)
		self.dlgExchange.SetItemToolTip(self.tooltipItem)
		self.privateShopBuilder.SetItemToolTip(self.tooltipItem)

		self.__InitWhisper()
		self.DRAGON_SOUL_IS_QUALIFIED = FALSE

	def MakeHyperlinkTooltip(self, hyperlink): 
		tokens = hyperlink.split(":") 
		if tokens and len(tokens): 
			type = tokens[0] 
			if "item" == type: 
				self.hyperlinkItemTooltip.SetHyperlinkItem(tokens) 
			else: 
				self.OpenWhisperDialog(type)  

	## Make Windows & Dialogs
	################################

	def Close(self):
		if self.Itemshop_v2:
			self.Itemshop_v2.Destroy()
		del self.Itemshop_v2
		if self.dlgWhisperWithoutTarget:
			self.dlgWhisperWithoutTarget.Destroy()
			del self.dlgWhisperWithoutTarget

		if uiQuest.QuestDialog.__dict__.has_key("QuestCurtain"):
			uiQuest.QuestDialog.QuestCurtain.Close()

		if self.wndQuestWindow:
			for key, eachQuestWindow in self.wndQuestWindow.items():
				eachQuestWindow.nextCurtainMode = -1
				eachQuestWindow.CloseSelf()
				eachQuestWindow = None
		self.wndQuestWindow = {}
		
		if app.ENABLE_WHEEL_OF_FORTUNE:
			if self.wndWheelofFortune:
				self.wndWheelofFortune.Hide()
				self.wndWheelofFortune.Destroy()
				self.wndWheelofFortune=None
		if self.wndChat:
			self.wndChat.Destroy()

		if self.wndTaskBar:
			self.wndTaskBar.Destroy()
		
		if self.wndExpandedTaskBar:
			self.wndExpandedTaskBar.Destroy()
			
		if app.LWT_BUFF_UPDATE and self.dlgBuffiSkill:
			self.dlgBuffiSkill.Destroy()
			
		# if self.wndEnergyBar:
			# self.wndEnergyBar.Destroy()

		if self.wndCharacter:
			self.wndCharacter.Destroy()

		if self.wndInventory:
			self.wndInventory.Destroy()
			
		if self.wndDragonSoul:
			self.wndDragonSoul.Destroy()

		if self.wndDragonSoulRefine:
			self.wndDragonSoulRefine.Destroy()

		if self.dlgExchange:
			self.dlgExchange.Destroy()

		if self.dlgPointReset:
			self.dlgPointReset.Destroy()

		if self.dlgShop:
			self.dlgShop.Destroy()

		if self.dlgRestart:
			self.dlgRestart.Destroy()

		if self.dlgSystem:
			self.dlgSystem.Destroy()

		if self.dlgPassword:
			self.dlgPassword.Destroy()

		if self.wndMiniMap:
			self.wndMiniMap.Destroy()
			
		if self.wndFarmBlock:
			self.wndFarmBlock.Destroy()

		if self.wndSafebox:
			self.wndSafebox.Destroy()

		if self.wndWeb:
			self.wndWeb.Destroy()
			self.wndWeb = None

		if self.wndMall:
			self.wndMall.Destroy()

		if self.wndParty:
			self.wndParty.Destroy()

		if self.wndHelp:
			self.wndHelp.Destroy()
			
		if self.wndCardsInfo:
			self.wndCardsInfo.Destroy()

		if self.wndCards:
			self.wndCards.Destroy()

		if self.wndCardsIcon:
			self.wndCardsIcon.Destroy()
			
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			if self.wndMeleyRanking:
				self.wndMeleyRanking.Destroy()

		if app.ENABLE_SASH_SYSTEM:
			if self.wndSashCombine:
				self.wndSashCombine.Destroy()

			if self.wndSashAbsorption:
				self.wndSashAbsorption.Destroy()

		if app.ENABLE_CHANGELOOK_SYSTEM:
			if self.wndChangeLook:
				self.wndChangeLook.Destroy()

		if self.wndCube:
			self.wndCube.Destroy()
			
		if self.wndCubeResult:
			self.wndCubeResult.Destroy()

		if self.wndMessenger:
			self.wndMessenger.Destroy()
			
		if self.wndItemFinder:
			self.wndItemFinder.Destroy()

		if self.wndGuild:
			self.wndGuild.Destroy()

		if self.privateShopBuilder:
			self.privateShopBuilder.Destroy()

		if self.dlgRefineNew:
			self.dlgRefineNew.Destroy()

		if self.wndGuildBuilding:
			self.wndGuildBuilding.Destroy()

		if self.wndGameButton:
			self.wndGameButton.Destroy()
		if self.wndTalent:
			self.wndTalent.Destroy()

		# ITEM_MALL
		if self.mallPageDlg:
			self.mallPageDlg.Destroy()
		# END_OF_ITEM_MALL
        
		if app.ENABLE_NEW_PET_SYSTEM:
			if self.wndPetMainWindow:
				self.wndPetMainWindow.Destroy()
				
		if app.ENABLE_ASLAN_LOTTERY:
			if self.wndLottery:
				self.wndLottery.Destroy()
		
		if app.ENABLE_SHOW_CHEST_DROP:
			if self.dlgChestDrop:
				self.dlgChestDrop.Destroy()
				
		if app.ENABLE_ASLAN_TELEPORTPANEL:
			if self.wndTeleportPanel:
				self.wndTeleportPanel.Destroy()

		if app.ENABLE_EXTENDED_BATTLE_PASS:
			if self.wndBattlePassExtended:
				self.wndBattlePassExtended.Destroy()

		# ACCESSORY_REFINE_ADD_METIN_STONE
		if self.wndItemSelect:
			self.wndItemSelect.Destroy()
		# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE
		
		if hasattr(app, "ENABLE_DUNGEON_COOL_TIME"):
			if self.wndDungeonCoolTime:
				if self.wndDungeonCoolTime.IsShow():
					self.wndDungeonCoolTime.Close()

				self.wndDungeonCoolTime.Destroy()
		
		if app.ENABLE_CUBE_RENEWAL:
			if self.wndCubeRenewal:
				self.wndCubeRenewal.Destroy()
				self.wndCubeRenewal.Close()
				
		if app.ENABLE_SWITCHBOT:
			if self.wndSwitchbot:
				self.wndSwitchbot.Destroy()

		if app.ENABLE_RENDER_TARGET_SYSTEM:
			if self.wndTargetRender:
				self.wndTargetRender.Destroy()
				
		if app.ENABLE_BIYOLOG:
			if self.wndBio:
				self.wndBio.Destroy()
				del self.wndBio
				
		if app.WORLD_BOSS_YUMA:
			if self.WorldbossHwnd:
				self.WorldbossHwnd = {}

		self.wndChatLog.Destroy()
		if app.ENABLE_DUNGEON_INFO_SYSTEM:
			if self.wndDungeonInfo:
				self.wndDungeonInfo.Destroy()
		for btn in self.questButtonList:
			btn.SetEvent(0)
		for btn in self.whisperButtonList:
			btn.SetEvent(0)
		for dlg in self.whisperDialogDict.itervalues():
			dlg.Destroy()
		for brd in self.guildScoreBoardDict.itervalues():
			brd.Destroy()
		for dlg in self.equipmentDialogDict.itervalues():
			dlg.Destroy()

		# ITEM_MALL
		del self.mallPageDlg
		# END_OF_ITEM_MALL

		del self.wndGuild
		del self.wndMessenger
		del self.wndUICurtain
		del self.wndChat
		del self.wndTaskBar
		if app.ENABLE_CUBE_RENEWAL:
			del self.wndCubeRenewal
		if self.wndExpandedTaskBar:
			del self.wndExpandedTaskBar
		# del self.wndEnergyBar
		del self.wndCharacter
		del self.wndInventory
		if self.wndDragonSoul:
			del self.wndDragonSoul
		if self.wndDragonSoulRefine:
			del self.wndDragonSoulRefine
		if app.LWT_BUFF_UPDATE:
			del self.dlgBuffiSkill
		del self.dlgExchange
		del self.dlgPointReset
		del self.dlgShop
		del self.dlgRestart
		del self.dlgSystem
		del self.dlgPassword
		del self.hyperlinkItemTooltip
		del self.tooltipItem
		del self.tooltipSkill
		del self.wndMiniMap
		del self.wndFarmBlock
		del self.wndSafebox
		del self.wndMall
		del self.wndParty
		del self.wndHelp
		del self.wndCardsInfo
		del self.wndCards
		del self.wndCardsIcon
		if app.ENABLE_MELEY_LAIR_DUNGEON:
			del self.wndMeleyRanking
		if app.ENABLE_SASH_SYSTEM:
			del self.wndSashCombine
			del self.wndSashAbsorption
		if app.ENABLE_CHANGELOOK_SYSTEM:
			del self.wndChangeLook
		del self.wndCube
		del self.wndCubeResult
		del self.privateShopBuilder
		del self.inputDialog
		if app.ENABLE_LOTTERY_SYSTEM:
			if self.lottery:
				self.lottery.Destroy()
				del self.lottery
		del self.wndItemFinder
		del self.offlineDecoration
		del self.wndChatLog
		del self.dlgRefineNew
		del self.wndGuildBuilding
		del self.wndGameButton
		if app.ENABLE_NEW_PET_SYSTEM:
			del self.wndPetMainWindow
		if app.ENABLE_ASLAN_TELEPORTPANEL:
			del self.wndTeleportPanel
		del self.tipBoard
		del self.bigBoard
		del self.wndItemSelect
		if app.ENABLE_ASLAN_LOTTERY:
			del self.wndLottery
		if hasattr(app, "ENABLE_DUNGEON_COOL_TIME"):
			del self.wndDungeonCoolTime
		if app.ENABLE_SWITCHBOT:
			del self.wndSwitchbot
		if app.ENABLE_SHOW_CHEST_DROP:
			if self.dlgChestDrop:
				del self.dlgChestDrop
		del self.wndTalent
		if app.ENABLE_RENDER_TARGET_SYSTEM:
			del self.wndTargetRender
		if app.ENABLE_SHOP_SEARCH_SYSTEM:
			if self.wndPrivateShopSearch:
				self.wndPrivateShopSearch.Destroy()
				
		if app.ENABLE_EXTENDED_BATTLE_PASS:
			del self.wndBattlePassExtended

		self.questButtonList = []
		if app.ENABLE_DUNGEON_INFO_SYSTEM:
			if self.wndDungeonInfo:
				del self.wndDungeonInfo
		self.whisperButtonList = []
		self.whisperDialogDict = {}
		self.privateShopAdvertisementBoardDict = {}
		self.guildScoreBoardDict = {}
		self.equipmentDialogDict = {}

		if self.wndGiftBox:
			self.wndGiftBox.Clear()
			self.wndGiftBox.Hide()
			self.wndGiftBox.Destroy()
		del self.wndGiftBox

		uiChat.DestroyChatInputSetWindow()

	def OpenGift(self):
		if self.wndGameButton:
			self.wndGameButton.ShowGiftButton()

	## Skill
	def OnUseSkill(self, slotIndex, coolTime):
		self.wndCharacter.OnUseSkill(slotIndex, coolTime)
		self.wndTaskBar.OnUseSkill(slotIndex, coolTime)
		self.wndGuild.OnUseSkill(slotIndex, coolTime)

	def OnActivateSkill(self, slotIndex):
		self.wndCharacter.OnActivateSkill(slotIndex)
		self.wndTaskBar.OnActivateSkill(slotIndex)

	def OnDeactivateSkill(self, slotIndex):
		self.wndCharacter.OnDeactivateSkill(slotIndex)
		self.wndTaskBar.OnDeactivateSkill(slotIndex)

	def OnChangeCurrentSkill(self, skillSlotNumber):
		self.wndTaskBar.OnChangeCurrentSkill(skillSlotNumber)

	def SelectMouseButtonEvent(self, dir, event):
		self.wndTaskBar.SelectMouseButtonEvent(dir, event)

	## Refresh
	def RefreshAlignment(self):
		self.wndCharacter.RefreshAlignment()

	def RefreshStatus(self):
		self.wndTaskBar.RefreshStatus()
		self.wndCharacter.RefreshStatus()
		self.wndInventory.RefreshStatus()
		# if self.wndEnergyBar:
			# self.wndEnergyBar.RefreshStatus()
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.RefreshStatus()

	def RefreshStamina(self):
		self.wndTaskBar.RefreshStamina()

	def RefreshSkill(self):
		self.wndCharacter.RefreshSkill()
		self.wndTaskBar.RefreshSkill()
		if app.LWT_BUFF_UPDATE and self.dlgBuffiSkill:
			self.dlgBuffiSkill.RefreshSkillData()

	def RefreshInventory(self):
		self.wndTaskBar.RefreshQuickSlot()
		self.wndInventory.RefreshItemSlot()
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.RefreshItemSlot()

	def RefreshCharacter(self): ## Character 페이지의 얼굴, Inventory 페이지의 전신 그림 등의 Refresh
		self.wndCharacter.RefreshCharacter()
		self.wndTaskBar.RefreshQuickSlot()

	def RefreshQuest(self):
		self.wndCharacter.RefreshQuest()

	def RefreshSafebox(self):
		self.wndSafebox.RefreshSafebox()

	# ITEM_MALL
	def RefreshMall(self):
		self.wndMall.RefreshMall()

	def OpenItemMall(self):
		if not self.mallPageDlg:
			self.mallPageDlg = uiShop.MallPageDialog()

		self.mallPageDlg.Open()
	# END_OF_ITEM_MALL

	def RefreshMessenger(self):
		self.wndMessenger.RefreshMessenger()

	def RefreshGuildInfoPage(self):
		self.wndGuild.RefreshGuildInfoPage()

	def RefreshGuildBoardPage(self):
		self.wndGuild.RefreshGuildBoardPage()

	def RefreshGuildMemberPage(self):
		self.wndGuild.RefreshGuildMemberPage()

	def RefreshGuildMemberPageGradeComboBox(self):
		self.wndGuild.RefreshGuildMemberPageGradeComboBox()

	def RefreshGuildSkillPage(self):
		self.wndGuild.RefreshGuildSkillPage()

	def RefreshGuildGradePage(self):
		self.wndGuild.RefreshGuildGradePage()

	def DeleteGuild(self):
		self.wndMessenger.ClearGuildMember()
		self.wndGuild.DeleteGuild()

	def RefreshMobile(self):
		self.dlgSystem.RefreshMobile()

	def OnMobileAuthority(self):
		self.dlgSystem.OnMobileAuthority()

	def OnBlockMode(self, mode):
		self.dlgSystem.OnBlockMode(mode)

	## Calling Functions
	# PointReset
	def OpenPointResetDialog(self):
		self.dlgPointReset.Show()
		self.dlgPointReset.SetTop()

	def ClosePointResetDialog(self):
		self.dlgPointReset.Close()

	# Shop
	def OpenShopDialog(self, vid):
		self.wndInventory.Show()
		self.wndInventory.SetTop()
		self.dlgShop.Open(vid)
		self.dlgShop.SetTop()

	def CloseShopDialog(self):
		self.dlgShop.Close()

	def RefreshShopDialog(self):
		self.dlgShop.Refresh()
		
	if app.ENABLE_SHOW_CHEST_DROP:
		def AddChestDropInfo(self, chestVnum, pageIndex, slotIndex, itemVnum, itemCount):
			self.dlgChestDrop.AddChestDropItem(int(chestVnum), int(pageIndex), int(slotIndex), int(itemVnum), int(itemCount))
			
		def RefreshChestDropInfo(self, chestVnum):
			self.dlgChestDrop.RefreshItems(chestVnum)

	## Quest
	def OpenCharacterWindowQuestPage(self):
		self.wndCharacter.Show()
		self.wndCharacter.SetState(6)

	def OpenQuestWindow(self, skin, idx):
		if constInfo.INPUT_IGNORE == 1:
			return 

		wnds = ()

		q = uiQuest.QuestDialog(skin, idx)
		q.SetWindowName("QuestWindow" + str(idx))
		q.Show()
		if skin:
			q.Lock()
			wnds = self.__HideWindows()

			# UNKNOWN_UPDATE
			q.AddOnDoneEvent(lambda tmp_self, args=wnds: self.__ShowWindows(args))
			# END_OF_UNKNOWN_UPDATE

		if skin:
			q.AddOnCloseEvent(q.Unlock)
		q.AddOnCloseEvent(lambda key = self.wndQuestWindowNewKey:ui.__mem_func__(self.RemoveQuestDialog)(key))
		self.wndQuestWindow[self.wndQuestWindowNewKey] = q

		self.wndQuestWindowNewKey = self.wndQuestWindowNewKey + 1

		# END_OF_UNKNOWN_UPDATE
		
	def RemoveQuestDialog(self, key):
		del self.wndQuestWindow[key]

	## Exchange
	def StartExchange(self):
		self.dlgExchange.OpenDialog()
		self.dlgExchange.Refresh()

	def EndExchange(self):
		self.dlgExchange.CloseDialog()

	def RefreshExchange(self):
		self.dlgExchange.Refresh()

	if app.WJ_ENABLE_TRADABLE_ICON:
		def CantTradableItemExchange(self, dstSlotIndex, srcSlotIndex):
			self.dlgExchange.CantTradableItem(dstSlotIndex, srcSlotIndex)

	if app.LWT_BUFF_UPDATE:
		def OpenBuffiDialog(self):
			self.dlgBuffiSkill.Open()

		def CloseBuffiDialog(self):
			self.dlgBuffiSkill.Close()

	## Party
	def AddPartyMember(self, pid, name):
		self.wndParty.AddPartyMember(pid, name)

		self.__ArrangeQuestButton()

	def UpdatePartyMemberInfo(self, pid):
		self.wndParty.UpdatePartyMemberInfo(pid)

	def RemovePartyMember(self, pid):
		self.wndParty.RemovePartyMember(pid)
		self.__ArrangeQuestButton()

	def LinkPartyMember(self, pid, vid):
		self.wndParty.LinkPartyMember(pid, vid)

	def UnlinkPartyMember(self, pid):
		self.wndParty.UnlinkPartyMember(pid)

	def UnlinkAllPartyMember(self):
		self.wndParty.UnlinkAllPartyMember()

	def ExitParty(self):
		self.wndParty.ExitParty()
		self.__ArrangeQuestButton()

	def PartyHealReady(self):
		self.wndParty.PartyHealReady()

	def ChangePartyParameter(self, distributionMode):
		self.wndParty.ChangePartyParameter(distributionMode)

	## Safebox
	def AskSafeboxPassword(self):
		if self.wndSafebox.IsShow():
			return

		# SAFEBOX_PASSWORD
		self.dlgPassword.SetTitle(localeInfo.PASSWORD_TITLE)
		self.dlgPassword.SetSendMessage("/safebox_password ")
		# END_OF_SAFEBOX_PASSWORD

		self.dlgPassword.ShowDialog()

	def OpenSafeboxWindow(self, size):
		self.dlgPassword.CloseDialog()
		self.wndSafebox.ShowWindow(size)

	def RefreshSafeboxMoney(self):
		self.wndSafebox.RefreshSafeboxMoney()

	def CommandCloseSafebox(self):
		self.wndSafebox.CommandCloseSafebox()
		
	if app.WORLD_BOSS_YUMA:
		def WorldbossNotification(self, szString):
			for i in range(len(constInfo.WORLD_BOSS_TEXT_POSITION)):
				if constInfo.WORLD_BOSS_TEXT_POSITION[i] == 0:
					constInfo.WORLD_BOSS_TEXT_POSITION[i] = 1
					self.WorldbossHwnd[i] = uiworldbosstext.WorldbossNotification(szString, i)
					break

	# ITEM_MALL
	def AskMallPassword(self):
		if self.wndMall.IsShow():
			return
		self.dlgPassword.SetTitle(localeInfo.MALL_PASSWORD_TITLE)
		self.dlgPassword.SetSendMessage("/mall_password ")
		self.dlgPassword.ShowDialog()

	def OpenMallWindow(self, size):
		self.dlgPassword.CloseDialog()
		self.wndMall.ShowWindow(size)

	def CommandCloseMall(self):
		self.wndMall.CommandCloseMall()
	# END_OF_ITEM_MALL

	## Guild
	def OnStartGuildWar(self, guildSelf, guildOpp):
		self.wndGuild.OnStartGuildWar(guildSelf, guildOpp)

		guildWarScoreBoard = uiGuild.GuildWarScoreBoard()
		guildWarScoreBoard.Open(guildSelf, guildOpp)
		guildWarScoreBoard.Show()
		self.guildScoreBoardDict[uiGuild.GetGVGKey(guildSelf, guildOpp)] = guildWarScoreBoard

	def OnEndGuildWar(self, guildSelf, guildOpp):
		self.wndGuild.OnEndGuildWar(guildSelf, guildOpp)

		key = uiGuild.GetGVGKey(guildSelf, guildOpp)

		if not self.guildScoreBoardDict.has_key(key):
			return

		self.guildScoreBoardDict[key].Destroy()
		del self.guildScoreBoardDict[key]

	# GUILDWAR_MEMBER_COUNT
	def UpdateMemberCount(self, gulidID1, memberCount1, guildID2, memberCount2):
		key = uiGuild.GetGVGKey(gulidID1, guildID2)

		if not self.guildScoreBoardDict.has_key(key):
			return

		self.guildScoreBoardDict[key].UpdateMemberCount(gulidID1, memberCount1, guildID2, memberCount2)
	# END_OF_GUILDWAR_MEMBER_COUNT

	def OnRecvGuildWarPoint(self, gainGuildID, opponentGuildID, point):
		key = uiGuild.GetGVGKey(gainGuildID, opponentGuildID)
		if not self.guildScoreBoardDict.has_key(key):
			return

		guildBoard = self.guildScoreBoardDict[key]
		guildBoard.SetScore(gainGuildID, opponentGuildID, point)

	## PK Mode
	def OnChangePKMode(self):
		self.wndCharacter.RefreshAlignment()
		self.dlgSystem.OnChangePKMode()

	## Refine
	
	if app.ENABLE_REFINE_RENEWAL:
		def CheckRefineDialog(self, isFail):
			self.dlgRefineNew.CheckRefine(isFail)
			
	def OpenRefineDialog(self, targetItemPos, nextGradeItemVnum, cost, prob, type):
		self.dlgRefineNew.Open(targetItemPos, nextGradeItemVnum, cost, prob, type)

	def AppendMaterialToRefineDialog(self, vnum, count):
		self.dlgRefineNew.AppendMaterial(vnum, count)

	## Show & Hide
	def ShowDefaultWindows(self):
		self.wndTaskBar.Show()
		self.wndMiniMap.Show()
		self.wndMiniMap.ShowMiniMap()
		# if self.wndEnergyBar:
			# self.wndEnergyBar.Show()

	def ShowAllWindows(self):
		self.wndTaskBar.Show()
		self.wndCharacter.Show()
		self.wndInventory.Show()
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.Show()
			self.wndDragonSoulRefine.Show()
		self.wndChat.Show()
		self.wndMiniMap.Show()
		# if self.wndEnergyBar:
			# self.wndEnergyBar.Show()
		if self.wndExpandedTaskBar:
			self.wndExpandedTaskBar.Show()
			self.wndExpandedTaskBar.SetTop()

	def HideAllWindows(self):
		if self.wndTaskBar:
			self.wndTaskBar.Hide()
			
		if app.ENABLE_SWITCHBOT:
			if self.wndSwitchbot:
				self.wndSwitchbot.Hide()
		
		# if self.wndEnergyBar:
			# self.wndEnergyBar.Hide()
			
		if self.wndTaskBar.TaskBarLeft:
			self.wndTaskBar.TaskBarLeft.Hide()

		if self.wndTaskBar.TaskBarLeft2:
			self.wndTaskBar.TaskBarLeft2.Hide()

		if self.wndCharacter:
			self.wndCharacter.Hide()

		if self.wndInventory:
			self.wndInventory.Hide()
			
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.Hide()
			self.wndDragonSoulRefine.Hide()

		if self.wndChat:
			self.wndChat.Hide()

		if self.wndMiniMap:
			self.wndMiniMap.Hide()

		if self.wndMessenger:
			self.wndMessenger.Hide()
            
		if app.ENABLE_NEW_PET_SYSTEM:
			if self.wndPetMainWindow:
				self.wndPetMainWindow.Hide()
				
		if app.ENABLE_ASLAN_LOTTERY:
			if self.wndLottery:
				self.wndLottery.Hide()
				
		if app.ENABLE_ASLAN_TELEPORTPANEL:
			if self.wndTeleportPanel:
				self.wndTeleportPanel.Hide()

		if app.ENABLE_EXTENDED_BATTLE_PASS:
			if self.wndBattlePassExtended:
				self.wndBattlePassExtended.Hide()

		if self.wndGuild:
			self.wndGuild.Hide()
			
		if self.wndExpandedTaskBar:
			self.wndExpandedTaskBar.Hide()
 
		if app.ENABLE_RENDER_TARGET_SYSTEM:
			if self.wndTargetRender:
				self.wndTargetRender.Hide()

	def ShowMouseImage(self):
		self.wndTaskBar.ShowMouseImage()
		if app.ENABLE_DUNGEON_INFO_SYSTEM:
			if self.wndDungeonInfo:
				self.wndDungeonInfo.Hide()

	def HideMouseImage(self):
		self.wndTaskBar.HideMouseImage()

	def ToggleChat(self):
		if TRUE == self.wndChat.IsEditMode():
			self.wndChat.CloseChat()
		else:
			# 웹페이지가 열렸을때는 채팅 입력이 안됨
			if self.wndWeb and self.wndWeb.IsShow():
				pass
			else:
				self.wndChat.OpenChat()

	def IsOpenChat(self):
		return self.wndChat.IsEditMode()

	def SetChatFocus(self):
		self.wndChat.SetChatFocus()

	def OpenRestartDialog(self):
		self.dlgRestart.OpenDialog()
		self.dlgRestart.SetTop()

	def CloseRestartDialog(self):
		self.dlgRestart.Close()

	def ToggleSystemDialog(self):
		if FALSE == self.dlgSystem.IsShow():
			self.dlgSystem.OpenDialog()
			self.dlgSystem.SetTop()
		else:
			self.dlgSystem.Close()

	def OpenSystemDialog(self):
		self.dlgSystem.OpenDialog()
		self.dlgSystem.SetTop()

	def ToggleMessenger(self):
		if self.wndMessenger.IsShow():
			self.wndMessenger.Hide()
		else:
			self.wndMessenger.SetTop()
			self.wndMessenger.Show()

	def ToggleMiniMap(self):
		if app.IsPressed(app.DIK_LSHIFT) or app.IsPressed(app.DIK_RSHIFT):
			if FALSE == self.wndMiniMap.isShowMiniMap():
				self.wndMiniMap.ShowMiniMap()
				self.wndMiniMap.SetTop()
			else:
				self.wndMiniMap.HideMiniMap()

		else:
			self.wndMiniMap.ToggleAtlasWindow()

	def PressMKey(self):
		if app.IsPressed(app.DIK_LALT) or app.IsPressed(app.DIK_RALT):
			self.ToggleMessenger()

		else:
			self.ToggleMiniMap()

	def SetMapName(self, mapName):
		self.wndMiniMap.SetMapName(mapName)

	def MiniMapScaleUp(self):
		self.wndMiniMap.ScaleUp()

	def MiniMapScaleDown(self):
		self.wndMiniMap.ScaleDown()

	def ToggleCharacterWindow(self,number):
		if FALSE == player.IsObserverMode():
			if FALSE == self.wndCharacter.IsShow():
				self.wndCharacter.Show()
				self.wndCharacter.SetTop()
				self.wndCharacter.OpenEvents(number)
			else:
				if self.wndCharacter.IsShow():
					self.wndCharacter.OverOutItem()
					self.wndCharacter.Hide()
				else:
					self.wndCharacter.Show()
					self.wndCharacter.OpenEvents(number)

	def OpenCharacterWindowWithState(self, state):
		if FALSE == player.IsObserverMode():
			self.wndCharacter.SetState(state)
			self.wndCharacter.Show()
			self.wndCharacter.SetTop()

	def ToggleCharacterWindowStatusPage(self):
		self.ToggleCharacterWindow(0)

	def ToggleInventoryWindow(self):
		if FALSE == player.IsObserverMode():
			if FALSE == self.wndInventory.IsShow():
				self.wndInventory.Show()
				self.wndInventory.SetTop()
			else:
				self.wndInventory.OverOutItem()
				self.wndInventory.Close()

	if app.ENABLE_EXTENDED_BATTLE_PASS:
		def ReciveOpenExtBattlePass(self):
			if False == self.isFirstOpeningExtBattlePass:
				self.isFirstOpeningExtBattlePass = True
				self.wndBattlePassExtended.SetPage("NORMAL")
			if False == self.wndBattlePassExtended.IsShow():
				self.ToggleBattlePassExtended()
			else:
				self.wndBattlePassExtended.SetPage(self.wndBattlePassExtended.GetPage())

		def ToggleBattlePassExtended(self):
			if False == self.isFirstOpeningExtBattlePass:
				net.SendExtBattlePassAction(1)
			if False == self.wndBattlePassExtended.IsShow():
				self.wndBattlePassExtended.Show()
				self.wndBattlePassExtended.SetTop()
			else:
				self.wndBattlePassExtended.Close()
		
		def AddExtendedBattleGeneralInfo(self, BattlePassType, BattlePassName, BattlePassID, battlePassStartTime, battlePassEndTime):
			if self.wndBattlePassExtended:
				self.wndBattlePassExtended.RecvGeneralInfo(BattlePassType, BattlePassName, BattlePassID, battlePassStartTime, battlePassEndTime)
		
		def AddExtendedBattlePassMission(self, battlepassType, battlepassID, missionIndex, missionType, missionInfo1, missionInfo2, missionInfo3):
			if self.wndBattlePassExtended:
				self.wndBattlePassExtended.AddMission(battlepassType, battlepassID, missionIndex, missionType, missionInfo1, missionInfo2, missionInfo3)

		def UpdateExtendedBattlePassMission(self, battlepassType, missionIndex, missionType, newProgress):
			if self.wndBattlePassExtended:
				self.wndBattlePassExtended.UpdateMission(battlepassType, missionIndex, missionType, newProgress)

		def AddExtendedBattlePassMissionReward(self, battlepassType, battlepassID, missionIndex, missionType, itemVnum, itemCount):
			if self.wndBattlePassExtended:
				self.wndBattlePassExtended.AddMissionReward(battlepassType, battlepassID, missionIndex, missionType, itemVnum, itemCount)

		def AddExtendedBattlePassReward(self, battlepassType, battlepassID, itemVnum, itemCount):
			if self.wndBattlePassExtended:
				self.wndBattlePassExtended.AddReward(battlepassType, battlepassID, itemVnum, itemCount)

		def AddExtBattlePassRanklistEntry(self, playername, battlepassType, battlepassID, startTime, endTime):
			if self.wndBattlePassExtended:
				self.wndBattlePassExtended.AddRankingEntry(playername, battlepassType, battlepassID, startTime, endTime)
	
	if app.ENABLE_NEW_PET_SYSTEM:
		def TogglePetMain(self):
			if False == player.IsObserverMode():
				if False == self.wndPetMainWindow.IsShow():
					self.wndPetMainWindow.Show()
					self.wndPetMainWindow.SetTop()
				else:
					self.wndPetMainWindow.Close()
	
		def Pet_RecivePetType(self, type):
			self.wndPetMainWindow.AnswerPetType(type)
			
		def Pet_ReciveAttr(self, type):
			self.wndPetMainWindow.RecivePetRenewAttr(type)
			
		def Pet_SetEvolution(self, evo):
			petname = [localeInfo.PET_INFORMATION_STAGE1, localeInfo.PET_INFORMATION_STAGE2, localeInfo.PET_INFORMATION_STAGE3, localeInfo.PET_INFORMATION_STAGE4]
			self.wndPetMainWindow.SetEvolveName(petname[int(evo)])
		
		def Pet_SetCanEvolution(self, type):
			self.wndPetMainWindow.SetCanEvolution(type)
		
		def Pet_SetName(self, name):
			self.wndPetMainWindow.SetName(name)
		
		def Pet_SetLevel(self, level, evo):
			self.wndPetMainWindow.SetLevel(level, evo)
		
		def Pet_SetDuration(self, dur, durt):
			self.wndPetMainWindow.SetDuration(dur, durt)
		
		def Pet_SetAge(self, ages):
			self.wndPetMainWindow.SetAges(int(ages))

		def Pet_SetBonus(self, hp, att, dif):
			self.wndPetMainWindow.SetHp(hp)
			self.wndPetMainWindow.SetAtt(att)
			self.wndPetMainWindow.SetDef(dif)
			
		def Pet_Setskill(self, slot, idx, lv):
			self.wndPetMainWindow.SetSkill(slot, idx, lv)
				
		def Pet_SetSkillSlotCoolTime(self, slot, time):
			self.wndPetMainWindow.SetSkillSlotCoolTime(slot, time)

		def Pet_SetIcon(self, vnum):
			self.wndPetMainWindow.SetImageSlot(vnum)
			
		def Pet_SetExp(self, level, exp, expi, exptot):
			self.wndPetMainWindow.SetExperience(level, exp, expi, exptot)
			
		def Pet_Unsummon(self):
			self.wndPetMainWindow.SetDefaultInfo()
	
	if app.ENABLE_ASLAN_TELEPORTPANEL:
		def ToggleTeleportPanel(self):
			if self.wndTeleportPanel:
				if False == self.wndTeleportPanel.IsShow():
					self.wndTeleportPanel.Show()
					self.wndTeleportPanel.SetTop()
				else:
					self.wndTeleportPanel.Close()
		
		def ReceiveTeleportQuestCommand(self, command):
			self.wndTeleportPanel.ReceiveQuestCommand(command)

	if app.ENABLE_ASLAN_LOTTERY:
		def ToggleAslanLotteryWindow(self):
			if False == self.wndLottery.IsShow():
				self.wndLottery.Show()
				self.wndLottery.SetTop()
				
		def RefreshLottoBasicInfo(self):
			self.wndLottery.RefreshLottoBasicInfo()
			
		def RefreshLottoTicketInfo(self):
			self.wndLottery.RefreshLottoTicketInfo()

	
	def ToggleExpandedButton(self):
		if FALSE == player.IsObserverMode():
			if FALSE == self.wndExpandedTaskBar.IsShow():
				self.wndExpandedTaskBar.Show()
				self.wndExpandedTaskBar.SetTop()
			else:
				self.wndExpandedTaskBar.Close()

	# 용혼석
	def DragonSoulActivate(self, deck):
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.ActivateDragonSoulByExtern(deck)

	def DragonSoulDeactivate(self):
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			self.wndDragonSoul.DeactivateDragonSoul()
	
	def Highligt_Item(self, inven_type, inven_pos):
		if player.DRAGON_SOUL_INVENTORY == inven_type:
				if app.ENABLE_DRAGON_SOUL_SYSTEM:
						self.wndDragonSoul.HighlightSlot(inven_pos)
		elif player.SLOT_TYPE_INVENTORY == inven_type:
			self.wndInventory.HighlightSlot(inven_pos)
			
	def DragonSoulGiveQuilification(self):
		self.DRAGON_SOUL_IS_QUALIFIED = TRUE
		self.wndExpandedTaskBar.SetToolTipText(uiTaskBar.ExpandedTaskBar.BUTTON_DRAGON_SOUL, uiScriptLocale.TASKBAR_DRAGON_SOUL)
		
	if app.ENABLE_LOTTERY_SYSTEM:
		def ToggleLotteryWindow(self):
			if self.lottery:
				self.lottery.OpenWindow()
				
		def OpenLotteryWindow(self):
			if self.lottery:
				self.lottery.Open()
				
		def CloseLotteryWindow(self):
			if self.lottery:
				self.lottery.Close()

		def InitRollLP(self, count):
			if self.lottery:
				self.lottery.InitRollLP(count)
		
	def ToggleDragonSoulWindow(self):
		if FALSE == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if FALSE == self.wndDragonSoul.IsShow():
					if self.DRAGON_SOUL_IS_QUALIFIED:
						self.wndDragonSoul.Show()
					else:
						try:
							self.wndPopupDialog.SetText(localeInfo.DRAGON_SOUL_UNQUALIFIED)
							self.wndPopupDialog.Open()
						except:
							self.wndPopupDialog = uiCommon.PopupDialog()
							self.wndPopupDialog.SetText(localeInfo.DRAGON_SOUL_UNQUALIFIED)
							self.wndPopupDialog.Open()
				else:
					self.wndDragonSoul.Close()
					
	def ToggleDragonSoulWindowWithNoInfo(self):
		if FALSE == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if FALSE == self.wndDragonSoul.IsShow():
					if self.DRAGON_SOUL_IS_QUALIFIED:
						self.wndDragonSoul.Show()
				else:
					self.wndDragonSoul.Close()
					
	if app.ENABLE_DUNGEON_INFO_SYSTEM:
		def ShowDungeonInfoInterface(self):
			if False == self.wndDungeonInfo.IsShow():
				self.wndDungeonInfo.Open()
			else:
				self.wndDungeonInfo.Close()
				
	def FailDragonSoulRefine(self, reason, inven_type, inven_pos):
		if FALSE == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if TRUE == self.wndDragonSoulRefine.IsShow():
					self.wndDragonSoulRefine.RefineFail(reason, inven_type, inven_pos)
 
	def SucceedDragonSoulRefine(self, inven_type, inven_pos):
		if FALSE == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if TRUE == self.wndDragonSoulRefine.IsShow():
					self.wndDragonSoulRefine.RefineSucceed(inven_type, inven_pos)
 
	def OpenDragonSoulRefineWindow(self):
		if FALSE == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if FALSE == self.wndDragonSoulRefine.IsShow():
					self.wndDragonSoulRefine.Show()
					if None != self.wndDragonSoul:
						if FALSE == self.wndDragonSoul.IsShow():
							self.wndDragonSoul.Show()

	def CloseDragonSoulRefineWindow(self):
		if FALSE == player.IsObserverMode():
			if app.ENABLE_DRAGON_SOUL_SYSTEM:
				if TRUE == self.wndDragonSoulRefine.IsShow():
					self.wndDragonSoulRefine.Close()

	# 용혼석 끝
	
	def ToggleGuildWindow(self):
		if not self.wndGuild.IsShow():
			if self.wndGuild.CanOpen():
				self.wndGuild.Open()
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.GUILD_YOU_DO_NOT_JOIN)
		else:
			self.wndGuild.OverOutItem()
			self.wndGuild.Hide()

	def ToggleChatLogWindow(self):
		if self.wndChatLog.IsShow():
			self.wndChatLog.Hide()
		else:
			self.wndChatLog.Show()

	if app.ENABLE_SWITCHBOT:
		def ToggleSwitchbotWindow(self):
			if self.wndSwitchbot.IsShow():
				self.wndSwitchbot.Close()
			else:
				self.wndSwitchbot.Open()
				
		def RefreshSwitchbotWindow(self):
			if self.wndSwitchbot and self.wndSwitchbot.IsShow():
				self.wndSwitchbot.RefreshSwitchbotWindow()

		def RefreshSwitchbotItem(self, slot):
			if self.wndSwitchbot and self.wndSwitchbot.IsShow():
				self.wndSwitchbot.RefreshSwitchbotItem(slot)

	def CheckGameButton(self):
		if self.wndGameButton:
			self.wndGameButton.CheckGameButton()

	def __OnClickStatusPlusButton(self):
		self.ToggleCharacterWindow(0)

	def __OnClickSkillPlusButton(self):
		self.ToggleCharacterWindow(3)

	def __OnClickQuestButton(self):
		self.ToggleCharacterWindow(6)

	def __OnClickHelpButton(self):
		player.SetPlayTime(1)
		self.CheckGameButton()
		self.OpenHelpWindow()
		
	#def Update(self):
	#	if self.wndCharacter:
	#		self.wndCharacter.Update()

	def __OnClickBuildButton(self):
		self.BUILD_OpenWindow()

	def OpenHelpWindow(self):
		self.wndUICurtain.Show()
		self.wndHelp.Open()

	def CloseHelpWindow(self):
		self.wndUICurtain.Hide()
		self.wndHelp.Close()

	def OpenWebWindow(self, url):
		self.wndWeb.Open(url)

		# 웹페이지를 열면 채팅을 닫는다
		self.wndChat.CloseChat()
		
	if app.ENABLE_MELEY_LAIR_DUNGEON:
		def OpenMeleyRanking(self):
			self.wndMeleyRanking.Open()

		def RankMeleyRanking(self, line, name, members, time):
			self.wndMeleyRanking.AddRank(line, name, members, time)

	# show GIFT
	def ShowGift(self):
		self.wndTaskBar.ShowGift()
		
	if app.ENABLE_CUBE_RENEWAL:
		def BINARY_CUBE_RENEWAL_OPEN(self):
			self.wndCubeRenewal.Show()
	    	
	def CloseWbWindow(self):
		self.wndWeb.Close()
		
	def OpenCardsInfoWindow(self):
		self.wndCardsInfo.Open()
		
	def OpenCardsWindow(self, safemode):
		self.wndCards.Open(safemode)
		
	def UpdateCardsInfo(self, hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, hand_4, hand_4_v, hand_5, hand_5_v, cards_left, points):
		self.wndCards.UpdateCardsInfo(hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, hand_4, hand_4_v, hand_5, hand_5_v, cards_left, points)
		
	def UpdateCardsFieldInfo(self, hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points):
		self.wndCards.UpdateCardsFieldInfo(hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points)
		
	def CardsPutReward(self, hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points):
		self.wndCards.CardsPutReward(hand_1, hand_1_v, hand_2, hand_2_v, hand_3, hand_3_v, points)
		
	def CardsShowIcon(self):
		self.wndCardsIcon.Show()

	if app.ENABLE_SASH_SYSTEM:
		def ActSash(self, iAct, bWindow):
			if iAct == 1:
				if bWindow == True:
					if not self.wndSashCombine.IsOpened():
						self.wndSashCombine.Open()
					
					if not self.wndInventory.IsShow():
						self.wndInventory.Show()
				else:
					if not self.wndSashAbsorption.IsOpened():
						self.wndSashAbsorption.Open()
					
					if not self.wndInventory.IsShow():
						self.wndInventory.Show()
				
				self.wndInventory.RefreshBagSlotWindow()
			elif iAct == 2:
				if bWindow == True:
					if self.wndSashCombine.IsOpened():
						self.wndSashCombine.Close()
				else:
					if self.wndSashAbsorption.IsOpened():
						self.wndSashAbsorption.Close()
				
				self.wndInventory.RefreshBagSlotWindow()
			elif iAct == 3 or iAct == 4:
				if bWindow == True:
					if self.wndSashCombine.IsOpened():
						self.wndSashCombine.Refresh(iAct)
				else:
					if self.wndSashAbsorption.IsOpened():
						self.wndSashAbsorption.Refresh(iAct)
				
				self.wndInventory.RefreshBagSlotWindow()

	if app.ENABLE_CHANGELOOK_SYSTEM:
		def ActChangeLook(self, iAct):
			if iAct == 1:
				if not self.wndChangeLook.IsOpened():
					self.wndChangeLook.Open()

				if not self.wndInventory.IsShow():
					self.wndInventory.Show()

				self.wndInventory.RefreshBagSlotWindow()
			elif iAct == 2:
				if self.wndChangeLook.IsOpened():
					self.wndChangeLook.Close()

				self.wndInventory.RefreshBagSlotWindow()
			elif iAct == 3 or iAct == 4:
				if self.wndChangeLook.IsOpened():
					self.wndChangeLook.Refresh()

				self.wndInventory.RefreshBagSlotWindow()

	def OpenCubeWindow(self):
		self.wndCube.Open()

		if FALSE == self.wndInventory.IsShow():
			self.wndInventory.Show()
			
	def ShowItemFinder(self):
		self.wndItemFinder.Show()

	def AppendInfoFinder(self, index, name_monster, prob, activi, vnum, count, name_item):
		self.wndItemFinder.AppendInfo(index, name_monster, prob, activi, vnum, count, name_item)

	def UpdateCubeInfo(self, gold, itemVnum, count):
		self.wndCube.UpdateInfo(gold, itemVnum, count)

	def CloseCubeWindow(self):
		self.wndCube.Close()

	def FailedCubeWork(self):
		self.wndCube.Refresh()

	def SucceedCubeWork(self, itemVnum, count):
		self.wndCube.Clear()
		
		print "큐브 제작 성공! [%d:%d]" % (itemVnum, count)

		if 0: # 결과 메시지 출력은 생략 한다
			self.wndCubeResult.SetPosition(*self.wndCube.GetGlobalPosition())
			self.wndCubeResult.SetCubeResultItem(itemVnum, count)
			self.wndCubeResult.Open()
			self.wndCubeResult.SetTop()

	def __HideWindows(self):
		hideWindows = self.wndTaskBar,\
						self.wndTaskBar.TaskBarLeft,\
						self.wndTaskBar.TaskBarLeft2,\
						self.wndCharacter,\
						self.wndInventory,\
						self.wndMiniMap,\
						self.wndGuild,\
						self.wndMessenger,\
						self.wndChat,\
						self.wndParty,\
						self.wndGameButton,
		if app.ENABLE_LOTTERY_SYSTEM:
			if self.lottery:
				hideWindows += self.lottery,

		if app.ENABLE_ASLAN_LOTTERY:
			if self.wndLottery:
				hideWindows += self.wndLottery,
                
		# if self.wndEnergyBar:
			# hideWindows += self.wndEnergyBar,
 			
		if self.wndExpandedTaskBar:
			hideWindows += self.wndExpandedTaskBar,
 			
		if app.ENABLE_DRAGON_SOUL_SYSTEM:
			hideWindows += self.wndDragonSoul,\
						self.wndDragonSoulRefine,
		hideWindows += self.wndFarmBlock,

		if app.ENABLE_NEW_PET_SYSTEM:
			if self.wndPetMainWindow:
				hideWindows += self.wndPetMainWindow,
				
		if hasattr(app, "ENABLE_DUNGEON_COOL_TIME"):
			hideWindows += self.wndDungeonCoolTime,
						
		if app.ENABLE_DUNGEON_INFO_SYSTEM:
			if self.wndDungeonInfo:
				hideWindows += self.wndDungeonInfo,

		if app.ENABLE_SWITCHBOT and self.wndSwitchbot:
			hideWindows += self.wndSwitchbot,

		if app.ENABLE_ASLAN_TELEPORTPANEL:
			if self.wndTeleportPanel:
				hideWindows += self.wndTeleportPanel,
				
		if app.ENABLE_RENDER_TARGET_SYSTEM:
			hideWindows += self.wndTargetRender,
	
		if app.ENABLE_EXTENDED_BATTLE_PASS:
			if self.wndBattlePassExtended:
				hideWindows += self.wndBattlePassExtended,

		hideWindows = filter(lambda x:x.IsShow(), hideWindows)
		map(lambda x:x.Hide(), hideWindows)
		import sys

		self.HideAllQuestButton()
		self.HideAllWhisperButton()

		if self.wndChat.IsEditMode():
			self.wndChat.CloseChat()

		return hideWindows

	def __ShowWindows(self, wnds):
		import sys
		map(lambda x:x.Show(), wnds)
		global IsQBHide
		if not IsQBHide:
			self.ShowAllQuestButton()
		else:
			self.HideAllQuestButton()

		self.ShowAllWhisperButton()

	def BINARY_OpenAtlasWindow(self):
		if self.wndMiniMap:
			self.wndMiniMap.ShowAtlas()

	def BINARY_SetObserverMode(self, flag):
		self.wndGameButton.SetObserverMode(flag)

	# ACCESSORY_REFINE_ADD_METIN_STONE
	def BINARY_OpenSelectItemWindow(self):
		self.wndItemSelect.Open()
	# END_OF_ACCESSORY_REFINE_ADD_METIN_STONE

	def OpenNewTestWindow(self):
		if self.wndTalent.IsShow():
			self.wndTalent.Hide()
		else:
			self.wndTalent.Show()
	#####################################################################################
	### Private Shop ###

	def OpenPrivateShopInputNameDialog(self):
		#if player.IsInSafeArea():
		#	chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.CANNOT_OPEN_PRIVATE_SHOP_IN_SAFE_AREA)
		#	return

		inputDialog = uiCommon.InputDialog()
		inputDialog.SetTitle(localeInfo.PRIVATE_SHOP_INPUT_NAME_DIALOG_TITLE)
		inputDialog.SetMaxLength(32)
		inputDialog.SetAcceptEvent(ui.__mem_func__(self.OpenPrivateShopBuilder))
		inputDialog.SetCancelEvent(ui.__mem_func__(self.ClosePrivateShopInputNameDialog))
		inputDialog.Open()
		self.inputDialog = inputDialog

	def ClosePrivateShopInputNameDialog(self):
		self.inputDialog = None
		if self.offlineDecoration.IsShow():
			self.offlineDecoration.Hide()
		return True	
				
	def OpenOfflineShopDecoration(self):
		offlineDecoration = uimyshopdeco.UiShopDeco()
		offlineDecoration.Show()
		self.offlineDecoration = offlineDecoration

	def OpenPrivateShopBuilder(self):

		if not self.inputDialog:
			return TRUE

		if not len(self.inputDialog.GetText()):
			return TRUE

		self.privateShopBuilder.Open(self.inputDialog.GetText())
		self.ClosePrivateShopInputNameDialog()
		return TRUE

	def AppearPrivateShop(self, vid, text):

		board = uiPrivateShopBuilder.PrivateShopAdvertisementBoard()
		board.Open(vid, text)

		self.privateShopAdvertisementBoardDict[vid] = board

	def DisappearPrivateShop(self, vid):

		if not self.privateShopAdvertisementBoardDict.has_key(vid):
			return

		del self.privateShopAdvertisementBoardDict[vid]
		uiPrivateShopBuilder.DeleteADBoard(vid)

	#####################################################################################
	### Equipment ###

	def OpenEquipmentDialog(self, vid):
		import uiequipmentdialog

		if app.ENABLE_PVP_ADVANCED:
			if self.equipmentDialogDict.has_key(vid):
				self.equipmentDialogDict[vid].Destroy()
				self.CloseEquipmentDialog(vid)

		dlg = uiequipmentdialog.EquipmentDialog()
		dlg.SetItemToolTip(self.tooltipItem)
		dlg.SetCloseEvent(ui.__mem_func__(self.CloseEquipmentDialog))
		dlg.Open(vid)

		self.equipmentDialogDict[vid] = dlg

	def SetEquipmentDialogItem(self, vid, slotIndex, vnum, count):
		if not vid in self.equipmentDialogDict:
			return
		self.equipmentDialogDict[vid].SetEquipmentDialogItem(slotIndex, vnum, count)

	def SetEquipmentDialogSocket(self, vid, slotIndex, socketIndex, value):
		if not vid in self.equipmentDialogDict:
			return
		self.equipmentDialogDict[vid].SetEquipmentDialogSocket(slotIndex, socketIndex, value)

	def SetEquipmentDialogAttr(self, vid, slotIndex, attrIndex, type, value):
		if not vid in self.equipmentDialogDict:
			return
		self.equipmentDialogDict[vid].SetEquipmentDialogAttr(slotIndex, attrIndex, type, value)

	def CloseEquipmentDialog(self, vid):
		if not vid in self.equipmentDialogDict:
			return

		if app.ENABLE_PVP_ADVANCED:
			if self.equipmentDialogDict.has_key(vid):
				self.equipmentDialogDict[vid].Destroy()

		del self.equipmentDialogDict[vid]

	#####################################################################################

	#####################################################################################
	### Quest ###	
	def BINARY_ClearQuest(self, index):
		btn = self.__FindQuestButton(index)
		if 0 != btn:
			self.__DestroyQuestButton(btn)		
	
	def RecvQuest(self, index, name):
		# QUEST_LETTER_IMAGE
		self.BINARY_RecvQuest(index, name, "file", localeInfo.GetLetterImageName())
		# END_OF_QUEST_LETTER_IMAGE

	def BINARY_RecvQuest(self, index, name, iconType, iconName):

		btn = self.__FindQuestButton(index)
		if 0 != btn:
			self.__DestroyQuestButton(btn)

		btn = uiWhisper.WhisperButton()

		# QUEST_LETTER_IMAGE
		##!! 20061026.levites.퀘스트_이미지_교체
		import item
		if "item"==iconType:
			item.SelectItem(int(iconName))
			buttonImageFileName=item.GetIconImageFileName()
		else:
			buttonImageFileName=iconName

		if localeInfo.IsEUROPE():
			if "highlight" == iconType:
				btn.SetUpVisual("locale/ymir_ui/highlighted_quest.tga")
				btn.SetOverVisual("locale/ymir_ui/highlighted_quest_r.tga")
				btn.SetDownVisual("locale/ymir_ui/highlighted_quest_r.tga")
			else:
				btn.SetUpVisual(localeInfo.GetLetterCloseImageName())
				btn.SetOverVisual(localeInfo.GetLetterOpenImageName())
				btn.SetDownVisual(localeInfo.GetLetterOpenImageName())				
		else:
			btn.SetUpVisual(buttonImageFileName)
			btn.SetOverVisual(buttonImageFileName)
			btn.SetDownVisual(buttonImageFileName)
			btn.Flash()
		# END_OF_QUEST_LETTER_IMAGE

		if localeInfo.IsARABIC():
			btn.SetToolTipText(name, 0, 35)
			btn.ToolTipText.SetHorizontalAlignCenter()
		else:
			btn.SetToolTipText(name, -20, 35)
			btn.ToolTipText.SetHorizontalAlignLeft()
			
		btn.SetEvent(ui.__mem_func__(self.__StartQuest), btn)
		btn.Show()

		btn.index = index
		btn.name = name

		self.questButtonList.insert(0, btn)
		self.__ArrangeQuestButton()

		#chat.AppendChat(chat.CHAT_TYPE_NOTICE, localeInfo.QUEST_APPEND)

	def __ArrangeQuestButton(self):

		screenWidth = wndMgr.GetScreenWidth()
		screenHeight = wndMgr.GetScreenHeight()

		##!! 20061026.levites.퀘스트_위치_보정
		if self.wndParty.IsShow():
			xPos = 100 + 30
		else:
			xPos = 20

		if localeInfo.IsARABIC():
			xPos = xPos + 15

		yPos = 170 * screenHeight / 600
		yCount = (screenHeight - 330) / 63

		count = 0
		for btn in self.questButtonList:

			btn.SetPosition(xPos + (int(count/yCount) * 100), yPos + (count%yCount * 63))
			count += 1
			global IsQBHide
			if IsQBHide:
				btn.Hide()
			else:
				btn.Show()

	def __StartQuest(self, btn):
		event.QuestButtonClick(btn.index)
		self.__DestroyQuestButton(btn)

	def __FindQuestButton(self, index):
		for btn in self.questButtonList:
			if btn.index == index:
				return btn

		return 0

	def __DestroyQuestButton(self, btn):
		btn.SetEvent(0)
		self.questButtonList.remove(btn)
		self.__ArrangeQuestButton()

	def HideAllQuestButton(self):
		for btn in self.questButtonList:
			btn.Hide()

	def ShowAllQuestButton(self):
		for btn in self.questButtonList:
			btn.Show()
	#####################################################################################

	#####################################################################################
	### Whisper ###

	def __InitWhisper(self):
		chat.InitWhisper(self)

	## 채팅창의 "메시지 보내기"를 눌렀을때 이름 없는 대화창을 여는 함수
	## 이름이 없기 때문에 기존의 WhisperDialogDict 와 별도로 관리된다.
	def OpenWhisperDialogWithoutTarget(self):
		if not self.dlgWhisperWithoutTarget:
			dlgWhisper = uiWhisper.WhisperDialog(self.MinimizeWhisperDialog, self.CloseWhisperDialog)
			dlgWhisper.BindInterface(self)
			dlgWhisper.LoadDialog()
			dlgWhisper.OpenWithoutTarget(self.RegisterTemporaryWhisperDialog)
			dlgWhisper.SetPosition(self.windowOpenPosition*30,self.windowOpenPosition*30)
			dlgWhisper.Show()
			self.dlgWhisperWithoutTarget = dlgWhisper

			self.windowOpenPosition = (self.windowOpenPosition+1) % 5

		else:
			self.dlgWhisperWithoutTarget.SetTop()
			self.dlgWhisperWithoutTarget.OpenWithoutTarget(self.RegisterTemporaryWhisperDialog)

	## 이름 없는 대화창에서 이름을 결정했을때 WhisperDialogDict에 창을 넣어주는 함수
	def RegisterTemporaryWhisperDialog(self, name):
		if not self.dlgWhisperWithoutTarget:
			return

		btn = self.__FindWhisperButton(name)
		if 0 != btn:
			self.__DestroyWhisperButton(btn)

		elif self.whisperDialogDict.has_key(name):
			oldDialog = self.whisperDialogDict[name]
			oldDialog.Destroy()
			del self.whisperDialogDict[name]

		self.whisperDialogDict[name] = self.dlgWhisperWithoutTarget
		self.dlgWhisperWithoutTarget.OpenWithTarget(name)
		self.dlgWhisperWithoutTarget = None
		self.__CheckGameMaster(name)

	## 캐릭터 메뉴의 1:1 대화 하기를 눌렀을때 이름을 가지고 바로 창을 여는 함수
	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def OpenWhisperDialog(self, name, job = -1, level = -1, empire = -1, guild = "", language = "", status = "", location = "", year = "", month = "", day = ""):
			if not self.whisperDialogDict.has_key(name):
				dlg = self.__MakeWhisperDialog(name)
				dlg.OpenWithTarget(name)
				if self.GetExistProfile(job, level, empire, guild, language, status, location, year, month, day):
					dlg.RecvWhisperProfile(job, level, empire, guild, language, status, location, year, month, day)
				dlg.chatLine.SetFocus()
				dlg.Show()

				self.__CheckGameMaster(name)
				btn = self.__FindWhisperButton(name)
				if 0 != btn:
					dlg.RecvWhisperProfile(btn.job, btn.level, btn.empire, btn.guild, btn.language, btn.status, btn.location, btn.year, btn.month, btn.day)
					self.__DestroyWhisperButton(btn)
	else:
		def OpenWhisperDialog(self, name):
			if not self.whisperDialogDict.has_key(name):
				dlg = self.__MakeWhisperDialog(name)
				dlg.OpenWithTarget(name)
				dlg.chatLine.SetFocus()
				dlg.Show()

				self.__CheckGameMaster(name)
				btn = self.__FindWhisperButton(name)
				if 0 != btn:
					self.__DestroyWhisperButton(btn)	
					

	## 다른 캐릭터로부터 메세지를 받았을때 일단 버튼만 띄워 두는 함수
	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def RecvWhisper(self, name, job = -1, level = -1, empire = -1, guild = "", language = "", status = "", location = "", year = "", month = "", day = ""):
			if name:
				constInfo.TARGET_LANGS[name] = language
			if not self.whisperDialogDict.has_key(name):
				btn = self.__FindWhisperButton(name)

				if 0 == btn:
					btn = self.__MakeWhisperButton(name, job, level, empire, guild, language, status, location, year, month, day)
					btn.Flash()
					app.FlashApplication()
					chat.AppendChat(chat.CHAT_TYPE_NOTICE, localeInfo.RECEIVE_MESSAGE % (name))
				else:
					btn.job = job
					btn.level = level
					btn.empire = empire
					btn.guild = guild
					btn.language = language
					btn.status = status
					btn.location = location
					btn.year = year
					btn.month = month
					btn.day = day				
					btn.Flash()
					app.FlashApplication()

			elif self.IsGameMasterName(name):
				dlg = self.whisperDialogDict[name]
				dlg.SetGameMasterLook()
				if self.GetExistProfile(job, level, empire, guild, language, status, location, year, month, day):
					dlg.RecvWhisperProfile(job, level, empire, guild, language, status, location, year, month, day)
	else:
		def RecvWhisper(self, name):
			if not self.whisperDialogDict.has_key(name):
				btn = self.__FindWhisperButton(name)
				if 0 == btn:
					btn = self.__MakeWhisperButton(name)
					btn.Flash()
					app.FlashApplication()
					chat.AppendChat(chat.CHAT_TYPE_NOTICE, localeInfo.RECEIVE_MESSAGE % (name))
				else:
					btn.Flash()
					app.FlashApplication()
			elif self.IsGameMasterName(name):
				dlg = self.whisperDialogDict[name]
				dlg.SetGameMasterLook()
				

	def MakeWhisperButton(self, name):
		self.__MakeWhisperButton(name)
		
	def OpenFarmBlock(self):
		if not self.wndFarmBlock.IsShow():
			self.wndFarmBlock.Open()
		else:
			self.wndFarmBlock.Close()
		
	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def GetExistProfile(self, job, level, empire, guild, language, status, location, year, month, day):
			if job == -1 or level == -1 or empire == -1 or language == "":
				return False
			return True

		def RecvWhisperProfile(self, name, job, level, empire, guild, language, status, location, year, month, day):
			if self.whisperDialogDict.has_key(name):
				self.whisperDialogDict[name].RecvWhisperProfile(job, level, empire, guild, language, status, location, year, month, day)
			else:
				btn = self.__FindWhisperButton(name)
				if btn != 0:
					btn.job = job
					btn.level = level
					btn.empire = empire
					btn.guild = guild
					btn.language = language
					btn.status = status
					btn.location = location
					btn.year = year
					btn.month = month
					btn.day = day
		
	if app.ENABLE_LANG_AND_EMPIRE_FLAG:
		def SetInterfaceFlag(self, name, language, empire):
			if self.whisperDialogDict.has_key(name):
				self.whisperDialogDict[name].SetFlag(language, empire)
			else:
				btn = self.__FindWhisperButton(name)
				if btn != 0:
					btn.languageID = language
					btn.empireID = empire	

	## 버튼을 눌렀을때 창을 여는 함수
	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def ShowWhisperDialog(self, btn):
			try:
				self.__MakeWhisperDialog(btn.name)
				dlgWhisper = self.whisperDialogDict[btn.name]
				dlgWhisper.OpenWithTarget(btn.name)

				if self.GetExistProfile(btn.job, btn.level, btn.empire, btn.guild, btn.language, btn.status, btn.location, btn.year, btn.month, btn.day):
					dlgWhisper.RecvWhisperProfile(btn.job, btn.level, btn.empire, btn.guild, btn.language, btn.status, btn.location, btn.year, btn.month, btn.day)
					
				dlgWhisper.Show()
				self.__CheckGameMaster(btn.name)
			except:
				import dbg
				dbg.TraceError("interface.ShowWhisperDialog - Failed to find key")
			self.__DestroyWhisperButton(btn)
	else:
		def ShowWhisperDialog(self, btn):
			try:
				self.__MakeWhisperDialog(btn.name)
				dlgWhisper = self.whisperDialogDict[btn.name]
				dlgWhisper.OpenWithTarget(btn.name)
				dlgWhisper.Show()
				self.__CheckGameMaster(btn.name)
			except:
				import dbg
				dbg.TraceError("interface.ShowWhisperDialog - Failed to find key")
			self.__DestroyWhisperButton(btn)

	## WhisperDialog 창에서 최소화 명령을 수행했을때 호출되는 함수
	## 창을 최소화 합니다.
	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def MinimizeWhisperDialog(self, name, job, level, empire, guild, language, status, location, year, month, day):
			if 0 != name:
				self.__MakeWhisperButton(name, job, level, empire, guild, language, status, location, year, month, day)
			self.CloseWhisperDialog(name)
	else:
		def MinimizeWhisperDialog(self, name):
			if 0 != name:
				self.__MakeWhisperButton(name)
			self.CloseWhisperDialog(name)

	## WhisperDialog 창에서 닫기 명령을 수행했을때 호출되는 함수
	## 창을 지웁니다.
	if app.ENABLE_LANG_AND_EMPIRE_FLAG:
		def CloseWhisperDialog(self, name):
			#if not isinstance(name, str):
			#	chat.AppendChat(chat.CHAT_TYPE_INFO, "Acesta nu este un nume")
			#	return
			if 0 == name:
				if self.dlgWhisperWithoutTarget:
					self.dlgWhisperWithoutTarget.Destroy()
					self.dlgWhisperWithoutTarget = None
				return
			try:
				if self.whisperDialogDict.has_key(name):
					dlgWhisper = self.whisperDialogDict[name]
					dlgWhisper.Destroy()
					del self.whisperDialogDict[name]
			except:
				import dbg
				dbg.TraceError("interface.CloseWhisperDialog - Failed to find key#33333")
	else:
		def CloseWhisperDialog(self, name):
			if 0 == name:
				if self.dlgWhisperWithoutTarget:
					self.dlgWhisperWithoutTarget.Destroy()
					self.dlgWhisperWithoutTarget = None
				return
			try:
				dlgWhisper = self.whisperDialogDict[name]
				dlgWhisper.Destroy()
				del self.whisperDialogDict[name]
			except:
				import dbg
				dbg.TraceError("interface.CloseWhisperDialog - Failed to find key")	

	## 버튼의 개수가 바뀌었을때 버튼을 재정렬 하는 함수
	def __ArrangeWhisperButton(self):

		screenWidth = wndMgr.GetScreenWidth()
		screenHeight = wndMgr.GetScreenHeight()

		xPos = screenWidth - 70
		yPos = 170 * screenHeight / 600
		yCount = (screenHeight - 330) / 63
		#yCount = (screenHeight - 285) / 63

		count = 0
		for button in self.whisperButtonList:

			button.SetPosition(xPos + (int(count/yCount) * -50), yPos + (count%yCount * 63))
			count += 1

	## 이름으로 Whisper 버튼을 찾아 리턴해 주는 함수
	## 버튼은 딕셔너리로 하지 않는 것은 정렬 되어 버려 순서가 유지 되지 않으며
	## 이로 인해 ToolTip들이 다른 버튼들에 의해 가려지기 때문이다.
	def __FindWhisperButton(self, name):
		for button in self.whisperButtonList:
			if button.name == name:
				return button

		return 0

	## 창을 만듭니다.
	def __MakeWhisperDialog(self, name):
		dlgWhisper = uiWhisper.WhisperDialog(self.MinimizeWhisperDialog, self.CloseWhisperDialog)
		dlgWhisper.BindInterface(self)
		dlgWhisper.LoadDialog()
		dlgWhisper.SetPosition(self.windowOpenPosition*30,self.windowOpenPosition*30)
		self.whisperDialogDict[name] = dlgWhisper

		self.windowOpenPosition = (self.windowOpenPosition+1) % 5

		return dlgWhisper

	## 버튼을 만듭니다.
	if app.ENABLE_RENEW_MESSENGER_WHISPER:
		def __MakeWhisperButton(self, name, job = -1, level = -1, empire = -1, guild = "", language = "", status = "", location = "", year = "", month = "", day = ""):
			whisperButton = uiWhisper.WhisperButton()
			whisperButton.SetUpVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
			whisperButton.SetOverVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
			whisperButton.SetDownVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
			if self.IsGameMasterName(name):
				whisperButton.SetToolTipTextWithColor(name, 0xffffa200)
			else:
				whisperButton.SetToolTipText(name)
			whisperButton.ToolTipText.SetHorizontalAlignCenter()
			whisperButton.SetEvent(ui.__mem_func__(self.ShowWhisperDialog), whisperButton)
			whisperButton.Show()
			
			whisperButton.name = name
			whisperButton.job = job
			whisperButton.level = level
			whisperButton.empire = empire
			whisperButton.guild = guild
			whisperButton.language = language
			whisperButton.status = status
			whisperButton.location = location
			whisperButton.year = year
			whisperButton.month = month
			whisperButton.day = day	
			
			self.whisperButtonList.insert(0, whisperButton)
			self.__ArrangeWhisperButton()
			return whisperButton
	else:
		def __MakeWhisperButton(self, name):
			whisperButton = uiWhisper.WhisperButton()
			whisperButton.SetUpVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
			whisperButton.SetOverVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
			whisperButton.SetDownVisual("d:/ymir work/ui/game/windows/btn_mail_up.sub")
			if self.IsGameMasterName(name):
				whisperButton.SetToolTipTextWithColor(name, 0xffffa200)
			else:
				whisperButton.SetToolTipText(name)
			whisperButton.ToolTipText.SetHorizontalAlignCenter()
			whisperButton.SetEvent(ui.__mem_func__(self.ShowWhisperDialog), whisperButton)
			whisperButton.Show()
			whisperButton.name = name
			self.whisperButtonList.insert(0, whisperButton)
			self.__ArrangeWhisperButton()
			return whisperButton

	def __DestroyWhisperButton(self, button):
		button.SetEvent(0)
		self.whisperButtonList.remove(button)
		self.__ArrangeWhisperButton()

	def HideAllWhisperButton(self):
		for btn in self.whisperButtonList:
			btn.Hide()

	def ShowAllWhisperButton(self):
		for btn in self.whisperButtonList:
			btn.Show()

	def __CheckGameMaster(self, name):
		if not self.listGMName.has_key(name):
			return
		if self.whisperDialogDict.has_key(name):
			dlg = self.whisperDialogDict[name]
			dlg.SetGameMasterLook()

	def RegisterGameMasterName(self, name):
		if self.listGMName.has_key(name):
			return
		self.listGMName[name] = "GM"

	def IsGameMasterName(self, name):
		if self.listGMName.has_key(name):
			return TRUE
		else:
			return FALSE

	#####################################################################################

	#####################################################################################
	### Guild Building ###

	def BUILD_OpenWindow(self):
		self.wndGuildBuilding = uiGuild.BuildGuildBuildingWindow()
		self.wndGuildBuilding.Open()
		self.wndGuildBuilding.wnds = self.__HideWindows()
		self.wndGuildBuilding.SetCloseEvent(ui.__mem_func__(self.BUILD_CloseWindow))

	def BUILD_CloseWindow(self):
		self.__ShowWindows(self.wndGuildBuilding.wnds)
		self.wndGuildBuilding = None

	def BUILD_OnUpdate(self):
		if not self.wndGuildBuilding:
			return

		if self.wndGuildBuilding.IsPositioningMode():
			import background
			x, y, z = background.GetPickingPoint()
			self.wndGuildBuilding.SetBuildingPosition(x, y, z)

	def BUILD_OnMouseLeftButtonDown(self):
		if not self.wndGuildBuilding:
			return

		# GUILD_BUILDING
		if self.wndGuildBuilding.IsPositioningMode():
			self.wndGuildBuilding.SettleCurrentPosition()
			return TRUE
		elif self.wndGuildBuilding.IsPreviewMode():
			pass
		else:
			return TRUE
		# END_OF_GUILD_BUILDING
		return FALSE

	def BUILD_OnMouseLeftButtonUp(self):
		if not self.wndGuildBuilding:
			return

		if not self.wndGuildBuilding.IsPreviewMode():
			return TRUE

		return FALSE

	def BULID_EnterGuildArea(self, areaID):
		# GUILD_BUILDING
		mainCharacterName = player.GetMainCharacterName()
		masterName = guild.GetGuildMasterName()

		if mainCharacterName != masterName:
			return

		if areaID != player.GetGuildID():
			return
		# END_OF_GUILD_BUILDING

		self.wndGameButton.ShowBuildButton()

	def BULID_ExitGuildArea(self, areaID):
		self.wndGameButton.HideBuildButton()

	#####################################################################################

	def IsEditLineFocus(self):
		if self.ChatWindow.chatLine.IsFocus():
			return 1

		if self.ChatWindow.chatToLine.IsFocus():
			return 1

		return 0

	if app.ENABLE_SHOP_SEARCH_SYSTEM:
		def OpenPrivateShopSearch(self, type):
			if not self.wndSwitchbot.IsShow():
				if not player.IsOpenPrivateShop():
					if self.wndPrivateShopSearch:
						self.wndPrivateShopSearch.Open(type)
				else:
					chat.AppendChat(chat.CHAT_TYPE_INFO,"Erst Laden schlie?n")
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO,"Erst Switchbot schlie?n")
				

		def ClosePrivateShopSearch(self):
			if self.wndPrivateShopSearch:
				self.wndPrivateShopSearch.Close()
		def RefreshShopSearch(self):
			self.wndPrivateShopSearch.RefreshMe()
			self.wndPrivateShopSearch.RefreshList()

	def EmptyFunction(self):
		pass

	def GetInventoryPageIndex(self):
		if self.wndInventory:
			return self.wndInventory.GetInventoryPageIndex()
		else:
			return -1

	if app.WJ_ENABLE_TRADABLE_ICON:
		def SetOnTopWindow(self, onTopWnd):
			self.onTopWindow = onTopWnd

		def GetOnTopWindow(self):
			return self.onTopWindow

		def RefreshMarkInventoryBag(self):
			self.wndInventory.RefreshMarkSlots()

	if hasattr(app, "ENABLE_DUNGEON_COOL_TIME"):
		def OpenDungeonCoolTimeWindow(self, floor, cooltime):
			self.wndDungeonCoolTime.Open()
			self.wndDungeonCoolTime.SetFloor(floor)
			self.wndDungeonCoolTime.SetCoolTime(cooltime)

		def SetShadowPotionEndTime(self, endTime):
			self.wndDungeonCoolTime.SetShadowPotionEndTime(endTime)

		def ClearDungeonCoolTime(self):
			self.wndDungeonCoolTime.Clear()

		def SetGameInstance(self, gameInstance):
			self.gameInstance = gameInstance

		def GetGameInstance(self):
			return self.gameInstance

	if app.ENABLE_BIYOLOG:
		def MakeBioWindow(self):
			self.wndBio = uiBiyolog.BiologWindow()
			self.wndBio.LoadEmpty()
			self.wndBio.Hide()
			
	if app.ENABLE_HIDE_COSTUME_SYSTEM:
		def RefreshVisibleCostume(self):
			self.wndInventory.RefreshVisibleCostume()

	if app.ENABLE_WHEEL_OF_FORTUNE:
		def MakeWheelofFortune(self):
			if self.wndWheelofFortune == None:
				self.wndWheelofFortune = uiWheelofFortune.WheelofFortune()
		def OpenWheelofFortune(self):
			self.MakeWheelofFortune()
			if self.wndWheelofFortune.IsShow():
				self.wndWheelofFortune.Close()
			else:
				self.wndWheelofFortune.Open()
		def SetItemData(self, cmd):
			self.MakeWheelofFortune()
			self.wndWheelofFortune.SetItemData(str(cmd))
		def OnSetWhell(self, giftIndex):
			self.MakeWheelofFortune()
			self.wndWheelofFortune.OnSetWhell(int(giftIndex))
		def GetGiftData(self, itemVnum, itemCount):
			self.MakeWheelofFortune()
			self.wndWheelofFortune.GetGiftData(int(itemVnum), int(itemCount))

if hasattr(app, "ENABLE_DUNGEON_COOL_TIME"):
	_instance = None

	def GetInstance():
		global _instance
		return _instance

	def SetInstance(instance):
		global _instance
		
		if _instance:
			del _instance
		
		_instance = instance
	
	if app.INGAME_WIKI:
		def ToggleWikiNew(self):
			import net
			net.ToggleWikiWindow()