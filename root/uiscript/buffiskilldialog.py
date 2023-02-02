import uiScriptLocale

MAX_SKILL_COUNT = 5
BOARD_WIDTH = 360
BOARD_HEIGHT = 290

window = {
	"name" : "AssistantSkillDialog",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
		
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : BOARD_WIDTH-13,
					"color" : "red",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":BOARD_WIDTH/2-10, "y":4, "text": "Buffi System", "text_horizontal_align":"center" },
					),
				},
				{
					"name" : "arkaPlan",
					"type" : "thinboard_circle",
					"x" : 15, "y" : 35, "width" : 200, "height" : 75,
					"children" :
					(
						{
						"name" : "buffiBilgiler",
						"type" : "image",
						
						"x" : 0, "y" : 1,
						"image" : "larry/buffi_gui/baslik1.tga",
						},
						# {
							# "name" : "skillSlot3", "type" : "grid_table", "x" : 10, "y" : 30, "start_index" : 0,
							# "x_count" : MAX_SKILL_COUNT, "y_count" : 1, "x_step" : 32, "y_step" : 32, "x_blank" : 5, "y_blank" : 4,
							# "image" : "d:/ymir work/ui/Public/Slot_Base.sub", "horizontal_align" : "center",
						# },
						{ "name" : "buffiTitle", "type" : "text", "x" : 0, "y" : -26, "text" : "Information", "all_align":"center", "color" : 0xffc71616 },
						{ "name" : "buffiInfo_1", "type" : "text", "x" : 0, "y" : -8, "text" : "This is your Buff Helper. You can", "all_align":"center" },
						{ "name" : "buffiInfo_2", "type" : "text", "x" : 0, "y" : -0+4, "text" : "equip them with armour, weapons, hair,", "all_align":"center" },
						{ "name" : "buffiInfo_3", "type" : "text", "x" : 0, "y" : -0+15, "text" : "costumes. ATTENTION:", "all_align":"center" },
						{ "name" : "buffiInfo_4", "type" : "text", "x" : 0, "y" : -0+13+13, "text" : "Items with bonuses are not taken over!", "all_align":"center" },
					),
				},
				{
					"name" : "arkaPlan",
					"type" : "thinboard_circle",
					"x" : 15, "y" : 115, "width" : 200, "height" : 75,
					"children" :
					(
						{
						"name" : "beceriBilgiler",
						"type" : "image",
						
						"x" : 0, "y" : 1,
						"image" : "larry/buffi_gui/baslik1.tga",
						},
						{
							"name" : "skillSlot", "type" : "grid_table", "x" : 10, "y" : 30, "start_index" : 0,
							"x_count" : MAX_SKILL_COUNT, "y_count" : 1, "x_step" : 32, "y_step" : 32, "x_blank" : 5, "y_blank" : 4,
							"image" : "d:/ymir work/slot_lager/slot.tga", "horizontal_align" : "center",
						},
						{ "name" : "becerilerTitle", "type" : "text", "x" : 0, "y" : -26, "text" : "Skills", "all_align":"center", "color" : 0xffc71616 },
					),
				},
				{
					"name" : "arkaPlan",
					"type" : "thinboard_circle",
					"x" : 15, "y" : 195, "width" : 200, "height" : 75,
					"children" :
					(
						{
						"name" : "buffiDerece",
						"type" : "image",
						
						"x" : 0, "y" : 1,
						"image" : "larry/buffi_gui/baslik1.tga",
						},
						# {
							# "name" : "skillSlot1", "type" : "grid_table", "x" : 10, "y" : 30, "start_index" : 0,
							# "x_count" : MAX_SKILL_COUNT, "y_count" : 1, "x_step" : 32, "y_step" : 32, "x_blank" : 5, "y_blank" : 4,
							# "image" : "d:/ymir work/ui/Public/Slot_Base.sub", "horizontal_align" : "center",
						# },
						{ "name" : "becerilerTitle", "type" : "text", "x" : 0, "y" : -26, "text" : "Time", "all_align":"center", "color" : 0xffc71616 },
					),
				},
				{
					"name" : "arkaPlan",
					"type" : "thinboard_circle",
					"x" : 220, "y" : 35, "width" : 125, "height" : 225,
					"children" :
					(
						{
						"name" : "ModelView2",
						"type" : "image",
						
						"x" : 0, "y" : 1,
						"image" : "larry/buffi_gui/baslik2.tga",
						},
						{
							"name" : "kostumAP",
							"type" : "image",
							"x" : 3, "y" : 25,
							"image" : "larry/buffi_gui/female_multi.tga" 
						},
						{
							"name" : "itemSlotlar",
							"type" : "slot",
					
							"x" : 0,
							"y" : 0,
					
							"width" : 300,
							"height" : 300,
							
							"slot" :
							(
								{"index":1, "x":56, "y":68, "width":31, "height":64}, # Rüstungsslot
								{"index":2, "x":56, "y":31, "width":32, "height":32}, #Haarslot
								{"index":3, "x":17, "y":38, "width":31, "height":96}, #Waffenslot
								{"index":4, "x":17, "y":142, "width":31, "height":32}, #Shinigslot 1 links
								{"index":5, "x":74, "y":142, "width":31, "height":32}, #Shinigslot 1 rechts
								{"index":6, "x":17, "y":177, "width":31, "height":32}, #Shinigslot 2 links
								{"index":7, "x":74, "y":177, "width":31, "height":32}, #Shinigslot 2 rechts
							),
						},
						{ "name" : "ekipmanlarTitle", "type" : "text", "x" : 0, "y" : -101, "text" : "Equipment", "all_align":"center", "color" : 0xffc71616 },

					),
				},
			),
		},
	),
}