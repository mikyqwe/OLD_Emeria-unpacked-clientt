import uiScriptLocale

BOARD_WIDTH = 736
BOARD_HEIGHT = 483

ACHIEVEMENTSYSTEM_PATH = "locale/de/ui/achievementsystem/"

window = {
	"name" : "Achievementsystem",

	"x" : SCREEN_WIDTH/2-BOARD_WIDTH/2,
	"y" : 10,

	"style" : ("movable", "float"),

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "img_background",
			"type" : "board",
			"style" : ("attach",),
			
			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"children" :
			(
				{
					"name" : "titlebar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 8,
					"y" : 8,

					"width" : BOARD_WIDTH-15,

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":0, "y":3, "text":'Achievementsystem',"horizontal_align" : "center", "text_horizontal_align":"center",},
					),
				},
				{
					"name": "main_progressbar",
					
					"x" : 9,
					"y" : 25,
					
					"width" : 714,
					"height" : 54,

					"style" : ("attach",),
					
					"children": 
					(
						{
							"name" : "img_main_progressbar_empty",
							"type" : "image",
							"style" : ("attach",),
							
							"image" : ACHIEVEMENTSYSTEM_PATH+"other/main_progressbar_empty.tga",
							"x" : 0,
							"y" : 0,
						},
						{
							 "name" : "eimg_main_progressbar_full",
							 "type" : "expanded_image",
							 "style" : ("attach",),
							
							 "image" : ACHIEVEMENTSYSTEM_PATH+"other/main_progressbar_full.tga",
							 "x" : 63,
							 "y" : 12,

							 "width" : 643,
							 "height" : 29,
						},
						{
							 "name" : "img_main_progressbar_completed",
							 "type" : "expanded_image",
							 "style" : ("attach",),
							
							 "image" : ACHIEVEMENTSYSTEM_PATH+"other/main_progressbar_completed.tga",
							 "x" : 63,
							 "y" : 12,

							 "width" : 643,
							 "height" : 29,
						},
                        {
						    "name" : "txt_main_progressbar_title",
						    "type" : "text",
						    "text" : "Erledigte Achievements",
                            "fontsize" : "LARGE",
						    "x" : 74,
						    "y" : 17,
					    },
                        ## not in use
                        #{
						   # "name" : "txt_main_progressbar_value",
						   # "type" : "text",
						   # "text" : "0",
                           # "fontsize" : "LARGE",
						   # "x" : 40,
						    #"y" : 22,
					    #}
					),
				},
				{
					"name": "Menue",
					
					"x" : 0,
					"y" : 78,
					
					"width" : BOARD_WIDTH,
					"height" : 29,

					"style" : ("attach",),
					
					"children": 
					(
						{
							"name" : "img_category_underlay",
							"type" : "image",
							"style" : ("attach",),
							
							"image" : ACHIEVEMENTSYSTEM_PATH+"other/category_underlay.tga",
							"x" : 48,
							"y" : 0,
						},
						{
							"name": "category_menue_content",
							
							"x" : 0,
							"y" : 0,
							
							"width" : 643,
							"height" : 29,

							"style" : ("attach",),
							
							"children": 
							(
								{
									"name" : "btn_category_menue_content_0", 
									"type" : "radio_button",
									"text" : "menue_0",
									"x" : 78+1,
									"y" : 7,
									"default_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/left/btn_menue_left_norm.tga",
									"over_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/left/btn_menue_left_hover.tga",
									"down_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/left/btn_menue_left_press.tga",
								},
								{
									"name" : "btn_category_menue_content_1", 
									"type" : "radio_button",
									"text" : "menue_1",
									"x" : 170+1,
									"y" : 7,
									"default_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/mid/btn_menue_mid_norm.tga",
									"over_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/mid/btn_menue_mid_hover.tga",
									"down_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/mid/btn_menue_mid_press.tga",
								},
								{
									"name" : "btn_category_menue_content_2", 
									"type" : "radio_button",
									"text" : "menue_2",
									"x" : 270-2,
									"y" : 7,
									"default_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/mid/btn_menue_mid_norm.tga",
									"over_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/mid/btn_menue_mid_hover.tga",
									"down_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/mid/btn_menue_mid_press.tga",
								},
								{
									"name" : "btn_category_menue_content_3", 
									"type" : "radio_button",
									"text" : "menue_3",
									"x" : 370-4,
									"y" : 7,
									"default_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/mid/btn_menue_mid_norm.tga",
									"over_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/mid/btn_menue_mid_hover.tga",
									"down_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/mid/btn_menue_mid_press.tga",
								},
								{
									"name" : "btn_category_menue_content_4", 
									"type" : "radio_button",
									"text" : "menue_4",
									"x" : 470-6,
									"y" : 7,
									"default_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/mid/btn_menue_mid_norm.tga",
									"over_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/mid/btn_menue_mid_hover.tga",
									"down_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/mid/btn_menue_mid_press.tga",
								},
								{
									"name" : "btn_category_menue_content_5", 
									"type" : "radio_button",
									"text" : "menue_5",
									"x" : 567-6,
									"y" : 7,
									"default_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/right/btn_menue_right_norm.tga",
									"over_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/right/btn_menue_right_hover.tga",
									"down_image" : ACHIEVEMENTSYSTEM_PATH+"button/menue/right/btn_menue_right_press.tga",
								},
							),
						},
                        {
							"name" : "btn_arrow_left", 
							"type" : "button",
							"text" : "",
							"x" : 28,
							"y" : 9,
							"default_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/left/btn_arrow_left_norm.tga",
							"over_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/left/btn_arrow_left_hover.tga",
							"down_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/left/btn_arrow_left_press.tga",
						},
						{
							"name" : "btn_arrow_right", 
							"type" : "button",
							"text" : "",
							"x" : 690,
							"y" : 9,
							"default_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/right/btn_arrow_right_norm.tga",
							"over_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/right/btn_arrow_right_hover.tga",
							"down_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/right/btn_arrow_right_press.tga",
						},
					),
				},
				{
					"name": "content",
					
					"x" : 0,
					"y" : 105,
					
					"width" : BOARD_WIDTH,
					"height" : 378,

					"style" : ("attach",),
					
					"children": 
					(
						{
							"name": "overview_page",
							
							"x" : 0,
							"y" : 0,
							
							"width" : BOARD_WIDTH,
							"height" : 378,

							"style" : ("attach",),
							
							"children": 
							(
								{
									"name" : "img_overview_underlay",
									"type" : "image",
									"style" : ("attach",),
									
									"image" : ACHIEVEMENTSYSTEM_PATH+"overview/overview_underlay.tga",
									"x" : 59,
									"y" : 49,
								},
								{
									"name": "categorys_progress",
									
									"x" : 0,
									"y" : 0,
									
									"width" : BOARD_WIDTH,
									"height" : 200,

									"style" : ("attach",),
									
									"children": 
									(
										{
											"name": "categorys_progress_content",
											
											"x" : 0,
											"y" : 0,
											
											"width" : BOARD_WIDTH,
											"height" : 350,

											"style" : ("attach",),
											
											"children": 
											(
												{
													"name": "categorys_progress_content_0",
													
													"x" : 55,
													"y" : 28+35*0,
													
													"width" : 400,
													"height" : 36,

													"style" : ("attach",),
													
													"children": 
													(
														{
															"name" : "img_categorys_progress_content_title_0",
															"type" : "image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"other/title_underlay.tga",
															"x" : 0,
															"y" : 0,
															
															"children" :
															(
																{
																	"name" : "txt_categorys_progress_content_title_0",
																	"type" : "text",
																	"text" : "category_title_0",
																	"x" : 0,
																	"y" : 5,
																	"horizontal_align" : "center",
																	"text_horizontal_align" : "center",
																},
															),
														},
														{
															"name" : "img_categorys_progress_content_progressbar_empty_0",
															"type" : "image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_empty.tga",
															"x" : 4,
															"y" : 21,
														},
														{
															"name" : "eimg_categorys_progress_content_progressbar_full_0",
															"type" : "expanded_image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_full.tga",
															"x" : 5,
															"y" : 22,

															"width" : 384,
															"height" : 13,
														},
														 {
															 "name" : "img_categorys_progress_content_progressbar_full_completed_0",
															 "type" : "image",
															 "style" : ("attach",),
															
															 "image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_completed.tga",
															 "x" : 5,
															 "y" : 22,
															 "children" :
															 (
																 #{
																	# "name" : "txt_categorys_progress_content_progressbar_full_completed_title_0",
																	# "type" : "text",
																	# "text" : "COMPLETED",
																	# "x" : 0,
																	# "y" : 5,
																	# "horizontal_align" : "center",
																	# "text_horizontal_align" : "center",
																 #},
															 ),
														 },
                                                        ## not used but maybe later?
														#{
														#	"name" : "txt_categorys_progress_content_progressbar_title_0",
														#	"type" : "text",
														#	"text" : "progressbar_title_0",
														#	"x" : 40,
														#	"y" : 22,
														#},
													),
												},

                                                {
													"name": "categorys_progress_content_1",
													
													"x" : 55,
													"y" : 28+35*1,
													
													"width" : 400,
													"height" : 36,

													"style" : ("attach",),
													
													"children": 
													(
														{
															"name" : "img_categorys_progress_content_title_1",
															"type" : "image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"other/title_underlay.tga",
															"x" : 0,
															"y" : 0,
															
															"children" :
															(
																{
																	"name" : "txt_categorys_progress_content_title_1",
																	"type" : "text",
																	"text" : "category_title_1",
																	"x" : 0,
																	"y" : 5,
																	"horizontal_align" : "center",
																	"text_horizontal_align" : "center",
																},
															),
														},
														{
															"name" : "img_categorys_progress_content_progressbar_empty_1",
															"type" : "image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_empty.tga",
															"x" : 4,
															"y" : 21,
														},
														{
															"name" : "eimg_categorys_progress_content_progressbar_full_1",
															"type" : "expanded_image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_full.tga",
															"x" : 5,
															"y" : 22,

															"width" : 384,
															"height" : 13,
														},
														 {
															 "name" : "img_categorys_progress_content_progressbar_full_completed_1",
															 "type" : "image",
															 "style" : ("attach",),
															
															 "image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_completed.tga",
															 "x" : 5,
															 "y" : 22,
															 "children" :
															 (
																 #{
																	# "name" : "txt_categorys_progress_content_progressbar_full_completed_title_1",
																	# "type" : "text",
																	# "text" : "COMPLETED",
																	# "x" : 0,
																	# "y" : 5,
																	# "horizontal_align" : "center",
																	# "text_horizontal_align" : "center",
																 #},
															 ),
														 },
                                                        ## not used but maybe later?
														#{
														#	"name" : "txt_categorys_progress_content_progressbar_title_1",
														#	"type" : "text",
														#	"text" : "progressbar_title_1",
														#	"x" : 40,
														#	"y" : 22,
														#},
													),
												},

                                                {
													"name": "categorys_progress_content_2",
													
													"x" : 55,
													"y" : 28+35*2,
													
													"width" : 400,
													"height" : 36,

													"style" : ("attach",),
													
													"children": 
													(
														{
															"name" : "img_categorys_progress_content_title_2",
															"type" : "image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"other/title_underlay.tga",
															"x" : 0,
															"y" : 0,
															
															"children" :
															(
																{
																	"name" : "txt_categorys_progress_content_title_2",
																	"type" : "text",
																	"text" : "category_title_2",
																	"x" : 0,
																	"y" : 5,
																	"horizontal_align" : "center",
																	"text_horizontal_align" : "center",
																},
															),
														},
														{
															"name" : "img_categorys_progress_content_progressbar_empty_2",
															"type" : "image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_empty.tga",
															"x" : 4,
															"y" : 21,
														},
														{
															"name" : "eimg_categorys_progress_content_progressbar_full_2",
															"type" : "expanded_image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_full.tga",
															"x" : 5,
															"y" : 22,

															"width" : 384,
															"height" : 13,
														},
														 {
															 "name" : "img_categorys_progress_content_progressbar_full_completed_2",
															 "type" : "image",
															 "style" : ("attach",),
															
															 "image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_completed.tga",
															 "x" : 5,
															 "y" : 22,
															 "children" :
															 (
																 #{
																	# "name" : "txt_categorys_progress_content_progressbar_full_completed_title_2",
																	# "type" : "text",
																	# "text" : "COMPLETED",
																	# "x" : 0,
																	# "y" : 5,
																	# "horizontal_align" : "center",
																	# "text_horizontal_align" : "center",
																 #},
															 ),
														 },
                                                        ## not used but maybe later?
														#{
														#	"name" : "txt_categorys_progress_content_progressbar_title_2",
														#	"type" : "text",
														#	"text" : "progressbar_title_2",
														#	"x" : 40,
														#	"y" : 22,
														#},
													),
												},

                                                {
													"name": "categorys_progress_content_3",
													
													"x" : 55,
													"y" : 28+35*3,
													
													"width" : 400,
													"height" : 36,

													"style" : ("attach",),
													
													"children": 
													(
														{
															"name" : "img_categorys_progress_content_title_3",
															"type" : "image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"other/title_underlay.tga",
															"x" : 0,
															"y" : 0,
															
															"children" :
															(
																{
																	"name" : "txt_categorys_progress_content_title_3",
																	"type" : "text",
																	"text" : "category_title_3",
																	"x" : 0,
																	"y" : 5,
																	"horizontal_align" : "center",
																	"text_horizontal_align" : "center",
																},
															),
														},
														{
															"name" : "img_categorys_progress_content_progressbar_empty_3",
															"type" : "image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_empty.tga",
															"x" : 4,
															"y" : 21,
														},
														{
															"name" : "eimg_categorys_progress_content_progressbar_full_3",
															"type" : "expanded_image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_full.tga",
															"x" : 5,
															"y" : 22,

															"width" : 384,
															"height" : 13,
														},
														 {
															 "name" : "img_categorys_progress_content_progressbar_full_completed_3",
															 "type" : "image",
															 "style" : ("attach",),
															
															 "image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_completed.tga",
															 "x" : 5,
															 "y" : 22,
															 "children" :
															 (
																 #{
																	# "name" : "txt_categorys_progress_content_progressbar_full_completed_title_3",
																	# "type" : "text",
																	# "text" : "COMPLETED",
																	# "x" : 0,
																	# "y" : 5,
																	# "horizontal_align" : "center",
																	# "text_horizontal_align" : "center",
																 #},
															 ),
														 },
                                                        # not used but maybe later?
														#{
														#	"name" : "txt_categorys_progress_content_progressbar_title_3",
														#	"type" : "text",
														#	"text" : "progressbar_title_3",
														#	"x" : 40,
														#	"y" : 22,
														#},
													),
												},

                                                {
													"name": "categorys_progress_content_4",
													
													"x" : 55,
													"y" : 28+35*4,
													
													"width" : 400,
													"height" : 36,

													"style" : ("attach",),
													
													"children": 
													(
														{
															"name" : "img_categorys_progress_content_title_4",
															"type" : "image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"other/title_underlay.tga",
															"x" : 0,
															"y" : 0,
															
															"children" :
															(
																{
																	"name" : "txt_categorys_progress_content_title_4",
																	"type" : "text",
																	"text" : "category_title_4",
																	"x" : 0,
																	"y" : 5,
																	"horizontal_align" : "center",
																	"text_horizontal_align" : "center",
																},
															),
														},
														{
															"name" : "img_categorys_progress_content_progressbar_empty_4",
															"type" : "image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_empty.tga",
															"x" : 4,
															"y" : 21,
														},
														{
															"name" : "eimg_categorys_progress_content_progressbar_full_4",
															"type" : "expanded_image",
															"style" : ("attach",),
															
															"image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_full.tga",
															"x" : 5,
															"y" : 22,

															"width" : 384,
															"height" : 13,
														},
														 {
															 "name" : "img_categorys_progress_content_progressbar_full_completed_4",
															 "type" : "image",
															 "style" : ("attach",),
															
															 "image" : ACHIEVEMENTSYSTEM_PATH+"overview/categorys_progress_content_progressbar_completed.tga",
															 "x" : 5,
															 "y" : 22,
															 "children" :
															 (
																 #{
																	# "name" : "txt_categorys_progress_content_progressbar_full_completed_title_4",
																	# "type" : "text",
																	# "text" : "COMPLETED",
																	# "x" : 0,
																	# "y" : 5,
																	# "horizontal_align" : "center",
																	# "text_horizontal_align" : "center",
																 #},
															 ),
														 },
                                                        # not used but maybe later?
														#{
														#	"name" : "txt_categorys_progress_content_progressbar_title_4",
														#	"type" : "text",
														#	"text" : "progressbar_title_4",
														#	"x" : 40,
														#	"y" : 22,
														#},
													),
												},

											),
										},
									),
								},
                                {
									"name": "statistic",
									
									"x" : 55,
									"y" : 223,
									
									"width" : 391,
									"height" : 112,

									"style" : ("attach",),
									
									"children": 
									(
										{
											"name" : "img_statistic_title",
											"type" : "image",
											"style" : ("attach",),
															
											"image" : ACHIEVEMENTSYSTEM_PATH+"other/title_underlay.tga",
											"x" : 0,
											"y" : 0,
															
											"children" :
											(
												{
													"name" : "txt_statistic_title",
													"type" : "text",
													"text" : "Statistik",
													"x" : 0,
													"y" : 5,
													"horizontal_align" : "center",
													"text_horizontal_align" : "center",
												},
											),
										},
										{
											"name": "statistic_content",
											
											"x" : 0,
											"y" : 0,
											
											"width" : BOARD_WIDTH,
											"height" : 350,

											"style" : ("attach",),
											
											"children": 
											(
                                                {
											        "name": "statistic_content_0",
											
											        "x" : 15,
											        "y" : 35+25*0,
											
											        "width" : 200,
											        "height" : 25,

											        "style" : ("attach",),
											
											        "children": 
											        (
                                                        {
													        "name" : "txt_statistic_content_title_0",
													        "type" : "text",
													        "text" : "statistic_0",
													        "x" : 0,
													        "y" : 0,
												        },
                                                        {
													        "name" : "txt_statistic_content_value_0",
													        "type" : "text",
													        "text" : "0",
													        "x" : 140,
													        "y" : 0,
												        },
                                                    ),
                                                },
                                                {
											        "name": "statistic_content_1",
											
											        "x" : 15,
											        "y" : 35+25*1,
											
											        "width" : 200,
											        "height" : 25,

											        "style" : ("attach",),
											
											        "children": 
											        (
                                                        {
													        "name" : "txt_statistic_content_title_1",
													        "type" : "text",
													        "text" : "statistic_1",
													        "x" : 0,
													        "y" : 0,
												        },
                                                        {
													        "name" : "txt_statistic_content_value_1",
													        "type" : "text",
													        "text" : "0",
													        "x" : 140,
													        "y" : 0,
												        },
                                                    ),
                                                },
                                                {
											        "name": "statistic_content_2",
											
											        "x" : 15,
											        "y" : 35+25*2,
											
											        "width" : 200,
											        "height" : 25,

											        "style" : ("attach",),
											
											        "children": 
											        (
                                                        {
													        "name" : "txt_statistic_content_title_2",
													        "type" : "text",
													        "text" : "statistic_2",
													        "x" : 0,
													        "y" : 0,
												        },
                                                        {
													        "name" : "txt_statistic_content_value_2",
													        "type" : "text",
													        "text" : "0",
													        "x" : 140,
													        "y" : 0,
												        },
                                                    ),
                                                },
											    {
											        "name": "statistic_content_achievementpoints",
											
											        "x" : 233,
											        "y" : 29,
											
											        "width" : 147,
											        "height" : 73,

											        "style" : ("attach",),
											
											        "children": 
											        (
                                                        {
													        "name" : "txt_statistic_content_achievementpoints_title",
													        "type" : "text",
													        "text" : "Achievementpunkte",
													        "x" : 24,
													        "y" : 0,
												        },
                                                        {
													        "name" : "txt_statistic_content_achievementpoints_value",
													        "type" : "text",
													        "text" : "0",
                                                            "fontsize" : "LARGE",
                                                            "horizontal_align" : "center",
															"text_horizontal_align" : "center",
													        "x" : 0,
													        "y" : 35,
												        },
                                                    ),
                                                },
                                            ),
                                        },
                                    ),
                                },
								{
							        "name" : "btn_categorys_arrow_up", 
							        "type" : "button",
							        "text" : "",
							        "x" : 260,
							        "y" : 20,
							        "default_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/up/btn_arrow_up_norm.tga",
							        "over_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/up/btn_arrow_up_hover.tga",
							        "down_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/up/btn_arrow_up_press.tga",
						        },
                                {
							        "name" : "btn_categorys_arrow_down", 
							        "type" : "button",
							        "text" : "",
							        "x" : 260,
							        "y" : 220,
							        "default_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/down/btn_arrow_down_norm.tga",
							        "over_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/down/btn_arrow_down_hover.tga",
							        "down_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/down/btn_arrow_down_press.tga",
						        },
                                {
									"name": "recent_tasks_done",
											
									"x" : 463,
									"y" : 26,
											
									"width" : 197,
									"height" : 310,

									"style" : ("attach",),
											
									"children": 
									(
                                        {
											"name" : "img_recent_tasks_done_title",
											"type" : "image",
											"style" : ("attach",),
															
											"image" : ACHIEVEMENTSYSTEM_PATH+"other/title_underlay.tga",
											"x" : 50,
											"y" : 0,
															
											"children" :
											(
												{
													"name" : "txt_recent_tasks_done_title",
													"type" : "text",
													"text" : "Kürzlich erledigt",
													"x" : 0,
													"y" : 5,
													"horizontal_align" : "center",
													"text_horizontal_align" : "center",
												},
											),
										},
                                        {
											"name": "recent_tasks_done_content",
											
											"x" : 0,
											"y" : 0,
											
											"width" : BOARD_WIDTH,
											"height" : 350,

											"style" : ("attach",),
											
											"children": 
											(
												{
													"name": "recent_tasks_done_content_0",
													
													"x" : 15,
													"y" : 52+39*0,
													
													"width" : 177,
													"height" : 39,

													"style" : ("attach",),
													
													"children":
                                                    (
                                                        {
											                "name" : "img_recent_tasks_done_title_0",
											                "type" : "image",
											                "style" : ("attach",),
															
											                "image" : ACHIEVEMENTSYSTEM_PATH+"overview/recent_tasks_done_content_achievement_done_underlay.tga",
											                "x" : 0,
											                "y" : 0,

                                                            "children" : 
                                                            (
                                                                {
													                "name" : "txt_recent_tasks_done_content_task_title_0",
													                "type" : "text",
													                "text" : "task_title_0",
                                                                    "horizontal_align" : "center",
															        "text_horizontal_align" : "center",
													                "x" : 0,
													                "y" : 9,
												                },
                                                                {
													                "name" : "txt_recent_tasks_done_content_task_value_0",
													                "type" : "text",
													                "text" : "+0",
													                "x" : 153,
													                "y" : 7,
												                },
                                                            ),
                                                        },
                                                    ),
                                                },

                                                {
													"name": "recent_tasks_done_content_1",
													
													"x" : 15,
													"y" : 52+39*1,
													
													"width" : 177,
													"height" : 39,

													"style" : ("attach",),
													
													"children":
                                                    (
                                                        {
											                "name" : "img_recent_tasks_done_title_1",
											                "type" : "image",
											                "style" : ("attach",),
															
											                "image" : ACHIEVEMENTSYSTEM_PATH+"overview/recent_tasks_done_content_achievement_done_underlay.tga",
											                "x" : 0,
											                "y" : 0,

                                                            "children" : 
                                                            (
                                                                {
													                "name" : "txt_recent_tasks_done_content_task_title_1",
													                "type" : "text",
													                "text" : "task_title_1",
                                                                    "horizontal_align" : "center",
															        "text_horizontal_align" : "center",
													                "x" : 0,
													                "y" : 9,
												                },
                                                                {
													                "name" : "txt_recent_tasks_done_content_task_value_1",
													                "type" : "text",
													                "text" : "+0",
													                "x" : 153,
													                "y" : 7,
												                },
                                                            ),
                                                        },
                                                    ),
                                                },

                                                {
													"name": "recent_tasks_done_content_2",
													
													"x" : 15,
													"y" : 52+39*2,
													
													"width" : 177,
													"height" : 39,

													"style" : ("attach",),
													
													"children":
                                                    (
                                                        {
											                "name" : "img_recent_tasks_done_title_2",
											                "type" : "image",
											                "style" : ("attach",),
															
											                "image" : ACHIEVEMENTSYSTEM_PATH+"overview/recent_tasks_done_content_achievement_done_underlay.tga",
											                "x" : 0,
											                "y" : 0,

                                                            "children" : 
                                                            (
                                                                {
													                "name" : "txt_recent_tasks_done_content_task_title_2",
													                "type" : "text",
													                "text" : "task_title_2",
                                                                    "horizontal_align" : "center",
															        "text_horizontal_align" : "center",
													                "x" : 0,
													                "y" : 9,
												                },
                                                                {
													                "name" : "txt_recent_tasks_done_content_task_value_2",
													                "type" : "text",
													                "text" : "+0",
													                "x" : 153,
													                "y" : 7,
												                },
                                                            ),
                                                        },
                                                    ),
                                                },

                                                {
													"name": "recent_tasks_done_content_3",
													
													"x" : 15,
													"y" : 52+39*3,
													
													"width" : 177,
													"height" : 39,

													"style" : ("attach",),
													
													"children":
                                                    (
                                                        {
											                "name" : "img_recent_tasks_done_title_3",
											                "type" : "image",
											                "style" : ("attach",),
															
											                "image" : ACHIEVEMENTSYSTEM_PATH+"overview/recent_tasks_done_content_achievement_done_underlay.tga",
											                "x" : 0,
											                "y" : 0,

                                                            "children" : 
                                                            (
                                                                {
													                "name" : "txt_recent_tasks_done_content_task_title_3",
													                "type" : "text",
													                "text" : "task_title_3",
                                                                    "horizontal_align" : "center",
															        "text_horizontal_align" : "center",
													                "x" : 0,
													                "y" : 9,
												                },
                                                                {
													                "name" : "txt_recent_tasks_done_content_task_value_3",
													                "type" : "text",
													                "text" : "+0",
													                "x" : 153,
													                "y" : 7,
												                },
                                                            ),
                                                        },
                                                    ),
                                                },

                                                {
													"name": "recent_tasks_done_content_4",
													
													"x" : 15,
													"y" : 52+39*4,
													
													"width" : 177,
													"height" : 39,

													"style" : ("attach",),
													
													"children":
                                                    (
                                                        {
											                "name" : "img_recent_tasks_done_title_4",
											                "type" : "image",
											                "style" : ("attach",),
															
											                "image" : ACHIEVEMENTSYSTEM_PATH+"overview/recent_tasks_done_content_achievement_done_underlay.tga",
											                "x" : 0,
											                "y" : 0,

                                                            "children" : 
                                                            (
                                                                {
													                "name" : "txt_recent_tasks_done_content_task_title_4",
													                "type" : "text",
													                "text" : "task_title_4",
                                                                    "horizontal_align" : "center",
															        "text_horizontal_align" : "center",
													                "x" : 0,
													                "y" : 9,
												                },
                                                                {
													                "name" : "txt_recent_tasks_done_content_task_value_4",
													                "type" : "text",
													                "text" : "+0",
													                "x" : 153,
													                "y" : 7,
												                },
                                                            ),
                                                        },
                                                    ),
                                                },

                                                {
													"name": "recent_tasks_done_content_5",
													
													"x" : 15,
													"y" : 52+39*5,
													
													"width" : 177,
													"height" : 39,

													"style" : ("attach",),
													
													"children":
                                                    (
                                                        {
											                "name" : "img_recent_tasks_done_title_5",
											                "type" : "image",
											                "style" : ("attach",),
															
											                "image" : ACHIEVEMENTSYSTEM_PATH+"overview/recent_tasks_done_content_achievement_done_underlay.tga",
											                "x" : 0,
											                "y" : 0,

                                                            "children" : 
                                                            (
                                                                {
													                "name" : "txt_recent_tasks_done_content_task_title_5",
													                "type" : "text",
													                "text" : "task_title_5",
                                                                    "horizontal_align" : "center",
															        "text_horizontal_align" : "center",
													                "x" : 0,
													                "y" : 9,
												                },
                                                                {
													                "name" : "txt_recent_tasks_done_content_task_value_5",
													                "type" : "text",
													                "text" : "+0",
													                "x" : 153,
													                "y" : 7,
												                },
                                                            ),
                                                        },
                                                    ),
                                                },
                                            ),
                                        },
                                        {
							                "name" : "btn_arrow_up", 
							                "type" : "button",
							                "text" : "",
							                "x" : 100,
							                "y" : 33,
							                "default_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/up/btn_arrow_up_norm.tga",
							                "over_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/up/btn_arrow_up_hover.tga",
							                "down_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/up/btn_arrow_up_press.tga",
						                },
                                        {
							                "name" : "btn_arrow_down", 
							                "type" : "button",
							                "text" : "",
							                "x" : 100,
							                "y" : 291,
							                "default_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/down/btn_arrow_down_norm.tga",
							                "over_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/down/btn_arrow_down_hover.tga",
							                "down_image" : ACHIEVEMENTSYSTEM_PATH+"button/arrows/down/btn_arrow_down_press.tga",
						                },
                                    ),
                                },
							),
						},

						{
							"name": "tasks_page",
							
							"x" : 0,
							"y" : 0,
							
							"width" : BOARD_WIDTH,
							"height" : 378,

							"style" : ("attach",),
							
							"children": 
							(
								{
									"name" : "img_tasks_page_underlay",
									"type" : "image",
									"style" : ("attach",),
									
									"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_page_underlay.tga",
									"x" : 71,
									"y" : 25,
								},
								{
									"name" : "btn_tasks_page_change_state_all", 
									"type" : "radio_button",
									"text" : "Alle",
									"x" : 83+117*0,
									"y" : 35,
									"default_image" : ACHIEVEMENTSYSTEM_PATH+"button/title_flag/btn_title_flag_norm.tga",
									"over_image" : ACHIEVEMENTSYSTEM_PATH+"button/title_flag/btn_title_flag_hover.tga",
									"down_image" : ACHIEVEMENTSYSTEM_PATH+"button/title_flag/btn_title_flag_press.tga",
								},
								{
									"name" : "btn_tasks_page_change_state_pending", 
									"type" : "radio_button",
									"text" : "Ausstehend",
									"x" : 83+117*1,
									"y" : 35,
									"default_image" : ACHIEVEMENTSYSTEM_PATH+"button/title_flag/btn_title_flag_norm.tga",
									"over_image" : ACHIEVEMENTSYSTEM_PATH+"button/title_flag/btn_title_flag_hover.tga",
									"down_image" : ACHIEVEMENTSYSTEM_PATH+"button/title_flag/btn_title_flag_press.tga",
								},
								{
									"name" : "btn_tasks_page_change_state_done", 
									"type" : "radio_button",
									"text" : "Erledigt",
									"x" : 83+117*2,
									"y" : 35,
									"default_image" : ACHIEVEMENTSYSTEM_PATH+"button/title_flag/btn_title_flag_norm.tga",
									"over_image" : ACHIEVEMENTSYSTEM_PATH+"button/title_flag/btn_title_flag_hover.tga",
									"down_image" : ACHIEVEMENTSYSTEM_PATH+"button/title_flag/btn_title_flag_press.tga",
								},
								{
									"name": "tasks_page_content",
							
									"x" : 88,
									"y" : 60,
							
									"width" : 554,
									"height" : 236,

									"style" : ("attach",),
							
									"children": 
									(
										{
											"name": "tasks_page_content_0",
							
											"x" : 0,
											"y" : 0+30*0,
							
											"width" : 554,
											"height" : 30,

											"style" : ("attach",),
							
											"children": 
											(
												{
													"name" : "img_tasks_page_content_progressbar_empty_0",
													"type" : "image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_empty.tga",
													"x" : 0,
													"y" : 4,
												},
												{
													"name" : "eimg_tasks_page_content_progressbar_full_0",
													"type" : "expanded_image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_full.tga",
													"x" : 1,
													"y" : 4,

													"width" : 384,
													"height" : 13,
												},
												 {
													 "name" : "img_tasks_page_content_progressbar_full_completed_0",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_completed.tga",
													 "x" : 1,
													 "y" : 4,
													 "children" :
													 (
														 #{
															# "name" : "txt_tasks_page_content_progressbar_full_completed_title_0",
															# "type" : "text",
															# "text" : "COMPLETED",
															# "x" : 0,
															# "y" : 5,
															# "horizontal_align" : "center",
															# "text_horizontal_align" : "center",
														 #},
													 ),
												 },
												{
													 "name" : "txt_tasks_page_content_progressbar_title_0",
													 "type" : "text",
													 "text" : "title_0",
													 "x" : 30,
													 "y" : 10,
												},
												{
													 "name" : "img_tasks_page_content_progressbar_flag_0",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progessbar_flag.tga",
													 "x" : 522,
													 "y" : 4,
													 "children" :
													 (
														 {
															 "name" : "txt_tasks_page_content_progressbar_flag_value_0",
															 "type" : "text",
															 "text" : "0",
															 "x" : 0,
															 "y" : 5,
															 "horizontal_align" : "center",
															 "text_horizontal_align" : "center",
														 },
													 ),
												},
											),
										},

										{
											"name": "tasks_page_content_1",
							
											"x" : 0,
											"y" : 0+30*1,
							
											"width" : 554,
											"height" : 30,

											"style" : ("attach",),
							
											"children": 
											(
												{
													"name" : "img_tasks_page_content_progressbar_empty_1",
													"type" : "image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_empty.tga",
													"x" : 0,
													"y" : 4,
												},
												{
													"name" : "eimg_tasks_page_content_progressbar_full_1",
													"type" : "expanded_image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_full.tga",
													"x" : 1,
													"y" : 4,

													"width" : 384,
													"height" : 13,
												},
												 {
													 "name" : "img_tasks_page_content_progressbar_full_completed_1",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_completed.tga",
													 "x" : 1,
													 "y" : 4,
													 "children" :
													 (
														 #{
															# "name" : "txt_tasks_page_content_progressbar_full_completed_title_1",
															# "type" : "text",
															# "text" : "COMPLETED",
															# "x" : 0,
															# "y" : 5,
															# "horizontal_align" : "center",
															# "text_horizontal_align" : "center",
														 #},
													 ),
												 },
												{
													 "name" : "txt_tasks_page_content_progressbar_title_1",
													 "type" : "text",
													 "text" : "title_1",
													 "x" : 30,
													 "y" : 10,
												},
												{
													 "name" : "img_tasks_page_content_progressbar_flag_1",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progessbar_flag.tga",
													 "x" : 522,
													 "y" : 4,
													 "children" :
													 (
														 {
															 "name" : "txt_tasks_page_content_progressbar_flag_value_1",
															 "type" : "text",
															 "text" : "0",
															 "x" : 0,
															 "y" : 5,
															 "horizontal_align" : "center",
															 "text_horizontal_align" : "center",
														 },
													 ),
												},
											),
										},
										{
											"name": "tasks_page_content_2",
							
											"x" : 0,
											"y" : 0+30*2,
							
											"width" : 554,
											"height" : 30,

											"style" : ("attach",),
							
											"children": 
											(
												{
													"name" : "img_tasks_page_content_progressbar_empty_2",
													"type" : "image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_empty.tga",
													"x" : 0,
													"y" : 4,
												},
												{
													"name" : "eimg_tasks_page_content_progressbar_full_2",
													"type" : "expanded_image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_full.tga",
													"x" : 1,
													"y" : 4,

													"width" : 384,
													"height" : 13,
												},
												 {
													 "name" : "img_tasks_page_content_progressbar_full_completed_2",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_completed.tga",
													 "x" : 1,
													 "y" : 4,
													 "children" :
													 (
														 #{
															# "name" : "txt_tasks_page_content_progressbar_full_completed_title_2",
															# "type" : "text",
															# "text" : "COMPLETED",
															# "x" : 0,
															# "y" : 5,
															# "horizontal_align" : "center",
															# "text_horizontal_align" : "center",
														 #},
													 ),
												 },
												{
													 "name" : "txt_tasks_page_content_progressbar_title_2",
													 "type" : "text",
													 "text" : "title_2",
													 "x" : 30,
													 "y" : 10,
												},
												{
													 "name" : "img_tasks_page_content_progressbar_flag_2",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progessbar_flag.tga",
													 "x" : 522,
													 "y" : 4,
													 "children" :
													 (
														 {
															 "name" : "txt_tasks_page_content_progressbar_flag_value_2",
															 "type" : "text",
															 "text" : "0",
															 "x" : 0,
															 "y" : 5,
															 "horizontal_align" : "center",
															 "text_horizontal_align" : "center",
														 },
													 ),
												},
											),
										},
										{
											"name": "tasks_page_content_3",
							
											"x" : 0,
											"y" : 0+30*3,
							
											"width" : 554,
											"height" : 30,

											"style" : ("attach",),
							
											"children": 
											(
												{
													"name" : "img_tasks_page_content_progressbar_empty_3",
													"type" : "image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_empty.tga",
													"x" : 0,
													"y" : 4,
												},
												{
													"name" : "eimg_tasks_page_content_progressbar_full_3",
													"type" : "expanded_image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_full.tga",
													"x" : 1,
													"y" : 4,

													"width" : 384,
													"height" : 13,
												},
												 {
													 "name" : "img_tasks_page_content_progressbar_full_completed_3",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_completed.tga",
													 "x" : 1,
													 "y" : 4,
													 "children" :
													 (
														 #{
															# "name" : "txt_tasks_page_content_progressbar_full_completed_title_3",
															# "type" : "text",
															# "text" : "COMPLETED",
															# "x" : 0,
															# "y" : 5,
															# "horizontal_align" : "center",
															# "text_horizontal_align" : "center",
														 #},
													 ),
												 },
												{
													 "name" : "txt_tasks_page_content_progressbar_title_3",
													 "type" : "text",
													 "text" : "title_3",
													 "x" : 30,
													 "y" : 10,
												},
												{
													 "name" : "img_tasks_page_content_progressbar_flag_3",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progessbar_flag.tga",
													 "x" : 522,
													 "y" : 4,
													 "children" :
													 (
														 {
															 "name" : "txt_tasks_page_content_progressbar_flag_value_3",
															 "type" : "text",
															 "text" : "0",
															 "x" : 0,
															 "y" : 5,
															 "horizontal_align" : "center",
															 "text_horizontal_align" : "center",
														 },
													 ),
												},
											),
										},
										{
											"name": "tasks_page_content_4",
							
											"x" : 0,
											"y" : 0+30*4,
							
											"width" : 554,
											"height" : 30,

											"style" : ("attach",),
							
											"children": 
											(
												{
													"name" : "img_tasks_page_content_progressbar_empty_4",
													"type" : "image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_empty.tga",
													"x" : 0,
													"y" : 4,
												},
												{
													"name" : "eimg_tasks_page_content_progressbar_full_4",
													"type" : "expanded_image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_full.tga",
													"x" : 1,
													"y" : 4,

													"width" : 384,
													"height" : 13,
												},
												 {
													 "name" : "img_tasks_page_content_progressbar_full_completed_4",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_completed.tga",
													 "x" : 1,
													 "y" : 4,
													 "children" :
													 (
														 #{
															# "name" : "txt_tasks_page_content_progressbar_full_completed_title_4",
															# "type" : "text",
															# "text" : "COMPLETED",
															# "x" : 0,
															# "y" : 5,
															# "horizontal_align" : "center",
															# "text_horizontal_align" : "center",
														 #},
													 ),
												 },
												{
													 "name" : "txt_tasks_page_content_progressbar_title_4",
													 "type" : "text",
													 "text" : "title_4",
													 "x" : 30,
													 "y" : 10,
												},
												{
													 "name" : "img_tasks_page_content_progressbar_flag_4",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progessbar_flag.tga",
													 "x" : 522,
													 "y" : 4,
													 "children" :
													 (
														 {
															 "name" : "txt_tasks_page_content_progressbar_flag_value_4",
															 "type" : "text",
															 "text" : "0",
															 "x" : 0,
															 "y" : 5,
															 "horizontal_align" : "center",
															 "text_horizontal_align" : "center",
														 },
													 ),
												},
											),
										},
										{
											"name": "tasks_page_content_5",
							
											"x" : 0,
											"y" : 0+30*5,
							
											"width" : 554,
											"height" : 30,

											"style" : ("attach",),
							
											"children": 
											(
												{
													"name" : "img_tasks_page_content_progressbar_empty_5",
													"type" : "image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_empty.tga",
													"x" : 0,
													"y" : 4,
												},
												{
													"name" : "eimg_tasks_page_content_progressbar_full_5",
													"type" : "expanded_image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_full.tga",
													"x" : 1,
													"y" : 4,

													"width" : 384,
													"height" : 13,
												},
												 {
													 "name" : "img_tasks_page_content_progressbar_full_completed_5",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_completed.tga",
													 "x" : 1,
													 "y" : 4,
													 "children" :
													 (
														 #{
															# "name" : "txt_tasks_page_content_progressbar_full_completed_title_5",
															# "type" : "text",
															# "text" : "COMPLETED",
															# "x" : 0,
															# "y" : 5,
															# "horizontal_align" : "center",
															# "text_horizontal_align" : "center",
														 #},
													 ),
												 },
												{
													 "name" : "txt_tasks_page_content_progressbar_title_5",
													 "type" : "text",
													 "text" : "title_5",
													 "x" : 30,
													 "y" : 10,
												},
												{
													 "name" : "img_tasks_page_content_progressbar_flag_5",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progessbar_flag.tga",
													 "x" : 522,
													 "y" : 4,
													 "children" :
													 (
														 {
															 "name" : "txt_tasks_page_content_progressbar_flag_value_5",
															 "type" : "text",
															 "text" : "0",
															 "x" : 0,
															 "y" : 5,
															 "horizontal_align" : "center",
															 "text_horizontal_align" : "center",
														 },
													 ),
												},
											),
										},

										{
											"name": "tasks_page_content_6",
							
											"x" : 0,
											"y" : 0+30*6,
							
											"width" : 554,
											"height" : 30,

											"style" : ("attach",),
							
											"children": 
											(
												{
													"name" : "img_tasks_page_content_progressbar_empty_6",
													"type" : "image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_empty.tga",
													"x" : 0,
													"y" : 4,
												},
												{
													"name" : "eimg_tasks_page_content_progressbar_full_6",
													"type" : "expanded_image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_full.tga",
													"x" : 1,
													"y" : 4,

													"width" : 384,
													"height" : 13,
												},
												 {
													 "name" : "img_tasks_page_content_progressbar_full_completed_6",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_completed.tga",
													 "x" : 1,
													 "y" : 4,
													 "children" :
													 (
														 #{
															# "name" : "txt_tasks_page_content_progressbar_full_completed_title_6",
															# "type" : "text",
															# "text" : "COMPLETED",
															# "x" : 0,
															# "y" : 5,
															# "horizontal_align" : "center",
															# "text_horizontal_align" : "center",
														 #},
													 ),
												 },
												{
													 "name" : "txt_tasks_page_content_progressbar_title_6",
													 "type" : "text",
													 "text" : "title_6",
													 "x" : 30,
													 "y" : 10,
												},
												{
													 "name" : "img_tasks_page_content_progressbar_flag_6",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progessbar_flag.tga",
													 "x" : 522,
													 "y" : 4,
													 "children" :
													 (
														 {
															 "name" : "txt_tasks_page_content_progressbar_flag_value_6",
															 "type" : "text",
															 "text" : "0",
															 "x" : 0,
															 "y" : 5,
															 "horizontal_align" : "center",
															 "text_horizontal_align" : "center",
														 },
													 ),
												},
											),
										},

										{
											"name": "tasks_page_content_7",
							
											"x" : 0,
											"y" : 0+30*7,
							
											"width" : 554,
											"height" : 30,

											"style" : ("attach",),
							
											"children": 
											(
												{
													"name" : "img_tasks_page_content_progressbar_empty_7",
													"type" : "image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_empty.tga",
													"x" : 0,
													"y" : 4,
												},
												{
													"name" : "eimg_tasks_page_content_progressbar_full_7",
													"type" : "expanded_image",
													"style" : ("attach",),
															
													"image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_full.tga",
													"x" : 1,
													"y" : 4,

													"width" : 384,
													"height" : 13,
												},
												 {
													 "name" : "img_tasks_page_content_progressbar_full_completed_7",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progressbar_completed.tga",
													 "x" : 1,
													 "y" : 4,
													 "children" :
													 (
														 #{
															# "name" : "txt_tasks_page_content_progressbar_full_completed_title_7",
															# "type" : "text",
															# "text" : "COMPLETED",
															# "x" : 0,
															# "y" : 5,
															# "horizontal_align" : "center",
															# "text_horizontal_align" : "center",
														 #},
													 ),
												 },
												{
													 "name" : "txt_tasks_page_content_progressbar_title_7",
													 "type" : "text",
													 "text" : "title_7",
													 "x" : 30,
													 "y" : 10,
												},
												{
													 "name" : "img_tasks_page_content_progressbar_flag_7",
													 "type" : "image",
													 "style" : ("attach",),
															
													 "image" : ACHIEVEMENTSYSTEM_PATH+"tasks/tasks_content_progessbar_flag.tga",
													 "x" : 522,
													 "y" : 4,
													 "children" :
													 (
														 {
															 "name" : "txt_tasks_page_content_progressbar_flag_value_7",
															 "type" : "text",
															 "text" : "0",
															 "x" : 0,
															 "y" : 5,
															 "horizontal_align" : "center",
															 "text_horizontal_align" : "center",
														 },
													 ),
												},
											),
										},
									),
								},
								{
									"name" : "scrollbar_tasks_page_content",
									"type" : "scrollbar",

									"x" : 645,
									"y" : 33,

									"size" : 288,
								},
							),
						},
					),
				},
				
			),
		},
	),
}