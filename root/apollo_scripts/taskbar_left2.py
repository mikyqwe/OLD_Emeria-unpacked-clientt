import uiScriptLocale
import app
import apollo_interface
ROOT = "d:/ymir work/ui/game/"
BASE =  apollo_interface.PATCH_SPECIAL + "/taskbar"

Y_ADD_POSITION = 0

window = {
	"name" : "TaskBar",

	"x" : SCREEN_WIDTH - 240,
	"y" : SCREEN_HEIGHT - 55,

	"width" : 255,
	"height" : 158,


	"children" :
	(


		{
			"name" : "BG",
			"type" : "image",

			"x" : 55,
			"y" : 0,

			"width" : 128,
			"height" : 128,

			"image" : BASE+"/new_right.png",

		},
		{
			"name" : "SystemButton",
			"type" : "button",

			"x" : 199,#207,
			"y" : 13,#23,

			"tooltip_text" : uiScriptLocale.TASKBAR_SYSTEM,
			
			"default_image" : "d:/ymir work/interface/button/option_normal.tga",
			"over_image" : "d:/ymir work/interface/button/option_hover.tga",
			"down_image" : "d:/ymir work/interface/button/option_active.tga",

			#"default_image" : BASE + "/btn_options_01_normal.png",
			#"over_image" : BASE + "/btn_options_02_hover.png",
			#"down_image" : BASE + "/btn_options_03_active.png",
		},

		{
			"name" : "InventoryButton",
			"type" : "button",

			"x" : 112,#120,
			"y" : 13,#22,

			"tooltip_text" : uiScriptLocale.TASKBAR_INVENTORY,
			
			"default_image" : "d:/ymir work/interface/button/inventory_normal.tga",
			"over_image" : "d:/ymir work/interface/button/inventory_hover.tga",
			"down_image" : "d:/ymir work/interface/button/inventory_active.tga",

			#"default_image" : BASE + "/btn_inventory_01_normal.png",
			#"over_image" : BASE + "/btn_inventory_02_hover.png",
			#"down_image" : BASE + "/btn_inventory_03_active.png",
		},
		{
			"name" : "MessengerButton",
			"type" : "button",


			"x" : 155,#163,
			"y" : 13,#23,

			"tooltip_text" : uiScriptLocale.TASKBAR_MESSENGER,
			
			"default_image" : "d:/ymir work/interface/button/messenger_normal.tga",
			"over_image" : "d:/ymir work/interface/button/messenger_hover.tga",
			"down_image" : "d:/ymir work/interface/button/messenger_active.tga",

			#"default_image" : BASE + "/btn_friends_01_normal.png",
			#"over_image" : BASE + "/btn_friends_02_hover.png",
			#"down_image" : BASE + "/btn_friends_03_active.png",
		},

	),
}
