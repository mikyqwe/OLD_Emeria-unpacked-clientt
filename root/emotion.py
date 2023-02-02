import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import player
import chrmgr
import chr
import app

EMOTION_VERSION = 2

if EMOTION_VERSION == 2:
	EMOTION_CLAP = 1
	EMOTION_CONGRATULATION = 2
	EMOTION_FORGIVE = 3
	EMOTION_ANGRY = 4
	EMOTION_ATTRACTIVE = 5
	EMOTION_SAD = 6
	EMOTION_SHY = 7
	EMOTION_CHEERUP = 8
	EMOTION_BANTER = 9
	EMOTION_JOY = 10
	EMOTION_CHEERS_1 = 11
	EMOTION_CHEERS_2 = 12
	EMOTION_DANCE_1 = 13
	EMOTION_DANCE_2 = 14
	EMOTION_DANCE_3 = 15
	EMOTION_DANCE_4 = 16
	EMOTION_DANCE_5 = 17
	EMOTION_DANCE_6 = 18
	EMOTION_KISS = 51
	EMOTION_FRENCH_KISS = 52
	EMOTION_SLAP = 53
	if app.ENABLE_NEW_EMOTION_SYSTEM:
		EMOTION_BACKFLIP 	= app.SLOT_EMOTION_START
		EMOTION_BOXING		= app.SLOT_EMOTION_START + 1
		EMOTION_BREAKDANCE	= app.SLOT_EMOTION_START + 2
		EMOTION_DAB			= app.SLOT_EMOTION_START + 3
		EMOTION_FACEPALM	= app.SLOT_EMOTION_START + 4
		EMOTION_JERKOFF		= app.SLOT_EMOTION_START + 5
		EMOTION_NEW_DANCE_1	= app.SLOT_EMOTION_START + 6
		EMOTION_PUSHKICK	= app.SLOT_EMOTION_START + 7
		EMOTION_THROW_MONEY	= app.SLOT_EMOTION_START + 8
		EMOTION_NEW_DANCE_2	= app.SLOT_EMOTION_START + 9
		EMOTION_TWERK		= app.SLOT_EMOTION_START + 10
		EMOTION_SEX 		= app.SLOT_EMOTION_START + 11
		EMOTION_LICKING 	= app.SLOT_EMOTION_START + 12
		EMOTION_BLOWJOB 	= app.SLOT_EMOTION_START + 13
	
	EMOTION_DICT = {
		EMOTION_CLAP :			{"name": localeInfo.EMOTION_CLAP, 		"command":"/clap"},
		EMOTION_DANCE_1 :		{"name": localeInfo.EMOTION_DANCE_1, 	"command":"/dance1"},
		EMOTION_DANCE_2 :		{"name": localeInfo.EMOTION_DANCE_2, 	"command":"/dance2"},
		EMOTION_DANCE_3 :		{"name": localeInfo.EMOTION_DANCE_3, 	"command":"/dance3"},
		EMOTION_DANCE_4 :		{"name": localeInfo.EMOTION_DANCE_4, 	"command":"/dance4"},
		EMOTION_DANCE_5 :		{"name": localeInfo.EMOTION_DANCE_5, 	"command":"/dance5"},
		EMOTION_DANCE_6 :		{"name": localeInfo.EMOTION_DANCE_6, 	"command":"/dance6"},
		EMOTION_CONGRATULATION :	{"name": localeInfo.EMOTION_CONGRATULATION,	"command":"/congratulation"},
		EMOTION_FORGIVE :		{"name": localeInfo.EMOTION_FORGIVE, 	"command":"/forgive"},
		EMOTION_ANGRY :			{"name": localeInfo.EMOTION_ANGRY, 		"command":"/angry"},
		EMOTION_ATTRACTIVE :		{"name": localeInfo.EMOTION_ATTRACTIVE, 	"command":"/attractive"},
		EMOTION_SAD :			{"name": localeInfo.EMOTION_SAD, 		"command":"/sad"},
		EMOTION_SHY :			{"name": localeInfo.EMOTION_SHY, 		"command":"/shy"},
		EMOTION_CHEERUP :		{"name": localeInfo.EMOTION_CHEERUP, 	"command":"/cheerup"},
		EMOTION_BANTER :		{"name": localeInfo.EMOTION_BANTER, 	"command":"/banter"},
		EMOTION_JOY :			{"name": localeInfo.EMOTION_JOY, 		"command":"/joy"},
		EMOTION_CHEERS_1 :		{"name": localeInfo.EMOTION_CHEERS_1, 	"command":"/cheer1"},
		EMOTION_CHEERS_2 :		{"name": localeInfo.EMOTION_CHEERS_2, 	"command":"/cheer2"},
		EMOTION_KISS :			{"name": localeInfo.EMOTION_CLAP_KISS, 	"command":"/kiss"},
		EMOTION_FRENCH_KISS :		{"name": localeInfo.EMOTION_FRENCH_KISS, 	"command":"/french_kiss"},
		EMOTION_SLAP :			{"name": localeInfo.EMOTION_SLAP, 		"command":"/slap"},
		
		EMOTION_BACKFLIP :		{"name": localeInfo.EMOTION_BACKFLIP, 		"command":"/backflip"},
		EMOTION_BOXING :		{"name": localeInfo.EMOTION_BOXING, 		"command":"/boxing"},
		EMOTION_BREAKDANCE :	{"name": localeInfo.EMOTION_BREAKDANCE, 	"command":"/breakdance"},
		EMOTION_DAB :			{"name": localeInfo.EMOTION_DAB, 			"command":"/dab"},
		EMOTION_FACEPALM :		{"name": localeInfo.EMOTION_FACEPALM, 		"command":"/facepalm"},
		EMOTION_JERKOFF :		{"name": localeInfo.EMOTION_JERKOFF, 		"command":"/jerkoff"},
		EMOTION_NEW_DANCE_1 :	{"name": localeInfo.EMOTION_NEW_DANCE_1,	"command":"/new_dance_1"},
		EMOTION_PUSHKICK :		{"name": localeInfo.EMOTION_PUSHKICK, 		"command":"/pushkick"},
		EMOTION_THROW_MONEY :	{"name": localeInfo.EMOTION_THROW_MONEY, 	"command":"/throw_money"},
		EMOTION_NEW_DANCE_2 :	{"name": localeInfo.EMOTION_NEW_DANCE_2, 	"command":"/new_dance_2"},
		EMOTION_TWERK :			{"name": localeInfo.EMOTION_TWERK, 			"command":"/twerk"},
		
		EMOTION_SEX :			{"name": localeInfo.EMOTION_SEX, 			"command":"/sex"},
		EMOTION_LICKING :		{"name": localeInfo.EMOTION_LICKING, 		"command":"/licking"},
		EMOTION_BLOWJOB :		{"name": localeInfo.EMOTION_BLOWJOB, 		"command":"/blowjob"},
	}
	#if app.ENABLE_NEW_EMOTION_SYSTEM:
	#	 EMOTION_DICT.update({
	#		EMOTION_BACKFLIP :		{"name": localeInfo.EMOTION_BACKFLIP, 		"command":"/backflip"},
	#		EMOTION_BOXING :		{"name": localeInfo.EMOTION_BOXING, 		"command":"/boxing"},
	#		EMOTION_BREAKDANCE :	{"name": localeInfo.EMOTION_BREAKDANCE, 	"command":"/breakdance"},
	#		EMOTION_DAB :			{"name": localeInfo.EMOTION_DAB, 			"command":"/dab"},
	#		EMOTION_FACEPALM :		{"name": localeInfo.EMOTION_FACEPALM, 		"command":"/facepalm"},
	#		EMOTION_JERKOFF :		{"name": localeInfo.EMOTION_JERKOFF, 		"command":"/jerkoff"},
	#		EMOTION_NEW_DANCE_1 :	{"name": localeInfo.EMOTION_NEW_DANCE_1,	"command":"/new_dance_1"},
	#		EMOTION_PUSHKICK :		{"name": localeInfo.EMOTION_PUSHKICK, 		"command":"/pushkick"},
	#		EMOTION_THROW_MONEY :	{"name": localeInfo.EMOTION_THROW_MONEY, 	"command":"/throw_money"},
	#		EMOTION_NEW_DANCE_2 :	{"name": localeInfo.EMOTION_NEW_DANCE_2, 	"command":"/new_dance_2"},
	#		EMOTION_TWERK :			{"name": localeInfo.EMOTION_TWERK, 			"command":"/twerk"},
	#		
	#		EMOTION_SEX :			{"name": localeInfo.EMOTION_SEX, 			"command":"/sex"},
	#		EMOTION_LICKING :		{"name": localeInfo.EMOTION_LICKING, 		"command":"/licking"},
	#		EMOTION_BLOWJOB :		{"name": localeInfo.EMOTION_BLOWJOB, 		"command":"/blowjob"},
	#	 })
	
	ICON_DICT = {
		#EMOTION_CLAP 		: 	"interface_emperorapollo/common/emotions/clap.png",
		#EMOTION_CHEERS_1	:	"interface_emperorapollo/common/emotions/happy.png",
		#EMOTION_CHEERS_2	:	"interface_emperorapollo/common/emotions/cheerup.png",

		#EMOTION_DANCE_1		:	"interface_emperorapollo/common/emotions/dance1.png",
		#EMOTION_DANCE_2		:	"interface_emperorapollo/common/emotions/dance2.png",

		#EMOTION_CONGRATULATION	:	"interface_emperorapollo/common/emotions/congratulation.png",
		#EMOTION_FORGIVE		:	"interface_emperorapollo/common/emotions/forgive.png",
		#EMOTION_ANGRY		:	"interface_emperorapollo/common/emotions/angry.png",
		#EMOTION_ATTRACTIVE	:	"interface_emperorapollo/common/emotions/attractive.png",
		#EMOTION_SAD		:	"interface_emperorapollo/common/emotions/sad.png",
		#EMOTION_SHY		:	"interface_emperorapollo/common/emotions/shy.png",
		#EMOTION_CHEERUP		:	"interface_emperorapollo/common/emotions/cheerup.png",
		#EMOTION_BANTER		:	"interface_emperorapollo/common/emotions/banter.png",
		#EMOTION_JOY		:	"interface_emperorapollo/common/emotions/joy.png",
		#EMOTION_DANCE_1		:	"interface_emperorapollo/common/emotions/dance1.png",
		#EMOTION_DANCE_2		:	"interface_emperorapollo/common/emotions/dance2.png",
		#EMOTION_DANCE_3		:	"interface_emperorapollo/common/emotions/dance3.png",
		#EMOTION_DANCE_4		:	"interface_emperorapollo/common/emotions/dance4.png",
		#EMOTION_DANCE_5		:	"interface_emperorapollo/common/emotions/dance5.png",
		#EMOTION_DANCE_6		:	"interface_emperorapollo/common/emotions/dance6.png",

		#EMOTION_KISS		:	"interface_emperorapollo/common/emotions/kiss.png",
		#EMOTION_FRENCH_KISS	:	"interface_emperorapollo/common/emotions/fkiss.png",
		#EMOTION_SLAP		:	"interface_emperorapollo/common/emotions/slap.png",
	}

	ANI_DICT = {
		chr.MOTION_CLAP :			"clap.msa",
		chr.MOTION_CHEERS_1 :			"cheers_1.msa",
		chr.MOTION_CHEERS_2 :			"cheers_2.msa",
		chr.MOTION_DANCE_1 :			"dance_1.msa",
		chr.MOTION_DANCE_2 :			"dance_2.msa",
		chr.MOTION_DANCE_3 :			"dance_3.msa",
		chr.MOTION_DANCE_4 :			"dance_4.msa",
		chr.MOTION_DANCE_5 :			"dance_5.msa",
		chr.MOTION_DANCE_6 :			"dance_6.msa",
		chr.MOTION_CONGRATULATION :		"congratulation.msa",
		chr.MOTION_FORGIVE :			"forgive.msa",
		chr.MOTION_ANGRY :			"angry.msa",
		chr.MOTION_ATTRACTIVE :			"attractive.msa",
		chr.MOTION_SAD :			"sad.msa",
		chr.MOTION_SHY :			"shy.msa",
		chr.MOTION_CHEERUP :			"cheerup.msa",
		chr.MOTION_BANTER :			"banter.msa",
		chr.MOTION_JOY :			"joy.msa",
		chr.MOTION_FRENCH_KISS_WITH_WARRIOR :	"french_kiss_with_warrior.msa",
		chr.MOTION_FRENCH_KISS_WITH_ASSASSIN :	"french_kiss_with_assassin.msa",
		chr.MOTION_FRENCH_KISS_WITH_SURA :	"french_kiss_with_sura.msa",
		chr.MOTION_FRENCH_KISS_WITH_SHAMAN :	"french_kiss_with_shaman.msa",
		chr.MOTION_KISS_WITH_WARRIOR :		"kiss_with_warrior.msa",
		chr.MOTION_KISS_WITH_ASSASSIN :		"kiss_with_assassin.msa",
		chr.MOTION_KISS_WITH_SURA :		"kiss_with_sura.msa",
		chr.MOTION_KISS_WITH_SHAMAN :		"kiss_with_shaman.msa",
		chr.MOTION_SLAP_HIT_WITH_WARRIOR :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_ASSASSIN :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SURA :		"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SHAMAN :	"slap_hit.msa",
		chr.MOTION_SLAP_HURT_WITH_WARRIOR :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_ASSASSIN :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SURA :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SHAMAN :	"slap_hurt.msa",
	}
	# if app.ENABLE_WOLFMAN_CHARACTER:
		# ANI_DICT.update({
			# chr.MOTION_FRENCH_KISS_WITH_WOLFMAN :	"french_kiss_with_wolfman.msa",
			# chr.MOTION_KISS_WITH_WOLFMAN :			"kiss_with_wolfman.msa",
			# chr.MOTION_SLAP_HIT_WITH_WOLFMAN :		"slap_hit.msa",
			# chr.MOTION_SLAP_HURT_WITH_WOLFMAN :		"slap_hurt.msa",
		# })

elif EMOTION_VERSION == 1:
	EMOTION_CLAP = 1
	EMOTION_CHEERS_1 = 2
	EMOTION_CHEERS_2 = 3
	EMOTION_DANCE_1 = 4
	EMOTION_DANCE_2 = 5
	EMOTION_KISS = 51
	EMOTION_FRENCH_KISS = 52
	EMOTION_SLAP = 53

	EMOTION_DICT = {
		EMOTION_CLAP :			{"name": localeInfo.EMOTION_CLAP, 		"command":"/clap"},
		EMOTION_CHEERS_1 :		{"name": localeInfo.EMOTION_CHEERS_1, 	"command":"/cheer1"},
		EMOTION_CHEERS_2 :		{"name": localeInfo.EMOTION_CHEERS_2, 	"command":"/cheer2"},
		EMOTION_DANCE_1 :		{"name": localeInfo.EMOTION_DANCE_1, 	"command":"/dance1"},
		EMOTION_DANCE_2 :		{"name": localeInfo.EMOTION_DANCE_2, 	"command":"/dance2"},
		EMOTION_KISS :			{"name": localeInfo.EMOTION_CLAP_KISS, 	"command":"/kiss"},
		EMOTION_FRENCH_KISS :		{"name": localeInfo.EMOTION_FRENCH_KISS, 	"command":"/french_kiss"},
		EMOTION_SLAP :			{"name": localeInfo.EMOTION_SLAP, 		"command":"/slap"},
	}

	ICON_DICT = {
		EMOTION_CLAP 		: 	"interface_emperorapollo/common/emotions/emotion_clap.sub",
		EMOTION_CHEERS_1	:	"interface_emperorapollo/common/emotions/happy.png",
		EMOTION_CHEERS_2	:	"interface_emperorapollo/common/emotions/cheerup.png",

		EMOTION_DANCE_1		:	"interface_emperorapollo/common/emotions/dance1.png",
		EMOTION_DANCE_2		:	"interface_emperorapollo/common/emotions/dance2.png",

		EMOTION_KISS		:	"interface_emperorapollo/common/emotions/kiss.png",
		EMOTION_FRENCH_KISS	:	"interface_emperorapollo/common/emotions/fkiss.png",
		EMOTION_SLAP		:	"interface_emperorapollo/common/emotions/slap.png",
	}

	ANI_DICT = {
		chr.MOTION_CLAP :			"clap.msa",
		chr.MOTION_CHEERS_1 :			"cheers_1.msa",
		chr.MOTION_CHEERS_2 :			"cheers_2.msa",
		chr.MOTION_DANCE_1 :			"dance_1.msa",
		chr.MOTION_DANCE_2 :			"dance_2.msa",
		chr.MOTION_FRENCH_KISS_WITH_WARRIOR :	"french_kiss_with_warrior.msa",
		chr.MOTION_FRENCH_KISS_WITH_ASSASSIN :	"french_kiss_with_assassin.msa",
		chr.MOTION_FRENCH_KISS_WITH_SURA :	"french_kiss_with_sura.msa",
		chr.MOTION_FRENCH_KISS_WITH_SHAMAN :	"french_kiss_with_shaman.msa",
		chr.MOTION_KISS_WITH_WARRIOR :		"kiss_with_warrior.msa",
		chr.MOTION_KISS_WITH_ASSASSIN :		"kiss_with_assassin.msa",
		chr.MOTION_KISS_WITH_SURA :		"kiss_with_sura.msa",
		chr.MOTION_KISS_WITH_SHAMAN :		"kiss_with_shaman.msa",
		chr.MOTION_SLAP_HIT_WITH_WARRIOR :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_ASSASSIN :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SURA :		"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SHAMAN :	"slap_hit.msa",
		chr.MOTION_SLAP_HURT_WITH_WARRIOR :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_ASSASSIN :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SURA :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SHAMAN :	"slap_hurt.msa",
	}
else:
	EMOTION_CLAP = 1
	EMOTION_CHEERS_1 = 2
	EMOTION_CHEERS_2 = 3
	EMOTION_KISS = 51
	EMOTION_FRENCH_KISS = 52
	EMOTION_SLAP = 53

	EMOTION_DICT = {
		EMOTION_CLAP :			{"name": localeInfo.EMOTION_CLAP, 		"command":"/clap"},
		EMOTION_CHEERS_1 :		{"name": localeInfo.EMOTION_CHEERS_1, 	"command":"/cheer1"},
		EMOTION_CHEERS_2 :		{"name": localeInfo.EMOTION_CHEERS_2, 	"command":"/cheer2"},
		EMOTION_KISS :			{"name": localeInfo.EMOTION_CLAP_KISS, 	"command":"/kiss"},
		EMOTION_FRENCH_KISS :		{"name": localeInfo.EMOTION_FRENCH_KISS, 	"command":"/french_kiss"},
		EMOTION_SLAP :			{"name": localeInfo.EMOTION_SLAP, 		"command":"/slap"},
	}

	ICON_DICT = {
		EMOTION_CLAP 		: 	"interface_emperorapollo/common/emotions/emotion_clap.sub",
		EMOTION_CHEERS_1	:	"interface_emperorapollo/common/emotions/happy.png",
		EMOTION_CHEERS_2	:	"interface_emperorapollo/common/emotions/cheerup.png",

		EMOTION_KISS		:	"interface_emperorapollo/common/emotions/kiss.png",
		EMOTION_FRENCH_KISS	:	"interface_emperorapollo/common/emotions/fkiss.png",
		EMOTION_SLAP		:	"interface_emperorapollo/common/emotions/slap.png",
	}

	ANI_DICT = {
		chr.MOTION_CLAP :			"clap.msa",
		chr.MOTION_CHEERS_1 :			"cheers_1.msa",
		chr.MOTION_CHEERS_2 :			"cheers_2.msa",
		chr.MOTION_FRENCH_KISS_WITH_WARRIOR :	"french_kiss_with_warrior.msa",
		chr.MOTION_FRENCH_KISS_WITH_ASSASSIN :	"french_kiss_with_assassin.msa",
		chr.MOTION_FRENCH_KISS_WITH_SURA :	"french_kiss_with_sura.msa",
		chr.MOTION_FRENCH_KISS_WITH_SHAMAN :	"french_kiss_with_shaman.msa",
		chr.MOTION_KISS_WITH_WARRIOR :		"kiss_with_warrior.msa",
		chr.MOTION_KISS_WITH_ASSASSIN :		"kiss_with_assassin.msa",
		chr.MOTION_KISS_WITH_SURA :		"kiss_with_sura.msa",
		chr.MOTION_KISS_WITH_SHAMAN :		"kiss_with_shaman.msa",
		chr.MOTION_SLAP_HIT_WITH_WARRIOR :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_ASSASSIN :	"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SURA :		"slap_hit.msa",
		chr.MOTION_SLAP_HIT_WITH_SHAMAN :	"slap_hit.msa",
		chr.MOTION_SLAP_HURT_WITH_WARRIOR :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_ASSASSIN :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SURA :	"slap_hurt.msa",
		chr.MOTION_SLAP_HURT_WITH_SHAMAN :	"slap_hurt.msa",
	}


def __RegisterSharedEmotionAnis(mode, path):
	chrmgr.SetPathName(path)
	chrmgr.RegisterMotionMode(mode)

	for key, val in ANI_DICT.items():
		chrmgr.RegisterMotionData(mode, key, val)

def RegisterEmotionAnis(path):
	actionPath = path + "action/"
	weddingPath = path + "wedding/"

	__RegisterSharedEmotionAnis(chr.MOTION_MODE_GENERAL, actionPath)
	__RegisterSharedEmotionAnis(chr.MOTION_MODE_WEDDING_DRESS, actionPath)

	chrmgr.SetPathName(weddingPath)
	chrmgr.RegisterMotionMode(chr.MOTION_MODE_WEDDING_DRESS)
	chrmgr.RegisterMotionData(chr.MOTION_MODE_WEDDING_DRESS, chr.MOTION_WAIT, "wait.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_WEDDING_DRESS, chr.MOTION_WALK, "walk.msa")
	chrmgr.RegisterMotionData(chr.MOTION_MODE_WEDDING_DRESS, chr.MOTION_RUN, "walk.msa")

def RegisterEmotionIcons():
	for key, val in ICON_DICT.items():
		player.RegisterEmotionIcon(key, val)

