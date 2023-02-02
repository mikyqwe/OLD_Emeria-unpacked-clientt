import uiScriptLocale
import constInfo
import apollo_interface

PET_UI_ROOT = "d:/ymir work/ui/pet/"
EXP_Y_ADD_POSITION = 0

FEED_WINDOW_WIDTH = 130
FEED_WINDOW_HEIGHT = 170

TITLEBAR_X = 8
TITLEBAR_Y = 7
TITLEBAR_WIDTH = FEED_WINDOW_WIDTH - 15

window = {
	"name" : "PetFeedWindow",
	"style" : ("movable", "float",),
	
	"x" : SCREEN_WIDTH - 500 + 328 -148,
	"y" : SCREEN_HEIGHT - 595 + 240,	

	"width" : 130,
	"height" : 170,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : FEED_WINDOW_WIDTH,
			"height" : FEED_WINDOW_HEIGHT,

			"children" :
			(
				## Pet Feed Title
				{
					"name" : "PetFeed_TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : TITLEBAR_X,
					"y" : TITLEBAR_Y,

					"width" : TITLEBAR_WIDTH,
					
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":-9, "y": -9, "text": uiScriptLocale.PET_FEED_ITEM_TITLE, "all_align":"center" },
					),
				},
				## Pet Feed Area
				{
					"name" : "Pet_Feed_Area",
					"type" : "window",
					"style" : ("attach",),
					
					"x" : 0,
					"y" : 26,
					
					"width" : 128,
					"height" : 144,
					"children" :
					(								
						## Pet Feed Slot
						{
							"name" : "FeedItemSlot",
							"type" : "grid_table",

							"x" : 17,
							"y" : 11,

							"start_index" : 0,
							"x_count" : 3,
							"y_count" : 3,
							"x_step" : 32,
							"y_step" : 32,

							"image" : apollo_interface.PATCH_COMMON + "/slot_rectangle/slot.png",
							#"image" : "d:/ymir work/ui/public/Slot_Base.sub"
						},
						
						## Pet Feed Button
						{
							"name" : "FeedButton",
							"type" : "button",

							"x" : 0,
							"y" : 110,

							"text" : uiScriptLocale.PET_FFED_BUTTON_TEXT,
							
							"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
							"horizontal_align" : "center",
						},
					),						
					
				}, ## End of Pet Feed Area
			),				
		},
	),
}
