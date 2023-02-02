import uiScriptLocale
import app
import apollo_interface

window = {
	"name" : "SpecialStorageWindow",

	"x" : SCREEN_WIDTH - 400,
	"y" : 200,

	"style" : ("movable", "float",),

	"width" : 184,
	"height" : 328+32+30,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 184,
			"height" : 350+32+30,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : 169,
					"color" : "gray",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":84, "y":4, "text":uiScriptLocale.UPGRADE_STORAGE_TITLE, "text_horizontal_align":"center" },
					),
				},

				## Item Slot
				{
					"name" : "ItemSlot",
					"type" : "grid_table",

					"x" : 12,
					"y" : 34,

					"start_index" : 0,
					"x_count" : 5,
					"y_count" : 9,
					"x_step" : 32,
					"y_step" : 32,

					"image" : apollo_interface.PATCH_COMMON + "/slot_rectangle/slot.png",
				},
				
				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",

					"x" : 14,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/special_lager/special_lager_button_normal.tga",
					"over_image" : "d:/ymir work/ui/special_lager/special_lager_button_hover.tga",
					"down_image" : "d:/ymir work/ui/special_lager/special_lager_button_down.tga",

					"children" :
					(
						{
							"name" : "Inventory_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "I",
						},
					),
				},
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",

					"x" : 14 + (78/2),
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/special_lager/special_lager_button_normal.tga",
					"over_image" : "d:/ymir work/ui/special_lager/special_lager_button_hover.tga",
					"down_image" : "d:/ymir work/ui/special_lager/special_lager_button_down.tga",

					"children" :
					(
						{
							"name" : "Inventory_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "II",
						},
					),
				},
				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",

					"x" : 14 + (78/2)*2,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/special_lager/special_lager_button_normal.tga",
					"over_image" : "d:/ymir work/ui/special_lager/special_lager_button_hover.tga",
					"down_image" : "d:/ymir work/ui/special_lager/special_lager_button_down.tga",

					"children" :
					(
						{
							"name" : "Inventory_Tab_03_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "III",
						},
					),
				},
				{
					"name" : "Inventory_Tab_04",
					"type" : "radio_button",

					"x" : 14 + (78/2)*3,
					"y" : 295+32,

					"default_image" : "d:/ymir work/ui/special_lager/special_lager_button_normal.tga",
					"over_image" : "d:/ymir work/ui/special_lager/special_lager_button_hover.tga",
					"down_image" : "d:/ymir work/ui/special_lager/special_lager_button_down.tga",

					"children" :
					(
						{
							"name" : "Inventory_Tab_04_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",

							"text" : "IV",
						},
					),
				},
				
				{
					"name" : "Category_Tab_01",
					"type" : "radio_button",

					"x" : 14,
					"y" : 295+32+30,

					"default_image" : "d:/ymir work/ui/special_lager/upgrade_normal.tga",
					"over_image" : "d:/ymir work/ui/special_lager/upgrade_hover.tga",
					"down_image" : "d:/ymir work/ui/special_lager/upgrade_down.tga",

					"children" :
					(
						{
							"name" : "Category_Tab_01_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",
						},
					),
				},
					
				{
					"name" : "Category_Tab_02",
					"type" : "radio_button",

					"x" : 14+52,
					"y" : 295+32+30,

					"default_image" : "d:/ymir work/ui/special_lager/books_normal.tga",
					"over_image" : "d:/ymir work/ui/special_lager/books_hover.tga",
					"down_image" : "d:/ymir work/ui/special_lager/books_down.tga",

					"children" :
					(
						{
							"name" : "Category_Tab_02_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",
						},
					),
				},
				
				{
					"name" : "Category_Tab_03",
					"type" : "radio_button",

					"x" : 14+52+52,
					"y" : 295+32+30,

					"default_image" : "d:/ymir work/ui/special_lager/stones_normal.tga",
					"over_image" : "d:/ymir work/ui/special_lager/stones_hover.tga",
					"down_image" : "d:/ymir work/ui/special_lager/stones_down.tga",

					"children" :
					(
						{
							"name" : "Category_Tab_03_Print",
							"type" : "text",

							"x" : 0,
							"y" : 0,

							"all_align" : "center",
						},
					),
				},
			),
		},
	),
}