import uiScriptLocale
import apollo_interface

default_x = 541-107
default_y = 370
ICON_SLOT_FILE = apollo_interface.PATCH_COMMON+"/slot_ellipse/slot.png"


window = {
	"name" : "CharacterWindow",
	"style" : ("movable", "float",),
	"x" : 24,
	"y" : (SCREEN_HEIGHT - 37 - 361) / 2,
	"width" : default_x,
	"height" : default_y,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board2",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width"  : default_x,
			"height" : default_y,
			"children":
			(
				{
					"name" : "Guild_Page",
					"type" : "window",
					"style" : ("attach",),
					"x" : 0,
					"y" : 0,
					"width" : default_x,
					"height" : default_y,
					"children" :
					(
						## Title Area
						{
							"name" : "Guild_TitleBar", "type" : "titlebar", "x" : 8, "y" : 7, "width" : default_x-20, "color" : "red",
							"children" :
							(
								{ "name" : "ButtonCollapse", "type" : "button", "x":321+20, "y":5, "default_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_expand_01_normal.png", "over_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_expand_02_hover.png", "down_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_expand_03_active.png", },
								{ "name" : "ButtonExpande", "type" : "button", "x":321, "y":5, "default_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_collapse_01_normal.png", "over_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_collapse_02_hover.png", "down_image" : apollo_interface.PATCH_BUTTONS+"/titlebar_collapse_03_active.png", },
								{ "name" : "TitleName", "type":"text", "x":0, "y":-11, "text":apollo_interface.GUILD_TITLE, "color":0xffcaa76f, "all_align":"center" },
							),
						},

						{"name":"Guild_Input", "type":"new_board", "x":13+367, "y":35, "width":143-110, "height":323},

						{
							"name":"Guild_Status", "type":"window", "x":10, "y":36, "width":372, "height":350,
							"children" :
							(
									{
										"name":"Board1",
										"type":"new_board",

										"x":0,
										"y":0,

										"width" : 325+43,
										"height": 100,
										"children":

										(
											## GuildName
											{
												"name" : "GuildName", "type" : "text", "x" : 30, "y" : 25,
												"children" :
												(
													{
														"name" : "GuildNameSlot",
														"type" : "image",
														"x" : 70,
														"y" : -7,
														"image" : apollo_interface.PATCH_SPECIAL + "/guild/chenar1.png",
														"children" :
														(
															{"name" : "GuildNameValue", "type":"text", "text":uiScriptLocale.GUILD_INFO_NAME_VALUE, "x":50, "y":6, "color" : 0xffa07970, "text_horizontal_align":"center"},
														),
													},
												),
											},

											## GuildMaster
											{
												"name" : "GuildMaster", "type" : "window", "x" : 140, "y" : 25, "width" : 100, "height" : 50,
												"children" :
												(
													{
														"name" : "GuildMasterNameSlot",
														"type" : "text",
														"x" : 80,
														"y" : -7,

														"children" :
														(

															{"name" : "GuildMaster", "type" : "image", "x" : -7, "y" : 0, "image" : apollo_interface.PATCH_SPECIAL_1 + "/leader.png" },
															{"name" : "GuildMasterBar", "type" : "image", "x" : 20, "y" : 0, "image" : apollo_interface.PATCH_SPECIAL + "/guild/chenar1.png" },
															{"name" : "GuildMasterNameValue", "type":"text", "text":uiScriptLocale.GUILD_INFO_MASTER_VALUE, "x":65, "y":6, "color" : 0xffa07970, "text_horizontal_align":"center"},

														),
													},
												),
											},


											## LargeGuildMark
											{
												"name" : "GuildMark",
												"type" : "button",
												"x" : 15,
												"y" : 12,
												"width" : 48+1,
												"height" : 36+1,

												"default_image" : apollo_interface.PATCH_SPECIAL + "/guild/guildicon_slot.png",
												"over_image" : apollo_interface.PATCH_SPECIAL + "/guild/guildicon_slot.png",
												"down_image" : apollo_interface.PATCH_SPECIAL + "/guild/guildicon_slot.png",
												
												"children" :
												(
													{
														"name" : "LargeGuildMark",
														"type" : "mark",
														"x" : 10,
														"y" : 10,
													},

													{
														"name":"LevelSlot",
														"type":"image",
														"x":47,
														"y":38,
														"image":apollo_interface.PATCH_COMMON+"/input/level_round.png",
														"children":
														(
															{ "name":"GuildLevelValue","type":"text","text":"99", "color" : 0xfff8d090, "x":1,"y":-1,"all_align":"center",},
														),
													}
												),
											},
											#exp
											{
												"name" : "Experience",
												"type" : "window",

												"x" : 0,
												"y" : 7,

												"width" : 48+1,
												"height" : 36+1,

												"children" :
												(

													{
														"name":"PercentExp",
														"type":"text",

														"x":100,
														"y":15*3,

														"text":"100.00%",
														"color" : 0xfff8d090,

													},

													## CurrentExperience

													{
														"name" : "CurrentExperience", "type" : "text", "x" : 36*5, "y" : 15*3, "color" : 0xffa08784, "text" : "",
														"children" :
														(
															{
																"name" : "CurrentExperienceSlot",
																"type" : "text",
																"x" : 55,
																"y" : 6,
																# "image" : LARGE_VALUE_FILE,
																"children" :
																(
																	{"name" : "CurrentExperienceValue", "type":"text", "text":"10000000", "x":0, "y":0, "color" : 0xffa08784, "all_align":"center"},
																),
															},
														),
													},



													{
														"name":"ExpImgEmpty",
														"type":"image",
														"x":95,
														"y":60,
														"image": apollo_interface.PATCH_SPECIAL+"/character/exp_gauge_empty.png",
													},

													{
														"name":"ExpImgFull",
														"type":"expanded_image",
														"x":95,
														"y":60,
														"image": apollo_interface.PATCH_SPECIAL+"/character/exp_gauge_full.png",
													},
												),
											},
										),
									},

									{
										"name":"Board2",
										"type":"new_board",

										"x":0,
										"y":101,

										"width" : 325+43,
										"height": 85,
										"children":

										(
											## GuildMemberCount
											{
												"name" : "GuildMemberCount", "type" : "text", "x" : 30, "y" : 20, "color" : 0xffa08784, "text" : uiScriptLocale.GUILD_INFO_MEMBER_NUM,
												"children" :
												(
													{
														"name" : "GuildMemberCountSlot",
														"type" : "image",
														"x" : 90,
														"y" : -6,
														"image" : apollo_interface.PATCH_SPECIAL + "/guild/member.png",
														"children" :
														(
															{"name" : "GuildMemberCountValue", "type":"text", "text":"30 / 32", "x":0, "y":0, "color" : 0xffa07970, "all_align":"center"},
														),
													},
												),
											},

											## GuildMemberLevelAverage
											{
												"name" : "GuildMemberLevelAverage", "type" : "text", "x" : 30, "y" : 50, "color" : 0xffa08784, "text" : uiScriptLocale.GUILD_INFO_MEMBER_AVG_LEVEL,
												"children" :
												(
													{
														"name" : "GuildMemberLevelAverageSlot",
														"type" : "image",
														"x" : 115,
														"y" : -6,
														"image" :  apollo_interface.PATCH_SPECIAL + "/guild/g_level.png",
														"children" :
														(
															{"name" : "GuildMemberLevelAverageValue", "type":"text", "text":"53", "color" :  0xffa07970, "x":0, "y":0, "all_align":"center"},
														),
													},
												),
											},

											{
												"name" : "GuildDonateWindow",
												"type" : "image",
												"x" : 225,
												"y" : 2,
												"image" : apollo_interface.PATCH_SPECIAL + "/guild/button_slot.png",
												"children" :
												(
													{
														"name" : "OfferButton",
														"type" : "button",
														"x" : 7,
														"y" : 5,
														"text_color" : 0xfff8d090,
														"text" : uiScriptLocale.GUILD_INFO_OFFER_EXP,

														"default_image" :  apollo_interface.PATCH_SPECIAL + "/guild/buttons/button_guild_normal.png",
														"over_image" :  apollo_interface.PATCH_SPECIAL + "/guild/buttons/button_guild_hover.png",
														"down_image" :  apollo_interface.PATCH_SPECIAL + "/guild/buttons/button_guild_active.png",
													},
												),
											},

											{
												"name" : "DeclareWarWindow",
												"type" : "image",
												"x" : 225,
												"y" : 45,
												"image" : apollo_interface.PATCH_SPECIAL + "/guild/button_slot_inverted.png",
												"children" :
												(
													{
														"name" : "DeclareWarButton",
														"type" : "button",
														"x" : 7,
														"y" : 5,
														"text_color" : 0xfff8d090,
														"text" : uiScriptLocale.GUILD_WAR_DECLARE,

														"default_image" :  apollo_interface.PATCH_SPECIAL + "/guild/buttons/button_guild_normal.png",
														"over_image" :  apollo_interface.PATCH_SPECIAL + "/guild/buttons/button_guild_hover.png",
														"down_image" :  apollo_interface.PATCH_SPECIAL + "/guild/buttons/button_guild_active.png",
													},
												),
											},
										),
									},

									{
										"name":"Board4",
										"type":"new_board",

										"x":0,
										"y":188,

										"width" : 325+43,
										"height": 133,
										"children":

										(
											{
												"name" : "Buttonbackgr",
												"type" : "window",
												"x" : 40,
												"y" : 2,
												"width" : 10,
												"height": 10,
												"children" :
												(
													{
														"name" : "Credits",
														"type" : "text",
														"x" : 20,
														"y" : 10+15,
														"color" : 0xfff8d090,
														"text" : "If you want to do a Guild run:",
													},

													{
														"name" : "KingSora",
														"type" : "text",
														"x" : 60,
														"y" : 25+15,
														"color" : 0xff866a65,
														"text" : "Please make sure the" + " |cff786044 PVP Mode",
													},

													{
														"name" : "Emperor_Tasho",
														"type" : "text",
														"x" : 60,
														"y" : 40+15,
														"color" : 0xff866a65,
														"text" : "Guild is" + "|cff786044 active",
													},
												),
											},
										),
									},
							),
						},
						{
							"name":"Guild_Chat", "type":"window", "x":10, "y":36, "width":371, "height":322,
							"children" :
							(
								{
									"name":"Comment_section",
									"type":"new_board",

									"x":0,
									"y":0,

									"width" : 325+43,
									"height": 235,
								},
								{
									"name":"Type_section",
									"type":"new_board",

									"x":0,
									"y":235,

									"width" : 325+43,
									"height": 85,
									"children":

									(
										{
											"name" : "Buttonbackgr",
											"type" : "window",
											"x" : 42,
											"y" : 7,
											"width" : 10,
											"height": 10,
											"children" :
											(
												{
													"name":"ChenarChat",
													"type":"image",
													"x":-34,
													"y":8,

													"image" : apollo_interface.PATCH_SPECIAL + "/guild/chenar_chat2.png",
												},
											),
										},
									),
								},
							),
						},
						{
							"name":"Guild_Members", "type":"window", "x":10, "y":36, "width":372, "height":350,
							"children" :
							(
								{
									"name":"Guild_Members_1",
									"type":"new_board",

									"x":0,
									"y":0,

									"width" : 325+43,
									"height": 30,
								},

								{
									"name":"Guild_Members_2",
									"type":"new_board",

									"x":0,
									"y":45,

									"width" : 325+43,
									"height": 265+12,
								},
							),
						},
						{
							"name":"Guild_Skills", "type":"window", "x":10, "y":36, "width":371, "height":322,
							"children" :
							(
								{
									"name":"Board1",
									"type":"window",

									"x":0,
									"y":0,

									"width" : 325+43,
									"height": 330,
									"children":
									(
										{
											"name":"Board_1",
											"type":"new_board",

											"x":0,
											"y":0,

											"width" : 325+43,
											"height": 130,
											"children":
											(

												{
													"name":"Skill_btitle",
													"type":"text",
													"x":145,
													"y" : 20,
													"text" : uiScriptLocale.GUILD_SKILL_STATE,
													"color" : 0xfff8d090,
													"children" :
													(
														{
															"name":"Title_text",
															"type" : "image",


															"x":-65,
															"y":-5,
															"image": apollo_interface.PATCH_COMMON + "/horizontal_bar/center.png",
														},
													),
												},



												{
													"name":"Passive_Skill_Plus_Label",
													"type":"text",
													"x":90,
													"y":55,
													# "text": uiScriptLocale.CHARACTER_PSTATUS,
													"color" : 0xffa08784,
													"children" :
													(
														{
															"name":"Skill_Plus_Value",
															"type":"text",
															"x":95,
															"y":0,
															"text":"99",
															"text_horizontal_align":"center",
															"color" : 0xfff8d090,
														},
													),
												},

												{
													"name":"Board2",
													"type":"new_board",

													"x":0,
													"y":132,

													"width" : 325+43,
													"height": 100,
													"children":
													(
														{
															"name":"Dragon_God_Power_Title",
															"type":"text",
															"x":165,
															"y" : 150-138,
															"text" : "Guild points:",
															"color" : 0xfff8d090,
															"children" :
															(
																{
																	"name":"Title_text",
																	"type" : "image",


																	"x":-90,
																	"y":-5,
																	"image": apollo_interface.PATCH_COMMON + "/horizontal_bar/center.png",
																},
															),
														},

														{
															"name":"EnergyEmpty",
															"type":"image",
															"x" : 20,
															"y" : 70,
															"image" : apollo_interface.PATCH_SPECIAL + "/guild/energy_gauge_empty.png",
														},
														{
															"name" : "EnergyFull",
															"type" : "expanded_image",

															"x" : 22,
															"y" : 70,

															"image" : apollo_interface.PATCH_SPECIAL + "/guild/energy_gauge_full.png",
														},

														{
															"name" : "Dragon_God_Power_Slot",
															"type":"text",
															"x":70,
															"y" : 45,
															"text":"",
															"color" : 0xffa08784,
															"children" :
															(

																{
																	"name":"Dragon_God_Power_Value",
																	"type":"text",
																	"x" : 110,
																	"y" : 5,
																	"color" : 0xfff8d090,
																	"all_align" : "center",
																	"text" : "",
																},

															),
														},
													),
												},

											),
										},
									),
								},

								{
									"name":"Board3",
									"type":"new_board",

									"x":0,
									"y":234,

									"width" : 325+43,
									"height": 86,

								},

								{
									"name" : "DonateEnergyWindow",
									"type" : "image",
									"x" : 125,
									"y" : 236,
									"image" : apollo_interface.PATCH_SPECIAL + "/guild/button_slot.png",
									"children" :
									(
										{
											"name" : "DonateEnergyButton",
											"type" : "button",
											"x" : 7,
											"y" : 5,
											"text_color" : 0xfff8d090,
											"text" : uiScriptLocale.GUILD_SKIlL_HEAL_GSP,

											"default_image" :  apollo_interface.PATCH_SPECIAL + "/guild/buttons/button_guild_normal.png",
											"over_image" :  apollo_interface.PATCH_SPECIAL + "/guild/buttons/button_guild_hover.png",
											"down_image" :  apollo_interface.PATCH_SPECIAL + "/guild/buttons/button_guild_active.png",
										},
									),
								},
							),
						},
						{
							"name":"Guild_Authority", "type":"window", "x":10, "y":36, "width":372, "height":350,
							"children" :
							(
								{
									"name":"Guild_Authority_1",
									"type":"new_board",

									"x":0,
									"y":0,

									"width" : 325+43,
									"height": 30,
								},

								{
									"name":"Guild_Authority_2",
									"type":"new_board",

									"x":0,
									"y":45,

									"width" : 325+43,
									"height": 265+12,
								},
							),
						},
					),
				},
			),
		},
	),
}
