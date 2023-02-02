import uiScriptLocale
import apollo_interface

LOCALE_PATH = uiScriptLocale.LOGIN_PATH
SERVER_BOARD_HEIGHT = 220 + 180
SERVER_LIST_HEIGHT = 171 + 180
LOGIN_PATH = "locale/es/ui/login_nuevo/"
INTERFACE_PATH = "locale/es/ui/"

window = {
	"name" : "LoginWindow",
	"sytle" : ("movable",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(


		## Board
		{
			"name" : "bg",
			"type" : "expanded_image",
			"x" : 0,
			"y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image": "%s/background.png" % apollo_interface.PATCH_LOGIN,
		},



		{
			"name" : "accountLog",
			"type" : "expanded_image",
			"x" : (SCREEN_WIDTH + 262+84) / 2,
			"y" : (SCREEN_HEIGHT - 300) / 2 + (50 * (float(SCREEN_HEIGHT) / 768.0)),

			"image": "%s/option_board_3.png" %apollo_interface.PATCH_LOGIN,
			"children" :
			(
				{
					"name": "account_1",
					"type": "text",

					"x": 50,
					"y": 20,

					"color": 0xffb7a06c,
					"text": apollo_interface.SAVE_EMPTY,
				},
				{
					"name": "account_2",
					"type": "text",

					"x": 50,
					"y": 20+38,

					"color": 0xffb7a06c,
					"text": apollo_interface.SAVE_EMPTY,
				},
				{
					"name": "account_3",
					"type": "text",

					"x": 50,
					"y": 20+38*2,

					"color": 0xffb7a06c,
					"text": apollo_interface.SAVE_EMPTY,
				},
				{
					"name": "account_4",
					"type": "text",

					"x": 50,
					"y": 20+38*3,

					"color": 0xffb7a06c,
					"text": apollo_interface.SAVE_EMPTY,
				},
			),
		},

		{
			"name" : "buttonMinimize",
			"type" : "button",

			"x" : (SCREEN_WIDTH + 610+84) / 2,
			"y" : (SCREEN_HEIGHT - 204) / 2 + (50 * (float(SCREEN_HEIGHT) / 768.0)),

			"default_image": "%s/costume/button_savelog/btn_belt_close_01_normal.png" % apollo_interface.PATCH_COMMON,
			"over_image": "%s/costume/button_savelog/btn_belt_close_02_hover.png" % apollo_interface.PATCH_COMMON,
			"down_image": "%s/costume/button_savelog/btn_belt_close_03_active.png" % apollo_interface.PATCH_COMMON,
		},

		## Panel_Login
		{
			"name" : "LoginBoard",
			"type" : "thinboard",

			"x" : (SCREEN_WIDTH - 365) / 2,
			"y" : (SCREEN_HEIGHT - 460) / 2 + (50 * (float(SCREEN_HEIGHT) / 768.0)),

			"width" : 360,
			"height" : 330,

			"children" :
			(
				{
					"name": "Hover",
					"type": "text",

					"x": 155,
					"y": 40,

					"text" : apollo_interface.SERVER_NAME,

					"color": apollo_interface.COLOR_HOVER,

					"children":
					(
						{
							"name": "hoverImg",
							"type": "image",

							"x": -70,
							"y": 15,

							"image": "%s/horizontal_bar/center_inverted.png" % apollo_interface.PATCH_COMMON,
						},
					),
				},
				{
					"name": "Separator_Buttons",
					"type": "image",

					"x": 232,
					"y": 115+5,

					"image": "%s/costume/separator_buttons.png" % apollo_interface.PATCH_COMMON,
				},
				
				{
					
					"name": "id_inputs",
					"type": "image",

					"x": 40,
					"y": 100,

					"image": "%s/costume/input.png" % apollo_interface.PATCH_COMMON,

					"children":
					(
						{
							"name": "Separator_ID",
							"type": "image",

							"x": 20,
							"y": -53+25,

							"image": "%s/costume/separator_input.png" % apollo_interface.PATCH_COMMON,
						},
						{
							"name": "Dialog_ID",
							"type": "text",

							"x": 35,
							"y": -45+25,

							"color" : apollo_interface.COLOR_LOGIN_TEXT,

							"text" : apollo_interface.ID_LOGIN,
						},

					),
				},
				{
					"name": "pwd_inputs",
					"type": "image",

					"x": 40,
					"y": 133+20,

					"image": "%s/costume/input.png" % apollo_interface.PATCH_COMMON,

					"children":
					(
						{
							"name": "Separator_PW",
							"type": "image",

							"x": 20,
							"y": -53+25,

							"image": "%s/costume/separator_input.png" % apollo_interface.PATCH_COMMON,
						},
						{
							"name": "Dialog_PW",
							"type": "text",

							"x": 35,
							"y": -45+25,

							"color" : apollo_interface.COLOR_LOGIN_TEXT,

							"text" : apollo_interface.PW_LOGIN,
						},

					),
				},
				{
					"name" : "LoginButton",
					"type" : "button",

					"x": 100,
					"y": -20-10,

					"horizontal_align": "center",
					"vertical_align": "center",

					"text" : "Anmelden",
					"text_color" : apollo_interface.COLOR_HOVER,

					"default_image": "%s/costume/btn_option_on.png" % apollo_interface.PATCH_COMMON,
					"over_image": "%s/costume/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
					"down_image": "%s/costume/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
				},
				{
					"name" : "LoginExitButton",
					"type" : "button",

					"x": 100,
					"y": 10-10,

					"horizontal_align": "center",
					"vertical_align": "center",

					"text" : "Abbrechen",
					"text_color" : apollo_interface.COLOR_HOVER,

					"default_image": "%s/costume/btn_option_on.png" % apollo_interface.PATCH_COMMON,
					"over_image": "%s/costume/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
					"down_image": "%s/costume/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
				},


				{
					"name" : "WithoutAccount",
					"type" : "text",

					"x" : 40,
					"y" : 110,
					"vertical_align" : "center",
					"text_vertical_align" : "center",

					"color" : 0xFFa07970,

					"text" : apollo_interface.LOGIN_NOACCOUNT,
				},
				{
					"name": "hoverInvert",
					"type": "image",

					"x": 75,
					"y": 240,

					"image": "%s/horizontal_bar/center.png" % apollo_interface.PATCH_COMMON,
				},

				{
					"name" : "buttonExpand",
					"type" : "button",

					"x" : 354,
					"y" : 125,

					"default_image": "%s/costume/button_savelog/btn_belt_open_01_normal.png" % apollo_interface.PATCH_COMMON,
					"over_image": "%s/costume/button_savelog/btn_belt_open_02_hover.png" % apollo_interface.PATCH_COMMON,
					"down_image": "%s/costume/button_savelog/btn_belt_open_03_active.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
	),
}
