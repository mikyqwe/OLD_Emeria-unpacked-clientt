import uiScriptLocale
import item
import app
import localeInfo

LOCALE_PATH = "d:/ymir work/ui/privatesearch/"
GOLD_COLOR	= 0xFFFEE3AE

if app.ENABLE_SHOP_SEARCH_SYSTEM:
	BOARD_WIDTH = 923
	window = {
		"name" : "PrivateShopSearchDialog",

		"x" : 0,
		"y" : 0,

		"style" : ("movable", "float",),

		"width" : BOARD_WIDTH,
		"height" : 545,

		"children" :
		(

			{
				"name" : "board",
				"type" : "board_with_titlebar_shop",
				"x" : 0, "y" : 0,
				"width" : BOARD_WIDTH,
				"height" : 545,
				
				"title" : uiScriptLocale.PRIVATESHOPSEARCH_SEARCH_BAR,
			
				"children" :
						(
							##FilterIMG
							{
								"name" : "Filter",
								"type" : "button",
								"x" : 142,
								"y" : 38,
								"default_image" : LOCALE_PATH + "filter.png",
								"over_image" 	: LOCALE_PATH + "filter_over.png",
								"down_image" 	: LOCALE_PATH + "filter_down.png",
							},
					
							##Beschreibung
							{
							"name" : "label_0",
							"type" : "text",
							"text" : "Name:",
							"color" : 0xffc3c2bd,
							"x" : "240",
							"y" : "40",
							},
							{
							"name" : "label_1",
							"type" : "text",
							"text" : uiScriptLocale.PRIVATESHOPSEARCH_SELLER+":",
							"color" : 0xffc3c2bd,
							"x" : "510",
							"y" : "40",
							},
							{
							"name" : "label_0",
							"type" : "text",
							"text" : uiScriptLocale.PRIVATESHOPSEARCH_VALUE,
							"color" : 0xffc3c2bd,
							"x" : "625",
							"y" : "40",
							},
							{
							"name" : "label_0",
							"type" : "text",
							"text" : uiScriptLocale.PRIVATESHOPSEARCH_PRICE+":",
							"color" : 0xffc3c2bd,
							"x" : "730",
							"y" : "40",
							},
							
					
							## ItemNameEditLine
							{
								"name" : "ItemNameSlot",
								"type" : "image",
								"x" : 12,
								"y" : 42,
								"image" : LOCALE_PATH+"private_leftSlotImg.sub",
								"children" :
								(
									{
										"name" : "ItemNameValue",
										"type" : "editline",
										"x" : 5,
										"y" : 5,
										"width" : 130,
										"height" : 50,
										"input_limit" : 20,
										"text" : "",
									},
								),
							},
							
							## Elendosfiles_Logo
							{
							"name" : "Elendosfiles_logo",
							"type" : "image",
							"x" : 0,
							"y" : 405,
		
							"text" : "",
		
							"image" : "d:/ymir work/ui/logo_elendos.png",
							},
							
							## tab_menu_01
							{
								"name" : "ItemTypeImg",
								"type" : "expanded_image",
								"x" : 204,
								"y" : 60,
								"width" : 10,
								"image" : "d:/ymir work/ui/main-part.png",
								"x_scale" : 1.22, 
								"y_scale" : 1.0,
							},	
							{
								"name" : "first_prev_button", "type" : "button",
								"x" : 230+365, "y" : 518,

								"default_image" : LOCALE_PATH + "private_first_prev_btn_01.sub",
								"over_image" 	: LOCALE_PATH + "private_first_prev_btn_02.sub",
								"down_image" 	: LOCALE_PATH + "private_first_prev_btn_01.sub",
							},
							{
								"name" : "prev_button", "type" : "button",
								"x" : 230+395, "y" : 518,
			
								"default_image" : LOCALE_PATH + "private_prev_btn_01.sub",
								"over_image" 	: LOCALE_PATH + "private_prev_btn_02.sub",
								"down_image" 	: LOCALE_PATH + "private_prev_btn_01.sub",
							},
							{
								"name" : "page1_button", "type" : "button",
								"x" : 275+370, "y" : 515,
			
								"text" : "10000",
			
								"default_image" : LOCALE_PATH + "private_pagenumber_00.sub",
								"over_image" 	: LOCALE_PATH + "private_pagenumber_01.sub",
								"down_image" 	: LOCALE_PATH + "private_pagenumber_02.sub",
							},
							{
								"name" : "page2_button", "type" : "button",
								"x" : 310+370, "y" : 515,
			
								"text" : "2000",
			
								"default_image" : LOCALE_PATH + "private_pagenumber_00.sub",
								"over_image" 	: LOCALE_PATH + "private_pagenumber_01.sub",
								"down_image" 	: LOCALE_PATH + "private_pagenumber_02.sub",
							},
							{
								"name" : "page3_button", "type" : "button",
								"x" : 345+370, "y" : 515,
								
								"text" : "300",
			
								"default_image" : LOCALE_PATH + "private_pagenumber_00.sub",
								"over_image" 	: LOCALE_PATH + "private_pagenumber_01.sub",
								"down_image" 	: LOCALE_PATH + "private_pagenumber_02.sub",
							},
							{
								"name" : "page4_button", "type" : "button",
								"x" : 380+370, "y" : 515,
			
								"text" : "4",
			
								"default_image" : LOCALE_PATH + "private_pagenumber_00.sub",
								"over_image" 	: LOCALE_PATH + "private_pagenumber_01.sub",
								"down_image" 	: LOCALE_PATH + "private_pagenumber_02.sub",
							},
							{
								"name" : "page5_button", "type" : "button",
								"x" : 415+370, "y" : 515,
			
								"text" : "50000",
			
								"default_image" : LOCALE_PATH + "private_pagenumber_00.sub",
								"over_image" 	: LOCALE_PATH + "private_pagenumber_01.sub",
								"down_image" 	: LOCALE_PATH + "private_pagenumber_02.sub",
							},
							{
								"name" : "next_button", "type" : "button",
								"x" : 453+385, "y" : 518,
			
								"default_image" : LOCALE_PATH + "private_next_btn_01.sub",
								"over_image" 	: LOCALE_PATH + "private_next_btn_02.sub",
								"down_image" 	: LOCALE_PATH + "private_next_btn_01.sub",
							},
							{
								"name" : "last_next_button", "type" : "button",
								"x" : 453+415, "y" : 518,
			
								"default_image" : LOCALE_PATH + "private_last_next_btn_01.sub",
								"over_image" 	: LOCALE_PATH + "private_last_next_btn_02.sub",
								"down_image" 	: LOCALE_PATH + "private_last_next_btn_01.sub",
							},
						),
			},
			
			{
				"name" : "BoardFilter",
				"type" : "board_with_titlebar",

				"x" : 200,
				"y" : 55,

				"width" : 140,
				"height" : 230,
				

				"title" : "Filter",
				"children" :
				(
					## LevelText
					{
						"name" : "LevelImg",
						"type" : "image",
						"x" : 10,
						"y" : 135-100,
						"image" : LOCALE_PATH+"private_leftNameImg.sub",
						"children" :
						(
							{ "name" : "LevelText", "type" : "text", "text_horizontal_align":"center", "x" : 60, "y" : 5, "text" : uiScriptLocale.PRIVATESHOPSEARCH_LEVEL },
						),
					},
					## LevelText2
					{ "name" : "LevelText2", "type" : "text", "x" : 65, "y" : 158-100, "text" : "~", "fontsize":"LARGE",},
					## minLevelEditLine
					{
						"name" : "minLevelSlot",
						"type" : "image",
						"x" : 12,
						"y" : 155-100,
						"image" : LOCALE_PATH+"private_leftSlotHalfImg.sub",

						"children" :
						(
							{
								"name" : "minLevelValue",
								"type" : "editline",
								"x" : 2,
								"y" : 3,
								"width" : 36,
								"height" : 15,
								"input_limit" : 3,
								"only_number" : 1,
								"text" : "1",
							},
						),
					},
					## maxLevelEditLine
					{
					
						"name" : "maxLevelSlot",
						"type" : "image",
						"x" : 90,
						"y" : 155-100,
						"image" : LOCALE_PATH+"private_leftSlotHalfImg.sub",

						"children" :
						(
							{
								"name" : "maxLevelValue",
								"type" : "editline",
								"x" : 2,
								"y" : 3,
								"width" : 36,
								"height" : 15,
								"input_limit" : 3,
								"only_number" : 1,
								"text" : "120",
							},
						),
					},
					## refineText
					{
						"name" : "refineImg",
						"type" : "image",
						"x" : 10,
						"y" : 175-100,
						"image" : LOCALE_PATH+"private_leftNameImg.sub",
						"children" :
						(
							{ "name" : "refineText", "type" : "text", "text_horizontal_align":"center", "x" : 60, "y" : 5, "text" : uiScriptLocale.PRIVATESHOPSEARCH_REFINE, "color":GOLD_COLOR },
						),
					},
					## refineText2
					{ "name" : "refineText2", "type" : "text", "x" : 65, "y" : 198-100, "text" : "~", "fontsize":"LARGE"},
					## minrefineEditLine
					{
						"name" : "minrefineSlot",
						"type" : "image",
						"x" : 12,
						"y" : 195-100,
						"image" : LOCALE_PATH+"private_leftSlotHalfImg.sub",
						"children" :
						(
							{
								"name" : "minrefineValue",
								"type" : "editline",
								"x" : 2,
								"y" : 3,
								"width" : 36,
								"height" : 15,
								"input_limit" : 3,
								"only_number" : 1,
								"text" : "0",
							},
						),
					},
					## maxrefineEditLine
					{
						"name" : "maxrefineSlot",
						"type" : "image",
						"x" : 90,
						"y" : 195-100,
						"image" : LOCALE_PATH+"private_leftSlotHalfImg.sub",

						"children" :
						(
							{
								"name" : "maxrefineValue",
								"type" : "editline",
								"x" : 2,
								"y" : 3,
								"width" : 36,
								"height" : 15,
								"input_limit" : 3,
								"only_number" : 1,
								"text" : "9",
							},
						),
					},
					## GoldText
					{
						"name" : "GoldImg",
						"type" : "image",
						"x" : 10,
						"y" : 215-100,
						"image" : LOCALE_PATH+"private_leftNameImg.sub",
						"children" :
						(
							{ "name" : "GoldText", "type" : "text", "text_horizontal_align":"center", "x" : 60, "y" : 5, "text" : uiScriptLocale.PRIVATESHOPSEARCH_PRICE, "color":GOLD_COLOR },
						),
					},
					## GoldminEditLine
					{
						"name":"Money_Icon",
						"type":"image",

						"x":12,
						"y":255-100,

						"image":"d:/ymir work/ui/game/windows/money_icon.sub",
					},
					{
						"name" : "GoldminSlot",
						"type" : "image",
						"x" : 32,
						"y" : 235+10-100,
						"image" : LOCALE_PATH+"private_leftSlotImg_2.sub",

						"children" :
						(
							{
								"name" : "GoldminValue",
								"type" : "editline",
								"x" : 2,
								"y" : 3,
								"width" : 94,
								"height" : 15,
								"input_limit" : 16,
								"only_number" : 1,
								"text" : "0",
							},
						),
					},
					## GoldmaxEditLine
					{
						"name" : "GoldmaxSlot",
						"type" : "image",
						"x" : 32,
						"y" : 255+10-100,
						"image" : LOCALE_PATH+"private_leftSlotImg_2.sub",

						"children" :
						(
							{
								"name" : "GoldmaxValue",
								"type" : "editline",
								"x" : 2,
								"y" : 3,
								"width" : 94,
								"height" : 15,
								"input_limit" : 18,
								"only_number" : 1,
								"text" : "999999999999999",
							},
						),
					},
					## FindButton
					{
						"name" : "SearchButton",
						"type" : "button",

						"x" : 10,
						"y" : 255+35-100,

						"text" : uiScriptLocale.PRIVATESHOPSEARCH_SEARCH,

						"default_image" : LOCALE_PATH + "private_findbuttonImg01.sub",
						"over_image" : LOCALE_PATH + "private_findbuttonImg02.sub",
						"down_image" : LOCALE_PATH + "private_findbuttonImg03.sub",
					},
					## BuyButton
					{
					"name" : "BuyButton",
					"type" : "button",

					"x" : BOARD_WIDTH - 30,
					"y" : 40,

					"text" : "",

					"default_image" : LOCALE_PATH + "private_findbuttonImg02_shop.sub",
					"over_image" : LOCALE_PATH + "private_findbuttonImg01_shop.sub",
					"down_image" : LOCALE_PATH + "private_findbuttonImg03_shop.sub",
					},		
				),
			},
		),
	}