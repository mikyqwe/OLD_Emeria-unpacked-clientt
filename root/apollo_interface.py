import app
import ui
import os
import playerSettingModule
import uiScriptLocale
import uiapollo


APOLLO_PATCH = "apollo_scripts"

#Colors
COLOR_NORMAL = 0xffa08784
COLOR_HOVER = 0xfff8d090
COLOR_LOGIN_TEXT = 0xffcbab9d
COLOR_TEXT1= 0xffA08784
COLOR_TEXT2 = 0xffA07970

COLOR_RED = 0xffa33437
COLOR_BLUE = 0xff3453a3

global REGBUTTON
global FORGOTPASS

#Login Redirect Links
REGBUTTON = "http://elendos.shop"
FORO = "http://elendos.shop"

#PATCHES
PATCH_COMMON = "interface_EmperorApollo/common"
PATCH_SPECIAL = "interface_EmperorApollo/special"
PATCH_SPECIAL_1 = "interface_EmperorApollo/icons/special"
PATCH_GUILD = "interface_EmperorApollo/special/guild"
PATCH_LOGIN = "interface_EmperorApollo/login"
PATCH_ICON = "interface_EmperorApollo/icons"
PATCH_BUTTONS = "interface_EmperorApollo/common/button"
PATCH_BRADIO = "interface_EmperorApollo/common/radio"
PATCH_HORIZONTAL_BAR = PATCH_COMMON + "/horizontal_bar/"
PATCH_UISCRIPT = "uiscript/"
PATCH_CHECK = "interface_EmperorApollo/common/radio/"
PATCH_DROPDW = "interface_EmperorApollo/common/dropdown/"
APOLLO_SCRIPTS = "apollo_scripts/"
APOLLO_PATCH = "interface_EmperorApollo/"
PATCH_TASKBAR = "interface_EmperorApollo/special/taskbar/"
APOLLO_EMPIRE = "interface_EmperorApollo/char_empire/"
APOLLO_FACE = "interface_emperorapollo/icons/faces/"
PATCH_DUEL = "interface_EmperorApollo/duel/"
PATCH_EMOTIONS = "interface_EmperorApollo/special/character/emotions/"


#LOGIN Interface

ID_LOGIN = "Benutzername / ID"
PW_LOGIN = "Passwort / PW"
LOGIN_NOACCOUNT = "Noch kein Account?"
SAVE_EMPTY = "Leerer Slot"
#SAVE
SAVE_SUCCES = "Logininformationen erfolgreich gespeichert."
SAVE_FAIL = "Logininformationen NICHT gespeichert."
#DELETE
DELETE_FAIL = "Logininformationen NICHT gelaescht."
#autoLogin
AUTOLOGIN_FAIL = "Auf dieser Taste ist nichts gespeichert!"
#GOLD Info
SAVE_BUTTON = "Speichert nebenstehende Logininformationen auf dem Tastenslot."
DELETE_BUTTON = "Laescht die Logininformationen auf dem Tastenslot."
PRESS_KEY = "Draecke die Taste auf deiner Tastatur um dich anzumelden!."

#LOGIN CONNECTION
IP = "164.132.213.112"
CH1 = 13001
CH2 = 14070
CH3 = 15070
CH4 = 16070
AUTH = 11002
SERVER_NAME = "Athena2"
#END LOGIN CONNECTION


CHANNEL_1 = "Channel I"
CHANNEL_2 = "Channel II"
CHANNEL_3 = "|cffc94431 Channel III"
CHANNEL_4 = "|cffc94431 Channel IV"

REGISTER = "                  Registriere dich hier!"
PWFORGOT = "Du kannst deine Logindaten speichern."

ID_HOLD = "8-16 Zeichen (a-Z,0-9)"
PW_HOLD = "8-16 Zeichen (a-Z,0-9)"

SELECT_NO_GUILD = "No guild"

#CREATECARACTER
NAME = "Name:"
GENDER = "Waehle dein Geschlecht:"
RACE = "Waehle deine Rasse:"
SHAPE = "Waehle dein Grundgewand:"
#RACE
RACE_WAR = "Krieger"
RACE_NINJA = "Ninja"
RACE_SURA = "Sura"
RACE_SHAMAN = "Schamane"
RACE_WOLF = "Lykaner"
#GENDER
GENDER_MAN = "Maennlich"
GENDER_WOMAN = "Weiblich"
#SHAPE
SHAPE_1 = "1. Gewand"
SHAPE_2 = "2. Gewand"
#
CANCEL = "Cancel"
CREATE = "Create"

#SelectCharacter
VIT = "Vitality"
INT = "Intelligence"
STR = "Strength"
DEX = "Flexibility"


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ uiCHaracter #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Main Page buttons
PAGE_TEXT_1 = "Status"
PAGE_TEXT_2 = "Characteristics"
PAGE_TEXT_3 = "Bonuses"
PAGE_TEXT_4 = "Skills"
PAGE_TEXT_5 = "Emotions"
PAGE_TEXT_6 = "Statistics"
PAGE_TEXT_7 = "Quests"
PAGE_TEXT_8 = "Daily"
#Page 1
NAME_HP = "(HP) Life:"
NAME_SP = "(SP) Mana:"
NAME_VIT = "(VIT) Vitality:"
NAME_INT = "(INT) Intelligence:"
NAME_STR = "(SIR) Strength:"
NAME_DEX = "(DEX) Fate:"

#

CHARACTER_PSTATUS = "Guilds power:"
CHARACTER_FROM	= "From"

POINTS_DESK = "Available points:"
#Page 2
PG2_BONUS_1 = "Speed Movement"
PG2_BONUS_2 = "Attack Speed"
PG2_BONUS_3 = "Magic Speed"
PG2_BONUS_4 = "Magic Power"
PG2_BONUS_5 = "Magic defense"
PG2_BONUS_6 = "Dodge"
PG2_BONUS_7 = "Attack"
PG2_BONUS_8 = "Defense"

#Page 3
ON = "An"
OFF = "Aus"

OFENSIVE_BONUSES = "Ofensive Bonuses"
DEFENSIVE_BONUSES = "Defensive Bonuses"
OTHER_BONUSES = "Other Bonuses"
#-----------
Offensive_bonuse = [uiapollo.TOOLTIP_APPLY_ATTBONUS_HUMAN, uiapollo.TOOLTIP_APPLY_CRITICAL_PCT, uiapollo.TOOLTIP_APPLY_PENETRATE_PCT, uiapollo.TOOLTIP_NORMAL_HIT_DAMAGE_BONUS, uiapollo.TOOLTIP_SKILL_DAMAGE_BONUS, uiapollo.TOOLTIP_APPLY_ATTBONUS_MONSTER, uiapollo.TOOLTIP_APPLY_ATTBONUS_DEVIL, uiapollo.TOOLTIP_APPLY_ATTBONUS_UNDEAD, uiapollo.TOOLTIP_APPLY_ATTBONUS_ANIMAL, uiapollo.TOOLTIP_APPLY_ATTBONUS_ORC, uiapollo.TOOLTIP_APPLY_ATTBONUS_MILGYO, uiapollo.TOOLTIP_APPLY_POISON_REDUCE,]
Offensive_bonuse_Val = [43,40,41,122,121,53,48,47,44,45,46,37,]
#-----------
Defensive_bonuse = [uiapollo.TOOLTIP_APPLY_RESIST_SWORD, uiapollo.TOOLTIP_APPLY_RESIST_TWOHAND, uiapollo.TOOLTIP_APPLY_RESIST_DAGGER, uiapollo.TOOLTIP_APPLY_RESIST_BELL, uiapollo.TOOLTIP_APPLY_RESIST_FAN, uiapollo.TOOLTIP_RESIST_BOW, uiapollo.TOOLTIP_APPLY_DODGE, uiapollo.TOOLTIP_RESIST_MAGIC, uiapollo.TOOLTIP_APPLY_BLOCK, uiapollo.TOOLTIP_APPLY_IMMUNE_STUN,uiapollo.TOOLTIP_APPLY_DODGE, uiapollo.TOOLTIP_HP_REGEN, uiapollo.TOOLTIP_SP_REGEN, uiapollo.TOOLTIP_APPLY_STEAL_HP, uiapollo.TOOLTIP_APPLY_STEAL_SP, uiapollo.TOOLTIP_APPLY_EXP_DOUBLE_BONUS, uiapollo.TOOLTIP_APPLY_GOLD_DOUBLE_BONUS, uiapollo.TOOLTIP_APPLY_ITEM_DROP_BONUS,]
Defensive_bonuse_Val = [69,70,71,72,73,74,68,77,67,88,67,32,33,63,64,83,84,85,]
#-----------
Other_bonuses = [uiapollo.TOOLTIP_APPLY_ATTBONUS_WARRIOR, uiapollo.TOOLTIP_APPLY_ATTBONUS_ASSASSIN, uiapollo.TOOLTIP_APPLY_ATTBONUS_SURA, uiapollo.TOOLTIP_APPLY_ATTBONUS_SHAMAN ,uiapollo.TOOLTIP_APPLY_RESIST_WARRIOR, uiapollo.TOOLTIP_APPLY_RESIST_ASSASSIN, uiapollo.TOOLTIP_APPLY_RESIST_SURA, uiapollo.TOOLTIP_APPLY_RESIST_SHAMAN, uiapollo.TOOLTIP_CON, uiapollo.TOOLTIP_INT, uiapollo.TOOLTIP_STR, uiapollo.TOOLTIP_DEX, ]
Other_bonuses_Val = [54,55,55,57,59,60,61,62,13,15,12,14,]
#-----------



SHOW_NIGHT_TXT = "Nacht:"
SHOW_SNOW_TXT = "Schneefall:"


#Page 4

SKILL_BUTTON_1 = "Page 1"
SKILL_BUTTON_2 = "Page 2"
SUPPORT_TITLE = "Standard Skills"

#Page 5

EMOTICON_PAGE_TITLE_NORMAL = "Normal actions"
EMOTICON_PAGE_TITLE_INTERAK = "Interactive actions"

#Page 6

STATISTICS_TITLE_1 = "Getotete Monster"
STATISTICS_TITLE_2 = "Getotete Metin"
STATISTICS_TITLE_3 = "Getotete Duelle"
STATISTICS_TITLE_4 = "Getotete Player"
STATISTICS_TITLE_5 = "Besiegte Spieler"
STATISTICS_TITLE_6 = "Besiegte Spieler |cffe5ad4d[Gelb]|cffa08784"
STATISTICS_TITLE_7 = "Besiegte Spieler |cffc94431[Rot]|cffa08784"
STATISTICS_TITLE_8 = "Besiegte Spieler |cff467ddd[Blau]|cffa08784"

#Quest
TEXT_QUEST_1 = "Zu erledigen bis 24 Uhr"
TEXT_QUEST_2 = "Zu erledigen bis 24 Uhr"
TEXT_QUEST_3 = "Zu erledigen bis 24 Uhr"

#----------------------------------- GUILD
#Main Page buttons
PAGE_TEXT_GUILD_1 = "Guild info"
PAGE_TEXT_GUILD_2 = "News"
PAGE_TEXT_GUILD_3 = "Members"
PAGE_TEXT_GUILD_4 = "Guild Skills"
PAGE_TEXT_GUILD_5 = "Ranking management"
PAGE_TEXT_GUILD_6 = "Statistics"
PAGE_TEXT_GUILD_7 = "Orders"

#MEMBER

NAME_TEXT = "Name"
RACE_TEXT = "Breed"
LEVEL_TEXT = "Level"
INVEST_TEXT = "Invest."
RANG_TEXT = "Position/Rank"


#Member Auth

NR_GRADE = "Nr."
NAME_GRADE = "Position/Rank"
INVITE_TEXT = "Invite"
DISMISS_TEXT = "Dismissed"
WRITE_TEXT = "Writing"
SKILL_TEXT = "Skills"


#----------------------------------  OPTIONS
OPTION_TITLE = "Optionen"
#Main Page buttons
PAGE_TEXT_OPTIONS_1 = "Player"
PAGE_TEXT_OPTIONS_2 = "Display"
PAGE_TEXT_OPTIONS_3 = "Graphics & Textures"
PAGE_TEXT_OPTIONS_4 = "Sound"
PAGE_TEXT_OPTIONS_5 = "Interface Settings"

DAY = "d:/ymir work/environment/dawnmistwood.msenv"
NIGHT = "d:/ymir work/environment/mtthunder.msenv"

#Texts
PVP_MODE = "PVP Modus:"
BLOCK = "Block:"

#Page 3
ON = "On"
OFF = "Off"

SHOW_NIGHT_TXT = "Night:"
SHOW_SNOW_TXT = "Snowfall:"
#Page 4
MUSIC = "Effect sounds:"
SOUND = "Music loudness:"
MUSIC_TITLE_TEXT = "Current title:"
CHANGE_MUSIC_BUTTON_TEXT = "Change"

#GUILD
GUILD_TITLE = "Guild"
PAGE_TEXT_GUILD_1 = "Guild info"
PAGE_TEXT_GUILD_2 = "News"
PAGE_TEXT_GUILD_3 = "Members"
PAGE_TEXT_GUILD_4 = "Guild Skills"
PAGE_TEXT_GUILD_5 = "Ranking management"

#First
IMPORTANT = "Important Messege!"
TEXT_TYPE_MESSEGE = "Write Message..."

FACE_IMAGE_DICT_SMALL = {
	playerSettingModule.RACE_WARRIOR_M	: APOLLO_FACE + "small/icon_mwarrior.png",
	playerSettingModule.RACE_WARRIOR_W	: APOLLO_FACE + "small/icon_wwarrior.png",
	playerSettingModule.RACE_ASSASSIN_M	: APOLLO_FACE + "small/icon_mninja.png",
	playerSettingModule.RACE_ASSASSIN_W	: APOLLO_FACE + "small/icon_wninja.png",
	playerSettingModule.RACE_SURA_M		: APOLLO_FACE + "small/icon_msura.png",
	playerSettingModule.RACE_SURA_W		: APOLLO_FACE + "small/icon_wsura.png",
	playerSettingModule.RACE_SHAMAN_M	: APOLLO_FACE + "small/icon_mshaman.png",
	playerSettingModule.RACE_SHAMAN_W	: APOLLO_FACE + "small/icon_wshaman.png",
	
}

FACE_IMAGE_DICT_MEDIUM = {
	playerSettingModule.RACE_WARRIOR_M	: APOLLO_FACE + "medium/icon_mwarrior.png",
	playerSettingModule.RACE_WARRIOR_W	: APOLLO_FACE + "medium/icon_wwarrior.png",
	playerSettingModule.RACE_ASSASSIN_M	: APOLLO_FACE + "medium/icon_mninja.png",
	playerSettingModule.RACE_ASSASSIN_W	: APOLLO_FACE + "medium/icon_wninja.png",
	playerSettingModule.RACE_SURA_M		: APOLLO_FACE + "medium/icon_msura.png",
	playerSettingModule.RACE_SURA_W		: APOLLO_FACE + "medium/icon_wsura.png",
	playerSettingModule.RACE_SHAMAN_M	: APOLLO_FACE + "medium/icon_mshaman.png",
	playerSettingModule.RACE_SHAMAN_W	: APOLLO_FACE + "medium/icon_wshaman.png",
}

#Big
FACE_IMAGE_DICT = {
	playerSettingModule.RACE_WARRIOR_M	: APOLLO_FACE + "icon_mwarrior.png",
	playerSettingModule.RACE_WARRIOR_W	: APOLLO_FACE + "icon_wwarrior.png",
	playerSettingModule.RACE_ASSASSIN_M	: APOLLO_FACE + "icon_mninja.png",
	playerSettingModule.RACE_ASSASSIN_W	: APOLLO_FACE + "icon_wninja.png",
	playerSettingModule.RACE_SURA_M		: APOLLO_FACE + "icon_msura.png",
	playerSettingModule.RACE_SURA_W		: APOLLO_FACE + "icon_wsura.png",
	playerSettingModule.RACE_SHAMAN_M	: APOLLO_FACE + "icon_mshaman.png",
	playerSettingModule.RACE_SHAMAN_W	: APOLLO_FACE + "icon_wshaman.png",

}

EQUIPEMENT_GENDER = {
	playerSettingModule.RACE_WARRIOR_M	: "%s/inventory/inventory_m_13slots.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_WARRIOR_W	: "%s/inventory/inventory_w_13slots.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_ASSASSIN_M	: "%s/inventory/inventory_m_13slots.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_ASSASSIN_W	: "%s/inventory/inventory_w_13slots.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_SURA_M		: "%s/inventory/inventory_m_13slots.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_SURA_W	: "%s/inventory/inventory_w_13slots.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_SHAMAN_M	: "%s/inventory/inventory_m_13slots.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_SHAMAN_W	: "%s/inventory/inventory_w_13slots.png" % PATCH_SPECIAL,
	
}

COSTUME_GENDER = {
	playerSettingModule.RACE_WARRIOR_M	: "%s/inventory/costume_m.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_WARRIOR_W	: "%s/inventory/costume_w.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_ASSASSIN_M	: "%s/inventory/costume_m.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_ASSASSIN_W	: "%s/inventory/costume_w.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_SURA_M		: "%s/inventory/costume_m.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_SURA_W	: "%s/inventory/costume_w.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_SHAMAN_M	: "%s/inventory/costume_m.png" % PATCH_SPECIAL,
	playerSettingModule.RACE_SHAMAN_W	: "%s/inventory/costume_w.png" % PATCH_SPECIAL,
	
}
