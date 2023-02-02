WINDOW_WIDTH = 410
WINDOW_HEIGHT = 440

RENDER_TARGET_INDEX = 66

window = {
	"name" : "RenderTargetWindow",

	"x" : 0,
	"y" : 0,

	"style" : ("movable", "float",),

	"width" : WINDOW_WIDTH,
	"height" : WINDOW_HEIGHT,

	"children":
	(
		{
			"name" : "board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : WINDOW_WIDTH,
			"height" : WINDOW_HEIGHT,

			"title" : "Preview",
			"children" :
			(
				# RenderView
				{
					"name" : "RenderTarget",
					"type" : "render_target",
					"style" : ("attach",),

					"x" : 10,
					"y" : 30,

					"width" : 390,
					"height" : 400,

					"index" : RENDER_TARGET_INDEX,
					"children" :
					(
						{
							"name" : "MoveUp",
							"type" : "button",

							"x" : 110,
							"y" : 375,

							"tooltip_text" : "Move Up",

							"default_image" : "d:/ymir work/ui/render/render_up_normal.tga",
							"over_image" : "d:/ymir work/ui/render/render_up_hover.tga",
							"down_image" : "d:/ymir work/ui/render/render_up_normal.tga",
						},

						{
							"name" : "MoveDown",
							"type" : "button",

							"x" : 130,
							"y" : 375,

							"tooltip_text" : "Move Down",

							"default_image" : "d:/ymir work/ui/render/render_down_normal.tga",
							"over_image" : "d:/ymir work/ui/render/render_down_hover.tga",
							"down_image" : "d:/ymir work/ui/render/render_down_normal.tga",
						},
						{
							"name" : "RotateLeft",
							"type" : "button",

							"x" : 150,
							"y" : 375,

							"tooltip_text" : "Left Rotate",

							"default_image" : "d:/ymir work/ui/render/render_stanga_mormal.tga",
							"over_image" : "d:/ymir work/ui/render/render_stanga_hover.tga",
							"down_image" : "d:/ymir work/ui/render/render_stanga_mormal.tga",
						},

						{
							"name" : "RotateRight",
							"type" : "button",

							"x" : 170,
							"y" : 375,

							"tooltip_text" : "Right Rotate",

							"default_image" : "d:/ymir work/ui/render/render_dreapta_normal.tga",
							"over_image" : "d:/ymir work/ui/render/render_dreapta_hover.tga",
							"down_image" : "d:/ymir work/ui/render/render_dreapta_normal.tga",
						},

						{
							"name" : "Refresh",
							"type" : "button",

							"x" : 190,
							"y" : 375,

							"tooltip_text" : "Refresh",

							"default_image" : "d:/ymir work/ui/render/render_refresh_normal.tga",
							"over_image" : "d:/ymir work/ui/render/render_refresh_hover.tga",
							"down_image" : "d:/ymir work/ui/render/render_refresh_normal.tga",
						},

						{
							"name" : "DoEmotion",
							"type" : "button",

							"x" : 210,
							"y" : 375,

							"tooltip_text" : "Emotion",

							"default_image" : "d:/ymir work/ui/render/render_emo_normal.tga",
							"over_image" : "d:/ymir work/ui/render/render_emo_hover.tga",
							"down_image" : "d:/ymir work/ui/render/render_emo_normal.tga",
						},

						{
							"name" : "ZoomIn",
							"type" : "button",

							"x" : 230,
							"y" : 375,

							"tooltip_text" : "Zoom In",

							"default_image" : "d:/ymir work/ui/render/render_zoomin_normal.tga",
							"over_image" : "d:/ymir work/ui/render/render_zoomin_hover.tga",
							"down_image" : "d:/ymir work/ui/render/render_zoomin_normal.tga",
						},

						{
							"name" : "ZoomOut",
							"type" : "button",

							"x" : 250,
							"y" : 375,

							"tooltip_text" : "Zoom Out",

							"default_image" : "d:/ymir work/ui/render/render_zoomout_normal.tga",
							"over_image" : "d:/ymir work/ui/render/render_zoomout_hover.tga",
							"down_image" : "d:/ymir work/ui/render/render_zoomout_normal.tga",
						},
					),
				},
			),
		},
	),
}