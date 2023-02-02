import uiScriptLocale
import apollo_interface
ROOT = "d:/ymir work/ui/public/"

DEFAULT_VALOR = 55
X_S = 50

window = {
	"name" : "SystemDialog",
	"style" : ("movable","float"),

	"x" : SCREEN_WIDTH/2 - 142,
	"y" : SCREEN_HEIGHT/2 - 174,

	"width" : 260,
	"height" : DEFAULT_VALOR+(139*50),

	"children" :
	(
		{
			"name" : "board",
			"type" : "thinmenu",
			"style" : ("movable","float",),

			"x" : 0,
			"y" : 0,

			"width" : DEFAULT_VALOR,

			"children" :
			(
				{
					"name" : "mall_button",
					"type" : "button",
					"x" : 10+32,
					"y" : X_S,
					"text" : uiScriptLocale.SYSTEM_MALL,
					"text_color" : 0xffF8BF24,
					"default_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_hovar.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_active.png",
				},

				{
					"name" : "patchnotes_button", "type" : "button", "x" : 10, "y" : Y_START + Y_STEP*1,
					"default_image" : ROOT + "XLarge_Button_01.sub", "over_image" : ROOT + "XLarge_Button_02.sub", "down_image" : ROOT + "XLarge_Button_03.sub",
					"text" : "Patchnotes", 
				},

				{
					"name" : "system_option_button",
					"type" : "button",

					"x" : 10+32,
					"y" : X_S+10*4,

					"text" : uiScriptLocale.SYSTEMOPTION_TITLE,
					"text_color" : 0xffF8BF24,
					"default_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_hovar.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_active.png",
				},
				{
					"name" : "change_button",
					"type" : "button",
					"x" : 10+32,
					"y" : X_S+10*7,
					"text" : uiScriptLocale.SYSTEM_CHANGE,
					# "text_color" : 0xffF8BF24,
					"default_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_hovar.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_active.png",
				},
				{
					"name" : "logout_button",
					"type" : "button",
					"x" : 10+32,
					"y" : X_S+10*10,
					"text" : uiScriptLocale.SYSTEM_LOGOUT,
					"default_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_hovar.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_active.png",
				},
				{
					"name" : "exit_button",
					"type" : "button",
					"x" : 10+32,
					"y" : X_S+10*13,
					"text" : uiScriptLocale.SYSTEM_EXIT,
					"default_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_hovar.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_active.png",
				},
				{
					"name" : "help_button",
					"type" : "button",
					"x" : 10+32,
					"y" : X_S+10*17,
					"text" : uiScriptLocale.SYSTEM_HELP,
					"default_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_hovar.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_active.png",
				},
				{
					"name" : "cancel_button",
					"type" : "button",
					"x" : 10+32,
					"y" : X_S+10*20,
					"text" : uiScriptLocale.CANCEL,
					"default_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_hovar.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/menu/button_menu_active.png",
				},
				{
					"name" : "achievement_button",
					"type" : "button",

					"x" : 10+32,
					"y" : X_S+10*50,

					# "text" : "Achievementsystem",

					# "default_image" : ROOT + "XLarge_Button_01.sub",
					# "over_image" : ROOT + "XLarge_Button_02.sub",
					# "down_image" : ROOT + "XLarge_Button_03.sub",
				},
			),
		},
	),
}
