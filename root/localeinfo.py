import app
import constInfo
import net

MAP_TRENT02 = "MAP_TRENT02" # �ӽ�
MAP_WL = "MAP_WL" # �ӽ�
MAP_NUSLUCK = "MAP_NUSLUCK" # �ӽ� 
MAP_TREE2 = "MAP_TREE2"

BLEND_POTION_NO_TIME = " "
BLEND_POTION_NO_INFO = " "

APP_TITLE = "Elendosfiles - The best Metin2 Serverfiles"

GUILD_HEADQUARTER = "Main Building"
GUILD_FACILITY = "Facility"
GUILD_OBJECT = "Object"
GUILD_MEMBER_COUNT_INFINITY = "INFINITY"

LOGIN_FAILURE_WEB_BLOCK = "BLOCK_LOGIN(WEB)"
LOGIN_FAILURE_BLOCK_LOGIN = "BLOCK_LOGIN"
CHANNEL_NOTIFY_FULL = "CHANNEL_NOTIFY_FULL"

GUILD_BUILDING_LIST_TXT = app.GetLocalePath() + "/GuildBuildingList.txt"

GUILD_MARK_MIN_LEVEL = "3"
GUILD_MARK_NOT_ENOUGH_LEVEL = "��巹�� 3�̻� ���� �����մϴ�."

ERROR_MARK_UPLOAD_NEED_RECONNECT = "UploadMark: Reconnect to game"
ERROR_MARK_CHECK_NEED_RECONNECT = "CheckMark: Reconnect to game"

VIRTUAL_KEY_ALPHABET_LOWERS  = r"[1234567890]/qwertyuiop\=asdfghjkl;`'zxcvbnm.,"
VIRTUAL_KEY_ALPHABET_UPPERS  = r'{1234567890}?QWERTYUIOP|+ASDFGHJKL:~"ZXCVBNM<>'
VIRTUAL_KEY_SYMBOLS    = '!@#$%^&*()_+|{}:"<>?~'
VIRTUAL_KEY_NUMBERS    = "1234567890-=\[];',./`"
VIRTUAL_KEY_SYMBOLS_BR    = '!@#$%^&*()_+|{}:"<>?~����������������'

__IS_ENGLISH	= "ENGLISH" == app.GetLocaleServiceName()	
__IS_HONGKONG	= "HONGKONG" == app.GetLocaleServiceName()
__IS_NEWCIBN	= "locale/newcibn" == app.GetLocalePath()
__IS_EUROPE		= "EUROPE" == app.GetLocaleServiceName()		
__IS_CANADA		= "locale/ca" == app.GetLocalePath()
__IS_BRAZIL		= "locale/br" == app.GetLocalePath()
__IS_SINGAPORE	= "locale/sg" == app.GetLocalePath()
__IS_VIETNAM	= "locale/vn" == app.GetLocalePath()
__IS_ARABIC		= "locale/ae" == app.GetLocalePath()
__IS_CIBN10		= "locale/cibn10" == app.GetLocalePath()
__IS_WE_KOREA	= "locale/we_korea" == app.GetLocalePath()
__IS_TAIWAN		= "locale/taiwan" == app.GetLocalePath()
__IS_JAPAN		= "locale/japan" == app.GetLocalePath()	
LOGIN_FAILURE_WRONG_SOCIALID = "ASDF"
LOGIN_FAILURE_SHUTDOWN_TIME = "ASDF"

if __IS_CANADA:
	__IS_EUROPE = TRUE

def IsYMIR():
	return "locale/ymir" == app.GetLocalePath()

def IsJAPAN():
	return "locale/japan" == app.GetLocalePath()

def IsENGLISH():
	global __IS_ENGLISH
	return __IS_ENGLISH

def IsHONGKONG():
	global __IS_HONGKONG
	return __IS_HONGKONG

def IsTAIWAN():
	return "locale/taiwan" == app.GetLocalePath()

def IsNEWCIBN():
	return "locale/newcibn" == app.GetLocalePath()

def IsCIBN10():
	global __IS_CIBN10
	return __IS_CIBN10
	
def IsEUROPE():
	global __IS_EUROPE
	return __IS_EUROPE

def IsCANADA():
	global __IS_CANADA
	return __IS_CANADA

def IsBRAZIL():
	global __IS_BRAZIL
	return __IS_BRAZIL

def IsVIETNAM():
	global __IS_VIETNAM
	return __IS_VIETNAM

def IsSINGAPORE():
	global __IS_SINGAPORE
	return __IS_SINGAPORE
	
def IsARABIC():
	global __IS_ARABIC
	return __IS_ARABIC

def IsWE_KOREA():
	return "locale/we_korea" == app.GetLocalePath()
	
# SUPPORT_NEW_KOREA_SERVER
def LoadLocaleData():
	if IsYMIR():
		import net
		SERVER = "�赵 ����"
		if SERVER == net.GetServerInfo()[:len(SERVER)]:
			app.SetCHEONMA(0)
			app.LoadLocaleData("locale/we_korea")
			constInfo.ADD_DEF_BONUS_ENABLE = 0
		else:
			app.SetCHEONMA(1)
			app.LoadLocaleData("locale/ymir")
			constInfo.ADD_DEF_BONUS_ENABLE = 1
	else:
		app.LoadLocaleData(app.GetLocalePath())

def IsCHEONMA():
	return IsYMIR()		# ���� YMIR �������� ������ õ��������. õ�������� ���� �ݱ� ������ ���� �� ����.

# END_OF_SUPPORT_NEW_KOREA_SERVER

def mapping(**kwargs): return kwargs

def SNA(text):	
	def f(x):
		return text
	return f

def SA(text):
	def f(x):
		return text % x
	return f
	
import app
def FormatTime(time):
	m, s = divmod(time, 60)
	h, m = divmod(m, 60)
	return "%02d:%02d:%02d" % (h, m, s)	

def LoadLocaleFile(srcFileName, localeDict):

	funcDict = {"SA":SA, "SNA":SNA}

	lineIndex = 1

	try:
		lines = pack_open(srcFileName, "r").readlines()
	except IOError:
		import dbg
		dbg.LogBox("LoadLocaleError(%(srcFileName)s)" % locals())
		app.Abort()

	for line in lines:
		try:		
			tokens = line[:-1].split("\t")
			if len(tokens) == 2:
				localeDict[tokens[0]] = tokens[1]
			elif len(tokens) >= 3:
				type = tokens[2].strip()
				if type:
					localeDict[tokens[0]] = funcDict[type](tokens[1])
				else:
					localeDict[tokens[0]] = tokens[1]
			else:
				raise RuntimeError, "Unknown TokenSize"

			lineIndex += 1
		except:
			import dbg
			dbg.LogBox("%s: line(%d): %s" % (srcFileName, lineIndex, line), "Error")
			raise


"""
all = ["locale","error"]
import os
if os.path.exists("lang/idioma.txt"):
	pass
else:
	file = open('lang/idioma.txt', 'a')
	file.write("Espain")
	file.close()

lines = open("lang/idioma.txt").readlines()
firstLine = str(lines[0].replace("\n", ""))
	
if firstLine.split("=")[0] == "Italy":
	LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()
		
elif firstLine.split("=")[0] == "Espain":
	LOCALE_FILE_NAME = "lang\\es/locale_game.txt"

elif firstLine.split("=")[0] == "Germany":
	LOCALE_FILE_NAME = "lang\\gm/locale_game.txt"

elif firstLine.split("=")[0] == "Poland":
	LOCALE_FILE_NAME = "lang\\pl/locale_game.txt"

elif firstLine.split("=")[0] == "Romany":
	LOCALE_FILE_NAME = "lang\\rm/locale_game.txt"
	
elif firstLine.split("=")[0] == "Turkey":
	LOCALE_FILE_NAME = "lang\\tk/locale_game.txt
"""

if IsEUROPE()  and  IsBRAZIL()  :
	FN_GM_MARK = "%s/effect/gm.mse"	% app.GetLocalePath()
	LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()
	constInfo.IN_GAME_SHOP_ENABLE = 0
elif IsSINGAPORE() :
	FN_GM_MARK = "%s/effect/gm.mse"	% app.GetLocalePath()
	LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()
	constInfo.IN_GAME_SHOP_ENABLE = 0
elif IsNEWCIBN() :
	##���Ӹ��̱�����.
	APP_TITLE = "������2"
	FN_GM_MARK = "%s/effect/gm.mse"	% app.GetLocalePath()
	LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()
	constInfo.IN_GAME_SHOP_ENABLE = 1
elif IsTAIWAN():
	APP_TITLE = "��III��"
	FN_GM_MARK = "%s/effect/gm.mse"	% app.GetLocalePath()
	LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()

	constInfo.IN_GAME_SHOP_ENABLE = 1
	
else:
	FN_GM_MARK = "%s/effect/gm.mse"	% app.GetLocalePath()
	LOCALE_FILE_NAME = "%s/locale_game.txt" % app.GetLocalePath()

	constInfo.IN_GAME_SHOP_ENABLE = 1
	
import app
if app.ENABLE_PREMIUM_EFFECT_ABOVE_HEAD:
	FN_PREMIUM_MARK = "%s/effect/premium.mse"	% app.GetLocalePath()
	
LoadLocaleFile(LOCALE_FILE_NAME, globals())

init = False
class localeInfo(object):
	def __init__(self):
		global init

		if not init:
			net.SetLocaleinfoHandler(self)
			init = True

	def __getattribute__(self, name):
		if not globals().has_key(name):
			import dbg
			dbg.TraceError("LanguageError: Key {} not found.".format(name))
			return "Translate-Me"

		return globals()[name]

########################################################################################################
## NOTE : �������� ������ "������/�� �����ðڽ��ϱ�?" ���ڿ��� ���� ������ ���� �ڵ�
dictSingleWord = {
	"m":1, "n":1, "r":1, "M":1, "N":1, "R":1, "l":1, "L":1, "1":1, "3":1, "6":1, "7":1, "8":1, "0":1,
}

dictDoubleWord = {
	"��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1,
	"��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1,
	"��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "�v":1, "��":1, "��":1, "��":1, "�R":1, "��":1, "��":1, "��":1, "��":1, "��":1,
	"��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1,
	"��":1, "�x":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1,
	"��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "�m":1, "��":1, "��":1, "��":1, "�O":1, "��":1, "��":1, "��":1, "��":1, "�l":1,
	"��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1,
	"��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1,
	"��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "�u":1,
	"��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1,
	"��":1, "�X":1, "��":1, "��":1, "��":1, "��":1, "��":1, "�o":1, "��":1, "��":1, "��":1, "�y":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1,
	"��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1,
	"��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "�p":1,
	"¥":1, "¹":1, "¼":1, "��":1, "��":1, "�c":1, "��":1, "��":1, "��":1, "��":1, "°":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "�R":1, "��":1, "��":1, "�n":1,
	"��":1, "í":1, "ó":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "ġ":1, "ä":1, "��":1, "ü":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "�M":1,
	"ī":1, "ļ":1, "Ŀ":1, "��":1, "��":1, "��":1, "��":1, "ť":1, "ũ":1, "Ű":1, "ĳ":1, "�m":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1,
	"Ÿ":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "Ʃ":1, "Ʈ":1, "Ƽ":1, "��":1, "�O":1, "��":1, "��":1, "��":1, "��":1, "��":1, "ơ":1, "��":1, "Ƣ":1, "Ʒ":1,
	"��":1, "��":1, "��":1, "��":1, "��":1, "ǥ":1, "Ǫ":1, "ǻ":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "ǡ":1, "��":1, "Ǵ":1, "�R":1, "ǣ":1, "Ƕ":1, "�c":1,
	"��":1, "��":1, "��":1, "��":1, "ȣ":1, "ȿ":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "��":1, "ȭ":1, "ȳ":1, "��":1, "��":1, "ȸ":1, "��":1, "��":1,
}

locale = mapping(
)


def GetAuxiliaryWordType(text):

	textLength = len(text)

	if textLength > 1:

		singleWord = text[-1]

		if (singleWord >= '0' and singleWord <= '9') or\
			(singleWord >= 'a' and singleWord <= 'z') or\
			(singleWord >= 'A' and singleWord <= 'Z'):
			if not dictSingleWord.has_key(singleWord):
				return 1

		elif dictDoubleWord.has_key(text[-2:]):
			return 1

	return 0



def CutMoneyString(sourceText, startIndex, endIndex, insertingText, backText):

	sourceLength = len(sourceText)

	if sourceLength < startIndex:
		return backText

	text = sourceText[max(0, sourceLength-endIndex):sourceLength-startIndex]

	if not text:
		return backText

	if long(text) <= 0:
		return backText

	text = str(int(text))

	if backText:
		backText = " " + backText

	return text + insertingText + backText

def SecondToDHM(time):
	if time < 60:
		if IsARABIC():
			return "%.2f %s" % (time, SECOND)
		else:
			return "0" + MINUTE
		
	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60) % 24
	day = int(int((time / 60) / 60) / 24)

	text = ""

	if day > 0:
		text += str(day) + DAY
		text += " "

	if hour > 0:
		text += str(hour) + HOUR
		text += " "

	if minute > 0:
		text += str(minute) + MINUTE

	return text

def SecondToHM(time):

	if time < 60:
		if IsARABIC():
			return "%.2f %s" % (time, SECOND)
		else:
			return "0" + MINUTE

	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60)

	text = ""

	if hour > 0:
		text += str(hour) + HOUR
		if hour > 0:
			text += " "

	if minute > 0:
		text += str(minute) + MINUTE

	return text

def SecondToHMS(time):
	if time < 60:
		return "%d%s" % (time, SECOND)

	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60) % 24

	text = ""

	if hour > 0:
		text += str(hour) + HOUR
		if hour > 0:
			text += " "

	if minute > 0:
		text += str(minute) + MINUTE
		if minute > 0:
			text += " "

	if second > 0:
		text += str(second) + SECOND

	return text

if app.ENABLE_NEW_PET_SYSTEM:
	def SecondToPetTime(time):
		if time < 60:
			return "0" + MINUTE

		second = int(time % 60)
		minute = int((time / 60) % 60)
		hour = int((time / 60) / 60)
		day = int(int((time / 60) / 60) / 24)

		text = ""

		if day > 0:
			if day == 1:
				text += str(day) + " " + PET_INFORMATION_DAY
			else:
				text += str(day) + " " + PET_INFORMATION_DAYS
			text += " "

		elif hour > 0:
			if hour == 1:
				text += str(hour) + " " + PET_INFORMATION_HOUR
			else:
				text += str(hour) + " " + PET_INFORMATION_HOURS
			text += " "

		elif minute > 0:
			if minute == 1:
				text += str(minute) + " " + PET_INFORMATION_MINUTE
			else:
				text += str(minute) + " " + PET_INFORMATION_MINUTES

		return text
		
	def SecondToPetLifeTime(time):
		if time < 86400:
			return "0" + DAY

		day = int(int((time / 60) / 60) / 24)

		text = ""

		if day > 0:
			text += str(day) + DAY

		return text

	def PetTimeTextInfo(time):
		minute = int(time % 60)
		hour = int(time / 60) % 24
		day = int(int((time / 60) / 24))

		text = ""

		if day > 0:
			text += str(day) + DAY
			text += " "

		if hour > 0:
			text += str(hour) + HOUR
			text += " "

		if minute > 0:
			text += str(minute) + MINUTE

		return text

def PlayerTimeTextIntroSel(time):
	if time == 0:
		return "0 " + HOUR + " - " + "0 " + MINUTE

	minute = int(time) % 60
	hour = int(time / 60)

	text = ""
	
	text += str(hour) + " " + HOUR
	text += " - "

	text += str(minute) + " " + MINUTE

	return text

def GetAlignmentTitleName(alignment):
	if alignment >= 12000:
		return TITLE_NAME_LIST[0]
	elif alignment >= 8000:
		return TITLE_NAME_LIST[1]
	elif alignment >= 4000:
		return TITLE_NAME_LIST[2]
	elif alignment >= 1000:
		return TITLE_NAME_LIST[3]
	elif alignment >= 0:
		return TITLE_NAME_LIST[4]
	elif alignment > -4000:
		return TITLE_NAME_LIST[5]
	elif alignment > -8000:
		return TITLE_NAME_LIST[6]
	elif alignment > -12000:
		return TITLE_NAME_LIST[7]

	return TITLE_NAME_LIST[8]
	
if app.ENABLE_REBORN_SYSTEM:	
	TITLEREBORN_NAME_LIST = (REBORN_LEVEL1, REBORN_LEVEL2, REBORN_LEVEL3, REBORN_NONE)
	
if app.ENABLE_REBORN_SYSTEM:	
	def GetRebornTitleName(reborn):
		if reborn == 1:
			return TITLEREBORN_NAME_LIST[2]
		elif reborn == 2:
			return TITLEREBORN_NAME_LIST[1]
		elif reborn == 3:
			return TITLEREBORN_NAME_LIST[0]
		elif reborn == 0:
			return TITLEREBORN_NAME_LIST[3]
	
if app.ENABLE_TITLE_SYSTEM:
	TITLEPRESTIGE_NAME_LIST = (TITLE_1,TITLE_2,TITLE_3,TITLE_4,TITLE_5,TITLE_6,TITLE_7,TITLE_8,TITLE_9,TITLE_10,TITLE_11,TITLE_12,TITLE_13,TITLE_14,TITLE_15,TITLE_16,TITLE_17,TITLE_18,TITLE_19,TITLE_0)

if app.ENABLE_TITLE_SYSTEM:	
	def GetPrestigeTitleName(prestige):
		if prestige == 1:
			return TITLEPRESTIGE_NAME_LIST[0]
		elif prestige == 2:
			return TITLEPRESTIGE_NAME_LIST[1]
		elif prestige == 3:
			return TITLEPRESTIGE_NAME_LIST[2]
		elif prestige == 4:
			return TITLEPRESTIGE_NAME_LIST[3]
		elif prestige == 5:
			return TITLEPRESTIGE_NAME_LIST[4]
		elif prestige == 6:
			return TITLEPRESTIGE_NAME_LIST[5]
		elif prestige == 7:
			return TITLEPRESTIGE_NAME_LIST[6]
		elif prestige == 8:
			return TITLEPRESTIGE_NAME_LIST[7]
		elif prestige == 9:
			return TITLEPRESTIGE_NAME_LIST[8]
		elif prestige == 10:
			return TITLEPRESTIGE_NAME_LIST[9]
		elif prestige == 11:
			return TITLEPRESTIGE_NAME_LIST[10]
		elif prestige == 12:
			return TITLEPRESTIGE_NAME_LIST[11]
		elif prestige == 13:
			return TITLEPRESTIGE_NAME_LIST[12]
		elif prestige == 14:
			return TITLEPRESTIGE_NAME_LIST[13]
		elif prestige == 15:
			return TITLEPRESTIGE_NAME_LIST[14]
		elif prestige == 16:
			return TITLEPRESTIGE_NAME_LIST[15]
		elif prestige == 17:
			return TITLEPRESTIGE_NAME_LIST[16]
		elif prestige == 18:
			return TITLEPRESTIGE_NAME_LIST[17]
		elif prestige == 19:
			return TITLEPRESTIGE_NAME_LIST[18]
		elif prestige == 0:
			return TITLEPRESTIGE_NAME_LIST[19]

OPTION_PVPMODE_MESSAGE_DICT = {
	0 : PVP_MODE_NORMAL,
	1 : PVP_MODE_REVENGE,
	2 : PVP_MODE_KILL,
	3 : PVP_MODE_PROTECT,
	4 : PVP_MODE_GUILD,
}

error = mapping(
	CREATE_WINDOW = GAME_INIT_ERROR_MAIN_WINDOW,
	CREATE_CURSOR = GAME_INIT_ERROR_CURSOR,
	CREATE_NETWORK = GAME_INIT_ERROR_NETWORK,
	CREATE_ITEM_PROTO = GAME_INIT_ERROR_ITEM_PROTO,
	CREATE_MOB_PROTO = GAME_INIT_ERROR_MOB_PROTO,
	CREATE_NO_DIRECTX = GAME_INIT_ERROR_DIRECTX,
	CREATE_DEVICE = GAME_INIT_ERROR_GRAPHICS_NOT_EXIST,
	CREATE_NO_APPROPRIATE_DEVICE = GAME_INIT_ERROR_GRAPHICS_BAD_PERFORMANCE,
	CREATE_FORMAT = GAME_INIT_ERROR_GRAPHICS_NOT_SUPPORT_32BIT,
	NO_ERROR = ""
)


GUILDWAR_NORMAL_DESCLIST = [GUILD_WAR_USE_NORMAL_MAP, GUILD_WAR_LIMIT_30MIN, GUILD_WAR_WIN_CHECK_SCORE]
GUILDWAR_WARP_DESCLIST = [GUILD_WAR_USE_BATTLE_MAP, GUILD_WAR_WIN_WIPE_OUT_GUILD, GUILD_WAR_REWARD_POTION]
GUILDWAR_CTF_DESCLIST = [GUILD_WAR_USE_BATTLE_MAP, GUILD_WAR_WIN_TAKE_AWAY_FLAG1, GUILD_WAR_WIN_TAKE_AWAY_FLAG2, GUILD_WAR_REWARD_POTION]

MINIMAP_ZONE_NAME_DICT = {
	"metin2_map_a1"  : MAP_A1,
	"map_a2"         : MAP_A2,
	"metin2_map_a3"  : MAP_A3,
	"metin2_map_b1"  : MAP_B1,
	"map_b2"         : MAP_B2,
	"metin2_map_b3"  : MAP_B3,
	"metin2_map_c1"  : MAP_C1,
	"map_c2"         : MAP_C2,
	"metin2_map_c3"  : MAP_C3,
	"map_n_snowm_01" : MAP_SNOW,
	"metin2_map_n_flame_01" : MAP_FLAME,
	"metin2_map_n_desert_01" : MAP_DESERT,
	"metin2_map_milgyo" : MAP_TEMPLE,
	"metin2_map_spiderdungeon" : MAP_SPIDER,
	"metin2_map_deviltower1" : MAP_SKELTOWER,
	"metin2_map_guild_01" : MAP_AG,
	"metin2_map_guild_02" : MAP_BG,
	"metin2_map_guild_03" : MAP_CG,
	"metin2_map_trent" : MAP_TREE,
	"metin2_map_trent02" : MAP_TREE2,
	"season1/metin2_map_WL_01" : MAP_WL,
	"season1/metin2_map_nusluck01" : MAP_NUSLUCK,
    "Metin2_map_CapeDragonHead" : MAP_CAPE,
    "metin2_map_Mt_Thunder" : MAP_THUNDER,
    "metin2_map_dawnmistwood" : MAP_DAWN,
    "metin2_map_BayBlackSand" : MAP_BAY,
}



JOBINFO_TITLE = [
	[JOB_WARRIOR0, JOB_WARRIOR1, JOB_WARRIOR2,],
	[JOB_ASSASSIN0, JOB_ASSASSIN1, JOB_ASSASSIN2,],
	[JOB_SURA0, JOB_SURA1, JOB_SURA2,],
	[JOB_SHAMAN0, JOB_SHAMAN1, JOB_SHAMAN2,],
]

JOBINFO_DATA_LIST = [
	[
		["Ÿ���� ��Ͱ� ������ �ʴ� ������",
		"�ⰳ�� ������� ���þ� [����]���",
		"�θ���. ��� ���⿡���� �׵��� ",
		"�ڷ� �������� ������, ��ġ�� ����",
		"�̱� ���� ���Ḧ ���� �ܽ�����",
		"����� ���� �ο�⵵ �Ѵ�. �̵���",
		"�� �ܷõ� ������ ��, ������ ���ݷ�",
		"���� ���� �ּ��ο��� ����������",
		"Ȱ���Ѵ�.                      ",],
		["���� �Ϲ����� ������ �����, ",
		"�������� ���� ���� �������� ����",
		"���� Ȱ���Ѵ�. ���� Ư���� �ٷ���",
		"�������� ���� ����Ʈ�� �����ϵ�, ",
		"�������� ���� ������ / ����",
		"Ȯ���� ���� ü���� �ø���. ����",
		"������ ��Ȯ���� ���̱� ���� ��ø",
		"���� ����Ʈ�� ������ �ʿ䰡 �ִ�.",],
		["��� ������ ���ŷ��� �̿��ϴ�",
		"��/�ٰŸ� ������ �����, �� ���",
		"�ϳ��ϳ��� ���� ���ݷ����� ���忡��",
		"Ȱ���Ѵ�. ���� Ư���� �ٷ��� ����",
		"���� ���� ����Ʈ�� �����ϵ�, ",
		"��/�ٰŸ� ������ ��Ȯ���� ���߷���",
		"���� ��ø�� �ø���. ���� ���� �� ",
		"�� ���ݿ� ���� ������ / ����",
		"Ȯ���� ���� ü�¿��� ����Ʈ��",
		"������ �ʿ䰡 �ִ�.        ",],		
	],
	[
		["�ڰ��� ��� ��Ȳ������ �ڽ���",
		"���� ����� ������ ����� �ӹ���",
		"�����ϸ鼭 ������ ������ �����ϴ�", 
		"�ڵ��̴�. �̵��� ���� ������ �ż�",
		"�ϸ�, ���� �� ���� �����ϰ� ������",
		"�ൿ���� ���� �޼ҿ� ġ��Ÿ�� ����",
		"��, ���忡�� ������ ���� ������",
		"ȭ���� �������� �ڽ��� �����",
		"�����δ�.                   "],
		["�μ� �ܰ��� �ֹ���� �ٷ��, �ż�",
		"�ϰ� ġ�� ������ �ڰ� Ư���� ������",
		"���� ���忡�� Ȱ���Ѵ�. ���� Ư����",
		"��ø�� �������� ���� ����Ʈ�� ����",
		"�ϵ�, �ٷ��� �÷� ���ݷ��� ���δ�.",
		"���� �������� ���� ������/���� ",
		"����� ���� ü�¿��� ����Ʈ��",
		"������ �ʿ䰡 �ִ�.          ",],
		["Ȱ�� �ֹ���� �ٷ��, �� �þ߿�",
		"�����Ÿ��� ���� ���Ÿ� ��������",
		"���忡�� Ȱ���Ѵ�. ���� Ư����",
		"���� �������� ������ ���� ��ø��",
		"�������� �÷��� �ϸ�, ���Ÿ�",
		"������ ������ ������ ���� �ٷ���",
		"�ø� �ʿ䰡 �ִ�. ���� ���鿡��",
		"�����Ǿ��� ��, �� ���ݿ� ��Ƽ��",
		"���� ������/���� ����� ����",
		"ü�¿��� ����Ʈ�� ������ �ʿ䰡",
		"�ִ�.                        ", ],
	],
	[
		["����� [���� ������]�� �Ӽ�����",
		"â���� Ư�� �Ӽ��� �����̴�. ",
		"�׵��� ���忡�� ������ ��⸦ ����",
		"��Ű��, �Ǹ��� ���� ���� ��ź����",
		"���� ��ȥ�� ������ ��������. ����",
		"�̵��� �ڽ��� �˰� ���ʿ� �����",
		"���� �Ǿ�, ���忡�� ���� ���� ����",
		"���ݷ��� �����ϱ⵵ �ϴµ�, ������",
		"�׿���±� ����� ������ ������",
		"������� ���� ���þ� [����]�̶�",
		"�θ��⸦ ���� �ɴ´�."],
		["ȯ������ ����� �Ǹ��� ������",
		"������� ������ ���⳪ ����",
		"�Ǿ� ���� ���� ���� ����������",
		"���忡�� Ȱ���Ѵ�. ���� Ư����",
		"������ ���������� ���� ���", 
		"�Ǹ��� ������ ������ ����ǹǷ�,",
		"���ɰ� �ٷ��� �������� ����",
		"����Ʈ�� �����ϵ�, ������ ����",
		"������/���� Ȯ���� ���� ü����",
		"�ø���. ���� ������ ��Ȯ����",
		"ȸ�Ǹ� ���ؼ� ��ø���� ����Ʈ��",
		"������ �ʿ䰡 �ִ�.           ",],
		["�渶���� ������� ���� �����",
		"�ֹ��� �Ǹ��� �������� ���忡��",
		"Ȱ���Ѵ�. ���� Ư���� ���� ������",
		"���̹Ƿ� ������ �������� ����",
		"����Ʈ�� �����ϵ�, ���Ÿ� ����",
		"������ ��Ȯ���� ���� ��ø�� �ø���.",
		"���� ���� �Ǿ�����, �� ���ݿ� ����",
		"������ / ���� Ȯ���� ���� ü�¿���",
		"����Ʈ�� ������ �ʿ䰡 �ִ�.    ",],
	],
	[
		["������ ��Ű� �ڿ�, �� ������",
		"���� �ٷ� �� �ִ� ������ �����̴�.",
		"�׵��� �Ĺ濡�� �Ʊ��� �����ϰ�",
		"��ģ ������ �λ��� ȸ�� ��Ű��",
		"������ ��⸦ ��½�Ų��. �׵���",
		"�Ʊ��� ����� �޽��� �����ϴ� �ڸ� ",
		"���� �뼭���� ������, �׷� �ڵ�",
		"���Դ� �� �� ���� ���� �ֹ���",
		"��Ʈ�� �� ������� ���� ¡���Ѵ�.",],
		["õ�決�� ������� ���� ��������",
		"�����ֹ��� ���ϸ�, ���� �� / ����",
		"�������κ��� �Ʊ��� ��Ų��. ����",
		"Ư���� ���� �ɷ��� ���̹Ƿ� ������",
		"�������� ���� ����Ʈ�� �����ϵ�,",
		"�����Ǿ��� ��, �� ���ݿ� ����",
		"������ / ���� Ȯ���� ���� ü����",
		"�ø���. ���� ���Ÿ� ���� ������",
		"��Ȯ���� ���� ��ø���� ����Ʈ��",
		"������ �ʿ䰡 �ִ�.           ",],
		["���ڱ��� ������� �ڿ��� ����",
		"���� �Ʊ��� ȸ���ϰ�, ������ ",
		"������ ������ ���鿡�� ū �����",
		"���� �� �ִ� �̵��̴�. ������",
		"Ư���� ���� �ɷ��� ���̹Ƿ� ������",
		"�������� ���� ����Ʈ�� �����ϵ�,",
		"�����Ǿ�����, �� ���ݿ� ����",
		"������ / ���� Ȯ���� ���� ü����",
		"�ø���. ���� ���Ÿ� ���� ������",
		"��Ȯ���� ���� ��ø���� ����Ʈ��",
		"������ �ʿ䰡 �ִ�.             "],
	],
]


WHISPER_ERROR = {
	1 : CANNOT_WHISPER_NOT_LOGON,
	2 : CANNOT_WHISPER_DEST_REFUSE,
	3 : CANNOT_WHISPER_SELF_REFUSE,
}

NOTIFY_MESSAGE = {
	"CANNOT_EQUIP_SHOP" : CANNOT_EQUIP_IN_SHOP,
	"CANNOT_EQUIP_EXCHANGE" : CANNOT_EQUIP_IN_EXCHANGE,
}


ATTACK_ERROR_TAIL_DICT = {
	"IN_SAFE" : CANNOT_ATTACK_SELF_IN_SAFE,
	"DEST_IN_SAFE" : CANNOT_ATTACK_DEST_IN_SAFE,
}

SHOT_ERROR_TAIL_DICT = {
	"EMPTY_ARROW" : CANNOT_SHOOT_EMPTY_ARROW,
	"IN_SAFE" : CANNOT_SHOOT_SELF_IN_SAFE,
	"DEST_IN_SAFE" : CANNOT_SHOOT_DEST_IN_SAFE,
}
	
USE_SKILL_ERROR_TAIL_DICT = {	
	"IN_SAFE" : CANNOT_SKILL_SELF_IN_SAFE,
	"NEED_TARGET" : CANNOT_SKILL_NEED_TARGET,
	"NEED_EMPTY_BOTTLE" : CANNOT_SKILL_NEED_EMPTY_BOTTLE,
	"NEED_POISON_BOTTLE" : CANNOT_SKILL_NEED_POISON_BOTTLE,
	"REMOVE_FISHING_ROD" : CANNOT_SKILL_REMOVE_FISHING_ROD,
	"NOT_YET_LEARN" : CANNOT_SKILL_NOT_YET_LEARN,
	"NOT_MATCHABLE_WEAPON" : CANNOT_SKILL_NOT_MATCHABLE_WEAPON,
	"WAIT_COOLTIME" : CANNOT_SKILL_WAIT_COOLTIME,
	"NOT_ENOUGH_HP" : CANNOT_SKILL_NOT_ENOUGH_HP,
	"NOT_ENOUGH_SP" : CANNOT_SKILL_NOT_ENOUGH_SP,
	"CANNOT_USE_SELF" : CANNOT_SKILL_USE_SELF,
	"ONLY_FOR_ALLIANCE" : CANNOT_SKILL_ONLY_FOR_ALLIANCE,
	"CANNOT_ATTACK_ENEMY_IN_SAFE_AREA" : CANNOT_SKILL_DEST_IN_SAFE,
	"CANNOT_APPROACH" : CANNOT_SKILL_APPROACH,
	"CANNOT_ATTACK" : CANNOT_SKILL_ATTACK,
	"ONLY_FOR_CORPSE" : CANNOT_SKILL_ONLY_FOR_CORPSE,
	"EQUIP_FISHING_ROD" : CANNOT_SKILL_EQUIP_FISHING_ROD, 
	"NOT_HORSE_SKILL" : CANNOT_SKILL_NOT_HORSE_SKILL,
	"HAVE_TO_RIDE" : CANNOT_SKILL_HAVE_TO_RIDE,
}

LEVEL_LIST=["", HORSE_LEVEL1, HORSE_LEVEL2, HORSE_LEVEL3]

HEALTH_LIST=[
	HORSE_HEALTH0,
	HORSE_HEALTH1, 
	HORSE_HEALTH2,
	HORSE_HEALTH3,
]


USE_SKILL_ERROR_CHAT_DICT = {	
	"NEED_EMPTY_BOTTLE" : SKILL_NEED_EMPTY_BOTTLE,
	"NEED_POISON_BOTTLE" : SKILL_NEED_POISON_BOTTLE, 
	"ONLY_FOR_GUILD_WAR" : SKILL_ONLY_FOR_GUILD_WAR,
}

SHOP_ERROR_DICT = {
	"NOT_ENOUGH_MONEY" : SHOP_NOT_ENOUGH_MONEY,
	"SOLDOUT" : SHOP_SOLDOUT,
	"INVENTORY_FULL" : SHOP_INVENTORY_FULL,
	"INVALID_POS" : SHOP_INVALID_POS,
	"NOT_ENOUGH_MONEY_EX" : SHOP_NOT_ENOUGH_MONEY_EX,
}

if app.ENABLE_MULTISHOP:
	SHOP_ERROR_DICT.update({
		"NOT_ENOUGH_ITEM" : SHOP_NOT_ENOUGH_ITEM,
		}
	)

STAT_MINUS_DESCRIPTION = {
	"HTH-" : STAT_MINUS_CON,
	"INT-" : STAT_MINUS_INT,
	"STR-" : STAT_MINUS_STR,
	"DEX-" : STAT_MINUS_DEX,
}

MODE_NAME_LIST = ( PVP_OPTION_NORMAL, PVP_OPTION_REVENGE, PVP_OPTION_KILL, PVP_OPTION_PROTECT, )
TITLE_NAME_LIST = ( PVP_LEVEL0, PVP_LEVEL1, PVP_LEVEL2, PVP_LEVEL3, PVP_LEVEL4, PVP_LEVEL5, PVP_LEVEL6, PVP_LEVEL7, PVP_LEVEL8, )

def GetLetterImageName():
	return "interface_EmperorApollo/icons/special/scroll_close.png"
def GetLetterOpenImageName():
	return "interface_EmperorApollo/icons/special/scroll_open.png"
def GetLetterCloseImageName():
	return "interface_EmperorApollo/icons/special/scroll_close.png"

def DO_YOU_SELL_ITEM(sellItemName, sellItemCount, sellItemPrice):
	if sellItemCount > 1 :
		return DO_YOU_SELL_ITEM2 % (sellItemName, sellItemCount, NumberToMoneyString(sellItemPrice) )
	else:
		return DO_YOU_SELL_ITEM1 % (sellItemName, NumberToMoneyString(sellItemPrice) )

def DO_YOU_BUY_ITEM(buyItemName, buyItemCount, buyItemPrice) :
	if buyItemCount > 1 :
		return DO_YOU_BUY_ITEM2 % ( buyItemName, buyItemCount, buyItemPrice )
	else:
		return DO_YOU_BUY_ITEM1 % ( buyItemName, buyItemPrice )
		
def REFINE_FAILURE_CAN_NOT_ATTACH(attachedItemName) :
	return REFINE_FAILURE_CAN_NOT_ATTACH0 % (attachedItemName)

def REFINE_FAILURE_NO_SOCKET(attachedItemName) :
	return REFINE_FAILURE_NO_SOCKET0 % (attachedItemName)

def REFINE_FAILURE_NO_GOLD_SOCKET(attachedItemName) :
	return REFINE_FAILURE_NO_GOLD_SOCKET0 % (attachedItemName)
	
def HOW_MANY_ITEM_DO_YOU_DROP(dropItemName, dropItemCount) :
	if dropItemCount > 1 :
		return HOW_MANY_ITEM_DO_YOU_DROP2 % (dropItemName, dropItemCount)
	else :	
		return HOW_MANY_ITEM_DO_YOU_DROP1 % (dropItemName)

def FISHING_NOTIFY(isFish, fishName) :
	if isFish :
		return FISHING_NOTIFY1 % ( fishName )
	else :
		return FISHING_NOTIFY2 % ( fishName )

def FISHING_SUCCESS(isFish, fishName) :
	if isFish :
		return FISHING_SUCCESS1 % (fishName)
	else :
		return FISHING_SUCCESS2 % (fishName)
		
def NumberToMoneyString(n) :
	if n <= 0 :
		return "0 %s" % (MONETARY_UNIT0)

	return "%s %s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]), MONETARY_UNIT0) 

def NumberToSecondaryCoinString(n) :
	if n <= 0 :
		return "0 %s" % (MONETARY_UNIT_JUN)

	return "%s %s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]), MONETARY_UNIT_JUN) 
	
def NumberToEXPString(n) :
	if n <= 0 :
		return "0"

	return "%s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]))

def NumberToWithItemString(n,c):
	if n <= 0:
		return "0 %s" % (c)
	return "%s %s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]), c)
		
def NumberWithPoint(n) :
	if n <= 0 :
		return "0"

	return "%s" % ('.'.join([ i-3<0 and str(n)[:i] or str(n)[i-3:i] for i in range(len(str(n))%3, len(str(n))+1, 3) if i ]))

def SecondToDHMS(time):
	second = int(time % 60)
	minute = int((time / 60) % 60)
	hour = int((time / 60) / 60) % 24
	day = int(int((time / 60) / 60) / 24)

	text = ""

	if day > 0:
		text += str(day) + " " + DAY
		text += " "

	if hour > 0:
		text += str(hour) + " " + HOUR
		text += " "

	if minute > 0:
		text += str(minute) + " " + MINUTE
		text += " "

	if second > 0:
		text += str(second) + " " + SECOND

	return text
