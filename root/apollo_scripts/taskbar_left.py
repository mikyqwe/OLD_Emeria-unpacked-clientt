import uiScriptLocale
import app
import apollo_interface
ROOT = "d:/ymir work/ui/game/"
BASE =  apollo_interface.PATCH_SPECIAL + "/taskbar/"

Y_ADD_POSITION = 0

window = {
	"name" : "TaskBar",

	"x" : 0,
	"y" : SCREEN_HEIGHT - 124,

	"width" : 165,
	"height" : 158,

	"children" :
	(


		{
			"name" : "Window1",
			"type" : "window",

			"x" : 48,
			"y" : -33,

			"width" : 110,
			"height" : 108,


		},
		{
			"name" : "BG",
			"type" : "image",

			"x" : 0,
			"y" : 0,

			"image" : BASE+"new_left_side.png"

		},

		{
			"name" : "MiniMapWindow2",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : 110,
			"height" : 108,


		},

		{
			"name" : "EXPGauge_01",
			"type" : "expanded_image_vertical",

			"x" : 151,
			"y" : 92,

			"image" : BASE+"progress_exp_full.png",

		},

		{
			"name" : "CharacterButton",
			"type" : "button",

			"x" : 10,
			"y" : 35,

			"tooltip_text" : uiScriptLocale.TASKBAR_CHARACTER,

			"default_image" : BASE + "btn_characterinfo_01_normal.png",
			"over_image" : BASE + "btn_characterinfo_02_hover.png",
			"down_image" : BASE + "btn_characterinfo_03_active.png",
		},

		{
			"name" : "ItemShopButton",
			"type" : "button",

			"x" : 12,
			"y" : 65,

			"tooltip_text" : "ItemShop",

			"default_image" : BASE + "btn_inventory_01_normal.png",
			"over_image" : BASE + "btn_inventory_02_hover.png",
			"down_image" : BASE + "btn_inventory_03_active.png",
		},
	),
}
