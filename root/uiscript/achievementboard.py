import uiScriptLocale
Abstand = 30
Board_width = 220

ACHIEVEMENTSYSTEM_PATH = "locale/de/ui/achievementsystem/"


window = {
	"name" : "achievementboard",
	"style" : ("movable", "float",),

	"x" : SCREEN_WIDTH - Board_width - 15,
	"y" : SCREEN_HEIGHT - 90 - 15,

	"width" : Board_width,
	"height" : 90,

	"children" :
	(
		{
			"name" : "board",
			"type" : "image",

			"x" : 0,
			"y" : 0,

			
			"image" : ACHIEVEMENTSYSTEM_PATH+"other/achievement_done.tga",

			"children" :
			(
				# {
					# "name" : "Achievement_Image",
					# "type" : "image",

					# "x" : 19,
					# "y" : 14 + 10,

					# "image" : "d:/ymir work/ui/public/achievement_small.sub",
				# },
				{
					"name" : "Achievement_Filler",
					"type" : "text",

					"x" : 80,
					"y" : 5,

					"text" : "Achievement erreicht:",
				},
				{
					"name" : "Achievement_Text",
					"type" : "text",

					"x" : 80,
					"y" : 25,

					"text" : "Achievement",
				},
				{
					"name" : "Achievement_Points_Text",
					"type" : "text",

					"x" : 100,
					"y" : 25,

					"text" : "",
				},
				{
					"name" : "Count_Filler",
					"type" : "text",

					"x" : 80,
					"y" : 45,

					"text" : "",
				},
				{
					"name" : "Count_Achievement_Text",
					"type" : "text",

					"x" : 125,
					"y" : 45,

					"text" : "",
				},
				{
					"name" : "Achievement_Info_1",
					"type" : "text",

					"x" : 80,
					"y" : 5,

					"text" : "",
				},
				{
					"name" : "Achievement_Info_2",
					"type" : "text",

					"x" : 80,
					"y" : 25,

					"text" : "",
				},
				{
					"name" : "Achievement_Info_3",
					"type" : "text",

					"x" : 80,
					"y" : 45,

					"text" : "",
				},
			),
		},
	),
}
