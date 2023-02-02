import uiScriptLocale
import apollo_interface

ROOT_PATH = "d:/ymir work/ui/public/"
LOCALE_PATH = uiScriptLocale.SELECT_PATH

BOARD_X = SCREEN_WIDTH * (65) / 800
BOARD_Y = SCREEN_HEIGHT * (220) / 600

BOARD_ITEM_ADD_POSITION = -40

window = {
	"name" : "SelectCharacterWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "BackGround", "type" : "expanded_image",
			"x" : 0,
			"y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image": "%s/background.png" %apollo_interface.PATCH_LOGIN,
		},
		{
			"name" : "charrend",
			"type" : "text",

			"x" : (SCREEN_WIDTH/2) + 400,
			"y" : (SCREEN_HEIGHT/2) - 300,

			"width" : "800",
			"height" : "600",
		},

		{
			"name" : "GuildNameSlot",
			"type" : "text",

			"x" : (SCREEN_WIDTH/2) + 160,
			"y" : (SCREEN_HEIGHT/2) - 140,

			"text" : "",

			"children" :
			(
				{
					"name" : "GuildNamea",
					"type" : "image",

					"x" : -20,
					"y" : 8,

					"image" : "%s/costume/pointer.png" % apollo_interface.PATCH_COMMON,
				},
				{
					"name" : "GuildSpecificator",
					"type" : "text",

					"x" : 110/2,
					"y" : 1,

					"fontname" : "Tahoma:16.5",

					"text" : "Gilde:",
					"color" : apollo_interface.COLOR_HOVER,
					"all_align" : "center",
				},

				{
					"name" : "GuildName",
					"type" : "text",

					"x" : 60 + 130/2,
					"y" : 1,

					"fontname" : "Tahoma:16",
					"color" : 0xff940000,
					"text" : uiScriptLocale.SELECT_NO_GUILD,

					"all_align" : "center",
				},
			),
		},
		{
			"name" : "character_name",
			"type" : "text",

			"x" : (SCREEN_WIDTH/2) - 410,
			"y" : (SCREEN_HEIGHT/2) - 75,

			"text" : "",

			"children" :
			(
				{
					"name" : "character_name_slot",
					"type" : "image",

					"x" : 100,
					"y" : 15,

					"image" : "%s/costume/pointer_fliped.png" % apollo_interface.PATCH_COMMON,
				},
				{
					"name" : "character_name_indicator",
					"type" : "text",

					"x" : 115 + 110/2,
					"y" : -2,

					"text" : "Name:",
					"fontname" : "Tahoma:16.5",
					"color" : 0xffffd286,
					"text_horizontal_align" : "left",
				},
				{
					"name" : "character_name_value",
					"type" : "text",

					"x" : 155 + 130/2,
					"y" : -2,

					"text" : "Apollo",
					"fontname" : "Tahoma:16",
					"color" : 0xffffd286,
					"text_horizontal_align" : "left",
				},
			),
		},
		{
			"name" : "character_level",
			"type" : "text",

			"x" : (SCREEN_WIDTH/2) - 350,
			"y" : (SCREEN_HEIGHT/2) - 256  ,


			"text" : "",

			"children" :
			(
				{
					"name" : "character_level_slot",
					"type" : "image",

					"x" : 170,
					"y" : 20,

					"image" : "%s/costume/pointer_level.png" % apollo_interface.PATCH_COMMON,
				},
				{
					"name" : "character_level_indicator",
					"type" : "text",

					"x" : 140 + 130/2,
					"y" : 5,

					"text" : "Level:",
					"fontname" : "Tahoma:16.5",
					"color" : apollo_interface.COLOR_HOVER,

					"text_horizontal_align" : "center",
				},
				{
					"name" : "character_level_value",
					"type" : "text",

					"x" : 180 + 130/2,
					"y" : 6,

					"text" : "120",
					"fontname" : "Tahoma:16",
					"color" : apollo_interface.COLOR_HOVER,

					"text_horizontal_align" : "center",
				},
			),
		},

		{
			"name" : "character_hth",
			"type" : "text",

			"x" : (SCREEN_WIDTH/2) - 222,
			"y" : (SCREEN_HEIGHT/2) - 40,

			"fontname" : "Tahoma:12",
			"text" : apollo_interface.VIT,
			"color" : apollo_interface.COLOR_HOVER,

			"text_horizontal_align" : "right",

			"children" :
			(
				{
					"name" : "gauge_back1",
					"type" : "expanded_image",

					"x" : 0,
					"y" : 2,

					"image" : "%s/costume/gauge/gauge_empty.png" % apollo_interface.PATCH_COMMON,
				},
				{
					"name" : "gauge_hth",
					"type" : "expanded_image",

					"x" : -5,
					"y" : 2.3,

					"image" : "%s/costume/gauge/gauge_red.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
		{
			"name" : "character_int",
			"type" : "text",
			"x" : (SCREEN_WIDTH/2) - 222,
			"y" : (SCREEN_HEIGHT/2) - 20,

			"fontname" : "Tahoma:12",
			"text" : apollo_interface.INT,
			"color" : apollo_interface.COLOR_HOVER,

			"text_horizontal_align" : "right",

			"children" :
			(
				{
					"name" : "gauge_back1",
					"type" : "expanded_image",

					"x" : 0,
					"y" : 2,

					"image" : "%s/costume/gauge/gauge_empty.png" % apollo_interface.PATCH_COMMON,
				},
				{
					"name" : "gauge_int",
					"type" : "expanded_image",

					"x" : -5,
					"y" : 2.3,

					"image" : "%s/costume/gauge/gauge_pink.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
		{
			"name" : "character_str",
			"type" : "text",
			"x" : (SCREEN_WIDTH/2) - 222,
			"y" : (SCREEN_HEIGHT/2),

			"fontname" : "Tahoma:12",
			"text" : apollo_interface.STR,
			"color" : apollo_interface.COLOR_HOVER,

			"text_horizontal_align" : "right",

			"children" :
			(
				{
					"name" : "gauge_back1",
					"type" : "expanded_image",

					"x" : 0,
					"y" : 2,

					"image" : "%s/costume/gauge/gauge_empty.png" % apollo_interface.PATCH_COMMON,
				},
				{
					"name" : "gauge_str",
					"type" : "expanded_image",

					"x" : -5,
					"y" : 2.3,

					"image" : "%s/costume/gauge/gauge_purple.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
		{
			"name" : "character_dex",
			"type" : "text",
			"x" : (SCREEN_WIDTH/2) - 222,
			"y" : (SCREEN_HEIGHT/2) + 20 ,

			"fontname" : "Tahoma:12",
			"text" : apollo_interface.DEX,
			"color" : apollo_interface.COLOR_HOVER,

			"text_horizontal_align" : "right",

			"children" :
			(
				{
					"name" : "gauge_back1",
					"type" : "expanded_image",

					"x" : 0,
					"y" : 2,

					"image" : "%s/costume/gauge/gauge_empty.png" % apollo_interface.PATCH_COMMON,
				},
				{
					"name" : "gauge_dex",
					"type" : "expanded_image",

					"x" : -5,
					"y" : 2.3,

					"image" : "%s/costume/gauge/gauge_blue.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
		{
			"name" : "start_button",
			"type" : "button",

			"x" : (SCREEN_WIDTH/2) + 220,
			"y" : (SCREEN_HEIGHT/2) - 25,

			"text" : "Start",

			"default_image": "%s/costume/selectcaracter/buttons/btn_option_on.png" % apollo_interface.PATCH_COMMON,
			"over_image": "%s/costume/selectcaracter/buttons/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
			"down_image": "%s/costume/selectcaracter/buttons/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/selectcaracter/buttons/btn_option_disabled.png" % apollo_interface.PATCH_COMMON,

		},
		{
			"name" : "create_button",
			"type" : "button",

			"x" : (SCREEN_WIDTH/2) + 220,
			"y" : (SCREEN_HEIGHT/2) + 55,

			"text" : "Create",

			"default_image": "%s/costume/selectcaracter/buttons/btn_option_on.png" % apollo_interface.PATCH_COMMON,
			"over_image": "%s/costume/selectcaracter/buttons/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
			"down_image": "%s/costume/selectcaracter/buttons/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/selectcaracter/buttons/btn_option_disabled.png" % apollo_interface.PATCH_COMMON,

		},
		{
			"name" : "delete_button",
			"type" : "button",

			"x" : (SCREEN_WIDTH/2) + 220,
			"y" : (SCREEN_HEIGHT/2) + 15,

			# "text_color" : apollo_interface.COLOR_HOVER,

			"text" : "Delete",


			"default_image": "%s/costume/selectcaracter/buttons/btn_option_on.png" % apollo_interface.PATCH_COMMON,
			"over_image": "%s/costume/selectcaracter/buttons/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
			"down_image": "%s/costume/selectcaracter/buttons/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/selectcaracter/buttons/btn_option_disabled.png" % apollo_interface.PATCH_COMMON,

		},
		{
			"name" : "channel_backgr",
			"type" : "image",

			"x" : (SCREEN_WIDTH/2) + 145,
			"y" : (SCREEN_HEIGHT/2) - 105,

			"image" : apollo_interface.PATCH_COMMON+"/costume/selectcaracter/channel_backgr.png",
		},
		## Buttons
		{
			"name" : "left_button",
			"type" : "button",

			"x" : (SCREEN_WIDTH/2) + 175,
			"y" : (SCREEN_HEIGHT/2) - 60,

			"default_image" : "%s/button/titlebar_collapse_01_normal.png" % apollo_interface.PATCH_COMMON,
			"over_image" : "%s/button/titlebar_collapse_02_hover.png" % apollo_interface.PATCH_COMMON,
			"down_image" : "%s/button/titlebar_collapse_03_active.png" % apollo_interface.PATCH_COMMON,
		},
		{
			"name" : "right_button",
			"type" : "button",

			"x" : (SCREEN_WIDTH/2) + 353,
			"y" : (SCREEN_HEIGHT/2) - 60,

			"default_image" : "%s/button/titlebar_expand_01_normal.png" % apollo_interface.PATCH_COMMON,
			"over_image" : "%s/button/titlebar_expand_02_hover.png" % apollo_interface.PATCH_COMMON,
			"down_image" : "%s/button/titlebar_expand_03_active.png" % apollo_interface.PATCH_COMMON,
		},

		{
			"name" : "character_txt1",
			"type" : "text",

			"x" : (SCREEN_WIDTH/2) + 190+17,
			"y" : (SCREEN_HEIGHT/2) - 60,

			"text" : "Charakter Nr.     din  ",
			"fontname" : "Tahoma:14",

			"color" : apollo_interface.COLOR_HOVER,

			"text_horizontal_align" : "left",
		},



		{
			"name" : "character_txt2",
			"type" : "text",

			"x" : (SCREEN_WIDTH/2) + 273+13,
			"y" : (SCREEN_HEIGHT/2) - 60,

			"text" : " X          5",
			"fontname" : "Tahoma:14",

			"r" : 0.6549,
			"g" : 0.0156,
			"b" : 0.0156,

			"text_horizontal_align" : "left",
		},
	),
}
