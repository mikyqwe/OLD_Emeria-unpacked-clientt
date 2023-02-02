import uiScriptLocale

MAINBOARD_WIDTH = 402
MAINBOARD_HEIGHT = 320
MAINBOARD_X = (SCREEN_WIDTH/2) - (MAINBOARD_WIDTH/2)
MAINBOARD_Y = (SCREEN_HEIGHT/2) - (MAINBOARD_HEIGHT/2)

LEFTBOARD_WIDTH = 174
LEFTBOARD_HEIGHT = 269
LEFTBOARD_X = 13
LEFTBOARD_Y = 36

RIGHTBOARD_WIDTH = 196
RIGHTBOARD_HEIGHT = 269
RIGHTBOARD_X = 192
RIGHTBOARD_Y = 36

window = {
	"name" : "MyShopDecoWindow",
	"style" : ("movable", "float",),
	
	"x" : MAINBOARD_X,
	"y" : MAINBOARD_Y,	

	"width" : MAINBOARD_WIDTH,
	"height" : MAINBOARD_HEIGHT,
	
	"children" :
	(
		## MainBoard
		{
			"name" : "MyShopDecoBoard",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : MAINBOARD_WIDTH,
			"height" : MAINBOARD_HEIGHT,
			
			"children" :
			(
				## Title Bar
				{
					"name" : "MyShopTitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6, "y" : 7, "width" : MAINBOARD_WIDTH - 13,
					
					"children" :
					(
						{ "name" : "TitleName", "type" : "text", "x" : 0, "y" : -11, "text": "Shop Decorations", "all_align":"center" },
					),
				},
				
				
				
				## Right Board
				{
					"name" : "RightBoard",
					"type" : "thinboard_circle",
					"x" : RIGHTBOARD_X, "y" : RIGHTBOARD_Y, "width" : RIGHTBOARD_WIDTH, "height" : RIGHTBOARD_HEIGHT,
					
					"children" : 
					(
						## Title Bar (Default �ber den Render Target)
						{
							"name" : "ModelView",
							"type" : "image",
							
							"x" : 195 - RIGHTBOARD_X, "y" : 34 - RIGHTBOARD_Y,
							"image" : "d:/ymir work/offline_shop_deco_new/button_over_rendertarget.tga",
							
							"children" :
							(
								{ "name" : "ModelName", "type" : "text", "x" : 0, "y" : 0, "text" : "123", "all_align":"center" },
							),
						},
										
						{
							"name" : "RenderTarget",
							"type" : "render_target",
									
							"x" : 195 - RIGHTBOARD_X,
							"y" : 62 - RIGHTBOARD_Y,
									
							"width" : 190,
							"height" : 210, #306
									
							"index" : 1,
						},

						## Button Cancel
						{
							"name" : "CancelButton",
							"type" : "button",

							"x" : 201 - RIGHTBOARD_X,
							"y" : 278 - RIGHTBOARD_Y,

							"text" : "Close",
							"text_height" : 6,

							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
						},

						## Button Complete
						{
							"name" : "CompleteButton",
							"type" : "button",

							"x" : 293 - RIGHTBOARD_X,
							"y" : 278 - RIGHTBOARD_Y,

							"text" : "Ok",
							"text_height" : 6,

							"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
							"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
							"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
						},
					),
				}, ## Right Board End
			),
		}, ## MainBoard End
	),
}