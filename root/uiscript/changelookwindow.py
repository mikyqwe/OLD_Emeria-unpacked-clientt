import uiScriptLocale

BUTTON_ROOT = "d:/ymir work/ui/public/"

window = {
	"name" : "ChangeLookWindow",
	"x" : 0,
	"y" : 0,
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - 176 - 287 - 10,
	"y" : SCREEN_HEIGHT - 37 - 525,

	"width" : 205,
	"height" : 270,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : 205,
			"height" : 270,
			"children" :
			(
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),
					"x" : 6,
					"y" : 6,
					"width" : 190,
					"color" : "yellow",
					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",
							"x" : 95,
							"y" : 3,
							"text" : "",
							"text_horizontal_align" : "center"
						},
					),
				},
				{
					"name" : "ChangeLook_SlotImg",
					"type" : "image",
					"x" : 9,
					"y" : 35,
					"image" : "d:/ymir work/interface/transmutation/new_transmutationwindow.tga",
					"children" :
					(
						{
							"name" : "ChangeLookSlot",
							"type" : "slot",
					
							"x" : -1,
							"y" : 3,
					
							"width" : 190,
							"height" : 200,
					
							"slot" : (
										{
											"index" : 0,
											"x" : 24,
											"y" : 30,
											"width" : 31,
											"height" : 96
										},
										{
											"index" : 1,
											"x" : 129,
											"y" : 30,
											"width" : 31,
											"height" : 96
										},
							),
						},
					),
				},
				{
					"name" : "Cost",
					"type" : "text",
					"text" : "",
					"text_horizontal_align" : "center",
					"x" : 102,
					"y" : 215,
				},
				{
					"name" : "AcceptButton",
					"type" : "button",
					"x" : 40,
					"y" : 235,
					"text" : uiScriptLocale.OK,
					"default_image" : "d:/ymir work/ui/xlarge_thin_button_01.tga",
					"over_image" : "d:/ymir work/ui/xlarge_thin_button_02.tga",
					"down_image" : "d:/ymir work/ui/xlarge_thin_button_03.tga",
				},
				{
					"name" : "CancelButton",
					"type" : "button",
					"x" : 114,
					"y" : 235,
					"text" : uiScriptLocale.CANCEL,
					"default_image" : "d:/ymir work/ui/xlarge_thin_button_01.tga",
					"over_image" : "d:/ymir work/ui/xlarge_thin_button_02.tga",
					"down_image" : "d:/ymir work/ui/xlarge_thin_button_03.tga",
				},
			),
		},
	),
}