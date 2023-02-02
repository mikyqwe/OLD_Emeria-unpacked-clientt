import uiScriptLocale
import item
import apollo_interface 

EQUIPMENT_START_INDEX = 180

window = {
	"name" : "BeltInventoryWindow",

	"x" : SCREEN_WIDTH - 176 - 140,
	"y" : SCREEN_HEIGHT - 37 - 565 + 209 + 32,

	"width" : 148,
	"height" : 139,	

	"children" :
	(
		## Expand Buttons
		{
			"name" : "ExpandBtn",
			"type" : "button",

			"x" : 2,
			"y" : 15,

			"default_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_belt_open_01_normal.png",
			"over_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_belt_open_02_hover.png",
			"down_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_belt_open_03_active.png",
		},

		
		## Belt Inventory Layer (include minimize button)
		{
			"name" : "BeltInventoryLayer",
#			"type" : "board",
#			"style" : ("attach", "float"),

			"x" : 5,
			"y" : 0,

			"width" : 148,
			"height" : 139,

			"children" :
			(
				## Minimize Button
				{
					"name" : "MinimizeBtn",
					"type" : "button",

					"x" : 2,
					"y" : 15,

					"width" : 10,
					
					"default_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_belt_close_01_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_belt_close_02_hover.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/inventory/btn_belt_close_03_active.png",
					
				},

				## Real Belt Inventory Board
				{
					"name" : "BeltInventoryBoard",
					"type" : "image",
					"style" : ("attach", "float"),

					"x" : 10,
					"y" : 0,

					"width" : 138,
					"height" : 139,
	
					"image" : apollo_interface.PATCH_SPECIAL + "/inventory/wnd_belt.png",
					
					
					"children" :
					(
						## Belt Inventory Slots
						{
							"name" : "BeltInventorySlot",
							"type" : "grid_table",

							"x" : 9,
							"y" : 9,

							"start_index" : item.BELT_INVENTORY_SLOT_START,
							"x_count" : 4,
							"y_count" : 4,
							"x_step" : 32,
							"y_step" : 32,

							"image" : apollo_interface.PATCH_COMMON + "/slot_rectangle/slot.png",
						},
					),
				},
			)
		},

	),
}
