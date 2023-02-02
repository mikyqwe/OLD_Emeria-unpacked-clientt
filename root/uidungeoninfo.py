import app
import ui
import uiToolTip
import grp
import item
import player
import constInfo
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import uiScriptLocale
import uiCommon
import net
import renderTarget
import nonplayer
import constInfo

class DungeonInfo(ui.ScriptWindow):
	TOOLTIP_NORMAL_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
	TOOLTIP_SPECIAL_COLOR = grp.GenerateColor(1.0, 0.7843, 0.0, 1.0)
	MIN_SCROLLBAR_LIST = 10

	AFFECT_DICT = {
		item.APPLY_MAX_HP : localeInfo.TOOLTIP_MAX_HP,
		item.APPLY_MAX_SP : localeInfo.TOOLTIP_MAX_SP,
		item.APPLY_CON : localeInfo.TOOLTIP_CON,
		item.APPLY_INT : localeInfo.TOOLTIP_INT,
		item.APPLY_STR : localeInfo.TOOLTIP_STR,
		item.APPLY_DEX : localeInfo.TOOLTIP_DEX,
		item.APPLY_ATT_SPEED : localeInfo.TOOLTIP_ATT_SPEED,
		item.APPLY_MOV_SPEED : localeInfo.TOOLTIP_MOV_SPEED,
		item.APPLY_CAST_SPEED : localeInfo.TOOLTIP_CAST_SPEED,
		item.APPLY_HP_REGEN : localeInfo.TOOLTIP_HP_REGEN,
		item.APPLY_SP_REGEN : localeInfo.TOOLTIP_SP_REGEN,
		item.APPLY_POISON_PCT : localeInfo.TOOLTIP_APPLY_POISON_PCT,
		item.APPLY_STUN_PCT : localeInfo.TOOLTIP_APPLY_STUN_PCT,
		item.APPLY_SLOW_PCT : localeInfo.TOOLTIP_APPLY_SLOW_PCT,
		item.APPLY_CRITICAL_PCT : localeInfo.TOOLTIP_APPLY_CRITICAL_PCT,
		item.APPLY_PENETRATE_PCT : localeInfo.TOOLTIP_APPLY_PENETRATE_PCT,

		item.APPLY_ATTBONUS_WARRIOR : localeInfo.TOOLTIP_APPLY_ATTBONUS_WARRIOR,
		item.APPLY_ATTBONUS_ASSASSIN : localeInfo.TOOLTIP_APPLY_ATTBONUS_ASSASSIN,
		item.APPLY_ATTBONUS_SURA : localeInfo.TOOLTIP_APPLY_ATTBONUS_SURA,
		item.APPLY_ATTBONUS_SHAMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_SHAMAN,
		item.APPLY_ATTBONUS_MONSTER : localeInfo.TOOLTIP_APPLY_ATTBONUS_MONSTER,

		item.APPLY_ATTBONUS_HUMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_HUMAN,
		item.APPLY_ATTBONUS_ANIMAL : localeInfo.TOOLTIP_APPLY_ATTBONUS_ANIMAL,
		item.APPLY_ATTBONUS_ORC : localeInfo.TOOLTIP_APPLY_ATTBONUS_ORC,
		item.APPLY_ATTBONUS_MILGYO : localeInfo.TOOLTIP_APPLY_ATTBONUS_MILGYO,
		item.APPLY_ATTBONUS_UNDEAD : localeInfo.TOOLTIP_APPLY_ATTBONUS_UNDEAD,
		item.APPLY_ATTBONUS_DEVIL : localeInfo.TOOLTIP_APPLY_ATTBONUS_DEVIL,
		item.APPLY_STEAL_HP : localeInfo.TOOLTIP_APPLY_STEAL_HP,
		item.APPLY_STEAL_SP : localeInfo.TOOLTIP_APPLY_STEAL_SP,
		item.APPLY_MANA_BURN_PCT : localeInfo.TOOLTIP_APPLY_MANA_BURN_PCT,
		item.APPLY_DAMAGE_SP_RECOVER : localeInfo.TOOLTIP_APPLY_DAMAGE_SP_RECOVER,
		item.APPLY_BLOCK : localeInfo.TOOLTIP_APPLY_BLOCK,
		item.APPLY_DODGE : localeInfo.TOOLTIP_APPLY_DODGE,
		item.APPLY_RESIST_SWORD : localeInfo.TOOLTIP_APPLY_RESIST_SWORD,
		item.APPLY_RESIST_TWOHAND : localeInfo.TOOLTIP_APPLY_RESIST_TWOHAND,
		item.APPLY_RESIST_DAGGER : localeInfo.TOOLTIP_APPLY_RESIST_DAGGER,
		item.APPLY_RESIST_BELL : localeInfo.TOOLTIP_APPLY_RESIST_BELL,
		item.APPLY_RESIST_FAN : localeInfo.TOOLTIP_APPLY_RESIST_FAN,
		item.APPLY_RESIST_BOW : localeInfo.TOOLTIP_RESIST_BOW,
		item.APPLY_RESIST_FIRE : localeInfo.TOOLTIP_RESIST_FIRE,
		item.APPLY_RESIST_ELEC : localeInfo.TOOLTIP_RESIST_ELEC,
		item.APPLY_RESIST_MAGIC : localeInfo.TOOLTIP_RESIST_MAGIC,
		item.APPLY_RESIST_WIND : localeInfo.TOOLTIP_APPLY_RESIST_WIND,
		item.APPLY_REFLECT_MELEE : localeInfo.TOOLTIP_APPLY_REFLECT_MELEE,
		item.APPLY_REFLECT_CURSE : localeInfo.TOOLTIP_APPLY_REFLECT_CURSE,
		item.APPLY_POISON_REDUCE : localeInfo.TOOLTIP_APPLY_POISON_REDUCE,
		item.APPLY_KILL_SP_RECOVER : localeInfo.TOOLTIP_APPLY_KILL_SP_RECOVER,
		item.APPLY_EXP_DOUBLE_BONUS : localeInfo.TOOLTIP_APPLY_EXP_DOUBLE_BONUS,
		item.APPLY_GOLD_DOUBLE_BONUS : localeInfo.TOOLTIP_APPLY_GOLD_DOUBLE_BONUS,
		item.APPLY_ITEM_DROP_BONUS : localeInfo.TOOLTIP_APPLY_ITEM_DROP_BONUS,
		item.APPLY_POTION_BONUS : localeInfo.TOOLTIP_APPLY_POTION_BONUS,
		item.APPLY_KILL_HP_RECOVER : localeInfo.TOOLTIP_APPLY_KILL_HP_RECOVER,
		item.APPLY_IMMUNE_STUN : localeInfo.TOOLTIP_APPLY_IMMUNE_STUN,
		item.APPLY_IMMUNE_SLOW : localeInfo.TOOLTIP_APPLY_IMMUNE_SLOW,
		item.APPLY_IMMUNE_FALL : localeInfo.TOOLTIP_APPLY_IMMUNE_FALL,
		item.APPLY_BOW_DISTANCE : localeInfo.TOOLTIP_BOW_DISTANCE,
		item.APPLY_DEF_GRADE_BONUS : localeInfo.TOOLTIP_DEF_GRADE,
		item.APPLY_ATT_GRADE_BONUS : localeInfo.TOOLTIP_ATT_GRADE,
		item.APPLY_MAGIC_ATT_GRADE : localeInfo.TOOLTIP_MAGIC_ATT_GRADE,
		item.APPLY_MAGIC_DEF_GRADE : localeInfo.TOOLTIP_MAGIC_DEF_GRADE,
		item.APPLY_MAX_STAMINA : localeInfo.TOOLTIP_MAX_STAMINA,
		item.APPLY_MALL_ATTBONUS : localeInfo.TOOLTIP_MALL_ATTBONUS,
		item.APPLY_MALL_DEFBONUS : localeInfo.TOOLTIP_MALL_DEFBONUS,
		item.APPLY_MALL_EXPBONUS : localeInfo.TOOLTIP_MALL_EXPBONUS,
		item.APPLY_MALL_ITEMBONUS : localeInfo.TOOLTIP_MALL_ITEMBONUS,
		item.APPLY_MALL_GOLDBONUS : localeInfo.TOOLTIP_MALL_GOLDBONUS,
		item.APPLY_SKILL_DAMAGE_BONUS : localeInfo.TOOLTIP_SKILL_DAMAGE_BONUS,
		item.APPLY_NORMAL_HIT_DAMAGE_BONUS : localeInfo.TOOLTIP_NORMAL_HIT_DAMAGE_BONUS,
		item.APPLY_SKILL_DEFEND_BONUS : localeInfo.TOOLTIP_SKILL_DEFEND_BONUS,
		item.APPLY_NORMAL_HIT_DEFEND_BONUS : localeInfo.TOOLTIP_NORMAL_HIT_DEFEND_BONUS,
		item.APPLY_PC_BANG_EXP_BONUS : localeInfo.TOOLTIP_MALL_EXPBONUS_P_STATIC,
		item.APPLY_PC_BANG_DROP_BONUS : localeInfo.TOOLTIP_MALL_ITEMBONUS_P_STATIC,
		item.APPLY_RESIST_WARRIOR : localeInfo.TOOLTIP_APPLY_RESIST_WARRIOR,
		item.APPLY_RESIST_ASSASSIN : localeInfo.TOOLTIP_APPLY_RESIST_ASSASSIN,
		item.APPLY_RESIST_SURA : localeInfo.TOOLTIP_APPLY_RESIST_SURA,
		item.APPLY_RESIST_SHAMAN : localeInfo.TOOLTIP_APPLY_RESIST_SHAMAN,
		#item.APPLY_RESIST_WOLFMAN : localeInfo.TOOLTIP_APPLY_RESIST_WOLFMAN, # app.ENABLE_WOLFMAN_CHARACTER
		item.APPLY_MAX_HP_PCT : localeInfo.TOOLTIP_APPLY_MAX_HP_PCT,
		item.APPLY_MAX_SP_PCT : localeInfo.TOOLTIP_APPLY_MAX_SP_PCT,
		item.APPLY_ENERGY : localeInfo.TOOLTIP_ENERGY,
		item.APPLY_COSTUME_ATTR_BONUS : localeInfo.TOOLTIP_COSTUME_ATTR_BONUS,
		
		item.APPLY_MAGIC_ATTBONUS_PER : localeInfo.TOOLTIP_MAGIC_ATTBONUS_PER,
		item.APPLY_MELEE_MAGIC_ATTBONUS_PER : localeInfo.TOOLTIP_MELEE_MAGIC_ATTBONUS_PER,
		item.APPLY_RESIST_ICE : localeInfo.TOOLTIP_RESIST_ICE,
		item.APPLY_RESIST_EARTH : localeInfo.TOOLTIP_RESIST_EARTH,
		item.APPLY_RESIST_DARK : localeInfo.TOOLTIP_RESIST_DARK,
		item.APPLY_ANTI_CRITICAL_PCT : localeInfo.TOOLTIP_ANTI_CRITICAL_PCT,
		item.APPLY_ANTI_PENETRATE_PCT : localeInfo.TOOLTIP_ANTI_PENETRATE_PCT,
		#item.APPLY_ANTI_RESIST_MAGIC : localeInfo.APPLY_ANTI_RESIST_MAGIC,
		#97 : localeInfo.TOOLTIP_ITEM_REDUCE_MAGIC,
	}
	
	DUNGEON_TYPE = {
		0 : localeInfo.DUNGEON_INFO_TYPE0,
		1 : localeInfo.DUNGEON_INFO_TYPE1,
		2 : localeInfo.DUNGEON_INFO_TYPE2
	}

	DUNGEON_ORGANIZATION = {
		0 : localeInfo.DUNGEON_INFO_ORGANIZATION0,
		1 : localeInfo.DUNGEON_INFO_ORGANIZATION1,
		2 : localeInfo.DUNGEON_INFO_ORGANIZATION2
	}

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.dungeonIndex = 0
		self.dungeonButton = {}
		self.dungeonImage = {}
		self.dungeonImageIcon = {}
		self.dungeonName = {}
		self.questionDialog = None
		self.dungeonRankingIndex = None
		self.renderModelPreview = None
		self.isAlreadyLoaded = False

	def __del__(self):
		ui.ScriptWindow.__del__(self)

		self.dungeonIndex = 0
		self.dungeonButton = {}
		self.dungeonImage = {}
		self.dungeonImageIcon = {}
		self.dungeonName = {}
		self.questionDialog = None
		self.dungeonRankingIndex = None
		self.renderModelPreview = None
		self.isAlreadyLoaded = False

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/dungeoninfowindow.py")
		except:
			import exception
			exception.Abort("DungeonInfo.LoadDialog.LoadScript")

		try:
			self.dungeonBoard = self.GetChild("DungeonBoard")
			self.dungeonBoardTitleBar = self.GetChild("DungeonBoardTitleBar")

			self.dungeonButtonBoard = self.GetChild("DungeonButtonBoard")
			self.dungeonButtonThinBoard = self.GetChild("DungeonButtonThinBoard")

			self.dungeonInfoItem = self.GetChild("DungeonInfoItem")
			self.dungeonInfoItemSlot = self.GetChild("DungeonInfoItemSlot")

			self.dungeonScrollBar = self.GetChild("ScrollBar")
			self.dungeonInfoBoard = self.GetChild("DungeonInfoBoard")

			self.dungeonInfoName = self.GetChild("DungeonInfoName")
			self.dungeonInfoType = self.GetChild("DungeonInfoType")
			self.dungeonInfoOrganization = self.GetChild("DungeonInfoOrganization")
			self.dungeonInfoLevelLimit = self.GetChild("DungeonInfoLevelLimit")
			self.dungeonInfoPartyMembers = self.GetChild("DungeonInfoPartyMembers")
			self.dungeonInfoCooldown = self.GetChild("DungeonInfoCooldown")
			self.dungeonInfoDuration = self.GetChild("DungeonInfoDuration")
			self.dungeonInfoEntrance = self.GetChild("DungeonInfoEntrance")
			self.dungeonInfoStrengthBonus = self.GetChild("DungeonInfoStrengthBonus")
			self.dungeonInfoResistanceBonus = self.GetChild("DungeonInfoResistanceBonus")
			self.dungeonInfoTotalFinished = self.GetChild("DungeonInfoTotalFinished")
			self.dungeonInfoFastestTime = self.GetChild("DungeonInfoFastestTime")
			self.dungeonInfoHighestDamage = self.GetChild("DungeonInfoHighestDamage")

			self.dungeonInfoTeleportButton = self.GetChild("DungeonInfoTeleportButton")
			self.closeDungeonBoard = self.GetChild("CloseDungeonBoard")

			self.dungeonRank1Button = self.GetChild("DungeonRank1Button")
			self.dungeonRank2Button = self.GetChild("DungeonRank2Button")
			self.dungeonRank3Button = self.GetChild("DungeonRank3Button")
			
			self.dungeonRenderTarget = self.GetChild("DungeonInfoRender")
			self.dungeonRenderTarget.SetEvent(ui.__mem_func__(self.OnPressedInfoButton))

		except:
			import exception
			exception.Abort("DungeonInfo.LoadDialog.GetChild")

		self.dungeonBoardTitleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.closeDungeonBoard.SetEvent(ui.__mem_func__(self.Close))
		self.dungeonInfoTeleportButton.SetEvent(self.TeleportDungeon)

		self.dungeonRank1Button.SetEvent(lambda arg = 1: self.OpenRankingBoard(arg))
		self.dungeonRank2Button.SetEvent(lambda arg = 2: self.OpenRankingBoard(arg))
		self.dungeonRank3Button.SetEvent(lambda arg = 3: self.OpenRankingBoard(arg))

		self.toolTip = uiToolTip.ToolTip()

		self.LoadDungeonButtons()
		self.LoadDungeonInfoBoard(self.dungeonIndex)

		self.isAlreadyLoaded = True

	def OnPressedInfoButton(self):
		if self.renderModelPreview:
			self.OnRenderBossClose()
		elif int(constInfo.dungeonInfo[self.dungeonIndex]['boss_vnum']) != 0:
			self.OnRenderBoss(int(constInfo.dungeonInfo[self.dungeonIndex]['boss_vnum']))

	def OnRenderBoss(self, model):

		RENDER_TARGET_INDEX = 2

		self.renderModelPreview = ui.ThinBoardDungeon()
		self.renderModelPreview.SetParent(self)
		self.renderModelPreview.SetSize(190+10, 280+30)
		self.renderModelPreview.SetPosition(537, 431 / 6)
		self.renderModelPreview.Show()

		self.modelPreviewTarget = ui.RenderTarget()
		self.modelPreviewTarget.SetParent(self.renderModelPreview)
		self.modelPreviewTarget.SetSize(190, 280)
		self.modelPreviewTarget.SetPosition(5, 22)
		self.modelPreviewTarget.SetRenderTarget(RENDER_TARGET_INDEX)
		self.modelPreviewTarget.Show()

		self.modelPreviewTargetText = ui.TextLine()
		self.modelPreviewTargetText.SetParent(self.renderModelPreview)
		self.modelPreviewTargetText.SetPackedFontColor(0xffFFB96D)
		self.modelPreviewTargetText.SetPosition(0, 5)
		self.modelPreviewTargetText.SetText(nonplayer.GetMonsterName(int(constInfo.dungeonInfo[self.dungeonIndex]['boss_vnum'])))
		self.modelPreviewTargetText.SetOutline()
		self.modelPreviewTargetText.SetFeather(False)
		self.modelPreviewTargetText.SetWindowHorizontalAlignCenter()
		self.modelPreviewTargetText.SetHorizontalAlignCenter()
		self.modelPreviewTargetText.Show()
		renderTarget.SetBackground(RENDER_TARGET_INDEX, "d:/ymir work/ui/game/myshop_deco/model_view_bg.sub")
		renderTarget.SetVisibility(RENDER_TARGET_INDEX, True)
		renderTarget.SelectModel(RENDER_TARGET_INDEX, model)

	def OnChangeRenderBoss(self, vnum):
		RENDER_TARGET_INDEX = 2
		renderTarget.SelectModel(RENDER_TARGET_INDEX, vnum)
		self.modelPreviewTargetText.SetText(nonplayer.GetMonsterName(vnum))
		
	def OnRenderBossClose(self):
		RENDER_TARGET_INDEX = 2

		if self.renderModelPreview:
			self.renderModelPreview.Hide()
			self.modelPreviewTargetText.Hide()

			self.renderModelPreview = None
			self.modelPreviewTargetText = None

			renderTarget.SetVisibility(RENDER_TARGET_INDEX, False)
			
	def Close(self):
		if self.toolTip:
			self.toolTip = None

		self.isAlreadyLoaded = False
		
		self.OnRenderBossClose()
		
		self.Hide()

	def GetAffectString(self, affectType):
		if 0 == affectType:
			return None

		try:
			bonus = self.AFFECT_DICT[affectType](affectType)
			bonus = bonus.replace('%', '').replace('+', '')
			result = ''.join([i for i in bonus if not i.isdigit()])
			return result
		except TypeError:
			return "UNKNOWN_VALUE[%s] %s" % (affectType, affectType)
		except KeyError:
			return "UNKNOWN_TYPE[%s] %s" % (affectType, affectType)
		
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if not self.isAlreadyLoaded:
			self.LoadDialog()

		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def LoadDungeonButtons(self):
		if not constInfo.dungeonInfo:
			return

		dungeonInfoLen = len(constInfo.dungeonInfo)
		for index in xrange(min(self.MIN_SCROLLBAR_LIST, len(constInfo.dungeonInfo))):
			self.AppendDungeonButton(
				index,\
				self.dungeonButtonBoard,\
				3, 3 + (38 * index)
			)

		# middleBarScale = 1.0
		#if len(constInfo.dungeonInfo) > self.MIN_SCROLLBAR_LIST:
		#	middleBarScale = float(self.MIN_SCROLLBAR_LIST) / float(dungeonInfoLen)		
		#	self.dungeonScrollBar.SetMiddleBarScale(middleBarScale)
		#	self.dungeonScrollBar.Show()

		self.dungeonScrollBar.SetScrollEvent(self.OnScroll)

	def OnScroll(self):
		button_count = len(self.dungeonButton)
		pos = int(self.dungeonScrollBar.GetPos() * (len(constInfo.dungeonInfo) - button_count))

		self.dungeonButton = {}
		self.dungeonImage = {}
		self.dungeonImageIcon = {}
		self.dungeonName = {}

		for idx in xrange(min(self.MIN_SCROLLBAR_LIST, button_count)):
			realPos = idx + pos

			self.AppendDungeonButton(
				realPos,\
				self.dungeonButtonBoard,\
				3, 3 + (38 * idx)
			)

			if realPos != self.dungeonIndex:
				self.dungeonButton[realPos].SetUpVisual("d:/ymir work/dungeon_info_new/dungeon_info_normal.tga")
				self.dungeonButton[realPos].SetOverVisual("d:/ymir work/dungeon_info_new/dungeon_info_hover.tga")
				self.dungeonButton[realPos].SetDownVisual("d:/ymir work/dungeon_info_new/dungeon_info_down.tga")

	def AppendDungeonButton(self, index, parent, x, y):
		self.dungeonButton[index] = ui.Button()
		self.dungeonButton[index].SetParent(parent)
		self.dungeonButton[index].SetUpVisual("d:/ymir work/dungeon_info_new/dungeon_info_normal.tga")
		self.dungeonButton[index].SetOverVisual("d:/ymir work/dungeon_info_new/dungeon_info_hover.tga")
		self.dungeonButton[index].SetDownVisual("d:/ymir work/dungeon_info_new/dungeon_info_down.tga")
		self.dungeonButton[index].SetPosition(x, y)
		self.dungeonButton[index].SetEvent(lambda: self.LoadDungeonInfoBoard(index))
		self.dungeonButton[index].Show()

		self.dungeonImage[index] = ui.ImageBox()
		self.dungeonImage[index].SetParent(self.dungeonButton[index])
		## Slot Button links im Dungeon Info (bei den Bildern)
		self.dungeonImage[index].LoadImage("d:/ymir work/ui/game/mailbox/mailbox_icon_empty.sub")
		self.dungeonImage[index].SetPosition(1, 2)
		self.dungeonImage[index].Show()

		self.dungeonImageIcon[index] = ui.Button()
		self.dungeonImageIcon[index].SetParent(self.dungeonImage[index])

		mapIndex = constInfo.dungeonInfo[index]['map_index']
		self.dungeonImageIcon[index].SetUpVisual("d:/ymir work/ui/game/dungeon_info/icons/%d.tga" % mapIndex)
		self.dungeonImageIcon[index].SetOverVisual("d:/ymir work/ui/game/dungeon_info/icons/%d.tga" % mapIndex)
		self.dungeonImageIcon[index].SetDownVisual("d:/ymir work/ui/game/dungeon_info/icons/%d.tga" % mapIndex)
		self.dungeonImageIcon[index].SetEvent(lambda: self.LoadDungeonInfoBoard(index))

		self.dungeonImageIcon[index].SetPosition(0, 0)
		self.dungeonImageIcon[index].Show()

		self.dungeonName[index] = ui.TextLine()
		self.dungeonName[index].SetParent(self.dungeonButton[index])
		self.dungeonName[index].SetPosition(40, 10)
		self.dungeonName[index].SetText("%s" % constInfo.dungeonInfo[index]['map'])
		self.dungeonName[index].Show()

	def LoadDungeonInfoBoard(self, index):
		self.dungeonIndex = index
		## Buttons linke seite fürs Dungeon Info wo der name der Maps drauf steht
		self.dungeonButton[self.dungeonIndex].SetUpVisual("d:/ymir work/dungeon_info_new/dungeon_info_normal.tga")
		self.dungeonButton[self.dungeonIndex].SetOverVisual("d:/ymir work/dungeon_info_new/dungeon_info_hover.tga")
		self.dungeonButton[self.dungeonIndex].SetDownVisual("d:/ymir work/dungeon_info_new/dungeon_info_down.tga")

		pos = int(self.dungeonScrollBar.GetPos() * (len(constInfo.dungeonInfo) - len(self.dungeonButton)))
		for idx in xrange(len(self.dungeonButton)):
			realPos = idx + pos
			if realPos != self.dungeonIndex:
			## Buttons linke seite fürs Dungeon Info wo der name der Maps drauf steht
				self.dungeonButton[realPos].SetUpVisual("d:/ymir work/dungeon_info_new/dungeon_info_normal.tga")
				self.dungeonButton[realPos].SetOverVisual("d:/ymir work/dungeon_info_new/dungeon_info_hover.tga")
				self.dungeonButton[realPos].SetDownVisual("d:/ymir work/dungeon_info_new/dungeon_info_down.tga")

		dungeonMap = str(constInfo.dungeonInfo[self.dungeonIndex]['map'])
		dungeonType = constInfo.dungeonInfo[self.dungeonIndex]['type']
		dungeonOrganization = constInfo.dungeonInfo[self.dungeonIndex]['organization']
		dungeonLevelMin = constInfo.dungeonInfo[self.dungeonIndex]['min_level']
		dungeonLevelMax = constInfo.dungeonInfo[self.dungeonIndex]['max_level']
		dungeonPartyMembers = constInfo.dungeonInfo[self.dungeonIndex]['party_members']
		dungeonCooldown = constInfo.dungeonInfo[self.dungeonIndex]['cooldown']
		dungeonDuration = constInfo.dungeonInfo[self.dungeonIndex]['duration']
		dungeonEntranceMap = str(constInfo.dungeonInfo[self.dungeonIndex]['entrance_map'])
		dungeonStrengthBonus = self.GetAffectString(constInfo.dungeonInfo[self.dungeonIndex]['strength_bonus'])
		dungeonResistanceBonus = self.GetAffectString(constInfo.dungeonInfo[self.dungeonIndex]['resistance_bonus'])
		dungeonItemVnum = int(constInfo.dungeonInfo[self.dungeonIndex]['item_vnum'])
		dungeonFinished = int(constInfo.dungeonInfo[self.dungeonIndex]['finished'])
		dungeonFastestTime = constInfo.dungeonInfo[self.dungeonIndex]['fastest_time']
		dungeonHighestDamage = int(constInfo.dungeonInfo[self.dungeonIndex]['highest_damage'])

		self.dungeonInfoName.SetText("%s" % dungeonMap)
		self.dungeonInfoType.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_TYPE, self.DUNGEON_TYPE[dungeonType]))
		self.dungeonInfoOrganization.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_ORGANIZATION, self.DUNGEON_ORGANIZATION[dungeonOrganization]))
		self.dungeonInfoLevelLimit.SetText("%s : %d - %d" % (uiScriptLocale.DUNGEON_INFO_LEVEL_LIMIT, dungeonLevelMin, dungeonLevelMax))
		self.dungeonInfoPartyMembers.SetText("%s : %d" % (uiScriptLocale.DUNGEON_INFO_PARTY_MEMBERS, dungeonPartyMembers))
		self.dungeonInfoCooldown.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_COOLDOWN, self.FormatTime(dungeonCooldown)))
		self.dungeonInfoDuration.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_DURATION, self.FormatTime(dungeonDuration)))
		self.dungeonInfoEntrance.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_ENTRANCE, dungeonEntranceMap))
		self.dungeonInfoStrengthBonus.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_STRENGTH, dungeonStrengthBonus))
		self.dungeonInfoResistanceBonus.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_RESISTANCE, dungeonResistanceBonus))
		self.dungeonInfoTotalFinished.SetText("%s : %d" % (uiScriptLocale.DUNGEON_INFO_TOTAL_FINISHED, dungeonFinished))
		self.dungeonInfoFastestTime.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_FASTEST_TIME, self.FormatTime(dungeonFastestTime)))
		self.dungeonInfoHighestDamage.SetText("%s : %d" % (uiScriptLocale.DUNGEON_INFO_HIGHEST_DAMAGE, dungeonHighestDamage))

		if dungeonItemVnum > 0:
			self.dungeonInfoItemSlot.LoadImage("icon/item/%d.tga" % dungeonItemVnum)
		else:
			self.dungeonInfoItemSlot.LoadImage("d:/ymir work/ui/pet/skill_button/skill_enable_button.sub")

		if self.renderModelPreview:
			self.OnChangeRenderBoss(int(constInfo.dungeonInfo[self.dungeonIndex]['boss_vnum']))
	def FormatTime(self, seconds):
		if seconds == 0:
			return localeInfo.DUNGEON_INFO_NONE

		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)

		return "%d:%02d:%02d" % (h, m, s)

	def TeleportDungeon(self):
		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.Open()
		self.questionDialog.SetText(localeInfo.DUNGEON_INFO_TELEPORT % str(constInfo.dungeonInfo[self.dungeonIndex]['map']))
		self.questionDialog.SetAcceptText(localeInfo.UI_ACCEPT)
		self.questionDialog.SetCancelText(localeInfo.UI_DENY)
		self.questionDialog.SetAcceptEvent(lambda arg = True: self.AnswerTeleport(arg))
		self.questionDialog.SetCancelEvent(lambda arg = False: self.AnswerTeleport(arg))
		self.questionDialog.SetTop()

	def AnswerTeleport(self, answer):
		if not self.questionDialog:
			return

		if answer == True:
			import event

			dungeonMapCoordX = int(constInfo.dungeonInfo[self.dungeonIndex]['map_coord_x'])
			dungeonMapCoordY = int(constInfo.dungeonInfo[self.dungeonIndex]['map_coord_y'])

			net.DungeonTeleport(dungeonMapCoordX, dungeonMapCoordY)

		self.questionDialog.Close()
		self.questionDialog = None

	def OpenRankingBoard(self, rankType):
		if rankType > 0:
			import event
			net.DungeonRank(self.dungeonIndex, rankType)
			constInfo.dungeonRanking["ranking_type"] = rankType
			
	def OnUpdate(self):
		if self.toolTip:
			if self.dungeonInfoItemSlot.IsIn():
				self.toolTip.ClearToolTip()

				dungeonItemVnum = constInfo.dungeonInfo[self.dungeonIndex]['item_vnum']
				if dungeonItemVnum > 0:
					item.SelectItem(dungeonItemVnum)

					self.toolTip.AppendTextLine(item.GetItemName(), self.TOOLTIP_SPECIAL_COLOR)
					self.toolTip.AppendDescription(item.GetItemDescription(), 26)

					self.toolTip.AlignHorizonalCenter()
					self.toolTip.ShowToolTip()

			else:
				self.toolTip.HideToolTip()

class DungeonRank(ui.ScriptWindow):
	SLOT_RANKING = 0
	SLOT_PLAYER_NAME = 1
	SLOT_PLAYER_LEVEL = 2
	SLOT_POINT_TYPE = 3

	MAX_LINE_COUNT = 5

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.NowStartLineNumber = 0
		self.dungeonRankingScrollBar = None
		self.ResultButtonList = []
		self.ResultSlotList = {}
		self.MyResultSlotList = []

		self.isAlreadyLoaded = False

	def __del__(self):
		ui.ScriptWindow.__del__(self)

		self.NowStartLineNumber = 0
		self.dungeonRankingScrollBar = None
		self.ResultButtonList = []
		self.ResultSlotList = {}
		self.MyResultSlotList = []

		self.isAlreadyLoaded = False

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/dungeonrankingwindow.py")
		except:
			import exception
			exception.Abort("DungeonRank.LoadDialog.LoadScript")

		try:
			self.dungeonRankingTitleBar = self.GetChild("DungeonRankingTitleBar")
			self.dungeonRankingTitleName = self.GetChild("DungeonRankingTitleName")
			self.dungeonRankingScrollBar = self.GetChild("DungeonRankingScrollBar")

			self.dungeonRankingResultPosition = self.GetChild("ResultRanking")
			self.dungeonRankingResultName = self.GetChild("ResultName")
			self.dungeonRankingResultLevel = self.GetChild("ResultLevel")
			self.dungeonRankingResultPoints = self.GetChild("ResultPoints")

		except:
			import exception
			exception.Abort("DungeonRank.__LoadWindow.SetObject")

		self.dungeonRankingTitleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.dungeonRankingScrollBar.SetScrollEvent(ui.__mem_func__(self.OnScrollControl))

		self.MakeUiBoard()
		self.RefreshDungeonRanking()

		self.isAlreadyLoaded = True

	def MakeUiBoard(self):
		try:
			yPos = 0
			for i in range(0, self.MAX_LINE_COUNT+1):
				yPos = 65 + i * 24
				if i == 5:
					yPos += 10

				RankingSlotImage = ui.MakeImageBox(self, "d:/ymir work/ui/public/parameter_slot_00.sub", 23, yPos)
				RankingSlotImage.SetAlpha(0)
				RankingSlot = ui.MakeTextLine(RankingSlotImage)
				self.Children.append(RankingSlotImage)
				self.Children.append(RankingSlot)

				GuildNameImage = ui.MakeImageBox(self, "d:/ymir work/ui/public/parameter_slot_04.sub", 77, yPos)
				GuildNameImage.SetAlpha(0)
				GuildNameSlot = ui.MakeTextLine(GuildNameImage)
				self.Children.append(GuildNameImage)
				self.Children.append(GuildNameSlot)

				MemberCountSlotImage = ui.MakeImageBox(self, "d:/ymir work/ui/public/parameter_slot_00.sub", 205, yPos)
				MemberCountSlotImage.SetAlpha(0)
				MemberCountSlot = ui.MakeTextLine(MemberCountSlotImage)
				self.Children.append(MemberCountSlotImage)
				self.Children.append(MemberCountSlot)

				ClearTimeSlotImage = ui.MakeImageBox(self, "d:/ymir work/ui/public/parameter_slot_00.sub", 270, yPos)
				ClearTimeSlotImage.SetAlpha(0)
				ClearTimeSlot = ui.MakeTextLine(ClearTimeSlotImage)
				self.Children.append(ClearTimeSlotImage)
				self.Children.append(ClearTimeSlot)

				if i < self.MAX_LINE_COUNT:
					tempguildlankingslotlist = []
					tempguildlankingslotlist.append(RankingSlot)

					tempguildlankingslotlist.append(GuildNameSlot)
					tempguildlankingslotlist.append(MemberCountSlot)
					tempguildlankingslotlist.append(ClearTimeSlot)
					self.ResultSlotList[i] = tempguildlankingslotlist
				else:
					self.MyResultSlotList.append(RankingSlot)
					self.MyResultSlotList.append(GuildNameSlot)
					self.MyResultSlotList.append(MemberCountSlot)
					self.MyResultSlotList.append(ClearTimeSlot)

				itemSlotButtonImage = ui.MakeButton(self, 21, yPos, "", "d:/ymir work/ui/game/guild/dragonlairranking/", "ranking_list_button01.sub", "ranking_list_button02.sub", "ranking_list_button02.sub")
				itemSlotButtonImage.Show()
				itemSlotButtonImage.Disable()
				self.Children.append(itemSlotButtonImage)

				if i < self.MAX_LINE_COUNT:
					self.ResultButtonList.append(itemSlotButtonImage)

		except:
			import exception
			exception.Abort("GuildWindow_GuildDragonLairWindow.MakeUiBoard")

	def RefreshDungeonRanking(self):
		self.AllClear()

		dungeonRankingType = constInfo.dungeonRanking["ranking_type"]
		dungeonRankingList = constInfo.dungeonRanking["ranking_list"]
		# print 'dungeonRankingList', dungeonRankingList
		if not dungeonRankingList:
			return

		if dungeonRankingType == 1:
			self.dungeonRankingTitleName.SetText(uiScriptLocale.DUNGEON_RANKING_TYPE1)
			self.dungeonRankingResultPoints.SetText(uiScriptLocale.DUNGEON_RANKING_POINT_TYPE1)
		elif dungeonRankingType == 2:
			self.dungeonRankingTitleName.SetText(uiScriptLocale.DUNGEON_RANKING_TYPE2)
			self.dungeonRankingResultPoints.SetText(uiScriptLocale.DUNGEON_RANKING_POINT_TYPE2)
		elif dungeonRankingType == 3:
			self.dungeonRankingTitleName.SetText(uiScriptLocale.DUNGEON_RANKING_TYPE3)
			self.dungeonRankingResultPoints.SetText(uiScriptLocale.DUNGEON_RANKING_POINT_TYPE3)

		for line, ResultSlotList in self.ResultSlotList.items():
			nowindex = line + self.NowStartLineNumber

			if nowindex >= len(dungeonRankingList):
				break

			rankingData = dungeonRankingList[nowindex]

			ResultSlotList[self.SLOT_RANKING].SetText(str(nowindex+1))
			ResultSlotList[self.SLOT_PLAYER_NAME].SetText(str(rankingData[0]))
			ResultSlotList[self.SLOT_PLAYER_LEVEL].SetText(str(rankingData[1]))
			if dungeonRankingType == 2:
				ResultSlotList[self.SLOT_POINT_TYPE].SetText(self.FormatTime(rankingData[2]))
			else:
				ResultSlotList[self.SLOT_POINT_TYPE].SetText(str(rankingData[2]))
			self.ResultButtonList[line].Show()

		self.MyResultSlotList[self.SLOT_RANKING].SetText("-")
		self.MyResultSlotList[self.SLOT_PLAYER_NAME].SetText("-")
		self.MyResultSlotList[self.SLOT_PLAYER_LEVEL].SetText("-")
		self.MyResultSlotList[self.SLOT_POINT_TYPE].SetText("-")

		self.dungeonRankingScrollBar.SetMiddleBarSize(float(self.MAX_LINE_COUNT) / float(self.CheckNowItemCount()))

	def FormatTime(self, seconds):
		if seconds == 0:
			return 0

		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)

		return "%d:%02d:%02d" % (h, m, s)

	def AllClear(self):
		for line, ResultSlotList in self.ResultSlotList.items():
			ResultSlotList[self.SLOT_RANKING].SetText("")
			ResultSlotList[self.SLOT_PLAYER_NAME].SetText("")
			ResultSlotList[self.SLOT_PLAYER_LEVEL].SetText("")
			ResultSlotList[self.SLOT_POINT_TYPE].SetText("")
			self.ResultButtonList[line].SetUp()
			self.ResultButtonList[line].Hide()

		self.MyResultSlotList[self.SLOT_RANKING].SetText("-")
		self.MyResultSlotList[self.SLOT_PLAYER_NAME].SetText("-")
		self.MyResultSlotList[self.SLOT_PLAYER_LEVEL].SetText("-")
		self.MyResultSlotList[self.SLOT_POINT_TYPE].SetText("-")

	def Close(self):
		constInfo.DUNGEONINFO_OPEN = 0
		self.isAlreadyLoaded = False
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def CheckNowItemCount(self):
		if len(constInfo.dungeonRanking["ranking_list"]) <= self.MAX_LINE_COUNT:
			return self.MAX_LINE_COUNT
		else:
			return len(constInfo.dungeonRanking["ranking_list"])

	def OnScrollControl(self):
		nowitemcount = 0
		if len(constInfo.dungeonRanking["ranking_list"]) <= self.MAX_LINE_COUNT :
			nowitemcount = 0
		else:
			nowitemcount = (len(constInfo.dungeonRanking["ranking_list"]) - self.MAX_LINE_COUNT)

		pos = self.dungeonRankingScrollBar.GetPos() * nowitemcount

		if not int(pos) == self.NowStartLineNumber:
			self.NowStartLineNumber = int(pos)
			self.RefreshDungeonRanking()

	def Open(self):
		if not self.isAlreadyLoaded:
			self.LoadDialog()

		self.NowStartLineNumber = 0
		self.dungeonRankingScrollBar.SetPos(0)

		self.SetCenterPosition()
		self.SetTop()
		self.Show()
