import uiScriptLocale

RUMI_ROOT = "d:/ymir work/ui/minigame/rumi/"

window = {
	"name" : "MiniGameWindow",
	
	"x" : SCREEN_WIDTH - 186 - 100,
	"y" : 50,
	
	"width" : 100,
	"height" : 58,
	
	"children" :
	(
		{
			"name" : "mini_game_window",
			"type" : "window",
			
			"x" : 0,
			"y" : 0,
			
			"width" : 100,
			"height" : 58,
			
			"children" :
			(
				{
					"name" : "minigame_rumi_button",
					"type" : "button",
					
					"x" : 30,
					"y" : 40,
					
					"default_image" : RUMI_ROOT + "rumi_button_min.sub",
					"over_image" : RUMI_ROOT + "rumi_button_min.sub",
					"down_image" : RUMI_ROOT + "rumi_button_min.sub",
				},
			),
		},		
	),	
}
