import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import uiCommon
import constInfo
import exception
import item
import player
import net
import grp
import app
import ui
import mouseModule
import dbg
import uiToolTip
import chat
import event
import wndMgr
import talenttree

class TalentTreeWindow(ui.ScriptWindow):
	isLoad = False

	def __init__(self):
		self.current_points = 0
		self.point_skill = 0
		self.skill_01_points = 0
		self.skill_02_points = 0
		self.skill_03_points = 0
		self.skill_04_points = 0
		self.skill_05_points = 0
		self.skill_06_points = 0
		self.skill_07_points = 0
		self.skill_08_points = 0
		self.skill_09_points = 0
		self.skill_10_points = 0
		self.skill_11_points = 0
		self.skill_12_points = 0
		self.skill_13_points = 0
		self.skill_14_points = 0
		self.skill_15_points = 0
		self.tooltipItem = uiToolTip.ItemToolTip()
		ui.ScriptWindow.__init__(self)

	def __del__(self):
		self.current_points = None
		self.point_skill = None
		self.skill_01_points = None
		self.skill_02_points = None
		self.skill_03_points = None
		self.skill_04_points = None
		self.skill_05_points = None
		self.skill_06_points = None
		self.skill_07_points = None
		self.skill_08_points = None
		self.skill_09_points = None
		self.skill_10_points = None
		self.skill_11_points = None
		self.skill_12_points = None
		self.skill_13_points = None
		self.skill_14_points = None
		self.skill_15_points = None
		ui.ScriptWindow.__del__(self)

	def Close(self):
		constInfo.talent_window = 0
		wndMgr.Hide(self.hWnd)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/talenttreewindow_v1.py")
		except:
			import exception
			exception.Abort("TalentTreeWindow.LoadWindow.LoadObject")


		try:
			self.Header = self.GetChild2("Talenttree_Levelup_Header_02")
			self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))
			self.GetChild("TitleName").SetText(localeInfo.TALENT_TREE_HEADER01)
			self.GetChild("TitleName2").SetText(localeInfo.TALENT_TREE_HEADER02)
			
			self.Skill_01_default = self.GetChild("Skill_01_default")
			self.Skill_01_active = self.GetChild("Skill_01_active")
			if constInfo.SKILL_LEARNED[0][0] == 0:
				self.Skill_01_active.Hide()
			if constInfo.SKILL_LEARNED[0][0] == 1:
				self.Skill_01_default.Hide()
				self.Skill_01_active.Show()
				
			
			self.Skill_02_default = self.GetChild("Skill_02_default")
			self.Skill_02_active = self.GetChild("Skill_02_active")
			if constInfo.SKILL_LEARNED[0][1] == 0:
				self.Skill_02_active.Hide()
			if constInfo.SKILL_LEARNED[0][1] == 1:
				self.Skill_02_default.Hide()
				self.Skill_02_active.Show()
			
			self.Skill_03_default = self.GetChild("Skill_03_default")
			self.Skill_03_active = self.GetChild("Skill_03_active")
			if constInfo.SKILL_LEARNED[0][2] == 0:
				self.Skill_03_active.Hide()
			if constInfo.SKILL_LEARNED[0][2] == 1:
				self.Skill_03_default.Hide()
				self.Skill_03_active.Show()
			
			self.Skill_04_default = self.GetChild("Skill_04_default")
			self.Skill_04_active = self.GetChild("Skill_04_active")
			if constInfo.SKILL_LEARNED[0][3] == 0:
				self.Skill_04_active.Hide()
			if constInfo.SKILL_LEARNED[0][3] == 1:
				self.Skill_04_default.Hide()
				self.Skill_04_active.Show()
			
			self.Skill_05_default = self.GetChild("Skill_05_default")
			self.Skill_05_active = self.GetChild("Skill_05_active")
			if constInfo.SKILL_LEARNED[0][4] == 0:
				self.Skill_05_active.Hide()
			if constInfo.SKILL_LEARNED[0][4] == 1:
				self.Skill_05_default.Hide()
				self.Skill_05_active.Show()
			
			self.Skill_06_default = self.GetChild("Skill_06_default")
			self.Skill_06_active = self.GetChild("Skill_06_active")
			if constInfo.SKILL_LEARNED[1][0] == 0:
				self.Skill_06_active.Hide()
			if constInfo.SKILL_LEARNED[1][0] == 1:
				self.Skill_06_default.Hide()
				self.Skill_06_active.Show()
			
			self.Skill_07_default = self.GetChild("Skill_07_default")
			self.Skill_07_active = self.GetChild("Skill_07_active")
			if constInfo.SKILL_LEARNED[1][1] == 0:
				self.Skill_07_active.Hide()
			if constInfo.SKILL_LEARNED[1][1] == 1:
				self.Skill_07_default.Hide()
				self.Skill_07_active.Show()
			
			self.Skill_08_default = self.GetChild("Skill_08_default")
			self.Skill_08_active = self.GetChild("Skill_08_active")
			if constInfo.SKILL_LEARNED[1][2] == 0:
				self.Skill_08_active.Hide()
			if constInfo.SKILL_LEARNED[1][2] == 1:
				self.Skill_08_default.Hide()
				self.Skill_08_active.Show()
			
			self.Skill_09_default = self.GetChild("Skill_09_default")
			self.Skill_09_active = self.GetChild("Skill_09_active")
			if constInfo.SKILL_LEARNED[1][3] == 0:
				self.Skill_09_active.Hide()
			if constInfo.SKILL_LEARNED[1][3] == 1:
				self.Skill_09_default.Hide()
				self.Skill_09_active.Show()
			
			self.Skill_10_default = self.GetChild("Skill_10_default")
			self.Skill_10_active = self.GetChild("Skill_10_active")
			if constInfo.SKILL_LEARNED[2][0] == 0:
				self.Skill_10_active.Hide()
			if constInfo.SKILL_LEARNED[2][0] == 1:
				self.Skill_10_default.Hide()
				self.Skill_10_active.Show()
			
			self.Skill_11_default = self.GetChild("Skill_11_default")
			self.Skill_11_active = self.GetChild("Skill_11_active")
			if constInfo.SKILL_LEARNED[2][1] == 0:
				self.Skill_11_active.Hide()
			if constInfo.SKILL_LEARNED[2][1] == 1:
				self.Skill_11_default.Hide()
				self.Skill_11_active.Show()
			
			self.Skill_12_default = self.GetChild("Skill_12_default")
			self.Skill_12_active = self.GetChild("Skill_12_active")
			if constInfo.SKILL_LEARNED[2][2] == 0:
				self.Skill_12_active.Hide()
			if constInfo.SKILL_LEARNED[2][2] == 1:
				self.Skill_12_default.Hide()
				self.Skill_12_active.Show()
			
			self.Skill_13_default = self.GetChild("Skill_13_default")
			self.Skill_13_active = self.GetChild("Skill_13_active")
			if constInfo.SKILL_LEARNED[3][0] == 0:
				self.Skill_13_active.Hide()
			if constInfo.SKILL_LEARNED[3][0] == 1:
				self.Skill_13_default.Hide()
				self.Skill_13_active.Show()
			
			self.Skill_14_default = self.GetChild("Skill_14_default")
			self.Skill_14_active = self.GetChild("Skill_14_active")
			if constInfo.SKILL_LEARNED[3][1] == 0:
				self.Skill_14_active.Hide()
			if constInfo.SKILL_LEARNED[3][1] == 1:
				self.Skill_14_default.Hide()
				self.Skill_14_active.Show()
			
			self.Skill_15_default = self.GetChild("Skill_15_default")
			self.Skill_15_active = self.GetChild("Skill_15_active")
			if constInfo.SKILL_LEARNED[4][0] == 0:
				self.Skill_15_active.Hide()
			if constInfo.SKILL_LEARNED[4][0] == 1:
				self.Skill_15_default.Hide()
				self.Skill_15_active.Show()
			
			self.Skill_01_Points = self.GetChild("Skill_01_Points")
			self.Skill_02_Points = self.GetChild("Skill_02_Points")
			self.Skill_03_Points = self.GetChild("Skill_03_Points")
			self.Skill_04_Points = self.GetChild("Skill_04_Points")
			self.Skill_05_Points = self.GetChild("Skill_05_Points")
			self.Skill_06_Points = self.GetChild("Skill_06_Points")
			self.Skill_07_Points = self.GetChild("Skill_07_Points")
			self.Skill_08_Points = self.GetChild("Skill_08_Points")
			self.Skill_09_Points = self.GetChild("Skill_09_Points")
			self.Skill_10_Points = self.GetChild("Skill_10_Points")
			self.Skill_11_Points = self.GetChild("Skill_11_Points")
			self.Skill_12_Points = self.GetChild("Skill_12_Points")
			self.Skill_13_Points = self.GetChild("Skill_13_Points")
			self.Skill_14_Points = self.GetChild("Skill_14_Points")
			self.Skill_15_Points = self.GetChild("Skill_15_Points")

			SkillUp_01 = ui.Button()
			if constInfo.SKILL_LEARNED[0][0] == 0:
				SkillUp_01.SetParent(self.Skill_01_default)
			if constInfo.SKILL_LEARNED[0][0] == 1:
				SkillUp_01.SetParent(self.Skill_01_active)
			SkillUp_01.SetPosition(0, 20)
			SkillUp_01.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_01.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_01.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_01.SetEvent(self.ChangeSkillText_01)
			self.SkillUp_01 = SkillUp_01
			
			SkillUp_02 = ui.Button()
			if constInfo.SKILL_LEARNED[0][1] == 0:
				SkillUp_02.SetParent(self.Skill_02_default)
			if constInfo.SKILL_LEARNED[0][1] == 1:
				SkillUp_02.SetParent(self.Skill_02_active)
			SkillUp_02.SetPosition(0, 20)
			SkillUp_02.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_02.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_02.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_02.SetEvent(self.ChangeSkillText_02)
			self.SkillUp_02 = SkillUp_02
			
			SkillUp_03 = ui.Button()
			if constInfo.SKILL_LEARNED[0][2] == 0:
				SkillUp_03.SetParent(self.Skill_03_default)
			if constInfo.SKILL_LEARNED[0][2] == 1:
				SkillUp_03.SetParent(self.Skill_03_active)
			SkillUp_03.SetPosition(0, 20)
			SkillUp_03.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_03.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_03.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_03.SetEvent(self.ChangeSkillText_03)
			self.SkillUp_03 = SkillUp_03
			
			SkillUp_04 = ui.Button()
			if constInfo.SKILL_LEARNED[0][3] == 0:
				SkillUp_04.SetParent(self.Skill_04_default)
			if constInfo.SKILL_LEARNED[0][3] == 1:
				SkillUp_04.SetParent(self.Skill_04_active)
			SkillUp_04.SetPosition(0, 20)
			SkillUp_04.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_04.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_04.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_04.SetEvent(self.ChangeSkillText_04)
			self.SkillUp_04 = SkillUp_04
			
			SkillUp_05 = ui.Button()
			if constInfo.SKILL_LEARNED[0][4] == 0:
				SkillUp_05.SetParent(self.Skill_05_default)
			if constInfo.SKILL_LEARNED[0][4] == 1:
				SkillUp_05.SetParent(self.Skill_05_active)
			SkillUp_05.SetPosition(0, 20)
			SkillUp_05.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_05.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_05.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_05.SetEvent(self.ChangeSkillText_05)
			self.SkillUp_05 = SkillUp_05
			
			SkillUp_06 = ui.Button()
			if constInfo.SKILL_LEARNED[1][0] == 0:
				SkillUp_06.SetParent(self.Skill_06_default)
			if constInfo.SKILL_LEARNED[1][0] == 1:
				SkillUp_06.SetParent(self.Skill_06_active)
			SkillUp_06.SetPosition(0, 20)
			SkillUp_06.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_06.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_06.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_06.SetEvent(self.ChangeSkillText_06)
			self.SkillUp_06 = SkillUp_06
			
			SkillUp_07 = ui.Button()
			if constInfo.SKILL_LEARNED[1][1] == 0:
				SkillUp_07.SetParent(self.Skill_07_default)
			if constInfo.SKILL_LEARNED[1][1] == 1:
				SkillUp_07.SetParent(self.Skill_07_active)
			SkillUp_07.SetPosition(0, 20)
			SkillUp_07.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_07.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_07.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_07.SetEvent(self.ChangeSkillText_07)
			self.SkillUp_07 = SkillUp_07
			
			SkillUp_08 = ui.Button()
			if constInfo.SKILL_LEARNED[1][2] == 0:
				SkillUp_08.SetParent(self.Skill_08_default)
			if constInfo.SKILL_LEARNED[1][2] == 1:
				SkillUp_08.SetParent(self.Skill_08_active)
			SkillUp_08.SetPosition(0, 20)
			SkillUp_08.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_08.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_08.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_08.SetEvent(self.ChangeSkillText_08)
			self.SkillUp_08 = SkillUp_08
			
			SkillUp_09 = ui.Button()
			if constInfo.SKILL_LEARNED[1][3] == 0:
				SkillUp_09.SetParent(self.Skill_09_default)
			if constInfo.SKILL_LEARNED[1][3] == 1:
				SkillUp_09.SetParent(self.Skill_09_active)
			SkillUp_09.SetPosition(0, 20)
			SkillUp_09.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_09.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_09.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_09.SetEvent(self.ChangeSkillText_09)
			self.SkillUp_09 = SkillUp_09
			
			SkillUp_10 = ui.Button()
			if constInfo.SKILL_LEARNED[2][0] == 0:
				SkillUp_10.SetParent(self.Skill_10_default)
			if constInfo.SKILL_LEARNED[2][0] == 1:
				SkillUp_10.SetParent(self.Skill_10_active)
			SkillUp_10.SetPosition(0, 20)
			SkillUp_10.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_10.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_10.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_10.SetEvent(self.ChangeSkillText_10)
			self.SkillUp_10 = SkillUp_10
			
			SkillUp_11 = ui.Button()
			if constInfo.SKILL_LEARNED[2][1] == 0:
				SkillUp_11.SetParent(self.Skill_11_default)
			if constInfo.SKILL_LEARNED[2][1] == 1:
				SkillUp_11.SetParent(self.Skill_11_active)
			SkillUp_11.SetPosition(0, 20)
			SkillUp_11.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_11.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_11.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_11.SetEvent(self.ChangeSkillText_11)
			self.SkillUp_11 = SkillUp_11
			
			SkillUp_12 = ui.Button()
			if constInfo.SKILL_LEARNED[2][2] == 0:
				SkillUp_12.SetParent(self.Skill_12_default)
			if constInfo.SKILL_LEARNED[2][2] == 1:
				SkillUp_12.SetParent(self.Skill_12_active)
			SkillUp_12.SetPosition(0, 20)
			SkillUp_12.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_12.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_12.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_12.SetEvent(self.ChangeSkillText_12)
			self.SkillUp_12 = SkillUp_12
			
			SkillUp_13 = ui.Button()
			if constInfo.SKILL_LEARNED[3][0] == 0:
				SkillUp_13.SetParent(self.Skill_13_default)
			if constInfo.SKILL_LEARNED[3][0] == 1:
				SkillUp_13.SetParent(self.Skill_13_active)
			SkillUp_13.SetPosition(0, 20)
			SkillUp_13.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_13.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_13.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_13.SetEvent(self.ChangeSkillText_13)
			self.SkillUp_13 = SkillUp_13
			
			SkillUp_14 = ui.Button()
			if constInfo.SKILL_LEARNED[3][1] == 0:
				SkillUp_14.SetParent(self.Skill_14_default)
			if constInfo.SKILL_LEARNED[3][1] == 1:
				SkillUp_14.SetParent(self.Skill_14_active)
			SkillUp_14.SetPosition(0, 20)
			SkillUp_14.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_14.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_14.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_14.SetEvent(self.ChangeSkillText_14)
			self.SkillUp_14 = SkillUp_14
			
			SkillUp_15 = ui.Button()
			if constInfo.SKILL_LEARNED[4][0] == 0:
				SkillUp_15.SetParent(self.Skill_15_default)
			if constInfo.SKILL_LEARNED[4][0] == 1:
				SkillUp_15.SetParent(self.Skill_15_active)
			SkillUp_15.SetPosition(0, 20)
			SkillUp_15.SetUpVisual("d:/ymir work/ui/talent_tree_v1/plus_button_default.tga")
			SkillUp_15.SetOverVisual("d:/ymir work/ui/talent_tree_v1/plus_button_over.tga")
			SkillUp_15.SetDownVisual("d:/ymir work/ui/talent_tree_v1/plus_button_down.tga")
			SkillUp_15.SetEvent(self.ChangeSkillText_15)
			self.SkillUp_15 = SkillUp_15

		except:
			import exception
			exception.Abort("TalentTreeWindow.LoadWindow.BindObject")

		self.BuildElements()
		
		self.GetChild("TitleBar").SetCloseEvent(ui.__mem_func__(self.Close))


	def ChangeSkillText_01(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_01')
		if constInfo.SKILL_LEARNED[0][0] == 0:
			self.Skill_01_default.Hide()
			self.Skill_01_active.Show()
			self.Skill_01_Points.SetText("%d" % constInfo.SKILL_POINTS[0][0])
			self.Skill_01_Points.SetParent(self.Skill_01_active)
			self.SkillUp_01.SetParent(self.Skill_01_active)
			constInfo.SKILL_LEARNED[0][0] = 1
		if constInfo.SKILL_LEARNED[0][0] == 1:
			self.Skill_01_Points.SetText("%d" % constInfo.SKILL_POINTS[0][0])
		
	def ChangeSkillText_02(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_02')
		if constInfo.SKILL_LEARNED[0][1] == 0:
			self.Skill_02_default.Hide()
			self.Skill_02_active.Show()
			self.Skill_02_Points.SetText("%d" % constInfo.SKILL_POINTS[0][1])
			self.Skill_02_Points.SetParent(self.Skill_02_active)
			self.SkillUp_02.SetParent(self.Skill_02_active)
			constInfo.SKILL_LEARNED[0][1] = 1
		if constInfo.SKILL_LEARNED[0][1] == 1:
			self.Skill_02_Points.SetText("%d" % constInfo.SKILL_POINTS[0][1])
		
	def ChangeSkillText_03(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_03')
		if constInfo.SKILL_LEARNED[0][2] == 0:
			self.Skill_03_default.Hide()
			self.Skill_03_active.Show()
			self.Skill_03_Points.SetText("%d" % constInfo.SKILL_POINTS[0][2])
			self.Skill_03_Points.SetParent(self.Skill_03_active)
			self.SkillUp_03.SetParent(self.Skill_03_active)
			constInfo.SKILL_LEARNED[0][2] = 1
		if constInfo.SKILL_LEARNED[0][2] == 1:
			self.Skill_03_Points.SetText("%d" % constInfo.SKILL_POINTS[0][2])
		
	def ChangeSkillText_04(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_04')
		if constInfo.SKILL_LEARNED[0][3] == 0:
			self.Skill_04_default.Hide()
			self.Skill_04_active.Show()
			self.Skill_04_Points.SetText("%d" % constInfo.SKILL_POINTS[0][3])
			self.Skill_04_Points.SetParent(self.Skill_04_active)
			self.SkillUp_04.SetParent(self.Skill_04_active)
			constInfo.SKILL_LEARNED[0][3] = 1
		if constInfo.SKILL_LEARNED[0][3] == 1:
			self.Skill_04_Points.SetText("%d" % constInfo.SKILL_POINTS[0][3])
		
	def ChangeSkillText_05(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_05')
		if constInfo.SKILL_LEARNED[0][4] == 0:
			self.Skill_05_default.Hide()
			self.Skill_05_active.Show()
			self.Skill_05_Points.SetText("%d" % constInfo.SKILL_POINTS[0][4])
			self.Skill_05_Points.SetParent(self.Skill_05_active)
			self.SkillUp_05.SetParent(self.Skill_05_active)
			constInfo.SKILL_LEARNED[0][4] = 1
		if constInfo.SKILL_LEARNED[0][4] == 1:
			self.Skill_05_Points.SetText("%d" % constInfo.SKILL_POINTS[0][4])
		
	def ChangeSkillText_06(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_06')
		if constInfo.SKILL_LEARNED[1][0] == 0:
			self.Skill_06_default.Hide()
			self.Skill_06_active.Show()
			self.Skill_06_Points.SetText("%d" % constInfo.SKILL_POINTS[1][0])
			self.Skill_06_Points.SetParent(self.Skill_06_active)
			self.SkillUp_06.SetParent(self.Skill_06_active)
			constInfo.SKILL_LEARNED[1][0] = 1
		if constInfo.SKILL_LEARNED[1][0] == 1:
			self.Skill_06_Points.SetText("%d" % constInfo.SKILL_POINTS[1][0])
		
	def ChangeSkillText_07(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_07')
		if constInfo.SKILL_LEARNED[1][1] == 0:
			self.Skill_07_default.Hide()
			self.Skill_07_active.Show()
			self.Skill_07_Points.SetText("%d" % constInfo.SKILL_POINTS[1][1])
			self.Skill_07_Points.SetParent(self.Skill_07_active)
			self.SkillUp_07.SetParent(self.Skill_07_active)
			constInfo.SKILL_LEARNED[1][1] = 1
		if constInfo.SKILL_LEARNED[1][1] == 1:
			self.Skill_07_Points.SetText("%d" % constInfo.SKILL_POINTS[1][1])
		
	def ChangeSkillText_08(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_08')
		if constInfo.SKILL_LEARNED[1][2] == 0:
			self.Skill_08_default.Hide()
			self.Skill_08_active.Show()
			self.Skill_08_Points.SetText("%d" % constInfo.SKILL_POINTS[1][2])
			self.Skill_08_Points.SetParent(self.Skill_08_active)
			self.SkillUp_08.SetParent(self.Skill_08_active)
			constInfo.SKILL_LEARNED[1][2] = 1
		if constInfo.SKILL_LEARNED[1][2] == 1:
			self.Skill_08_Points.SetText("%d" % constInfo.SKILL_POINTS[1][2])
		
	def ChangeSkillText_09(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_09')
		if constInfo.SKILL_LEARNED[1][3] == 0:
			self.Skill_09_default.Hide()
			self.Skill_09_active.Show()
			self.Skill_09_Points.SetText("%d" % constInfo.SKILL_POINTS[1][3])
			self.Skill_09_Points.SetParent(self.Skill_09_active)
			self.SkillUp_09.SetParent(self.Skill_09_active)
			constInfo.SKILL_LEARNED[1][3] = 1
		if constInfo.SKILL_LEARNED[1][3] == 1:
			self.Skill_09_Points.SetText("%d" % constInfo.SKILL_POINTS[1][3])
		
	def ChangeSkillText_10(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_10')
		if constInfo.SKILL_LEARNED[2][0] == 0:
			self.Skill_10_default.Hide()
			self.Skill_10_active.Show()
			self.Skill_10_Points.SetText("%d" % constInfo.SKILL_POINTS[2][0])
			self.Skill_10_Points.SetParent(self.Skill_10_active)
			self.SkillUp_10.SetParent(self.Skill_10_active)
			constInfo.SKILL_LEARNED[2][0] = 1
		if constInfo.SKILL_LEARNED[2][0] == 1:
			self.Skill_10_Points.SetText("%d" % constInfo.SKILL_POINTS[2][0])
		
	def ChangeSkillText_11(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_11')
		if constInfo.SKILL_LEARNED[2][1] == 0:
			self.Skill_11_default.Hide()
			self.Skill_11_active.Show()
			self.Skill_11_Points.SetText("%d" % constInfo.SKILL_POINTS[2][1])
			self.Skill_11_Points.SetParent(self.Skill_11_active)
			self.SkillUp_11.SetParent(self.Skill_11_active)
			constInfo.SKILL_LEARNED[2][1] = 1
		if constInfo.SKILL_LEARNED[2][1] == 1:
			self.Skill_11_Points.SetText("%d" % constInfo.SKILL_POINTS[2][1])
		
	def ChangeSkillText_12(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_12')
		if constInfo.SKILL_LEARNED[2][2] == 0:
			self.Skill_12_default.Hide()
			self.Skill_12_active.Show()
			self.Skill_12_Points.SetText("%d" % constInfo.SKILL_POINTS[2][2])
			self.Skill_12_Points.SetParent(self.Skill_12_active)
			self.SkillUp_12.SetParent(self.Skill_12_active)
			constInfo.SKILL_LEARNED[2][2] = 1
		if constInfo.SKILL_LEARNED[2][2] == 1:
			self.Skill_12_Points.SetText("%d" % constInfo.SKILL_POINTS[2][2])
		
	def ChangeSkillText_13(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_13')
		if constInfo.SKILL_LEARNED[3][0] == 0:
			self.Skill_13_default.Hide()
			self.Skill_13_active.Show()
			self.Skill_13_Points.SetText("%d" % constInfo.SKILL_POINTS[3][0])
			self.Skill_13_Points.SetParent(self.Skill_13_active)
			self.SkillUp_13.SetParent(self.Skill_13_active)
			constInfo.SKILL_LEARNED[3][0] = 1
		if constInfo.SKILL_LEARNED[3][0] == 1:
			self.Skill_13_Points.SetText("%d" % constInfo.SKILL_POINTS[3][0])
		
	def ChangeSkillText_14(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_14')
		if constInfo.SKILL_LEARNED[3][1] == 0:
			self.Skill_14_default.Hide()
			self.Skill_14_active.Show()
			self.Skill_14_Points.SetText("%d" % constInfo.SKILL_POINTS[3][1])
			self.Skill_14_Points.SetParent(self.Skill_14_active)
			self.SkillUp_14.SetParent(self.Skill_14_active)
			constInfo.SKILL_LEARNED[3][1] = 1
		if constInfo.SKILL_LEARNED[3][1] == 1:
			self.Skill_14_Points.SetText("%d" % constInfo.SKILL_POINTS[3][1])
		
	def ChangeSkillText_15(self):
		talenttree.cqc.SendQuestCommand('TALENT_UP_15')
		if constInfo.SKILL_LEARNED[4][0] == 0:
			self.Skill_15_default.Hide()
			self.Skill_15_active.Show()
			self.Skill_15_Points.SetText("%d" % constInfo.SKILL_POINTS[4][0])
			self.Skill_15_Points.SetParent(self.Skill_15_active)
			self.SkillUp_15.SetParent(self.Skill_15_active)
			constInfo.SKILL_LEARNED[4][0] = 1
		if constInfo.SKILL_LEARNED[4][0] == 1:
			self.Skill_15_Points.SetText("%d" % constInfo.SKILL_POINTS[4][0])

	def __ShowToolTip(self, slotIndex):
		if self.tooltipItem:
			self.tooltipItem.SetChangeLookWindowItem(self.SlotsIndexes[slotIndex])

	def OverInItem(self, slotIndex):
		slotIndex = slotIndex
		self.__ShowToolTip(slotIndex)

	def OverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()
	
	def BuildElements(self):
		self.currentPoints = ui.TextLine()
		self.currentPoints.SetParent(self.Header)
		self.currentPoints.SetPosition(210, 3)
		self.currentPoints.Show()

		## TOOLTIPS ##
		self.tlInfo = uiToolTip.ItemToolTip()
		self.tlInfo.Hide()
		self.tooltipInfo = [self.tlInfo]*5

		self.tlInfo2 = uiToolTip.ItemToolTip()
		self.tlInfo2.Hide()
		self.tooltipInfo2 = [self.tlInfo2]*5
		
		self.tlInfo3 = uiToolTip.ItemToolTip()
		self.tlInfo3.Hide()
		self.tooltipInfo3 = [self.tlInfo3]*5
		
		self.tlInfo4 = uiToolTip.ItemToolTip()
		self.tlInfo4.Hide()
		self.tooltipInfo4 = [self.tlInfo4]*5
		
		self.tlInfo5 = uiToolTip.ItemToolTip()
		self.tlInfo5.Hide()
		self.tooltipInfo5 = [self.tlInfo5]*5
		
		self.tlInfo6 = uiToolTip.ItemToolTip()
		self.tlInfo6.Hide()
		self.tooltipInfo6 = [self.tlInfo6]*5
		
		self.tlInfo7 = uiToolTip.ItemToolTip()
		self.tlInfo7.Hide()
		self.tooltipInfo7 = [self.tlInfo7]*5
		
		self.tlInfo8 = uiToolTip.ItemToolTip()
		self.tlInfo8.Hide()
		self.tooltipInfo8 = [self.tlInfo8]*5
		
		self.tlInfo9 = uiToolTip.ItemToolTip()
		self.tlInfo9.Hide()
		self.tooltipInfo9 = [self.tlInfo9]*5
		
		self.tlInfo10 = uiToolTip.ItemToolTip()
		self.tlInfo10.Hide()
		self.tooltipInfo10 = [self.tlInfo10]*5
		
		self.tlInfo11 = uiToolTip.ItemToolTip()
		self.tlInfo11.Hide()
		self.tooltipInfo11 = [self.tlInfo11]*5
		
		self.tlInfo12 = uiToolTip.ItemToolTip()
		self.tlInfo12.Hide()
		self.tooltipInfo12 = [self.tlInfo12]*5
		
		self.tlInfo13 = uiToolTip.ItemToolTip()
		self.tlInfo13.Hide()
		self.tooltipInfo13 = [self.tlInfo13]*5
		
		self.tlInfo14 = uiToolTip.ItemToolTip()
		self.tlInfo14.Hide()
		self.tooltipInfo14 = [self.tlInfo14]*5
		
		self.tlInfo15 = uiToolTip.ItemToolTip()
		self.tlInfo15.Hide()
		self.tooltipInfo15 = [self.tlInfo15]*5
		

	def OnUpdate(self):
		## TOOLTIPS ##
		for i in xrange(5):
			if self.Skill_01_default.IsIn() or self.Skill_01_active.IsIn():
				if constInfo.ShowToolTip[0][0] == 0:
					self.tlInfo = uiToolTip.ItemToolTip()
					self.tlInfo.Hide()
					self.tooltipInfo = [self.tlInfo]*5
					if constInfo.SKILL_POINTS[0][0] < 5:
						self.InformationText = [localeInfo.SKILL01_TOOLTIP_TITLE,
												localeInfo.SKILL01_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][0] * int(localeInfo.SKILL_STEP_01)),
												localeInfo.S_01_TALENT_DESCR_01,
												localeInfo.S_01_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL01_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][0] * int(localeInfo.SKILL_STEP_01) + int(localeInfo.SKILL_STEP_01))
						]
					else:
						self.InformationText = [localeInfo.SKILL01_TOOLTIP_TITLE,
												localeInfo.SKILL01_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][0] * int(localeInfo.SKILL_STEP_01)),
												localeInfo.S_01_TALENT_DESCR_01,
												localeInfo.S_01_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo[i].SetFollow(True)
						self.tooltipInfo[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo[i].AppendTextLine(self.InformationText[i], TITLE_COLOR)
							self.tlInfo.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo[i].AppendTextLine(self.InformationText[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo[i].AppendTextLine(self.InformationText[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo[i].AppendTextLine(self.InformationText[i], NEGATIVE_COLOR)
						self.tooltipInfo[i].toolTipWidth += 15
					self.tooltipInfo[i].Show()
					constInfo.ShowToolTip[0][0] = 1
			else:
				self.tooltipInfo[i].Hide()
				constInfo.ShowToolTip[0][0] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_02_default.IsIn() or self.Skill_02_active.IsIn():
				if constInfo.ShowToolTip[0][1] == 0:
					self.tlInfo2 = uiToolTip.ItemToolTip()
					self.tlInfo2.Hide()
					self.tooltipInfo2 = [self.tlInfo2]*5
					if constInfo.SKILL_POINTS[0][1] < 5:
						self.InformationText2 = [localeInfo.SKILL02_TOOLTIP_TITLE,
												localeInfo.SKILL02_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][1] * int(localeInfo.SKILL_STEP_02)),
												localeInfo.S_02_TALENT_DESCR_01,
												localeInfo.S_02_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL02_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][1] * int(localeInfo.SKILL_STEP_02) + int(localeInfo.SKILL_STEP_02))
						]
					else:
						self.InformationText2 = [localeInfo.SKILL02_TOOLTIP_TITLE,
												localeInfo.SKILL02_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][1] * int(localeInfo.SKILL_STEP_02)),
												localeInfo.S_02_TALENT_DESCR_01,
												localeInfo.S_02_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo2[i].SetFollow(True)
						self.tooltipInfo2[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo2[i].AppendTextLine(self.InformationText2[i], TITLE_COLOR)
							self.tlInfo2.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo2[i].AppendTextLine(self.InformationText2[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo2.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo2[i].AppendTextLine(self.InformationText2[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo2.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo2[i].AppendTextLine(self.InformationText2[i], NEGATIVE_COLOR)
						self.tooltipInfo2[i].toolTipWidth += 15
					self.tooltipInfo2[i].Show()
					constInfo.ShowToolTip[0][1] = 1
			else:
				self.tooltipInfo2[i].Hide()
				constInfo.ShowToolTip[0][1] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_03_default.IsIn() or self.Skill_03_active.IsIn():
				if constInfo.ShowToolTip[0][2] == 0:
					self.tlInfo3 = uiToolTip.ItemToolTip()
					self.tlInfo3.Hide()
					self.tooltipInfo3 = [self.tlInfo3]*5
					if constInfo.SKILL_POINTS[0][2] < 5:
						self.InformationText3 = [localeInfo.SKILL03_TOOLTIP_TITLE,
												localeInfo.SKILL03_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][2] * int(localeInfo.SKILL_STEP_03)) + "%",
												localeInfo.S_03_TALENT_DESCR_01,
												localeInfo.S_03_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL03_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][2] * int(localeInfo.SKILL_STEP_03) + int(localeInfo.SKILL_STEP_03)) + "%"
						]
					else:
						self.InformationText3 = [localeInfo.SKILL03_TOOLTIP_TITLE,
												localeInfo.SKILL03_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][2] * int(localeInfo.SKILL_STEP_03)) + "%",
												localeInfo.S_03_TALENT_DESCR_01,
												localeInfo.S_03_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo3[i].SetFollow(True)
						self.tooltipInfo3[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo3[i].AppendTextLine(self.InformationText3[i], TITLE_COLOR)
							self.tlInfo3.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo3[i].AppendTextLine(self.InformationText3[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo3.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo3[i].AppendTextLine(self.InformationText3[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo3.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo3[i].AppendTextLine(self.InformationText3[i], NEGATIVE_COLOR)
						self.tooltipInfo3[i].toolTipWidth += 15
					self.tooltipInfo3[i].Show()
					constInfo.ShowToolTip[0][2] = 1
			else:
				self.tooltipInfo3[i].Hide()
				constInfo.ShowToolTip[0][2] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_04_default.IsIn() or self.Skill_04_active.IsIn():
				if constInfo.ShowToolTip[0][3] == 0:
					self.tlInfo4 = uiToolTip.ItemToolTip()
					self.tlInfo4.Hide()
					self.tooltipInfo4 = [self.tlInfo4]*5
					if constInfo.SKILL_POINTS[0][3] < 5:
						self.InformationText4 = [localeInfo.SKILL04_TOOLTIP_TITLE,
												localeInfo.SKILL04_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][3] * int(localeInfo.SKILL_STEP_04)),
												localeInfo.S_04_TALENT_DESCR_01,
												localeInfo.S_04_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL04_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][3] * int(localeInfo.SKILL_STEP_04) + int(localeInfo.SKILL_STEP_04))
						]
					else:
						self.InformationText4 = [localeInfo.SKILL04_TOOLTIP_TITLE,
												localeInfo.SKILL04_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][3] * int(localeInfo.SKILL_STEP_04)),
												localeInfo.S_04_TALENT_DESCR_01,
												localeInfo.S_04_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo4[i].SetFollow(True)
						self.tooltipInfo4[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo4[i].AppendTextLine(self.InformationText4[i], TITLE_COLOR)
							self.tlInfo4.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo4[i].AppendTextLine(self.InformationText4[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo4.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo4[i].AppendTextLine(self.InformationText4[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo4.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo4[i].AppendTextLine(self.InformationText4[i], NEGATIVE_COLOR)
						self.tooltipInfo4[i].toolTipWidth += 15
					self.tooltipInfo4[i].Show()
					constInfo.ShowToolTip[0][3] = 1
			else:
				self.tooltipInfo4[i].Hide()
				constInfo.ShowToolTip[0][3] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_05_default.IsIn() or self.Skill_05_active.IsIn():
				if constInfo.ShowToolTip[0][4] == 0:
					self.tlInfo5 = uiToolTip.ItemToolTip()
					self.tlInfo5.Hide()
					self.tooltipInfo5 = [self.tlInfo5]*5
					if constInfo.SKILL_POINTS[0][4] < 5:
						self.InformationText5 = [localeInfo.SKILL05_TOOLTIP_TITLE,
												localeInfo.SKILL05_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][4] * int(localeInfo.SKILL_STEP_05)),
												localeInfo.S_05_TALENT_DESCR_01,
												localeInfo.S_05_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL05_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][4] * int(localeInfo.SKILL_STEP_05) + int(localeInfo.SKILL_STEP_05))
						]
					else:
						self.InformationText5 = [localeInfo.SKILL05_TOOLTIP_TITLE,
												localeInfo.SKILL05_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[0][4] * int(localeInfo.SKILL_STEP_05)),
												localeInfo.S_05_TALENT_DESCR_01,
												localeInfo.S_05_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo5[i].SetFollow(True)
						self.tooltipInfo5[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo5[i].AppendTextLine(self.InformationText5[i], TITLE_COLOR)
							self.tlInfo5.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo5[i].AppendTextLine(self.InformationText5[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo5.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo5[i].AppendTextLine(self.InformationText5[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo5.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo5[i].AppendTextLine(self.InformationText5[i], NEGATIVE_COLOR)
						self.tooltipInfo5[i].toolTipWidth += 15
					self.tooltipInfo5[i].Show()
					constInfo.ShowToolTip[0][4] = 1
			else:
				self.tooltipInfo5[i].Hide()
				constInfo.ShowToolTip[0][4] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_06_default.IsIn() or self.Skill_06_active.IsIn():
				if constInfo.ShowToolTip[1][0] == 0:
					self.tlInfo6 = uiToolTip.ItemToolTip()
					self.tlInfo6.Hide()
					self.tooltipInfo6 = [self.tlInfo6]*5
					if constInfo.SKILL_POINTS[1][0] < 5:
						self.InformationText6 = [localeInfo.SKILL06_TOOLTIP_TITLE,
												localeInfo.SKILL06_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[1][0] * int(localeInfo.SKILL_STEP_06)),
												localeInfo.S_06_TALENT_DESCR_01,
												localeInfo.S_06_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL06_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[1][0] * int(localeInfo.SKILL_STEP_06) + int(localeInfo.SKILL_STEP_06))
						]
					else:
						self.InformationText6 = [localeInfo.SKILL06_TOOLTIP_TITLE,
												localeInfo.SKILL06_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[1][0] * int(localeInfo.SKILL_STEP_06)),
												localeInfo.S_06_TALENT_DESCR_01,
												localeInfo.S_06_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo6[i].SetFollow(True)
						self.tooltipInfo6[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo6[i].AppendTextLine(self.InformationText6[i], TITLE_COLOR)
							self.tlInfo6.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo6[i].AppendTextLine(self.InformationText6[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo6.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo6[i].AppendTextLine(self.InformationText6[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo6.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo6[i].AppendTextLine(self.InformationText6[i], NEGATIVE_COLOR)
						self.tooltipInfo6[i].toolTipWidth += 15
					self.tooltipInfo6[i].Show()
					constInfo.ShowToolTip[1][0] = 1
			else:
				self.tooltipInfo6[i].Hide()
				constInfo.ShowToolTip[1][0] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_07_default.IsIn() or self.Skill_07_active.IsIn():
				if constInfo.ShowToolTip[1][1] == 0:
					self.tlInfo7 = uiToolTip.ItemToolTip()
					self.tlInfo7.Hide()
					self.tooltipInfo7 = [self.tlInfo7]*5
					if constInfo.SKILL_POINTS[1][1] < 5:
						self.InformationText7 = [localeInfo.SKILL07_TOOLTIP_TITLE,
												localeInfo.SKILL07_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[1][1] * int(localeInfo.SKILL_STEP_07)) + "%",
												localeInfo.S_07_TALENT_DESCR_01,
												localeInfo.S_07_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL07_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[1][1] * int(localeInfo.SKILL_STEP_07) + int(localeInfo.SKILL_STEP_07)) + "%"
						]
					else:
						self.InformationText7 = [localeInfo.SKILL07_TOOLTIP_TITLE,
												localeInfo.SKILL07_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[1][1] * int(localeInfo.SKILL_STEP_07)) + "%",
												localeInfo.S_07_TALENT_DESCR_01,
												localeInfo.S_07_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo7[i].SetFollow(True)
						self.tooltipInfo7[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo7[i].AppendTextLine(self.InformationText7[i], TITLE_COLOR)
							self.tlInfo7.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo7[i].AppendTextLine(self.InformationText7[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo7.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo7[i].AppendTextLine(self.InformationText7[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo7.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo7[i].AppendTextLine(self.InformationText7[i], NEGATIVE_COLOR)
						self.tooltipInfo7[i].toolTipWidth += 15
					self.tooltipInfo7[i].Show()
					constInfo.ShowToolTip[1][1] = 1
			else:
				self.tooltipInfo7[i].Hide()
				constInfo.ShowToolTip[1][1] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_08_default.IsIn() or self.Skill_08_active.IsIn():
				if constInfo.ShowToolTip[1][2] == 0:
					self.tlInfo8 = uiToolTip.ItemToolTip()
					self.tlInfo8.Hide()
					self.tooltipInfo8 = [self.tlInfo8]*5
					if constInfo.SKILL_POINTS[1][2] < 5:
						self.InformationText8 = [localeInfo.SKILL08_TOOLTIP_TITLE,
												localeInfo.SKILL08_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[1][2] * int(localeInfo.SKILL_STEP_08)) + "%",
												localeInfo.S_08_TALENT_DESCR_01,
												localeInfo.S_08_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL08_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[1][2] * int(localeInfo.SKILL_STEP_08) + int(localeInfo.SKILL_STEP_08)) + "%"
						]
					else:
						self.InformationText8 = [localeInfo.SKILL08_TOOLTIP_TITLE,
												localeInfo.SKILL08_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[1][2] * int(localeInfo.SKILL_STEP_08)) + "%",
												localeInfo.S_08_TALENT_DESCR_01,
												localeInfo.S_08_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo8[i].SetFollow(True)
						self.tooltipInfo8[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo8[i].AppendTextLine(self.InformationText8[i], TITLE_COLOR)
							self.tlInfo8.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo8[i].AppendTextLine(self.InformationText8[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo8.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo8[i].AppendTextLine(self.InformationText8[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo8.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo8[i].AppendTextLine(self.InformationText8[i], NEGATIVE_COLOR)
						self.tooltipInfo8[i].toolTipWidth += 15
					self.tooltipInfo8[i].Show()
					constInfo.ShowToolTip[1][2] = 1
			else:
				self.tooltipInfo8[i].Hide()
				constInfo.ShowToolTip[1][2] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_09_default.IsIn() or self.Skill_09_active.IsIn():
				if constInfo.ShowToolTip[1][3] == 0:
					self.tlInfo9 = uiToolTip.ItemToolTip()
					self.tlInfo9.Hide()
					self.tooltipInfo9 = [self.tlInfo9]*5
					if constInfo.SKILL_POINTS[1][3] < 5:
						self.InformationText9 = [localeInfo.SKILL09_TOOLTIP_TITLE,
												localeInfo.SKILL09_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[1][3] * int(localeInfo.SKILL_STEP_09)),
												localeInfo.S_09_TALENT_DESCR_01,
												localeInfo.S_09_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL09_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[1][3] * int(localeInfo.SKILL_STEP_09) + int(localeInfo.SKILL_STEP_09))
						]
					else:
						self.InformationText9 = [localeInfo.SKILL09_TOOLTIP_TITLE,
												localeInfo.SKILL09_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[1][3] * int(localeInfo.SKILL_STEP_09)),
												localeInfo.S_09_TALENT_DESCR_01,
												localeInfo.S_09_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo9[i].SetFollow(True)
						self.tooltipInfo9[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo9[i].AppendTextLine(self.InformationText9[i], TITLE_COLOR)
							self.tlInfo9.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo9[i].AppendTextLine(self.InformationText9[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo9.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo9[i].AppendTextLine(self.InformationText9[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo9.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo9[i].AppendTextLine(self.InformationText9[i], NEGATIVE_COLOR)
						self.tooltipInfo9[i].toolTipWidth += 15
					self.tooltipInfo9[i].Show()
					constInfo.ShowToolTip[1][3] = 1
			else:
				self.tooltipInfo9[i].Hide()
				constInfo.ShowToolTip[1][3] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_10_default.IsIn() or self.Skill_10_active.IsIn():
				if constInfo.ShowToolTip[2][0] == 0:
					self.tlInfo10 = uiToolTip.ItemToolTip()
					self.tlInfo10.Hide()
					self.tooltipInfo10 = [self.tlInfo10]*5
					if constInfo.SKILL_POINTS[2][0] < 5:
						self.InformationText10 = [localeInfo.SKILL10_TOOLTIP_TITLE,
												localeInfo.SKILL10_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[2][0]) + "%",
												localeInfo.S_10_TALENT_DESCR_01,
												localeInfo.S_10_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL10_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[2][0] + int(localeInfo.SKILL_STEP_10)) + "%"
						]
					else:
						self.InformationText10 = [localeInfo.SKILL10_TOOLTIP_TITLE,
												localeInfo.SKILL10_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[2][0]) + "%",
												localeInfo.S_10_TALENT_DESCR_01,
												localeInfo.S_10_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo10[i].SetFollow(True)
						self.tooltipInfo10[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo10[i].AppendTextLine(self.InformationText10[i], TITLE_COLOR)
							self.tlInfo10.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo10[i].AppendTextLine(self.InformationText10[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo10.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo10[i].AppendTextLine(self.InformationText10[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo10.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo10[i].AppendTextLine(self.InformationText10[i], NEGATIVE_COLOR)
						self.tooltipInfo10[i].toolTipWidth += 15
					self.tooltipInfo10[i].Show()
					constInfo.ShowToolTip[2][0] = 1
			else:
				self.tooltipInfo10[i].Hide()
				constInfo.ShowToolTip[2][0] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_11_default.IsIn() or self.Skill_11_active.IsIn():
				if constInfo.ShowToolTip[2][1] == 0:
					self.tlInfo11 = uiToolTip.ItemToolTip()
					self.tlInfo11.Hide()
					self.tooltipInfo11 = [self.tlInfo11]*5
					if constInfo.SKILL_POINTS[2][1] < 5:
						self.InformationText11 = [localeInfo.SKILL11_TOOLTIP_TITLE,
												localeInfo.SKILL11_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[2][1]) + "%",
												localeInfo.S_11_TALENT_DESCR_01,
												localeInfo.S_11_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL11_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[2][1] + int(localeInfo.SKILL_STEP_11)) + "%"
						]
					else:
						self.InformationText11 = [localeInfo.SKILL11_TOOLTIP_TITLE,
												localeInfo.SKILL11_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[2][1]) + "%",
												localeInfo.S_11_TALENT_DESCR_01,
												localeInfo.S_11_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo11[i].SetFollow(True)
						self.tooltipInfo11[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo11[i].AppendTextLine(self.InformationText11[i], TITLE_COLOR)
							self.tlInfo11.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo11[i].AppendTextLine(self.InformationText11[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo11.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo11[i].AppendTextLine(self.InformationText11[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo11.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo11[i].AppendTextLine(self.InformationText11[i], NEGATIVE_COLOR)
						self.tooltipInfo11[i].toolTipWidth += 15
					self.tooltipInfo11[i].Show()
					constInfo.ShowToolTip[2][1] = 1
			else:
				self.tooltipInfo11[i].Hide()
				constInfo.ShowToolTip[2][1] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_12_default.IsIn() or self.Skill_12_active.IsIn():
				if constInfo.ShowToolTip[2][2] == 0:
					self.tlInfo12 = uiToolTip.ItemToolTip()
					self.tlInfo12.Hide()
					self.tooltipInfo12 = [self.tlInfo12]*5
					if constInfo.SKILL_POINTS[2][2] < 5:
						self.InformationText12 = [localeInfo.SKILL12_TOOLTIP_TITLE,
												localeInfo.SKILL12_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[2][2] * int(localeInfo.SKILL_STEP_12)),
												localeInfo.S_12_TALENT_DESCR_01,
												localeInfo.S_12_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL12_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[2][2] * int(localeInfo.SKILL_STEP_12) + int(localeInfo.SKILL_STEP_12))
						]
					else:
						self.InformationText12 = [localeInfo.SKILL12_TOOLTIP_TITLE,
												localeInfo.SKILL12_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[2][2] * int(localeInfo.SKILL_STEP_12)),
												localeInfo.S_12_TALENT_DESCR_01,
												localeInfo.S_12_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo12[i].SetFollow(True)
						self.tooltipInfo12[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo12[i].AppendTextLine(self.InformationText12[i], TITLE_COLOR)
							self.tlInfo12.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo12[i].AppendTextLine(self.InformationText12[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo12.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo12[i].AppendTextLine(self.InformationText12[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo12.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo12[i].AppendTextLine(self.InformationText12[i], NEGATIVE_COLOR)
						self.tooltipInfo12[i].toolTipWidth += 15
					self.tooltipInfo12[i].Show()
					constInfo.ShowToolTip[2][2] = 1
			else:
				self.tooltipInfo12[i].Hide()
				constInfo.ShowToolTip[2][2] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_13_default.IsIn() or self.Skill_13_active.IsIn():
				if constInfo.ShowToolTip[3][0] == 0:
					self.tlInfo13 = uiToolTip.ItemToolTip()
					self.tlInfo13.Hide()
					self.tooltipInfo13 = [self.tlInfo13]*5
					if constInfo.SKILL_POINTS[3][0] < 5:
						self.InformationText13 = [localeInfo.SKILL13_TOOLTIP_TITLE,
												localeInfo.SKILL13_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[3][0] * int(localeInfo.SKILL_STEP_13)) + "%",
												localeInfo.S_13_TALENT_DESCR_01,
												localeInfo.S_13_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL13_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[3][0] * int(localeInfo.SKILL_STEP_13) + int(localeInfo.SKILL_STEP_13)) + "%"
						]
					else:
						self.InformationText13 = [localeInfo.SKILL13_TOOLTIP_TITLE,
												localeInfo.SKILL13_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[3][0] * int(localeInfo.SKILL_STEP_13)) + "%",
												localeInfo.S_13_TALENT_DESCR_01,
												localeInfo.S_13_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo13[i].SetFollow(True)
						self.tooltipInfo13[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo13[i].AppendTextLine(self.InformationText13[i], TITLE_COLOR)
							self.tlInfo13.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo13[i].AppendTextLine(self.InformationText13[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo13.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo13[i].AppendTextLine(self.InformationText13[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo13.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo13[i].AppendTextLine(self.InformationText13[i], NEGATIVE_COLOR)
						self.tooltipInfo13[i].toolTipWidth += 15
					self.tooltipInfo13[i].Show()
					constInfo.ShowToolTip[3][0] = 1
			else:
				self.tooltipInfo13[i].Hide()
				constInfo.ShowToolTip[3][0] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_14_default.IsIn() or self.Skill_14_active.IsIn():
				if constInfo.ShowToolTip[3][1] == 0:
					self.tlInfo14 = uiToolTip.ItemToolTip()
					self.tlInfo14.Hide()
					self.tooltipInfo14 = [self.tlInfo14]*5
					if constInfo.SKILL_POINTS[3][1] < 5:
						self.InformationText14 = [localeInfo.SKILL14_TOOLTIP_TITLE,
												localeInfo.SKILL14_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[3][1] * int(localeInfo.SKILL_STEP_14)) + "%",
												localeInfo.S_14_TALENT_DESCR_01,
												localeInfo.S_14_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL14_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[3][1] * int(localeInfo.SKILL_STEP_14) + int(localeInfo.SKILL_STEP_14)) + "%"
						]
					else:
						self.InformationText14 = [localeInfo.SKILL14_TOOLTIP_TITLE,
												localeInfo.SKILL14_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[3][1] * int(localeInfo.SKILL_STEP_14)) + "%",
												localeInfo.S_14_TALENT_DESCR_01,
												localeInfo.S_14_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo14[i].SetFollow(True)
						self.tooltipInfo14[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo14[i].AppendTextLine(self.InformationText14[i], TITLE_COLOR)
							self.tlInfo14.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo14[i].AppendTextLine(self.InformationText14[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo14.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo14[i].AppendTextLine(self.InformationText14[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo14.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo14[i].AppendTextLine(self.InformationText14[i], NEGATIVE_COLOR)
						self.tooltipInfo14[i].toolTipWidth += 15
					self.tooltipInfo14[i].Show()
					constInfo.ShowToolTip[3][1] = 1
			else:
				self.tooltipInfo14[i].Hide()
				constInfo.ShowToolTip[3][1] = 0
##############################################################
		for i in xrange(5):
			if self.Skill_15_default.IsIn() or self.Skill_15_active.IsIn():
				if constInfo.ShowToolTip[4][0] == 0:
					self.tlInfo15 = uiToolTip.ItemToolTip()
					self.tlInfo15.Hide()
					self.tooltipInfo15 = [self.tlInfo15]*5
					if constInfo.SKILL_POINTS[4][0] < 5:
						self.InformationText15 = [localeInfo.SKILL15_TOOLTIP_TITLE,
												localeInfo.SKILL15_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[4][0]) + "%",
												localeInfo.S_15_TALENT_DESCR_01,
												localeInfo.S_15_TALENT_DESCR_02,
												localeInfo.NEW_LEVEL_DESCR + " " + localeInfo.SKILL15_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[4][0] + int(localeInfo.SKILL_STEP_15)) + "%"
						]
					else:
						self.InformationText15 = [localeInfo.SKILL15_TOOLTIP_TITLE,
												localeInfo.SKILL15_TOOLTIP_LINE1 + " +%d" % int(constInfo.SKILL_POINTS[4][0]) + "%",
												localeInfo.S_15_TALENT_DESCR_01,
												localeInfo.S_15_TALENT_DESCR_02,
												"(MAX.) "
						]

					for i in xrange(5):
						self.tooltipInfo15[i].SetFollow(True)
						self.tooltipInfo15[i].AlignHorizonalCenter()
						if i == 0:
							TITLE_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
							self.tooltipInfo15[i].AppendTextLine(self.InformationText15[i], TITLE_COLOR)
							self.tlInfo15.AppendSpace(5)
						elif i == 1:
							SPECIAL_POSITIVE_COLOR = grp.GenerateColor(0.6911, 0.8754, 0.7068, 1.0)
							self.tooltipInfo15[i].AppendTextLine(self.InformationText15[i], SPECIAL_POSITIVE_COLOR)
							self.tlInfo15.AppendSpace(5)
						elif i == 2 or i == 3:
							DESCR_COLOR = 0xffBEB47D
							self.tooltipInfo15[i].AppendTextLine(self.InformationText15[i], DESCR_COLOR)
						elif i == 4:
							self.tlInfo15.AppendSpace(5)
							NEGATIVE_COLOR = grp.GenerateColor(0.9, 0.4745, 0.4627, 1.0)
							self.tooltipInfo15[i].AppendTextLine(self.InformationText15[i], NEGATIVE_COLOR)
						self.tooltipInfo15[i].toolTipWidth += 15
					self.tooltipInfo15[i].Show()
					constInfo.ShowToolTip[4][0] = 1
			else:
				self.tooltipInfo15[i].Hide()
				constInfo.ShowToolTip[4][0] = 0
##############################################################
		
		self.currentPoints.SetText("verf.: [ %d" % constInfo.CURRENT_POINTS + " ]")
		
		self.Skill_01_Points.SetText("%d" % constInfo.SKILL_POINTS[0][0])
		self.Skill_02_Points.SetText("%d" % constInfo.SKILL_POINTS[0][1])
		self.Skill_03_Points.SetText("%d" % constInfo.SKILL_POINTS[0][2])
		self.Skill_04_Points.SetText("%d" % constInfo.SKILL_POINTS[0][3])
		self.Skill_05_Points.SetText("%d" % constInfo.SKILL_POINTS[0][4])
		self.Skill_06_Points.SetText("%d" % constInfo.SKILL_POINTS[1][0])
		self.Skill_07_Points.SetText("%d" % constInfo.SKILL_POINTS[1][1])
		self.Skill_08_Points.SetText("%d" % constInfo.SKILL_POINTS[1][2])
		self.Skill_09_Points.SetText("%d" % constInfo.SKILL_POINTS[1][3])
		self.Skill_10_Points.SetText("%d" % constInfo.SKILL_POINTS[2][0])
		self.Skill_11_Points.SetText("%d" % constInfo.SKILL_POINTS[2][1])
		self.Skill_12_Points.SetText("%d" % constInfo.SKILL_POINTS[2][2])
		self.Skill_13_Points.SetText("%d" % constInfo.SKILL_POINTS[3][0])
		self.Skill_14_Points.SetText("%d" % constInfo.SKILL_POINTS[3][1])
		self.Skill_15_Points.SetText("%d" % constInfo.SKILL_POINTS[4][0])
		
		
		if constInfo.SKILL_LEARNED[0][0] == 1:
			self.Skill_01_default.Hide()
			self.Skill_01_active.Show()
			self.Skill_01_Points.SetText("%d" % constInfo.SKILL_POINTS[0][0])
			self.Skill_01_Points.SetParent(self.Skill_01_active)
			self.SkillUp_01.SetParent(self.Skill_01_active)
		if constInfo.SKILL_LEARNED[0][0] == 0:
			self.Skill_01_active.Hide()
			self.Skill_01_default.Show()
			self.Skill_01_Points.SetText("-")
			self.Skill_01_Points.SetParent(self.Skill_01_default)
			self.SkillUp_01.SetParent(self.Skill_01_default)
		
		if constInfo.SKILL_LEARNED[0][1] == 1:
			self.Skill_02_default.Hide()
			self.Skill_02_active.Show()
			self.Skill_02_Points.SetText("%d" % constInfo.SKILL_POINTS[0][1])
			self.Skill_02_Points.SetParent(self.Skill_02_active)
			self.SkillUp_02.SetParent(self.Skill_02_active)
		if constInfo.SKILL_LEARNED[0][1] == 0:
			self.Skill_02_active.Hide()
			self.Skill_02_default.Show()
			self.Skill_02_Points.SetText("-")
			self.Skill_02_Points.SetParent(self.Skill_02_default)
			self.SkillUp_02.SetParent(self.Skill_02_default)
			
		if constInfo.SKILL_LEARNED[0][2] == 1:
			self.Skill_03_default.Hide()
			self.Skill_03_active.Show()
			self.Skill_03_Points.SetText("%d" % constInfo.SKILL_POINTS[0][2])
			self.Skill_03_Points.SetParent(self.Skill_03_active)
			self.SkillUp_03.SetParent(self.Skill_03_active)
		if constInfo.SKILL_LEARNED[0][2] == 0:
			self.Skill_03_active.Hide()
			self.Skill_03_default.Show()
			self.Skill_03_Points.SetText("-")
			self.Skill_03_Points.SetParent(self.Skill_03_default)
			self.SkillUp_03.SetParent(self.Skill_03_default)
			
		if constInfo.SKILL_LEARNED[0][3] == 1:
			self.Skill_04_default.Hide()
			self.Skill_04_active.Show()
			self.Skill_04_Points.SetText("%d" % constInfo.SKILL_POINTS[0][3])
			self.Skill_04_Points.SetParent(self.Skill_04_active)
			self.SkillUp_04.SetParent(self.Skill_04_active)
		if constInfo.SKILL_LEARNED[0][3] == 0:
			self.Skill_04_active.Hide()
			self.Skill_04_default.Show()
			self.Skill_04_Points.SetText("-")
			self.Skill_04_Points.SetParent(self.Skill_04_default)
			self.SkillUp_04.SetParent(self.Skill_04_default)
		
		if constInfo.SKILL_LEARNED[0][4] == 1:
			self.Skill_05_default.Hide()
			self.Skill_05_active.Show()
			self.Skill_05_Points.SetText("%d" % constInfo.SKILL_POINTS[0][4])
			self.Skill_05_Points.SetParent(self.Skill_05_active)
			self.SkillUp_05.SetParent(self.Skill_05_active)
		if constInfo.SKILL_LEARNED[0][4] == 0:
			self.Skill_05_active.Hide()
			self.Skill_05_default.Show()
			self.Skill_05_Points.SetText("-")
			self.Skill_05_Points.SetParent(self.Skill_05_default)
			self.SkillUp_05.SetParent(self.Skill_05_default)
			
		if constInfo.SKILL_LEARNED[1][0] == 1:
			self.Skill_06_default.Hide()
			self.Skill_06_active.Show()
			self.Skill_06_Points.SetText("%d" % constInfo.SKILL_POINTS[1][0])
			self.Skill_06_Points.SetParent(self.Skill_06_active)
			self.SkillUp_06.SetParent(self.Skill_06_active)
		if constInfo.SKILL_LEARNED[1][0] == 0:
			self.Skill_06_active.Hide()
			self.Skill_06_default.Show()
			self.Skill_06_Points.SetText("-")
			self.Skill_06_Points.SetParent(self.Skill_06_default)
			self.SkillUp_06.SetParent(self.Skill_06_default)
			
		if constInfo.SKILL_LEARNED[1][1] == 1:
			self.Skill_07_default.Hide()
			self.Skill_07_active.Show()
			self.Skill_07_Points.SetText("%d" % constInfo.SKILL_POINTS[1][1])
			self.Skill_07_Points.SetParent(self.Skill_07_active)
			self.SkillUp_07.SetParent(self.Skill_07_active)
		if constInfo.SKILL_LEARNED[1][1] == 0:
			self.Skill_07_active.Hide()
			self.Skill_07_default.Show()
			self.Skill_07_Points.SetText("-")
			self.Skill_07_Points.SetParent(self.Skill_07_default)
			self.SkillUp_07.SetParent(self.Skill_07_default)
		
		if constInfo.SKILL_LEARNED[1][2] == 1:
			self.Skill_08_default.Hide()
			self.Skill_08_active.Show()
			self.Skill_08_Points.SetText("%d" % constInfo.SKILL_POINTS[1][2])
			self.Skill_08_Points.SetParent(self.Skill_08_active)
			self.SkillUp_08.SetParent(self.Skill_08_active)
		if constInfo.SKILL_LEARNED[1][2] == 0:
			self.Skill_08_active.Hide()
			self.Skill_08_default.Show()
			self.Skill_08_Points.SetText("-")
			self.Skill_08_Points.SetParent(self.Skill_08_default)
			self.SkillUp_08.SetParent(self.Skill_08_default)
			
		if constInfo.SKILL_LEARNED[1][3] == 1:
			self.Skill_09_default.Hide()
			self.Skill_09_active.Show()
			self.Skill_09_Points.SetText("%d" % constInfo.SKILL_POINTS[1][3])
			self.Skill_09_Points.SetParent(self.Skill_09_active)
			self.SkillUp_09.SetParent(self.Skill_09_active)
		if constInfo.SKILL_LEARNED[1][3] == 0:
			self.Skill_09_active.Hide()
			self.Skill_09_default.Show()
			self.Skill_09_Points.SetText("-")
			self.Skill_09_Points.SetParent(self.Skill_09_default)
			self.SkillUp_09.SetParent(self.Skill_09_default)
			
		if constInfo.SKILL_LEARNED[2][0] == 1:
			self.Skill_10_default.Hide()
			self.Skill_10_active.Show()
			self.Skill_10_Points.SetText("%d" % constInfo.SKILL_POINTS[2][0])
			self.Skill_10_Points.SetParent(self.Skill_10_active)
			self.SkillUp_10.SetParent(self.Skill_10_active)
		if constInfo.SKILL_LEARNED[2][0] == 0:
			self.Skill_10_active.Hide()
			self.Skill_10_default.Show()
			self.Skill_10_Points.SetText("-")
			self.Skill_10_Points.SetParent(self.Skill_10_default)
			self.SkillUp_10.SetParent(self.Skill_10_default)
		
		if constInfo.SKILL_LEARNED[2][1] == 1:
			self.Skill_11_default.Hide()
			self.Skill_11_active.Show()
			self.Skill_11_Points.SetText("%d" % constInfo.SKILL_POINTS[2][1])
			self.Skill_11_Points.SetParent(self.Skill_11_active)
			self.SkillUp_11.SetParent(self.Skill_11_active)
		if constInfo.SKILL_LEARNED[2][1] == 0:
			self.Skill_11_active.Hide()
			self.Skill_11_default.Show()
			self.Skill_11_Points.SetText("-")
			self.Skill_11_Points.SetParent(self.Skill_11_default)
			self.SkillUp_11.SetParent(self.Skill_11_default)
			
		if constInfo.SKILL_LEARNED[2][2] == 1:
			self.Skill_12_default.Hide()
			self.Skill_12_active.Show()
			self.Skill_12_Points.SetText("%d" % constInfo.SKILL_POINTS[2][2])
			self.Skill_12_Points.SetParent(self.Skill_12_active)
			self.SkillUp_12.SetParent(self.Skill_12_active)
		if constInfo.SKILL_LEARNED[2][2] == 0:
			self.Skill_12_active.Hide()
			self.Skill_12_default.Show()
			self.Skill_12_Points.SetText("-")
			self.Skill_12_Points.SetParent(self.Skill_12_default)
			self.SkillUp_12.SetParent(self.Skill_12_default)
			
		if constInfo.SKILL_LEARNED[3][0] == 1:
			self.Skill_13_default.Hide()
			self.Skill_13_active.Show()
			self.Skill_13_Points.SetText("%d" % constInfo.SKILL_POINTS[3][0])
			self.Skill_13_Points.SetParent(self.Skill_13_active)
			self.SkillUp_13.SetParent(self.Skill_13_active)
		if constInfo.SKILL_LEARNED[3][0] == 0:
			self.Skill_13_active.Hide()
			self.Skill_13_default.Show()
			self.Skill_13_Points.SetText("-")
			self.Skill_13_Points.SetParent(self.Skill_13_default)
			self.SkillUp_13.SetParent(self.Skill_13_default)
		
		if constInfo.SKILL_LEARNED[3][1] == 1:
			self.Skill_14_default.Hide()
			self.Skill_14_active.Show()
			self.Skill_14_Points.SetText("%d" % constInfo.SKILL_POINTS[3][1])
			self.Skill_14_Points.SetParent(self.Skill_14_active)
			self.SkillUp_14.SetParent(self.Skill_14_active)
		if constInfo.SKILL_LEARNED[3][1] == 0:
			self.Skill_14_active.Hide()
			self.Skill_14_default.Show()
			self.Skill_14_Points.SetText("-")
			self.Skill_14_Points.SetParent(self.Skill_14_default)
			self.SkillUp_14.SetParent(self.Skill_14_default)
			
		if constInfo.SKILL_LEARNED[4][0] == 1:
			self.Skill_15_default.Hide()
			self.Skill_15_active.Show()
			self.Skill_15_Points.SetText("%d" % constInfo.SKILL_POINTS[4][0])
			self.Skill_15_Points.SetParent(self.Skill_15_active)
			self.SkillUp_15.SetParent(self.Skill_15_active)
		if constInfo.SKILL_LEARNED[4][0] == 0:
			self.Skill_15_active.Hide()
			self.Skill_15_default.Show()
			self.Skill_15_Points.SetText("-")
			self.Skill_15_Points.SetParent(self.Skill_15_default)
			self.SkillUp_15.SetParent(self.Skill_15_default)
		
		if constInfo.SKILLUP_BUTTON[0][0] == 0:
			self.SkillUp_01.Hide()
		if constInfo.SKILLUP_BUTTON[0][0] == 1:
			self.SkillUp_01.Show()
			
		if constInfo.SKILLUP_BUTTON[0][1] == 0:
			self.SkillUp_02.Hide()   
		if constInfo.SKILLUP_BUTTON[0][1] == 1:
			self.SkillUp_02.Show()
			
		if constInfo.SKILLUP_BUTTON[0][2] == 0:
			self.SkillUp_03.Hide()   
		if constInfo.SKILLUP_BUTTON[0][2] == 1:
			self.SkillUp_03.Show()
			
		if constInfo.SKILLUP_BUTTON[0][3] == 0:
			self.SkillUp_04.Hide()
		if constInfo.SKILLUP_BUTTON[0][3] == 1:
			self.SkillUp_04.Show()
			
		if constInfo.SKILLUP_BUTTON[0][4] == 0:
			self.SkillUp_05.Hide()
		if constInfo.SKILLUP_BUTTON[0][4] == 1:
			self.SkillUp_05.Show()

		if constInfo.SKILLUP_BUTTON[1][0] == 0:
			self.SkillUp_06.Hide()
		if constInfo.SKILLUP_BUTTON[1][0] == 1:
			self.SkillUp_06.Show()
			
		if constInfo.SKILLUP_BUTTON[1][1] == 0:
			self.SkillUp_07.Hide()   
		if constInfo.SKILLUP_BUTTON[1][1] == 1:
			self.SkillUp_07.Show()
			
		if constInfo.SKILLUP_BUTTON[1][2] == 0:
			self.SkillUp_08.Hide()   
		if constInfo.SKILLUP_BUTTON[1][2] == 1:
			self.SkillUp_08.Show()
			
		if constInfo.SKILLUP_BUTTON[1][3] == 0:
			self.SkillUp_09.Hide()
		if constInfo.SKILLUP_BUTTON[1][3] == 1:
			self.SkillUp_09.Show()
			
		if constInfo.SKILLUP_BUTTON[2][0] == 0:
			self.SkillUp_10.Hide()
		if constInfo.SKILLUP_BUTTON[2][0] == 1:
			self.SkillUp_10.Show()
			
		if constInfo.SKILLUP_BUTTON[2][1] == 0:
			self.SkillUp_11.Hide()
		if constInfo.SKILLUP_BUTTON[2][1] == 1:
			self.SkillUp_11.Show()
			
		if constInfo.SKILLUP_BUTTON[2][2] == 0:
			self.SkillUp_12.Hide()   
		if constInfo.SKILLUP_BUTTON[2][2] == 1:
			self.SkillUp_12.Show()
			
		if constInfo.SKILLUP_BUTTON[3][0] == 0:
			self.SkillUp_13.Hide()   
		if constInfo.SKILLUP_BUTTON[3][0] == 1:
			self.SkillUp_13.Show()
			
		if constInfo.SKILLUP_BUTTON[3][1] == 0:
			self.SkillUp_14.Hide()
		if constInfo.SKILLUP_BUTTON[3][1] == 1:
			self.SkillUp_14.Show()
			
		if constInfo.SKILLUP_BUTTON[4][0] == 0:
			self.SkillUp_15.Hide()
		if constInfo.SKILLUP_BUTTON[4][0] == 1:
			self.SkillUp_15.Show()

	def Open(self):
		if not self.isLoad:
			self.isLoad = True
			self.LoadWindow()

			self.SetTop()
			self.SetCenterPosition()
			self.Show()

	def Close(self):
		constInfo.talent_window = 0
		self.Hide()

	def OnPressEscapeKey(self):
		constInfo.talent_window = 0
		for i in xrange(5):
			self.tooltipInfo[i].SetFollow(True)
			self.tooltipInfo[i].AlignHorizonalCenter()
			self.tooltipInfo[i].Hide()
			self.tooltipInfo2[i].SetFollow(True)
			self.tooltipInfo2[i].AlignHorizonalCenter()
			self.tooltipInfo2[i].Hide()
			self.tooltipInfo3[i].SetFollow(True)
			self.tooltipInfo3[i].AlignHorizonalCenter()
			self.tooltipInfo3[i].Hide()
			self.tooltipInfo4[i].SetFollow(True)
			self.tooltipInfo4[i].AlignHorizonalCenter()
			self.tooltipInfo4[i].Hide()
			self.tooltipInfo5[i].SetFollow(True)
			self.tooltipInfo5[i].AlignHorizonalCenter()
			self.tooltipInfo5[i].Hide()
			self.tooltipInfo6[i].SetFollow(True)
			self.tooltipInfo6[i].AlignHorizonalCenter()
			self.tooltipInfo6[i].Hide()
			self.tooltipInfo7[i].SetFollow(True)
			self.tooltipInfo7[i].AlignHorizonalCenter()
			self.tooltipInfo7[i].Hide()
			self.tooltipInfo8[i].SetFollow(True)
			self.tooltipInfo8[i].AlignHorizonalCenter()
			self.tooltipInfo8[i].Hide()
			self.tooltipInfo9[i].SetFollow(True)
			self.tooltipInfo9[i].AlignHorizonalCenter()
			self.tooltipInfo9[i].Hide()
			self.tooltipInfo10[i].SetFollow(True)
			self.tooltipInfo10[i].AlignHorizonalCenter()
			self.tooltipInfo10[i].Hide()
			self.tooltipInfo11[i].SetFollow(True)
			self.tooltipInfo11[i].AlignHorizonalCenter()
			self.tooltipInfo11[i].Hide()
			self.tooltipInfo12[i].SetFollow(True)
			self.tooltipInfo12[i].AlignHorizonalCenter()
			self.tooltipInfo12[i].Hide()
			self.tooltipInfo13[i].SetFollow(True)
			self.tooltipInfo13[i].AlignHorizonalCenter()
			self.tooltipInfo13[i].Hide()
			self.tooltipInfo14[i].SetFollow(True)
			self.tooltipInfo14[i].AlignHorizonalCenter()
			self.tooltipInfo14[i].Hide()
			self.tooltipInfo15[i].SetFollow(True)
			self.tooltipInfo15[i].AlignHorizonalCenter()
			self.tooltipInfo15[i].Hide()
		self.Close()
		return True

	def OnCloseEvent(self):
		self.isLoad = False
		constInfo.talent_window = 0
		self.Close()

	def __OnClosePopupDialog(self):
		pass


# uitalenttree_v1 = TalentTreeWindow()
# uitalenttree_v1.Open()