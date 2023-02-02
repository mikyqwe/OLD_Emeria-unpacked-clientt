import uiScriptLocale
import item
import apollo_interface
import app

COSTUME_START_INDEX = item.COSTUME_SLOT_START
SHINING_START_INDEX = item.SHINING_SLOT_START
SKILL_START_INDEX = item.SKILL_COSTUME_SLOT_START

window = {
	"name" : "CostumeWindow",
	"x" : SCREEN_WIDTH - 230 - 140,
	"y" : SCREEN_HEIGHT - 37 - 650,
	"style" : ("movable", "float",),
	"width" : 145,
	"height" : 180,
	"children" :
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : 145,
			"height" : 205,
			"title" : uiScriptLocale.COSTUME_WINDOW_TITLE,
			"children" :
			(
				{
					"name" : "Costume_Page",
					"type" : "window",
					"style" : ("attach",),
					"x" : 3,
					"y" : 3,
					"width" : 127,
					"height" : 236 + 11,
					"children" :
					(
						{
							"name" : "Costume_Base",
							"type" : "image",
							"x" : 10,
							"y" : 35,
							"image" : "%s/inventory/costume_m.png" % apollo_interface.PATCH_SPECIAL,
							"children" :
							(
								{
									"name" : "CostumeSlot",
									"type" : "slot",
									"x" : 3,
									"y" : 3,
									"width" : 127,
									"height" : 236 + 11,
									"slot" : (
										{"index":COSTUME_START_INDEX+0, "x":50, "y":40, "width":32, "height":64},
										{"index":COSTUME_START_INDEX+1, "x":50, "y": 0, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+2, "x":67, "y":115, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+3, "x":10, "y":5, "width":32, "height":32},
										{"index":COSTUME_START_INDEX+4, "x":10, "y":112, "width":32, "height":32},
									),
								},
								## ENABLE_HIDE_COSTUME_SYSTEM
								{
									"name" : "BodyToolTipButton",
									"type" : "toggle_button",

									"x" : 43,
									"y" : 37,
									"tooltip_text" : uiScriptLocale.HIDE_COSTUME,

									"default_image" : "d:/ymir work/ui/pattern/visible_mark_01.tga",
									"over_image" : "d:/ymir work/ui/pattern/visible_mark_02.tga",
									"down_image" : "d:/ymir work/ui/pattern/visible_mark_03.tga",
								},
								{
									"name" : "HairToolTipButton",
									"type" : "toggle_button",

									"x" : 43,
									"y" : 0,
									"tooltip_text" : uiScriptLocale.HIDE_COSTUME,

									"default_image" : "d:/ymir work/ui/pattern/visible_mark_01.tga",
									"over_image" : "d:/ymir work/ui/pattern/visible_mark_02.tga",
									"down_image" : "d:/ymir work/ui/pattern/visible_mark_03.tga",
								},
								{
									"name" : "SashToolTipButton",
									"type" : "toggle_button",

									"x" : 56,
									"y" : 110,
									"tooltip_text" : uiScriptLocale.HIDE_COSTUME,

									"default_image" : "d:/ymir work/ui/pattern/visible_mark_01.tga",
									"over_image" : "d:/ymir work/ui/pattern/visible_mark_02.tga",
									"down_image" : "d:/ymir work/ui/pattern/visible_mark_03.tga",
								},
								{
									"name" : "WeaponToolTipButton",
									"type" : "toggle_button",

									"x" : 9,
									"y" : 9,
									"tooltip_text" : uiScriptLocale.HIDE_COSTUME,

									"default_image" : "d:/ymir work/ui/pattern/visible_mark_01.tga",
									"over_image" : "d:/ymir work/ui/pattern/visible_mark_02.tga",
									"down_image" : "d:/ymir work/ui/pattern/visible_mark_03.tga",
								},
							),
						},
					),
				},
				{
					"name" : "Shining_Page",
					"type" : "window",
					"style" : ("attach",),
					"x" : 3,
					"y" : 3,
					"width" : 127,
					"height" : 236 + 11,

					"children" :
					(
						{
							"name" : "Shining_Base",
							"type" : "image",
							"x" : 10,
							"y" : 35,
							"image" : "%s/inventory/shining_fenster.tga" % apollo_interface.PATCH_SPECIAL,
							"children" :
							(
								{
									"name" : "ShiningSlot",
									"type" : "slot",

									"x" : 3,
									"y" : 3,

									"width" : 127,
									"height" : 236 + 11,
									
									"slot" : (
										{"index":SHINING_START_INDEX+0, "x":10, "y":5, "width":32, "height":32}, # Waffe1
										{"index":SHINING_START_INDEX+1, "x":10, "y":48, "width":32, "height":32},  # Waffe2
										{"index":SHINING_START_INDEX+2, "x":10, "y":91, "width":32, "height":32}, # Waffe3
										{"index":SHINING_START_INDEX+3, "x":66, "y":5, "width":32, "height":32}, # Armor1
										{"index":SHINING_START_INDEX+4, "x":66, "y":48, "width":32, "height":32}, # Armor2
										{"index":SHINING_START_INDEX+5, "x":66, "y": 91, "width":32, "height":32}, # Kopf
										{"index":item.EQUIPMENT_DITO, "x":10, "y": 112, "width":32, "height":32}, # Dito
										# TODO aurasystem neue shining slots 
									),
								},
							),
						},
					),
				},
				{
					"name" : "Skill_Page",
					"type" : "window",
					"style" : ("attach",),
					"x" : 3,
					"y" : 3,
					"width" : 127,
					"height" : 236 + 11,

					"children" :
					(
						{
							"name" : "Skill_Base",
							"type" : "image",
							"x" : 10,
							"y" : 35,
							"image" : "%s/inventory/skillkosi_fenster.tga" % apollo_interface.PATCH_SPECIAL,
							"children" :
							(
								{
									"name" : "SkillSlot",
									"type" : "slot",

									"x" : 3,
									"y" : 3,

									"width" : 127,
									"height" : 236 + 11,

									"slot" : (
										{"index":SKILL_START_INDEX+0, "x":10, "y":5, "width":32, "height":32}, 
										{"index":SKILL_START_INDEX+1, "x":10, "y":48, "width":32, "height":32},
										{"index":SKILL_START_INDEX+2, "x":10, "y":91, "width":32, "height":32},
										{"index":SKILL_START_INDEX+3, "x":66, "y": 5, "width":32, "height":32},
										{"index":SKILL_START_INDEX+4, "x":66, "y":48, "width":32, "height":32},
										{"index":SKILL_START_INDEX+5, "x":66, "y":91, "width":32, "height":32},
									),
								},
							),
						},	
					),
				},
				## END_OF_ENABLE_HIDE_COSTUME_SYSTEM
				{
					"name" : "ChangeButton",
					"type" : "button",

					"x" : 113,
					"y" : 38,

					"tooltip_text" : uiScriptLocale.CHANGE_SHINING,

					"default_image" : "%s/button/titlebar_1_normal.png" % apollo_interface.PATCH_COMMON,
					"over_image" : "%s/button/titlebar_1_hover.png" % apollo_interface.PATCH_COMMON,
					"down_image" : "%s/button/titlebar_1_active.png" % apollo_interface.PATCH_COMMON,
				},
			),
		},
	),
}
