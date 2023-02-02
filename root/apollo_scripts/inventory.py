import uiScriptLocale
import item
import apollo_interface

import player
EQUIPMENT_START_INDEX = player.EQUIPMENT_SLOT_START
# -------------------------SLOT ACCE --------------------------------------******
SLOT_ACCE_ILLUMINA = item.COSTUME_SLOT_START
# -------------------------SLOT ACCE --------------------------------------******

INVENTORY_TAB_PATH = "d:/ymir work/ui/special_inventory/"

window = {
	"name" : "InventoryWindow",

	## Open Inventar Positio
	"x" : SCREEN_WIDTH - 200,
	"y" : SCREEN_HEIGHT - 37 - 649,
 
	"style" : ("movable", "float",),
 
	"width" : 200,
	"height" : 641,
 
	"children" :
	(
		## Inventory, Equipment Slots
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),
 
			"x" : 0,
			"y" : 0,

			"width" : 190,
			"height" : 641,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),
				
					"x" : 8 + 30,
					"y" : 7,
				
					"width" : 174 - 30,
					"color" : "yellow",
				
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":85 - 30, "y":5, "text":uiScriptLocale.INVENTORY_TITLE, "text_horizontal_align":"center" },
					),
				},
				# sort
				{
					"name" : "YenileButtonn",
					"type" : "image",
					"style" : ("attach",),

					"x" : 8,
					"y" : 7,

					"image" : "d:/ymir work/ui/pattern/titlebar_inv_refresh_baseframe.tga",

					"children" :
					(
						{
							"name" : "YenileButton",
							"type" : "button",

							"x" : 11,
							"y" : 3,

							"default_image" : "d:/ymir work/ui/refresh_small_button_01.sub",
							"over_image" : "d:/ymir work/ui/refresh_small_button_02.sub",
							"down_image" : "d:/ymir work/ui/refresh_small_button_03.sub",
							"disable_image" : "d:/ymir work/ui/refresh_small_button_04.sub",
						},
					),
				},
				## Equipment Slot
				{
					"name" : "Gender_Equipment",
					"type" : "image",

					"x" : 10,
					"y" : 33,

					"image" : "%s/inventory/costume_m.png" % apollo_interface.PATCH_SPECIAL,

					"children" :
					(

						{
							"name" : "EquipmentSlot",
							"type" : "slot",

							"x" : 3,
							"y" : 3,

							"width" : 150,
							"height" : 182,

							"slot" : (
										{"index":EQUIPMENT_START_INDEX+0, "x":43, "y":41, "width":32, "height":64},#dreapta-jos
										{"index":EQUIPMENT_START_INDEX+1, "x":43, "y":6, "width":32, "height":32},#
										{"index":EQUIPMENT_START_INDEX+2, "x":43, "y":151, "width":32, "height":32},#
										{"index":EQUIPMENT_START_INDEX+3, "x":80, "y":75, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+4, "x":3, "y":3, "width":32, "height":96},
										{"index":EQUIPMENT_START_INDEX+5, "x":116, "y":75, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+6, "x":116, "y":43, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+7, "x":116, "y":151, "width":32, "height":32},

										{"index":EQUIPMENT_START_INDEX+8, "x":116, "y":112, "width":32, "height":32},

										{"index":EQUIPMENT_START_INDEX+9, "x":114, "y":2, "width":32, "height":32},
										{"index":EQUIPMENT_START_INDEX+10, "x":78, "y":43, "width":32, "height":32},
										{"index":item.EQUIPMENT_RING1, "x":5, "y":150, "width":32, "height":32},
										{"index":item.EQUIPMENT_RING2, "x":80, "y":150, "width":32, "height":32},
										{"index":item.EQUIPMENT_BELT, "x":80, "y":106, "width":32, "height":32},
										{"index":item.EQUIPMENT_PET, "x":5, "y":106, "width":32, "height":32},
									),
						},
						## 
						{
							"name" : "Equipment_Tab_01",
							"type" : "radio_button",

							"x" : 86,
							"y" : 161,

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

							"children" :
							(
								{
									"name" : "Equipment_Tab_01_Print",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",

									"text" : "I",
								},
							),
						},
						## 
						{
							"name" : "Equipment_Tab_02",
							"type" : "radio_button",

							"x" : 86 + 32,
							"y" : 161,

							"default_image" : "d:/ymir work/ui/game/windows/tab_button_small_01.sub",
							"over_image" : "d:/ymir work/ui/game/windows/tab_button_small_02.sub",
							"down_image" : "d:/ymir work/ui/game/windows/tab_button_small_03.sub",

							"children" :
							(
								{
									"name" : "Equipment_Tab_02_Print",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"all_align" : "center",

									"text" : "II",
								},
							),
						},
					),
				},
				
				## CostumeButton
				{
					"name" : "CostumeButton",
					"type" : "button",

					"x" : 160+12,
					"y" : 60+10,

					"tooltip_text" : uiScriptLocale.COSTUME_TITLE,

					"default_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_costume_01_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_costume_02_hover.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_costume_03_active.png",
				},

				## MallButton
				{
					"name" : "MallButton",
					"type" : "button",

					"x" : 160+12,
					"y" : 90+10,

					"tooltip_text" : uiScriptLocale.MALL_TITLE,

					"default_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_itemshop_01_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_itemshop_02_hover.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_itemshop_03_active.png",
				},
				##Inventory Board
				{
					"name" : "inv_board",
					"type" : "new_board",

					"x" : 9,
					"y" : 258,

					"width" : 169,
					"height" : 297 + 30,

				},
				## Yang Board
				{
					"name" : "Yang_board",
					"type" : "new_board",

					"x" : 9,
					"y" : 552+5 + 30,

					"width" : 169,
					"height" : 0,

				},
				{
				    "name" : "ItemSlot",
				    "type" : "grid_table",

				    "x" : 14,
				    "y" : 258+5 + 30,

				    "start_index" : 0,
				    "x_count" : 5,
				    "y_count" : 9,
				    "x_step" : 32,
				    "y_step" : 32,

				    "image" : apollo_interface.PATCH_COMMON + "/slot_rectangle/slot.png",
				},
				 ## Print
				{
				    "name":"Money_Slot",
				    "type":"button",

				    "x":15,
				    "y":22*2,

				    "horizontal_align":"center",
				    "vertical_align":"bottom",

				    "default_image" : apollo_interface.PATCH_SPECIAL + "/inventory/chenar_yang.png",
				    "over_image" : apollo_interface.PATCH_SPECIAL + "/inventory/chenar_yang.png",
				    "down_image" : apollo_interface.PATCH_SPECIAL + "/inventory/chenar_yang.png",

				    "children" :
				    (
						{
							"name":"Money_Icon",
							"type":"image",

							"x":-27,
							"y":0,

							"image": apollo_interface.PATCH_SPECIAL_1 + "/yang.png",
						},

						{
							"name" : "Money",
							"type" : "text",

							"x" : 10,
							"y" : 6,

							"horizontal_align" : "right",
							"text_horizontal_align" : "right",
							"color" : 0xfff8d090,
							"text" : "111123456789",
						},
				    ),
				},{
					"name" : "TabControl",
					"type" : "window",

					"x" : 10,
					"y" : 33 + 191 + 9,

					"width" : 169,
					"height" : 32,

					"children" :
					(
						## Tab
						{
							"name" : "Inventory_Type_01",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 169,
							"height" : 32,

							"image" : INVENTORY_TAB_PATH+"tab_normal.sub",
						},
						{
							"name" : "Inventory_Type_02",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 169,
							"height" : 32,

							"image" : INVENTORY_TAB_PATH+"tab_book.sub",
						},
						{
							"name" : "Inventory_Type_03",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 169,
							"height" : 32,

							"image" : INVENTORY_TAB_PATH+"tab_stone.sub",
						},
						{
							"name" : "Inventory_Type_04",
							"type" : "image",

							"x" : 0,
							"y" : 0,

							"width" : 169,
							"height" : 32,

							"image" : INVENTORY_TAB_PATH+"tab_uitem.sub",
						},
						## RadioButton
						{
							"name" : "Inventory_Type_Button_01",
							"type" : "radio_button",
							"x" : 3, "y" : 0,
							"width" : 42, "height" : 30,
							"tooltip_text" : uiScriptLocale.INVENTORY_TITLE,
							"tooltip_x" : 0, "tooltip_y" : -13,
							"tooltip_text_color" : 0xffffba00,
						},
						{
							"name" : "Inventory_Type_Button_02",
							"type" : "radio_button",
							"x" : 3+42, "y" : 0,
							"width" : 41, "height" : 30,
							"tooltip_text" : uiScriptLocale.SPECIAL_INVENTORY_SKILLBOOK_TITLE,
							"tooltip_x" : 0, "tooltip_y" : -13,
							"tooltip_text_color" : 0xffffba00,
						},
						{
							"name" : "Inventory_Type_Button_03",
							"type" : "radio_button",
							"x" : 3+42+41, "y" : 0,
							"width" : 41, "height" : 30,
							"tooltip_text" : uiScriptLocale.SPECIAL_INVENTORY_STONE_TITLE,
							"tooltip_x" : 0, "tooltip_y" : -13,
							"tooltip_text_color" : 0xffffba00,
						},
						{
							"name" : "Inventory_Type_Button_04",
							"type" : "radio_button",
							"x" : 3+42+41+41, "y" : 0,
							"width" : 42, "height" : 30,
							"tooltip_text" : uiScriptLocale.SPECIAL_INVENTORY_MATERIAL_TITLE,
							"tooltip_x" : 0, "tooltip_y" : -13,
							"tooltip_text_color" : 0xffffba00,
						},
					),
				},
				## Inventar Seite I
				{
					"name" : "Inventory_Tab_01",
					"type" : "radio_button",

					"x" : 10 + 5,
					"y" : 33 + 195 + 40,

					"default_image" : INVENTORY_TAB_PATH+"tab_button_hover.sub",
					"over_image" : INVENTORY_TAB_PATH+"tab_button_down.sub",
					"down_image" : INVENTORY_TAB_PATH+"tab_button_active.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_1,

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
				## Inventar Seite II
				{
					"name" : "Inventory_Tab_02",
					"type" : "radio_button",

					"x" : 10 + 47,
					"y" : 33 + 195 + 40,

					"default_image" : INVENTORY_TAB_PATH+"tab_button_hover.sub",
					"over_image" : INVENTORY_TAB_PATH+"tab_button_down.sub",
					"down_image" : INVENTORY_TAB_PATH+"tab_button_active.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_2,

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
				## Inventar Seite III
				{
					"name" : "Inventory_Tab_03",
					"type" : "radio_button",

					"x" : 10 + 89,
					"y" : 33 + 195 + 40,

					"default_image" : INVENTORY_TAB_PATH+"tab_button_hover.sub",
					"over_image" : INVENTORY_TAB_PATH+"tab_button_down.sub",
					"down_image" : INVENTORY_TAB_PATH+"tab_button_active.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_3,

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
				## Inventar Seite IV
				{
					"name" : "Inventory_Tab_04",
					"type" : "radio_button",

					"x" : 10 + 131,
					"y" : 33 + 195 + 40,

					"default_image" : INVENTORY_TAB_PATH+"tab_button_hover.sub",
					"over_image" : INVENTORY_TAB_PATH+"tab_button_down.sub",
					"down_image" : INVENTORY_TAB_PATH+"tab_button_active.sub",
					"tooltip_text" : uiScriptLocale.INVENTORY_PAGE_BUTTON_TOOLTIP_4,

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
			),
		},
	),
}

