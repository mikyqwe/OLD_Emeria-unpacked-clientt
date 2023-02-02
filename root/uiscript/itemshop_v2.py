import uiScriptLocale

BOARDWIDTH = 750
BOARDHEIGHT = 500

MAINFOLDER = "locale/de/ui/"

window = {
	"name" : "Itemshop",

	"x" : SCREEN_WIDTH/2-BOARDWIDTH/2,
	"y" : SCREEN_HEIGHT /2-BOARDHEIGHT/2,

	"style" : ("movable", "float",),

	"width" : BOARDWIDTH,
	"height" : BOARDHEIGHT,

	"children" :
	(
		{
			"name" : "Board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARDWIDTH,
			"height" : BOARDHEIGHT,

			"children" :
			(
				{
					"name": "Menue",
					
					"x" : 0,
					"y" : 0,
					
					"width" : BOARDWIDTH,
					"height" : 200,

					"style" : ("movable", "attach",),
					
					"children": 
					(
						## Buttons
						{
							"name" : "btn_startpage", 
							"type" : "button",
							"text" : "Startseite",
							"x" : 27,
							"y" : 64,
							"default_image" : MAINFOLDER+"itemshop/btn_first_page_norm.sub",
							"over_image" : MAINFOLDER+"itemshop/btn_first_page_hover.sub",
							"down_image" : MAINFOLDER+"itemshop/btn_first_page_press.sub",
						},
						{
							"name" : "btn_itemshop", 
							"type" : "button",
							"text" : "Itemshop",
							"x" : 193,
							"y" : 64,
							"default_image" : MAINFOLDER+"itemshop/btn_other_page_norm.sub",
							"over_image" : MAINFOLDER+"itemshop/btn_other_page_hover.sub",
							"down_image" : MAINFOLDER+"itemshop/btn_other_page_press.sub",
						},
						{
							"name" : "btn_voteshop", 
							"type" : "button",
							"text" : "Voteshop",
							"x" : 360,
							"y" : 64,
							"default_image" : MAINFOLDER+"itemshop/btn_other_page_norm.sub",
							"over_image" : MAINFOLDER+"itemshop/btn_other_page_hover.sub",
							"down_image" : MAINFOLDER+"itemshop/btn_other_page_press.sub",
						},
						{
							"name" : "btn_achievementshop", 
							"type" : "button",
							"text" : "Achievementshop",
							"x" : 527,
							"y" : 64,
							"default_image" : MAINFOLDER+"itemshop/btn_other_page_norm.sub",
							"over_image" : MAINFOLDER+"itemshop/btn_other_page_hover.sub",
							"down_image" : MAINFOLDER+"itemshop/btn_other_page_press.sub",
						},
						## Close button
						# {
							# "name" : "btn_close", 
							# "type" : "button",
							# "x" : 714,
							# "y" : 5,
							# "default_image" : MAINFOLDER+"itemshop/btn_close_norm.sub",
							# "over_image" : MAINFOLDER+"itemshop/btn_close_hover.sub",
							# "down_image" : MAINFOLDER+"itemshop/btn_close_press.sub",
						# },
						## Question button
						# {
							# "name" : "btn_question", 
							# "type" : "button",
							# "x" : 672,
							# "y" : 5,
							# "default_image" : MAINFOLDER+"itemshop/btn_question_norm.sub",
							# "over_image" : MAINFOLDER+"itemshop/btn_question_hover.sub",
							# "down_image" : MAINFOLDER+"itemshop/btn_question_press.sub",
						# },
						
						## Collect coins
						#{
						#	"name" : "sb_c_coins",
						#	"type" : "image",
						#	"x" : 547,
						#	"y" : 25,
						#	"image" : "itemshop/black_large_slotbar.sub",
							
						#	"children" :
						#	(
						#		{
						#			"name" : "tx_c_coins",
						#			"type" : "text",
						#			"text" : "100 C-Punkte",
						#			"x" : 2,
						#			"y" : 2,
						#		},
						#	),
						#},
						## Itemshop coins
						{
							"name" : "sb_i_coins",
							"type" : "image",
							"x" : 80,
							"y" : 35,
							"image" : MAINFOLDER+"itemshop/black_large_slotbar.sub",
							
							"children" :
							(
								{
									"name" : "tx_i_coins",
									"type" : "text",
									"text" : "100.000 I-Coins",
									"x" : 0,
									"y" : 3,
									"horizontal_align" : "center",
									"text_horizontal_align" : "center",
								},
							),
						},
						## Voteshop coins
						{
							"name" : "sb_v_coins",
							"type" : "image",
							"x" : 270,
							"y" : 35,
							"image" : MAINFOLDER+"itemshop/black_large_slotbar.sub",
							
							"children" :
							(
								{
									"name" : "tx_v_coins",
									"type" : "text",
									"text" : "100 V-Coins",
									"x" : 0,
									"y" : 3,
									"horizontal_align" : "center",
									"text_horizontal_align" : "center",
								},
							),
						},
						## Achievementshop coins
						{
							"name" : "sb_a_coins",
							"type" : "image",
							"x" : 460,
							"y" : 35,
							"image" : MAINFOLDER+"itemshop/black_large_slotbar.sub",
							
							"children" :
							(
								{
									"name" : "tx_a_coins",
									"type" : "text",
									"text" : "100 A-Coins",
									"x" : 0,
									"y" : 3,
									"horizontal_align" : "center",
									"text_horizontal_align" : "center",
								},
							),
						},
					),
				},
				
				{
					"name": "Startpage",
					
					"x" : 0,
					"y" : 100,
					
					"width" : BOARDWIDTH,
					"height" : 500,
					"style" : ("movable", "attach",),
					
					"children": 
					(
						## BANNER 
						{
							"name": "Banner",
					
							"x" : 0,
							"y" : 0,
					
							"width" : BOARDWIDTH,
							"height" : 250,

							"style" : ("movable", "attach",),

							"children": 
							(
								{
									"name" : "image_banner_background",
									"type" : "image",
									"style" : ("movable", "attach",),
									"x" : 30,
									"y" : 5,
									"image" : MAINFOLDER+"itemshop/news_box.sub",
								},
								{
									"name" : "image_banner",
									"type" : "image",
									"style" : ("movable", "attach",),
									"x" : 33,
									"y" : 8,
									"image" : MAINFOLDER+"itemshop/banner/banner_0.jpg",
								},
								{
									"name" : "image_fade_banner",
									"type" : "image",
									"style" : ("movable", "attach",),
									"x" : 33,
									"y" : 8,
									"image" : MAINFOLDER+"itemshop/banner/banner_0.jpg",
								},
								## Banner page one
								{
									"name" : "btn_banner_0", 
									"type" : "toggle_button",
									"x" : 525+15,
									"y" : 230,
									"default_image" :  MAINFOLDER+"itemshop/dot_norm.sub",
									"over_image" : MAINFOLDER+"itemshop/dot_hover.sub",
									"down_image" :  MAINFOLDER+"itemshop/dot_press.sub",
								},
								## Banner page two
								{
									"name" : "btn_banner_1", 
									"type" : "toggle_button",
									"x" : 545+15,
									"y" : 230,
									"default_image" :  MAINFOLDER+"itemshop/dot_norm.sub",
									"over_image" : MAINFOLDER+"itemshop/dot_hover.sub",
									"down_image" :  MAINFOLDER+"itemshop/dot_press.sub",
								},
							),
						},
						## HOT OFFERS
						{
							"name": "HotOffers",
					
							"x" : 596,
							"y" : 5,
					
							"width" : BOARDWIDTH,
							"height" : 320,
							"style" : ("movable", "attach",),
							"children": 
							(
								{
									"name" : "image_hotOffers_background",
									"type" : "image",
									"style" : ("movable", "attach",),
									"x" : 0,
									"y" : 0,
									"image" : MAINFOLDER+"itemshop/hot_offer_box.sub",

									"children": 
									(
										{
											"name" : "image_hotOffers_text",
											"type" : "image",
											"style" : ("movable", "attach",),
											"x" : 0,
											"y" : 0,
											"image" : MAINFOLDER+"itemshop/red_medium_slotbar.sub",
											"children": 
											(
												{
													"name" : "tx_hotOffers",
													"type" : "text",
													"text" : "HEIßE ANGEBOTE",
													"x" : 2,
													"y" : 2,
												},
											),
										},
										{
											"name" : "btn_hotOffers_up", 
											"type" : "button",
											"x" : 54,
											"y" : 24,
											"default_image" : MAINFOLDER+"itemshop/arrow_up_norm.sub",
											"over_image" : MAINFOLDER+"itemshop/arrow_up_hover.sub",
											"down_image" : MAINFOLDER+"itemshop/arrow_up_press.sub",
										},
										{
											"name" : "btn_hotOffers_down", 
											"type" : "button",
											"x" : 54,
											"y" : 276,
											"default_image" : MAINFOLDER+"itemshop/arrow_down_norm.sub",
											"over_image" : MAINFOLDER+"itemshop/arrow_down_hover.sub",
											"down_image" : MAINFOLDER+"itemshop/arrow_down_press.sub",
										},
									),
								},
							),
						},
						## MOST BOUGHT
						{
							"name": "MostBought",
					
							"x" : 30,
							"y" : 260,
					
							"width" : 559,
							"height" : 114,
							"style" : ("movable", "attach",),
							"children": 
							(
								{
									"name" : "image_mostBought_background",
									"type" : "image",
									"style" : ("movable", "attach",),
									"x" : 0,
									"y" : 0,
									"image" : MAINFOLDER+"itemshop/most_bought_box.sub",
									"children": 
									(
										{
											"name" : "image_mostBought_text",
											"type" : "image",
											"style" : ("movable", "attach",),
											"x" : 0,
											"y" : 0,
											"image" : MAINFOLDER+"itemshop/red_large_slotbar.sub",
											"children": 
											(
												{
													"name" : "tx_mostBought",
													"type" : "text",
													"text" : "MEIST GEKAUFT",
													"x" : 2,
													"y" : 2,
												},
											),
										},
										{
											"name" : "btn_mostBought_left", 
											"type" : "button",
											"x" : 11,
											"y" : 48,
											"default_image" : MAINFOLDER+"itemshop/arrow_left_norm.sub",
											"over_image" : MAINFOLDER+"itemshop/arrow_left_hover.sub",
											"down_image" : MAINFOLDER+"itemshop/arrow_left_press.sub",
										},
										{
											"name" : "btn_mostBought_right", 
											"type" : "button",
											"x" : 510,
											"y" : 48,
											"default_image" : MAINFOLDER+"itemshop/arrow_right_norm.sub",
											"over_image" : MAINFOLDER+"itemshop/arrow_right_hover.sub",
											"down_image" : MAINFOLDER+"itemshop/arrow_right_press.sub",
										},
									),
								},
							),
						},
						## Coins buy button
						{
							"name" : "btn_buy_coins", 
							"type" : "button",
							"text" : "COINS KAUFEN",

							"x" : 592,
							"y" : 336,

							"default_image" : MAINFOLDER+"itemshop/btn_coins_buy_norm.sub",
							"over_image" : MAINFOLDER+"itemshop/btn_coins_buy_hover.sub",
							"down_image" : MAINFOLDER+"itemshop/btn_coins_buy_press.sub",
						},
						## Vote button
						{
							"name" : "btn_vote", 
							"type" : "button",
							"text" : "VOTEN",

							"x" : 592,
							"y" : 336+25,

							"default_image" : MAINFOLDER+"itemshop/btn_coins_buy_norm.sub",
							"over_image" : MAINFOLDER+"itemshop/btn_coins_buy_hover.sub",
							"down_image" : MAINFOLDER+"itemshop/btn_coins_buy_press.sub",
						},
					),
				},
				{
					"name": "Itemshop",
					
					"x" : 0,
					"y" : 100,
					
					"width" : BOARDWIDTH,
					"height" : 500,
					"style" : ("movable", "attach",),
					
					"children": 
					 (
						 ## On Sale
						{
							"name": "IsOnSale",
					
							"x" : 210,
							"y" : 4,
					
							"width" : 513,
							"height" : 376,
							"style" : ("movable", "attach",),
							"children": 
							(
								{
									"name" : "image_IsOnSale_background",
									"type" : "image",
									"x" : 0,
									"y" : 0,
									"image" :  MAINFOLDER+"itemshop/on_sale_box.sub",
									"children": 
									(
										{
											"name" : "btn_IsOnSale_left", 
											"type" : "button",
											"x" : 7,
											"y" : 170,
											"default_image" : MAINFOLDER+"itemshop/arrow_left_norm.sub",
											"over_image" : MAINFOLDER+"itemshop/arrow_left_hover.sub",
											"down_image" : MAINFOLDER+"itemshop/arrow_left_press.sub",
										},
										{
											"name" : "btn_IsOnSale_right", 
											"type" : "button",
											"x" : 469,
											"y" : 170,
											"default_image" : MAINFOLDER+"itemshop/arrow_right_norm.sub",
											"over_image" : MAINFOLDER+"itemshop/arrow_right_hover.sub",
											"down_image" : MAINFOLDER+"itemshop/arrow_right_press.sub",
										},
									),
								},
							),
						},
						{
							"name": "IsCategory",
					
							"x" : 29,
							"y" : 6,
					
							"width" : 164,
							"height" : 373,
							"style" : ("movable", "attach",),
							"children": 
							(
								## Category
								{
									"name" : "image_IsCategory_background",
									"type" : "image",
									"x" : 0,
									"y" : 0,
									"image" :  MAINFOLDER+"itemshop/category_box.sub",
								},
								{
									"name" : "btn_IsCategory_up", 
									"type" : "button",
									"x" : 68,
									"y" : 4,
									"default_image" : MAINFOLDER+"itemshop/arrow_up_norm.sub",
									"over_image" : MAINFOLDER+"itemshop/arrow_up_hover.sub",
									"down_image" : MAINFOLDER+"itemshop/arrow_up_press.sub",
								},
								{
									"name" : "btn_IsCategory_down", 
									"type" : "button",
									"x" : 68,
									"y" : 335,
									"default_image" : MAINFOLDER+"itemshop/arrow_down_norm.sub",
									"over_image" : MAINFOLDER+"itemshop/arrow_down_hover.sub",
									"down_image" : MAINFOLDER+"itemshop/arrow_down_press.sub",
								},
							),
						},
						{
							"name" : "tx_IsOnSale_pageNr",
							"type" : "text",
							"text" : "0 / 1",
							"x" : 690,
							"y" : 355,
						},
					 ),
				 },
					{
					"name": "Voteshop",
					
					"x" : 0,
					"y" : 100,
					
					"width" : BOARDWIDTH,
					"height" : 500,
					"style" : ("movable", "attach",),
					
					"children": 
					 (
						 ## On Sale
						{
							"name": "VsOnSale",
					
							"x" : 210,
							"y" : 4,
					
							"width" : 513,
							"height" : 376,
							"style" : ("movable", "attach",),
							"children": 
							(
								 {
									"name" : "image_VsOnSale_background",
									"type" : "image",
									"x" : 0,
									"y" : 0,
									"image" :  MAINFOLDER+"itemshop/on_sale_box.sub",
									"children": 
									(
										{
											"name" : "btn_VsOnSale_left", 
											"type" : "button",
											"x" : 7,
											"y" : 170,
											"default_image" : MAINFOLDER+"itemshop/arrow_left_norm.sub",
											"over_image" : MAINFOLDER+"itemshop/arrow_left_hover.sub",
											"down_image" : MAINFOLDER+"itemshop/arrow_left_press.sub",
										},
										{
											"name" : "btn_VsOnSale_right", 
											"type" : "button",
											"x" : 469,
											"y" : 170,
											"default_image" : MAINFOLDER+"itemshop/arrow_right_norm.sub",
											"over_image" : MAINFOLDER+"itemshop/arrow_right_hover.sub",
											"down_image" : MAINFOLDER+"itemshop/arrow_right_press.sub",
										},
									),
								},
							),
						},
						{
							"name": "VsCategory",
					
							"x" : 29,
							"y" : 6,
					
							"width" : 164,
							"height" : 373,
							"style" : ("movable", "attach",),
							"children": 
							(
								## Category
								{
									"name" : "image_VsCategory_background",
									"type" : "image",
									"x" : 0,
									"y" : 0,
									"image" :  MAINFOLDER+"itemshop/category_box.sub",
								},
								{
									"name" : "btn_VsCategory_up", 
									"type" : "button",
									"x" : 68,
									"y" : 4,
									"default_image" : MAINFOLDER+"itemshop/arrow_up_norm.sub",
									"over_image" : MAINFOLDER+"itemshop/arrow_up_hover.sub",
									"down_image" : MAINFOLDER+"itemshop/arrow_up_press.sub",
								},
								{
									"name" : "btn_VsCategory_down", 
									"type" : "button",
									"x" : 68,
									"y" : 335,
									"default_image" : MAINFOLDER+"itemshop/arrow_down_norm.sub",
									"over_image" : MAINFOLDER+"itemshop/arrow_down_hover.sub",
									"down_image" : MAINFOLDER+"itemshop/arrow_down_press.sub",
								},
							),
						},
						{
							"name" : "tx_VsOnSale_pageNr",
							"type" : "text",
							"text" : "0 / 1",
							"x" : 690,
							"y" : 355,
						},
					 ),
				 },
				 
				 {
					"name": "Achievementshop",
					
					"x" : 0,
					"y" : 100,
					
					"width" : BOARDWIDTH,
					"height" : 500,
					"style" : ("movable", "attach",),
					
					"children": 
					 (
						 ## On Sale
						{
							"name": "AsOnSale",
					
							"x" : 210,
							"y" : 4,
					
							"width" : 513,
							"height" : 376,
							"style" : ("movable", "attach",),
							"children": 
							(
								{
									"name" : "image_AsOnSale_background",
									"type" : "image",
									"x" : 0,
									"y" : 0,
									"image" :  MAINFOLDER+"itemshop/on_sale_box.sub",
									"children": 
									(
										{
											"name" : "btn_AsOnSale_left", 
											"type" : "button",
											"x" : 7,
											"y" : 170,
											"default_image" : MAINFOLDER+"itemshop/arrow_left_norm.sub",
											"over_image" : MAINFOLDER+"itemshop/arrow_left_hover.sub",
											"down_image" : MAINFOLDER+"itemshop/arrow_left_press.sub",
										},
										{
											"name" : "btn_AsOnSale_right", 
											"type" : "button",
											"x" : 469,
											"y" : 170,
											"default_image" : MAINFOLDER+"itemshop/arrow_right_norm.sub",
											"over_image" : MAINFOLDER+"itemshop/arrow_right_hover.sub",
											"down_image" : MAINFOLDER+"itemshop/arrow_right_press.sub",
										},
									),
								},
							),
						},
						{
							"name": "AsCategory",
					
							"x" : 29,
							"y" : 6,
					
							"width" : 164,
							"height" : 373,
							"style" : ("movable", "attach",),
							"children": 
							(
								## Category
								{
									"name" : "image_AsCategory_background",
									"type" : "image",
									"x" : 0,
									"y" : 0,
									"image" :  MAINFOLDER+"itemshop/category_box.sub",
								},
								{
									"name" : "btn_AsCategory_up", 
									"type" : "button",
									"x" : 68,
									"y" : 4,
									"default_image" : MAINFOLDER+"itemshop/arrow_up_norm.sub",
									"over_image" : MAINFOLDER+"itemshop/arrow_up_hover.sub",
									"down_image" : MAINFOLDER+"itemshop/arrow_up_press.sub",
								},
								{
									"name" : "btn_AsCategory_down", 
									"type" : "button",
									"x" : 68,
									"y" : 335,
									"default_image" : MAINFOLDER+"itemshop/arrow_down_norm.sub",
									"over_image" : MAINFOLDER+"itemshop/arrow_down_hover.sub",
									"down_image" : MAINFOLDER+"itemshop/arrow_down_press.sub",
								},
							),
						},
						{
							"name" : "tx_AsOnSale_pageNr",
							"type" : "text",
							"text" : "0 / 1",
							"x" : 690,
							"y" : 355,
						},
					 ),
				 },
				 {
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : BOARDWIDTH-15,

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":3, "text":'Itemshop',"horizontal_align" : "center", "text_horizontal_align":"center",},
					),
				},
			),
		},
	),
}