import uiScriptLocale

COLOR_TITLE = 0xFFFEE3AE
COLOR_NR_1 = 0xFFFFD200
COLOR_NR_2 = 0xFFF5E493
COLOR_NR_3 = 0xFFDF7900
COLOR_OWN = 0xFFF0C600
COLOR = 0xFFA2A2A2

RANKING_IMG_PATH = "d:/ymir work/ui/public/ranklist/"

MAINBOARD_WIDTH = 710
MAINBOARD_HEIGHT = 405
MAINBOARD_X = 12
MAINBOARD_Y = 35

BG_BOARD_WIDTH = MAINBOARD_WIDTH - 24
BG_BOARD_HEIGHT = MAINBOARD_HEIGHT - 35 - 12
BG_BOARD_X = 12
BG_BOARD_Y = 35

LEFTBOARD_WIDTH = 143 + 24
LEFTBOARD_HEIGHT = BG_BOARD_HEIGHT - 26
LEFTBOARD_X = 13
LEFTBOARD_Y = 13

RIGHTBOARD_WIDTH = 455 + 24
RIGHTBOARD_HEIGHT = BG_BOARD_HEIGHT - 26
RIGHTBOARD_X = 13 + LEFTBOARD_WIDTH + 13
RIGHTBOARD_Y = 13

RANKLIST_START_Y = 12 + 28

window = {
	"name" : "LotteryRankingWindow",
	"style" : ("movable", "float",),

	"x" : (SCREEN_WIDTH / 2) - (MAINBOARD_WIDTH / 2),
	"y" : (SCREEN_HEIGHT / 2) - (MAINBOARD_HEIGHT / 2) ,

	"width" : MAINBOARD_WIDTH,
	"height" : MAINBOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"x" : 0,
			"y" : 0,
			"width" : MAINBOARD_WIDTH,
			"height" : MAINBOARD_HEIGHT,
			"title" : uiScriptLocale.LOTTO_RANKLIST_TITLE,
			"children" :
			(
				{
					"name" : "BackgroundBoard",
					"type" : "thinboard",
					"x" : BG_BOARD_X,
					"y" : BG_BOARD_Y,
					"width" : BG_BOARD_WIDTH,
					"height" : BG_BOARD_HEIGHT,
					"children" :
					(
						{
							"name" : "ButtonListBoard",
							"type" : "thinboard_round",
							"x" : LEFTBOARD_X,
							"y" : LEFTBOARD_Y ,
							"width" : LEFTBOARD_WIDTH,
							"height" : LEFTBOARD_HEIGHT,
							"children" :
							(
								{
									"name" : "jackpotbtn",
									"type" : "radio_button",

									"x" : 12,
									"y" : 12,

									"text" : "Gewonnene Jackpots",
									"text" : uiScriptLocale.LOTTO_Elendos_JACKPOT_WIN,
									
									#"text_color" : 0xffff9900,
									#"text_outline" : 1,
									
									"default_image" : RANKING_IMG_PATH + "select_button_normal.sub",
									"over_image" : RANKING_IMG_PATH + "select_button_hover.sub",
									"down_image" : RANKING_IMG_PATH + "select_button_select.sub",
								},
								{
									"name" : "winbtn",
									"type" : "radio_button",
					
									"x" : 12,
									"y" : 12 + 42 + 12,
					
									"text" : uiScriptLocale.LOTTO_Elendos_GESAMMT2_WIN,
									#"text_color" : 0xffff9900,
									#"text_outline" : 1,
					
									"default_image" : RANKING_IMG_PATH + "select_button_normal.sub",
									"over_image" : RANKING_IMG_PATH + "select_button_hover.sub",
									"down_image" : RANKING_IMG_PATH + "select_button_select.sub",
								},
							),
						},
						{
							"name" : "RankingListBoard",
							"type" : "thinboard_round",
							"x" : RIGHTBOARD_X,
							"y" : RIGHTBOARD_Y,
							"width" : RIGHTBOARD_WIDTH,
							"height" : RIGHTBOARD_HEIGHT,
							"children" :
							(
								{
									"name" : "bg_ranking_title", 
									"type" : "image", 
									"horizontal_align" : "center",
									"x" : 0, "y" : 12, 
									"image" : RANKING_IMG_PATH + "ranking_titlebar_column_4.sub",
									"children" :
									(
										{"name" : "title_0", "type":"text", "text": "", "x": 86 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_TITLE},
										{"name" : "title_1", "type":"text", "text": "", "x": 193 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_TITLE},
										{"name" : "title_2", "type":"text", "text": "", "x": 299 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_TITLE},
										{"name" : "title_3", "type":"text", "text": "", "x": 402 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_TITLE},
									),
								},
								{
									"name" : "bg_ranking_row_0", 
									"type" : "image", 
									"horizontal_align" : "center",
									"x" : 0, "y" : RANKLIST_START_Y + 26 * 0, 
									"image" : RANKING_IMG_PATH + "ranking_list_column_4.sub",
									"children" :
									(
										{"name" : "row_0_0", "type":"text", "text": "", "x": 16 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_1},
										{"name" : "row_0_1", "type":"text", "text": "", "x": 86 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_1},
										{"name" : "row_0_2", "type":"text", "text": "", "x": 193 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_1},
										{"name" : "row_0_3", "type":"text", "text": "", "x": 299 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_1},
										{"name" : "row_0_4", "type":"text", "text": "", "x": 402 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_1},
										{ "name" : "flag_0_1",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_0.sub"},
										{ "name" : "flag_0_2",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_1.sub"},
										{ "name" : "flag_0_3",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_2.sub"},
									),
								},
								{
									"name" : "bg_ranking_row_1", 
									"type" : "image", 
									"horizontal_align" : "center",
									"x" : 0, "y" : RANKLIST_START_Y+ 26 * 1, 
									"image" : RANKING_IMG_PATH + "ranking_list_column_4.sub",
									"children" :
									(
										{"name" : "row_1_0", "type":"text", "text": "", "x": 16 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_2},
										{"name" : "row_1_1", "type":"text", "text": "", "x": 86 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_2},
										{"name" : "row_1_2", "type":"text", "text": "", "x": 193 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_2},
										{"name" : "row_1_3", "type":"text", "text": "", "x": 299 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_2},
										{"name" : "row_1_4", "type":"text", "text": "", "x": 402 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_2},
										{ "name" : "flag_1_1",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_0.sub"},
										{ "name" : "flag_1_2",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_1.sub"},
										{ "name" : "flag_1_3",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_2.sub"},
									),
								},
								{
									"name" : "bg_ranking_row_2", 
									"type" : "image", 
									"horizontal_align" : "center",
									"x" : 0, "y" : RANKLIST_START_Y + 26 * 2, 
									"image" : RANKING_IMG_PATH + "ranking_list_column_4.sub",
									"children" :
									(
										{"name" : "row_2_0", "type":"text", "text": "", "x": 16 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_3},
										{"name" : "row_2_1", "type":"text", "text": "", "x": 86 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_3},
										{"name" : "row_2_2", "type":"text", "text": "", "x": 193 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_3},
										{"name" : "row_2_3", "type":"text", "text": "", "x": 299 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_3},
										{"name" : "row_2_4", "type":"text", "text": "", "x": 402 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_NR_3},
										{ "name" : "flag_2_1",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_0.sub"},
										{ "name" : "flag_2_2",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_1.sub"},
										{ "name" : "flag_2_3",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_2.sub"},
									),
								},
								{
									"name" : "bg_ranking_row_3", 
									"type" : "image", 
									"horizontal_align" : "center",
									"x" : 0, "y" : RANKLIST_START_Y + 26 * 3, 
									"image" : RANKING_IMG_PATH + "ranking_list_column_4.sub",
									"children" :
									(
										{"name" : "row_3_0", "type":"text", "text": "", "x": 16 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_3_1", "type":"text", "text": "", "x": 86 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_3_2", "type":"text", "text": "", "x": 193 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_3_3", "type":"text", "text": "", "x": 299 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_3_4", "type":"text", "text": "", "x": 402 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{ "name" : "flag_3_1",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_0.sub"},
										{ "name" : "flag_3_2",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_1.sub"},
										{ "name" : "flag_3_3",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_2.sub"},
									),
								},
								{
									"name" : "bg_ranking_row_4", 
									"type" : "image", 
									"horizontal_align" : "center",
									"x" : 0, "y" : RANKLIST_START_Y + 26 * 4, 
									"image" : RANKING_IMG_PATH + "ranking_list_column_4.sub",
									"children" :
									(
										{"name" : "row_4_0", "type":"text", "text": "", "x": 16 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_4_1", "type":"text", "text": "", "x": 86 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_4_2", "type":"text", "text": "", "x": 193 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_4_3", "type":"text", "text": "", "x": 299 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_4_4", "type":"text", "text": "", "x": 402 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{ "name" : "flag_4_1",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_0.sub"},
										{ "name" : "flag_4_2",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_1.sub"},
										{ "name" : "flag_4_3",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_2.sub"},
									),
								},
								{
									"name" : "bg_ranking_row_5", 
									"type" : "image", 
									"horizontal_align" : "center",
									"x" : 0, "y" : RANKLIST_START_Y + 26 * 5, 
									"image" : RANKING_IMG_PATH + "ranking_list_column_4.sub",
									"children" :
									(
										{"name" : "row_5_0", "type":"text", "text": "", "x": 16 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_5_1", "type":"text", "text": "", "x": 86 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_5_2", "type":"text", "text": "", "x": 193 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_5_3", "type":"text", "text": "", "x": 299 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_5_4", "type":"text", "text": "", "x": 402 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{ "name" : "flag_5_1",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_0.sub"},
										{ "name" : "flag_5_2",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_1.sub"},
										{ "name" : "flag_5_3",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_2.sub"},
									),
								},
								{
									"name" : "bg_ranking_row_6", 
									"type" : "image", 
									"horizontal_align" : "center",
									"x" : 0, "y" : RANKLIST_START_Y + 26 * 6, 
									"image" : RANKING_IMG_PATH + "ranking_list_column_4.sub",
									"children" :
									(
										{"name" : "row_6_0", "type":"text", "text": "", "x": 16 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_6_1", "type":"text", "text": "", "x": 86 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_6_2", "type":"text", "text": "", "x": 193 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_6_3", "type":"text", "text": "", "x": 299 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_6_4", "type":"text", "text": "", "x": 402 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{ "name" : "flag_6_1",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_0.sub"},
										{ "name" : "flag_6_2",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_1.sub"},
										{ "name" : "flag_6_3",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_2.sub"},
									),
								},
								{
									"name" : "bg_ranking_row_7", 
									"type" : "image", 
									"horizontal_align" : "center",
									"x" : 0, "y" : RANKLIST_START_Y + 26 * 7, 
									"image" : RANKING_IMG_PATH + "ranking_list_column_4.sub",
									"children" :
									(
										{"name" : "row_7_0", "type":"text", "text": "", "x": 16 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_7_1", "type":"text", "text": "", "x": 86 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_7_2", "type":"text", "text": "", "x": 193 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_7_3", "type":"text", "text": "", "x": 299 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_7_4", "type":"text", "text": "", "x": 402 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{ "name" : "flag_7_1",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_0.sub"},
										{ "name" : "flag_7_2",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_1.sub"},
										{ "name" : "flag_7_3",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_2.sub"},
									),
								},
								{
									"name" : "bg_ranking_row_8", 
									"type" : "image", 
									"horizontal_align" : "center",
									"x" : 0, "y" : RANKLIST_START_Y + 26 * 8, 
									"image" : RANKING_IMG_PATH + "ranking_list_column_4.sub",
									"children" :
									(
										{"name" : "row_8_0", "type":"text", "text": "", "x": 16 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_8_1", "type":"text", "text": "", "x": 86 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_8_2", "type":"text", "text": "", "x": 193 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_8_3", "type":"text", "text": "", "x": 299 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_8_4", "type":"text", "text": "", "x": 402 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{ "name" : "flag_8_1",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_0.sub"},
										{ "name" : "flag_8_2",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_1.sub"},
										{ "name" : "flag_8_3",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_2.sub"},
									),
								},
								{
									"name" : "bg_ranking_row_9", 
									"type" : "image", 
									"horizontal_align" : "center",
									"x" : 0, "y" : RANKLIST_START_Y + 26 * 9, 
									"image" : RANKING_IMG_PATH + "ranking_list_column_4.sub",
									"children" :
									(
										{"name" : "row_9_0", "type":"text", "text": "", "x": 16 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_9_1", "type":"text", "text": "", "x": 86 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_9_2", "type":"text", "text": "", "x": 193 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_9_3", "type":"text", "text": "", "x": 299 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{"name" : "row_9_4", "type":"text", "text": "", "x": 402 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR},
										{ "name" : "flag_9_1",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_0.sub"},
										{ "name" : "flag_9_2",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_1.sub"},
										{ "name" : "flag_9_3",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_2.sub"},
									),
								},
								{
									"name" : "bg_ranking_own", 
									"type" : "image", 
									"horizontal_align" : "center",
									"x" : 0, "y" : RANKLIST_START_Y + 26 * 10 + 2, 
									"image" : RANKING_IMG_PATH + "ranking_own_column_4.sub",
									"children" :
									(
										{"name" : "own_0", "type":"text", "text": "", "x": 16 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_OWN},
										{"name" : "own_1", "type":"text", "text": "", "x": 86 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_OWN},
										{"name" : "own_2", "type":"text", "text": "", "x": 193 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_OWN},
										{"name" : "own_3", "type":"text", "text": "", "x": 299 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_OWN},
										{"name" : "own_4", "type":"text", "text": "", "x": 402 , "y": 11, "text_horizontal_align":"center", "text_vertical_align":"center", "color" : COLOR_OWN},
										{ "name" : "flag_own_0",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_0.sub"},
										{ "name" : "flag_own_1",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_1.sub"},
										{ "name" : "flag_own_2",  "type" : "image", "x" : 299 - 17, "y" : 1,  "image" : RANKING_IMG_PATH + "flag_2.sub"},
									),
								},
							),
						},
					),
				},
			),
		},
	),
}
