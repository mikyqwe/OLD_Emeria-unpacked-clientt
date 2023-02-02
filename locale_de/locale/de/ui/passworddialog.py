import uiScriptLocale
window = {
	"name" : "PasswordDialog",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 250,
	"height" : 150,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",

			"x" : 0,
			"y" : 0,

			"width" : 250,
			"height" : 200,

			"children" :
			(

				#내용
				{
					"name" : "Desc1",
					"type" : "text",

					"x" : 250/2,
					"y" : 50,

					"text" : uiScriptLocale.PASSWORD_DESC_1,
					"text_horizontal_align":"center"
				},
				#내용2
				{
					"name" : "Desc2",
					"type" : "text",

					"x" : 250/2,
					"y" : 62,

					"text" : uiScriptLocale.PASSWORD_DESC_2,
					"text_horizontal_align":"center"
				},
				## Title
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 12,
 
					"width" : 234,
					"color" : "gray",

					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",

							"x" : 234/2,
							"y" : 7,

							"text" : uiScriptLocale.PASSWORD_TITLE,
							"text_horizontal_align":"center"
						},
					),
				},

				## Password Slot
				{
					"name" : "password_slot",
					"type" : "image",

					"x" : 0,
					"y" : 79,
					"horizontal_align" : "center",

					"image" : "d:/ymir work/ui/public/Parameter_Slot_02.sub",

					"children" :
					(
						{
							"name" : "password_value",
							"type" : "editline",

							"x" : 3,
							"y" : 3,

							"width" : 60,
							"height" : 18,

							"input_limit" : 6,
							"secret_flag" : 1,
						},
					),
				},
				{
					"name" : "Desc3",
					"type" : "text",

					"x" : 250/2,
					"y" : 100,

					"text" : uiScriptLocale.PASSWORD_DESC_3,
					"text_horizontal_align":"center"
				},
				{
					"name" : "Desc4",
					"type" : "text",

					"x" : 250/2,
					"y" : 112,

					"text" : uiScriptLocale.PASSWORD_DESC_4,
					"text_horizontal_align":"center"
				},
				{
					"name" : "Desc5",
					"type" : "text",

					"x" : 250/2,
					"y" : 124,

					"text" : uiScriptLocale.PASSWORD_DESC_5,
					"text_horizontal_align":"center"
				},
				## Button
				{
					"name" : "accept_button",
					"type" : "button",

					"x" : 250/2 - 61 - 5,
					"y" : 140,

					"text" : uiScriptLocale.OK,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
				{
					"name" : "cancel_button",
					"type" : "button",

					"x" : 250/2 + 5,
					"y" : 140,

					"text" : uiScriptLocale.CANCEL,

					"default_image" : "d:/ymir work/ui/public/middle_button_01.sub",
					"over_image" : "d:/ymir work/ui/public/middle_button_02.sub",
					"down_image" : "d:/ymir work/ui/public/middle_button_03.sub",
				},
			),
		},
	),
}
