import uiScriptLocale

MAIN_PATH = "d:/ymir work/ui/intro_elendos/"
COMMON_PATH = "d:/ymir work/ui/intro_elendos/common/"
BUTTON_PATH = "d:/ymir work/ui/intro_elendos/button/"

EXIT_BUTTON_Y = 320
if SCREEN_HEIGHT < 800:
	EXIT_BUTTON_Y = 200

window = {
    "name" : "SelectEmpireWindow",
    "x" : 0, "y" : 0,
    "width" : SCREEN_WIDTH, "height" : SCREEN_HEIGHT,
    "children" : (
        {
            "name" : "BackgroundImage", "type" : "expanded_image",
            "x" : 0, "y" : 0,
            "x_scale" : float(SCREEN_WIDTH) / 1920.0, "y_scale" : float(SCREEN_HEIGHT) / 1080.0,
            "image" : MAIN_PATH + "background_empireselect.jpg",
        },
		{ "name" : "video_layer",  "type" : "window", "x" : 0, "y" : 0, "width" : SCREEN_WIDTH, "height" : SCREEN_HEIGHT, },
		
        {
            "name" : "ContainerEmpireRed", "type" : "image",
            "x" : -416 + 133, "y" : 0 - 40, "horizontal_align" : "center", "vertical_align" : "center",
            "image" : MAIN_PATH + "empire_select_board.tga",
            "children" : (
                { "name" : "TitleTextKingdomRed", "type" : "text", "x" : 65, "y" : 29, "color" : 0xff9a8b70, "fontsize" : "LARGE", "text" : "Shinsoo" },
                { "name" : "FlagRedImage", "type" : "image", "x" : 59, "y" : 89, "image" : COMMON_PATH + "empire_red.sub" },
                {
                    "name" : "DescTextKingdomRed", "type" : "multi_text",
                    "x" : 24, "y" : 192, "width" : 219, "height" : 80, "color" : 0xff9a8b70,
                    "text" : "Here you can select the Red Empire. The Red[ENTER]Empire was blessed on Elendosfiles by Dragon God.[ENTER]We wish you much fun!",
                },
				{
					"name" : "ButtonSelectRedEmpire", "type" : "button",
					"x" : 19, "y" : 283,
					"default_image" : BUTTON_PATH + "button_select_normal.sub",
					"over_image" : BUTTON_PATH + "button_select_hover.sub",
					"down_image" : BUTTON_PATH + "button_select_down.sub",
				},
            ),
        },
        {
            "name" : "ContainerEmpireYellow", "type" : "image",
            "x" : -132 + 133, "y" : 0 - 40, "horizontal_align" : "center", "vertical_align" : "center",
            "image" : MAIN_PATH + "empire_select_board.tga",
            "children" : (
                { "name" : "TitleTextKingdomYellow", "type" : "text", "x" : 65, "y" : 29, "color" : 0xff9a8b70, "fontsize" : "LARGE", "text" : "Chunjo" },
                { "name" : "FlagRedImage", "type" : "image", "x" : 59, "y" : 89, "image" : COMMON_PATH + "empire_yellow.sub" },
                {
                    "name" : "DescTextKingdomYellow", "type" : "multi_text",
                    "x" : 24, "y" : 192, "width" : 219, "height" : 80, "color" : 0xff9a8b70,
                    "text" : "Here you can select the Yellow Empire. The[ENTER]Yellow Empire was blessed on Elendosfiles by[ENTER]Dragon God. We wish you much fun!",
                },
				{
					"name" : "ButtonSelectYellowEmpire", "type" : "button",
					"x" : 19, "y" : 283,
					"default_image" : BUTTON_PATH + "button_select_normal.sub",
					"over_image" : BUTTON_PATH + "button_select_hover.sub",
					"down_image" : BUTTON_PATH + "button_select_down.sub",
				},
            ),
        },
        {
            "name" : "ContainerEmpireBlue", "type" : "image",
            "x" : 156 + 133, "y" : 0 - 40, "horizontal_align" : "center", "vertical_align" : "center",
            "image" : MAIN_PATH + "empire_select_board.tga",
            "children" : (
                { "name" : "TitleTextKingdomBlue", "type" : "text", "x" : 65, "y" : 29, "color" : 0xff9a8b70, "fontsize" : "LARGE", "text" : "Jinno" },
                { "name" : "FlagRedImage", "type" : "image", "x" : 59, "y" : 89, "image" : COMMON_PATH + "empire_blue.sub" },
                {
                    "name" : "DescTextKingdomBlue", "type" : "multi_text",
                    "x" : 24, "y" : 192, "width" : 219, "height" : 80, "color" : 0xff9a8b70,
                    "text" : "Here you can select the Blue Empire. The Blue[ENTER]Empire was blessed on Elendosfiles by Dragon God.[ENTER]We wish you much fun!",
                },
				{
					"name" : "ButtonSelectBlueEmpire", "type" : "button",
					"x" : 19, "y" : 283,
					"default_image" : BUTTON_PATH + "button_select_normal.sub",
					"over_image" : BUTTON_PATH + "button_select_hover.sub",
					"down_image" : BUTTON_PATH + "button_select_down.sub",
				},
            ),
        },

		{
			"name" : "ExitButton", "type" : "button",
			"x" : 0, "y" : EXIT_BUTTON_Y, "horizontal_align" : "center", "vertical_align" : "center",
			"default_image" : BUTTON_PATH + "button_exit_normal.sub",
			"over_image" : BUTTON_PATH + "button_exit_hover.sub",
			"down_image" : BUTTON_PATH + "button_exit_down.sub",
		},
    ),
}