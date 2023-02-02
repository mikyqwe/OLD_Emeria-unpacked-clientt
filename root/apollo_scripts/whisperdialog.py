import uiScriptLocale, grp

import apollo_interface
ROOT = "d:/ymir work/ui/public/"
SMALL_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_01.sub"
LARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_03.sub"
XLARGE_VALUE_FILE = "d:/ymir work/ui/public/Parameter_Slot_04.sub"
CREATE_BOARD_X = 392
CREATE_BOARD_Y = 212
COLOR_LINE = 0xff5b5e5e

CREATE_BOARD_X2 = 190
CREATE_BOARD_Y2 = 205


window = {
	"name" : "WhisperDialog",
	"style" : ("movable", "float",),
	"x" : SCREEN_WIDTH + 447,
	"y" : 0,
	"width" : 447,
	"height" : 200,

	"children" :
	(
		{
			"name" : "Board_Whisper_Profile",
			"type" : "board",
			"style" : ("attach",),
			"x" : - 167,
			"y" : 15,
			"width" : 190,
			"height" : 205,
			"children" :
			(
			
				{
					"name" : "Background",
					"type" : "bar",
					"x" : 7,
					"y" : 10,
					"width" : CREATE_BOARD_X2,
					"height" : CREATE_BOARD_Y2-20,
					"color" : grp.GenerateColor(0.0, 0.0, 0.0, 0.6),
				},
			
				{ "name" : "LINE_BGCREATE_LEFT", "type" : "line", "x" : 8, "y" : 10, "width" : 0, "height" : CREATE_BOARD_Y2-20, "color" : COLOR_LINE, },
				{ "name" : "LINE_BGCREATE_DOWN", "type" : "line", "x" : 8, "y" : CREATE_BOARD_Y2-10, "width" : CREATE_BOARD_X2-17, "height" : 0, "color" : COLOR_LINE, },
				{ "name" : "LINE_BGCREATE_UP", "type" : "line", "x" : 8, "y" : 10, "width" : CREATE_BOARD_X2-17, "height" : 0, "color" : COLOR_LINE, },
			
				{
					"name" : "Whisper_Profile",
					"type" : "window",
					"x" : 9,
					"y" : 10,
					"width" : 0,
					"height" : 0,
					"children" :
					(
						## Whisper_Profile_Photo
						{
							"name" : "Whisper_Profile_Photo",
							"type" : "slotbar",
							"x" : 3,
							"y" : 5,
							"width" : 50,
							"height" : 48,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Photo_Icon",
									"type" : "expanded_image",
									"style" : ("attach",),
									"x" : 0,
									"y" : 3,
									"horizontal_align" : "center",
									"image" : "icon/face/warrior_m.tga",
								},	
							),
						},
						
						{ "name" : "LINE_UNDERCOVER_A", "type":"image", "x" : 52, "y" : 5, "image" : "d:/ymir work/ui/game/profile/bar.tga", },
						{ "name" : "LINE_UNDERCOVER_B", "type":"image", "x" : 52, "y" : 5 + 27, "image" : "d:/ymir work/ui/game/profile/bar.tga", },

						## Whisper_Profile_Empire
						{"name": "Whisper_Profile_Empire_Title", "type" : "text", "x" : 60, "y" : 7, "text" : "Empire"},
						{
							"name" : "Whisper_Profile_Empire",
							"type" : "slotbar",
							"x" : 125,
							"y" : 7,
							"width" : 19,
							"height" : 16,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Empire_Icon",
									"type" : "expanded_image",
									"style" : ("attach",),
									"x" : 2,
									"y" : 2,
									"image" : "d:/ymir work/ui/game/profile/empire_a_256.dds",
								},	
							),
						},
						
						## Whisper_Profile_Language
						{"name": "Whisper_Profile_Language_Title", "type" : "text", "x" : 60, "y" : 35, "text" : uiScriptLocale.PROFILE_LANGUAGE},
						{
							"name" : "Whisper_Profile_Language",
							"type" : "slotbar",
							"x" : 125,
							"y" : 35,
							"width" : 19,
							"height" : 16,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Language_Icon",
									"type" : "expanded_image",
									"style" : ("attach",),
									"x" : 1,
									"y" : 2,
									"image" : "d:/ymir work/ui/flag/en.tga",
								},	
							),
						},

						## Whisper_Profile_Name
						{
							"name" : "Whisper_Profile_Name", "type" : "text", "x" : 5, "y" : 65, "text" : uiScriptLocale.PROFILE_NAME,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Name_Slot",
									"type" : "image",
									"x" : 60,
									"y" : -2,
									"image" : LARGE_VALUE_FILE,
									"children" :
									(
										{"name" : "Whisper_Profile_Name_Value", "type": "text", "text": "", "x": 0, "y": 0, "all_align": "center"},
									),
								},
							),
						},
						
						## Whisper_Profile_Level
						{
							"name" : "Whisper_Profile_Level", "type" : "text", "x" : 5, "y" : 85, "text" : uiScriptLocale.PROFILE_LEVEL,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Level_Slot",
									"type" : "image",
									"x" : 60,
									"y" : -2,
									"image" : LARGE_VALUE_FILE,
									"children" :
									(
										{"name" : "Whisper_Profile_Level_Value", "type": "text", "text": "", "x": 0, "y": 0, "all_align": "center"},
									),
								},
							),
						},
						
						## Whisper_Profile_Guild
						{
							"name" : "Whisper_Profile_Guild", "type" : "text", "x" : 5, "y" : 105, "text" : uiScriptLocale.PROFILE_GUILD,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Guild_Slot",
									"type" : "image",
									"x" : 60,
									"y" : -2,
									"image" : LARGE_VALUE_FILE,
									"children" :
									(
										{"name" : "Whisper_Profile_Guild_Value", "type":"text", "text": "", "x":0, "y":0, "all_align": "center"},
									),
								},
							),
						},
						
						## Whisper_Profile_Status
						{
							"name" : "Whisper_Profile_Status", "type" : "text", "x" : 5, "y" : 125, "text" : uiScriptLocale.PROFILE_STATUS,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Status_Slot",
									"type" : "image",
									"x" : 60,
									"y" : -2,
									"image" : LARGE_VALUE_FILE,
									"children" :
									(
										{"name" : "Whisper_Profile_Status_Value", "type": "text", "text": "", "x": 2, "y": 1, "text_horizontal_align" : "left"},
									),
								},
							),
						},

						## Whisper_Profile_Birthday
						{
							"name" : "Whisper_Profile_Birthday", "type" : "text", "x" : 5, "y" : 145, "text" : uiScriptLocale.PROFILE_BIRTHDAY,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Birthday_Slot",
									"type" : "image",
									"x" : 60,
									"y" : -2,
									"image" : LARGE_VALUE_FILE,
									"children" :
									(
										{"name" : "Whisper_Profile_Birthday_Value", "type":"text", "text": "", "x":0, "y":0, "all_align": "center"},
									),
								},
							),
						},
						
						## Whisper_Profile_Location
						{
							"name" : "Whisper_Profile_Location", "type" : "text", "x" : 5, "y" : 165, "text" : uiScriptLocale.PROFILE_LOCATION,
							"children" :
							(
								{
									"name" : "Whisper_Profile_Location_Slot",
									"type" : "image",
									"x" : 60,
									"y" : -2,
									"image" : LARGE_VALUE_FILE,
									"children" :
									(
										{"name" : "Whisper_Profile_Location_Value", "type":"text", "text": "", "x":2, "y":0, "all_align": "center"},
									),
								},
							),
						},
					),
				},
			)
		},
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 280,
			"height" : 200,

			"children" :
			(	
				## Title
				{
					"name" : "name_slot",
					"type" : "image",
					"style" : ("attach",),

					"x" : 10,
					"y" : 10,

					"image": apollo_interface.PATCH_SPECIAL + "/whisper/name_slot.png",

					"children" :
					(
						{
							"name" : "titlename",
							"type" : "text",

							"x" : 10,
							"y" : 5,
							"color" : 0xfff8d090,
							"text" : uiScriptLocale.WHISPER_NAME,
						},
						{
							"name" : "titlename_edit",
							"type" : "editline",

							"x" : 10,
							"y" : 5,

							"width" : 120,
							"height" : 17,

							"input_limit" : PLAYER_NAME_MAX_LEN,

							"text" : uiScriptLocale.WHISPER_NAME,
						},
					),
				},

				{
					"name" : "gamemastermark",
					"type" : "expanded_image",
					"style" : ("attach",),

					"x" : 206,
					"y" : 6,

					"x_scale" : 0.2,
					"y_scale" : 0.2,

					"image" : LOCALE_PATH + "/effect/ymirred.tga",
				},
				{
					"name" : "language_flag",
					"type" : "expanded_image",
					"style" : ("attach",),
					"x" : 500,
					"y" : 25,
					"x_scale" : 0.2,
					"y_scale" : 0.2,
				},
				
				{
					"name" : "empire_flag",
					"type" : "expanded_image",
					"style" : ("attach",),
					"x" : 500,
					"y" : 25,
					"x_scale" : 0.2,
					"y_scale" : 0.2,
				},

				## Button
				{
					"name" : "ignorebutton",
					"type" : "toggle_button",

					"x" : 145,
					"y" : 10,

					"text" : uiScriptLocale.WHISPER_BAN,

					"default_image" : "d:/ymir work/ui/public/small_thin_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/small_thin_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/small_thin_button_03.sub",
				},
				{
					"name" : "reportviolentwhisperbutton",
					"type" : "button",

					"x" : 145,
					"y" : 10,

					"text" : uiScriptLocale.WHISPER_REPORT,

					"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
				},
				{
					"name" : "acceptbutton",
					"type" : "button",

					"x" : 145,
					"y" : 10,

					"text" : uiScriptLocale.OK,

					"default_image" : apollo_interface.PATCH_SPECIAL + "/whisper/ok_01_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/whisper/ok_02_hover.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/whisper/ok_03_active.png",
				},
				{
					"name" : "minimizebutton",
					"type" : "button",

					"x" : 280 - 41,
					"y" : 12,

					"tooltip_text" : uiScriptLocale.MINIMIZE,

					"default_image" : apollo_interface.PATCH_SPECIAL + "/whisper/thinboard_minimize_01_normal.png",
					"over_image" : apollo_interface.PATCH_SPECIAL + "/whisper/thinboard_minimize_02_hover.png",
					"down_image" : apollo_interface.PATCH_SPECIAL + "/whisper/thinboard_minimize_03_active.png",
				},
				#{
				#	"name" : "closebutton",
				#	"type" : "button",
                #
				#	"x" : 280 - 24,
				#	"y" : 12,
                #
				#	"tooltip_text" : uiScriptLocale.CLOSE,
                #
				#	"default_image" : apollo_interface.PATCH_SPECIAL + "/whisper/thinboard_close_01_normal.png",
				#	"over_image" : apollo_interface.PATCH_SPECIAL + "/whisper/thinboard_close_02_hover.png",
				#	"down_image" : apollo_interface.PATCH_SPECIAL + "/whisper/thinboard_close_03_active.png",
				#},

				## ScrollBar
				{
					"name" : "scrollbar",
					"type" : "new_scrollbar",

					"x" : 280 - 25,
					"y" : 35,

					"size" : 280 - 160,
				},

				## Edit Bar
				{
					"name" : "editbar",
					"type" : "bar",

					"x" : 10,
					"y" : 200 - 60,

					"width" : 280 - 18,
					"height" : 50,

					"color" : 0x77000000,

					"children" :
					(
						{
							"name" : "chatline",
							"type" : "editline",

							"x" : 5,
							"y" : 5,

							"width" : 280 - 70,
							"height" : 40,

							"with_codepage" : 1,
							"input_limit" : 40,
							"limit_width" : 280 - 90,
							"multi_line" : 1,
							

						},
						
						{
							"name" : "sendbutton",
							"type" : "button",

							"x" : 280 - 80,
							"y" : 25,

							"text" : uiScriptLocale.WHISPER_SEND,

							"default_image" : apollo_interface.PATCH_SPECIAL + "/whisper/send_01_normal.png",
							"over_image" : apollo_interface.PATCH_SPECIAL + "/whisper/send_02_hover.png",
							"down_image" : apollo_interface.PATCH_SPECIAL + "/whisper/send_03_active.png",
						},
					),
				},
			),
		},
		{
			"name" : "titlename_editBar",
			"type" : "image",
			"style" : ("attach",),
			"x" : 14,
			"y" : 40,
			"image":"d:/ymir work/ui/public/Parameter_Slot_05.sub",
			"children" :
			(
				{
					"name" : "titlename_edit",
					"type" : "editline",
					"x" : 3,
					"y" : 3,
					"width" : 120,
					"height" : 17,
					"input_limit" : PLAYER_NAME_MAX_LEN,
					"text" : uiScriptLocale.WHISPER_NAME,
				},
			),
		},
		{
			"name" : "acceptbutton",
			"type" : "button",

			"x" : 14 + 135,
			"y" : 40,

			"text" : uiScriptLocale.OK,

			"default_image" : "d:/ymir work/ui/public/small_thin_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/small_thin_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/small_thin_button_03.sub",
		},
	),
}
