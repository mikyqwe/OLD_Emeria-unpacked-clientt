import ui, player, item, net, uicommon, mouseModule, chat, constInfo

MAX_SKILL_COUNT = 5

class BuffiSkillDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.toolTipSkill = None
		self.toolTipItem = None
		self.toolbu = []

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearDictionary()
		self.toolTipSkill = None
		self.toolTipItem = None
		self.toolbu = []

	def LoadDialog(self):
		try:
			ui.PythonScriptLoader().LoadScriptFile(self, "uiscript/BuffiSkillDialog.py")
		except:
			import exception
			exception.Abort("BuffiSkillDialog.LoadDialog.LoadObject")
		try:
			self.GetChild("TitleBar").SetCloseEvent(self.Close)
			self.skillSlot = self.GetChild("skillSlot")
			self.itemSlot = self.GetChild("itemSlotlar")
		except:
			import exception
			exception.Abort("BuffiSkillDialog.LoadDialog.BindObject")

		self.skillSlot.SetOverInItemEvent(ui.__mem_func__(self.__OverInToolTip))
		self.skillSlot.SetOverOutItemEvent(ui.__mem_func__(self.__OverOutToolTip))
		self.itemSlot.SetSelectEmptySlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		self.itemSlot.SetSelectItemSlotEvent(ui.__mem_func__(self.__OnSelectEmptySlot))
		self.itemSlot.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.itemSlot.SetOverOutItemEvent(ui.__mem_func__(self.OverOutToolTipItem))
		self.itemSlot.SetUseSlotEvent(ui.__mem_func__(self.OnPressedSlotButton))

	def OnPressedSlotButton(self, slotNumber):
		self.sorudialog = uicommon.QuestionDialog()
		self.sorudialog.SetText("Are you sure?")
		self.sorudialog.SetAcceptEvent(lambda arg=TRUE: self.cikarUlan(slotNumber))
		self.sorudialog.SetCancelEvent(lambda arg=FALSE: self.sorudialog.Close())
		self.sorudialog.Open()

	def cikarUlan(self, gelen):
		net.SendChatPacket("/cikar_ulan %s" % (str(gelen)))
		self.sorudialog.Close()

	def SetSkillToolTip(self, skillToolTip):
		self.toolTipSkill = skillToolTip

	def SetItemToolTip(self, itemToolTip):
		self.toolTipItem = itemToolTip

	def Open(self):
		self.RefreshSkillData()
		self.SetCenterPosition()
		x,y = self.GetLocalPosition()
		self.SetPosition(50, y)
		del self.toolbu[:]
		ui.ScriptWindow.Show(self)

	def Close(self):
		if self.toolTipSkill:
			self.toolTipSkill.Hide()
		if self.toolTipItem:
			self.toolTipItem.Hide()
		ui.ScriptWindow.Hide(self)
		constInfo.BUFFI_GUI = False
		return True

	#def OnPressEscapeKey(self):
	#	self.Close()
	#	return True

	def RefreshSkillData(self):
		race = net.GetMainActorRace()
		group = net.GetMainActorSkillGroup()
		empire = net.GetMainActorEmpire()
    
		net.RegisterSkills(race, group, empire)
		for index in xrange(5):
			skillIndex = index +143
			slotIndex = player.GetSkillSlotIndex(skillIndex)
			skillGrade = player.GetSkillGrade(slotIndex)
			skillLevel = player.GetSkillLevel(slotIndex)

			self.skillSlot.SetSkillSlotNew(index , skillIndex, skillGrade, skillLevel)
			self.skillSlot.SetSlotCountNew(index , skillGrade, skillLevel)
			self.skillSlot.SetCoverButton(index , "d:/ymir work/ui/public/slot_cover_button_01.sub", "d:/ymir work/ui/public/slot_cover_button_02.sub", "d:/ymir work/ui/public/slot_cover_button_03.sub", "d:/ymir work/ui/public/slot_cover_button_04.sub", False, False)
			self.skillSlot.ShowSlotBaseImage(index )

        

	def __OnSelectEmptySlot(self, selectedSlotPos):
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			targetIndex = player.GetItemIndex(attachedSlotPos)
			if attachedSlotType != player.SLOT_TYPE_INVENTORY:
				return
				
			mouseModule.mouseController.DeattachObject()
				
			item.SelectItem(targetIndex)
			itemType = item.GetItemType()
			itemSubType = item.GetItemSubType()
			itemVnum = player.GetItemIndex(attachedSlotPos)
				
			if item.IsAntiFlag(item.ITEM_ANTIFLAG_FEMALE) or item.IsAntiFlag(item.ITEM_ANTIFLAG_SHAMAN):
				chat.AppendChat(1, "You cannot equip that!")
				return

			if itemSubType == item.COSTUME_TYPE_BODY or itemType == item.ITEM_TYPE_ARMOR:
				selectedSlotPos = 1
			elif itemSubType == item.COSTUME_TYPE_HAIR:
				selectedSlotPos = 2
			elif itemSubType == item.COSTUME_TYPE_WEAPON or itemType == item.ITEM_TYPE_WEAPON:
				selectedSlotPos = 3
			elif int(itemVnum) in (56202,56203,56204,56205,56206):
				selectedSlotPos = 4
			else:
				return

			if selectedSlotPos > 0:
				self.sorudialog = uicommon.QuestionDialog()
				self.sorudialog.SetText("Do you want to equip your item?")
				self.sorudialog.SetAcceptEvent(lambda arg=TRUE: self.takUlan(selectedSlotPos, itemVnum, attachedSlotPos))
				self.sorudialog.SetCancelEvent(lambda arg=FALSE: self.sorudialog.Close())
				self.sorudialog.Open()


	def takUlan(self, gelen, itemVnum, attachedSlotPos):
		net.SendChatPacket("/giy_ulan %s %s %s" % (str(itemVnum), (gelen), (attachedSlotPos)))
		self.sorudialog.Close()

	def SetBuffiKostum(self, vnum):
		self.itemSlot.SetItemSlot(1, int(vnum), 0)
		self.toolbu.append(int(vnum))

	def SetBuffiSac(self, vnum):
		self.itemSlot.SetItemSlot(2, int(vnum), 0)
		self.toolbu.append(int(vnum))

	def SetBuffiSilah(self, vnum):
		self.itemSlot.SetItemSlot(3, int(vnum), 0)
		self.toolbu.append(int(vnum))

	def SetBuffiKostumEfekt(self, vnum):
		self.itemSlot.SetItemSlot(4, int(vnum), 0)
		self.toolbu.append(int(vnum))


	def __OverInToolTip(self, slotIndex):
		if not self.toolTipSkill:
			return

		#skillGrade = player.GetSkillGrade(slotIndex)
		self.toolTipSkill.SetSkillOnlyName(slotIndex, slotIndex+143, 0)

	def __OverOutToolTip(self):
		if self.toolTipSkill:
			self.toolTipSkill.HideToolTip()

	def OverInItem(self, overSlotPos):
		self.toolTipItem.ClearToolTip()
		if not self.toolTipItem:
			return
		constInfo.BUFFI_GUI = True
		metinSlot = [player.GetItemMetinSocket(0, 0, 0) for i in xrange(player.METIN_SOCKET_MAX_NUM)]
		self.toolTipItem.AddItemData(self.toolbu[overSlotPos-1],metinSlot)	
		self.toolTipItem.ShowToolTip()


	def OverOutToolTipItem(self):
		if self.toolTipItem:
			self.toolTipItem.HideToolTip()
		constInfo.BUFFI_GUI = False