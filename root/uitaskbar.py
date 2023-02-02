import ui
import net
import item
import skill
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import wndMgr
import player
import constInfo
import mouseModule
import uiScriptLocale
import miniMap
import playerSettingModule
import app
import uiToolTip
import apollo_interface
from ui import ExpandedImageBox, ImageBox, Button

MOUSE_SETTINGS = [0, 0]

def InitMouseButtonSettings(left, right):
	global MOUSE_SETTINGS
	MOUSE_SETTINGS = [left, right]

def SetMouseButtonSetting(dir, event):
	global MOUSE_SETTINGS
	MOUSE_SETTINGS[dir] = event
	
def GetMouseButtonSettings():
	global MOUSE_SETTINGS
	return MOUSE_SETTINGS

def SaveMouseButtonSettings():
	global MOUSE_SETTINGS
	open("mouse.cfg", "w").write("%s\t%s" % tuple(MOUSE_SETTINGS))

def LoadMouseButtonSettings():
	global MOUSE_SETTINGS
	tokens = open("mouse.cfg", "r").read().split()

	if len(tokens) != 2:
		raise RuntimeError, "MOUSE_SETTINGS_FILE_ERROR"

	MOUSE_SETTINGS[0] = int(tokens[0])
	MOUSE_SETTINGS[1] = int(tokens[1])

def unsigned32(n):
	return n & 0xFFFFFFFFL



class GiftBox(ui.ScriptWindow):
	class TextToolTip(ui.Window):
		def __init__(self):
			ui.Window.__init__(self, "TOP_MOST")
			self.SetWindowName("GiftBox")
			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.textLine = textLine

		def __del__(self):
			ui.Window.__del__(self)

		def SetText(self, text):
			self.textLine.SetText(text)

		def OnRender(self):
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			self.textLine.SetPosition(mouseX, mouseY - 15)

	def __init__(self):
		#print "NEW TASKBAR  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		self.tooltipGift = self.TextToolTip()
		self.tooltipGift.Show()
		
	def __del__(self):
		#print "---------------------------------------------------------------------------- DELETE TASKBAR"
		ui.ScriptWindow.__del__(self)
		
	def GlobalButton(self):
		import multi
		MultiDialog = multi.MultiLanguage()
		MultiDialog.Show()
		self.Close()
		
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "giftbox.py")
		except:
			import exception
			exception.Abort("GiftBox.LoadWindow.LoadObject")		

		self.giftBoxIcon = self.GetChild("GiftBox_Icon")
		self.giftBoxToolTip = self.GetChild("GiftBox_ToolTip")
	
	def Destroy(self):		
		self.giftBoxIcon = 0
		self.giftBoxToolTip = 0		
				
class ExpandedTaskBar(ui.ScriptWindow):
	BUTTON_DRAGON_SOUL = 0
	BUTTON_PET_GUI = 1
	def __init__(self):
		ui.Window.__init__(self)
		self.SetWindowName("ExpandedTaskBar")
	
	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, uiScriptLocale.LOCALE_UISCRIPT_PATH + "ExpandedTaskBar.py")
		except:
			import exception
			exception.Abort("ExpandedTaskBar.LoadWindow.LoadObject")

		self.expandedTaskBarBoard = self.GetChild("ExpanedTaskBar_Board")

		self.toggleButtonDict = {}
		self.toggleButtonDict[ExpandedTaskBar.BUTTON_DRAGON_SOUL] = self.GetChild("DragonSoulButton")
		self.toggleButtonDict[ExpandedTaskBar.BUTTON_DRAGON_SOUL].SetParent(self)
		#self.toggleButtonDict[ExpandedTaskBar.BUTTON_PET_GUI] = self.GetChild("PetGuiButton")
		#self.toggleButtonDict[ExpandedTaskBar.BUTTON_PET_GUI].SetParent(self)
	
	def SetTop(self):
		super(ExpandedTaskBar, self).SetTop()	
		for button in self.toggleButtonDict.values():
			button.SetTop()
	
	def Show(self):
		ui.ScriptWindow.Show(self)
	
	def Close(self):
		self.Hide()
	
	def SetToolTipText(self, eButton, text):
		self.toggleButtonDict[eButton].SetToolTipText(text)
		
	def SetToggleButtonEvent(self, eButton, kEventFunc):
		self.toggleButtonDict[eButton].SetEvent(kEventFunc)

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
	
		
class TaskBar(ui.ScriptWindow):

	BUTTON_CHARACTER = 0
	BUTTON_INVENTORY = 1
	BUTTON_MESSENGER = 2
	BUTTON_SYSTEM = 3
	BUTTON_CHAT = 4
	BUTTON_EXPAND = 5
	IS_EXPANDED = FALSE

	MOUSE_BUTTON_LEFT = 0
	MOUSE_BUTTON_RIGHT = 1
	NONE = 255

	EVENT_MOVE = 0
	EVENT_ATTACK = 1
	EVENT_MOVE_AND_ATTACK = 2
	EVENT_CAMERA = 3
	EVENT_SKILL = 4
	EVENT_AUTO = 5

	GAUGE_WIDTH = 95
	GAUGE_HEIGHT = 13

	QUICKPAGE_NUMBER_FILENAME = [
		"btn_slotpageone",
		"btn_slotpagetwo",
		"btn_slotpagethree",
		"btn_slotpagefour",
	]

	#gift icon show and hide
	def ShowGift(self):
		if not localeInfo.IsBRAZIL():
			self.wndGiftBox.Show()
	
	def HideGift(self):
		self.wndGiftBox.Hide()

	class TextToolTip(ui.Window):
		def __init__(self):
			ui.Window.__init__(self, "TOP_MOST")

			textLine = ui.TextLine()
			textLine.SetParent(self)
			textLine.SetHorizontalAlignCenter()
			textLine.SetOutline()
			textLine.Show()
			self.textLine = textLine

		def __del__(self):
			ui.Window.__del__(self)

		def SetText(self, text):
			self.textLine.SetText(text)

		def OnRender(self):
			(mouseX, mouseY) = wndMgr.GetMousePosition()
			self.textLine.SetPosition(mouseX, mouseY - 15)

	class SkillButton(ui.SlotWindow):

		def __init__(self):
			ui.SlotWindow.__init__(self)

			self.event = 0
			self.arg = 0

			self.slotIndex = 0
			self.skillIndex = 0
			
			slotIndex = 0
			wndMgr.SetSlotBaseImage(self.hWnd, "d:/ymir work/ui/public/slot_base.sub", 1.0, 1.0, 1.0, 1.0)
			wndMgr.AppendSlot(self.hWnd, slotIndex, 0, 0, 32, 32)
			self.SetCoverButton(slotIndex,	"d:/ymir work/ui/public/slot_base.sub",\
											"d:/ymir work/ui/public/slot_base.sub",\
											"d:/ymir work/ui/public/slot_base.sub",\
											"d:/ymir work/ui/public/slot_base.sub", TRUE, FALSE)
			self.SetSize(32, 32)

		def __del__(self):
			ui.SlotWindow.__del__(self)

		def Destroy(self):
			if 0 != self.tooltipSkill:
				self.tooltipSkill.HideToolTip()

		def RefreshSkill(self):
			if 0 != self.slotIndex:
				self.SetSkill(self.slotIndex)

		def SetSkillToolTip(self, tooltip):
			self.tooltipSkill = tooltip

		def SetSkill(self, skillSlotNumber):
			slotNumber = 0
			skillIndex = player.GetSkillIndex(skillSlotNumber)
			skillGrade = player.GetSkillGrade(skillSlotNumber)
			skillLevel = player.GetSkillLevel(skillSlotNumber)
			skillType = skill.GetSkillType(skillIndex)

			self.skillIndex = skillIndex
			if 0 == self.skillIndex:
				self.ClearSlot(slotNumber)
				return

			self.slotIndex = skillSlotNumber

			self.SetSkillSlotNew(slotNumber, skillIndex, skillGrade, skillLevel)
			self.SetSlotCountNew(slotNumber, skillGrade, skillLevel)

			
			if player.IsSkillCoolTime(skillSlotNumber):
				(coolTime, elapsedTime) = player.GetSkillCoolTime(skillSlotNumber)
				self.SetSlotCoolTime(slotNumber, coolTime, elapsedTime)

			
			if player.IsSkillActive(skillSlotNumber):
				self.ActivateSlot(slotNumber)

		def SetSkillEvent(self, event, arg=0):
			self.event = event
			self.arg = arg

		def GetSkillIndex(self):
			return self.skillIndex

		def GetSlotIndex(self):
			return self.slotIndex

		def Activate(self, coolTime):
			self.SetSlotCoolTime(0, coolTime)

			if skill.IsToggleSkill(self.skillIndex):
				self.ActivateSlot(0)

		def Deactivate(self):
			if skill.IsToggleSkill(self.skillIndex):
				self.DeactivateSlot(0)

		def OnOverInItem(self, dummy):
			self.tooltipSkill.SetSkill(self.skillIndex)

		def OnOverOutItem(self):
			self.tooltipSkill.HideToolTip()

		def OnSelectItemSlot(self, dummy):
			if 0 != self.event:
				if 0 != self.arg:
					self.event(self.arg)
				else:
					self.event()

	
	def __init__(self):
		#print "NEW TASKBAR  ----------------------------------------------------------------------------"

		ui.ScriptWindow.__init__(self, "TOP_MOST")
		self.text = {}

		self.quickPageNumImageBox = None
		self.tooltipItem = 0
		self.tooltipSkill = 0
		self.TaskBarLeft = ui.ScriptWindow("TOP_MOST")
		self.TaskBarLeft2 = ui.ScriptWindow("TOP_MOST")
		self.mouseModeButtonList = [ ui.ScriptWindow("TOP_MOST"), ui.ScriptWindow("TOP_MOST") ]

		self.tooltipHP = self.TextToolTip()
		self.tooltipHP.Hide()
		self.tooltipSP = self.TextToolTip()
		self.tooltipSP.Hide()
		self.tooltipST = self.TextToolTip()
		self.tooltipST.Hide()
		self.tooltipEXP = self.TextToolTip()
		self.tooltipEXP.Hide()
		self.toolTipAlignment = uiToolTip.ToolTip()
		# self.toolTipAlignment.Hide()
		
		self.skillCategoryNameList = [ "ACTIVE_1", "ACTIVE_2", "ACTIVE_3" ]
		self.skillPageStartSlotIndexDict = {
			"ACTIVE_1" : 1, 
			"ACTIVE_2" : 21, 
			"ACTIVE_3" : 41, 
		}

		self.selectSkillButtonList = []
		
		self.lastUpdateQuickSlot = 0
		self.SetWindowName("TaskBar")
		self.LoadWindow()

	
	def __del__(self):
		#print "---------------------------------------------------------------------------- DELETE TASKBAR"
		ui.ScriptWindow.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()

			pyScrLoader.LoadScriptFile(self, "apollo_scripts/TaskBar.py")
			pyScrLoader.LoadScriptFile(self.TaskBarLeft, "apollo_scripts/TaskBar_left.py")
			pyScrLoader.LoadScriptFile(self.TaskBarLeft2, "apollo_scripts/TaskBar_left2.py")
			pyScrLoader.LoadScriptFile(self.mouseModeButtonList[self.MOUSE_BUTTON_LEFT], "apollo_scripts/MouseButtonWindow.py")
			pyScrLoader.LoadScriptFile(self.mouseModeButtonList[self.MOUSE_BUTTON_RIGHT], "apollo_scripts/RightMouseButtonWindow.py")
		except:
			import exception
			exception.Abort("TaskBar.LoadWindow.LoadObject")
		
		self.buttonpage = self.GetChild("ButtonPageSlots")
		self.buttonpage.SetEvent(self.SelectPageSlots)
		
		self.quickslot = []
		self.quickslot.append(self.GetChild("quick_slot_1"))
		self.quickslot.append(self.GetChild("quick_slot_2"))
		for slot in self.quickslot:
			slot.SetSlotStyle(wndMgr.SLOT_STYLE_NONE)
			slot.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectEmptyQuickSlot))
			slot.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemQuickSlot))
			slot.SetUnselectItemSlotEvent(ui.__mem_func__(self.UnselectItemQuickSlot))
			slot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
			slot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutItem))

		toggleButtonDict = {}
		toggleButtonDict[TaskBar.BUTTON_CHARACTER]=self.TaskBarLeft.GetChild("CharacterButton")
		toggleButtonDict[TaskBar.BUTTON_INVENTORY]=self.TaskBarLeft2.GetChild("InventoryButton")
		toggleButtonDict[TaskBar.BUTTON_MESSENGER]=self.TaskBarLeft2.GetChild("MessengerButton")
		toggleButtonDict[TaskBar.BUTTON_SYSTEM]=self.TaskBarLeft2.GetChild("SystemButton")

		try:
			toggleButtonDict[TaskBar.BUTTON_CHAT]=self.GetChild("ChatButton")
		except:
			toggleButtonDict[TaskBar.BUTTON_EXPAND]=self.GetChild("ExpandButton")
			TaskBar.IS_EXPANDED = TRUE
		

		if localeInfo.IsARABIC():
			systemButton = toggleButtonDict[TaskBar.BUTTON_SYSTEM]
			if systemButton.ToolTipText:
				tx, ty = systemButton.ToolTipText.GetLocalPosition()
				tw = systemButton.ToolTipText.GetWidth() 
				systemButton.ToolTipText.SetPosition(-tw/2, ty)
			
			
		
		race = net.GetMainActorRace()
		self.img = ui.ImageBox()
		self.img.SetParent(self.TaskBarLeft.GetChild("MiniMapWindow2"))
		self.img.SetPosition(39,0)
		self.img.LoadImage(apollo_interface.FACE_IMAGE_DICT[race])
		self.img.Show()

		mouseLeftButtonModeButton = self.GetChild("LeftMouseButton")
		mouseRightButtonModeButton = self.GetChild("RightMouseButton")
		mouseLeftButtonModeButton.SetEvent(ui.__mem_func__(self.ToggleLeftMouseButtonModeWindow))		
		mouseRightButtonModeButton.SetEvent(ui.__mem_func__(self.ToggleRightMouseButtonModeWindow))
		self.curMouseModeButton = [ mouseLeftButtonModeButton, mouseRightButtonModeButton ]

		(xLocalRight, yLocalRight) = mouseRightButtonModeButton.GetLocalPosition()
		self.curSkillButton = self.SkillButton()
		self.curSkillButton.SetParent(self)
		self.curSkillButton.SetPosition(xLocalRight, 3)
		self.curSkillButton.SetSkillEvent(ui.__mem_func__(self.ToggleRightMouseButtonModeWindow))
		self.curSkillButton.Hide()
	
		(xLeft, yLeft) = mouseLeftButtonModeButton.GetGlobalPosition()
		(xRight, yRight) = mouseRightButtonModeButton.GetGlobalPosition()
		leftModeButtonList = self.mouseModeButtonList[self.MOUSE_BUTTON_LEFT]
		leftModeButtonList.SetPosition(xLeft, yLeft - leftModeButtonList.GetHeight()-5)
		rightModeButtonList = self.mouseModeButtonList[self.MOUSE_BUTTON_RIGHT]
		rightModeButtonList.SetPosition(xRight - rightModeButtonList.GetWidth() + 32, yRight - rightModeButtonList.GetHeight()-5)
		rightModeButtonList.GetChild("button_skill").SetEvent(lambda adir=self.MOUSE_BUTTON_RIGHT, aevent=self.EVENT_SKILL: self.SelectMouseButtonEvent(adir, aevent))
		rightModeButtonList.GetChild("button_skill").Hide()
		
		'''
		mouseImage = ui.ImageBox("TOP_MOST")
		mouseImage.AddFlag("float")
		mouseImage.LoadImage("d:/ymir work/ui/game/taskbar/mouse_button_camera_02.sub")
		mouseImage.SetPosition(xRight, wndMgr.GetScreenHeight() - 34)
		mouseImage.Hide()
		self.mouseImage = mouseImage
		'''

		dir = self.MOUSE_BUTTON_LEFT
		wnd = self.mouseModeButtonList[dir]
		wnd.GetChild("button_move_and_attack").SetEvent(lambda adir=dir, aevent=self.EVENT_MOVE_AND_ATTACK: self.SelectMouseButtonEvent(adir, aevent))
		wnd.GetChild("button_auto_attack").SetEvent(lambda adir=dir, aevent=self.EVENT_AUTO: self.SelectMouseButtonEvent(adir, aevent))
		wnd.GetChild("button_camera").SetEvent(lambda adir=dir, aevent=self.EVENT_CAMERA: self.SelectMouseButtonEvent(adir, aevent))

		dir = self.MOUSE_BUTTON_RIGHT
		wnd = self.mouseModeButtonList[dir]
		wnd.GetChild("button_move_and_attack").SetEvent(lambda adir=dir, aevent=self.EVENT_MOVE_AND_ATTACK: self.SelectMouseButtonEvent(adir, aevent))
		wnd.GetChild("button_camera").SetEvent(lambda adir=dir, aevent=self.EVENT_CAMERA: self.SelectMouseButtonEvent(adir, aevent))

		self.HpEmpty = ExpandedImageBox()
		self.HpEmpty.AddFlag("not_pick")
		self.HpEmpty.SetParent(self.TaskBarLeft.GetChild("Window1"))
		self.HpEmpty.SetPosition(-24, 42)
		self.HpEmpty.LoadImage(apollo_interface.PATCH_SPECIAL + "/taskbar/gauge_hp/gauge_hp_empty.png")
		self.HpEmpty.Show()
		self.HpRefresh = []
		for i in xrange(0,6):
			part = ExpandedImageBox()
			part.AddFlag("not_pick")
			part.LoadImage(apollo_interface.PATCH_SPECIAL + "/taskbar/gauge_hp/gauge_hp_fill_0"+ str(i+1)+".png")
			part.SetAlpha(0.3)
			part.SetParent(self.TaskBarLeft.GetChild("Window1"))
			part.SetPosition(-24, 42)
			part.Show()
			self.HpRefresh.append(part)
		part = ExpandedImageBox()
		part.AddFlag("not_pick")
		part.LoadImage(apollo_interface.PATCH_SPECIAL + "/taskbar/gauge_hp/gauge_hp_transition.png")
		part.SetAlpha(0.3)
		part.SetParent(self.TaskBarLeft.GetChild("Window1"))
		part.SetPosition(-24, 42)
		part.Show()
		self.HpRefresh.append(part)

		self.HpFull = []
		for i in xrange(0,6):
			part = ExpandedImageBox()
			part.AddFlag("not_pick")
			part.LoadImage(apollo_interface.PATCH_SPECIAL + "/taskbar/gauge_hp/gauge_hp_fill_0"+ str(i+1)+".png")
			part.SetParent(self.TaskBarLeft.GetChild("Window1"))
			part.SetPosition(-24, 42)
			part.Show()
			self.HpFull.append(part)
		part = ExpandedImageBox()
		part.AddFlag("not_pick")
		part.LoadImage(apollo_interface.PATCH_SPECIAL + "/taskbar/gauge_hp/gauge_hp_transition.png")
		part.SetParent(self.TaskBarLeft.GetChild("Window1"))
		part.SetPosition(-24, 42)
		part.Show()
		self.HpFull.append(part)

		self.MpEmpty = ExpandedImageBox()
		self.MpEmpty.AddFlag("not_pick")
		self.MpEmpty.SetParent(self.TaskBarLeft.GetChild("Window1"))
		self.MpEmpty.SetPosition(-23, 42)
		self.MpEmpty.LoadImage(apollo_interface.PATCH_SPECIAL + "/taskbar/gauge_mp/gauge_mp_empty.png")
		self.MpEmpty.Show()


		self.MpRefresh = []
		for i in xrange(0,77):
			part = ExpandedImageBox()
			part.AddFlag("not_pick")
			s = str(i)
			if(i < 10):
				s = "0"+s
			part.LoadImage(apollo_interface.PATCH_SPECIAL + "/taskbar/gauge_mp/gauge_mp_fill_"+ s+".png")
			part.SetParent(self.TaskBarLeft.GetChild("Window1"))
			part.SetPosition(30, 95)
			part.SetAlpha(0.3)
			part.Hide()
			self.MpRefresh.append(part)

		self.MpFull = []
		for i in xrange(0,77):
			part = ExpandedImageBox()
			part.AddFlag("not_pick")
			s = str(i)
			if(i < 10):
				s = "0"+s
			part.LoadImage(apollo_interface.PATCH_SPECIAL + "/taskbar/gauge_mp/gauge_mp_fill_"+ s+".png")
			part.SetParent(self.TaskBarLeft.GetChild("Window1"))
			part.SetPosition(30, 95)
			part.Show()
			self.MpFull.append(part)
		
		# self.imgg = ui.ImageBox()
		# self.imgg.LoadImage("interface/byemperor_apollo/taskbar/bar_left.png")
		# self.imgg.SetParent(self.GetChild("Base_Board_01"))
		# self.imgg.SetPosition(0, 34)
		# self.imgg.Show()
		
		
		
		self.toggleButtonDict = toggleButtonDict
		
		self.TaskBarLeft.GetChild("ItemShopButton").SetEvent(self.OpenIShopWindow)
		
		self.expGauge = self.TaskBarLeft.GetChild("EXPGauge_01")

		
		
		self.TaskBarLeft.Show()
		self.TaskBarLeft2.Show()
		
		u = 0
		for i in xrange(2):
			self.text[i] = ui.TextLine()
			self.text[i].SetParent(self.TaskBarLeft.GetChild("MiniMapWindow2"))
			self.text[i].SetPosition(140,47+u)
			if i == 0:
				self.text[i].SetPackedFontColor(0xffa33437)
			else:
				self.text[i].SetPackedFontColor(0xff3453a3)
			self.text[i].Show()
			u += 15
		
		#giftbox object
		wndGiftBox = GiftBox()
		wndGiftBox.LoadWindow()
		self.wndGiftBox = wndGiftBox
	
		self.__LoadMouseSettings()
		self.RefreshStatus()
		self.RefreshQuickSlot()

	def __LoadMouseSettings(self):
		try:
			LoadMouseButtonSettings()
			(mouseLeftButtonEvent, mouseRightButtonEvent) = GetMouseButtonSettings()
			if not self.__IsInSafeMouseButtonSettingRange(mouseLeftButtonEvent) or not self.__IsInSafeMouseButtonSettingRange(mouseRightButtonEvent):
					raise RuntimeError, "INVALID_MOUSE_BUTTON_SETTINGS"
		except:
			InitMouseButtonSettings(self.EVENT_MOVE_AND_ATTACK, self.EVENT_CAMERA)
			(mouseLeftButtonEvent, mouseRightButtonEvent) = GetMouseButtonSettings()

		try:
			self.SelectMouseButtonEvent(self.MOUSE_BUTTON_LEFT,	mouseLeftButtonEvent)
			self.SelectMouseButtonEvent(self.MOUSE_BUTTON_RIGHT,	mouseRightButtonEvent)
		except:
			InitMouseButtonSettings(self.EVENT_MOVE_AND_ATTACK, self.EVENT_CAMERA)
			(mouseLeftButtonEvent, mouseRightButtonEvent) = GetMouseButtonSettings()

			self.SelectMouseButtonEvent(self.MOUSE_BUTTON_LEFT,	mouseLeftButtonEvent)
			self.SelectMouseButtonEvent(self.MOUSE_BUTTON_RIGHT,	mouseRightButtonEvent)



	def __IsInSafeMouseButtonSettingRange(self, arg):
		return arg >= self.EVENT_MOVE and arg <= self.EVENT_AUTO

	def Destroy(self):		
		SaveMouseButtonSettings()

		self.ClearDictionary()
		self.TaskBarLeft.ClearDictionary()
		self.TaskBarLeft2.ClearDictionary()
	
		self.mouseModeButtonList[0].ClearDictionary()
		self.mouseModeButtonList[1].ClearDictionary()
		self.TaskBarLeft = 0
		self.TaskBarLeft2 = 0
		self.mouseModeButtonList = 0
		self.curMouseModeButton = 0
		self.curSkillButton = 0
		self.selectSkillButtonList = 0


		self.img = None
		self.expGauge = None
		self.hpGauge = None
		self.mpGauge = None
	
		self.hpRecoveryGaugeBar = None
		self.spRecoveryGaugeBar = None
	
		self.tooltipItem = 0
		self.tooltipSkill = 0
		self.buttonpage = 0
		self.quickslot = 0
		self.toggleButtonDict = 0

		self.tooltipHP = 0
		self.tooltipSP = 0
		self.tooltipST = 0
		self.tooltipEXP = 0
		self.toolTipAlignment = 0

		# self.mouseImage = None
	
	def OpenIShopWindow(self):
		net.SendChatPacket("/in_game_mall")
	
	def SetToggleButtonEvent(self, eButton, kEventFunc):
		self.toggleButtonDict[eButton].SetEvent(kEventFunc)

	def SetItemToolTip(self, tooltipItem):
		self.tooltipItem = tooltipItem

	def SetSkillToolTip(self, tooltipSkill):
		self.tooltipSkill = tooltipSkill
		self.curSkillButton.SetSkillToolTip(self.tooltipSkill)

	## Mouse Image
	def ShowMouseImage(self):
		pass
		#self.mouseImage.SetTop()
		#self.mouseImage.Show()

	def HideMouseImage(self):
		player.SetQuickCameraMode(FALSE)
		#self.mouseImage.Hide()

	## Gauge
	def RefreshStatus(self):
		curHP = player.GetStatus(player.HP)
		maxHP = player.GetStatus(player.MAX_HP)
		curSP = player.GetStatus(player.SP)
		maxSP = player.GetStatus(player.MAX_SP)
		curEXP = unsigned32(player.GetStatus(player.EXP))
		nextEXP = unsigned32(player.GetStatus(player.NEXT_EXP))
		recoveryHP = player.GetStatus(player.HP_RECOVERY)
		recoverySP = player.GetStatus(player.SP_RECOVERY)
		
		self.RefreshStamina()
		self.SetExperience(curEXP, nextEXP)
		
	def RefreshStamina(self):
		curST = player.GetStatus(player.STAMINA)
		maxST = player.GetStatus(player.MAX_STAMINA)
		# self.SetST(curST, maxST)

	def RefreshSkill(self):
		self.curSkillButton.RefreshSkill()
		for button in self.selectSkillButtonList:
			button.RefreshSkill()

	def SetHp(self, _actual,_recovery, _max):
		_max = max(1, _max)
		trans_actual = 270 * (1.0-(float(_actual) / float(_max)))
		trans_recovery = 270 * (1.0-(float(_recovery) / float(_max)))
		for i in xrange(0,7):
			i2 =i
			if(i == 6):
				i2 = 0
			max_transition = 270.0 - float(i2)*45.0
			trans = -min(max_transition, trans_actual)
			trans_rec = -min(max_transition, trans_recovery)
			self.HpFull[i].SetRotation(trans)
			self.HpRefresh[i].SetRotation(trans_rec)
			
	def SetSp(self, _actual, _recovery, _max):
		max_show = 76 -int(76.0 * float(_actual)/ float(_max))
		max_rec =  76 -int(76.0 * float(_recovery)/ float(_max))
		for i in xrange(0,77):
			self.MpFull[i].Hide()
			self.MpRefresh[i].Hide()
		self.MpRefresh[max_rec].Show()
		self.MpFull[max_show].Show()

	def SetExperience(self, curPoint, maxPoint):
		curPoint = min(curPoint, maxPoint)
		if maxPoint > 0:
			self.expGauge.SetPercentage(curPoint, maxPoint)
		self.tooltipEXP.SetText("%s : %.2f%%" % (localeInfo.TASKBAR_EXP, float(curPoint) / max(1, float(maxPoint)) * 100))
	
		
	## QuickSlot
	def SelectPageSlots(self):
		player.SetQuickPage(player.GetQuickPage()+1)
		pageNum = player.GetQuickPage()
		try:
			self.buttonpage.SetUpVisual(apollo_interface.PATCH_SPECIAL + "/taskbar/" + self.QUICKPAGE_NUMBER_FILENAME[pageNum]+"_01_normal.png")
			self.buttonpage.SetOverVisual(apollo_interface.PATCH_SPECIAL + "/taskbar/" + self.QUICKPAGE_NUMBER_FILENAME[pageNum]+"_02_hover.png")
			self.buttonpage.SetDownVisual(apollo_interface.PATCH_SPECIAL + "/taskbar/" + self.QUICKPAGE_NUMBER_FILENAME[pageNum]+"_03_active.png")
		except:
			pass
	
	def RefreshQuickSlot(self):

		pageNum = player.GetQuickPage()

		startNumber = 0
		if not self.quickslot:
			return
			
		for slot in self.quickslot:

			for i in xrange(4):

				slotNumber = i+startNumber

				(Type, Position) = player.GetLocalQuickSlot(slotNumber)

				if player.SLOT_TYPE_NONE == Type:
					slot.ClearSlot(slotNumber)
					continue

				if player.SLOT_TYPE_INVENTORY == Type:

					itemIndex = player.GetItemIndex(Position)
					itemCount = player.GetItemCount(Position)
					if itemCount <= 1:
						itemCount = 0
					
					
					if constInfo.IS_AUTO_POTION(itemIndex):
						
						metinSocket = [player.GetItemMetinSocket(Position, j) for j in xrange(player.METIN_SOCKET_MAX_NUM)]
						
						if 0 != int(metinSocket[0]):
							slot.ActivateSlot(slotNumber)
						else:
							slot.DeactivateSlot(slotNumber)
					
					slot.SetItemSlot(slotNumber, itemIndex, itemCount)

				elif player.SLOT_TYPE_SKILL == Type:

					skillIndex = player.GetSkillIndex(Position)
					if 0 == skillIndex:
						slot.ClearSlot(slotNumber)
						continue

					skillType = skill.GetSkillType(skillIndex)
					if skill.SKILL_TYPE_GUILD == skillType:
						import guild
						skillGrade = 0
						skillLevel = guild.GetSkillLevel(Position)

					else:
						skillGrade = player.GetSkillGrade(Position)
						skillLevel = player.GetSkillLevel(Position)

					slot.SetSkillSlotNew(slotNumber, skillIndex, skillGrade, skillLevel)
					slot.SetSlotCountNew(slotNumber, skillGrade, skillLevel)
					slot.SetCoverButton(slotNumber)

				
					if player.IsSkillCoolTime(Position):
						(coolTime, elapsedTime) = player.GetSkillCoolTime(Position)
						slot.SetSlotCoolTime(slotNumber, coolTime, elapsedTime)

					
					if player.IsSkillActive(Position):
						slot.ActivateSlot(slotNumber)

				elif player.SLOT_TYPE_EMOTION == Type:

					emotionIndex = Position
					slot.SetEmotionSlot(slotNumber, emotionIndex)
					slot.SetCoverButton(slotNumber)
					slot.SetSlotCount(slotNumber, 0)

			slot.RefreshSlot()
			startNumber += 4

	def canAddQuickSlot(self, Type, slotNumber):

		if player.SLOT_TYPE_INVENTORY == Type:

			itemIndex = player.GetItemIndex(slotNumber)
			return item.CanAddToQuickSlotItem(itemIndex)

		return TRUE

	def AddQuickSlot(self, localSlotIndex):
		AttachedSlotType = mouseModule.mouseController.GetAttachedType()
		AttachedSlotNumber = mouseModule.mouseController.GetAttachedSlotNumber()
		AttachedItemIndex = mouseModule.mouseController.GetAttachedItemIndex()

		if player.SLOT_TYPE_QUICK_SLOT == AttachedSlotType:
			player.RequestMoveGlobalQuickSlotToLocalQuickSlot(AttachedSlotNumber, localSlotIndex)

		elif player.SLOT_TYPE_EMOTION == AttachedSlotType:

			player.RequestAddLocalQuickSlot(localSlotIndex, AttachedSlotType, AttachedItemIndex)

		elif TRUE == self.canAddQuickSlot(AttachedSlotType, AttachedSlotNumber):

			## Online Code
			player.RequestAddLocalQuickSlot(localSlotIndex, AttachedSlotType, AttachedSlotNumber)
		
		mouseModule.mouseController.DeattachObject()
		self.RefreshQuickSlot()

	def SelectEmptyQuickSlot(self, slotIndex):

		if TRUE == mouseModule.mouseController.isAttached():
			self.AddQuickSlot(slotIndex)

	def SelectItemQuickSlot(self, localQuickSlotIndex):

		if TRUE == mouseModule.mouseController.isAttached():
			self.AddQuickSlot(localQuickSlotIndex)

		else:
			globalQuickSlotIndex=player.LocalQuickSlotIndexToGlobalQuickSlotIndex(localQuickSlotIndex)
			mouseModule.mouseController.AttachObject(self, player.SLOT_TYPE_QUICK_SLOT, globalQuickSlotIndex, globalQuickSlotIndex)
	def UnselectItemQuickSlot(self, localSlotIndex):

		if FALSE == mouseModule.mouseController.isAttached():
			player.RequestUseLocalQuickSlot(localSlotIndex)
			return

		elif mouseModule.mouseController.isAttached():
			mouseModule.mouseController.DeattachObject()
			return


	def OnUseSkill(self, usedSlotIndex, coolTime):

		QUICK_SLOT_SLOT_COUNT = 4
		slotIndex = 0

		## Current Skill Button
		if usedSlotIndex == self.curSkillButton.GetSlotIndex():
			self.curSkillButton.Activate(coolTime)

		## Quick Slot
		for slotWindow in self.quickslot:

			for i in xrange(QUICK_SLOT_SLOT_COUNT):

				(Type, Position) = player.GetLocalQuickSlot(slotIndex)

				if Type == player.SLOT_TYPE_SKILL:
					if usedSlotIndex == Position:
						slotWindow.SetSlotCoolTime(slotIndex, coolTime)
						return

				slotIndex += 1

	def OnActivateSkill(self, usedSlotIndex):
		slotIndex = 0

		## Current Skill Button
		if usedSlotIndex == self.curSkillButton.GetSlotIndex():
			self.curSkillButton.Deactivate()

		## Quick Slot
		for slotWindow in self.quickslot:

			for i in xrange(4):

				(Type, Position) = player.GetLocalQuickSlot(slotIndex)

				if Type == player.SLOT_TYPE_SKILL:
					if usedSlotIndex == Position:
						slotWindow.ActivateSlot(slotIndex)
						return

				slotIndex += 1

	def OnDeactivateSkill(self, usedSlotIndex):
		slotIndex = 0

		## Current Skill Button
		if usedSlotIndex == self.curSkillButton.GetSlotIndex():
			self.curSkillButton.Deactivate()

		## Quick Slot
		for slotWindow in self.quickslot:

			for i in xrange(4):

				(Type, Position) = player.GetLocalQuickSlot(slotIndex)

				if Type == player.SLOT_TYPE_SKILL:
					if usedSlotIndex == Position:
						slotWindow.DeactivateSlot(slotIndex)
						return

				slotIndex += 1

	## ToolTip
	def OverInItem(self, slotNumber):
		if mouseModule.mouseController.isAttached():
			return

		(Type, Position) = player.GetLocalQuickSlot(slotNumber)

		if player.SLOT_TYPE_INVENTORY == Type:
			self.tooltipItem.SetInventoryItem(Position)
			self.tooltipSkill.HideToolTip()

		elif player.SLOT_TYPE_SKILL == Type:

			skillIndex = player.GetSkillIndex(Position)
			skillType = skill.GetSkillType(skillIndex)

			if skill.SKILL_TYPE_GUILD == skillType:
				import guild
				skillGrade = 0
				skillLevel = guild.GetSkillLevel(Position)

			else:
				skillGrade = player.GetSkillGrade(Position)
				skillLevel = player.GetSkillLevel(Position)

			self.tooltipSkill.SetSkillNew(Position, skillIndex, skillGrade, skillLevel)
			self.tooltipItem.HideToolTip()

	def OverOutItem(self):
		if 0 != self.tooltipItem:
			self.tooltipItem.HideToolTip()
		if 0 != self.tooltipSkill:
			self.tooltipSkill.HideToolTip()


	def OnUpdate(self):
		self.text[0].SetText(str(player.GetStatus(player.HP)))
		self.text[1].SetText(str(player.GetStatus(player.SP)))
		
		curHP = player.GetStatus(player.HP)
		maxHP = player.GetStatus(player.MAX_HP)
		curSP = player.GetStatus(player.SP)
		maxSP = player.GetStatus(player.MAX_SP)
		recoveryHP = player.GetStatus(player.HP_RECOVERY)
		recoverySP = player.GetStatus(player.SP_RECOVERY)
		self.SetHp(curHP, recoveryHP, maxHP)
		self.SetSp(curSP, recoverySP, maxSP)
		

		if app.GetGlobalTime() - self.lastUpdateQuickSlot > 500:
			self.lastUpdateQuickSlot = app.GetGlobalTime()
			self.RefreshQuickSlot()
		
		# if TRUE == self.expGauge.IsIn():
			# self.tooltipEXP.Show()
			# self.tooltipEXP.SetTop()
		# else:
		if self.tooltipEXP:
			self.tooltipEXP.Hide()
		
		if self.img and TRUE == self.img.IsIn():
			point, grade = player.GetAlignmentData()
			
			import colorInfo
			COLOR_DICT = {	0 : colorInfo.TITLE_RGB_GOOD_4,
							1 : colorInfo.TITLE_RGB_GOOD_3,
							2 : colorInfo.TITLE_RGB_GOOD_2,
							3 : colorInfo.TITLE_RGB_GOOD_1,
							4 : colorInfo.TITLE_RGB_NORMAL,
							5 : colorInfo.TITLE_RGB_EVIL_1,
							6 : colorInfo.TITLE_RGB_EVIL_2,
							7 : colorInfo.TITLE_RGB_EVIL_3,
							8 : colorInfo.TITLE_RGB_EVIL_4, }
			colorList = COLOR_DICT.get(grade, colorInfo.TITLE_RGB_NORMAL)
			gradeColor = ui.GenerateColor(colorList[0], colorList[1], colorList[2])
							
			self.toolTipAlignment.ClearToolTip()
			self.toolTipAlignment.AutoAppendTextLine(localeInfo.TITLE_NAME_LIST[grade], gradeColor)
			self.toolTipAlignment.AutoAppendTextLine(localeInfo.ALIGNMENT_NAME + str(point))
			self.toolTipAlignment.AlignHorizonalCenter()
			self.toolTipAlignment.ShowToolTip()
		else:
			if self.toolTipAlignment:
				self.toolTipAlignment.HideToolTip()
		
		
		if app.GetGlobalTime() - self.lastUpdateQuickSlot > 500:
			self.lastUpdateQuickSlot = app.GetGlobalTime()
			self.RefreshQuickSlot()
			
	## Skill
	def ToggleLeftMouseButtonModeWindow(self):

		wndMouseButtonMode = self.mouseModeButtonList[self.MOUSE_BUTTON_LEFT]

		if TRUE == wndMouseButtonMode.IsShow():

			wndMouseButtonMode.Hide()

		else:
			wndMouseButtonMode.Show()

	def ToggleRightMouseButtonModeWindow(self):

		wndMouseButtonMode = self.mouseModeButtonList[self.MOUSE_BUTTON_RIGHT]

		if TRUE == wndMouseButtonMode.IsShow():

			wndMouseButtonMode.Hide()
			self.CloseSelectSkill()

		else:
			wndMouseButtonMode.Show()
			self.OpenSelectSkill()

	def OpenSelectSkill(self):

		PAGE_SLOT_COUNT = 6

		(xSkillButton, y) = self.curSkillButton.GetGlobalPosition()
		y -= (37 + 32 + 1)

		for key in self.skillCategoryNameList:

			appendCount = 0
			startNumber = self.skillPageStartSlotIndexDict[key]
			x = xSkillButton

			getSkillIndex=player.GetSkillIndex
			getSkillLevel=player.GetSkillLevel
			for i in xrange(PAGE_SLOT_COUNT):

				skillIndex = getSkillIndex(startNumber+i)
				skillLevel = getSkillLevel(startNumber+i)

				if 0 == skillIndex:
					continue
				if 0 == skillLevel:
					continue
				if skill.IsStandingSkill(skillIndex):
					continue

				
				skillButton = self.SkillButton()
				skillButton.SetSkill(startNumber+i)
				skillButton.SetPosition(x, y)
				skillButton.SetSkillEvent(ui.__mem_func__(self.CloseSelectSkill), startNumber+i+1)
				skillButton.SetSkillToolTip(self.tooltipSkill)
				skillButton.SetTop()
				skillButton.Show()
				self.selectSkillButtonList.append(skillButton)

				appendCount += 1
				x -= 32

			if appendCount > 0:
				y -= 32

	def CloseSelectSkill(self, slotIndex=-1):

		self.mouseModeButtonList[self.MOUSE_BUTTON_RIGHT].Hide()
		for button in self.selectSkillButtonList:
			button.Destroy()

		self.selectSkillButtonList = []

		if -1 != slotIndex:
			self.curSkillButton.Show()
			self.curMouseModeButton[self.MOUSE_BUTTON_RIGHT].Hide()
			player.SetMouseFunc(player.MBT_RIGHT, player.MBF_SKILL)
			player.ChangeCurrentSkillNumberOnly(slotIndex-1)
		else:
			self.curSkillButton.Hide()
			self.curMouseModeButton[self.MOUSE_BUTTON_RIGHT].Show()

	def SelectMouseButtonEvent(self, dir, event):
		SetMouseButtonSetting(dir, event)

		self.CloseSelectSkill()
		self.mouseModeButtonList[dir].Hide()

		btn = 0
		type = self.NONE
		func = self.NONE
		tooltip_text = ""		
		
		if self.MOUSE_BUTTON_LEFT == dir:
			type = player.MBT_LEFT

		elif self.MOUSE_BUTTON_RIGHT == dir:
			type = player.MBT_RIGHT
		if self.EVENT_MOVE == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_move")
			func = player.MBF_MOVE
			tooltip_text = localeInfo.TASKBAR_MOVE
		elif self.EVENT_ATTACK == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_attack")
			func = player.MBF_ATTACK
			tooltip_text = localeInfo.TASKBAR_ATTACK
		elif self.EVENT_AUTO == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_auto_attack")
			func = player.MBF_AUTO
			tooltip_text = localeInfo.TASKBAR_AUTO
		elif self.EVENT_MOVE_AND_ATTACK == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_move_and_attack")
			func = player.MBF_SMART
			tooltip_text = localeInfo.TASKBAR_ATTACK
		elif self.EVENT_CAMERA == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_camera")
			func = player.MBF_CAMERA
			tooltip_text = localeInfo.TASKBAR_CAMERA
		elif self.EVENT_SKILL == event:
			btn = self.mouseModeButtonList[dir].GetChild("button_skill")
			func = player.MBF_SKILL
			tooltip_text = localeInfo.TASKBAR_SKILL

		if 0 != btn:
			self.curMouseModeButton[dir].SetToolTipText(tooltip_text, 0, -18)
			self.curMouseModeButton[dir].SetUpVisual(btn.GetUpVisualFileName())
			self.curMouseModeButton[dir].SetOverVisual(btn.GetOverVisualFileName())
			self.curMouseModeButton[dir].SetDownVisual(btn.GetDownVisualFileName())
			self.curMouseModeButton[dir].Show()

		player.SetMouseFunc(type, func)

	def OnChangeCurrentSkill(self, skillSlotNumber):
		self.curSkillButton.SetSkill(skillSlotNumber)
		self.curSkillButton.Show()
		self.curMouseModeButton[self.MOUSE_BUTTON_RIGHT].Hide()
