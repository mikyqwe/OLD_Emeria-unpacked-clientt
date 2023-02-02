import uiScriptLocale
import apollo_interface

MAINBOARD_WIDTH = 535 + 4
MAINBOARD_HEIGHT = 431

LEFTBOARD_WIDTH = 291
LEFTBOARD_HEIGHT = 382
LEFTBOARD_X = 13
LEFTBOARD_Y = 36

RIGHTBOARD_WIDTH = 196
RIGHTBOARD_HEIGHT = 382
RIGHTBOARD_X = 328 + 1
RIGHTBOARD_Y = 36

window = {
	"name" : "DungeonInfoWindow",
	"style" : ("movable", "float",),

	"x" : 0,
	"y" : 0,

	"width" : MAINBOARD_WIDTH,
	"height" : MAINBOARD_HEIGHT,

	"children" :
	(
		#######################
		##   DUNGEON_BOARD   ##
		{
			"name" : "DungeonBoard",
			"type" : "board",
			"style" : ("attach", "ltr"),

			"x" : 0,
			"y" : 0,

			"width" : MAINBOARD_WIDTH,
			"height" : MAINBOARD_HEIGHT,

			"children" :
			(
				################################
				##   DUNGEON_BOARD_TITLEBAR   ##
				{
					"name" : "DungeonBoardTitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 7,

					"width" : MAINBOARD_WIDTH - 13,

					"children" :
					(
						{
							"name" : "TitleName",
							"type" : "text",

							"x" : 0,
							"y" : -9,

							"text": uiScriptLocale.DUNGEON_INFO,
							"all_align":"center"
						},
					),
				},
				##   DUNGEON_BOARD_TITLEBAR   ##
				################################

				##############################
				##   DUNGEON_BUTTON_BOARD   ##
				{
					"name" : "DungeonButtonThinBoard",
					"type" : "thinboard",

					"x" : LEFTBOARD_X - 4,
					"y" : LEFTBOARD_Y - 4,

					"width" : LEFTBOARD_WIDTH + 8,
					"height" : LEFTBOARD_HEIGHT + 8,
				},
				{
					"name" : "DungeonButtonBoard",
					"type" : "thinboard_circle",

					"x" : LEFTBOARD_X,
					"y" : LEFTBOARD_Y,

					"width" : LEFTBOARD_WIDTH,
					"height" : LEFTBOARD_HEIGHT,

					"children" : 
					(
						## logininfo.py
					),
				},
				##   DUNGEON_BUTTON_BOARD   ##
				##############################

				########################################
				##   DUNGEON_BUTTON_BOARD_SCROLLBAR   ##
				{
					"name" : "ScrollBar",
					"type" : "new_scrollbar",

					"x" : LEFTBOARD_WIDTH + 18,
					"y" : 32,

					"size" : LEFTBOARD_HEIGHT + 9,
				},
				##   DUNGEON_BUTTON_BOARD_SCROLLBAR   ##
				########################################

				############################
				##   DUNGEON_INFO_BOARD   ##
				{
					"name" : "DungeonInfoThinBoard",
					"type" : "thinboard",

					"x" : RIGHTBOARD_X - 4,
					"y" : RIGHTBOARD_Y - 4,

					"width" : RIGHTBOARD_WIDTH + 8,
					"height" : RIGHTBOARD_HEIGHT + 8,
				},
				{
					"name" : "DungeonInfoBoard",
					"type" : "image",

					"x" : RIGHTBOARD_X,
					"y" : RIGHTBOARD_Y,

					#"width" : RIGHTBOARD_WIDTH,
					#"height" : RIGHTBOARD_HEIGHT,

					"image" : "d:/ymir work/ui/game/dungeon_info/dungeon_bg2.tga",

					"children" : 
					(
						## Title Bar
						{
							"name" : "DungeonInfoTitleBar",
							"type" : "image",

							"x" : 332 - RIGHTBOARD_X,
							"y" : 39 - RIGHTBOARD_Y,

							"image" : "d:/ymir work/dungeon_info_new/dungeon_info_prev.tga",

							"children" :
							(
								{
									"name" : "DungeonInfoName",
									"type" : "text",

									"x" : 0,
									"y" : 0,

									"text" : uiScriptLocale.DUNGEON_INFO_DUNGEON,
									"color" : 0xFFFEE3AE,
									"fontname" : "Tahoma:17",
									"all_align" : "center"
								},
								## Fragezeichen f�r Render Target anzeige
								{
									"name" : "DungeonInfoRender",
									"type" : "button",

									"x" : RIGHTBOARD_WIDTH /2 - 95 + 65 + 65 + 30,
									"y" : 4,

									"default_image" : "d:/ymir work/dungeon_info_new/fragezeichen_normal.tga",
									"over_image" : "d:/ymir work/dungeon_info_new/fragezeichen_hover.tga",
									"down_image" : "d:/ymir work/dungeon_info_new/fragezeichen_down.tga",
								},
							),
						},

						## Dungeon Type
						{
							"name" : "DungeonInfoType",
							"type" : "text",

							"x" : 10,
							"y" : 30 * 1,

							"text" : uiScriptLocale.DUNGEON_INFO_TYPE,
						},

						## Dungeon Organization
						{
							"name" : "DungeonInfoOrganization",
							"type" : "text",

							"x" : 10,
							"y" : 30 + 20 * 1,

							"text" : uiScriptLocale.DUNGEON_INFO_ORGANIZATION,
						},

						## Dungeon Level Limit
						{
							"name" : "DungeonInfoLevelLimit",
							"type" : "text",

							"x" : 10,
							"y" : 30 + 20 * 2,

							"text" : uiScriptLocale.DUNGEON_INFO_LEVEL_LIMIT,
						},

						## Dungeon Party Members
						{
							"name" : "DungeonInfoPartyMembers",
							"type" : "text",

							"x" : 10,
							"y" : 30 + 20 * 3,

							"text" : uiScriptLocale.DUNGEON_INFO_PARTY_MEMBERS,
						},

						## Dungeon Cooldown
						{
							"name" : "DungeonInfoCooldown",
							"type" : "text",

							"x" : 10,
							"y" : 30 + 20 * 4,

							"text" : uiScriptLocale.DUNGEON_INFO_COOLDOWN,
						},

						## Dungeon Duration
						{
							"name" : "DungeonInfoDuration",
							"type" : "text",

							"x" : 10,
							"y" : 30 + 20 * 5,

							"text" : uiScriptLocale.DUNGEON_INFO_DURATION,
						},

						## Dungeon Entrance
						{
							"name" : "DungeonInfoEntrance",
							"type" : "text",

							"x" : 10,
							"y" : 30 + 20 * 6,

							"text" : uiScriptLocale.DUNGEON_INFO_ENTRANCE,
						},

						## Dungeon Strength Bonus
						{
							"name" : "DungeonInfoStrengthBonus",
							"type" : "text",

							"x" : 10,
							"y" : 30 + 20 * 7,

							"text" : uiScriptLocale.DUNGEON_INFO_STRENGTH,
						},

						## Dungeon Resistance Bonus
						{
							"name" : "DungeonInfoResistanceBonus",
							"type" : "text",

							"x" : 10,
							"y" : 30 + 20 * 8,

							"text" : uiScriptLocale.DUNGEON_INFO_RESISTANCE,
						},

						## Dungeon Personal Stats
						{
							"name" : "DungeonInfoPersonal",
							"type" : "image",

							"x" : -5,
							"y" : RIGHTBOARD_HEIGHT / 2 + 15,

							"image" : "d:/ymir work/ui/pattern/seperator.tga",

							"children" :
							(
								# Personal Stats
								{
									"name" : "DungeonInfoPersonalStats",
									"type" : "text",

									"x" : 0,
									"y" : -5,

									"text" : uiScriptLocale.DUNGEON_INFO_PERSONAL_STATS,
									"color" : 0xFFFEE3AE,
									"all_align" : "center",
								},
							),
						},

						## Personal Stats - Total Finished
						{
							"name" : "DungeonInfoTotalFinished",
							"type" : "text",

							"x" : 10,
							"y" : 30 + 20 * 9 + 30,

							"text" : uiScriptLocale.DUNGEON_INFO_TOTAL_FINISHED,
						},

						## Personal Stats - Fastest Time
						{
							"name" : "DungeonInfoFastestTime",
							"type" : "text",

							"x" : 10,
							"y" : 30 + 20 * 10 + 30,

							"text" : uiScriptLocale.DUNGEON_INFO_FASTEST_TIME,
						},

						## Personal Stats - Highest DMG
						{
							"name" : "DungeonInfoHighestDamage",
							"type" : "text",

							"x" : 10,
							"y" : 30 + 20 * 11 + 30,

							"text" : uiScriptLocale.DUNGEON_INFO_HIGHEST_DAMAGE,
						},

						## Special Item Slot BG
						{
							"name" : "DungeonInfoItem",
							"type" : "expanded_image",
							"style" : ("attach",),

							"x" : RIGHTBOARD_WIDTH - 50,
							"y" : RIGHTBOARD_HEIGHT - 50,

							"image" : apollo_interface.PATCH_COMMON + "/slot_rectangle/slot.png",
							
							"children" :
							(
								## Special Item Slot
								{
									"name" : "DungeonInfoItemSlot",
									"type" : "image",

									"x" : 0,
									"y" : -1,
									"width" : 32,
									"height" : 32,

									"image" : "d:/ymir work/ui/pet/skill_button/skill_enable_button.sub",
								},
							),
						},

						## Rank buttons
						{
							"name" : "DungeonRank1Button",
							"type" : "button",

							"x" : RIGHTBOARD_WIDTH /2 - 95,
							"y" : RIGHTBOARD_HEIGHT - 80,

							"tooltip_text" : uiScriptLocale.DUNGEON_RANKING_TYPE1,
							"tooltip_x" : 0,
							"tooltip_y" : -13,

							"default_image" : "d:/ymir work/ui/game/guild/guildbuttons/declareselectpage/king_button00.sub",
							"over_image" : "d:/ymir work/ui/game/guild/guildbuttons/declareselectpage/king_button01.sub",
							"down_image" : "d:/ymir work/ui/game/guild/guildbuttons/declareselectpage/king_button02.sub",
						},
						{
							"name" : "DungeonRank2Button",
							"type" : "button",

							"x" : RIGHTBOARD_WIDTH /2 - 95 + 65,
							"y" : RIGHTBOARD_HEIGHT - 80,

							"tooltip_text" : uiScriptLocale.DUNGEON_RANKING_TYPE2,
							"tooltip_x" : 0,
							"tooltip_y" : -13,

							"default_image" : "d:/ymir work/ui/game/guild/guildbuttons/declareselectpage/time_button00.sub",
							"over_image" : "d:/ymir work/ui/game/guild/guildbuttons/declareselectpage/time_button01.sub",
							"down_image" : "d:/ymir work/ui/game/guild/guildbuttons/declareselectpage/time_button02.sub",
						},
						{
							"name" : "DungeonRank3Button",
							"type" : "button",

							"x" : RIGHTBOARD_WIDTH /2 - 95 + 65 + 65,
							"y" : RIGHTBOARD_HEIGHT - 80,

							"tooltip_text" : uiScriptLocale.DUNGEON_RANKING_TYPE3,
							"tooltip_x" : 0,
							"tooltip_y" : -13,

							"default_image" : "d:/ymir work/ui/game/guild/guildbuttons/declareselectpage/tiger_button00.sub",
							"over_image" : "d:/ymir work/ui/game/guild/guildbuttons/declareselectpage/tiger_button01.sub",
							"down_image" : "d:/ymir work/ui/game/guild/guildbuttons/declareselectpage/tiger_button02.sub",
						},

						# Teleport & Close buttons
						{
							"name" : "DungeonInfoTeleportButton",
							"type" : "button",

							"x" : RIGHTBOARD_WIDTH /2 - 85,
							"y" : RIGHTBOARD_HEIGHT - 25 - 25,

							"text" : uiScriptLocale.DUNGEON_INFO_TELEPORT,
							"default_image" : "d:/ymir work/ui/pet/feed_button/feed_button_default.sub",
							"over_image" : "d:/ymir work/ui/pet/feed_button/feed_button_over.sub",
							"down_image" : "d:/ymir work/ui/pet/feed_button/feed_button_down.sub",
						},
						{
							"name" : "CloseDungeonBoard",
							"type" : "button",

							"x" : RIGHTBOARD_WIDTH /2 - 85,
							"y" : RIGHTBOARD_HEIGHT - 25,

							"text" : uiScriptLocale.DUNGEON_INFO_CLOSE,
							"default_image" : "d:/ymir work/ui/pet/feed_button/feed_button_default.sub",
							"over_image" : "d:/ymir work/ui/pet/feed_button/feed_button_over.sub",
							"down_image" : "d:/ymir work/ui/pet/feed_button/feed_button_down.sub",
						},
					),
				},
				##   DUNGEON_INFO_BOARD   ##
				############################
			),
		},
		##   DUNGEON_BOARD   ##
		#######################
	),
}