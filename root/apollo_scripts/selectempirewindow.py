import uiScriptLocale
import apollo_interface

ROOT_PATH = "d:/ymir work/ui/public/"
LOCALE_PATH = uiScriptLocale.EMPIRE_PATH

ATALS_X = SCREEN_WIDTH * (282) / 800
ATALS_Y = SCREEN_HEIGHT * (170) / 600

window = {
	"name" : "SelectCharacterWindow",

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(	
		## Board
		{
			"name" : "bg",
			"type" : "expanded_image",
			"x" : 0,
			"y" : 0,
			"x_scale" : float(SCREEN_WIDTH) / 1920.0,
			"y_scale" : float(SCREEN_HEIGHT) / 1080.0,
			"image": "%s/background.png" % apollo_interface.PATCH_LOGIN,
		},
		
		{
			"name" : "SelectCharacterWindow",

			"x" : 0,
			"y" : -100,

			"width" : SCREEN_WIDTH,
			"height" : SCREEN_HEIGHT,

			"children" :
			(	
				
				
				{
					"name" : "BackGround_button_exi",
					"type" : "expanded_image",

					"x" : (SCREEN_WIDTH/2)-130,
					"y" : (SCREEN_HEIGHT/2)+ 148,

					"image": apollo_interface.APOLLO_PATCH + "char_create/gold_chen.png",
				},
				
				{
					"name" : "blue_button",
					"type" : "button",
				
					"x" : (SCREEN_WIDTH/2) - 265, 
					"y" : (SCREEN_HEIGHT/2) - 5,
				
					"default_image" : apollo_interface.APOLLO_EMPIRE + "flag_blue_empire_normal.png",
					"over_image" : apollo_interface.APOLLO_EMPIRE + "flag_blue_empire_hover.png",
					"down_image" : apollo_interface.APOLLO_EMPIRE + "flag_blue_empire_hover.png",
					"disable_image" : apollo_interface.APOLLO_EMPIRE + "flag_blue_empire_hover.png",
				},
				
				{
					"name" : "yellow_button",
					"type" : "button",
				
					"x" : (SCREEN_WIDTH/2) + 100, 
					"y" : (SCREEN_HEIGHT/2) - 5,
				
					"default_image" : apollo_interface.APOLLO_EMPIRE + "flag_yellow_empire_normal.png",
					"over_image" : apollo_interface.APOLLO_EMPIRE + "flag_yellow_empire_hover.png",
					"down_image" : apollo_interface.APOLLO_EMPIRE + "flag_yellow_empire_hover.png",
					"disable_image" : apollo_interface.APOLLO_EMPIRE + "flag_yellow_empire_hover.png",
				},

				{
					"name" : "red_button",
					"type" : "button",
				
					
					"x" : (SCREEN_WIDTH/2) - 83, 
					"y" : (SCREEN_HEIGHT/2) - 5,
				
					"default_image" : apollo_interface.APOLLO_EMPIRE + "flag_red_empire_normal.png",
					"over_image" : apollo_interface.APOLLO_EMPIRE + "flag_red_empire_hover.png",
					"down_image" : apollo_interface.APOLLO_EMPIRE + "flag_red_empire_hover.png",
					"disable_image" : apollo_interface.APOLLO_EMPIRE + "flag_red_empire_hover.png",
				},
				
				{
					"name" : "pfeil_blue",
					"type" : "expanded_image",
				
					"x" : (SCREEN_WIDTH/2) - 22-182, 
					"y" : (SCREEN_HEIGHT/2) - 40,
				
					"image" : apollo_interface.APOLLO_EMPIRE + "pfeil_down.png",
				},
				{
					"name" : "pfeil_red",
					"type" : "expanded_image",
				
					"x" : (SCREEN_WIDTH/2) - 22, 
					"y" : (SCREEN_HEIGHT/2) - 40,
				
					"image" : apollo_interface.APOLLO_EMPIRE + "pfeil_down.png",
				},
				{
					"name" : "pfeil_yellow",
					"type" : "expanded_image",
				
					"x" : (SCREEN_WIDTH/2) - 22+182, 
					"y" : (SCREEN_HEIGHT/2) - 40,
				
					"image" : apollo_interface.APOLLO_EMPIRE + "pfeil_down.png",
				},
				
				{
					"name" : "reichstitel",
					"type" : "text",
				
					"x" : (SCREEN_WIDTH/2), 
					"y" : (SCREEN_HEIGHT/2) + 168,
				
					"text" : "",
					"fontname" : "Tahoma Fett:18",
					
					"r" : 1,
					"g" : 1,
					"b" : 1,
					
					"text_horizontal_align" : "center",
				},
				
				{
					"name" : "reichtxt1",
					"type" : "text",
				
					"x" : (SCREEN_WIDTH/2), 
					"y" : (SCREEN_HEIGHT/2) + 188,
				
					"text" : "",
					"fontname" : "Tahoma Fett:12",
					
					"r" : 1,
					"g" : 1,
					"b" : 1,
					
					"text_horizontal_align" : "center",
				},
				{
					"name" : "reichtxt2",
					"type" : "text",
				
					"x" : (SCREEN_WIDTH/2), 
					"y" : (SCREEN_HEIGHT/2) + 201,
				
					"text" : "",
					"fontname" : "Tahoma Fett:12",
					
					"r" : 1,
					"g" : 1,
					"b" : 1,
					
					"text_horizontal_align" : "center",
				},
				
				{
					"name" : "exit_button",
					"type" : "button",

					"x" : (SCREEN_WIDTH/2)+6,
					"y" : (SCREEN_HEIGHT/2)+240,

					"default_image": "%s/costume/selectcaracter/buttons/btn_option_on.png" % apollo_interface.PATCH_COMMON,
					"over_image": "%s/costume/selectcaracter/buttons/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
					"down_image": "%s/costume/selectcaracter/buttons/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
					"disable_image" : "%s/costume/selectcaracter/buttons/btn_option_disabled.png" % apollo_interface.PATCH_COMMON,
							
					"children" : (
						{
							"name" : "txt",
							"type" : "text",
					
							"x" : (114/2),
							"y" : 13,
					
							"text" : "Beenden",
							"fontname" : "Tahoma Fett:14",
							
							"r" : 1,
							"g" : 1,
							"b" : 1,
							
							"text_horizontal_align" : "center",
						},
					),
				},
				{
					"name" : "select_button",
					"type" : "button",

					"x" : (SCREEN_WIDTH/2)-120,
					"y" : (SCREEN_HEIGHT/2)+240,

					"default_image": "%s/costume/selectcaracter/buttons/btn_option_on.png" % apollo_interface.PATCH_COMMON,
					"over_image": "%s/costume/selectcaracter/buttons/btn_option_ds.png" % apollo_interface.PATCH_COMMON,
					"down_image": "%s/costume/selectcaracter/buttons/btn_option_dn.png" % apollo_interface.PATCH_COMMON,
					"disable_image" : "%s/costume/selectcaracter/buttons/btn_option_disabled.png" % apollo_interface.PATCH_COMMON,
							
					"children" : (
						{
							"name" : "txt",
							"type" : "text",
					
							"x" : (114/2),
							"y" : 13,
					
							"text" : "Wählen",
							"fontname" : "Tahoma Fett:14",
							
							"r" : 1,
							"g" : 1,
							"b" : 1,
							
							"text_horizontal_align" : "center",
						},
					),
				},
			),
		},
	),
}
