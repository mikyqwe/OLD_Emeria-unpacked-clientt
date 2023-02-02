import uiScriptLocale
import localeInfo
import app
import apollo_interface

ROOT = "d:/ymir work/ui/minimap/"
BASE =  apollo_interface.PATCH_SPECIAL + "/taskbar/"

window = {
	"name" : "MiniMap",

	"x" : SCREEN_WIDTH - 145,
	"y" : 0,

	"width" : 168,
	"height" : 158,

	"children" :
	(
		## OpenWindow
		{
			"name" : "OpenWindow",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : 168,
			"height" : 158,

			"children" :
			(
				{
					"name" : "OpenWindowBGI",
					"type" : "image",
					"x" : -175,
					"y" : 0,
					"image" : BASE + "new_minimap.png",
				},
				
				
				## MiniMapWindow
				{
					"name" : "MiniMapWindow",
					"type" : "window",

					"x" : 4,
					"y" : 5,

					"width" : 128,
					"height" : 128,
				},
				## ScaleUpButton
				{
					"name" : "ScaleUpButton",
					"type" : "button",

					"x" : 10,
					"y" : 13,
					
					# "tooltip_text" : "ZoomIn",
					
					"default_image" : BASE + "btn_zoomin_01_normal.png",
					"over_image" : BASE + "btn_zoomin_02_hover.png",
					"down_image" : BASE + "btn_zoomin_03_active.png",
				},
				## ScaleDownButton
				{
					"name" : "ScaleDownButton",
					"type" : "button",

					"x" : -6,
					"y" : 32,

					# "tooltip_text" : "ZoomOut",
			
					"default_image" : BASE + "btn_zoomout_01_normal.png",
					"over_image" : BASE + "btn_zoomout_02_hover.png",
					"down_image" : BASE + "btn_zoomout_03_active.png",
				},
				## MiniMapHideButton
				{
					"name" : "MiniMapHideButton",
					"type" : "button",

					"x" : 112,
					"y" : 30,

					"default_image" : BASE + "btn_close_01_normal.png",
					"over_image" : BASE + "btn_close_02_hover.png",
					"down_image" : BASE + "btn_close_03_active.png",
				},
				## AtlasShowButton
				{
					"name" : "AtlasShowButton",
					"type" : "button",

					"x" : 3,
					"y" : 115,
					
					# "tooltip_text" : "Minimap[M]",
			
					"default_image" : BASE + "btn_atlas_01_normal.png",
					"over_image" : BASE + "btn_atlas_02_hover.png",
					"down_image" : BASE + "btn_atlas_03_active.png",
				},
				## BioButton
				{
					"name" : "bio",
					"type" : "button",

					"x" : 25,
					"y" : 125,
					"tooltip_text": localeInfo.BIO_TITLE,
					
					# "tooltip_text" : "Minimap[M]",
			
					"default_image" : "d:/ymir work/ui/Bio/btn_atlas_01_normal_bio.png",
					"over_image" : "d:/ymir work/ui/Bio/btn_atlas_02_hover_bio.png",
					"down_image" : "d:/ymir work/ui/Bio/btn_atlas_03_active_bio.png",
				},
				## Teleportbutton
				{
					"name" : "TeleportButton",
					"type" : "button",

					"x" : 50,
					"y" : 127,
					
					# "tooltip_text" : "Minimap[M]",
			
					"default_image" : "d:/ymir work/ui/Bio/Teleport_normal.png",
					"over_image" : "d:/ymir work/ui/Bio/Teleport_hover.png",
					"down_image" : "d:/ymir work/ui/Bio/Teleport_down.png",
				},
				## AtlasShowButton
				{
					"name" : "Achievement",
					"type" : "button",

					"x" : 120,
					"y" : 53,
					
					# "tooltip_text" : "Minimap[M]",
			
					"default_image" : BASE + "title_01.png",
					"over_image" : BASE + "title_02.png",
					"down_image" : BASE + "title_03.png",
				},
				
				## ServerInfo
				{
					"name" : "ServerInfo",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70,
					"y" : 140,
					
					"color" : 0xfff8d090,
					
					"text" : "",
				},
				## PositionInfo
				{
					"name" : "PositionInfo",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70,
					"y" : 160,

					"text" : "",
				},
				## ObserverCount
				{
					"name" : "ObserverCount",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 70,
					"y" : 180,

					"text" : "",
				},
				
				## ObserverCount
				{
					"name" : "Time",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 60,
					"y" : 190,

					"text" : "",
				},
				
				## ObserverCount
				{
					"name" : "online",
					"type" : "text",
					
					"text_horizontal_align" : "center",

					"outline" : 1,

					"x" : 50,
					"y" : 200,

					"text" : "",
				},
			),
		},
		{
			"name" : "CloseWindow",
			"type" : "window",

			"x" : 0,
			"y" : 0,

			"width" : 132,
			"height" : 48,

			"children" :
			(
				## ShowButton
				{
					"name" : "MiniMapShowButton",
					"type" : "button",

					"x" : 100,
					"y" : 4,

					"default_image" : ROOT + "minimap_open_default.sub",
					"over_image" : ROOT + "minimap_open_default.sub",
					"down_image" : ROOT + "minimap_open_default.sub",
				},
			),
		},
	),
}
