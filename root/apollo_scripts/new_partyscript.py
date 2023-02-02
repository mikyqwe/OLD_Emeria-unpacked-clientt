import uiScriptLocale
import apollo_interface
ROOT = "d:/ymir work/ui/public/"

window = {
	"name" : "PartyMemeberInfoBoard",

	"x" : 300,
	"y" : 60,

	"width" : 106,
	"height" : 56,

	"children" :
	(
		
		{
			"name" : "option_button",
			"type" : "button",

			"x" : 0,
			"y" : 0,

			"default_image" : "d:/ymir work/ui/game/windows/party_state_normal_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/party_state_normal_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/party_state_normal_03.sub",
		},

		{
			"name" : "BonusBoard",
			"type" : "image",
			

			"x" : 75,
			"y" : 16,
			
			"image" : apollo_interface.PATCH_SPECIAL+"/party/bonusboard.png"
		},
		{
			"name" : "Empty_Face",
			"type" : "image",
			

			"x" : 22,
			"y" : -10,
			
			
			
			"image" : apollo_interface.APOLLO_FACE + "medium/empty_face.png"
		},
		{
			"name" : "face_image",
			"type" : "image",
			

			"x" : 22,
			"y" : -10,
			
			
			"image" : apollo_interface.APOLLO_FACE + "medium/icon_mwarrior.png"
		},
		
		
		{
			"name" : "HP_empty",
			"type" : "image",

			"x" : 19,
			"y" : 30,
			
			
			"image" : apollo_interface.PATCH_SPECIAL+"/party/member_gauge_hp_empty.png"
		},
		{
			"name" : "hp_gauge",
			"type" : "expanded_image",
		
			"x" : 19,
			"y" : 30,
			
			"image" : apollo_interface.PATCH_SPECIAL+"/party/member_gauge_hp_fill.png"
		},
		{
			"name" : "bonus_info_icon",
			"type" : "image",

			"x" : 80,
			"y" : 27-6,

			"image" : apollo_interface.PATCH_SPECIAL+"/party/bonus_shower.png"
		},
		{
			"name" : "ExperienceImage",
			"type" : "image",

			"x" : 55,
			"y" : -10,

			"image" : apollo_interface.PATCH_SPECIAL+"/party/member_icon_exp_full.png"
		},
		{
			"name" : "AttackerImage",
			"type" : "image",

			"x" : 80,
			"y" : 27-6,

			"image" : apollo_interface.PATCH_SPECIAL+"/party/bonus_shower.png"
		},
		{
			"name" : "DefenderImage",
			"type" : "image",

			"x" : 80,
			"y" : 27-6,

			"image" : apollo_interface.PATCH_SPECIAL+"/party/bonus_shower.png"
		},
		{
			"name" : "BufferImage",
			"type" : "image",

			"x" : 80,
			"y" : 27-6,

			"image" : apollo_interface.PATCH_SPECIAL+"/party/bonus_shower.png"
		},
		{
			"name" : "SkillMasterImage",
			"type" : "image",

			"x" : 80,
			"y" : 27-6,

			"image" : apollo_interface.PATCH_SPECIAL+"/party/bonus_shower.png"
		},
		{
			"name" : "TimeBonusImage",
			"type" : "image",

			"x" : 80,
			"y" : 27-6,

			"image" : apollo_interface.PATCH_SPECIAL+"/party/bonus_shower.png"
		},
		{
			"name" : "RegenBonus",
			"type" : "image",

			"x" : 80,
			"y" : 27-6,

			"image" : apollo_interface.PATCH_SPECIAL+"/party/bonus_shower.png"
		},
	),
}
