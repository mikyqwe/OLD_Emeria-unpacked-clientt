import uiScriptLocale

PATCH_TASKBAR = "interface_EmperorApollo/special/taskbar"

window = {
	"name" : "ButtonWindow",

	"x" : 0,
	"y" : 0,

	"width" : 32,
	"height" : 32 * 3,

	"children" :
	(
		{
			"name" : "button_move_and_attack",
			"type" : "button",

			"x" : 0,
			"y" : 0,

			"tooltip_text" : uiScriptLocale.MOUSEBUTTON_ATTACK,
			"tooltip_x" : -40,
			"tooltip_y" : 9,

			"default_image" : PATCH_TASKBAR + "/btn_attacknormal_01_normal.png",
			"over_image" : PATCH_TASKBAR + "/btn_attacknormal_02_hover.png",
			"down_image" : PATCH_TASKBAR + "/btn_attacknormal_03_active.png",
		},
		{
			"name" : "button_auto_attack",
			"type" : "button",

			"x" : 0,
			"y" : 32,

			"tooltip_text" : uiScriptLocale.MOUSEBUTTON_AUTO_ATTACK,
			"tooltip_x" : -40,
			"tooltip_y" : 9,
		
		
			"default_image" : PATCH_TASKBAR + "/btn_attackauto_01_normal.png",
			"over_image" : PATCH_TASKBAR + "/btn_attackauto_02_hover.png",
			"down_image" : PATCH_TASKBAR + "/btn_attackauto_03_active.png",
			
		},
		{
			"name" : "button_camera",
			"type" : "button",

			"x" : 0,
			"y" : 64,

			"tooltip_text" : uiScriptLocale.MOUSEBUTTON_CAMERA,
			"tooltip_x" : -40,
			"tooltip_y" : 9,
			
			"default_image" : PATCH_TASKBAR + "/btn_camera_01_normal.png",
			"over_image" : PATCH_TASKBAR + "/btn_camera_02_hover.png",
			"down_image" : PATCH_TASKBAR + "/btn_camera_03_active.png",
		},
	),
}