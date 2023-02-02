import dbg
import player
import item
import grp
import wndMgr
import skill
import shop
import exchange
import grpText
import safebox
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import app
import background
import nonplayer
import chr
import ui
import mouseModule
import constInfo
import shiningnames
import renderTarget
import uiScriptLocale
if app.ENABLE_SASH_SYSTEM:
	import sash
if app.ENABLE_RENDER_TARGET_SYSTEM:
	import renderTarget

WARP_SCROLLS = [22011, 22000, 22010]
DESC_DEFAULT_MAX_COLS = 26 
DESC_WESTERN_MAX_COLS = 35
DESC_WESTERN_MAX_WIDTH = 220
def chop(n):
	return round(n - 0.5, 1)
if app.INGAME_WIKI:
	def GET_AFFECT_STRING(affType, affValue):
		if 0 == affType:
			return None
		
		try:
			affectString = ItemToolTip.AFFECT_DICT[affType]
			if type(affectString) != str:
				return affectString(affValue)

			if affectString.find("%d") != -1:
				return affectString % affValue
			else:
				return affectString
		except KeyError:
			return "UNKNOWN_TYPE[%s] %s" % (affType, affValue)
def pointop(n):
	t = int(n)
	if t / 10 < 1:
		return "0."+n
	else:		
		return n[0:len(n)-1]+"."+n[len(n)-1:]

def SplitDescription(desc, limit):
	total_tokens = desc.split()
	line_tokens = []
	line_len = 0
	lines = []
	for token in total_tokens:
		if "|" in token:
			sep_pos = token.find("|")
			line_tokens.append(token[:sep_pos])
			lines.append(" ".join(line_tokens))
			line_len = len(token) - (sep_pos + 1)
			line_tokens = [token[sep_pos+1:]]
		else:
			line_len += len(token)
			if len(line_tokens) + line_len > limit:
				lines.append(" ".join(line_tokens))
				line_len = len(token)
				line_tokens = [token]
			else:
				line_tokens.append(token)

	if line_tokens:
		lines.append(" ".join(line_tokens))
	return lines
###################################################################################################
## ToolTip
##
##   NOTE : CoAc´A Item°u SkillA≫ ≫o¼OA¸·I Æ?E­ ½AANμI¾uA½
##          CIAo¸¸ ±×´UAo AC¹I°¡ ¾ø¾i º¸AO
##
class ToolTip(ui.ThinBoard):
	TOOL_TIP_WIDTH = 190
	TOOL_TIP_HEIGHT = 10
	TEXT_LINE_HEIGHT = 17
	TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
	SPECIAL_TITLE_COLOR = grp.GenerateColor(1.0, 0.7843, 0.0, 1.0)
	NORMAL_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	FONT_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	PRICE_COLOR = 0xffFFB96D
	HIGH_PRICE_COLOR = SPECIAL_TITLE_COLOR
	MIDDLE_PRICE_COLOR = grp.GenerateColor(0.85, 0.85, 0.85, 1.0)
	LOW_PRICE_COLOR = grp.GenerateColor(0.7, 0.7, 0.7, 1.0)
	ENABLE_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	DISABLE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
	NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
	POSITIVE_COLOR = grp.GenerateColor(0.5411, 0.7254, 0.5568, 1.0)
	SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
	SPECIAL_POSITIVE_COLOR2 = grp.GenerateColor(0.8824, 0.9804, 0.8824, 1.0)
	ITEM_BUFF_LEVEL_COLOR = 0xffffd300
	ITEM_BUFF_TYPE_COLOR = 0xfffc9c3a
	ITEM_BUFF_RATE_COLOR = 0xff40e0d0
	ITEM_BUFF_DURATION_COLOR = 0xffadff00
	ITEM_BUFF_USAGE_COLOR = 0xffffffff	
	CONDITION_COLOR = 0xffBEB47D
	TYRANIS_TOOLTIP_COLOR = 0xff5FFFF3
	CHANGELOOK_ITEMNAME_COLOR = 0xffBCE55C
	CAN_LEVEL_UP_COLOR = 0xff8EC292
	CANNOT_LEVEL_UP_COLOR = DISABLE_COLOR
	NEED_SKILL_POINT_COLOR = 0xff9A9CDB
	ITEMVNUM_COLOR = 0xff90ee90
	def __init__(self, width = TOOL_TIP_WIDTH, isPickable=FALSE):
		ui.ThinBoard.__init__(self, "TOP_MOST")
		if isPickable:
			pass
		else:
			self.AddFlag("not_pick")
		self.AddFlag("float")
		self.followFlag = TRUE
		self.toolTipWidth = width
		self.xPos = -1
		self.yPos = -1
		self.defFontName = localeInfo.UI_DEF_FONT
		self.ClearToolTip()
	def __del__(self):
		ui.ThinBoard.__del__(self)
	def ClearToolTip(self):
		self.toolTipHeight = 12
		self.childrenList = []
	def SetFollow(self, flag):
		self.followFlag = flag
	def SetDefaultFontName(self, fontName):
		self.defFontName = fontName
	def AppendSpace(self, size):
		self.toolTipHeight += size
		self.ResizeToolTip()
	if app.INGAME_WIKI:
		def SetThinBoardSize(self, width, height = 12):
			self.toolTipWidth = width 
			self.toolTipHeight = height
	def AppendHorizontalLine(self):
		for i in xrange(2):
			horizontalLine = ui.Line()
			horizontalLine.SetParent(self)
			horizontalLine.SetPosition(0, self.toolTipHeight + 3 + i)
			horizontalLine.SetWindowHorizontalAlignCenter()
			horizontalLine.SetSize(150, 0)
			horizontalLine.Show()
			if 0 == i:
				horizontalLine.SetColor(0xff555555)
			else:
				horizontalLine.SetColor(0xff000000)
			self.childrenList.append(horizontalLine)
		self.toolTipHeight += 11
		self.ResizeToolTip()
	def AlignHorizonalCenter(self):
		for child in self.childrenList:
			(x, y)=child.GetLocalPosition()
			child.SetPosition(self.toolTipWidth/2, y)
		self.ResizeToolTip()
	def AutoAppendTextLine(self, text, color = FONT_COLOR, centerAlign = TRUE):
		textLine = ui.TextLine()
		textLine.SetParent(self)
		textLine.SetFontName(self.defFontName)
		textLine.SetPackedFontColor(color)
		textLine.SetText(text)
		textLine.SetOutline()
		textLine.SetFeather(FALSE)
		textLine.Show()
		if centerAlign:
			textLine.SetPosition(self.toolTipWidth/2, self.toolTipHeight)
			textLine.SetHorizontalAlignCenter()
		else:
			textLine.SetPosition(10, self.toolTipHeight)
		self.childrenList.append(textLine)
		(textWidth, textHeight)=textLine.GetTextSize()
		textWidth += 40
		textHeight += 5
		if self.toolTipWidth < textWidth:
			self.toolTipWidth = textWidth
		self.toolTipHeight += textHeight
		return textLine
	def AppendTextLine(self, text, color = FONT_COLOR, centerAlign = TRUE):
		textLine = ui.TextLine()
		textLine.SetParent(self)
		textLine.SetFontName(self.defFontName)
		textLine.SetPackedFontColor(color)
		textLine.SetText(text)
		textLine.SetOutline()
		textLine.SetFeather(FALSE)
		textLine.Show()
		if centerAlign:
			textLine.SetPosition(self.toolTipWidth/2, self.toolTipHeight)
			textLine.SetHorizontalAlignCenter()
		else:
			textLine.SetPosition(10, self.toolTipHeight)
		self.childrenList.append(textLine)
		self.toolTipHeight += self.TEXT_LINE_HEIGHT
		self.ResizeToolTip()
		return textLine
	def AppendDescription(self, desc, limit, color = FONT_COLOR):
		if localeInfo.IsEUROPE():
			self.__AppendDescription_WesternLanguage(desc, color)
		else:
			self.__AppendDescription_EasternLanguage(desc, limit, color)
	def __AppendDescription_EasternLanguage(self, description, characterLimitation, color=FONT_COLOR):
		length = len(description)
		if 0 == length:
			return
		lineCount = grpText.GetSplitingTextLineCount(description, characterLimitation)
		for i in xrange(lineCount):
			if 0 == i:
				self.AppendSpace(5)
			self.AppendTextLine(grpText.GetSplitingTextLine(description, characterLimitation, i), color)
	def __AppendDescription_WesternLanguage(self, desc, color=FONT_COLOR):
		lines = SplitDescription(desc, DESC_WESTERN_MAX_COLS)
		if not lines:
			return
		self.AppendSpace(5)
		for line in lines:
			self.AppendTextLine(line, color)

	def ResizeToolTip(self):
		self.SetSize(self.toolTipWidth, self.TOOL_TIP_HEIGHT + self.toolTipHeight)
	def SetTitle(self, name):
		self.AppendTextLine(name, self.TITLE_COLOR)
	def GetLimitTextLineColor(self, curValue, limitValue):
		if curValue < limitValue:
			return self.DISABLE_COLOR
		return self.ENABLE_COLOR
		
	def GetChangeTextLineColor(self, value, isSpecial=FALSE):
		if value > 0:
			if isSpecial:
				return self.SPECIAL_POSITIVE_COLOR
			else:
				return self.POSITIVE_COLOR
		if 0 == value:
			return self.NORMAL_COLOR
		return self.NEGATIVE_COLOR
	def SetToolTipPosition(self, x = -1, y = -1):
		self.xPos = x
		self.yPos = y
	def ShowToolTip(self):
		self.SetTop()
		self.Show()
		self.OnUpdate()
	def HideToolTip(self):
		self.Hide()
	def OnUpdate(self):
		if not self.followFlag:
			return
		x = 0
		y = 0
		width = self.GetWidth()
		height = self.toolTipHeight
		if -1 == self.xPos and -1 == self.yPos:
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			if mouseY < wndMgr.GetScreenHeight() - 300:
				y = mouseY + 40
			else:
				y = mouseY - height - 30
			x = mouseX - width/2				
		else:
			x = self.xPos - width/2
			y = self.yPos - height
		x = max(x, 0)
		y = max(y, 0)
		x = min(x + width/2, wndMgr.GetScreenWidth() - width/2) - width/2
		y = min(y + self.GetHeight(), wndMgr.GetScreenHeight()) - self.GetHeight()
		parentWindow = self.GetParentProxy()
		if parentWindow:
			(gx, gy) = parentWindow.GetGlobalPosition()
			x -= gx
			y -= gy
		self.SetPosition(x, y)
class ItemToolTip(ToolTip):
	if app.ENABLE_SEND_TARGET_INFO:
		isStone = False
		isBook = False
		isBook2 = False
		
	ModelPreviewBoard = None
	ModelPreview = None
	ModelPreviewText = None
		
	CHARACTER_NAMES = ( 
		localeInfo.TOOLTIP_WARRIOR,
		localeInfo.TOOLTIP_ASSASSIN,
		localeInfo.TOOLTIP_SURA,
		localeInfo.TOOLTIP_SHAMAN 
	)
	CHARACTER_COUNT = len(CHARACTER_NAMES)
	WEAR_NAMES = ( 
		localeInfo.TOOLTIP_ARMOR, 
		localeInfo.TOOLTIP_HELMET, 
		localeInfo.TOOLTIP_SHOES, 
		localeInfo.TOOLTIP_WRISTLET, 
		localeInfo.TOOLTIP_WEAPON, 
		localeInfo.TOOLTIP_NECK,
		localeInfo.TOOLTIP_EAR,
		localeInfo.TOOLTIP_UNIQUE,
		localeInfo.TOOLTIP_SHIELD,
		localeInfo.TOOLTIP_ARROW,
	)
	WEAR_COUNT = len(WEAR_NAMES)
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
		item.APPLY_ATTBONUS_ELEC : localeInfo.TOOLTIP_APPLY_ATTBONUS_ELEC,
		item.APPLY_ATTBONUS_FIRE : localeInfo.TOOLTIP_APPLY_ATTBONUS_FIRE,
		item.APPLY_ATTBONUS_ICE : localeInfo.TOOLTIP_APPLY_ATTBONUS_ICE,
		item.APPLY_ATTBONUS_WIND : localeInfo.TOOLTIP_APPLY_ATTBONUS_WIND,
		item.APPLY_ATTBONUS_EARTH : localeInfo.TOOLTIP_APPLY_ATTBONUS_EARTH,
		item.APPLY_ATTBONUS_DARK : localeInfo.TOOLTIP_APPLY_ATTBONUS_DARK,
	}
	if app.ENABLE_NEW_ATTRIBUTES:
		AFFECT_DICT.update( {item.APPLY_ATTBONUS_METIN : localeInfo.TOOLTIP_APPLY_ATTBONUS_METIN})
		AFFECT_DICT.update( {item.APPLY_ATTBONUS_BOSS : localeInfo.TOOLTIP_APPLY_ATTBONUS_BOSS})
	
	PET_SKILL_NAMES ={
		0 : localeInfo.PET_SKILL_TOOLTIP_00,
		1 : localeInfo.PET_SKILL_TOOLTIP_01,
		2 : localeInfo.PET_SKILL_TOOLTIP_02,
		3 : localeInfo.PET_SKILL_TOOLTIP_03,
		4 : localeInfo.PET_SKILL_TOOLTIP_04,
		5 : localeInfo.PET_SKILL_TOOLTIP_05,
		6 : localeInfo.PET_SKILL_TOOLTIP_06,
		7 : localeInfo.PET_SKILL_TOOLTIP_07,
		8 : localeInfo.PET_SKILL_TOOLTIP_08,
		9 : localeInfo.PET_SKILL_TOOLTIP_09,
		10 : localeInfo.PET_SKILL_TOOLTIP_10,
		11 : localeInfo.PET_SKILL_TOOLTIP_11,
		12 : localeInfo.PET_SKILL_TOOLTIP_12,
		13 : localeInfo.PET_SKILL_TOOLTIP_13,
		14 : localeInfo.PET_SKILL_TOOLTIP_14,
		15 : localeInfo.PET_SKILL_TOOLTIP_15,
		16 : localeInfo.PET_SKILL_TOOLTIP_16,
		17 : localeInfo.PET_SKILL_TOOLTIP_17,
		18 : localeInfo.PET_SKILL_TOOLTIP_18,
		19 : localeInfo.PET_SKILL_TOOLTIP_19,
		20 : localeInfo.PET_SKILL_TOOLTIP_20 ,
		21 : localeInfo.PET_SKILL_TOOLTIP_21,
		22 : localeInfo.PET_SKILL_TOOLTIP_22,
		23 : localeInfo.PET_SKILL_TOOLTIP_23,
	}
	
	ATTRIBUTE_NEED_WIDTH = {
		23 : 230,
		24 : 230,
		25 : 230,
		26 : 220,
		27 : 210,
		35 : 210,
		36 : 210,
		37 : 210,
		38 : 210,
		39 : 210,
		40 : 210,
		41 : 210,
		42 : 220,
		43 : 230,
		45 : 230,
	}
	ANTI_FLAG_DICT = {
		0 : item.ITEM_ANTIFLAG_WARRIOR,
		1 : item.ITEM_ANTIFLAG_ASSASSIN,
		2 : item.ITEM_ANTIFLAG_SURA,
		3 : item.ITEM_ANTIFLAG_SHAMAN,
	}
	FONT_COLOR = grp.GenerateColor(0.7607, 0.7607, 0.7607, 1.0)
	def __init__(self, *args, **kwargs):
		ToolTip.__init__(self, *args, **kwargs)
		self.itemVnum = 0
		self.isShopItem = FALSE
		# ¾ÆAIAU AøÆAA≫ C￥½ACO ¶§ CoAc A³¸?AI°¡ Aø¿eCO ¼o ¾ø´A ¾ÆAIAUAI¶o¸e °­A|·I Disable Color·I ¼³A¤ (AI¹I ±×·¸°O AUμ¿CI°i AOA¸³ª ²¨¾ß CO CE¿a°¡ AO¾i¼­)
		self.bCannotUseItemForceSetDisableColor = TRUE 
	def __del__(self):
		ToolTip.__del__(self)
		
	if app.ENABLE_RENDER_TARGET_SYSTEM:
		def CanViewRendering(self):
			race = player.GetRace()
			job = chr.RaceToJob(race)
			if not self.ANTI_FLAG_DICT.has_key(job):
				return False

			if item.IsAntiFlag(self.ANTI_FLAG_DICT[job]):
				return False

			sex = chr.RaceToSex(race)
			
			MALE = 1
			FEMALE = 0

			if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and sex == MALE:
				return False

			if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and sex == FEMALE:
				return False

			return True

		def CanViewRenderingSex(self):
			race = player.GetRace()
			sex = chr.RaceToSex(race)
			
			MALE = 1
			FEMALE = 0

			if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and sex == MALE:
				return False

			if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and sex == FEMALE:
				return False

			return True
		
	def SetCannotUseItemForceSetDisableColor(self, enable):
		self.bCannotUseItemForceSetDisableColor = enable
	def CanEquip(self):
		if not item.IsEquipmentVID(self.itemVnum):
			return TRUE
		race = player.GetRace()
		job = chr.RaceToJob(race)
		if not self.ANTI_FLAG_DICT.has_key(job):
			return FALSE
		if item.IsAntiFlag(self.ANTI_FLAG_DICT[job]):
			return FALSE
		sex = chr.RaceToSex(race)

		MALE = 1
		FEMALE = 0
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and sex == MALE:
			return FALSE
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and sex == FEMALE:
			return FALSE
		for i in xrange(item.LIMIT_MAX_NUM):
			(limitType, limitValue) = item.GetLimit(i)
			if item.LIMIT_LEVEL == limitType:
				if player.GetStatus(player.LEVEL) < limitValue:
					return FALSE
					
			elif item.LIMIT_PRESTIGE == limitType:
				if player.GetStatus(player.PRESTIGE) < limitValue:
					return FALSE		
			"""
			elif item.LIMIT_STR == limitType:
				if player.GetStatus(player.ST) < limitValue:
					return FALSE
			elif item.LIMIT_DEX == limitType:
				if player.GetStatus(player.DX) < limitValue:
					return FALSE
			elif item.LIMIT_INT == limitType:
				if player.GetStatus(player.IQ) < limitValue:
					return FALSE
			elif item.LIMIT_CON == limitType:
				if player.GetStatus(player.HT) < limitValue:
					return FALSE
			"""
		return TRUE
	def AppendTextLine(self, text, color = FONT_COLOR, centerAlign = TRUE):
		if not self.CanEquip() and self.bCannotUseItemForceSetDisableColor:
			color = self.DISABLE_COLOR
		return ToolTip.AppendTextLine(self, text, color, centerAlign)
		
	def ClearToolTip(self):
		self.isShopItem = FALSE
		self.toolTipWidth = self.TOOL_TIP_WIDTH
		ToolTip.ClearToolTip(self)
		
	if app.ENABLE_RENDER_TARGET_SYSTEM:
		def BindInterface(self, interface):
			self.interface = interface

	def SetInventoryItem(self, slotIndex, window_type = player.INVENTORY):
		itemVnum = player.GetItemIndex(window_type, slotIndex)
		itemCount = player.GetItemCount(window_type, slotIndex)
		item.SelectItem(itemVnum)
		itemType = item.GetItemType()
		if 0 == itemVnum:
			return
		self.ClearToolTip()
		if shop.IsOpen():
			if not shop.IsPrivateShop():
				self.AppendSellingPrice(player.GetISellItemPrice(window_type, slotIndex))
		metinSlot = [player.GetItemMetinSocket(window_type, slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		attrSlot = [player.GetItemAttribute(window_type, slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.INVENTORY, slotIndex)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
		
		if shop.IsOpen():
			if not shop.IsPrivateShop():
				self.AppendSpace(7) ##Platzhalter 
				self.AppendTextLine("|Eemoji/key_ctrl|e + |Eemoji/key_lclick|e - Direct sell") 
		
		notAllowedTargetRenderItemList = [38723, 86085, 86086, 86087, 86088, 86095, 86096, 86097, 86098, 86070, 86071, 86072, 86073, 86075, 86076, 86077, 86078, 86065, 86066, 86067, 86068, 50640, 71770, 71771, 71772, 71773, 71774, 71775, 71776, 70039, 50639, 77289, 77290, 55629, 18900, 50107, 50108, 71021, 71030, 71044, 71029, 71027, 71028, 71045, 27863, 27864, 27865, 27866, 27867, 27868, 27869, 27870, 27871, 27872, 27873, 27874, 27875, 27876, 27877, 27878, 27879, 27880, 27881, 27882, 27882, 27883, 27801, 27800, 27610, 71020, 50635, 50637, 50626, 50625, 50627, 50631, 50629, 50636, 50634, 50633, 50628, 50623, 50638, 50624, 50630, 50632, 76016, 86051, 86052, 86053, 86054, 86055, 86056, 86057, 86058, 86041, 86042, 86043, 86044, 86045, 86046, 86047, 86048, 86031, 86032, 86033, 86034, 86035, 86036, 86037, 86038, 86021, 86022, 86023, 86024, 86025, 86026, 86027, 86028, 86011, 86012, 86013, 86014, 86015, 86016, 86017, 86018, 86001, 86002, 86003, 86004, 86005, 86006, 86007, 86008, 85021, 85022, 85023, 85024, 85001, 85002, 85003, 85004, 85005, 85006, 85007, 85008, 85009, 85010, 85011, 85012, 85013, 85014, 85015, 85016, 85017, 85018, 72723, 50621, 72724, 55401, 55402, 55403, 55404, 55405, 55101, 55102, 55103, 55104, 55105, 55106, 55107, 55108, 55109, 55110, 55111, 55112, 55113, 55114, 55115, 55116, 55117, 55118, 55119, 55120, 55121, 55122, 55123, 71051, 71052, 95002, 55001, 55003, 55004, 55406, 55407, 55408, 55409, 55410, 55411, 72725, 72726, 72727, 71001, 71094, 76013, 76014, 25040, 70102, 71032, 71015, 71016, 71153, 27987, 72728, 72729, 72730, 25041, 27003, 27006, 27112, 27115, 50200, 50801, 50802, 50803, 50804, 50813, 50814, 50815, 50816, 50817, 50818, 50820, 70038, 25100, 71083, 71085, 71084, 71068, 79501, 91010, 91011]
		for i in xrange(len(notAllowedTargetRenderItemList)):
			if itemVnum == notAllowedTargetRenderItemList[i]:
				return
		
		if item.ITEM_TYPE_ARMOR == itemType and item.ARMOR_BODY == item.GetItemSubType():
			self.AppendTextLine("|Eemoji/key_shift|e + |Eemoji/key_rclick|e - Big Render Target")
			
		if item.ITEM_TYPE_WEAPON == itemType or item.ITEM_TYPE_COSTUME == itemType or item.COSTUME_TYPE_BODY == itemType or item.COSTUME_TYPE_HAIR == itemType or item.COSTUME_TYPE_WEAPON == itemType or item.COSTUME_TYPE_MOUNT == itemType:
			self.AppendTextLine("|Eemoji/key_shift|e + |Eemoji/key_rclick|e - Big Render Target")
		
		if itemVnum >= 33575 and itemVnum <= 33589:
			self.AppendTextLine("|Eemoji/key_shift|e + |Eemoji/key_rclick|e - Big Render Target")
		
		PetList = [22822, 22830, 22831, 22832, 22833, 22834, 22835, 22836, 22837, 55238, 55324, 55325, 55326, 55327, 55320, 55321, 55322, 55323, 78803, 57014, 34376, 34372, 55270, 55271, 55272, 55342, 53005, 53007, 57010, 57011, 57012, 57013, 34114, 34115, 53024, 53025, 53008, 53009, 57015, 57016]
		for i in xrange(len(PetList)):
			if itemVnum == PetList[i]:
				self.AppendTextLine("|Eemoji/key_shift|e + |Eemoji/key_rclick|e - Big Render Target")
				break

		#if itemCount > 1:
		#	if item.GetItemType() == 23 or itemVnum == 27987:
		#		self.AppendSpace(7) ##Platzhalter 
		#		self.AppendTextLine("|Eemoji/key_ctrl|e + |Eemoji/key_rclick|e - Open complete stack")
		
	if app.ENABLE_SEND_TARGET_INFO:
		def SetItemToolTipStone(self, itemVnum):
			self.itemVnum = itemVnum
			item.SelectItem(itemVnum)
			itemType = item.GetItemType()
			itemDesc = item.GetItemDescription()
			itemSummary = item.GetItemSummary()
			attrSlot = 0
			self.__AdjustMaxWidth(attrSlot, itemDesc)

			itemName = item.GetItemName()
			realName = itemName[:itemName.find("+")]
			self.SetTitle(realName + " +0 - +4")
			## Description ###
			self.AppendDescription(itemDesc, 26)
			self.AppendDescription(itemSummary, 26, self.CONDITION_COLOR)
			if item.ITEM_TYPE_METIN == itemType:
				self.AppendMetinInformation()
				self.AppendMetinWearInformation()
			for i in xrange(item.LIMIT_MAX_NUM):
				(limitType, limitValue) = item.GetLimit(i)
				if item.LIMIT_REAL_TIME_START_FIRST_USE == limitType:
					self.AppendRealTimeStartFirstUseLastTime(item, metinSlot, i)
				elif item.LIMIT_TIMER_BASED_ON_WEAR == limitType:
					self.AppendTimerBasedOnWearLastTime(metinSlot)
			self.ShowToolTip()
	def SetShopItem(self, slotIndex):
		itemVnum = shop.GetItemID(slotIndex)
		if 0 == itemVnum:
			return
		price = shop.GetItemPrice(slotIndex)
		self.ClearToolTip()
		self.isShopItem = TRUE
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(shop.GetItemMetinSocket(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(shop.GetItemAttribute(slotIndex, i))
		if app.ENABLE_CHANGELOOK_SYSTEM:
			transmutation = shop.GetItemTransmutation(slotIndex)
			if not transmutation:
				self.AddItemData(itemVnum, metinSlot, attrSlot)
			else:
				self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.INVENTORY, -1, transmutation)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
		if app.ENABLE_MULTISHOP:
			if shop.GetBuyWithItem(slotIndex) != 0:
				self.AppendPriceTextLine(shop.GetBuyWithItemCount(slotIndex), shop.GetBuyWithItem(slotIndex))
			else:
				self.AppendPrice(price)
		else:
			self.AppendPrice(price)
	def SetShopItemBySecondaryCoin(self, slotIndex):
		itemVnum = shop.GetItemID(slotIndex)
		if 0 == itemVnum:
			return
		price = shop.GetItemPrice(slotIndex)
		self.ClearToolTip()
		self.isShopItem = TRUE
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(shop.GetItemMetinSocket(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(shop.GetItemAttribute(slotIndex, i))
		if app.ENABLE_CHANGELOOK_SYSTEM:
			transmutation = shop.GetItemTransmutation(slotIndex)
			if not transmutation:
				self.AddItemData(itemVnum, metinSlot, attrSlot)
			else:
				self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.INVENTORY, -1, transmutation)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
		self.AppendPriceBySecondaryCoin(price)
	def SetExchangeOwnerItem(self, slotIndex):
		itemVnum = exchange.GetItemVnumFromSelf(slotIndex)
		if 0 == itemVnum:
			return
		self.ClearToolTip()
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(exchange.GetItemMetinSocketFromSelf(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(exchange.GetItemAttributeFromSelf(slotIndex, i))
		if app.ENABLE_CHANGELOOK_SYSTEM:
			transmutation = exchange.GetItemTransmutation(slotIndex, True)
			if not transmutation:
				self.AddItemData(itemVnum, metinSlot, attrSlot)
			else:
				self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.INVENTORY, -1, transmutation)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
	def SetExchangeTargetItem(self, slotIndex):
		itemVnum = exchange.GetItemVnumFromTarget(slotIndex)
		if 0 == itemVnum:
			return
		self.ClearToolTip()
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(exchange.GetItemMetinSocketFromTarget(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(exchange.GetItemAttributeFromTarget(slotIndex, i))
		if app.ENABLE_CHANGELOOK_SYSTEM:
			transmutation = exchange.GetItemTransmutation(slotIndex, False)
			if not transmutation:
				self.AddItemData(itemVnum, metinSlot, attrSlot)
			else:
				self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.INVENTORY, -1, transmutation)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
	def SetPrivateShopBuilderItem(self, invenType, invenPos, privateShopSlotIndex):
		itemVnum = player.GetItemIndex(invenType, invenPos)
		if 0 == itemVnum:
			return
		item.SelectItem(itemVnum)
		self.ClearToolTip()
		self.AppendSellingPrice(shop.GetPrivateShopItemPrice(invenType, invenPos))
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(invenPos, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(player.GetItemAttribute(invenPos, i))
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, invenType, invenPos)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0)
	def SetEditPrivateShopItem(self, invenType, invenPos, price):
		itemVnum = player.GetItemIndex(invenType, invenPos)
		if 0 == itemVnum:
			return
		item.SelectItem(itemVnum)
		self.ClearToolTip()
		self.AppendSellingPrice(price)
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(player.GetItemMetinSocket(invenPos, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(player.GetItemAttribute(invenPos, i))
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, invenType, invenPos)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0)
	def SetSafeBoxItem(self, slotIndex):
		itemVnum = safebox.GetItemID(slotIndex)
		if 0 == itemVnum:
			return
		self.ClearToolTip()
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(safebox.GetItemMetinSocket(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(safebox.GetItemAttribute(slotIndex, i))

		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, safebox.GetItemFlags(slotIndex), player.SAFEBOX, slotIndex, preview=0)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot, safebox.GetItemFlags(slotIndex), preview=0)
	def SetMallItem(self, slotIndex):
		itemVnum = safebox.GetMallItemID(slotIndex)
		if 0 == itemVnum:
			return
		self.ClearToolTip()
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(safebox.GetMallItemMetinSocket(slotIndex, i))
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append(safebox.GetMallItemAttribute(slotIndex, i))
		if app.ENABLE_CHANGELOOK_SYSTEM:
			self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.MALL, slotIndex)
		else:
			self.AddItemData(itemVnum, metinSlot, attrSlot)
	def SetItemToolTip(self, itemVnum):
		self.ClearToolTip()
		metinSlot = []
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlot.append(0)
		attrSlot = []
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			attrSlot.append((0, 0))
		self.AddItemData(itemVnum, metinSlot, attrSlot)
	def __AppendAttackSpeedInfo(self, item):
		atkSpd = item.GetValue(0)
		if atkSpd < 80:
			stSpd = localeInfo.TOOLTIP_ITEM_VERY_FAST
		elif atkSpd <= 95:
			stSpd = localeInfo.TOOLTIP_ITEM_FAST
		elif atkSpd <= 105:
			stSpd = localeInfo.TOOLTIP_ITEM_NORMAL
		elif atkSpd <= 120:
			stSpd = localeInfo.TOOLTIP_ITEM_SLOW
		else:
			stSpd = localeInfo.TOOLTIP_ITEM_VERY_SLOW
		self.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_SPEED % stSpd, self.NORMAL_COLOR)
	def __AppendAttackGradeInfo(self):
		atkGrade = item.GetValue(1)
		self.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_GRADE % atkGrade, self.GetChangeTextLineColor(atkGrade))
	def AppendItemIcon(self, itemVnum):
		itemImage = ui.ImageBox()
		itemImage.SetParent(self)
		itemImage.Show()
		itemImage.LoadImage(itemVnum)#item.GetIconImageFileName())
		itemImage.SetPosition((self.toolTipWidth/2), self.toolTipHeight)#- itemImage.GetWidth()/2
		self.toolTipHeight += itemImage.GetHeight()
		self.childrenList.append(itemImage)
		self.ResizeToolTip()

	if app.ENABLE_SASH_SYSTEM:
		def CalcSashValue(self, value, abs):
			if not value:
				return 0
			valueCalc = int((round(value * abs) / 100) - .5) + int(int((round(value * abs) / 100) - .5) > 0)
			if valueCalc <= 0 and value > 0:
				value = 1
			else:
				value = valueCalc
			return value
	def __AppendAttackPowerInfo(self, itemAbsChance = 0):
		minPower = item.GetValue(3)
		maxPower = item.GetValue(4)
		addPower = item.GetValue(5)

		if app.ENABLE_SASH_SYSTEM:
			if itemAbsChance:
				minPower = self.CalcSashValue(minPower, itemAbsChance)
				maxPower = self.CalcSashValue(maxPower, itemAbsChance)
				addPower = self.CalcSashValue(addPower, itemAbsChance)

		if maxPower > minPower:
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_POWER % (minPower + addPower, maxPower + addPower), self.POSITIVE_COLOR)
		else:
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_ATT_POWER_ONE_ARG % (minPower + addPower), self.POSITIVE_COLOR)
	def __AppendMagicAttackInfo(self, itemAbsChance = 0):
		minMagicAttackPower = item.GetValue(1)
		maxMagicAttackPower = item.GetValue(2)
		addPower = item.GetValue(5)

		if app.ENABLE_SASH_SYSTEM:
			if itemAbsChance:
				minMagicAttackPower = self.CalcSashValue(minMagicAttackPower, itemAbsChance)
				maxMagicAttackPower = self.CalcSashValue(maxMagicAttackPower, itemAbsChance)
				addPower = self.CalcSashValue(addPower, itemAbsChance)

		if minMagicAttackPower > 0 or maxMagicAttackPower > 0:
			if maxMagicAttackPower > minMagicAttackPower:
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_ATT_POWER % (minMagicAttackPower + addPower, maxMagicAttackPower + addPower), self.POSITIVE_COLOR)
			else:
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_ATT_POWER_ONE_ARG % (minMagicAttackPower + addPower), self.POSITIVE_COLOR)
	def __AppendMagicDefenceInfo(self, itemAbsChance = 0):
		magicDefencePower = item.GetValue(0)

		if app.ENABLE_SASH_SYSTEM:
			if itemAbsChance:
				magicDefencePower = self.CalcSashValue(magicDefencePower, itemAbsChance)

		if magicDefencePower > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_MAGIC_DEF_POWER % magicDefencePower, self.GetChangeTextLineColor(magicDefencePower))
	def __AppendAttributeInformation(self, attrSlot, itemAbsChance = 0):
		if 0 != attrSlot:
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				type = attrSlot[i][0]
				value = attrSlot[i][1]
				if 0 == value:
					continue

				affectString = self.__GetAffectString(type, value)
				if app.ENABLE_SASH_SYSTEM:
					if item.GetItemType() == item.ITEM_TYPE_COSTUME and item.GetItemSubType() == item.COSTUME_TYPE_SASH and itemAbsChance:
						value = self.CalcSashValue(value, itemAbsChance)
						affectString = self.__GetAffectString(type, value)

				if affectString:
					affectColor = self.__GetAttributeColor(i, value)
					self.AppendTextLine(affectString, affectColor)
	def __GetAttributeColor(self, index, value):
		if value > 0:
			if index >= 5:
				return self.SPECIAL_POSITIVE_COLOR2
			else:
				return self.SPECIAL_POSITIVE_COLOR
		elif value == 0:
			return self.NORMAL_COLOR
		else:
			return self.NEGATIVE_COLOR
	def __IsPolymorphItem(self, itemVnum):
		if itemVnum >= 70103 and itemVnum <= 70106:
			return 1
		return 0
	def __SetPolymorphItemTitle(self, monsterVnum):
		if localeInfo.IsVIETNAM():
			itemName =item.GetItemName()
			itemName+=" "
			itemName+=nonplayer.GetMonsterName(monsterVnum)
		else:
			itemName =nonplayer.GetMonsterName(monsterVnum)
			itemName+=" "
			itemName+=item.GetItemName()
		self.SetTitle(itemName)
	def __SetNormalItemTitle(self):
		if app.ENABLE_SEND_TARGET_INFO:
			if self.isStone:
				itemName = item.GetItemName()
				realName = itemName[:itemName.find("+")]
				self.SetTitle(realName + " +0 - +4")
			else:
				self.SetTitle(item.GetItemName())
		else:
			self.SetTitle(item.GetItemName())
	def __SetSpecialItemTitle(self):
		self.AppendTextLine(item.GetItemName(), self.SPECIAL_TITLE_COLOR)
	def __SetItemTitle(self, itemVnum, metinSlot, attrSlot):
		if localeInfo.IsCANADA():
			if 72726 == itemVnum or 72730 == itemVnum:
				self.AppendTextLine(item.GetItemName(), grp.GenerateColor(1.0, 0.7843, 0.0, 1.0))
				return

		if self.__IsPolymorphItem(itemVnum):
			self.__SetPolymorphItemTitle(metinSlot[0])
		else:
			if self.__IsAttr(attrSlot):
				self.__SetSpecialItemTitle()
				return
			self.__SetNormalItemTitle()
	def __IsAttr(self, attrSlot):
		if not attrSlot:
			return FALSE
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			type = attrSlot[i][0]
			if 0 != type:
				return TRUE
		return FALSE

	def AddRefineItemData(self, itemVnum, metinSlot, attrSlot = 0):
		for i in xrange(player.METIN_SOCKET_MAX_NUM):
			metinSlotData=metinSlot[i]
			if self.GetMetinItemIndex(metinSlotData) == constInfo.ERROR_METIN_STONE:
				metinSlot[i]=player.METIN_SOCKET_TYPE_SILVER
		self.AddItemData(itemVnum, metinSlot, attrSlot, preview=0)
	
	def AddItemData_Offline(self, itemVnum, itemDesc, itemSummary, metinSlot, attrSlot):
		self.__AdjustMaxWidth(attrSlot, itemDesc)
		self.__SetItemTitle(itemVnum, metinSlot, attrSlot)

		if self.__IsHair(itemVnum):	
			self.__AppendHairIcon(itemVnum)
		### Description ###
		self.AppendDescription(itemDesc, 26)
		self.AppendDescription(itemSummary, 26, self.CONDITION_COLOR)
	# def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, flags = 0, unbindTime = 0):

	def AddItemData(self, itemVnum, metinSlot, attrSlot = 0, flags = 0, window_type = player.INVENTORY, slotIndex = -1, transmutation = -1, preview = 1):
		self.itemVnum = itemVnum
		item.SelectItem(itemVnum)
		itemType = item.GetItemType()
		itemSubType = item.GetItemSubType()
		self.__ModelPreviewClose()
		
		if preview:
			if item.ITEM_TYPE_UNIQUE == itemType or item.ITEM_TYPE_QUEST == itemType:
				petItems = [22822, 22830, 22831, 22832, 22833, 22834, 22835, 22836, 22837, 55238, 55324, 55325, 55326, 55327, 55270, 55271, 55272, 55320, 55321, 55322, 55323, 57014, 57015, 53001, 57010, 57011, 57012, 57013, 53002, 33570, 33571, 33572, 33573, 33574, 55340, 55341, 55342, 33575, 33576, 55260, 33577, 33578, 33579, 33580, 33581, 33582, 33583, 33584, 53003, 53004, 53005, 53006, 53007, 53008, 53009, 53010, 53011, 53012, 53013, 53014, 53015, 53016, 53017, 53018, 53019, 53020, 53021, 53022, 53023, 53024, 53025, 34020, 34021, 34022, 34023, 34032, 34033, 34034, 34035, 34037, 34038, 34039, 34040, 34041, 34042, 34043, 34044, 34045, 33507, 33508, 33514, 33515, 53223, 53224, 53225, 50267, 34114, 34366, 34115, 34116, 78803, 34014, 34371, 34372, 34369, 34370, 34373, 34374, 34375, 34376]
				
				if itemVnum in petItems:
					self.__ModelPreview(itemVnum, 0, item.GetValue(3), window_type, transmutation, slotIndex) #in DB Value3 die Vnum des Model eintragen!

		if 50026 == itemVnum:
			if 0 != metinSlot:
				name = item.GetItemName()
				if metinSlot[0] > 0:
					name += " "
					name += localeInfo.NumberToMoneyString(metinSlot[0])
				self.SetTitle(name)
				self.ShowToolTip()
			return
			
		if app.ENABLE_VIP_SYSTEM and item.ITEM_TYPE_VIP == itemType:
			title = item.GetItemName() + " (" + localeInfo.SecondToDHM(metinSlot[0]) + ")"
			self.SetTitle(title)
			self.AppendDescription(item.GetItemDescription(), 26, self.CONDITION_COLOR)
			self.ShowToolTip()
			return
			
		### Skill Book ###
		if app.ENABLE_SEND_TARGET_INFO:
			if 50300 == itemVnum and not self.isBook:
				if 0 != metinSlot and not self.isBook:
					self.__SetSkillBookToolTip(metinSlot[0], localeInfo.TOOLTIP_SKILLBOOK_NAME, 1)
					self.ShowToolTip()
				elif self.isBook:
					self.SetTitle(item.GetItemName())
					self.AppendDescription(item.GetItemDescription(), 26)
					self.AppendDescription(item.GetItemSummary(), 26, self.CONDITION_COLOR)
					self.ShowToolTip()					
				return
			elif 70037 == itemVnum :
				if 0 != metinSlot and not self.isBook2:
					self.__SetSkillBookToolTip(metinSlot[0], localeInfo.TOOLTIP_SKILL_FORGET_BOOK_NAME, 0)
					self.AppendDescription(item.GetItemDescription(), 26)
					self.AppendDescription(item.GetItemSummary(), 26, self.CONDITION_COLOR)
					self.ShowToolTip()
				elif self.isBook2:
					self.SetTitle(item.GetItemName())
					self.AppendDescription(item.GetItemDescription(), 26)
					self.AppendDescription(item.GetItemSummary(), 26, self.CONDITION_COLOR)
					self.ShowToolTip()					
				return
			elif 70055 == itemVnum:
				if 0 != metinSlot:
					self.__SetSkillBookToolTip(metinSlot[0], localeInfo.TOOLTIP_SKILL_FORGET_BOOK_NAME, 0)
					self.AppendDescription(item.GetItemDescription(), 26)
					self.AppendDescription(item.GetItemSummary(), 26, self.CONDITION_COLOR)
					self.ShowToolTip()
				return
			if app.LWT_BUFF_UPDATE:
				if 92010 == itemVnum or 92011 == itemVnum and not self.isBook:
					if 0 != metinSlot and not self.isBook:
						self.__SetSkillBookToolTip(metinSlot[0], item.GetItemName(), 0)
						self.AppendDescription(item.GetItemDescription(), 26)
						self.AppendDescription(item.GetItemSummary(), 26, self.CONDITION_COLOR)
						self.ShowToolTip()
		else:
			if 50300 == itemVnum:
				if 0 != metinSlot:
					self.__SetSkillBookToolTip(metinSlot[0], localeInfo.TOOLTIP_SKILLBOOK_NAME, 1)
					self.ShowToolTip()
				return
			elif 70037 == itemVnum:
				if 0 != metinSlot:
					self.__SetSkillBookToolTip(metinSlot[0], localeInfo.TOOLTIP_SKILL_FORGET_BOOK_NAME, 0)
					self.AppendDescription(item.GetItemDescription(), 26)
					self.AppendDescription(item.GetItemSummary(), 26, self.CONDITION_COLOR)
					self.ShowToolTip()
				return
			elif 70055 == itemVnum:
				if 0 != metinSlot:
					self.__SetSkillBookToolTip(metinSlot[0], localeInfo.TOOLTIP_SKILL_FORGET_BOOK_NAME, 0)
					self.AppendDescription(item.GetItemDescription(), 26)
					self.AppendDescription(item.GetItemSummary(), 26, self.CONDITION_COLOR)
					self.ShowToolTip()
				return
		###########################################################################################
		itemDesc = item.GetItemDescription()
		itemSummary = item.GetItemSummary()
		isCostumeItem = 0
		isCostumeHair = 0
		isCostumeBody = 0
		if app.ENABLE_SASH_SYSTEM:
			isCostumeSash = 0
		isCostumeMount = 0

		if app.ENABLE_NEW_PET_SYSTEM:
			pet_evoname = [localeInfo.PET_INFORMATION_STAGE1, localeInfo.PET_INFORMATION_STAGE2, localeInfo.PET_INFORMATION_STAGE3, localeInfo.PET_INFORMATION_STAGE4]
			if itemVnum >= 55701 and itemVnum <= 55799:
				self.__AdjustMaxWidth(attrSlot, itemDesc)
				self.__SetItemTitle(itemVnum, 0, 0)
				self.AppendDescription(itemDesc, 26)
				self.AppendDescription(itemSummary, 26, self.CONDITION_COLOR)
				self.AppendSpace(5)

				LifeTime = int(app.GetGlobalTimeStamp() - metinSlot[2])
					
				if LifeTime < 0:
					LifeTime = int(metinSlot[2] - app.GetGlobalTimeStamp())

				# import chat
				#chat.AppendChat(chat.CHAT_TYPE_INFO, "MetinLen : %d" % int(metinSlot[5]))
				self.AppendTextLine(pet_evoname[int(metinSlot[5])], self.NORMAL_COLOR)
				self.AppendTextLine(uiScriptLocale.PET_INFORMATION_LEVEL+" "+str(metinSlot[4])+" ("+localeInfo.SecondToPetLifeTime(int(LifeTime))+")", self.NORMAL_COLOR)
				self.AppendTextLine(uiScriptLocale.PET_INFORMATION_HP+" +"+pointop(str(attrSlot[0][1]))+"%", self.SPECIAL_POSITIVE_COLOR)
				self.AppendTextLine(uiScriptLocale.PET_INFORMATION_ATT+" +"+pointop(str(attrSlot[1][1]))+"%", self.SPECIAL_POSITIVE_COLOR)
				self.AppendTextLine(uiScriptLocale.PET_INFORMATION_DEFENCE+" +"+pointop(str(attrSlot[2][1]))+"%", self.SPECIAL_POSITIVE_COLOR)
				self.AppendSpace(5)
				if attrSlot[3][1] != -1 or attrSlot[4][1] != -1 or attrSlot[5][1] != -1:
					self.AppendTextLine("Skills", self.SPECIAL_TITLE_COLOR)
				if attrSlot[3][1] != -1:
					if attrSlot[3][1] == 0:
						self.AppendTextLine(self.PET_SKILL_NAMES[attrSlot[3][1]], self.MIDDLE_PRICE_COLOR)
					else:
						self.AppendTextLine(self.PET_SKILL_NAMES[attrSlot[3][1]]+" (Lv."+str(attrSlot[3][0])+")", self.MIDDLE_PRICE_COLOR)
					
				if attrSlot[4][1] != -1:
					if attrSlot[4][1] == 0:
						self.AppendTextLine(self.PET_SKILL_NAMES[attrSlot[4][1]], self.MIDDLE_PRICE_COLOR)
					else:
						self.AppendTextLine(self.PET_SKILL_NAMES[attrSlot[4][1]]+" (Lv."+str(attrSlot[4][0])+")", self.MIDDLE_PRICE_COLOR)
				if attrSlot[5][1] != -1:
					if attrSlot[5][1] == 0:
						self.AppendTextLine(self.PET_SKILL_NAMES[attrSlot[5][1]], self.MIDDLE_PRICE_COLOR)
					else:
						self.AppendTextLine(self.PET_SKILL_NAMES[attrSlot[5][1]]+" (Lv."+str(attrSlot[5][0])+")", self.MIDDLE_PRICE_COLOR)
						
				self.AppendMallItemLastTime(metinSlot[1])
				self.ShowToolTip()
				return
			
			#Transportbox mit Pet
			if itemVnum == 55002:
				self.__AdjustMaxWidth(attrSlot, itemDesc)
				self.__SetItemTitle(itemVnum, 0, 0)
				if metinSlot[0] == 0:
					self.AppendDescription(itemDesc, 26)
					self.AppendDescription(itemSummary, 26, self.CONDITION_COLOR)
				else:
					self.AppendSpace(5)
					if metinSlot[0] >= 55701 and metinSlot[0] <= 55799:
						item.SelectItem(metinSlot[0])
						self.AppendTextLine(item.GetItemName(), self.SPECIAL_POSITIVE_COLOR)
						self.AppendSpace(5)

					AgeTime = int(metinSlot[2] / 60 / 60 / 24)

					self.AppendTextLine(pet_evoname[int(attrSlot[1][0])], self.NORMAL_COLOR)
					self.AppendTextLine(uiScriptLocale.PET_INFORMATION_LEVEL+" "+str(attrSlot[0][0])+" ("+str(AgeTime) + localeInfo.DAY+")", self.NORMAL_COLOR)
					self.AppendTextLine(uiScriptLocale.PET_INFORMATION_LIFE+": "+localeInfo.SecondToPetLifeTime(int(metinSlot[1]))+" / "+localeInfo.SecondToPetLifeTime(int(metinSlot[3])), self.NORMAL_COLOR)
					self.AppendSpace(5)
					self.AppendTextLine(uiScriptLocale.PET_INFORMATION_HP+" +"+pointop(str(attrSlot[0][1]))+"%", self.CONDITION_COLOR)
					self.AppendTextLine(uiScriptLocale.PET_INFORMATION_ATT+" +"+pointop(str(attrSlot[1][1]))+"%", self.CONDITION_COLOR)
					self.AppendTextLine(uiScriptLocale.PET_INFORMATION_DEFENCE+" +"+pointop(str(attrSlot[2][1]))+"%", self.CONDITION_COLOR)
					if attrSlot[3][1] != -1 or attrSlot[4][1] != -1 or attrSlot[5][1] != -1:
						self.AppendTextLine("__________________", self.CONDITION_COLOR)
						self.AppendSpace(5)
						self.AppendTextLine(uiScriptLocale.PET_INFORMATION_SKILL, self.NORMAL_COLOR)
					if attrSlot[3][1] != -1:
						if attrSlot[3][1] == 0:
							self.AppendTextLine(self.PET_SKILL_NAMES[attrSlot[3][1]], self.CONDITION_COLOR)
						else:
							self.AppendTextLine(self.PET_SKILL_NAMES[attrSlot[3][1]]+" (Lv."+str(attrSlot[3][0])+")", self.CONDITION_COLOR)
						
					if attrSlot[4][1] != -1:
						if attrSlot[4][1] == 0:
							self.AppendTextLine(self.PET_SKILL_NAMES[attrSlot[4][1]], self.CONDITION_COLOR)
						else:
							self.AppendTextLine(self.PET_SKILL_NAMES[attrSlot[4][1]]+" (Lv."+str(attrSlot[4][0])+")", self.CONDITION_COLOR)
					if attrSlot[5][1] != -1:
						if attrSlot[5][1] == 0:
							self.AppendTextLine(self.PET_SKILL_NAMES[attrSlot[5][1]], self.CONDITION_COLOR)
						else:
							self.AppendTextLine(self.PET_SKILL_NAMES[attrSlot[5][1]]+" (Lv."+str(attrSlot[5][0])+")", self.CONDITION_COLOR)
						self.AppendSpace(5)
		
					self.AppendTextLine("__________________", self.CONDITION_COLOR)
					self.AppendMallItemLastTime(metinSlot[5])
				self.ShowToolTip()
				return

		if app.ENABLE_COSTUME_SYSTEM:
			if item.ITEM_TYPE_COSTUME == itemType:
				isCostumeItem = 1
				isCostumeHair = item.COSTUME_TYPE_HAIR == itemSubType
				isCostumeBody = item.COSTUME_TYPE_BODY == itemSubType
				if app.ENABLE_SASH_SYSTEM:
					isCostumeSash = itemSubType == item.COSTUME_TYPE_SASH
				isCostumeMount = item.COSTUME_TYPE_MOUNT == itemSubType

				#dbg.TraceError("IS_COSTUME_ITEM! body(%d) hair(%d)" % (isCostumeBody, isCostumeHair))
		self.__AdjustMaxWidth(attrSlot, itemDesc)
		self.__SetItemTitle(itemVnum, metinSlot, attrSlot)

		vnum_1 = 53090
		vnum_2 = 53091
		vnum_3 = 53092
		if vnum_1 == itemVnum or vnum_2 == itemVnum or vnum_3 == itemVnum:
			color = self.FONT_COLOR
			value = int(metinSlot[0])
			name = "Dito System"
			
			if vnum_1 == itemVnum:
				color = grp.GenerateColor(0.0, 0.80, 0.0, 1.0)
				value = 10
				
			elif vnum_2 == itemVnum:
				color = grp.GenerateColor(0.0, 0.80, 0.0, 1.0)
				value = 30
				
			elif vnum_3 == itemVnum:
				color = grp.GenerateColor(0.0, 0.80, 0.0, 1.0)
				value = 70
			
			self.AppendDescription(item.GetItemDescription(), 26) 
			self.TextLine = self.SetTitle(name)
			#if self.__IsAttr(attrSlot):
			#	self.TextLine.SetPackedFontColor(HIGH_PRICE_COLOR)
			#else:
			#	self.TextLine.SetPackedFontColor(self.FONT_COLOR)
				
			self.AutoAppendTextLine("Dito Power: %d" % (value), color)
			self.AppendMallItemLastTime(metinSlot[0])
			self.ResizeToolTip()
			self.ShowToolTip()
			return
		
		
		### Hair Preview Image ###
		if self.__IsHair(itemVnum):	
			self.__AppendHairIcon(itemVnum)
		if chr.IsGameMaster(player.GetMainCharacterIndex()):
			self.AppendTextLine(localeInfo.ITEM_VNUM_TOOLTIP % (int(itemVnum)), self.ITEMVNUM_COLOR)
		### Description ###
		self.AppendDescription(itemDesc, 26)
		self.AppendDescription(itemSummary, 26, self.CONDITION_COLOR)

		if item.ITEM_TYPE_SHINING == itemType:

			aRarityWeapons = {60276: 0, 60277: 0, 60278: 0, 60279: 0, 60260: 1, 60263: 1, 60264: 1, 60267: 2, 60268: 2, 60270: 3}
			aRarityArmors = {60239: 0, 60240: 0, 60241: 0, 60242: 0, 60234: 1, 60236: 1, 60247: 1, 60244: 2, 60246: 2, 60231: 3}
			aRaritySepcials = {65205: 4, 65206: 4, 65207: 4, 65208: 4, 65209: 4, 65210: 4, 65211: 4, 65212: 4, 65213: 4, 65214: 4, 65215: 4, 65216: 4, 65217: 4, 65218: 4, 65219: 4, 65220: 4, 65221: 4, 65222: 4, 65223: 4, 65224: 4}
            
			aRarityNames = ["Common", "Uncommon", "Rare", "Very Rare", "Legendary"]
			aRarityColors = [0xff8099ff, 0xff6ffb86, 0xfffa6ffb, 0xffff3c33, 0xfffec901]
            
			GetColor = item.GetValue(0)
			SlotInfo = ["Shining-Weapon", "Shining-Armor", "Shining-Wing"]
			self.AppendTextLine("An item that gives you glamour.", self.CONDITION_COLOR)
			self.AppendTextLine("Equippable : [%s]" % SlotInfo[itemSubType],self.CHANGELOOK_ITEMNAME_COLOR )
            
			if itemSubType == item.SHINING_WEAPON:
				if itemVnum in aRarityWeapons.keys():
					self.AppendTextLine("[%s]" % aRarityNames[aRarityWeapons[itemVnum]], aRarityColors[aRarityWeapons[itemVnum]] )
			elif itemSubType == item.SHINING_ARMOR:
				if itemVnum in aRarityArmors.keys():
					self.AppendTextLine("[%s]" % aRarityNames[aRarityArmors[itemVnum]], aRarityColors[aRarityArmors[itemVnum]] )
			elif itemSubType == item.SHINING_SPECIAL:
				if itemVnum in aRaritySepcials.keys():
					self.AppendTextLine("[%s]" % aRarityNames[aRaritySepcials[itemVnum]], aRarityColors[aRaritySepcials[itemVnum]] )
			
			self.AppendSpace(7) ##Platzhalter
			if preview != 0:
				if itemSubType == item.SHINING_WEAPON:
					table = shiningnames.WEAPON[GetColor]
					self.__ModelPreview(itemVnum, 5, player.GetRace(), window_type, transmutation, slotIndex)
				elif itemSubType == item.SHINING_ARMOR:
					table = shiningnames.ARMOR[GetColor]
					self.__ModelPreview(itemVnum, 6, player.GetRace(), window_type, transmutation, slotIndex)
				elif itemSubType == item.SHINING_SPECIAL:
					table = shiningnames.SPEZIAL[GetColor]
					self.__ModelPreview(itemVnum, 7, player.GetRace(), window_type, transmutation, slotIndex)

			# self.AppendTextLine("%s" % table,self.TYRANIS_TOOLTIP_COLOR)
			self.__AppendLimitInformation()

		elif app.ENABLE_SKILL_COSTUME_SYSTEM and item.ITEM_TYPE_SKILL_COSTUME == itemType:
			self.__ModelPreview(itemVnum, 8, player.GetRace(), window_type, transmutation, slotIndex)
		### Weapon ###
		elif item.ITEM_TYPE_WEAPON == itemType:
			if constInfo.BUFFI_GUI == True:
				return
			self.__AppendLimitInformation()
			self.AppendSpace(5)
			## ºIA¤AI °æ¿i ¸¶°øA≫ ¸OAu C￥½ACN´U.
			if item.WEAPON_FAN == itemSubType:
				self.__AppendMagicAttackInfo()
				self.__AppendAttackPowerInfo()
			else:
				self.__AppendAttackPowerInfo()
				self.__AppendMagicAttackInfo()
			self.__AppendAffectInformation()
			self.__AppendAttributeInformation(attrSlot)
			if app.ENABLE_CHANGELOOK_SYSTEM:
				self.AppendTransmutation(window_type, slotIndex, transmutation)
			self.AppendWearableInformation()
			if itemVnum != 79501:
				self.__AppendMetinSlotInfo(metinSlot)
				
			if preview != 0:
				if item.WEAPON_SWORD == itemSubType: 
					if player.GetRace() != 7 and player.GetRace() != 3:
						self.__ModelPreview(itemVnum, 3, player.GetRace(), window_type, transmutation, slotIndex)
				if item.WEAPON_DAGGER == itemSubType or item.WEAPON_BOW == itemSubType: 
					if player.GetRace() == 5 or player.GetRace() == 1:
						self.__ModelPreview(itemVnum, 3, player.GetRace(), window_type, transmutation, slotIndex)
				if item.WEAPON_TWO_HANDED == itemSubType: 
					if player.GetRace() == 0 or player.GetRace() == 4:
						self.__ModelPreview(itemVnum, 3, player.GetRace(), window_type, transmutation, slotIndex)		
				if item.WEAPON_BELL == itemSubType or item.WEAPON_FAN == itemSubType: 
					if player.GetRace() == 7 or player.GetRace() == 3:
						self.__ModelPreview(itemVnum, 3, player.GetRace(), window_type, transmutation, slotIndex)
		### Armor ###
		elif item.ITEM_TYPE_ARMOR == itemType:
			self.__AppendLimitInformation()
			if constInfo.BUFFI_GUI == True:
				return
			## ¹æ¾i·A
			defGrade = item.GetValue(1)
			defBonus = item.GetValue(5)*2 ## ¹æ¾i·A C￥½A Aß¸ø μC´A ¹®A|¸| ¼oA¤
			if defGrade > 0:
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_DEF_GRADE % (defGrade+defBonus), self.GetChangeTextLineColor(defGrade))
			self.__AppendMagicDefenceInfo()
			self.__AppendAffectInformation()
			self.__AppendAttributeInformation(attrSlot)
			if preview != 0 and itemSubType == 0:
				if self.__ItemGetRace() == player.GetRace() or self.__ItemGetRace() == 3 and player.GetRace() == 7: 
					self.__ModelPreview(itemVnum, 2, player.GetRace(), window_type, transmutation, slotIndex)	
				if self.__ItemGetRace() == player.GetRace() or self.__ItemGetRace() == 1 and player.GetRace() == 5: 
					self.__ModelPreview(itemVnum, 2, player.GetRace(), window_type, transmutation, slotIndex)
				if self.__ItemGetRace() == player.GetRace() or self.__ItemGetRace() == 0 and player.GetRace() == 4: 
					self.__ModelPreview(itemVnum, 2, player.GetRace(), window_type, transmutation, slotIndex)
				else:
					self.__ModelPreview(itemVnum, 2, player.GetRace(), window_type, transmutation, slotIndex)	
					
			if app.ENABLE_CHANGELOOK_SYSTEM:				
				self.AppendTransmutation(window_type, slotIndex, transmutation)
			self.AppendWearableInformation()
			if itemSubType in (item.ARMOR_WRIST, item.ARMOR_NECK, item.ARMOR_EAR):				
				self.__AppendAccessoryMetinSlotInfo(metinSlot, constInfo.GET_ACCESSORY_MATERIAL_VNUM(itemVnum, itemSubType))
			else:
				self.__AppendMetinSlotInfo(metinSlot)
		### Ring Slot Item (Not UNIQUE) ###
		elif item.ITEM_TYPE_RING == itemType:
			self.__AppendLimitInformation()
			self.__AppendAffectInformation()
			self.__AppendAttributeInformation(attrSlot)
			#¹YAo ¼OAI ½A½ºAU °u·ACØ¼± ¾ÆA÷ ±aE¹ ¹IA¤
			#self.__AppendAccessoryMetinSlotInfo(metinSlot, 99001)
			bHasRealtimeFlag = 0
			for i in xrange(item.LIMIT_MAX_NUM):
				(limitType, limitValue) = item.GetLimit(i)
				if item.LIMIT_REAL_TIME == limitType:
					bHasRealtimeFlag = 1

			if bHasRealtimeFlag == 1:
				self.AppendMallItemLastTime(metinSlot[0])

		### Belt Item ###
		elif item.ITEM_TYPE_BELT == itemType:
			self.__AppendLimitInformation()
			self.__AppendAffectInformation()
			self.__AppendAttributeInformation(attrSlot)
			self.__AppendAccessoryMetinSlotInfo(metinSlot, constInfo.GET_BELT_MATERIAL_VNUM(itemVnum))
		## AU½ºAo ¾ÆAIAU ##
		elif 0 != isCostumeItem:
			if constInfo.BUFFI_GUI == True:
				return
			self.__AppendLimitInformation()
			
			if preview != 0:
				if itemSubType == 0: #body
					if self.__ItemGetRace() == player.GetRace():
						self.__ModelPreview(itemVnum, 2, player.GetRace(), window_type, transmutation, slotIndex)
					
				elif itemSubType == 1: #Hair 
					if item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR) == False and (player.GetRace() == 4 or player.GetRace() == 0):
						if(item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and chr.RaceToSex(player.GetRace()) == 0):
							self.__ModelPreview(item.GetValue(3), 1, player.GetRace(), window_type, transmutation, slotIndex)
						if(item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and chr.RaceToSex(player.GetRace()) == 1):
							self.__ModelPreview(item.GetValue(3), 1, player.GetRace(), window_type, transmutation, slotIndex)
					elif item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN) == False and (player.GetRace() == 5 or player.GetRace() == 1):
						if(item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and chr.RaceToSex(player.GetRace()) == 0):
							self.__ModelPreview(item.GetValue(3), 1, player.GetRace(), window_type, transmutation, slotIndex)
						if(item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and chr.RaceToSex(player.GetRace()) == 1):
							self.__ModelPreview(item.GetValue(3), 1, player.GetRace(), window_type, transmutation, slotIndex)
					elif item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA) == False and (player.GetRace() == 2 or player.GetRace() == 6):
						if(item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and chr.RaceToSex(player.GetRace()) == 0):
							self.__ModelPreview(item.GetValue(3), 1, player.GetRace(), window_type, transmutation, slotIndex)
						if(item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and chr.RaceToSex(player.GetRace()) == 1):
							self.__ModelPreview(item.GetValue(3), 1, player.GetRace(), window_type, transmutation, slotIndex)
					elif item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN) == False and (player.GetRace() == 7 or player.GetRace() == 3):
						if(item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and chr.RaceToSex(player.GetRace()) == 0):
							self.__ModelPreview(item.GetValue(3), 1, player.GetRace(), window_type, transmutation, slotIndex)
						if(item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and chr.RaceToSex(player.GetRace()) == 1):
							self.__ModelPreview(item.GetValue(3), 1, player.GetRace(), window_type, transmutation, slotIndex)
					else:
						if(item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and chr.RaceToSex(player.GetRace()) == 0):
							self.__ModelPreview(item.GetValue(3), 1, player.GetRace(), window_type, transmutation, slotIndex)
						if(item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and chr.RaceToSex(player.GetRace()) == 1):
							self.__ModelPreview(item.GetValue(3), 1, player.GetRace(), window_type, transmutation, slotIndex)
				elif itemSubType == 3: #weapon	
					if player.GetRace() != 7 and player.GetRace() != 3:
						self.__ModelPreview(itemVnum, 3, player.GetRace(), window_type, transmutation, slotIndex)
					if player.GetRace() == 5 or player.GetRace() == 1:
						self.__ModelPreview(itemVnum, 3, player.GetRace(), window_type, transmutation, slotIndex)
					if player.GetRace() == 0 or player.GetRace() == 4:
						self.__ModelPreview(itemVnum, 3, player.GetRace(), window_type, transmutation, slotIndex)		
					if player.GetRace() == 7 or player.GetRace() == 3:
						self.__ModelPreview(itemVnum, 3, player.GetRace(), window_type, transmutation, slotIndex)

			if isCostumeMount:
				self.__ModelPreview(itemVnum, 0, item.GetValue(3), window_type, transmutation, slotIndex)
					

			if app.ENABLE_SASH_SYSTEM:
				if isCostumeSash:
					## ABSORPTION RATE
					absChance = int(metinSlot[sash.ABSORPTION_SOCKET])
					self.AppendTextLine(localeInfo.SASH_ABSORB_CHANCE % (absChance), self.CONDITION_COLOR)
					## END ABSOPRTION RATE

					itemAbsorbedVnum = int(metinSlot[sash.ABSORBED_SOCKET])
					if itemAbsorbedVnum:
						## ATTACK / DEFENCE
						item.SelectItem(itemAbsorbedVnum)
						if item.GetItemType() == item.ITEM_TYPE_WEAPON:
							if item.GetItemSubType() == item.WEAPON_FAN:
								self.__AppendMagicAttackInfo(metinSlot[sash.ABSORPTION_SOCKET])
								item.SelectItem(itemAbsorbedVnum)
								self.__AppendAttackPowerInfo(metinSlot[sash.ABSORPTION_SOCKET])
							else:
								self.__AppendAttackPowerInfo(metinSlot[sash.ABSORPTION_SOCKET])
								item.SelectItem(itemAbsorbedVnum)
								self.__AppendMagicAttackInfo(metinSlot[sash.ABSORPTION_SOCKET])
						elif item.GetItemType() == item.ITEM_TYPE_ARMOR:
							defGrade = item.GetValue(1)
							defBonus = item.GetValue(5) * 2
							defGrade = self.CalcSashValue(defGrade, metinSlot[sash.ABSORPTION_SOCKET])
							defBonus = self.CalcSashValue(defBonus, metinSlot[sash.ABSORPTION_SOCKET])

							if defGrade > 0:
								self.AppendSpace(5)
								self.AppendTextLine(localeInfo.TOOLTIP_ITEM_DEF_GRADE % (defGrade + defBonus), self.GetChangeTextLineColor(defGrade))

							item.SelectItem(itemAbsorbedVnum)
							self.__AppendMagicDefenceInfo(metinSlot[sash.ABSORPTION_SOCKET])
						## END ATTACK / DEFENCE

						## EFFECT
						item.SelectItem(itemAbsorbedVnum)
						for i in xrange(item.ITEM_APPLY_MAX_NUM):
							(affectType, affectValue) = item.GetAffect(i)
							affectValue = self.CalcSashValue(affectValue, metinSlot[sash.ABSORPTION_SOCKET])
							affectString = self.__GetAffectString(affectType, affectValue)
							if affectString and affectValue > 0:
								self.AppendTextLine(affectString, self.GetChangeTextLineColor(affectValue))

							item.SelectItem(itemAbsorbedVnum)
						# END EFFECT

						item.SelectItem(itemVnum)
						## ATTR
						self.__AppendAttributeInformation(attrSlot, metinSlot[sash.ABSORPTION_SOCKET])
						# END ATTR
					else:
						# ATTR
						self.__AppendAttributeInformation(attrSlot)
						
						if itemVnum < 85020:
							if preview != 0:
								self.__ModelPreview(itemVnum, 4, self.__ItemGetRace(), window_type, transmutation, slotIndex)	
						#END ATTR
				else:
					self.__AppendAffectInformation()
					self.__AppendAttributeInformation(attrSlot)
			else:
				self.__AppendAffectInformation()
				self.__AppendAttributeInformation(attrSlot)
			if app.ENABLE_CHANGELOOK_SYSTEM:
				self.AppendTransmutation(window_type, slotIndex, transmutation)
			self.AppendWearableInformation()
			bHasRealtimeFlag = 0
			for i in xrange(item.LIMIT_MAX_NUM):
				(limitType, limitValue) = item.GetLimit(i)
				if item.LIMIT_REAL_TIME == limitType:
					bHasRealtimeFlag = 1

			if bHasRealtimeFlag == 1:
				self.AppendMallItemLastTime(metinSlot[0])

		## Rod ##
		elif item.ITEM_TYPE_ROD == itemType:
			if 0 != metinSlot:
				curLevel = item.GetValue(0) / 10
				curEXP = metinSlot[0]
				maxEXP = item.GetValue(2)
				self.__AppendLimitInformation()
				self.__AppendRodInformation(curLevel, curEXP, maxEXP)
		## Pick ##
		elif item.ITEM_TYPE_PICK == itemType:
			if 0 != metinSlot:
				curLevel = item.GetValue(0) / 10
				curEXP = metinSlot[0]
				maxEXP = item.GetValue(2)
				self.__AppendLimitInformation()
				self.__AppendPickInformation(curLevel, curEXP, maxEXP)
		## Lottery ##
		elif item.ITEM_TYPE_LOTTERY == itemType:
			if 0 != metinSlot:
				ticketNumber = int(metinSlot[0])
				stepNumber = int(metinSlot[1])
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_LOTTERY_STEP_NUMBER % (stepNumber), self.NORMAL_COLOR)
				self.AppendTextLine(localeInfo.TOOLTIP_LOTTO_NUMBER % (ticketNumber), self.NORMAL_COLOR);
		### Metin ###
		elif item.ITEM_TYPE_METIN == itemType:
			self.AppendMetinInformation()
			self.AppendMetinWearInformation()
		### Fish ###
		elif item.ITEM_TYPE_FISH == itemType:
			if 0 != metinSlot:
				self.__AppendFishInfo(metinSlot[0])
		### Gacha = Battle Shop Chest ###
		elif item.ITEM_TYPE_GACHA == itemType:
			if 0 != metinSlot:
				if self.isShopItem:
					restUsableCount = int(item.GetLimit(1)[1])
				else:
					restUsableCount = int(metinSlot[0])

				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_REST_USABLE_COUNT % (restUsableCount), grp.GenerateColor(0.5, 1.0, 0.3, 1.0))
		## item.ITEM_TYPE_BLEND
		elif item.ITEM_TYPE_BLEND == itemType:
			self.__AppendLimitInformation()
			if metinSlot:
				affectType = metinSlot[0]
				affectValue = metinSlot[1]
				time = metinSlot[2]
				self.AppendSpace(5)
				affectText = self.__GetAffectString(affectType, affectValue)
				self.AppendTextLine(affectText, self.NORMAL_COLOR)
				if app.ENABLE_EXTENDED_BLEND_AFFECT:
					status = metinSlot[3]

					self.AppendSpace(10)
					if status != 0:
						self.AppendTextLine(localeInfo.BLEND_ITEM_TOOLTIP_APPLY, 0xff86e57f) # RGB(134, 229, 127)
					else:
						self.AppendTextLine(localeInfo.BLEND_ITEM_TOOLTIP_UNAPPLIED, 0xfff15f5f) # RGB(241, 95, 95)

					self.AppendSpace(5)
					if time > item.MIN_INFINITE_DURATION:
						self.AppendTextLine(localeInfo.INFINITE_USE, self.CONDITION_COLOR)
					else:
						if time > 0:
							endTime = app.GetGlobalTimeStamp() + time
							leftSec = max(0, endTime - app.GetGlobalTimeStamp())
							self.AppendTextLine(localeInfo.LEFT_TIME + " : " + localeInfo.SecondToDHMS(leftSec), self.NORMAL_COLOR)
						else:
							self.AppendTextLine(localeInfo.BLEND_ITEM_TOOLTIP_NO_TIME)
				else:
					if time > 0:
						minute = (time / 60)
						second = (time % 60)
						timeString = localeInfo.TOOLTIP_POTION_TIME

						if minute > 0:
							timeString += str(minute) + localeInfo.TOOLTIP_POTION_MIN
						if second > 0:
							timeString += " " + str(second) + localeInfo.TOOLTIP_POTION_SEC

						self.AppendTextLine(timeString)
					# [MT-489] 제조창에 알수 없는 툴팁
					#else:
					#	self.AppendTextLine(localeInfo.BLEND_POTION_NO_TIME)
		elif item.ITEM_TYPE_UNIQUE == itemType:	
			#if app.WJ_EXTENDED_PET_SYSTEM and itemSubType == item.UNIQUE_USE_PET:
			#	self.__AppendLimitInformation()
			#	self.__AppendAffectInformation()
			#	return
			self.__AppendLimitInformation()
			self.__AppendAffectInformation()
			if 0 != metinSlot:
				bHasRealtimeFlag = 0

				for i in xrange(item.LIMIT_MAX_NUM):
					(limitType, limitValue) = item.GetLimit(i)
					if item.LIMIT_REAL_TIME == limitType:
						bHasRealtimeFlag = 1

				if 1 == bHasRealtimeFlag:
					self.AppendMallItemLastTime(metinSlot[0])		
				else:
					time = metinSlot[2]
					if 1 == item.GetValue(2): ## ½C½A°￡ AI¿e Flag / AaAø ¾ECØμμ AØ´U
						self.AppendMallItemLastTime(time)
					else:
						self.AppendUniqueItemLastTime(time)
		### Use ###
		elif item.ITEM_TYPE_USE == itemType:
			self.__AppendLimitInformation()
			if item.USE_POTION == itemSubType or item.USE_POTION_NODELAY == itemSubType:
				self.__AppendPotionInformation()
			elif item.USE_ABILITY_UP == itemSubType:
				self.__AppendAbilityPotionInformation()
			elif app.ENABLE_PICKUP_FILTER and app.ENABLE_AUTO_PICKUP and item.USE_AUTO_PICKUP == itemSubType:
				self.__AppendPickupFilterInformation(metinSlot)	
			## ¿μ¼® °¨Ao±a
			if 27989 == itemVnum or 76006 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])
					self.AppendSpace(5)
					self.AppendTextLine(localeInfo.TOOLTIP_REST_USABLE_COUNT % (6 - useCount), self.NORMAL_COLOR)
			## AIº￥Æ® °¨Ao±a
			elif 50004 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])
					self.AppendSpace(5)
					self.AppendTextLine(localeInfo.TOOLTIP_REST_USABLE_COUNT % (10 - useCount), self.NORMAL_COLOR)
			## AUμ¿¹°¾a
			elif constInfo.IS_AUTO_POTION(itemVnum):
				if 0 != metinSlot:
					## 0: E°¼ºE­, 1: ≫c¿e·®, 2: AN·®
					isActivated = int(metinSlot[0])
					usedAmount = float(metinSlot[1])
					totalAmount = float(metinSlot[2])

					if 0 == totalAmount:
						totalAmount = 1

					self.AppendSpace(5)
					if 0 != isActivated:
						self.AppendTextLine("(%s)" % (localeInfo.TOOLTIP_AUTO_POTION_USING), self.SPECIAL_POSITIVE_COLOR)
						self.AppendSpace(5)

					self.AppendTextLine(localeInfo.TOOLTIP_AUTO_POTION_REST % (100.0 - ((usedAmount / totalAmount) * 100.0)), self.POSITIVE_COLOR)

			## ±IE? ±a¾iºI
			elif itemVnum in WARP_SCROLLS:
				if 0 != metinSlot:
					xPos = int(metinSlot[0])
					yPos = int(metinSlot[1])
					if xPos != 0 and yPos != 0:
						(mapName, xBase, yBase) = background.GlobalPositionToMapInfo(xPos, yPos)

						localeMapName=localeInfo.MINIMAP_ZONE_NAME_DICT.get(mapName, "")
						self.AppendSpace(5)
						if localeMapName!="":						
							self.AppendTextLine(localeInfo.TOOLTIP_MEMORIZED_POSITION % (localeMapName, int(xPos-xBase)/100, int(yPos-yBase)/100), self.NORMAL_COLOR)
						else:
							self.AppendTextLine(localeInfo.TOOLTIP_MEMORIZED_POSITION_ERROR % (int(xPos)/100, int(yPos)/100), self.NORMAL_COLOR)
							dbg.TraceError("NOT_EXIST_IN_MINIMAP_ZONE_NAME_DICT: %s" % mapName)
			if 79000 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [MASTER]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Resist Damage Buff" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 24" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 164" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(80 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
	
					
			if 79001 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [GRAND]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Resist Damage Buff" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 29" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 224" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(60 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
					
			if 79002 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [PERFECT]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Resist Damage Buff" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 35" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 310" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(50 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
	
			if 79003 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [MASTER]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Dragon's Strength(Critical Buff)" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 24" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 110" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(80 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
	
					
			if 79004 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [GRAND]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Dragon's Strength(Critical Buff)" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 29" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 142" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(60 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
					
			if 79005 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [PERFECT]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Dragon's Strength(Critical Buff)" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 35" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 185" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(50 - useCount), self.ITEM_BUFF_USAGE_COLOR)					

			if 79006 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [MASTER]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Reflection" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 21" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 160" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(80 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
	
					
			if 79007 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [GRAND]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Reflection" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 31" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 224" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(60 - useCount), self.ITEM_BUFF_USAGE_COLOR)					
					
			if 79008 == itemVnum:
				if 0 != metinSlot:
					useCount = int(metinSlot[0])

					self.AppendSpace(5)
					self.AppendTextLine("Buff Level: [PERFECT]" , self.ITEM_BUFF_LEVEL_COLOR)
					self.AppendTextLine("Buff Type: Reflection" , self.ITEM_BUFF_TYPE_COLOR)			
					self.AppendTextLine("Buff Rate: 45" , self.ITEM_BUFF_RATE_COLOR)			
					self.AppendTextLine("Buff Duration: 310" , self.ITEM_BUFF_DURATION_COLOR)	
					self.AppendTextLine("Remaining Buffs: %s "  %(50 - useCount), self.ITEM_BUFF_USAGE_COLOR)

		if app.ENABLE_TITLE_SYSTEM:
			if itemVnum in (constInfo.TITLE_SYSTEM_ITEM_1, constInfo.TITLE_SYSTEM_ITEM_2, constInfo.TITLE_SYSTEM_ITEM_3):
				potion_list = {
					constInfo.TITLE_SYSTEM_ITEM_1 : ["[i]", "This item is purchased from the shopping area.", "This potion is for the title: %s" % localeInfo.TITLE_17, "|cFF6af200"+localeInfo.TITLE_POTION_PRICE_COINS_COLOR_0],
					constInfo.TITLE_SYSTEM_ITEM_2 : ["[i]", "This item is purchased from the shopping area", "This potion is for the title: %s" % localeInfo.TITLE_18, "|cFF6af200"+localeInfo.TITLE_POTION_PRICE_COINS_COLOR_1],	
					constInfo.TITLE_SYSTEM_ITEM_3 : ["[i]", "This item is purchased from the shopping area.", "This potion is for the title: %s" % localeInfo.TITLE_19, "|cFF6af200"+localeInfo.TITLE_POTION_PRICE_COINS_COLOR_2]}							

				self.AppendSpace(5)	
				for i in xrange(len(potion_list[itemVnum])):
					self.AppendTextLine(potion_list[itemVnum][i], self.SPECIAL_POSITIVE_COLOR)					 
			if item.USE_SPECIAL == itemSubType:
				bHasRealtimeFlag = 0
				for i in xrange(item.LIMIT_MAX_NUM):
					(limitType, limitValue) = item.GetLimit(i)
					if item.LIMIT_REAL_TIME == limitType:
						bHasRealtimeFlag = 1

				## AO´U¸e °u·A A¤º¸¸| C￥½ACO. ex) ³²Aº ½A°￡ : 6AI 6½A°￡ 58ºÐ 
				if 1 == bHasRealtimeFlag:
					self.AppendMallItemLastTime(metinSlot[0])
				else:
					# ... AI°A... ¼­¹o¿¡´A AI·± ½A°￡ A¼Aⓒ ¾EμC¾i AO´Aμ￥...
					# ¿O AI·±°O AO´AAo ¾EAo´A ¸øCI³ª ±×³E μIAU...
					if 0 != metinSlot:
						time = metinSlot[player.METIN_SOCKET_MAX_NUM-1]
						## ½C½A°￡ AI¿e Flag
						if 1 == item.GetValue(2):
							self.AppendMallItemLastTime(time)

			#elif item.USE_TIME_CHARGE_PER == itemSubType:
			#	bHasRealtimeFlag = 0
			#	for i in xrange(item.LIMIT_MAX_NUM):
			#		(limitType, limitValue) = item.GetLimit(i)
			#		if item.LIMIT_REAL_TIME == limitType:
			#			bHasRealtimeFlag = 1
			#	if metinSlot[2]:
			#		self.AppendTextLine(localeInfo.TOOLTIP_TIME_CHARGER_PER(metinSlot[2]))
			#	else:
			#		self.AppendTextLine(localeInfo.TOOLTIP_TIME_CHARGER_PER(item.GetValue(0)))
			#
			#	## AO´U¸e °u·A A¤º¸¸| C￥½ACO. ex) ³²Aº ½A°￡ : 6AI 6½A°￡ 58ºÐ 
			#	if 1 == bHasRealtimeFlag:
			#		self.AppendMallItemLastTime(metinSlot[0])
			#elif item.USE_TIME_CHARGE_FIX == itemSubType:
			#	bHasRealtimeFlag = 0
			#	for i in xrange(item.LIMIT_MAX_NUM):
			#		(limitType, limitValue) = item.GetLimit(i)
			#		if item.LIMIT_REAL_TIME == limitType:
			#			bHasRealtimeFlag = 1
			#	if metinSlot[2]:
			#		self.AppendTextLine(localeInfo.TOOLTIP_TIME_CHARGER_FIX(metinSlot[2]))
			#	else:
			#		self.AppendTextLine(localeInfo.TOOLTIP_TIME_CHARGER_FIX(item.GetValue(0)))

				## AO´U¸e °u·A A¤º¸¸| C￥½ACO. ex) ³²Aº ½A°￡ : 6AI 6½A°￡ 58ºÐ 
				if 1 == bHasRealtimeFlag:
					self.AppendMallItemLastTime(metinSlot[0])
		elif item.ITEM_TYPE_QUEST == itemType:
			for i in xrange(item.LIMIT_MAX_NUM):
				(limitType, limitValue) = item.GetLimit(i)
				if item.LIMIT_REAL_TIME == limitType:
					self.AppendMallItemLastTime(metinSlot[0])
		elif item.ITEM_TYPE_DS == itemType:
			self.AppendTextLine(self.__DragonSoulInfoString(itemVnum))
			self.__AppendAttributeInformation(attrSlot)
		else:
			self.__AppendLimitInformation()
		for i in xrange(item.LIMIT_MAX_NUM):
			(limitType, limitValue) = item.GetLimit(i)
			#dbg.TraceError("LimitType : %d, limitValue : %d" % (limitType, limitValue))

			if item.LIMIT_REAL_TIME_START_FIRST_USE == limitType:
				self.AppendRealTimeStartFirstUseLastTime(item, metinSlot, i)
				#dbg.TraceError("2) REAL_TIME_START_FIRST_USE flag On ")

			elif item.LIMIT_TIMER_BASED_ON_WEAR == limitType:
				self.AppendTimerBasedOnWearLastTime(metinSlot)
				#dbg.TraceError("1) REAL_TIME flag On ")
				
		if app.LWT_BUFF_UPDATE:	
			if constInfo.DISABLE_MODEL_PREVIEW == 0: #k?nt ihr gern einbauen in constinfo.py
				if constInfo.IS_BUFFI(itemVnum):
					self.__ModelPreview(itemVnum,0,34077, window_type, transmutation, slotIndex)
					renderTarget.SetBuffi(1, "d:/ymir work/render_test/render_elendosfiles.tga", metinSlot[1], metinSlot[2], int(self.Value3VerBana(metinSlot[3])))
		self.ShowToolTip()
		
	def Value3VerBana(self, id):
		item.SelectItem(id)
		return item.GetValue(3)
		
	def __DragonSoulInfoString (self, dwVnum):
		step = (dwVnum / 100) % 10
		refine = (dwVnum / 10) % 10
		if 0 == step:
			return localeInfo.DRAGON_SOUL_STEP_LEVEL1 + " " + localeInfo.DRAGON_SOUL_STRENGTH(refine)
		elif 1 == step:
			return localeInfo.DRAGON_SOUL_STEP_LEVEL2 + " " + localeInfo.DRAGON_SOUL_STRENGTH(refine)
		elif 2 == step:
			return localeInfo.DRAGON_SOUL_STEP_LEVEL3 + " " + localeInfo.DRAGON_SOUL_STRENGTH(refine)
		elif 3 == step:
			return localeInfo.DRAGON_SOUL_STEP_LEVEL4 + " " + localeInfo.DRAGON_SOUL_STRENGTH(refine)
		elif 4 == step:
			return localeInfo.DRAGON_SOUL_STEP_LEVEL5 + " " + localeInfo.DRAGON_SOUL_STRENGTH(refine)
		else:
			return ""
	## Ci¾iAI°¡?
	def __IsHair(self, itemVnum):
		return (self.__IsOldHair(itemVnum) or 
			self.__IsNewHair(itemVnum) or
			self.__IsNewHair2(itemVnum) or
			self.__IsNewHair3(itemVnum) or
			self.__IsCostumeHair(itemVnum)
			)
	def __IsOldHair(self, itemVnum):
		return itemVnum > 73000 and itemVnum < 74000	
	def __IsNewHair(self, itemVnum):
		return itemVnum > 74000 and itemVnum < 75000	
	def __IsNewHair2(self, itemVnum):
		return itemVnum > 75000 and itemVnum < 76000	
	def __IsNewHair3(self, itemVnum):
		return ((74012 < itemVnum and itemVnum < 74022) or
			(74262 < itemVnum and itemVnum < 74272) or
			(74512 < itemVnum and itemVnum < 74522) or
			(74762 < itemVnum and itemVnum < 74772) or
			(45000 < itemVnum and itemVnum < 47000) or
			(52840 < itemVnum and itemVnum < 52841) or
			(52272, 40280 <= itemVnum and itemVnum <= 52273, 40281))
			
	def __IsCostumeHair(self, itemVnum):
		return app.ENABLE_COSTUME_SYSTEM and self.__IsNewHair3(itemVnum - 100000)
		
	if app.ENABLE_RENDER_TARGET_SYSTEM:
		def ModelPreviewFull(self, itemVnum):
			item.SelectItem(itemVnum)
			itemType = item.GetItemType()
			itemSubType = item.GetItemSubType()

			itemRace = self.ItemGetRace(itemVnum)

			########## INITIALIZE TYPE/SUBTYPE LIST ##########
			IsPets   = (item.ITEM_TYPE_UNIQUE == itemType or item.ITEM_TYPE_QUEST == itemType)
			isCostumeMount = (itemType == item.ITEM_TYPE_COSTUME and itemSubType == item.COSTUME_TYPE_MOUNT)

			IsArmor    = (itemType == item.ITEM_TYPE_ARMOR and itemSubType == item.ARMOR_BODY)
			IsWeapon   = (itemType == item.ITEM_TYPE_WEAPON)

			IsCostumeBody  = (itemType == item.ITEM_TYPE_COSTUME and itemSubType == item.COSTUME_TYPE_BODY)
			IsCostumeHair  = (itemType == item.ITEM_TYPE_COSTUME and itemSubType == item.COSTUME_TYPE_HAIR)

			if app.ENABLE_COSTUME_WEAPON_SYSTEM:
				IsCostumeWeapon= (itemType == item.ITEM_TYPE_COSTUME and itemSubType == item.COSTUME_TYPE_WEAPON)

			##if app.ENABLE_EFFECT_SYSTEM:
			##	IsEffectBody = (itemType == item.ITEM_TYPE_COSTUME and item.IsWearableFlag(item.COSTUME_EFFECT_ARMOR))
			##	IsEffectWeapon = (itemType == item.ITEM_TYPE_COSTUME and item.IsWearableFlag(item.COSTUME_EFFECT_WEAPON))

			########## IF SELECTED FROM INVENTORY ##########
			if IsPets or isCostumeMount:
				mobVnum = item.GetValue(3)

				if mobVnum != 0:
					self.interface.wndTargetRender.DisplayUser(mobVnum)
					self.interface.wndTargetRender.Open()
			elif IsWeapon or (app.ENABLE_COSTUME_WEAPON_SYSTEM and IsCostumeWeapon):
				self.interface.wndTargetRender.DisplayUser(itemRace, False, itemVnum)
				self.interface.wndTargetRender.Open()
			elif IsArmor or IsCostumeBody:
				self.interface.wndTargetRender.DisplayUser(itemRace, False, 0, itemVnum)
				self.interface.wndTargetRender.Open()
			elif IsCostumeHair:
				self.interface.wndTargetRender.DisplayUser(itemRace, False, 0, 0, item.GetValue(3))
				self.interface.wndTargetRender.Open()
			elif app.ENABLE_EFFECT_SYSTEM and IsEffectBody:
				self.interface.wndTargetRender.DisplayUser(player.GetRace(), False, 0, 0, 0, item.GetValue(0))
				self.interface.wndTargetRender.Open()
			elif app.ENABLE_EFFECT_SYSTEM and IsEffectWeapon:
				self.interface.wndTargetRender.DisplayUser(player.GetRace(), False, 0, 0, 0, 0, itemVnum)
				self.interface.wndTargetRender.Open()

		def ItemGetRace(self, itemVnum = 0):
			races_m = []
			races_f = []
			MALES = [0, 5, 2, 7]
			FEMALES = [4, 1, 6, 3]
			
			item.SelectItem(itemVnum)

			if not item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR):
				races_m.append(MALES[0])
				races_f.append(FEMALES[0])
			if not item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN):
				races_m.append(MALES[1])
				races_f.append(FEMALES[1])
			if not item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA):
				races_m.append(MALES[2])
				races_f.append(FEMALES[2])
			if not item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN):
				races_m.append(MALES[3])
				races_f.append(FEMALES[3])
			
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE):
				races_f = []
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE):
				races_m = []
			
			race = player.GetRace()
			
			if race in races_m or race in races_f:
				return race
			
			if len(races_f) == 0:
				if race in races_m:
					return race
				if len(races_m) > 2:
					return races_m[app.GetRandom(0, len(races_m) - 1)]
				return races_m[0]
			
			elif len(races_m) == 0:
				if race in races_f:
					return race
				if len(races_f) > 2:
					return races_f[app.GetRandom(0, len(races_f) - 1)]
				return races_f[0]

			else:
				table = []
				for i in races_f:
					table.append(i)
				for i in races_m:
					table.append(i)
					
				return table[app.GetRandom(0, len(table) - 1)]
			
			return race

	if app.ENABLE_MULTISHOP:
		def AppendPriceTextLine(self, price, priceVnum):
			item.SelectItem(priceVnum)
			windowBack = ui.Window()
			windowBack.SetParent(self)

			textLine = ui.TextLine()
			textLine.SetParent(windowBack)
			textLine.SetFontName(self.defFontName)
			if player.GetItemCountByVnum(item.GetItemVnum()) >= int(price):
				textLine.SetPackedFontColor(self.POSITIVE_COLOR)
			else:
				textLine.SetPackedFontColor(self.NEGATIVE_COLOR)
			textLine.SetText("%sx" % (localeInfo.TOOLTIP_BUYPRICE % int(price)))
			textLine.SetOutline()
			textLine.SetFeather(False)
			textLine.SetPosition(0, 10)
			textLine.Show()

			itemImage = ui.ImageBox()
			itemImage.SetParent(windowBack)
			itemImage.LoadImage(item.GetIconImageFileName())
			itemImage.SetPosition(textLine.GetTextSize()[0] + 2, 0)
			itemImage.Show()

			textLineName = ui.TextLine()
			textLineName.SetParent(windowBack)
			textLineName.SetFontName(self.defFontName)
			
			if player.GetItemCountByVnum(item.GetItemVnum()) >= int(price):
				textLineName.SetPackedFontColor(self.POSITIVE_COLOR)
			else:
				textLineName.SetPackedFontColor(self.NEGATIVE_COLOR)
			textLineName.SetText("%s" % item.GetItemName())
			textLineName.SetOutline()
			textLineName.SetFeather(False)
			textLineName.SetPosition(textLine.GetTextSize()[0] + itemImage.GetWidth() + 4, 10)
			textLineName.Show()

			windowBack.SetPosition(0, self.toolTipHeight)
			windowBack.SetSize(textLine.GetTextSize()[0] + itemImage.GetWidth() + textLineName.GetTextSize()[0] + 6, 32)
			windowBack.SetWindowHorizontalAlignCenter()
			windowBack.Show()

			self.toolTipHeight += itemImage.GetHeight()

			self.childrenList.append(textLine)
			self.childrenList.append(textLineName)
			self.childrenList.append(itemImage)
			self.childrenList.append(windowBack)
			self.ResizeToolTip()

	def __AppendHairIcon(self, itemVnum):
		try:
			itemImage = ui.ImageBox()
			itemImage.SetParent(self)
			itemImage.Show()			
			if self.__IsOldHair(itemVnum):
				itemImage.LoadImage("d:/ymir work/item/quest/"+str(itemVnum)+".tga")
			elif self.__IsNewHair3(itemVnum):
				itemImage.LoadImage("icon/hair/%d.sub" % (itemVnum))
			elif self.__IsNewHair(itemVnum): # ±aA¸ Ci¾i ¹øE￡¸| ¿￢°a½AAN¼­ ≫c¿eCN´U. ≫o·I¿i ¾ÆAIAUAº 1000¸¸A­ ¹øE￡°¡ ´A¾u´U.
				itemImage.LoadImage("d:/ymir work/item/quest/"+str(itemVnum-1000)+".tga")
			elif self.__IsNewHair2(itemVnum):
				itemImage.LoadImage("icon/hair/%d.sub" % (itemVnum))
			elif self.__IsCostumeHair(itemVnum):
				itemImage.LoadImage("icon/hair/%d.sub" % (itemVnum - 100000))
			itemImage.SetPosition(itemImage.GetWidth()/2, self.toolTipHeight)
			self.toolTipHeight += itemImage.GetHeight()
			#self.toolTipWidth += itemImage.GetWidth()/2
			self.childrenList.append(itemImage)
			self.ResizeToolTip()
		except:
			pass
	## ≫cAIAi°¡ A≪ Description AI °æ¿i AøÆA ≫cAIAi¸| A¶A¤CN´U
	def __ModelPreview(self, Vnum, test, model, window_type, transmutation, slotIndex):
		
		if constInfo.DISABLE_MODEL_PREVIEW == 1: #k?nt ihr gern einbauen in constinfo.py
			return
		transmutationVnum = 0
		if transmutation == -1:
			if window_type == player.INVENTORY:
				transmutationVnum = player.GetItemTransmutation(window_type, slotIndex)
			elif window_type == player.SAFEBOX:
				transmutationVnum = safebox.GetItemTransmutation(slotIndex)
			elif window_type == player.MALL:
				transmutationVnum = safebox.GetItemMallTransmutation(slotIndex)
		else:
			transmutationVnum = transmutation
		
		if transmutationVnum != 0:
			Vnum = transmutationVnum


		RENDER_TARGET_INDEX = 1

		self.ModelPreviewBoard = ui.ThinBoard()
		self.ModelPreviewBoard.SetParent(self)
		self.ModelPreviewBoard.SetSize(190+10, 210+30)
		self.ModelPreviewBoard.SetPosition(-202, 0)
		self.ModelPreviewBoard.Show()

		self.ModelPreview = ui.RenderTarget()
		self.ModelPreview.SetParent(self.ModelPreviewBoard)
		self.ModelPreview.SetSize(190, 210)
		self.ModelPreview.SetPosition(5, 22)
		self.ModelPreview.SetRenderTarget(RENDER_TARGET_INDEX)
		self.ModelPreview.Show()

		self.ModelPreviewText = ui.TextLine()
		self.ModelPreviewText.SetParent(self.ModelPreviewBoard)
		self.ModelPreviewText.SetFontName(self.defFontName)
		self.ModelPreviewText.SetPackedFontColor(grp.GenerateColor(0.8824, 0.9804, 0.8824, 1.0))
		self.ModelPreviewText.SetPosition(0, 5)
		self.ModelPreviewText.SetText("Preview")
		self.ModelPreviewText.SetOutline()
		self.ModelPreviewText.SetFeather(False)
		self.ModelPreviewText.SetWindowHorizontalAlignCenter()
		self.ModelPreviewText.SetHorizontalAlignCenter()
		self.ModelPreviewText.Show()
		renderTarget.SetBackground(RENDER_TARGET_INDEX, "d:/ymir work/render_test/render_elendosfiles.tga")
		renderTarget.SetVisibility(RENDER_TARGET_INDEX, True)
		renderTarget.SelectModel(RENDER_TARGET_INDEX, model)
		if test == 1:
			renderTarget.SetHair(RENDER_TARGET_INDEX, Vnum)
		elif test == 2:
			renderTarget.SetArmor(RENDER_TARGET_INDEX, Vnum)	
		elif test == 3:
			renderTarget.SetWeapon(RENDER_TARGET_INDEX, Vnum)
		elif test == 4:
			renderTarget.SetAcce(RENDER_TARGET_INDEX, Vnum)
		elif test == 5:
			#Rustungskostum/Standardkostum
			if (player.GetItemIndex(item.COSTUME_SLOT_BODY) > 0): #Rustungskostum
				renderTarget.SetArmor(RENDER_TARGET_INDEX,  player.GetItemIndex(item.COSTUME_SLOT_BODY))
			elif (player.GetItemIndex(item.COSTUME_SLOT_BODY) < 1): #Standardrussi
				renderTarget.SetArmor(RENDER_TARGET_INDEX,  player.GetItemIndex(item.EQUIPMENT_BODY))

			#Waffenkostum/Standardwaffe
			if (player.GetItemIndex(item.COSTUME_SLOT_WEAPON) > 0): #Waffenkostum
				renderTarget.SetWeapon(RENDER_TARGET_INDEX, player.GetItemIndex(item.COSTUME_SLOT_WEAPON))
			elif (player.GetItemIndex(item.COSTUME_SLOT_WEAPON) < 1): #Standardwaffe
				renderTarget.SetWeapon(RENDER_TARGET_INDEX, player.GetItemIndex(item.EQUIPMENT_WEAPON))

			#Frisur
			if (player.GetItemIndex(item.COSTUME_SLOT_HAIR) > 0):
				item.SelectItem(player.GetItemIndex(item.COSTUME_SLOT_HAIR))
				renderTarget.SetHair(RENDER_TARGET_INDEX, item.GetValue(3))

			# ACCE
			#if (player.GetSash() > 0):
				#renderTarget.SetSash(RENDER_TARGET_INDEX, player.GetSash())

			# RUSTUNGSHINING
			#if (player.GetItemIndex(item.ITEM_TYPE_SHINING) > 0): #Rustungsshining
			#	renderTarget.ChangeArmorShining(RENDER_TARGET_INDEX, player.GetItemIndex(item.ITEM_TYPE_SHINING))

			# SPECIALSHINING
			#if (player.GetItemIndex(item.ITEM_TYPE_SHINING) > 0): #Specialshining
			#	renderTarget.ChangeSpecialShining(RENDER_TARGET_INDEX, player.GetItemIndex(item.ITEM_TYPE_SHINING))

			renderTarget.ChangeWeaponShining(RENDER_TARGET_INDEX, Vnum)

		elif test == 6:
			#Rustungskostum/Standardkostum
			if (player.GetItemIndex(item.COSTUME_SLOT_BODY) > 0): #Rustungskostum
				renderTarget.SetArmor(RENDER_TARGET_INDEX,  player.GetItemIndex(item.COSTUME_SLOT_BODY))
			elif (player.GetItemIndex(item.COSTUME_SLOT_BODY) < 1): #Standardrussi
				renderTarget.SetArmor(RENDER_TARGET_INDEX,  player.GetItemIndex(item.EQUIPMENT_BODY))

			#Waffenkostum/Standardwaffe
			if (player.GetItemIndex(item.COSTUME_SLOT_WEAPON) > 0): #Waffenkostum
				renderTarget.SetWeapon(RENDER_TARGET_INDEX, player.GetItemIndex(item.COSTUME_SLOT_WEAPON))
			elif (player.GetItemIndex(item.COSTUME_SLOT_WEAPON) < 1): #Standardwaffe
				renderTarget.SetWeapon(RENDER_TARGET_INDEX, player.GetItemIndex(item.EQUIPMENT_WEAPON))

			#Frisur
			if (player.GetItemIndex(item.COSTUME_SLOT_HAIR) > 0):
				item.SelectItem(player.GetItemIndex(item.COSTUME_SLOT_HAIR))
				renderTarget.SetHair(RENDER_TARGET_INDEX, item.GetValue(3))

			# ACCE
			#if (player.GetSash() > 0):
				#renderTarget.SetSash(RENDER_TARGET_INDEX, player.GetSash())

			# WAFFENSHINING
			#if (player.GetItemIndex(item.ITEM_TYPE_SHINING) > 0): #Waffenshining
			#	renderTarget.ChangeWeaponShining(RENDER_TARGET_INDEX, player.GetItemIndex(item.ITEM_TYPE_SHINING))

			# SPECIALSHINING
			#if (player.GetItemIndex(item.ITEM_TYPE_SHINING) > 0): #Specialshining
			#	renderTarget.ChangeSpecialShining(RENDER_TARGET_INDEX, player.GetItemIndex(item.ITEM_TYPE_SHINING))

			renderTarget.ChangeArmorShining(RENDER_TARGET_INDEX, Vnum)

		elif test == 7:
			#Rustungskostum/Standardkostum
			if (player.GetItemIndex(item.COSTUME_SLOT_BODY) > 0): #Rustungskostum
				renderTarget.SetArmor(RENDER_TARGET_INDEX,  player.GetItemIndex(item.COSTUME_SLOT_BODY))
			elif (player.GetItemIndex(item.COSTUME_SLOT_BODY) < 1): #Standardrussi
				renderTarget.SetArmor(RENDER_TARGET_INDEX,  player.GetItemIndex(item.EQUIPMENT_BODY))

			#Waffenkostum/Standardwaffe
			if (player.GetItemIndex(item.COSTUME_SLOT_WEAPON) > 0): #Waffenkostum
				renderTarget.SetWeapon(RENDER_TARGET_INDEX, player.GetItemIndex(item.COSTUME_SLOT_WEAPON))
			elif (player.GetItemIndex(item.COSTUME_SLOT_WEAPON) < 1): #Standardwaffe
				renderTarget.SetWeapon(RENDER_TARGET_INDEX, player.GetItemIndex(item.EQUIPMENT_WEAPON))

			#Frisur
			if (player.GetItemIndex(item.COSTUME_SLOT_HAIR) > 0):
				item.SelectItem(player.GetItemIndex(item.COSTUME_SLOT_HAIR))
				renderTarget.SetHair(RENDER_TARGET_INDEX, item.GetValue(3))

			# ACCE
			#if (player.GetSash() > 0):
			#	renderTarget.SetSash(RENDER_TARGET_INDEX, player.GetSash())

			# WAFFENSHINING
			#if (player.GetItemIndex(item.ITEM_TYPE_SHINING) > 0): #Waffenshining
			#	renderTarget.ChangeWeaponShining(RENDER_TARGET_INDEX, player.GetItemIndex(item.ITEM_TYPE_SHINING))

			# RUSTUNGSHINING
			#if (player.GetItemIndex(item.ITEM_TYPE_SHINING) > 0): #Rustungsshining
			#	renderTarget.ChangeArmorShining(RENDER_TARGET_INDEX, player.GetItemIndex(item.ITEM_TYPE_SHINING))

			renderTarget.ChangeSpecialShining(RENDER_TARGET_INDEX, Vnum)
		elif test == 8:
			#Rustungskostum/Standardkostum
			if (player.GetItemIndex(item.COSTUME_SLOT_BODY) > 0): #Rustungskostum
				renderTarget.SetArmor(RENDER_TARGET_INDEX,  player.GetItemIndex(item.COSTUME_SLOT_BODY))
			elif (player.GetItemIndex(item.COSTUME_SLOT_BODY) < 1): #Standardrussi
				renderTarget.SetArmor(RENDER_TARGET_INDEX,  player.GetItemIndex(item.EQUIPMENT_BODY))

			#Waffenkostum/Standardwaffe
			if (player.GetItemIndex(item.COSTUME_SLOT_WEAPON) > 0): #Waffenkostum
				renderTarget.SetWeapon(RENDER_TARGET_INDEX, player.GetItemIndex(item.COSTUME_SLOT_WEAPON))
			elif (player.GetItemIndex(item.COSTUME_SLOT_WEAPON) < 1): #Standardwaffe
				renderTarget.SetWeapon(RENDER_TARGET_INDEX, player.GetItemIndex(item.EQUIPMENT_WEAPON))

			#Frisur
			if (player.GetItemIndex(item.COSTUME_SLOT_HAIR) > 0):
				item.SelectItem(player.GetItemIndex(item.COSTUME_SLOT_HAIR))
				renderTarget.SetHair(RENDER_TARGET_INDEX, item.GetValue(3))
				
			renderTarget.SetSkillEffect(RENDER_TARGET_INDEX, Vnum)
			
	def __ModelPreviewClose(self):
		RENDER_TARGET_INDEX = 1

		if self.ModelPreviewBoard:
			self.ModelPreviewBoard.Hide()
			self.ModelPreview.Hide()
			self.ModelPreviewText.Hide()

			self.ModelPreviewBoard = None
			self.ModelPreview = None
			self.ModelPreviewText = None

			renderTarget.SetVisibility(RENDER_TARGET_INDEX, False)	
	
	def __ItemGetRace(self):
		race = 0

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN) and item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA) and item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN):
			race = 9
		elif item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR) and item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA) and item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN):
			race = 1
		elif item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR) and item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN) and item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN):
			race = 2
		elif item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR) and item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN) and item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA):
			race = 3

		sex = chr.RaceToSex(player.GetRace())
		MALE = 1
		FEMALE = 0

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE) and sex == MALE:
			race = player.GetRace() + 4

		if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) and sex == FEMALE:
			race = player.GetRace()

		if race == 0:
			race = player.GetRace()

		if race == 9:
			race = 0

		return race
	
	def __AdjustMaxWidth(self, attrSlot, desc):
		newToolTipWidth = self.toolTipWidth
		newToolTipWidth = max(self.__AdjustAttrMaxWidth(attrSlot), newToolTipWidth)
		newToolTipWidth = max(self.__AdjustDescMaxWidth(desc), newToolTipWidth)
		if newToolTipWidth > self.toolTipWidth:
			self.toolTipWidth = newToolTipWidth
			self.ResizeToolTip()
	def __AdjustAttrMaxWidth(self, attrSlot):
		if 0 == attrSlot:
			return self.toolTipWidth
		maxWidth = self.toolTipWidth
		for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
			type = attrSlot[i][0]
			value = attrSlot[i][1]
			if self.ATTRIBUTE_NEED_WIDTH.has_key(type):
				if value > 0:
					maxWidth = max(self.ATTRIBUTE_NEED_WIDTH[type], maxWidth)
					# ATTR_CHANGE_TOOLTIP_WIDTH
					#self.toolTipWidth = max(self.ATTRIBUTE_NEED_WIDTH[type], self.toolTipWidth)
					#self.ResizeToolTip()
					# END_OF_ATTR_CHANGE_TOOLTIP_WIDTH
		return maxWidth
	def __AdjustDescMaxWidth(self, desc):
		if len(desc) < DESC_DEFAULT_MAX_COLS:
			return self.toolTipWidth

		return DESC_WESTERN_MAX_WIDTH
	def __SetSkillBookToolTip(self, skillIndex, bookName, skillGrade):
		skillName = skill.GetSkillName(skillIndex)
		if not skillName:
			return
		if localeInfo.IsVIETNAM():
			itemName = bookName + " " + skillName
		else:
			itemName = skillName + " " + bookName
		self.SetTitle(itemName)
	def __AppendPickInformation(self, curLevel, curEXP, maxEXP):
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_PICK_LEVEL % (curLevel), self.NORMAL_COLOR)
		self.AppendTextLine(localeInfo.TOOLTIP_PICK_EXP % (curEXP, maxEXP), self.NORMAL_COLOR)
		if curEXP == maxEXP:
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_PICK_UPGRADE1, self.NORMAL_COLOR)
			self.AppendTextLine(localeInfo.TOOLTIP_PICK_UPGRADE2, self.NORMAL_COLOR)
			self.AppendTextLine(localeInfo.TOOLTIP_PICK_UPGRADE3, self.NORMAL_COLOR)
	def __AppendRodInformation(self, curLevel, curEXP, maxEXP):
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_FISHINGROD_LEVEL % (curLevel), self.NORMAL_COLOR)
		self.AppendTextLine(localeInfo.TOOLTIP_FISHINGROD_EXP % (curEXP, maxEXP), self.NORMAL_COLOR)
		if curEXP == maxEXP:
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_FISHINGROD_UPGRADE1, self.NORMAL_COLOR)
			self.AppendTextLine(localeInfo.TOOLTIP_FISHINGROD_UPGRADE2, self.NORMAL_COLOR)
			self.AppendTextLine(localeInfo.TOOLTIP_FISHINGROD_UPGRADE3, self.NORMAL_COLOR)
	def __AppendLimitInformation(self):
		appendSpace = FALSE
		for i in xrange(item.LIMIT_MAX_NUM):
			(limitType, limitValue) = item.GetLimit(i)
			if limitValue > 0:
				if FALSE == appendSpace:
					self.AppendSpace(5)
					appendSpace = TRUE
			else:
				continue
			if item.LIMIT_LEVEL == limitType:
				color = self.GetLimitTextLineColor(player.GetStatus(player.LEVEL), limitValue)
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_LEVEL % (limitValue), color)
			elif item.LIMIT_PRESTIGE == limitType:
				color = self.GetLimitTextLineColor(player.GetStatus(player.PRESTIGE), limitValue)
				#self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_PRESTIGE % (limitValue), color)		
				self.AppendTextLine("Prestige: %d" % (limitValue), color)	
			"""
			elif item.LIMIT_STR == limitType:
				color = self.GetLimitTextLineColor(player.GetStatus(player.ST), limitValue)
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_STR % (limitValue), color)
			elif item.LIMIT_DEX == limitType:
				color = self.GetLimitTextLineColor(player.GetStatus(player.DX), limitValue)
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_DEX % (limitValue), color)
			elif item.LIMIT_INT == limitType:
				color = self.GetLimitTextLineColor(player.GetStatus(player.IQ), limitValue)
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_INT % (limitValue), color)
			elif item.LIMIT_CON == limitType:
				color = self.GetLimitTextLineColor(player.GetStatus(player.HT), limitValue)
				self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_CON % (limitValue), color)
			"""
	def __GetAffectString(self, affectType, affectValue):
		if 0 == affectType:
			return None
		if 0 == affectValue:
			return None
		try:
			return self.AFFECT_DICT[affectType](affectValue)
		except TypeError:
			return "UNKNOWN_VALUE[%s] %s" % (affectType, affectValue)
		except KeyError:
			return "UNKNOWN_TYPE[%s] %s" % (affectType, affectValue)
	def __AppendAffectInformation(self):
		for i in xrange(item.ITEM_APPLY_MAX_NUM):
			(affectType, affectValue) = item.GetAffect(i)
			affectString = self.__GetAffectString(affectType, affectValue)
			if affectString:
				self.AppendTextLine(affectString, self.GetChangeTextLineColor(affectValue))
	def AppendWearableInformation(self):
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_ITEM_WEARABLE_JOB, self.NORMAL_COLOR)
		flagList = (
			not item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR),
			not item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN),
			not item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA),
			not item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN))
		characterNames = ""
		for i in xrange(self.CHARACTER_COUNT):
			name = self.CHARACTER_NAMES[i]
			flag = flagList[i]
			if flag:
				characterNames += " "
				characterNames += name
		textLine = self.AppendTextLine(characterNames, self.NORMAL_COLOR, TRUE)
		textLine.SetFeather()
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE):
			textLine = self.AppendTextLine(localeInfo.FOR_FEMALE, self.NORMAL_COLOR, TRUE)
			textLine.SetFeather()
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE):
			textLine = self.AppendTextLine(localeInfo.FOR_MALE, self.NORMAL_COLOR, TRUE)
			textLine.SetFeather()
	def __AppendPotionInformation(self):
		self.AppendSpace(5)
		healHP = item.GetValue(0)
		healSP = item.GetValue(1)
		healStatus = item.GetValue(2)
		healPercentageHP = item.GetValue(3)
		healPercentageSP = item.GetValue(4)
		if healHP > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_PLUS_HP_POINT % healHP, self.GetChangeTextLineColor(healHP))
		if healSP > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_PLUS_SP_POINT % healSP, self.GetChangeTextLineColor(healSP))
		if healStatus != 0:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_CURE)
		if healPercentageHP > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_PLUS_HP_PERCENT % healPercentageHP, self.GetChangeTextLineColor(healPercentageHP))
		if healPercentageSP > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_PLUS_SP_PERCENT % healPercentageSP, self.GetChangeTextLineColor(healPercentageSP))
	def __AppendAbilityPotionInformation(self):
		self.AppendSpace(5)
		abilityType = item.GetValue(0)
		time = item.GetValue(1)
		point = item.GetValue(2)
		if abilityType == item.APPLY_ATT_SPEED:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_PLUS_ATTACK_SPEED % point, self.GetChangeTextLineColor(point))
		elif abilityType == item.APPLY_MOV_SPEED:
			self.AppendTextLine(localeInfo.TOOLTIP_POTION_PLUS_MOVING_SPEED % point, self.GetChangeTextLineColor(point))
		if time > 0:
			minute = (time / 60)
			second = (time % 60)
			timeString = localeInfo.TOOLTIP_POTION_TIME
			if minute > 0:
				timeString += str(minute) + localeInfo.TOOLTIP_POTION_MIN
			if second > 0:
				timeString += " " + str(second) + localeInfo.TOOLTIP_POTION_SEC
			self.AppendTextLine(timeString)
	def GetPriceColor(self, price):
		if price>=constInfo.HIGH_PRICE:
			return self.HIGH_PRICE_COLOR
		if price>=constInfo.MIDDLE_PRICE:
			return self.MIDDLE_PRICE_COLOR
		else:
			return self.LOW_PRICE_COLOR

	def AppendPrice(self, price):	
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))

	def AppendPriceBySecondaryCoin(self, price):
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_BUYPRICE  % (localeInfo.NumberToSecondaryCoinString(price)), self.GetPriceColor(price))
	def AppendSellingPrice(self, price):
		if item.IsAntiFlag(item.ITEM_ANTIFLAG_SELL):			
			self.AppendTextLine(localeInfo.TOOLTIP_ANTI_SELL, self.DISABLE_COLOR)
			self.AppendSpace(5)
		else:
			self.AppendTextLine(localeInfo.TOOLTIP_SELLPRICE % (localeInfo.NumberToMoneyString(price)), self.GetPriceColor(price))
			self.AppendSpace(5)
	def AppendMetinInformation(self):
		affectType, affectValue = item.GetAffect(0)
		#affectType = item.GetValue(0)
		#affectValue = item.GetValue(1)
		affectString = self.__GetAffectString(affectType, affectValue)
		if affectString:
			self.AppendSpace(5)
			self.AppendTextLine(affectString, self.GetChangeTextLineColor(affectValue))
	def AppendMetinWearInformation(self):
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_SOCKET_REFINABLE_ITEM, self.NORMAL_COLOR)
		flagList = (item.IsWearableFlag(item.WEARABLE_BODY),
					item.IsWearableFlag(item.WEARABLE_HEAD),
					item.IsWearableFlag(item.WEARABLE_FOOTS),
					item.IsWearableFlag(item.WEARABLE_WRIST),
					item.IsWearableFlag(item.WEARABLE_WEAPON),
					item.IsWearableFlag(item.WEARABLE_NECK),
					item.IsWearableFlag(item.WEARABLE_EAR),
					item.IsWearableFlag(item.WEARABLE_UNIQUE),
					item.IsWearableFlag(item.WEARABLE_SHIELD),
					item.IsWearableFlag(item.WEARABLE_ARROW))
		wearNames = ""
		for i in xrange(self.WEAR_COUNT):
			name = self.WEAR_NAMES[i]
			flag = flagList[i]
			if flag:
				wearNames += "  "
				wearNames += name
		textLine = ui.TextLine()
		textLine.SetParent(self)
		textLine.SetFontName(self.defFontName)
		textLine.SetPosition(self.toolTipWidth/2, self.toolTipHeight)
		textLine.SetHorizontalAlignCenter()
		textLine.SetPackedFontColor(self.NORMAL_COLOR)
		textLine.SetText(wearNames)
		textLine.Show()
		self.childrenList.append(textLine)
		self.toolTipHeight += self.TEXT_LINE_HEIGHT
		self.ResizeToolTip()
	def GetMetinSocketType(self, number):
		if player.METIN_SOCKET_TYPE_NONE == number:
			return player.METIN_SOCKET_TYPE_NONE
		elif player.METIN_SOCKET_TYPE_SILVER == number:
			return player.METIN_SOCKET_TYPE_SILVER
		elif player.METIN_SOCKET_TYPE_GOLD == number:
			return player.METIN_SOCKET_TYPE_GOLD
		else:
			item.SelectItem(number)
			if item.METIN_NORMAL == item.GetItemSubType():
				return player.METIN_SOCKET_TYPE_SILVER
			elif item.METIN_GOLD == item.GetItemSubType():
				return player.METIN_SOCKET_TYPE_GOLD
			elif "USE_PUT_INTO_ACCESSORY_SOCKET" == item.GetUseType(number):
				return player.METIN_SOCKET_TYPE_SILVER
			elif "USE_PUT_INTO_RING_SOCKET" == item.GetUseType(number):
				return player.METIN_SOCKET_TYPE_SILVER
			elif "USE_PUT_INTO_BELT_SOCKET" == item.GetUseType(number):
				return player.METIN_SOCKET_TYPE_SILVER
		return player.METIN_SOCKET_TYPE_NONE
	def GetMetinItemIndex(self, number):
		if player.METIN_SOCKET_TYPE_SILVER == number:
			return 0
		if player.METIN_SOCKET_TYPE_GOLD == number:
			return 0
		return number
	def __AppendAccessoryMetinSlotInfo(self, metinSlot, mtrlVnum):		
		ACCESSORY_SOCKET_MAX_SIZE = 3		
		cur=min(metinSlot[0], ACCESSORY_SOCKET_MAX_SIZE)
		end=min(metinSlot[1], ACCESSORY_SOCKET_MAX_SIZE)
		affectType1, affectValue1 = item.GetAffect(0)
		affectList1=[0, max(1, affectValue1*10/100), max(2, affectValue1*20/100), max(3, affectValue1*40/100)]
		affectType2, affectValue2 = item.GetAffect(1)
		affectList2=[0, max(1, affectValue2*10/100), max(2, affectValue2*20/100), max(3, affectValue2*40/100)]
		mtrlPos=0
		mtrlList=[mtrlVnum]*cur+[player.METIN_SOCKET_TYPE_SILVER]*(end-cur)
		for mtrl in mtrlList:
			affectString1 = self.__GetAffectString(affectType1, affectList1[mtrlPos+1]-affectList1[mtrlPos])			
			affectString2 = self.__GetAffectString(affectType2, affectList2[mtrlPos+1]-affectList2[mtrlPos])
			leftTime = 0
			if cur == mtrlPos+1:
				leftTime=metinSlot[2]
			self.__AppendMetinSlotInfo_AppendMetinSocketData(mtrlPos, mtrl, affectString1, affectString2, leftTime)
			mtrlPos+=1
	def __AppendMetinSlotInfo(self, metinSlot):
		if self.__AppendMetinSlotInfo_IsEmptySlotList(metinSlot):
			return
			
		if app.ENABLE_EXTENDED_SOCKETS:
			for i in xrange(player.ITEM_STONES_MAX_NUM):
				self.__AppendMetinSlotInfo_AppendMetinSocketData(i, metinSlot[i])
		else:
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				self.__AppendMetinSlotInfo_AppendMetinSocketData(i, metinSlot[i])

	def __AppendMetinSlotInfo_IsEmptySlotList(self, metinSlot):
		if 0 == metinSlot:
			return 1
			
		if app.ENABLE_EXTENDED_SOCKETS:
			for i in xrange(player.ITEM_STONES_MAX_NUM):
				metinSlotData=metinSlot[i]
				if 0 != self.GetMetinSocketType(metinSlotData):
					if 0 != self.GetMetinItemIndex(metinSlotData):
						return 0
		else:
			for i in xrange(player.METIN_SOCKET_MAX_NUM):
				metinSlotData=metinSlot[i]
				if 0 != self.GetMetinSocketType(metinSlotData):
					if 0 != self.GetMetinItemIndex(metinSlotData):
						return 0

		return 1

	def __AppendMetinSlotInfo_AppendMetinSocketData(self, index, metinSlotData, custumAffectString="", custumAffectString2="", leftTime=0):
		slotType = self.GetMetinSocketType(metinSlotData)
		itemIndex = self.GetMetinItemIndex(metinSlotData)
		if 0 == slotType:
			return
		self.AppendSpace(5)
		slotImage = ui.ImageBox()
		slotImage.SetParent(self)
		slotImage.Show()
		## Name
		nameTextLine = ui.TextLine()
		nameTextLine.SetParent(self)
		nameTextLine.SetFontName(self.defFontName)
		nameTextLine.SetPackedFontColor(self.NORMAL_COLOR)
		nameTextLine.SetOutline()
		nameTextLine.SetFeather()
		nameTextLine.Show()			
		self.childrenList.append(nameTextLine)
		if player.METIN_SOCKET_TYPE_SILVER == slotType:
			slotImage.LoadImage("d:/ymir work/ui/game/windows/metin_slot_silver.sub")
		elif player.METIN_SOCKET_TYPE_GOLD == slotType:
			slotImage.LoadImage("d:/ymir work/ui/game/windows/metin_slot_gold.sub")
		self.childrenList.append(slotImage)

		if localeInfo.IsARABIC():
			slotImage.SetPosition(self.toolTipWidth - slotImage.GetWidth() - 9, self.toolTipHeight-1)
			nameTextLine.SetPosition(self.toolTipWidth - 50, self.toolTipHeight + 2)
		else:
			slotImage.SetPosition(9, self.toolTipHeight-1)
			nameTextLine.SetPosition(50, self.toolTipHeight + 2)
		metinImage = ui.ImageBox()
		metinImage.SetParent(self)
		metinImage.Show()
		self.childrenList.append(metinImage)
		if itemIndex:
			item.SelectItem(itemIndex)
			## Image
			try:
				metinImage.LoadImage(item.GetIconImageFileName())
			except:
				dbg.TraceError("ItemToolTip.__AppendMetinSocketData() - Failed to find image file %d:%s" % 
					(itemIndex, item.GetIconImageFileName())
				)
			nameTextLine.SetText(item.GetItemName())

			## Affect		
			affectTextLine = ui.TextLine()
			affectTextLine.SetParent(self)
			affectTextLine.SetFontName(self.defFontName)
			affectTextLine.SetPackedFontColor(self.POSITIVE_COLOR)
			affectTextLine.SetOutline()
			affectTextLine.SetFeather()
			affectTextLine.Show()			

			if localeInfo.IsARABIC():
				metinImage.SetPosition(self.toolTipWidth - metinImage.GetWidth() - 10, self.toolTipHeight)
				affectTextLine.SetPosition(self.toolTipWidth - 50, self.toolTipHeight + 16 + 2)
			else:
				metinImage.SetPosition(10, self.toolTipHeight)
				affectTextLine.SetPosition(50, self.toolTipHeight + 16 + 2)

			if custumAffectString:
				affectTextLine.SetText(custumAffectString)
			elif itemIndex!=constInfo.ERROR_METIN_STONE:
				affectType, affectValue = item.GetAffect(0)
				affectString = self.__GetAffectString(affectType, affectValue)
				if affectString:
					affectTextLine.SetText(affectString)
			else:
				affectTextLine.SetText(localeInfo.TOOLTIP_APPLY_NOAFFECT)

			self.childrenList.append(affectTextLine)			
			if custumAffectString2:
				affectTextLine = ui.TextLine()
				affectTextLine.SetParent(self)
				affectTextLine.SetFontName(self.defFontName)
				affectTextLine.SetPackedFontColor(self.POSITIVE_COLOR)
				affectTextLine.SetPosition(50, self.toolTipHeight + 16 + 2 + 16 + 2)
				affectTextLine.SetOutline()
				affectTextLine.SetFeather()
				affectTextLine.Show()
				affectTextLine.SetText(custumAffectString2)
				self.childrenList.append(affectTextLine)
				self.toolTipHeight += 16 + 2
			if 0 != leftTime:
				timeText = (localeInfo.LEFT_TIME + " : " + localeInfo.SecondToDHM(leftTime))
				timeTextLine = ui.TextLine()
				timeTextLine.SetParent(self)
				timeTextLine.SetFontName(self.defFontName)
				timeTextLine.SetPackedFontColor(self.POSITIVE_COLOR)
				timeTextLine.SetPosition(50, self.toolTipHeight + 16 + 2 + 16 + 2)
				timeTextLine.SetOutline()
				timeTextLine.SetFeather()
				timeTextLine.Show()
				timeTextLine.SetText(timeText)
				self.childrenList.append(timeTextLine)
				self.toolTipHeight += 16 + 2
		else:
			nameTextLine.SetText(localeInfo.TOOLTIP_SOCKET_EMPTY)
		self.toolTipHeight += 35
		self.ResizeToolTip()

	def __AppendFishInfo(self, size):
		if size > 0:
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_FISH_LEN % (float(size) / 100.0), self.NORMAL_COLOR)

	def AppendUniqueItemLastTime(self, restMin):
		if restMin > 0:
			restSecond = restMin*60
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.LEFT_TIME + " : " + localeInfo.SecondToDHM(restSecond), self.NORMAL_COLOR)

	def AppendMallItemLastTime(self, endTime):
		leftSec = max(0, endTime - app.GetGlobalTimeStamp())
		
		if app.ENABLE_COSTUME_EXTENDED_RECHARGE:
			if leftSec > item.MIN_INFINITE_DURATION:
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.INFINITE_USE, self.CONDITION_COLOR)
				return
		
		if leftSec > 0:
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.LEFT_TIME + " : " + localeInfo.SecondToDHM(leftSec), self.NORMAL_COLOR)

	def AppendTimerBasedOnWearLastTime(self, metinSlot):
		if 0 == metinSlot[0]:
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.CANNOT_USE, self.DISABLE_COLOR)
		else:
			endTime = app.GetGlobalTimeStamp() + metinSlot[0]
			self.AppendMallItemLastTime(endTime)		

	def AppendRealTimeStartFirstUseLastTime(self, item, metinSlot, limitIndex):		
		useCount = metinSlot[1]
		endTime = metinSlot[0]

		# CN ¹øAI¶oμμ ≫c¿eCß´U¸e Socket0¿¡ A¾·a ½A°￡(2012³a 3¿u 1AI 13½A 01ºÐ °°Aº..) AI ¹UCoAOA½.
		# ≫c¿eCIAo ¾E¾O´U¸e Socket0¿¡ AI¿e°¡´E½A°￡(AI¸|A×¸e 600 °°Aº °ª. AE´UA§)AI μe¾iAOA≫ ¼o AO°i, 0AI¶o¸e Limit Value¿¡ AO´A AI¿e°¡´E½A°￡A≫ ≫c¿eCN´U.
		if 0 == useCount:
			if 0 == endTime:
				(limitType, limitValue) = item.GetLimit(limitIndex)
				endTime = limitValue
			endTime += app.GetGlobalTimeStamp()

		self.AppendMallItemLastTime(endTime)
		
	if app.ENABLE_PICKUP_FILTER and app.ENABLE_AUTO_PICKUP:
		def __AppendPickupFilterInformation(self, metinSlot):
			isActivated = metinSlot[0]
			pickupFilterFlag = metinSlot[1]
			PICKUP_FILTER_IGNORE_LIST = [
				localeInfo.PICKUP_FILTER_IGNORE_WEAPON_LABEL,
				localeInfo.PICKUP_FILTER_IGNORE_ARMOR_LABEL,
				localeInfo.PICKUP_FILTER_IGNORE_HEAD_LABEL,
				localeInfo.PICKUP_FILTER_IGNORE_SHIELD_LABEL,
				localeInfo.PICKUP_FILTER_IGNORE_WRIST_LABEL,
				localeInfo.PICKUP_FILTER_IGNORE_FOOTS_LABEL,
				localeInfo.PICKUP_FILTER_IGNORE_NECK_LABEL,
				localeInfo.PICKUP_FILTER_IGNORE_EAR_LABEL,
				localeInfo.PICKUP_FILTER_IGNORE_ETC_LABEL
			]
			
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.PICKUP_FILTER_TITLE)	
			self.AppendSpace(1)			
			
			for i in xrange(len(PICKUP_FILTER_IGNORE_LIST)):
				if pickupFilterFlag & (1 << i):
					self.AppendTextLine(PICKUP_FILTER_IGNORE_LIST[i] + ": " + "X", self.DISABLE_COLOR)
				else:
					self.AppendTextLine(PICKUP_FILTER_IGNORE_LIST[i] + ": " + "I", self.POSITIVE_COLOR)
			
			self.AppendSpace(1)		
			self.AppendTextLine("|Eemoji/key_ctrl|e + |Eemoji/key_rclick|e - Edit")		
			
	if app.ENABLE_SASH_SYSTEM:
		def SetSashResultItem(self, slotIndex, window_type = player.INVENTORY):
			(itemVnum, MinAbs, MaxAbs) = sash.GetResultItem()
			if not itemVnum:
				return

			self.ClearToolTip()

			metinSlot = [player.GetItemMetinSocket(window_type, slotIndex, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			attrSlot = [player.GetItemAttribute(window_type, slotIndex, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

			item.SelectItem(itemVnum)
			itemType = item.GetItemType()
			itemSubType = item.GetItemSubType()
			if itemType != item.ITEM_TYPE_COSTUME and itemSubType != item.COSTUME_TYPE_SASH:
				return

			absChance = MaxAbs
			itemDesc = item.GetItemDescription()
			self.__AdjustMaxWidth(attrSlot, itemDesc)
			self.__SetItemTitle(itemVnum, metinSlot, attrSlot)
			self.AppendDescription(itemDesc, 26)
			self.AppendDescription(item.GetItemSummary(), 26, self.CONDITION_COLOR)
			self.__AppendLimitInformation()

			## ABSORPTION RATE
			# if MinAbs == MaxAbs:
				# self.AppendTextLine(localeInfo.SASH_ABSORB_CHANCE % (MinAbs), self.CONDITION_COLOR)
			# else:
				# self.AppendTextLine(localeInfo.SASH_ABSORB_CHANCE2 % (MinAbs, MaxAbs), self.CONDITION_COLOR)
			## END ABSOPRTION RATE

			itemAbsorbedVnum = int(metinSlot[sash.ABSORBED_SOCKET])
			if itemAbsorbedVnum:
				## ATTACK / DEFENCE
				item.SelectItem(itemAbsorbedVnum)
				if item.GetItemType() == item.ITEM_TYPE_WEAPON:
					if item.GetItemSubType() == item.WEAPON_FAN:
						self.__AppendMagicAttackInfo(absChance)
						item.SelectItem(itemAbsorbedVnum)
						self.__AppendAttackPowerInfo(absChance)
					else:
						self.__AppendAttackPowerInfo(absChance)
						item.SelectItem(itemAbsorbedVnum)
						self.__AppendMagicAttackInfo(absChance)
				elif item.GetItemType() == item.ITEM_TYPE_ARMOR:
					defGrade = item.GetValue(1)
					defBonus = item.GetValue(5) * 2
					defGrade = self.CalcSashValue(defGrade, absChance)
					defBonus = self.CalcSashValue(defBonus, absChance)

					if defGrade > 0:
						self.AppendSpace(5)
						self.AppendTextLine(localeInfo.TOOLTIP_ITEM_DEF_GRADE % (defGrade + defBonus), self.GetChangeTextLineColor(defGrade))

					item.SelectItem(itemAbsorbedVnum)
					self.__AppendMagicDefenceInfo(absChance)
				## END ATTACK / DEFENCE

				## EFFECT
				item.SelectItem(itemAbsorbedVnum)
				for i in xrange(item.ITEM_APPLY_MAX_NUM):
					(affectType, affectValue) = item.GetAffect(i)
					affectValue = self.CalcSashValue(affectValue, absChance)
					affectString = self.__GetAffectString(affectType, affectValue)
					if affectString and affectValue > 0:
						self.AppendTextLine(affectString, self.GetChangeTextLineColor(affectValue))

					item.SelectItem(itemAbsorbedVnum)
				# END EFFECT

			item.SelectItem(itemVnum)
			## ATTR
			self.__AppendAttributeInformation(attrSlot, MaxAbs)
			# END ATTR

			self.AppendWearableInformation()
			self.ShowToolTip()
		def SetSashResultAbsItem(self, slotIndex1, slotIndex2, window_type = player.INVENTORY):
			itemVnumSash = player.GetItemIndex(window_type, slotIndex1)
			itemVnumTarget = player.GetItemIndex(window_type, slotIndex2)
			if not itemVnumSash or not itemVnumTarget:
				return

			self.ClearToolTip()

			item.SelectItem(itemVnumSash)
			itemType = item.GetItemType()
			itemSubType = item.GetItemSubType()
			if itemType != item.ITEM_TYPE_COSTUME and itemSubType != item.COSTUME_TYPE_SASH:
				return

			metinSlot = [player.GetItemMetinSocket(window_type, slotIndex1, i) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
			attrSlot = [player.GetItemAttribute(window_type, slotIndex2, i) for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM)]

			itemDesc = item.GetItemDescription()
			self.__AdjustMaxWidth(attrSlot, itemDesc)
			self.__SetItemTitle(itemVnumSash, metinSlot, attrSlot)
			self.AppendDescription(itemDesc, 26)
			self.AppendDescription(item.GetItemSummary(), 26, self.CONDITION_COLOR)
			item.SelectItem(itemVnumSash)
			self.__AppendLimitInformation()

			## ABSORPTION RATE
			# self.AppendTextLine(localeInfo.SASH_ABSORB_CHANCE % (metinSlot[sash.ABSORPTION_SOCKET]), self.CONDITION_COLOR)
			## END ABSOPRTION RATE

			## ATTACK / DEFENCE
			itemAbsorbedVnum = itemVnumTarget
			item.SelectItem(itemAbsorbedVnum)
			if item.GetItemType() == item.ITEM_TYPE_WEAPON:
				if item.GetItemSubType() == item.WEAPON_FAN:
					self.__AppendMagicAttackInfo(metinSlot[sash.ABSORPTION_SOCKET])
					item.SelectItem(itemAbsorbedVnum)
					self.__AppendAttackPowerInfo(metinSlot[sash.ABSORPTION_SOCKET])
				else:
					self.__AppendAttackPowerInfo(metinSlot[sash.ABSORPTION_SOCKET])
					item.SelectItem(itemAbsorbedVnum)
					self.__AppendMagicAttackInfo(metinSlot[sash.ABSORPTION_SOCKET])
			elif item.GetItemType() == item.ITEM_TYPE_ARMOR:
				defGrade = item.GetValue(1)
				defBonus = item.GetValue(5) * 2
				defGrade = self.CalcSashValue(defGrade, metinSlot[sash.ABSORPTION_SOCKET])
				defBonus = self.CalcSashValue(defBonus, metinSlot[sash.ABSORPTION_SOCKET])

				if defGrade > 0:
					self.AppendSpace(5)
					self.AppendTextLine(localeInfo.TOOLTIP_ITEM_DEF_GRADE % (defGrade + defBonus), self.GetChangeTextLineColor(defGrade))

				item.SelectItem(itemAbsorbedVnum)
				self.__AppendMagicDefenceInfo(metinSlot[sash.ABSORPTION_SOCKET])
			## END ATTACK / DEFENCE

			## EFFECT
			item.SelectItem(itemAbsorbedVnum)
			for i in xrange(item.ITEM_APPLY_MAX_NUM):
				(affectType, affectValue) = item.GetAffect(i)
				affectValue = self.CalcSashValue(affectValue, metinSlot[sash.ABSORPTION_SOCKET])
				affectString = self.__GetAffectString(affectType, affectValue)
				if affectString and affectValue > 0:
					self.AppendTextLine(affectString, self.GetChangeTextLineColor(affectValue))

				item.SelectItem(itemAbsorbedVnum)
			## END EFFECT

			## ATTR
			item.SelectItem(itemAbsorbedVnum)
			for i in xrange(player.ATTRIBUTE_SLOT_MAX_NUM):
				type = attrSlot[i][0]
				value = attrSlot[i][1]
				if not value:
					continue

				value = self.CalcSashValue(value, metinSlot[sash.ABSORPTION_SOCKET])
				affectString = self.__GetAffectString(type, value)
				if affectString and value > 0:
					affectColor = self.__GetAttributeColor(i, value)
					self.AppendTextLine(affectString, affectColor)

				item.SelectItem(itemAbsorbedVnum)
			## END ATTR

			## WEARABLE
			item.SelectItem(itemVnumSash)
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_WEARABLE_JOB, self.NORMAL_COLOR)

			item.SelectItem(itemVnumSash)
			flagList = (
						not item.IsAntiFlag(item.ITEM_ANTIFLAG_WARRIOR),
						not item.IsAntiFlag(item.ITEM_ANTIFLAG_ASSASSIN),
						not item.IsAntiFlag(item.ITEM_ANTIFLAG_SURA),
						not item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN)
			)

			# if app.ENABLE_WOLFMAN_CHARACTER:
				# flagList += (not item.IsAntiFlag(item.ITEM_ANTIFLAG_WOLFMAN),)

			characterNames = ""
			for i in xrange(self.CHARACTER_COUNT):
				name = self.CHARACTER_NAMES[i]
				flag = flagList[i]
				if flag:
					characterNames += " "
					characterNames += name

			textLine = self.AppendTextLine(characterNames, self.NORMAL_COLOR, True)
			textLine.SetFeather()

			item.SelectItem(itemVnumSash)
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_MALE):
				textLine = self.AppendTextLine(localeInfo.FOR_FEMALE, self.NORMAL_COLOR, True)
				textLine.SetFeather()

			if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE):
				textLine = self.AppendTextLine(localeInfo.FOR_MALE, self.NORMAL_COLOR, True)
				textLine.SetFeather()
			## END WEARABLE

			self.ShowToolTip()
	if app.ENABLE_CHANGELOOK_SYSTEM:
		def AppendTransmutation(self, window_type, slotIndex, transmutation):
			itemVnum = 0
			if transmutation == -1:
				if window_type == player.INVENTORY:
					itemVnum = player.GetItemTransmutation(window_type, slotIndex)
				elif window_type == player.SAFEBOX:
					itemVnum = safebox.GetItemTransmutation(slotIndex)
				elif window_type == player.MALL:
					itemVnum = safebox.GetItemMallTransmutation(slotIndex)
			else:
				itemVnum = transmutation

			if not itemVnum:
				return

			item.SelectItem(itemVnum)
			itemName = item.GetItemName()
			if not itemName or itemName == "":
				return

			self.AppendSpace(5)
			title = "[ " + localeInfo.CHANGE_LOOK_TITLE + " ]"
			self.AppendTextLine(title, self.NORMAL_COLOR)
			textLine = self.AppendTextLine(itemName, self.CONDITION_COLOR, True)
			textLine.SetFeather()

class HyperlinkItemToolTip(ItemToolTip):
	def __init__(self):
		ItemToolTip.__init__(self, isPickable=TRUE)
		
	def SetHyperlinkItem(self, tokens):
		minTokenCount = 3 + player.METIN_SOCKET_MAX_NUM
		if app.ENABLE_CHANGELOOK_SYSTEM:
			minTokenCount += 1
		maxTokenCount = minTokenCount + 2 * player.ATTRIBUTE_SLOT_MAX_NUM
		if tokens and len(tokens) >= minTokenCount and len(tokens) <= maxTokenCount:
			head, vnum, flag = tokens[:3]
			itemVnum = int(vnum, 16)

			if app.ENABLE_EXTENDED_SOCKETS:
				if app.ENABLE_CHANGELOOK_SYSTEM:
					transmutation = 0
					metinSlot = [int(metin, 16) for metin in tokens[3:9]]
					rests = tokens[10:]
					cnv = [int(cnv, 16) for cnv in tokens[9:10]]
					transmutation = int(cnv[0])
				else:
					metinSlot = [int(metin, 16) for metin in tokens[3:9]]
					rests = tokens[9:]
			
			else:
				metinSlot = [int(metin, 16) for metin in tokens[3:6]]
				rests = tokens[6:]
	
			if rests:
				attrSlot = []
				rests.reverse()
				while rests:
					key = int(rests.pop(), 16)
					if rests:
						val = int(rests.pop())
						attrSlot.append((key, val))
				attrSlot += [(0, 0)] * (player.ATTRIBUTE_SLOT_MAX_NUM - len(attrSlot))
			else:
				attrSlot = [(0, 0)] * player.ATTRIBUTE_SLOT_MAX_NUM

			self.ClearToolTip()
			
			if app.ENABLE_CHANGELOOK_SYSTEM:
				if not transmutation:
					self.AddItemData(itemVnum, metinSlot, attrSlot)
				else:
					self.AddItemData(itemVnum, metinSlot, attrSlot, 0, player.INVENTORY, -1, transmutation)
			else:
				self.AddItemData(itemVnum, metinSlot, attrSlot)

			ItemToolTip.OnUpdate(self)
			
	def OnUpdate(self):
		pass
		
	def OnMouseLeftButtonDown(self):
		self.Hide()

class SkillToolTip(ToolTip):
	POINT_NAME_DICT = {
		player.LEVEL : localeInfo.SKILL_TOOLTIP_LEVEL,
		player.IQ : localeInfo.SKILL_TOOLTIP_INT,
	}
	SKILL_TOOL_TIP_WIDTH = 200
	PARTY_SKILL_TOOL_TIP_WIDTH = 340
	PARTY_SKILL_EXPERIENCE_AFFECT_LIST = (	( 2, 2,  10,),
											( 8, 3,  20,),
											(14, 4,  30,),
											(22, 5,  45,),
											(28, 6,  60,),
											(34, 7,  80,),
											(38, 8, 100,), )
	PARTY_SKILL_PLUS_GRADE_AFFECT_LIST = (	( 4, 2, 1, 0,),
											(10, 3, 2, 0,),
											(16, 4, 2, 1,),
											(24, 5, 2, 2,), )
	PARTY_SKILL_ATTACKER_AFFECT_LIST = (	( 36, 3, ),
											( 26, 1, ),
											( 32, 2, ), )
	SKILL_GRADE_NAME = {	player.SKILL_GRADE_MASTER : localeInfo.SKILL_GRADE_NAME_MASTER,
							player.SKILL_GRADE_GRAND_MASTER : localeInfo.SKILL_GRADE_NAME_GRAND_MASTER,
							player.SKILL_GRADE_PERFECT_MASTER : localeInfo.SKILL_GRADE_NAME_PERFECT_MASTER, }
	AFFECT_NAME_DICT =	{
							"HP" : localeInfo.TOOLTIP_SKILL_AFFECT_ATT_POWER,
							"ATT_GRADE" : localeInfo.TOOLTIP_SKILL_AFFECT_ATT_GRADE,
							"DEF_GRADE" : localeInfo.TOOLTIP_SKILL_AFFECT_DEF_GRADE,
							"ATT_SPEED" : localeInfo.TOOLTIP_SKILL_AFFECT_ATT_SPEED,
							"MOV_SPEED" : localeInfo.TOOLTIP_SKILL_AFFECT_MOV_SPEED,
							"DODGE" : localeInfo.TOOLTIP_SKILL_AFFECT_DODGE,
							"RESIST_NORMAL" : localeInfo.TOOLTIP_SKILL_AFFECT_RESIST_NORMAL,
							"REFLECT_MELEE" : localeInfo.TOOLTIP_SKILL_AFFECT_REFLECT_MELEE,
						}
	AFFECT_APPEND_TEXT_DICT =	{
									"DODGE" : "%",
									"RESIST_NORMAL" : "%",
									"REFLECT_MELEE" : "%",
								}
	def __init__(self):
		ToolTip.__init__(self, self.SKILL_TOOL_TIP_WIDTH)
	def __del__(self):
		ToolTip.__del__(self)
	def SetSkill(self, skillIndex, skillLevel = -1):
		if 0 == skillIndex:
			return
		if skill.SKILL_TYPE_GUILD == skill.GetSkillType(skillIndex):
			if self.SKILL_TOOL_TIP_WIDTH != self.toolTipWidth:
				self.toolTipWidth = self.SKILL_TOOL_TIP_WIDTH
				self.ResizeToolTip()
			self.AppendDefaultData(skillIndex)
			self.AppendSkillConditionData(skillIndex)
			self.AppendGuildSkillData(skillIndex, skillLevel)
		else:
			if self.SKILL_TOOL_TIP_WIDTH != self.toolTipWidth:
				self.toolTipWidth = self.SKILL_TOOL_TIP_WIDTH
				self.ResizeToolTip()
			slotIndex = player.GetSkillSlotIndex(skillIndex)
			skillGrade = player.GetSkillGrade(slotIndex)
			skillLevel = player.GetSkillLevel(slotIndex)
			skillCurrentPercentage = player.GetSkillCurrentEfficientPercentage(slotIndex)
			skillNextPercentage = player.GetSkillNextEfficientPercentage(slotIndex)
			self.AppendDefaultData(skillIndex)
			self.AppendSkillConditionData(skillIndex)
			self.AppendSkillDataNew(slotIndex, skillIndex, skillGrade, skillLevel, skillCurrentPercentage, skillNextPercentage)
			self.AppendSkillRequirement(skillIndex, skillLevel)
		self.ShowToolTip()
	def SetSkillNew(self, slotIndex, skillIndex, skillGrade, skillLevel):
		if 0 == skillIndex:
			return
		if player.SKILL_INDEX_TONGSOL == skillIndex:
			slotIndex = player.GetSkillSlotIndex(skillIndex)
			skillLevel = player.GetSkillLevel(slotIndex)
			self.AppendDefaultData(skillIndex)
			#self.AppendPartySkillData(skillGrade, skillLevel)
		elif player.SKILL_INDEX_RIDING == skillIndex:
			slotIndex = player.GetSkillSlotIndex(skillIndex)
			self.AppendSupportSkillDefaultData(skillIndex, skillGrade, skillLevel, 30)
		elif player.SKILL_INDEX_SUMMON == skillIndex:
			maxLevel = 10
			self.ClearToolTip()
			self.__SetSkillTitle(skillIndex, skillGrade)
			## Description
			description = skill.GetSkillDescription(skillIndex)
			self.AppendDescription(description, 25)
			if skillLevel == 10:
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL_MASTER % (skillLevel), self.NORMAL_COLOR)
				self.AppendTextLine(localeInfo.SKILL_SUMMON_DESCRIPTION % (skillLevel*10), self.NORMAL_COLOR)
			else:
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL % (skillLevel), self.NORMAL_COLOR)
				self.__AppendSummonDescription(skillLevel, self.NORMAL_COLOR)
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL % (skillLevel+1), self.NEGATIVE_COLOR)
				self.__AppendSummonDescription(skillLevel+1, self.NEGATIVE_COLOR)
		elif skill.SKILL_TYPE_GUILD == skill.GetSkillType(skillIndex):
			if self.SKILL_TOOL_TIP_WIDTH != self.toolTipWidth:
				self.toolTipWidth = self.SKILL_TOOL_TIP_WIDTH
				self.ResizeToolTip()
			self.AppendDefaultData(skillIndex)
			self.AppendSkillConditionData(skillIndex)
			self.AppendGuildSkillData(skillIndex, skillLevel)
		else:
			if self.SKILL_TOOL_TIP_WIDTH != self.toolTipWidth:
				self.toolTipWidth = self.SKILL_TOOL_TIP_WIDTH
				self.ResizeToolTip()
			slotIndex = player.GetSkillSlotIndex(skillIndex)
			skillCurrentPercentage = player.GetSkillCurrentEfficientPercentage(slotIndex)
			skillNextPercentage = player.GetSkillNextEfficientPercentage(slotIndex)
			self.AppendDefaultData(skillIndex, skillGrade)
			self.AppendSkillConditionData(skillIndex)
			self.AppendSkillDataNew(slotIndex, skillIndex, skillGrade, skillLevel, skillCurrentPercentage, skillNextPercentage)
			self.AppendSkillRequirement(skillIndex, skillLevel)
		self.ShowToolTip()
	def __SetSkillTitle(self, skillIndex, skillGrade):
		self.SetTitle(skill.GetSkillName(skillIndex, skillGrade))
		self.__AppendSkillGradeName(skillIndex, skillGrade)
	def __AppendSkillGradeName(self, skillIndex, skillGrade):		
		if self.SKILL_GRADE_NAME.has_key(skillGrade):
			self.AppendSpace(5)
			self.AppendTextLine(self.SKILL_GRADE_NAME[skillGrade] % (skill.GetSkillName(skillIndex, 0)), self.CAN_LEVEL_UP_COLOR)
	def SetSkillOnlyName(self, slotIndex, skillIndex, skillGrade):
		if 0 == skillIndex:
			return
		slotIndex = player.GetSkillSlotIndex(skillIndex)
		self.toolTipWidth = self.SKILL_TOOL_TIP_WIDTH
		self.ResizeToolTip()
		self.ClearToolTip()
		self.__SetSkillTitle(skillIndex, skillGrade)		
		self.AppendDefaultData(skillIndex, skillGrade)
		self.AppendSkillConditionData(skillIndex)		
		self.ShowToolTip()
	def AppendDefaultData(self, skillIndex, skillGrade = 0):
		self.ClearToolTip()
		self.__SetSkillTitle(skillIndex, skillGrade)
		## Level Limit
		levelLimit = skill.GetSkillLevelLimit(skillIndex)
		if levelLimit > 0:
			color = self.NORMAL_COLOR
			if player.GetStatus(player.LEVEL) < levelLimit:
				color = self.NEGATIVE_COLOR
			self.AppendSpace(5)
			self.AppendTextLine(localeInfo.TOOLTIP_ITEM_LIMIT_LEVEL % (levelLimit), color)
		## Description
		description = skill.GetSkillDescription(skillIndex)
		self.AppendDescription(description, 25)
	def AppendSupportSkillDefaultData(self, skillIndex, skillGrade, skillLevel, maxLevel):
		self.ClearToolTip()
		self.__SetSkillTitle(skillIndex, skillGrade)
		## Description
		description = skill.GetSkillDescription(skillIndex)
		self.AppendDescription(description, 25)
		if 1 == skillGrade:
			skillLevel += 19
		elif 2 == skillGrade:
			skillLevel += 29
		elif 3 == skillGrade:
			skillLevel = 40
		self.AppendSpace(5)
		self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL_WITH_MAX % (skillLevel, maxLevel), self.NORMAL_COLOR)
	def AppendSkillConditionData(self, skillIndex):
		conditionDataCount = skill.GetSkillConditionDescriptionCount(skillIndex)
		if conditionDataCount > 0:
			self.AppendSpace(5)
			for i in xrange(conditionDataCount):
				self.AppendTextLine(skill.GetSkillConditionDescription(skillIndex, i), self.CONDITION_COLOR)
	def AppendGuildSkillData(self, skillIndex, skillLevel):
		skillMaxLevel = 7
		skillCurrentPercentage = float(skillLevel) / float(skillMaxLevel)
		skillNextPercentage = float(skillLevel+1) / float(skillMaxLevel)
		## Current Level
		if skillLevel > 0:
			if self.HasSkillLevelDescription(skillIndex, skillLevel):
				self.AppendSpace(5)
				if skillLevel == skillMaxLevel:
					self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL_MASTER % (skillLevel), self.NORMAL_COLOR)
				else:
					self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL % (skillLevel), self.NORMAL_COLOR)
				#####
				for i in xrange(skill.GetSkillAffectDescriptionCount(skillIndex)):
					self.AppendTextLine(skill.GetSkillAffectDescription(skillIndex, i, skillCurrentPercentage), self.ENABLE_COLOR)
				## Cooltime
				coolTime = skill.GetSkillCoolTime(skillIndex, skillCurrentPercentage)
				if coolTime > 0:
					self.AppendTextLine(localeInfo.TOOLTIP_SKILL_COOL_TIME + str(coolTime), self.ENABLE_COLOR)
				## SP
				needGSP = skill.GetSkillNeedSP(skillIndex, skillCurrentPercentage)
				if needGSP > 0:
					self.AppendTextLine(localeInfo.TOOLTIP_NEED_GSP % (needGSP), self.ENABLE_COLOR)
		## Next Level
		if skillLevel < skillMaxLevel:
			if self.HasSkillLevelDescription(skillIndex, skillLevel+1):
				self.AppendSpace(5)
				self.AppendTextLine(localeInfo.TOOLTIP_NEXT_SKILL_LEVEL_1 % (skillLevel+1, skillMaxLevel), self.DISABLE_COLOR)
				#####
				for i in xrange(skill.GetSkillAffectDescriptionCount(skillIndex)):
					self.AppendTextLine(skill.GetSkillAffectDescription(skillIndex, i, skillNextPercentage), self.DISABLE_COLOR)
				## Cooltime
				coolTime = skill.GetSkillCoolTime(skillIndex, skillNextPercentage)
				if coolTime > 0:
					self.AppendTextLine(localeInfo.TOOLTIP_SKILL_COOL_TIME + str(coolTime), self.DISABLE_COLOR)
				## SP
				needGSP = skill.GetSkillNeedSP(skillIndex, skillNextPercentage)
				if needGSP > 0:
					self.AppendTextLine(localeInfo.TOOLTIP_NEED_GSP % (needGSP), self.DISABLE_COLOR)
	def AppendSkillDataNew(self, slotIndex, skillIndex, skillGrade, skillLevel, skillCurrentPercentage, skillNextPercentage):
		self.skillMaxLevelStartDict = { 0 : 17, 1 : 7, 2 : 10, }
		self.skillMaxLevelEndDict = { 0 : 20, 1 : 10, 2 : 10, }
		skillLevelUpPoint = 1
		realSkillGrade = player.GetSkillGrade(slotIndex)
		skillMaxLevelStart = self.skillMaxLevelStartDict.get(realSkillGrade, 15)
		skillMaxLevelEnd = self.skillMaxLevelEndDict.get(realSkillGrade, 20)
		## Current Level
		if skillLevel > 0:
			if self.HasSkillLevelDescription(skillIndex, skillLevel):
				self.AppendSpace(5)
				if skillGrade == skill.SKILL_GRADE_COUNT:
					pass
				elif skillLevel == skillMaxLevelEnd:
					self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL_MASTER % (skillLevel), self.NORMAL_COLOR)
				else:
					self.AppendTextLine(localeInfo.TOOLTIP_SKILL_LEVEL % (skillLevel), self.NORMAL_COLOR)
				self.AppendSkillLevelDescriptionNew(skillIndex, skillCurrentPercentage, self.ENABLE_COLOR)
		## Next Level
		if skillGrade != skill.SKILL_GRADE_COUNT:
			if skillLevel < skillMaxLevelEnd:
				if self.HasSkillLevelDescription(skillIndex, skillLevel+skillLevelUpPoint):
					self.AppendSpace(5)
					## HPº¸°­, °uAeE¸CC º¸A¶½ºA³AC °æ¿i
					if skillIndex == 141 or skillIndex == 142:
						self.AppendTextLine(localeInfo.TOOLTIP_NEXT_SKILL_LEVEL_3 % (skillLevel+1), self.DISABLE_COLOR)
					else:
						self.AppendTextLine(localeInfo.TOOLTIP_NEXT_SKILL_LEVEL_1 % (skillLevel+1, skillMaxLevelEnd), self.DISABLE_COLOR)
					self.AppendSkillLevelDescriptionNew(skillIndex, skillNextPercentage, self.DISABLE_COLOR)
	def AppendSkillLevelDescriptionNew(self, skillIndex, skillPercentage, color):
		affectDataCount = skill.GetNewAffectDataCount(skillIndex)
		if affectDataCount > 0:
			for i in xrange(affectDataCount):
				type, minValue, maxValue = skill.GetNewAffectData(skillIndex, i, skillPercentage)
				if not self.AFFECT_NAME_DICT.has_key(type):
					continue
				minValue = int(minValue)
				maxValue = int(maxValue)
				affectText = self.AFFECT_NAME_DICT[type]
				if "HP" == type:
					if minValue < 0 and maxValue < 0:
						minValue *= -1
						maxValue *= -1
					else:
						affectText = localeInfo.TOOLTIP_SKILL_AFFECT_HEAL
				affectText += str(minValue)
				if minValue != maxValue:
					affectText += " - " + str(maxValue)
				affectText += self.AFFECT_APPEND_TEXT_DICT.get(type, "")
				#import debugInfo
				#if debugInfo.IsDebugMode():
				#	affectText = "!!" + affectText
				self.AppendTextLine(affectText, color)

		else:
			for i in xrange(skill.GetSkillAffectDescriptionCount(skillIndex)):
				self.AppendTextLine(skill.GetSkillAffectDescription(skillIndex, i, skillPercentage), color)

		## Duration
		duration = skill.GetDuration(skillIndex, skillPercentage)
		if duration > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_SKILL_DURATION % (duration), color)
		## Cooltime
		coolTime = skill.GetSkillCoolTime(skillIndex, skillPercentage)
		if coolTime > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_SKILL_COOL_TIME + str(coolTime), color)
		## SP
		needSP = skill.GetSkillNeedSP(skillIndex, skillPercentage)
		if needSP != 0:
			continuationSP = skill.GetSkillContinuationSP(skillIndex, skillPercentage)
			if skill.IsUseHPSkill(skillIndex):
				self.AppendNeedHP(needSP, continuationSP, color)
			else:
				self.AppendNeedSP(needSP, continuationSP, color)
	def AppendSkillRequirement(self, skillIndex, skillLevel):
		skillMaxLevel = skill.GetSkillMaxLevel(skillIndex)
		if skillLevel >= skillMaxLevel:
			return
		isAppendHorizontalLine = FALSE
		## Requirement
		if skill.IsSkillRequirement(skillIndex):
			if not isAppendHorizontalLine:
				isAppendHorizontalLine = TRUE
				self.AppendHorizontalLine()
			requireSkillName, requireSkillLevel = skill.GetSkillRequirementData(skillIndex)
			color = self.CANNOT_LEVEL_UP_COLOR
			if skill.CheckRequirementSueccess(skillIndex):
				color = self.CAN_LEVEL_UP_COLOR
			self.AppendTextLine(localeInfo.TOOLTIP_REQUIREMENT_SKILL_LEVEL % (requireSkillName, requireSkillLevel), color)
		## Require Stat
		requireStatCount = skill.GetSkillRequireStatCount(skillIndex)
		if requireStatCount > 0:
			for i in xrange(requireStatCount):
				type, level = skill.GetSkillRequireStatData(skillIndex, i)
				if self.POINT_NAME_DICT.has_key(type):
					if not isAppendHorizontalLine:
						isAppendHorizontalLine = TRUE
						self.AppendHorizontalLine()
					name = self.POINT_NAME_DICT[type]
					color = self.CANNOT_LEVEL_UP_COLOR
					if player.GetStatus(type) >= level:
						color = self.CAN_LEVEL_UP_COLOR
					self.AppendTextLine(localeInfo.TOOLTIP_REQUIREMENT_STAT_LEVEL % (name, level), color)
	def HasSkillLevelDescription(self, skillIndex, skillLevel):
		if skill.GetSkillAffectDescriptionCount(skillIndex) > 0:
			return TRUE
		if skill.GetSkillCoolTime(skillIndex, skillLevel) > 0:
			return TRUE
		if skill.GetSkillNeedSP(skillIndex, skillLevel) > 0:
			return TRUE
		return FALSE
	def AppendMasterAffectDescription(self, index, desc, color):
		self.AppendTextLine(desc, color)
	def AppendNextAffectDescription(self, index, desc):
		self.AppendTextLine(desc, self.DISABLE_COLOR)
	def AppendNeedHP(self, needSP, continuationSP, color):
		self.AppendTextLine(localeInfo.TOOLTIP_NEED_HP % (needSP), color)
		if continuationSP > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_NEED_HP_PER_SEC % (continuationSP), color)
	def AppendNeedSP(self, needSP, continuationSP, color):
		if -1 == needSP:
			self.AppendTextLine(localeInfo.TOOLTIP_NEED_ALL_SP, color)
		else:
			self.AppendTextLine(localeInfo.TOOLTIP_NEED_SP % (needSP), color)
		if continuationSP > 0:
			self.AppendTextLine(localeInfo.TOOLTIP_NEED_SP_PER_SEC % (continuationSP), color)
	#def AppendPartySkillData(self, skillGrade, skillLevel):
	#	if 1 == skillGrade:
	#		skillLevel += 19
	#	elif 2 == skillGrade:
	#		skillLevel += 29
	#	elif 3 == skillGrade:
	#		skillLevel =  40
	#	if skillLevel <= 0:
	#		return
	#	skillIndex = player.SKILL_INDEX_TONGSOL
	#	slotIndex = player.GetSkillSlotIndex(skillIndex)
	#	skillPower = player.GetSkillCurrentEfficientPercentage(slotIndex)
	#	if localeInfo.IsBRAZIL():
	#		k = skillPower
	#	else:
	#		k = player.GetSkillLevel(skillIndex) / 100.0
	#	self.AppendSpace(5)
	#	self.AutoAppendTextLine(localeInfo.TOOLTIP_PARTY_SKILL_LEVEL % skillLevel, self.NORMAL_COLOR)
	#	if skillLevel>=10:
	#		import chat
	#		chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.PARTY_SKILL_ATTACKER)
	#		chat.AppendChat(chat.CHAT_TYPE_INFO, k)
	#		
	#		self.AutoAppendTextLine(localeInfo.PARTY_SKILL_ATTACKER % chop( 10 + 60 * k ))
	#	if skillLevel>=20:
	#		self.AutoAppendTextLine(localeInfo.PARTY_SKILL_BERSERKER 	% chop(1 + 5 * k))
	#		self.AutoAppendTextLine(localeInfo.PARTY_SKILL_TANKER 	% chop(50 + 1450 * k))
	#	if skillLevel>=25:
	#		self.AutoAppendTextLine(localeInfo.PARTY_SKILL_BUFFER % chop(5 + 45 * k ))
	#	if skillLevel>=35:
	#		self.AutoAppendTextLine(localeInfo.PARTY_SKILL_SKILL_MASTER % chop(25 + 600 * k ))
	#	if skillLevel>=40:
	#		self.AutoAppendTextLine(localeInfo.PARTY_SKILL_DEFENDER % chop( 5 + 30 * k ))
	#	self.AlignHorizonalCenter()
	def __AppendSummonDescription(self, skillLevel, color):
		if skillLevel > 1:
			self.AppendTextLine(localeInfo.SKILL_SUMMON_DESCRIPTION % (skillLevel * 10), color)
		elif 1 == skillLevel:
			self.AppendTextLine(localeInfo.SKILL_SUMMON_DESCRIPTION % (15), color)
		elif 0 == skillLevel:
			self.AppendTextLine(localeInfo.SKILL_SUMMON_DESCRIPTION % (10), color)
