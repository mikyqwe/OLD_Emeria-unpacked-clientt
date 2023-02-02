import app

OPTION_SHADOW = "SHADOW"

CODEPAGE = str(app.GetDefaultCodePage())

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


if "locale/ymir/" == app.GetLocalePath():

	LOCALE_INTERFACE_FILE_NAME = "locale/ymir/elendosfiles.txt"
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

	LOCALE_INTERFACE_FILE_NAME = "%s/elendosfiles.txt" % (name)

LoadLocaleFile(LOCALE_INTERFACE_FILE_NAME, locals())


