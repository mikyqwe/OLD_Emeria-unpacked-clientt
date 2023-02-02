import uiScriptLocale
import constInfo


PET_UI_ROOT = "d:/ymir work/ui/pet/"

HATCHING_WINDOW_WIDTH	= 176
HATCHING_WINDOW_HEIGHT	= 195

TITLEBAR_X = 8
TITLEBAR_Y = 7
TITLEBAR_WIDTH = HATCHING_WINDOW_WIDTH - 15

window = {
	"name" : "PetHatchingWindow",
	"style" : ("movable", "float",),
	
	"x" : SCREEN_WIDTH / 2 - HATCHING_WINDOW_WIDTH / 2,
	"y" : SCREEN_HEIGHT / 2 - HATCHING_WINDOW_HEIGHT / 2,

	"width" : HATCHING_WINDOW_WIDTH,
	"height" : HATCHING_WINDOW_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : HATCHING_WINDOW_WIDTH,
			"height" : HATCHING_WINDOW_HEIGHT,

			"children" :
			(
				# Pet Hatching Window Title
				{
					"name" : "PetHatching_TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : TITLEBAR_X,
					"y" : TITLEBAR_Y,

					"width" : TITLEBAR_WIDTH,
				
					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y": -8, "text": "", "all_align":"center" },
					),
				},
				
				## Pet Hatching Slot Img
				{ 
					"name" : "SlotBG", 
					"type" : "expanded_image", 
					"style" : ("attach",), 
					"x" : 68, 
					"y" : 40, 
					"image" : "d:/ymir work/ui/pet/Pet_Incu_slot_001.tga",
				},
				
				## Pet Hatching Slot
				{
					"name" : "HatchingItemSlot",
					"type" : "slot",
						
					#"image" : "d:/ymir work/ui/pet/Pet_Incu_slot_001.tga",

					"x" : 68 + 4,
					"y" : 40 + 4,
					"width" : 32,
					"height" : 32,

					"slot" : ({"index":0, "x":0, "y":0, "width":32, "height":32,},),
				},
				
				## Pet Hatching Money
				{
					"name" : "HatchingMoneyWindow", "type" : "window", "x" : 13, "y" : 136, "width" : 150, "height" : 14, "style" : ("attach",),
					"children" :
					(
						{"name":"HatchingMoney", "type":"text", "x":0, "y":0, "text": "", "r":1.0, "g":1.0, "b":1.0, "a":1.0, "all_align" : "center"},
					),
				},
				
				## Pet Hatching Button
				{
					"name" : "HatchingButton",
					"type" : "button",

					"x" : 0,
					"y" : 155,

					"text" : uiScriptLocale.PET_HATCHING_BUTTON,

					"default_image" : PET_UI_ROOT + "pet_gui_button_default.tga",
					"over_image" : PET_UI_ROOT + "pet_gui_button_hover.tga",
					"down_image" : PET_UI_ROOT + "pet_gui_button_down.tga",
					"disable_image" : PET_UI_ROOT + "pet_gui_button_down.tga",
					"horizontal_align" : "center",
				},
				
				## Pet Naming Area
				{
					"name" : "PetNamingBG", 
					"type" : "expanded_image",
					"style" : ("attach",),
					
					"x" : 12, 
					"y" : 83, 
					
					"image" : "d:/ymir work/ui/pet/Pet_Incu_001.tga",
					
					"children" :
					(
						## Pet Name Edit
						{
							"name" : "pet_name",
							"type" : "editline",

							"x" : 11,
							"y" : 28,

							"width" : 129,
							"height" : 16,

							"input_limit" : 12,

							#"text" : uiScriptLocale.WHISPER_NAME,
						},
					),
				},
						
				## Pet Naming Title
				{ 
					"name" : "PetNamingTitleWindow", "type" : "window", "x" : 22, "y" : 86, "width" : 130, "height" : 14, "style" : ("attach",),
					"children" :
					(
						{"name":"PetNamingTitle", "type":"text", "x":0, "y": 0, "text": uiScriptLocale.PET_HATCHING_NIK, "all_align" : "center"},
					),
				},
			),				
		},
	),
}
