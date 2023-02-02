import uiScriptLocale
import item

COSTUME_START_INDEX = item.COSTUME_SLOT_START
SHINING_START_INDEX = item.SHINING_SLOT_START

window = {
	"name" : "CostumeWindow",

	"x" : SCREEN_WIDTH - 225 - 250,
	"y" : SCREEN_HEIGHT - 37 - 350,

	"style" : ("movable", "float",),

	"width" : 140,
	"height" : (210 + 47-25),

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 140,
			"height" : (210 + 47-25),
			
			"title" : uiScriptLocale.COSTUME_WINDOW_TITLE,
		
			"children" :
			(

				## Equipment Slot
				{
					"name" : "Costume_Base",
					"type" : "image",

					"x" : 13,
					"y" : 38,
				
					"image" : uiScriptLocale.LOCALE_UISCRIPT_PATH + "costume/costume_bg.jpg",

					"children" :
					(
						{
							"name" : "Costume_Page",
							"type" : "window",
							"style" : ("attach",),

							"x" : 0,
							"y" : 0,

							"width" : 127,
							"height" : 227,

							"children" :
							(
								{
									"name" : "CostumeSlot",
									"type" : "slot",

									"x" : 3,
									"y" : 3,

									"width" : 127,
									"height" : 227,

									"slot" : (
												{"index":COSTUME_START_INDEX+0, "x":61, "y":45, "width":32, "height":64},
												{"index":COSTUME_START_INDEX+1, "x":61, "y": 8, "width":32, "height":32},
												{"index":COSTUME_START_INDEX+2, "x":61, "y":125, "width":32, "height":32},
												{"index":COSTUME_START_INDEX+3, "x":12, "y":12, "width":32, "height":32},
												{"index":COSTUME_START_INDEX+4, "x":12, "y":125, "width":32, "height":32},
											),
								},
							),
						},
						{
							"name" : "Shining_Page",
							"type" : "window",
							"style" : ("attach",),

							"x" : 0,
							"y" : 0,

							"width" : 127,
							"height" : 227,

							"children" :
							(
								{
									"name" : "ShiningSlot",
									"type" : "slot",

									"x" : 3,
									"y" : 3,

									"width" : 127,
									"height" : 227,

									"slot" : (
												#Waffe
												{"index":SHINING_START_INDEX+0, "x":16, "y":79, "width":32, "height":32},
												{"index":SHINING_START_INDEX+1, "x":16, "y":47, "width":32, "height":32},
												{"index":SHINING_START_INDEX+2, "x":16, "y":15, "width":32, "height":32},
												#Armor
												{"index":SHINING_START_INDEX+3, "x":65, "y":79, "width":32, "height":32},
												{"index":SHINING_START_INDEX+4, "x":65, "y":47, "width":32, "height":32},
												#Special
												{"index":SHINING_START_INDEX+5, "x":65, "y":12, "width":32, "height":32},
											),
								},
							),
						},
					),
				},
				{
					"name" : "ChangeButton",
					"type" : "button",

					"x" : 113,
					"y" : 38,

					"tooltip_text" : uiScriptLocale.CHANGE_SHINING,

					"default_image" : "uiscript/refresh/refresh_normal.tga",
					"over_image" : "uiscript/refresh/refresh_hover.tga",
					"down_image" : "uiscript/refresh/refresh_pressed.tga",
				},
				{
					"name" : "HideButton",
					"type" : "button",

					"x" : 10,
					"y" : 38,
					
					"tooltip_text" : "Hide/Show Costume",

					"default_image" : "uiscript/refresh/refresh_normal.tga",
					"over_image" : "uiscript/refresh/refresh_hover.tga",
					"down_image" : "uiscript/refresh/refresh_pressed.tga",
				},
			),
		},
	),
}
