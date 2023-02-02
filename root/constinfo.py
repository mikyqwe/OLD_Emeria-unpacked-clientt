import app
STORAGEQID = 0
SEL_LANG = 2
BUFFI_GUI = False
ENABLE_PROMOTION_CODE_SYSTEM = 1

QidForM2bob = 0
loadedShinings = False

DISABLE_MODEL_PREVIEW = 0
try:
	with open('render_target.cfg', 'r') as f:
		if f.read() == '1':
			DISABLE_MODEL_PREVIEW = 1
except:
	pass

WETTER = -1

if app.ENABLE_HIDE_COSTUME_SYSTEM:
	HIDDEN_BODY_COSTUME = 0
	HIDDEN_HAIR_COSTUME = 0
	if app.ENABLE_SASH_SYSTEM:
		HIDDEN_SASH_COSTUME = 0
	if app.ENABLE_COSTUME_WEAPON_SYSTEM:
		HIDDEN_WEAPON_COSTUME = 0

ANTIEXP = 0

ENABLE_INTRO_ANIMATION = 0
ENABLE_FAST_STATUS_POUNTS = True
LOADED_RESOURCES = 0

finder_counts = 0
finder_items = {}
#####
OffShopSearch = 0
OffShop = 0
buyed = 0
IS_SKILLCOLOR_FLAG = 0
if app.WORLD_BOSS_YUMA:
	WORLD_BOSS_TEXT_POSITION = [0, 0, 0 ,0 ,0]
	
####
if app.ENABLE_REFINE_RENEWAL:
	IS_AUTO_REFINE = False
	AUTO_REFINE_TYPE = 0
	AUTO_REFINE_DATA = {
		"ITEM" : [-1, -1],
		"NPC" : [0, -1, -1, 0]
	}
	
if app.ENABLE_EXTENDED_BLEND_AFFECT:
	def IS_BLEND_POTION(itemVnum):
		if itemVnum >= 50821 and itemVnum <= 50826:
			return 1
		elif itemVnum == 51002:
			return 1

		return 0

	def IS_EXTENDED_BLEND_POTION(itemVnum):
		if itemVnum >= 50921 and itemVnum <= 50937:
			return 1
		elif itemVnum == 50930:
			return 1

		return 0

if app.ENABLE_DUNGEON_INFO_SYSTEM:
	dungeonInfo = []
	dungeonRanking = {
		"ranking_type" : 0,
		"ranking_list" : []
	}
	IS_RENDER_OPEN = 0

TARGET_LANGS = {}

DUEL_IS_SHOW_EQUIP = 0
DUEL_SAVE_VID = 0
if app.ENABLE_SEND_TARGET_INFO:
	MONSTER_INFO_DATA = {}

ITEMSHOP = {
	'items' : {
			'startpage' : {
					'mostBought' : [],
					'hotOffers' : [],
					},
			'itemshop' : {},
			'voteshop' : {},
			'achievementshop' : {},
		},
	'tableUpdate' : '0000-00-00 00:00:00',
	'qid'	: 0,
	'questCMD' : '',
}

AVANDOS_CONTAINER_LOTTERY = {
	"index" : 0,
	"CMD" : "",
	"item_vnum_list": [],
	"item_rarity_list": []
}

if app.ENABLE_ASLAN_LOTTERY:
	NEW_TICKET_COST = 5000000

	lotto_jackpot = 0
	lotto_next_refresh = 0
	lotto_number_infos = {}
	
	lottery_new_ticket_slot = 0
	lottery_new_ticket_numbers = [ ]
	
	lottery_ranklist_jackpot_data = {}
	lottery_ranklist_money_data = {}

	lotto_ticket_data = {
		"ticket_1" : {
			"ticket_id" : 0,
			"ticket_buy_time" : "",
			"ticket_for_lottoid" : 0,
			"ticket_numbers" : [0, 0, 0, 0],
			"ticket_state" : 0,
			"win_numbers" : 0,
			"ticket_win_money" : 0,
		},
		"ticket_2" : {
			"ticket_id" : 0,
			"ticket_buy_time" : "",
			"ticket_for_lottoid" : 0,
			"ticket_numbers" : [0, 0, 0, 0],
			"ticket_state" : 0,
			"win_numbers" : 0,
			"ticket_win_money" : 0,
		},
		"ticket_3" : {
			"ticket_id" : 0,
			"ticket_buy_time" : "",
			"ticket_for_lottoid" : 0,
			"ticket_numbers" : [0, 0, 0, 0],
			"ticket_state" : 0,
			"win_numbers" : 0,
			"ticket_win_money" : 0,
		},
	}
   
# Hide Costume
QUEST_INDEX_06 = 0
costume = 0
costume1 = 0

QUEST_INDEX_PET_TYPE = 0

# OFFLINE_SHOPS
shop_cost=[]
gift_items={}
MyShops=[]
SHOPNAMES_RANGE = 5000

QID_MALL = 0

# option
IN_GAME_SHOP_ENABLE = 1
CONSOLE_ENABLE = 0

PVPMODE_ENABLE = 1
import app
if app.ENABLE_REBORN_SYSTEM:	
	mStrAnonymous = 0
PVPMODE_TEST_ENABLE = 0
PVPMODE_ACCELKEY_ENABLE = 1
PVPMODE_ACCELKEY_DELAY = 0.5
PVPMODE_PROTECTED_LEVEL = 30

if app.ENABLE_TITLE_SYSTEM:	
	TITLE_SYSTEM_ITEM_1 = 71520
	TITLE_SYSTEM_ITEM_2 = 71521
	TITLE_SYSTEM_ITEM_3 = 71522

INPUT_IGNORE = 0
pickInfo = 1

FOG_LEVEL0 = 4800.0
FOG_LEVEL1 = 9600.0
FOG_LEVEL2 = 12800.0
FOG_LEVEL = FOG_LEVEL0
FOG_LEVEL_LIST=[FOG_LEVEL0, FOG_LEVEL1, FOG_LEVEL2]		

CAMERA_MAX_DISTANCE_SHORT = 2500.0
CAMERA_MAX_DISTANCE_LONG = 3500.0
CAMERA_MAX_DISTANCE_LIST=[CAMERA_MAX_DISTANCE_SHORT, CAMERA_MAX_DISTANCE_LONG]
CAMERA_MAX_DISTANCE = CAMERA_MAX_DISTANCE_SHORT

GET_ITEM_DROP_QUESTION_DIALOG_STATUS = 1

CHRNAME_COLOR_INDEX = 0

ENVIRONMENT_NIGHT="d:/ymir work/environment/moonlight04.msenv"
# RAINING_SYSTEM
ENVIRONMENT_CYCLE="d:/ymir work/environment/raining_system/cycle/"
ENVIRONMENT_CYCLE_ID = 0
# END_OF_RAINING_SYSTEM

if app.ENABLE_NEW_PET_SYSTEM:
	PET_EVOLUTION = 0
	PET_LEVEL = 0
	PET_MAIN = 0
	FEEDWINDOW= 0
	FEEDWINDOWCLOSED= 0
	FEEDWINDOWITEM= 0
	FEEDWINDOWITEMCLOSED= 0
	SKILL_PET3 = 0
	SKILL_PET2 = 0
	SKILL_PET1 = 0
	LASTAFFECT_POINT = 0
	LASTAFFECT_VALUE = 0
	EVOLUTION = 0
	
	def IS_PET_ITEM(itemVnum):
		if itemVnum >= 55701 and itemVnum <= 55799:
			return 1
		return 0
	
# constant
HIGH_PRICE = 500000
MIDDLE_PRICE = 50000
ERROR_METIN_STONE = 28960
SUB2_LOADING_ENABLE = 1
EXPANDED_COMBO_ENABLE = 1
CONVERT_EMPIRE_LANGUAGE_ENABLE = 1
USE_ITEM_WEAPON_TABLE_ATTACK_BONUS = 0
ADD_DEF_BONUS_ENABLE = 1
LOGIN_COUNT_LIMIT_ENABLE = 0

USE_SKILL_EFFECT_UPGRADE_ENABLE = 1

VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD = 1
GUILD_MONEY_PER_GSP = 100
GUILD_WAR_TYPE_SELECT_ENABLE = 1
TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE = 0

HAIR_COLOR_ENABLE = 1
CONVERT_EMPIRE_LANGUAGE_ENABLE = 0
ARMOR_SPECULAR_ENABLE = 1
WEAPON_SPECULAR_ENABLE = 1
SEQUENCE_PACKET_ENABLE = 1
KEEP_ACCOUNT_CONNETION_ENABLE = 1
MINIMAP_POSITIONINFO_ENABLE = 0
USE_ITEM_WEAPON_TABLE_ATTACK_BONUS = 0
ADD_DEF_BONUS_ENABLE = 0
LOGIN_COUNT_LIMIT_ENABLE = 0
PVPMODE_PROTECTED_LEVEL = 15
TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE = 10

isItemQuestionDialog = 0

def GET_ITEM_QUESTION_DIALOG_STATUS():
	global isItemQuestionDialog
	return isItemQuestionDialog

def SET_ITEM_QUESTION_DIALOG_STATUS(flag):
	global isItemQuestionDialog
	isItemQuestionDialog = flag

import app
import net

########################

def SET_DEFAULT_FOG_LEVEL():
	global FOG_LEVEL
	app.SetMinFog(FOG_LEVEL)

def SET_FOG_LEVEL_INDEX(index):
	global FOG_LEVEL
	global FOG_LEVEL_LIST
	try:
		FOG_LEVEL=FOG_LEVEL_LIST[index]
	except IndexError:
		FOG_LEVEL=FOG_LEVEL_LIST[0]
	app.SetMinFog(FOG_LEVEL)

def GET_FOG_LEVEL_INDEX():
	global FOG_LEVEL
	global FOG_LEVEL_LIST
	return FOG_LEVEL_LIST.index(FOG_LEVEL)

########################

def SET_DEFAULT_CAMERA_MAX_DISTANCE():
	global CAMERA_MAX_DISTANCE
	app.SetCameraMaxDistance(CAMERA_MAX_DISTANCE)

def SET_CAMERA_MAX_DISTANCE_INDEX(index):
	global CAMERA_MAX_DISTANCE
	global CAMERA_MAX_DISTANCE_LIST
	try:
		CAMERA_MAX_DISTANCE=CAMERA_MAX_DISTANCE_LIST[index]
	except:
		CAMERA_MAX_DISTANCE=CAMERA_MAX_DISTANCE_LIST[0]

	app.SetCameraMaxDistance(CAMERA_MAX_DISTANCE)

def GET_CAMERA_MAX_DISTANCE_INDEX():
	global CAMERA_MAX_DISTANCE
	global CAMERA_MAX_DISTANCE_LIST
	return CAMERA_MAX_DISTANCE_LIST.index(CAMERA_MAX_DISTANCE)

########################

import chrmgr
import player
import app

def SET_DEFAULT_CHRNAME_COLOR():
	global CHRNAME_COLOR_INDEX
	chrmgr.SetEmpireNameMode(CHRNAME_COLOR_INDEX)

def SET_CHRNAME_COLOR_INDEX(index):
	global CHRNAME_COLOR_INDEX
	CHRNAME_COLOR_INDEX=index
	chrmgr.SetEmpireNameMode(index)

def GET_CHRNAME_COLOR_INDEX():
	global CHRNAME_COLOR_INDEX
	return CHRNAME_COLOR_INDEX

def SET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD(index):
	global VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD
	VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD = index

def GET_VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD():
	global VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD
	return VIEW_OTHER_EMPIRE_PLAYER_TARGET_BOARD

def SET_DEFAULT_CONVERT_EMPIRE_LANGUAGE_ENABLE():
	global CONVERT_EMPIRE_LANGUAGE_ENABLE
	net.SetEmpireLanguageMode(CONVERT_EMPIRE_LANGUAGE_ENABLE)

def SET_DEFAULT_USE_ITEM_WEAPON_TABLE_ATTACK_BONUS():
	global USE_ITEM_WEAPON_TABLE_ATTACK_BONUS
	player.SetWeaponAttackBonusFlag(USE_ITEM_WEAPON_TABLE_ATTACK_BONUS)

def SET_DEFAULT_USE_SKILL_EFFECT_ENABLE():
	global USE_SKILL_EFFECT_UPGRADE_ENABLE
	app.SetSkillEffectUpgradeEnable(USE_SKILL_EFFECT_UPGRADE_ENABLE)

def SET_TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE():
	global TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE
	app.SetTwoHandedWeaponAttSpeedDecreaseValue(TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE)

########################
import item

ACCESSORY_MATERIAL_LIST = [50623, 50624, 50625, 50626, 50627, 50628, 50629, 50630, 50631, 50632, 50633, 50634, 50635, 50636, 50637, 50638, 50639, 50640]
#ACCESSORY_MATERIAL_LIST = [50623, 50623, 50624, 50624, 50625, 50625, 50626, 50627, 50628, 50629, 50630, 50631, 50632, 50633, 
#			    50623, 50623, 50624, 50624, ]
JewelAccessoryInfos = [
		# jewel		wrist	neck	ear
		[ 50634,	14420,	16220,	17220 ],	
		[ 50635,	14500,	16500,	17500 ],	
		[ 50636,	14520,	16520,	17520 ],	
		[ 50637,	14540,	16540,	17540 ],	
		[ 50638,	14560,	16560,	17560 ],	
		[ 50639,	37680,	37660,	37670 ],
		[ 50640,	78000,	78010,	78020 ],
	]
def GET_ACCESSORY_MATERIAL_VNUM(vnum, subType):
	ret = vnum
	item_base = (vnum / 10) * 10
	for info in JewelAccessoryInfos:
		if item.ARMOR_WRIST == subType:	
			if info[1] == item_base:
				return info[0]
		elif item.ARMOR_NECK == subType:	
			if info[2] == item_base:
				return info[0]
		elif item.ARMOR_EAR == subType:	
			if info[3] == item_base:
				return info[0]
 
	if vnum >= 16210 and vnum <= 16219:
		return 50625

	if item.ARMOR_WRIST == subType:	
		WRIST_ITEM_VNUM_BASE = 14000
		ret -= WRIST_ITEM_VNUM_BASE
	elif item.ARMOR_NECK == subType:
		NECK_ITEM_VNUM_BASE = 16000
		ret -= NECK_ITEM_VNUM_BASE
	elif item.ARMOR_EAR == subType:
		EAR_ITEM_VNUM_BASE = 17000
		ret -= EAR_ITEM_VNUM_BASE

	type = ret/20

	if type<0 or type>=len(ACCESSORY_MATERIAL_LIST):
		type = (ret-170) / 20
		if type<0 or type>=len(ACCESSORY_MATERIAL_LIST):
			return 0

	return ACCESSORY_MATERIAL_LIST[type]

##################################################################
## ���� �߰��� '��Ʈ' ������ Ÿ�԰�, ��Ʈ�� ���Ͽ� ���� ������ ����.. 
## ��Ʈ�� ���Ͻý����� �Ǽ������� �����ϱ� ������, �� �Ǽ����� ���� �ϵ��ڵ�ó�� �̷������� �� ���ۿ� ����..

def GET_BELT_MATERIAL_VNUM(vnum, subType = 0):
	# ����� ��� ��Ʈ���� �ϳ��� ������(#18900)�� ���� ����
	return 18900

##################################################################
## �ڵ����� (HP: #72723 ~ #72726, SP: #72727 ~ #72730)

# �ش� vnum�� �ڵ������ΰ�?
def IS_AUTO_POTION(itemVnum):
	return IS_AUTO_POTION_HP(itemVnum) or IS_AUTO_POTION_SP(itemVnum)
	
# �ش� vnum�� HP �ڵ������ΰ�?
def IS_AUTO_POTION_HP(itemVnum):
	if 72723 <= itemVnum and 72726 >= itemVnum:
		return 1
	elif itemVnum >= 76021 and itemVnum <= 76022:		## ���� �� ������ ȭ���� �ູ
		return 1
	elif itemVnum == 79012:
		return 1
		
	return 0
	
# �ش� vnum�� SP �ڵ������ΰ�
def IS_AUTO_POTION_SP(itemVnum):
	if 72727 <= itemVnum and 72730 >= itemVnum:
		return 1
	elif itemVnum >= 76004 and itemVnum <= 76005:		## ���� �� ������ ������ �ູ
		return 1
	elif itemVnum == 79013:
		return 1
	elif itemVnum == 55701 or itemVnum == 55702 or itemVnum == 55703 or itemVnum == 55704 or itemVnum == 55705:
		return 1
				
	return 0
'''
def IS_AUTO_POTION_SP(itemVnum):
	if 72727 <= itemVnum and 72730 >= itemVnum:
		return 1
	elif itemVnum >= 76004 and itemVnum <= 76005:		## ���� �� ������ ������ �ູ
		return 1
	elif itemVnum == 79013:
		return 1
				
	return 0
'''

if app.LWT_BUFF_UPDATE:	
	def IS_BUFFI(itemVnum):
		items = [91010, 91011]
		return itemVnum in items

talent_window = 0
CURRENT_POINTS = 0
ShowToolTip = [
		[0,	0,	0, 0, 0],	
		[0,	0,	0, 0],	
		[0,	0,	0],	
		[0,	0],	
		[0],	
	]
SKILL_POINTS = [
		[0,	0,	0, 0, 0],	
		[0,	0,	0, 0],	
		[0,	0,	0],	
		[0,	0],	
		[0],	
	]
SKILLUP_BUTTON = [
		[0,	0,	0, 0, 0],	
		[0,	0,	0, 0],	
		[0,	0,	0],	
		[0,	0],	
		[0],	
	]
SKILL_LEARNED = [
		[0,	0,	0, 0, 0],	
		[0,	0,	0, 0],	
		[0,	0,	0],	
		[0,	0],	
		[0],	
	]
	
def minutetohour(time):
	return int((time / 60) / 60) % 24
def minutetominute(time):
	return int((time / 60) % 60)
def minutetosecond(time):
	return int(time % 60)


_interface_instance = None
def GetInterfaceInstance():
	global _interface_instance
	return _interface_instance
def SetInterfaceInstance(instance):
	global _interface_instance
	if _interface_instance:
		del _interface_instance
	_interface_instance = instance

_game_instance = None
def GetGameInstance():
	global _game_instance
	return _game_instance
def SetGameInstance(instance):
	global _game_instance
	if _game_instance:
		del _game_instance
	_game_instance = instance