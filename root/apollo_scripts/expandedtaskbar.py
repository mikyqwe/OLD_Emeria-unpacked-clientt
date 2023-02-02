import uiScriptLocale
import apollo_interface
ROOT = "d:/ymir work/ui/game/"

Y_ADD_POSITION = 0
window = {
	"name" : "ExpandTaskBar",

	"x" : SCREEN_WIDTH/2 - 208,
	"y" : SCREEN_HEIGHT - 84,

	"width" : 421,
	"height" : 43,

	"children" :
	(
		{
			"name" : "ExpanedTaskBar_Board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 421,
			"height" : 43,

			"children" :
			(
				##DragonSoulButton
				{
					"name" : "DragonSoulButton",
					"type" : "button",

					"x" : 11,
					"y" : 9,

					"tooltip_text" : uiScriptLocale.DRAGONSOUL_TITLE,

					"default_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_dcraft_01_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_dcraft_02_hover.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_dcraft_03_active.png",
				},
			),
		},		
	),
}
