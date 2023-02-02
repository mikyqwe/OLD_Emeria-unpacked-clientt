import uiScriptLocale
import apollo_interface

default_x = 541-107
default_y = 370
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
				{
					"name" : "Options_Page",
					"type" : "window",
					"style" : ("attach",),
					"x" : 0,
					"y" : 0,
					"width" : default_x,
					"height" : default_y,
					"children" :
					(
						## Title Area
						{
							"name" : "Options_TitleBar", "type" : "titlebar", "x" : 8, "y" : 7, "width" : default_x-20, "color" : "red",
							"children" :
							(
								{ "name" : "ButtonCollapse", "type" : "button", "x":321+20, "y":5, "default_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_expand_01_normal.png", "over_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_expand_02_hover.png", "down_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_expand_03_active.png", },
								{ "name" : "ButtonExpande", "type" : "button", "x":321, "y":5, "default_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_collapse_01_normal.png", "over_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_collapse_02_hover.png", "down_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_collapse_03_active.png", },
								{ "name" : "TitleName", "type":"text", "x":0, "y":-11, "text":apollo_interface.OPTION_TITLE, "color":0xffcaa76f, "all_align":"center" },
							),
						},

						{"name":"Options_Input", "type":"new_board", "x":13+367, "y":35, "width":143-110, "height":323},

						{
							"name":"Player_Status", "type":"window", "x":8, "y":36, "width":372, "height":350,
							"children" :
							(
									{"name":"Player_Status_1", "type":"new_board", "x":0, "y":0, "width":371, "height":125,
									"children" :
									(
										{ "name":"Title", "type":"text", "x":188, "y":15, "text":apollo_interface.PAGE_TEXT_OPTIONS_1, "color":0xffcaa76f, "text_horizontal_align":"center" },
										{ "name" : "Bar", "type" : "image", "x" : 82, "y" : 12, "image" : apollo_interface.PATCH_HORIZONTAL_BAR+"center.png", },
										{ "name":"Title_1", "type":"text", "x":70, "y":55, "text":apollo_interface.PVP_MODE, "color":0xffa08784, "text_horizontal_align":"center" },

									),
									},
									{"name":"Player_Status_2", "type":"new_board", "x":0, "y":127, "width":371, "height":195,
									"children" :
									(
										{ "name":"Title_1", "type":"text", "x":70, "y":30, "text":apollo_interface.BLOCK, "color":0xffa08784, "text_horizontal_align":"center" },

									),
									},
							),
						},
						{
							"name":"Player_Block_Status", "type":"new_board", "x":8, "y":36, "width":371, "height":322,
							"children" :
							(
								{ "name":"Title", "type":"text", "x":188, "y":15, "text":apollo_interface.PAGE_TEXT_OPTIONS_1, "color":0xffcaa76f, "text_horizontal_align":"center" },
								{ "name" : "Bar", "type" : "image", "x" : 82, "y" : 12, "image" : apollo_interface.PATCH_HORIZONTAL_BAR+"center.png", },
							),
						},
						{
							"name":"Player_Grafics", "type":"window", "x":8, "y":36, "width":372, "height":350,
							"children" :
							(
									{"name":"Player_Grafics_1", "type":"new_board", "x":0, "y":0, "width":371, "height":90,
									"children" :
									(
										{ "name":"Title", "type":"text", "x":188, "y":15, "text":apollo_interface.PAGE_TEXT_OPTIONS_3, "color":0xffcaa76f, "text_horizontal_align":"center" },
										{ "name" : "Bar", "type" : "image", "x" : 82, "y" : 12, "image" : apollo_interface.PATCH_HORIZONTAL_BAR+"center.png", },
									),
									},
									{"name":"Player_Grafics_2", "type":"new_board", "x":0, "y":92, "width":371, "height":80,},
									{"name":"Player_Grafics_3", "type":"new_board", "x":0, "y":92+82, "width":371, "height":148,},
							),
						},
						{
							"name":"Player_Sound", "type":"new_board", "x":8, "y":36, "width":371, "height":322,
							"children" :
							(
								{ "name":"Title", "type":"text", "x":188, "y":15, "text":apollo_interface.PAGE_TEXT_OPTIONS_4, "color":0xffcaa76f, "text_horizontal_align":"center" },
								{ "name" : "Bar", "type" : "image", "x" : 82, "y" : 12, "image" : apollo_interface.PATCH_HORIZONTAL_BAR+"center.png", },
							),
						},
					),
				},
			),
		},
	),
}
