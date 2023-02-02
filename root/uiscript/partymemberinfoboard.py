import uiScriptLocale

window = {
	"name" : "PartyMemeberInfoBoard",

	"x" : 0,
	"y" : 0,

	"width" : 106,
	"height" : 56,

	"children" :
	(

		{
			"name" : "BackGr",
			"type" : "image",


			"x" : 0,
			"y" : -5,
			"width" : 84,


			"image" : "d:/ymir work/interface/party/affects/bg_gradient.tga"
		},
		{
			"name" : "NameBoard",
			"type" : "image",


			"x" : 60,
			"y" : -2,
			"width" : 84,


			"image" : "d:/ymir work/interface/party/nameboard.tga"
		},

		{
			"name" : "StateButton",
			"type" : "button",

			"x" : 0,
			"y" : 0,

			"default_image" : "d:/ymir work/ui/game/windows/party_state_normal_01.sub",
			"over_image" : "d:/ymir work/ui/game/windows/party_state_normal_02.sub",
			"down_image" : "d:/ymir work/ui/game/windows/party_state_normal_03.sub",
		},

		{
			"name" : "NameSlot",
			"type" : "text",
			"style" : ("not_pick",),

			"x" : 80,
			"y" : 0,
			"width" : 84,
			"height" : 17,

			"children" :
			(
				{
					"name" : "NamePrint",
					"type" : "text",

					"x" : -2,
					"y" : 2,

					"text" : uiScriptLocale.PARTY_MEMBER_INFO_NAME,
				},
			),
		},
		{
			"name" : "BonusBoard",
			"type" : "image",


			"x" : 75,
			"y" : 22,
			"width" : 84,


			"image" : "d:/ymir work/interface/party/bonusboard.tga"
		},

		{
			"name" : "Empty_Face",
			"type" : "image",


			"x" : 22,
			"y" : -10,
			"width" : 84,


			"image" : "d:/ymir work/interface/party/face/empty_face.tga"
		},

		{
			"name" : "FaceImage",
			"type" : "image",


			"x" : 22,
			"y" : -10,
			"width" : 84,


			"image" : "d:/ymir work/interface/party/face/icon_mshaman.tga"
		},


		{
			"name" : "Gauge2",
			"type" : "image",
			"style" : ("not_pick",),

			"x" : 19,
			"y" : 30,
			"width" : 84,
			"color" : "red",

			"image" : "d:/ymir work/interface/party/hp_empty.tga"
		},
		{
			"name" : "Gauge",
			"type" : "expanded_image",
			"style" : ("not_pick",),

			"x" : 19,
			"y" : 30,
			"width" : 84,


			"image" : "d:/ymir work/interface/party/hp_full.tga"
		},

		{
			"name" : "ExperienceImage_Empty",
			"type" : "image",

			"x" : 55,
			"y" : -10,

			"image" : "d:/ymir work/interface/party/icon_exp_empty.tga"
		},

		{
			"name" : "ExperienceImage",
			"type" : "image",

			"x" : 55,
			"y" : -10,

			"image" : "d:/ymir work/interface/party/icon_exp_full.tga"
		},
		{
			"name" : "AttackerImage",
			"type" : "image",

			"x" : 80,
			"y" : 27,

			"image" : "d:/ymir work/interface/party/bonus_shower.tga"
		},
		{
			"name" : "DefenderImage",
			"type" : "image",

			"x" : 80,
			"y" : 27,

			"image" : "d:/ymir work/interface/party/bonus_shower.tga"
		},
		{
			"name" : "BufferImage",
			"type" : "image",

			"x" : 80,
			"y" : 27,

			"image" : "d:/ymir work/interface/party/bonus_shower.tga"
		},
		{
			"name" : "SkillMasterImage",
			"type" : "image",

			"x" : 80,
			"y" : 27,

			"image" : "d:/ymir work/interface/party/bonus_shower.tga"
		},
		{
			"name" : "TimeBonusImage",
			"type" : "image",

			"x" : 80,
			"y" : 27,

			"image" : "d:/ymir work/interface/party/bonus_shower.tga"
		},
		{
			"name" : "RegenBonus",
			"type" : "image",

			"x" : 80,
			"y" : 27,

			"image" : "d:/ymir work/interface/party/bonus_shower.tga"
		},
		{
			"name" : "IncreaseArea150",
			"type" : "image",
			"x" : 80,
			"y" : 27,

			"image" : "d:/ymir work/interface/party/bonus_shower.tga"
		},
		{
			"name" : "IncreaseArea200",
			"type" : "image",

			"x" : 80,
			"y" : 27,

			"image" : "d:/ymir work/interface/party/bonus_shower.tga"
		},

	),
}

