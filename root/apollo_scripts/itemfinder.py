import uiScriptLocale
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import apollo_interface
LOCALE_PATH = "d:/ymir work/ui/itemfinder/"
window = {
	"name" : "ItemFinder",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : 464,
	"height" : 380,

	"children" :
	(
		## Board and buttons
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 464,
			"height" : 380,

			"children" :
			(
				## TitleBar
				{"name" : "TitleBar","type" : "titlebar","style" : ("attach",),"x" : 8,"y" : 8,"width" : 464 - 15,"color" : "gray",
					"children" :
					(
						{ 
							"name":"TitleName", "type":"text", "x" : (464 - 15) / 2, "y":4, "text":"Find Specify Item Monster Drop", "text_horizontal_align":"center" 
						},
					),
				},
				{
					"name" : "Quest_BoardA",
					"type" : "border_a",
					
					"x" : 10,
					"y" : 35,

        			"width" : 433,
        			"height" : 49,
				},
				{
					"name" : "search_button",
					"type" : "button",

					"x" : -30,
					"y" : 48,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",

					"default_image" : "d:/ymir work/item_finder_new/such_button_normal.tga",
					"over_image" : "d:/ymir work/item_finder_new/such_button_hover.tga",
					"down_image" : "d:/ymir work/item_finder_new/such_button_down.tga",
				},
				{
					"name" : "clear_button",
					"type" : "button",

					"x" : 60,
					"y" : 48,

					"width" : 61,
					"height" : 21,

					"horizontal_align" : "center",

					"default_image" : "d:/ymir work/item_finder_new/delte_button_normal.tga",
					"over_image" : "d:/ymir work/item_finder_new/delte_button_hover.tga",
					"down_image" : "d:/ymir work/item_finder_new/delte_button_down.tga",
				},
				{
					"name" : "bg_findere", # Feld Links (Groﬂ)
					"type" : "image",
					"x" : 10,
					"y" : 83,
					"image" : "d:/ymir work/item_finder_new/hintergrund_finder_search.tga",
				},
				{
					"name" : "BG2", # Feld Rechts (Groﬂ)
					"type" : "image",
					"x" : 235,
					"y" : 83,
					"image" : "d:/ymir work/item_finder_new/preview_finder_search.tga",
				},
				{
					"name" : "ScrollBar","type" : "new_scrollbar","x" : 220,"y" : 90,"size" : 268,
				},
				{ 
					"name" : "TextPreviewTtiel", "type" : "text", "x" : 325, "y" : 99, "text" : "Preview", 
				},
				{
					"name" : "ItemNameImg",
					"type" : "image",
					"x" : 39,
					"y" : 275-238,
					"image" : "d:/ymir work/item_finder_new/item_names_normal.tga",
					"children" :
					(
						{ "name" : "ItemNameText", "type" : "text", "text_horizontal_align":"center", "x" : 60, "y" : 5, "text" : "", #"color":0xFFFEE3AE 
						},
					),
				},
				
				{
					"name" : "ItemNameSlot",
					"type" : "image",
					"x" : 19,
					"y" : 295-238,
					"image" : LOCALE_PATH+"private_leftSlotImg.sub",
					"children" :
					(
						{
							"name" : "ItemNameValue",
							"type" : "editline",
							"x" : 3,
							"y" : 3,
							"width" : 136,
							"height" : 15,
							"input_limit" : 20,
							"text" : "",
						},
					),
				},
	
			),
		},
	),
}