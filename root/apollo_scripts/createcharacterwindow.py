import uiScriptLocale
import apollo_interface
ROOT_PATH = "d:/ymir work/ui/public/"
LOCALE_PATH = "locale/de/ui/select/"
BOARD_X = SCREEN_WIDTH * (65) / 800
BOARD_Y = SCREEN_HEIGHT * (215) / 600

PLUS_BUTTON_WIDTH = 20
TEMPORARY_HEIGHT = 24 + 5

window = {
	"name" : "CreateCharacterWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "BackGround",
			"type" : "expanded_image",
			"x" : 0,
			"y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image": "%s/background.png" %apollo_interface.PATCH_LOGIN,
		},
		{
			"name" : "BackGround_infoChar",
			"type" : "expanded_image",

			"x" : (SCREEN_WIDTH/2)-270-145,
			"y" : (SCREEN_HEIGHT/2)- 140,

			"image": apollo_interface.APOLLO_PATCH + "char_create/shadow_chen.png",
		},
		{
			"name" : "BackGround_button_exi",
			"type" : "expanded_image",

			"x" : (SCREEN_WIDTH/2)-270-137,
			"y" : (SCREEN_HEIGHT/2)+ 85,

			"image": apollo_interface.APOLLO_PATCH + "char_create/gold_chen.png",
		},
		{
			"name" : "BackGround_button_gender",
			"type" : "expanded_image",

			"x" : (SCREEN_WIDTH/2)+145,
			"y" : (SCREEN_HEIGHT/2)+27,

			"image": apollo_interface.APOLLO_PATCH + "char_create/gold_chen.png",
		},
		{
			"name" : "BackGround_button_shape",
			"type" : "expanded_image",

			"x" : (SCREEN_WIDTH/2)+145,
			"y" : (SCREEN_HEIGHT/2)+127,

			"image": apollo_interface.APOLLO_PATCH + "char_create/gold_chen.png",
		},
		{
			"name" : "BackGround_button_race",
			"type" : "expanded_image",

			"x" : (SCREEN_WIDTH/2)+145+10,
			"y" : (SCREEN_HEIGHT/2) - 260,

			"image": apollo_interface.APOLLO_PATCH + "char_create/big_desc.png",
		},
		{
			"name" : "war_button",
			"type" : "button",

			"x" : (SCREEN_WIDTH/2)+175,
			"y" : (SCREEN_HEIGHT/2)-240,

			"text" : "",

			"default_image" : "%s/costume/createcaracter/char_change_normal.png" % apollo_interface.PATCH_COMMON,
			"over_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			"down_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			"children" :
			(
				{
					"name" : "war_text",
					"type" : "text",

					"x" : 60,
					"y" : 12,


					"fontname" : "Tahoma Bold:16",
					"color" : apollo_interface.COLOR_NORMAL,
					"text" : apollo_interface.RACE_WAR,
				},
				{
					"name" : "ico",
					"type" : "image",

					"x" : 152,
					"y" : 8,

					"image" : "%s/costume/createcaracter/warrior_icons.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
		{
			"name" : "ninja_button",
			"type" : "button",

			"x" : (SCREEN_WIDTH/2)+175,
			"y" : (SCREEN_HEIGHT/2)-240+46,

			"text" : "",

			"default_image" : "%s/costume/createcaracter/char_change_normal.png" % apollo_interface.PATCH_COMMON,
			"over_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			"down_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			"children" :
			(
				{
					"name" : "ninja_text",
					"type" : "text",

					"x" : 60,
					"y" : 12,


					"fontname" : "Tahoma Bold:16",
					"color" : apollo_interface.COLOR_NORMAL,
					"text" : apollo_interface.RACE_NINJA,
				},
				{
					"name" : "ico",
					"type" : "image",

					"x" : 152,
					"y" : 8,

					"image" : "%s/costume/createcaracter/assassin_icons.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
		{
			"name" : "sura_button",
			"type" : "button",

			"x" : (SCREEN_WIDTH/2)+175,
			"y" : (SCREEN_HEIGHT/2)-240+46+46,

			"text" : "",

			"default_image" : "%s/costume/createcaracter/char_change_normal.png" % apollo_interface.PATCH_COMMON,
			"over_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			"down_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			"children" :
			(
				{
					"name" : "sura_text",
					"type" : "text",

					"x" : 60,
					"y" : 12,


					"fontname" : "Tahoma Bold:16",
					"color" : apollo_interface.COLOR_NORMAL,
					"text" : apollo_interface.RACE_SURA,
				},
				{
					"name" : "ico",
					"type" : "image",

					"x" : 152,
					"y" : 8,

					"image" : "%s/costume/createcaracter/sura_icons.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
		{
			"name" : "shaman_button",
			"type" : "button",

			"x" : (SCREEN_WIDTH/2)+175,
			"y" : (SCREEN_HEIGHT/2)-240+46+46+46,

			"text" : "",

			"default_image" : "%s/costume/createcaracter/char_change_normal.png" % apollo_interface.PATCH_COMMON,
			"over_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			"down_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			"children" :
			(
				{
					"name" : "shaman_text",
					"type" : "text",

					"x" : 60,
					"y" : 12,


					"fontname" : "Tahoma Bold:16",
					"color" : apollo_interface.COLOR_NORMAL,
					"text" : apollo_interface.RACE_SHAMAN,
				},
				{
					"name" : "ico",
					"type" : "image",

					"x" : 152,
					"y" : 8,

					"image" : "%s/costume/createcaracter/schaman_icons.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
		# {
			# "name" : "wolf_button",
			# "type" : "button",

			# "x" : (SCREEN_WIDTH/2)+175,
			# "y" : (SCREEN_HEIGHT/2)-240+46+46+46+46,

			# "text" : "",

			# "default_image" : "%s/costume/createcaracter/char_change_normal.png" % apollo_interface.PATCH_COMMON,
			# "over_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			# "down_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			# "disable_image" : "%s/costume/createcaracter/char_change_active.png" % apollo_interface.PATCH_COMMON,
			# "children" :
			# (
				# {
					# "name" : "wolf_text",
					# "type" : "text",

					# "x" : 60,
					# "y" : 12,


					# "fontname" : "Tahoma Bold:16",
					# "color" : apollo_interface.COLOR_NORMAL,
					# "text" : apollo_interface.RACE_WOLF,
				# },
				# {
					# "name" : "ico",
					# "type" : "image",

					# "x" : 152,
					# "y" : 8,

					# "image" : "%s/costume/createcaracter/wolfman_icons.png" % apollo_interface.PATCH_COMMON,
				# },
			# ),
		# },
		{
			"name" : "character_name",
			"type" : "text",

			"x" : (SCREEN_WIDTH/2) - 350,
			"y" : (SCREEN_HEIGHT/2) - 255,

			"text" : "",

			"children" :
			(
				{
					"name" : "character_name_img",
					"type" : "text",

					"x" : 3,
					"y" : -2,

					"text" : apollo_interface.NAME,
					"fontname" : "Tahoma Bold:16.5",
					"color" : 0xffffd286,
					"text_horizontal_align" : "left",
				},
				{
					"name" : "character_name_value",
					"type" : "editline",

					"x" : 43+10,
					"y" : 0,

					"input_limit" : 12,

					"width" : 90,
					"height" : 20,
					"color" : 0xffffd286,
					"fontname" : "Tahoma Bold:14",
				},
			),
		},

		{
			"name" : "selectgendertxt",
			"type" : "text",

			"x" : (SCREEN_WIDTH/2)+175 +55,
			"y" : (SCREEN_HEIGHT/2)+10,

			"color" : apollo_interface.COLOR_HOVER,
			"fontname" : "Tahoma Bold:16",

			"text" : apollo_interface.GENDER,
		},
		{
			"name" : "selectclass",
			"type" : "text",

			"x" : (SCREEN_WIDTH/2)+175 + 64,
			"y" : (SCREEN_HEIGHT/2)-280,

			"color" : apollo_interface.COLOR_HOVER,
			"fontname" : "Tahoma Bold:16",

			"text" : apollo_interface.RACE,
		},
		{
			"name" : "selectshapetxt",
			"type" : "text",

			"x" : (SCREEN_WIDTH/2)+175 + 47,
			"y" : (SCREEN_HEIGHT/2)+102 + 8,

			"color" : apollo_interface.COLOR_HOVER,
			"fontname" : "Tahoma Bold:16",

			"text" : apollo_interface.SHAPE,
		},
		{
			"name" : "gender_button_01",
			"type" : "radio_button",

			"x" : (SCREEN_WIDTH/2)+165,
			"y" : (SCREEN_HEIGHT/2)+50,

			"default_image" : "%s/costume/selectcaracter/buttons/btn_option_on.png" % apollo_interface.PATCH_COMMON,
			"over_image" : "%s/costume/selectcaracter/buttons/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
			"down_image" : "%s/costume/selectcaracter/buttons/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/selectcaracter/buttons/btn_option_disabled.png" % apollo_interface.PATCH_COMMON,

			"children" : (
				{
					"name" : "txt",
					"type" : "text",

					"x" : (114/2),
					"y" : 13,

					"text" : apollo_interface.GENDER_MAN,
					"fontname" : "Tahoma Bold:14",

					"color" : apollo_interface.COLOR_HOVER,

					"text_horizontal_align" : "center",
				},
			),
		},
		{
			"name" : "gender_button_02",
			"type" : "radio_button",

			"x" : (SCREEN_WIDTH/2)+165+120,
			"y" : (SCREEN_HEIGHT/2)+50,

			"default_image" : "%s/costume/selectcaracter/buttons/btn_option_on.png" % apollo_interface.PATCH_COMMON,
			"over_image" : "%s/costume/selectcaracter/buttons/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
			"down_image" : "%s/costume/selectcaracter/buttons/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/selectcaracter/buttons/btn_option_disabled.png" % apollo_interface.PATCH_COMMON,

			"children" : (
				{
					"name" : "txt",
					"type" : "text",

					"x" : (114/2),
					"y" : 13,

					"text" : apollo_interface.GENDER_WOMAN,
					"fontname" : "Tahoma Bold:14",

					"color" : apollo_interface.COLOR_HOVER,

					"text_horizontal_align" : "center",
				},
			),
		},
		{
			"name" : "shape_button_01",
			"type" : "radio_button",

			"x" : (SCREEN_WIDTH/2)+165,
			"y" : (SCREEN_HEIGHT/2)+150,

			"default_image" : "%s/costume/selectcaracter/buttons/btn_option_on.png" % apollo_interface.PATCH_COMMON,
			"over_image" : "%s/costume/selectcaracter/buttons/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
			"down_image" : "%s/costume/selectcaracter/buttons/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/selectcaracter/buttons/btn_option_disabled.png" % apollo_interface.PATCH_COMMON,

			"children" : (
				{
					"name" : "txt",
					"type" : "text",

					"x" : (114/2),
					"y" : 13,

					"text" : apollo_interface.SHAPE_1,
					"fontname" : "Tahoma Bold:14",

					"color" : apollo_interface.COLOR_HOVER,

					"text_horizontal_align" : "center",
				},
			),
		},
		{
			"name" : "shape_button_02",
			"type" : "radio_button",

			"x" : (SCREEN_WIDTH/2)+165+120,
			"y" : (SCREEN_HEIGHT/2)+150,

			"default_image" : "%s/costume/selectcaracter/buttons/btn_option_on.png" % apollo_interface.PATCH_COMMON,
			"over_image" : "%s/costume/selectcaracter/buttons/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
			"down_image" : "%s/costume/selectcaracter/buttons/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/selectcaracter/buttons/btn_option_disabled.png" % apollo_interface.PATCH_COMMON,

			"children" : (
				{
					"name" : "txt",
					"type" : "text",

					"x" : (114/2),
					"y" : 13,

					"text" : apollo_interface.SHAPE_2,
					"fontname" : "Tahoma Bold:14",

					"color" : apollo_interface.COLOR_HOVER,

					"text_horizontal_align" : "center",
				},
			),
		},




		{
			"name" : "create_button",
			"type" : "button",

			"x" : (SCREEN_WIDTH/2)-270,
			"y" : (SCREEN_HEIGHT/2)+107,

			"default_image" : "%s/costume/selectcaracter/buttons/btn_option_on.png" % apollo_interface.PATCH_COMMON,
			"over_image" : "%s/costume/selectcaracter/buttons/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
			"down_image" : "%s/costume/selectcaracter/buttons/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/selectcaracter/buttons/btn_option_disabled.png" % apollo_interface.PATCH_COMMON,

			"children" : (
				{
					"name" : "txt",
					"type" : "text",

					"x" : (114/2),
					"y" : 13,

					"text" : apollo_interface.CREATE,
					"fontname" : "Tahoma Bold:14",

					"color" : apollo_interface.COLOR_HOVER,

					"text_horizontal_align" : "center",
				},
			),
		},
		{
			"name" : "cancel_button",
			"type" : "button",

			"x" : (SCREEN_WIDTH/2)-270-120,
			"y" : (SCREEN_HEIGHT/2)+107,

			"default_image" : "%s/costume/selectcaracter/buttons/btn_option_on.png" % apollo_interface.PATCH_COMMON,
			"over_image" : "%s/costume/selectcaracter/buttons/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
			"down_image" : "%s/costume/selectcaracter/buttons/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
			"disable_image" : "%s/costume/selectcaracter/buttons/btn_option_disabled.png" % apollo_interface.PATCH_COMMON,

			"children" : (
				{
					"name" : "txt",
					"type" : "text",

					"x" : (114/2),
					"y" : 13,

					"text" : apollo_interface.CANCEL,
					"fontname" : "Tahoma Bold:14",

					"color" : apollo_interface.COLOR_HOVER,

					"text_horizontal_align" : "center",
				},
			),
		},
		{
			"name" : "pointer",
			"type" : "image",

			"x" : (SCREEN_WIDTH/2) - 300 - 80,
			"y" : (SCREEN_HEIGHT/2) - 200-40,

			"image" : "%s/costume/pointer_fliped.png" % apollo_interface.PATCH_COMMON,
		},

		{
			"name" : "hth",
			"type" : "text",

			"x" : (SCREEN_WIDTH/2) - 300,
			"y" : (SCREEN_HEIGHT/2) - 220,

			"fontname" : "Tahoma Bold:12",
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
					"name" : "hth_gauge",
					"type" : "expanded_image",

					"x" : -5,
					"y" : 2.3,

					"image" : "%s/costume/gauge/gauge_red.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
		{
			"name" : "int",
			"type" : "text",
			"x" : (SCREEN_WIDTH/2) - 300,
			"y" : (SCREEN_HEIGHT/2) - 220+20,

			"fontname" : "Tahoma Bold:12",
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
					"name" : "int_gauge",
					"type" : "expanded_image",

					"x" : -5,
					"y" : 2.3,

					"image" : "%s/costume/gauge/gauge_pink.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
		{
			"name" : "str",
			"type" : "text",
			"x" : (SCREEN_WIDTH/2) - 300,
			"y" : (SCREEN_HEIGHT/2) - 220+20+20,

			"fontname" : "Tahoma Bold:12",
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
					"name" : "str_gauge",
					"type" : "expanded_image",

					"x" : -5,
					"y" : 2.3,

					"image" : "%s/costume/gauge/gauge_purple.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
		{
			"name" : "dex",
			"type" : "text",
			"x" : (SCREEN_WIDTH/2) - 300,
			"y" : (SCREEN_HEIGHT/2) - 220+20+20+20,

			"fontname" : "Tahoma Bold:12",
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
					"name" : "dex_gauge",
					"type" : "expanded_image",

					"x" : -5,
					"y" : 2.3,

					"image" : "%s/costume/gauge/gauge_blue.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
	),
}
