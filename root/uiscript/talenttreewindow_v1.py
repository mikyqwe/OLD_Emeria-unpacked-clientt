import uiScriptLocale
import item
import app
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
ROOT = "d:/ymir work/ui/talent_tree_v1/"
SKILLS = "d:/ymir work/ui/talent_tree_v1/skills/"
BUTTON_ROOT = "d:/ymir work/ui/public/"

BOARD_WIDTH = 400-100
BOARD_HEIGHT = 580-215

window = {
	"name" : "TimewalkWindow",

	"x" : (SCREEN_WIDTH/2) - (BOARD_WIDTH/2),
	"y" : (SCREEN_HEIGHT/2) - (BOARD_HEIGHT/2),

	"style" : ("movable", "float",),

	"width" : 400-100,
	"height" : 580-215,

	"children" :
	(
		{
			"name" : "board",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : 400-100,
			"height" : 580-215,
		
			"children" :
			(
				## Title
				{
					"name" : "TitleBar",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 6,
					"y" : 6,

					"width" : 385-100,
					"color" : "yellow",

					"children" :
					(
						{ "name":"TitleName", "type":"text", "x":142, "y":3, "text":"", "text_horizontal_align":"center" },
					),
				},
				{
					"name" : "Talenttree_Levelup_Header_02",
					"type" : "image",
					
					"x" : 19,
					"y" : 33,
					
					"image" : ROOT + "header.tga",
					
					"children" :
					(
						{ "name":"TitleName2", "type":"text", "x":13, "y":3, "text":"", "text_horizontal_align":"" },
					),
				},
				{
					"name" : "Shadowbox",
					"type" : "image",
					
					"x" : 19,
					"y" : 53,
					
					"image" : ROOT + "shadowbox_large.tga",
					
					"children" :
					(






						{
							"name" : "LINES",
							"type" : "image",
							
							"x" : 32,
							"y" : 15+33,
							
							"image" : ROOT+"lines.tga",
						},
						##SKILLS##
						##########
						#SKILL 01#
						##########
						{
							"name" : "Skill_01_default",
							"type" : "button",
							
							"x" : 15,
							"y" : 15,
							
							"default_image" : SKILLS+"slot01_deactive.tga",
							"over_image" : SKILLS+"slot01_deactive.tga",
							"down_image" : SKILLS+"slot01_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_01_active",
							"type" : "button",
							
							"x" : 15,
							"y" : 15,
							
							"default_image" : SKILLS+"slot01_active.tga",
							"over_image" : SKILLS+"slot01_active.tga",
							"down_image" : SKILLS+"slot01_active.tga",
							
							"children" :
							(
								{ "name":"Skill_01_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 02#
						##########
						{
							"name" : "Skill_02_default",
							"type" : "button",
							
							"x" : 15+50,
							"y" : 15,
							
							"default_image" : SKILLS+"slot02_deactive.tga",
							"over_image" : SKILLS+"slot02_deactive.tga",
							"down_image" : SKILLS+"slot02_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_02_active",
							"type" : "button",
							
							"x" : 15+50,
							"y" : 15,
							
							"default_image" : SKILLS+"slot02_active.tga",
							"over_image" : SKILLS+"slot02_active.tga",
							"down_image" : SKILLS+"slot02_active.tga",
							
							"children" :
							(
								{ "name":"Skill_02_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 03#
						##########
						{
							"name" : "Skill_03_default",
							"type" : "button",
							
							"x" : 15+50+50,
							"y" : 15,
							
							"default_image" : SKILLS+"slot03_deactive.tga",
							"over_image" : SKILLS+"slot03_deactive.tga",
							"down_image" : SKILLS+"slot03_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_03_active",
							"type" : "button",
							
							"x" : 15+50+50,
							"y" : 15,
							
							"default_image" : SKILLS+"slot03_active.tga",
							"over_image" : SKILLS+"slot03_active.tga",
							"down_image" : SKILLS+"slot03_active.tga",
							
							"children" :
							(
								{ "name":"Skill_03_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 04#
						##########
						{
							"name" : "Skill_04_default",
							"type" : "button",
							
							"x" : 15+50+50+50,
							"y" : 15,
							
							"default_image" : SKILLS+"slot04_deactive.tga",
							"over_image" : SKILLS+"slot04_deactive.tga",
							"down_image" : SKILLS+"slot04_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_04_active",
							"type" : "button",
							
							"x" : 15+50+50+50,
							"y" : 15,
							
							"default_image" : SKILLS+"slot04_active.tga",
							"over_image" : SKILLS+"slot04_active.tga",
							"down_image" : SKILLS+"slot04_active.tga",
							
							"children" :
							(
								{ "name":"Skill_04_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 05#
						##########
						{
							"name" : "Skill_05_default",
							"type" : "button",
							
							"x" : 15+50+50+50+50,
							"y" : 15,
							
							"default_image" : SKILLS+"slot05_deactive.tga",
							"over_image" : SKILLS+"slot05_deactive.tga",
							"down_image" : SKILLS+"slot05_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_05_active",
							"type" : "button",
							
							"x" : 15+50+50+50+50,
							"y" : 15,
							
							"default_image" : SKILLS+"slot05_active.tga",
							"over_image" : SKILLS+"slot05_active.tga",
							"down_image" : SKILLS+"slot05_active.tga",
							
							"children" :
							(
								{ "name":"Skill_05_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 06#
						##########
						{
							"name" : "Skill_06_default",
							"type" : "button",
							
							"x" : 15+25,
							"y" : 70,
							
							"default_image" : SKILLS+"slot06_deactive.tga",
							"over_image" : SKILLS+"slot06_deactive.tga",
							"down_image" : SKILLS+"slot06_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_06_active",
							"type" : "button",
							
							"x" : 15+25,
							"y" : 70,
							
							"default_image" : SKILLS+"slot06_active.tga",
							"over_image" : SKILLS+"slot06_active.tga",
							"down_image" : SKILLS+"slot06_active.tga",
							
							"children" :
							(
								{ "name":"Skill_06_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 07#
						##########
						{
							"name" : "Skill_07_default",
							"type" : "button",
							
							"x" : 15+25+50,
							"y" : 70,
							
							"default_image" : SKILLS+"slot07_deactive.tga",
							"over_image" : SKILLS+"slot07_deactive.tga",
							"down_image" : SKILLS+"slot07_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_07_active",
							"type" : "button",
							
							"x" : 15+25+50,
							"y" : 70,
							
							"default_image" : SKILLS+"slot07_active.tga",
							"over_image" : SKILLS+"slot07_active.tga",
							"down_image" : SKILLS+"slot07_active.tga",
							
							"children" :
							(
								{ "name":"Skill_07_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 08#
						##########
						{
							"name" : "Skill_08_default",
							"type" : "button",
							
							"x" : 15+25+50+50,
							"y" : 70,
							
							"default_image" : SKILLS+"slot08_deactive.tga",
							"over_image" : SKILLS+"slot08_deactive.tga",
							"down_image" : SKILLS+"slot08_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_08_active",
							"type" : "button",
							
							"x" : 15+25+50+50,
							"y" : 70,
							
							"default_image" : SKILLS+"slot08_active.tga",
							"over_image" : SKILLS+"slot08_active.tga",
							"down_image" : SKILLS+"slot08_active.tga",
							
							"children" :
							(
								{ "name":"Skill_08_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 09#
						##########
						{
							"name" : "Skill_09_default",
							"type" : "button",
							
							"x" : 15+25+50+50+50,
							"y" : 70,
							
							"default_image" : SKILLS+"slot09_deactive.tga",
							"over_image" : SKILLS+"slot09_deactive.tga",
							"down_image" : SKILLS+"slot09_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_09_active",
							"type" : "button",
							
							"x" : 15+25+50+50+50,
							"y" : 70,
							
							"default_image" : SKILLS+"slot09_active.tga",
							"over_image" : SKILLS+"slot09_active.tga",
							"down_image" : SKILLS+"slot09_active.tga",
							
							"children" :
							(
								{ "name":"Skill_09_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 10#
						##########
						{
							"name" : "Skill_10_default",
							"type" : "button",
							
							"x" : 15+50,
							"y" : 70+55,
							
							"default_image" : SKILLS+"slot10_deactive.tga",
							"over_image" : SKILLS+"slot10_deactive.tga",
							"down_image" : SKILLS+"slot10_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_10_active",
							"type" : "button",
							
							"x" : 15+50,
							"y" : 70+55,
							
							"default_image" : SKILLS+"slot10_active.tga",
							"over_image" : SKILLS+"slot10_active.tga",
							"down_image" : SKILLS+"slot10_active.tga",
							
							"children" :
							(
								{ "name":"Skill_10_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 11#
						##########
						{
							"name" : "Skill_11_default",
							"type" : "button",
							
							"x" : 15+50+50,
							"y" : 70+55,
							
							"default_image" : SKILLS+"slot11_deactive.tga",
							"over_image" : SKILLS+"slot11_deactive.tga",
							"down_image" : SKILLS+"slot11_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_11_active",
							"type" : "button",
							
							"x" : 15+50+50,
							"y" : 70+55,
							
							"default_image" : SKILLS+"slot11_active.tga",
							"over_image" : SKILLS+"slot11_active.tga",
							"down_image" : SKILLS+"slot11_active.tga",
							
							"children" :
							(
								{ "name":"Skill_11_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 12#
						##########
						{
							"name" : "Skill_12_default",
							"type" : "button",
							
							"x" : 15+50+50+50,
							"y" : 70+55,
							
							"default_image" : SKILLS+"slot12_deactive.tga",
							"over_image" : SKILLS+"slot12_deactive.tga",
							"down_image" : SKILLS+"slot12_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_12_active",
							"type" : "button",
							
							"x" : 15+50+50+50,
							"y" : 70+55,
							
							"default_image" : SKILLS+"slot12_active.tga",
							"over_image" : SKILLS+"slot12_active.tga",
							"down_image" : SKILLS+"slot12_active.tga",
							
							"children" :
							(
								{ "name":"Skill_12_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 13#
						##########
						{
							"name" : "Skill_13_default",
							"type" : "button",
							
							"x" : 15+50+25,
							"y" : 70+55+55,
							
							"default_image" : SKILLS+"slot13_deactive.tga",
							"over_image" : SKILLS+"slot13_deactive.tga",
							"down_image" : SKILLS+"slot13_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_13_active",
							"type" : "button",
							
							"x" : 15+50+25,
							"y" : 70+55+55,
							
							"default_image" : SKILLS+"slot13_active.tga",
							"over_image" : SKILLS+"slot13_active.tga",
							"down_image" : SKILLS+"slot13_active.tga",
							
							"children" :
							(
								{ "name":"Skill_13_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 14#
						##########
						{
							"name" : "Skill_14_default",
							"type" : "button",
							
							"x" : 15+50+25+50,
							"y" : 70+55+55,
							
							"default_image" : SKILLS+"slot14_deactive.tga",
							"over_image" : SKILLS+"slot14_deactive.tga",
							"down_image" : SKILLS+"slot14_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_14_active",
							"type" : "button",
							
							"x" : 15+50+25+50,
							"y" : 70+55+55,
							
							"default_image" : SKILLS+"slot14_active.tga",
							"over_image" : SKILLS+"slot14_active.tga",
							"down_image" : SKILLS+"slot14_active.tga",
							
							"children" :
							(
								{ "name":"Skill_14_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
						##########
						#SKILL 15#
						##########
						{
							"name" : "Skill_15_default",
							"type" : "button",
							
							"x" : 15+50+50,
							"y" : 70+55+55+55,
							
							"default_image" : SKILLS+"slot15_deactive.tga",
							"over_image" : SKILLS+"slot15_deactive.tga",
							"down_image" : SKILLS+"slot15_deactive.tga",
							"children" :
							(
								{ "name":"default", "type":"text", "x":21, "y":20, "text":"-", "text_horizontal_align":"" },
							),
						},
						{
							"name" : "Skill_15_active",
							"type" : "button",
							
							"x" : 15+50+50,
							"y" : 70+55+55+55,
							
							"default_image" : SKILLS+"slot15_active.tga",
							"over_image" : SKILLS+"slot15_active.tga",
							"down_image" : SKILLS+"slot15_active.tga",
							
							"children" :
							(
								{ "name":"Skill_15_Points", "type":"text", "x":21, "y":20, "text":"", "text_horizontal_align":"" },
							),
						},
					),
				},
			),
		},
	),
}

