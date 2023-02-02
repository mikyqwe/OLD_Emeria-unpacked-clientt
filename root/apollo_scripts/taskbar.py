import uiScriptLocale
import app
import apollo_interface
ROOT = "d:/ymir work/ui/game/"
BASE =  apollo_interface.PATCH_SPECIAL + "/taskbar/"

Y_ADD_POSITION = 0

window = {
	"name" : "TaskBar",

	"x" : 0,
	"y" : SCREEN_HEIGHT - 48,

	"width" : SCREEN_WIDTH,
	"height" : 158,

	"children" :
	(

		## Board
		{
			"name" : "Base_Board_01",
			"type" : "expanded_image",

			"x" : (SCREEN_WIDTH-594)/2,
			"y" : -7,

			"image" : BASE+"bg.png"
		},
		{
			"name" : "LeftMouseButton",
			"type" : "button",

			"x" : (SCREEN_WIDTH/2)-230-15+15+3,
			"y" :123-110,

			"default_image" : BASE + "btn_attacknormal_01_normal.png",
			"over_image" : BASE + "btn_attacknormal_02_hover.png",
			"down_image" : BASE + "btn_attacknormal_03_active.png",
		},
		{
			"name" : "RightMouseButton",
			"type" : "button",

			"x" : SCREEN_WIDTH/2 + 128 + 66 + +10+5,
			"y" : 183-110,

			"default_image" : BASE + "btn_camera_01_normal.png",
			"over_image" : BASE + "btn_camera_02_hover.png",
			"down_image" : BASE + "btn_camera_03_active.png",
		},
		## QuickBar
		{
			"name" : "quickslot_board",
			"type" : "window",

			"x" : SCREEN_WIDTH/2 - 128 + 32 + 10-120+18,
			"y" : 115-110,

			"width" : 256 + 14 + 2 + 11+100+10,
			"height" : 37,

			"children" :
			(
				{

					"name" : "ExpandButton",
					"type" : "button",

					"x" : 128+45+4,
					"y" : 13,
					"tooltip_text" : "Chat",


					"default_image" : BASE + "btn_chat_01_normal.png",
					"over_image" : BASE + "btn_chat_02_hover.png",
					"down_image" : BASE + "btn_chat_03_active.png",
				},
				{
					"name" : "quick_slot_1",
					"type" : "grid_table",

					"start_index" : 0,

					"x" : 0,
					"y" : 3,

					"x_count" : 4,
					"y_count" : 1,
					"x_step" : 32,
					"y_step" : 32,
					"x_blank" : 10,

					"image_r" : 1.0,
					"image_g" : 1.0,
					"image_b" : 1.0,
					"image_a" : 1.0,

					"children" :
					(
						{ "name" : "slot_1", "type" : "image", "x" : 3, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/1.sub", },
						{ "name" : "slot_2", "type" : "image", "x" : 35+10, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/2.sub", },
						{ "name" : "slot_3", "type" : "image", "x" : 67+20, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/3.sub", },
						{ "name" : "slot_4", "type" : "image", "x" : 99+30, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/4.sub", },
					),
				},
				{
					"name" : "quick_slot_2",
					"type" : "grid_table",

					"start_index" : 4,

					"x" : 128 + 14+60+17+1,
					"y" : 3,

					"x_count" : 4,
					"y_count" : 1,
					"x_step" : 32,
					"y_step" : 32,
					"x_blank" : 10,

					# "image" : "d:/ymir work/ui/slot.png",
					"image_r" : 1.0,
					"image_g" : 1.0,
					"image_b" : 1.0,
					"image_a" : 1.0,

					"children" :
					(
						{ "name" : "slot_5", "type" : "image", "x" : 3, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f1.sub", },
						{ "name" : "slot_6", "type" : "image", "x" : 35+10, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f2.sub", },
						{ "name" : "slot_7", "type" : "image", "x" : 67+22, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f3.sub", },
						{ "name" : "slot_8", "type" : "image", "x" : 99+32, "y" : 3, "image" : "d:/ymir work/ui/game/taskbar/f4.sub", },
					),
				},
				
			),
		},
		{

			"name" : "ButtonPageSlots",
			"type" : "button",

			"x" : SCREEN_WIDTH/2 - 128 + 32 + 10-120+18+397,
			"y" : 13,					
			
			"default_image" : BASE + "btn_slotpageone_01_normal.png",
			"over_image" :BASE + "btn_slotpageone_02_hover.png",
			"down_image" : BASE + "btn_slotpageone_03_active.png",

		},
	),
}
