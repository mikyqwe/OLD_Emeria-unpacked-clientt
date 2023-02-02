import apollo_interface
import uiScriptLocale

ROOT = "d:/ymir work/ui/game/"
ROW_BACKGROUND 	= 'd:/ymir work/ui/public/slot_base.sub'
ICON_FILE 		= apollo_interface.APOLLO_FACE + "icon_mwarrior.png"

BOARD_WIDTH  = 250
BOARD_HEIGHT = 124
ROW_START    = 28

TITLE_COLOR = {
	"r" : 254.0/255.0,
	"g" : 253.0/255.0,
	"b" : 196.0/255.0,
}

window = {
	"name" : "ExchangeDialog",

	"x" : SCREEN_WIDTH - 175 - BOARD_WIDTH,
	"y" : 65,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : BOARD_WIDTH - 14,
					"color" : "gray",

					"children" :
					(
						{
							"name" : "Title",
							"type" : "text",
							"text" : apollo_interface.DUEL_ACCEP,
							"x" : 0,
							"y" : -10,
							"fontsize" : "LARGE",
							"outline" : 1,
							"all_align" : "center",
							"color" : 0xfff8d090,
						},
					),
				},

				{
					"name" : "Guide_Background_0", "type" : "image",
					"x" : 5 + 0,
					"y" : ROW_START + (0 * 58) + 0,
					"width" : BOARD_WIDTH - 10,
					"height" : 58,
				},
				# {
					# "name" : "Chenars",
					# "type" : "image",
					# "x" : 30,
					# "y" : 40,
					# "width" : BOARD_WIDTH - 10,
					# "height" : 58,
					# "image" : "duel/chenars.png",
				# },
				{
					"name" : "ChenarName",
					"type" : "expanded_image",
					"x" : 30,
					"y" : 45,

					"width" : BOARD_WIDTH - 10,
					"height" : 58,

					"x_scale":1.2,
					"y_scale":0.73,

					"image" : apollo_interface.PATCH_SPECIAL + "/guild/chenar1.png",
				},
				{
					"name" : "ChenarText",
					"type" : "expanded_image",
					"x" : 30,
					"y" : 68,

					"width" : BOARD_WIDTH - 10,
					"height" : 58,

					"x_scale":1.45,
					"y_scale":0.73,

					"image" : apollo_interface.PATCH_SPECIAL + "/guild/chenar1.png",
				},
				{
					"name" : "CharacterIcon",
					"type" : "image",
					"x" : 5 + 5,
					"y" : ROW_START + (0 * 58) + 12,
					"width" : 32, "height" : 32,
					"image" : ICON_FILE,
				},
				{
					"name" : "RequesterName",
					"type" : "text",
					"text" : "Apollo Lv. 127",
					"x" : 5 + 60,
					"y" : ROW_START + (0 * 58) + 19,
					"color" : 0xfff8d090,
				},

				{
					"name" : "DuelText",
					"type" : "text",
					"text" : apollo_interface.DUEL_QUESTION,
					"x" : 5 + 60,
					"y" : ROW_START + (0 * 58) + 42,
					"color" : 0xffa08784,
				},



				## Owner
				{
					"name" : "Owner",
					"type" : "window",

					"x" : 124,
					"y" : 50,

					"width" : 130,
					"height" : 130,

					"children" :
					(

						{
							"name" : "Chenar",
							"type" : "image",

							"x" : 50,
							"y" : -5,

							"width" : 130,
							"height" : 130,


							"image" : "duel/chenar.png",
						},
						{
							"name" : "ApplyButton",
							"type" : "button",

							"x" : 52,
							"y" : -2,

							"text_color" : 0xfff8d090,

							"text" : apollo_interface.DUEL_ACCEP,

							"default_image" :  apollo_interface.PATCH_DUEL+"/btn_option_on.png",
							"over_image" :  apollo_interface.PATCH_DUEL+"/btn_option_ds.png",
							"down_image" :  apollo_interface.PATCH_DUEL+"/btn_option_dn.png",
						},

						{
							"name" : "DenyButton",
							"type" : "button",

							"x" : 52,
							"y" : 28,

							"text_color" : 0xfff8d090,

							"text" : apollo_interface.DUEL_DECLINE,

							"default_image" : apollo_interface.PATCH_DUEL+"/btn_option_on.png",
							"over_image" : apollo_interface.PATCH_DUEL+"/btn_option_ds.png",
							"down_image" : apollo_interface.PATCH_DUEL+"/btn_option_dn.png",
						},
					),
				},
			),
		},
	),
}
