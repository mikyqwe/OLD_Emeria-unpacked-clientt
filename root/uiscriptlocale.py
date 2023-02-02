import app

AUTOBAN_QUIZ_ANSWER = "ANSWER"
AUTOBAN_QUIZ_REFRESH = "REFRESH"
AUTOBAN_QUIZ_REST_TIME = "REST_TIME"

OPTION_DROPFILTER = "Drop Filter"
OPTION_DROPFILTER_ARMOR = "Armor"
OPTION_DROPFILTER_WEAPON = "Weapons" 
OPTION_DROPFILTER_SHIELD = "Shields" 
OPTION_DROPFILTER_JEWELLERY = "Jewellery" 
OPTION_DROPFILTER_HELMET = "Helmets"
OPTION_DROPFILTER_BOOT = "Boots"

OPTION_SHADOW = "SHADOW"

CODEPAGE = str(app.GetDefaultCodePage())

SPECIAL_STORAGE_UPGRADE_TITLE = "Upgrade"
SPECIAL_STORAGE_BOOK_TITLE = "Books"
SPECIAL_STORAGE_STONE_TITLE = "Stones"

#CUBE_TITLE = "Cube Window"

def LoadLocaleFile(srcFileName, localeDict):
	localeDict["CUBE_INFO_TITLE"] = "Recipe"
	localeDict["CUBE_REQUIRE_MATERIAL"] = "Requirements"
	localeDict["CUBE_REQUIRE_MATERIAL_OR"] = "or"
	
	try:
		lines = pack_open(srcFileName, "r").readlines()
	except IOError:
		import dbg
		dbg.LogBox("LoadUIScriptLocaleError(%(srcFileName)s)" % locals())
		app.Abort()

	for line in lines:
		tokens = line[:-1].split("\t")
		
		if len(tokens) >= 2:
			localeDict[tokens[0]] = tokens[1]			
			
		else:
			print len(tokens), lines.index(line), line


if "locale/ymir" == app.GetLocalePath():

	LOCALE_UISCRIPT_PATH	= "locale/ymir_ui/"

	WINDOWS_PATH	= "d:/ymir work/ui/game/949_windows/"
	SELECT_PATH		= "d:/ymir work/ui/intro/949_select/"
	GUILD_PATH		= "d:/ymir work/ui/game/949_guild/"
	EMPIRE_PATH		= "d:/ymir work/ui/intro/949_empire/"
	MAPNAME_PATH		= "locale/ymir_ui/mapname/"
	LOGIN_PATH		= "d:/ymir work/ui/intro/949_login/"

	JOBDESC_WARRIOR_PATH	= "locale/ymir/desc_warrior.txt"
	JOBDESC_ASSASSIN_PATH	= "locale/ymir/desc_assassin.txt"
	JOBDESC_SURA_PATH		= "locale/ymir/desc_sura.txt"
	JOBDESC_SHAMAN_PATH		= "locale/ymir/desc_shaman.txt"

	EMPIREDESC_A = "locale/ymir/desc_empire_a.txt"
	EMPIREDESC_B = "locale/ymir/desc_empire_b.txt"
	EMPIREDESC_C = "locale/ymir/desc_empire_c.txt"
	
	LOCALE_INTERFACE_FILE_NAME = "locale/ymir/locale_interface.txt"	
else:
	if "HONGKONG" == app.GetLocaleServiceName():
		name = "locale/hongkong"
	elif "JAPAN" == app.GetLocaleServiceName():
		name = "locale/japan"
	elif "TAIWAN" == app.GetLocaleServiceName():
		name = "locale/taiwan"
	elif "NEWCIBN" == app.GetLocaleServiceName():
		name = "locale/newcibn"
	elif "EUROPE" == app.GetLocaleServiceName():
		name = app.GetLocalePath()
	else:
		name = "locale/ymir"

	LOCALE_UISCRIPT_PATH = "%s/ui/" % (name)
	LOGIN_PATH = "%s/ui/login/" % (name)
	EMPIRE_PATH = "%s/ui/empire/" % (name)
	GUILD_PATH = "%s/ui/guild/" % (name)
	SELECT_PATH = "%s/ui/select/" % (name)
	WINDOWS_PATH = "%s/ui/windows/" % (name)
	MAPNAME_PATH = "%s/ui/mapname/" % (name)

	JOBDESC_WARRIOR_PATH = "%s/jobdesc_warrior.txt" % (name)
	JOBDESC_ASSASSIN_PATH = "%s/jobdesc_assassin.txt" % (name)
	JOBDESC_SURA_PATH = "%s/jobdesc_sura.txt" % (name)
	JOBDESC_SHAMAN_PATH = "%s/jobdesc_shaman.txt" % (name)

	EMPIREDESC_A = "%s/empiredesc_a.txt" % (name)
	EMPIREDESC_B = "%s/empiredesc_b.txt" % (name)
	EMPIREDESC_C = "%s/empiredesc_c.txt" % (name)
	CARDS_DESC = "mini_game_okey_desc.txt"
	"""	
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
		LOCALE_INTERFACE_FILE_NAME = "%s/locale_interface.txt" % (name)
		
	elif firstLine.split("=")[0] == "Espain":
		LOCALE_INTERFACE_FILE_NAME = "lang\\es/locale_interface.txt"

	elif firstLine.split("=")[0] == "Germany":
		LOCALE_INTERFACE_FILE_NAME = "lang\\gm/locale_interface.txt"
	
	elif firstLine.split("=")[0] == "Poland":
		LOCALE_INTERFACE_FILE_NAME = "lang\\pl/locale_interface.txt"
		
	elif firstLine.split("=")[0] == "Romany":
		LOCALE_INTERFACE_FILE_NAME = "lang\\rm/locale_interface.txt"
		
	elif firstLine.split("=")[0] == "Turkey":
		LOCALE_INTERFACE_FILE_NAME = "lang\\tk/locale_interface.txt"
		
	else:
		LOCALE_INTERFACE_FILE_NAME = "%s/locale_interface.txt" % (name)
"""
	LOCALE_INTERFACE_FILE_NAME = "%s/locale_interface.txt" % (name)

LoadLocaleFile(LOCALE_INTERFACE_FILE_NAME, locals())
