import uiScriptLocale
import apollo_interface

default_x = 441-107
default_y = 396 + 110
ICON_SLOT_FILE = apollo_interface.PATCH_COMMON+"/slot_ellipse/slot.png"


window = {
	"name" : "CharacterWindow",
	"style" : ("movable", "float",),
	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - 361) / 2,
	"width" : default_x,
	"height" : default_y,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board2",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width"  : default_x,
			"height" : default_y,
			"children":
			(
				## Title Area
				{
					"name" : "Character_TitleBar", "type" : "titlebar", "x" : 49, "y" : 7, "width" : 380, "color" : "red",
					"children" :
					(
						{ "name" : "ButtonCollapse", "type" : "button", "x":321-110, "y":5, "default_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_expand_01_normal.png", "over_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_expand_02_hover.png", "down_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_expand_03_active.png", },
						{ "name" : "ButtonExpande", "type" : "button", "x":321, "y":5, "default_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_collapse_01_normal.png", "over_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_collapse_02_hover.png", "down_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_collapse_03_active.png", },
						{ "name" : "TitleName", "type":"text", "x":0, "y":-11, "text":"Status", "color":0xffcaa76f, "all_align":"center" },
					),
				},
				{
					"name" : "Character_Page",
					"type" : "window",
					"style" : ("attach",),
					"x" : 0,
					"y" : 0,
					"width" : default_x,
					"height" : default_y,
					"children" :
					(
						{
							"name":"Caracter_Header", "type":"new_board", "x":8, "y":34, "width":271, "height":78,
							"children" :
							(
								## Name Slot
								{"name" : "NameSlot", "type" : "inputnew", "x" : 65, "y" : 11-5, "width" : 100,
								"children":
								(
									{ "name":"Character_Name", "type":"text", "x":45, "y":8, "text":"Noname", "color":0xffa07970, "text_horizontal_align":"center" },

								),
								},
								## Guild Slot
								{"name" : "Guild_Name_Slot", "type" : "inputnew", "x" : 65+95, "y" : 11-5, "width" : 100,
								"children":
								(
									{ "name":"Guild_Name", "type":"text", "x":45, "y":8, "text":"None", "color":0xffa07970, "text_horizontal_align":"center" },
								),
								},

								{ "name":"Procent", "type":"text", "x":42, "y":38, "text":"49,98%", "color":0xfff8d090, "text_horizontal_align":"center" },
								{ "name":"Exp_Value", "type":"text", "x":42+70, "y":38,  "text":"123", "color":0xffa08784, "text_horizontal_align":"center" },
								{ "name":"RestExp_Value", "type":"text", "x":42+70+95, "y":38,  "text":"123", "color":0xffa08784, "text_horizontal_align":"center" },
								{ "name" : "Exp_Slot", "type" : "expanded_image", "x" : 15, "y" : 55, "image" : apollo_interface.PATCH_SPECIAL+"/character/exp_gauge_empty.png", },
								{ "name" : "Exp_Full", "type" : "expanded_image", "x" : 15, "y" : 55, "image" : apollo_interface.PATCH_SPECIAL+"/character/exp_gauge_full.png", },
							),
						},
						{"name":"Caracter_Input", "type":"new_board", "x":13+267, "y":34, "width":143-110, "height":350},

						{
							"name":"Board_Status_0", "type":"new_board", "x":8, "y":36+78, "width":271, "height":110,
							"children" :
							(
								{ "name":"Title", "type":"text", "x":271/2, "y":8, "text":"Status", "color":0xffcaa76f, "text_horizontal_align":"center" },
								{ "name" : "Bar", "type" : "image", "x" : 32, "y" : 2, "image" : apollo_interface.PATCH_HORIZONTAL_BAR+"center.png", },
							),
						},
						{
							"name":"Board_Status_1", "type":"new_board", "x":8, "y":36+81+109, "width":271, "height":158,
							"children" :
							(
								{ "name":"Title", "type":"text", "x":271/2, "y":8, "text":apollo_interface.POINTS_DESK, "color":0xffa08784, "text_horizontal_align":"center" },

							),
						},
						{
							"name":"Board_Caracteristics", "type":"new_board", "x":8, "y":36+76, "width":271, "height":110+160+3,
							"children" :
							(
								{ "name":"Title", "type":"text", "x":271/2, "y":8, "text":apollo_interface.PAGE_TEXT_2, "color":0xffcaa76f, "text_horizontal_align":"center" },
								{ "name" : "Bar", "type" : "image", "x" : 32, "y" : 2, "image" : apollo_interface.PATCH_HORIZONTAL_BAR+"center.png", },
							),
						},
						{
							"name":"Board_Abilities", "type":"new_board", "x":8, "y":36+76, "width":271, "height":110+160+3,
							"children" :
							(
								# { "name":"Title", "type":"text", "x":271/2, "y":8, "text":apollo_interface.PAGE_TEXT_4, "color":0xffcaa76f, "text_horizontal_align":"center" },
								{ "name" : "Bar", "type" : "image", "x" : 32, "y" : 2, "image" : apollo_interface.PATCH_HORIZONTAL_BAR+"center.png", },

								{ "name":"Title1", "type":"text", "x":271/2, "y":8+153, "text":apollo_interface.SUPPORT_TITLE, "color":0xffcaa76f, "text_horizontal_align":"center" },
								{ "name" : "Bar1", "type" : "image", "x" : 32, "y" : 2+153, "image" : apollo_interface.PATCH_HORIZONTAL_BAR+"center.png", },
							),
						},
						{
							"name":"Board_Emotion", "type":"new_board", "x":8, "y":36+76, "width":271, "height":110+160+3,
							"children" :
							(
								{ "name":"Title", "type":"text", "x":271/2, "y":8, "text":apollo_interface.EMOTICON_PAGE_TITLE_NORMAL, "color":0xffcaa76f, "text_horizontal_align":"center" },
								{ "name" : "Bar", "type" : "image", "x" : 32, "y" : 2, "image" : apollo_interface.PATCH_HORIZONTAL_BAR+"center.png", },

								{ "name":"Title1", "type":"text", "x":271/2, "y":8+153, "text":apollo_interface.EMOTICON_PAGE_TITLE_INTERAK, "color":0xffcaa76f, "text_horizontal_align":"center" },
								{ "name" : "Bar1", "type" : "image", "x" : 32, "y" : 2+153, "image" : apollo_interface.PATCH_HORIZONTAL_BAR+"center.png", },
								
								{ "name":"Title2", "type":"text", "x":271/2, "y":8+153+70, "text":"Special Emotions", "color":0xffcaa76f, "text_horizontal_align":"center" },
								{ "name" : "Bar2", "type" : "image", "x" : 32, "y" : 2+153+70, "image" : apollo_interface.PATCH_HORIZONTAL_BAR+"center.png", },
							),
						},
						{
							"name":"Board_Quest", "type":"new_board", "x":8, "y":36+76, "width":271, "height":110+160+3,
							"children" :
							(
								{ "name":"Title", "type":"text", "x":271/2, "y":8, "text":apollo_interface.PAGE_TEXT_7, "color":0xffcaa76f, "text_horizontal_align":"center" },
								{ "name" : "Bar", "type" : "image", "x" : 32, "y" : 2, "image" : apollo_interface.PATCH_HORIZONTAL_BAR+"center.png", },
							),
						},

						
						## Face Slot
						{ "name" : "Face_Slot", "type" : "image", "x" : -10, "y" : -10-5, "image" : apollo_interface.PATCH_SPECIAL+"/character/character_slot.png", },
						{ "name" : "Face_Image", "type" : "image", "x" : -5, "y" : -31-5, "image" : apollo_interface.PATCH_ICON+"/faces/icon_wshaman.png" },
						{ "name":"Level_Header", "type":"image", "x":40, "y":44-5, "image":apollo_interface.PATCH_COMMON+"/input/level_round.png" },
						{ "name":"Level_Value", "type":"text", "x":57, "y":53-5, "text":"100", "color":0xfff8d090, "text_horizontal_align":"center" },

					## Header
					),
				},
			),
		},
	),
}
