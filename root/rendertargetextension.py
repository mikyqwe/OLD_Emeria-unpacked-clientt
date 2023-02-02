import ui
import wndMgr
import renderTarget
import player
import item
import app
import constInfo

class RenderTarget(ui.ScriptWindow):
	RENDER_TARGET_INDEX = 66
	Window = None

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.curRot = 0.0
		self.max_pos_x = wndMgr.GetScreenWidth()
		self.max_pos_y = wndMgr.GetScreenHeight()

		self.emotionTime = 0
		self.refreshTime = 0

		self.Initialize()
		self.Init()

	def Initialize(self):
		self.interface = None

	@staticmethod
	def Get():
		if RenderTarget.Window == None:
			RenderTarget.Window = RenderTarget()

		return RenderTarget.Window

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.Initialize()

	def DisplayUser(self, vRace=0, refresh=False, vItemWeapon=0, vItemArmor=0, vItemHair=0, vItemEffectBody=0, vItemEffectWeaponVnum = 0):
		if refresh:
			self.refreshTime = app.GetTime()
			return

		renderTarget.SetVisibility(self.RENDER_TARGET_INDEX, True)
		renderTarget.SelectModel(self.RENDER_TARGET_INDEX, vRace)

		if vRace > 7:
			return

		playerRace = player.GetRace() # Get player race

		########## IF SELECTED FROM INVENTORY ELSE GET EQUIPPED ITEM DATA ##########
		# Weapon / Costume
		if vItemWeapon:
			renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, vItemWeapon)
		else:
			weaponVnum = 0
			if app.ENABLE_COSTUME_WEAPON_SYSTEM and player.GetItemIndex(item.COSTUME_SLOT_WEAPON):
				weaponVnum = player.GetItemIndex(item.COSTUME_SLOT_WEAPON)
			elif player.GetItemIndex(item.EQUIPMENT_WEAPON):
				weaponVnum = player.GetItemIndex(item.EQUIPMENT_WEAPON)

			if playerRace == vRace and weaponVnum:
				renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, weaponVnum)

		# Armor / Costume
		if vItemArmor:
			renderTarget.SetArmor(self.RENDER_TARGET_INDEX, vItemArmor)
		else:
			armorVnum = 0
			if player.GetItemIndex(item.COSTUME_SLOT_BODY):
				armorVnum = player.GetItemIndex(item.COSTUME_SLOT_BODY)
			elif player.GetItemIndex(item.EQUIPMENT_BODY):
				armorVnum = player.GetItemIndex(item.EQUIPMENT_BODY)

			if playerRace == vRace and armorVnum:
				renderTarget.SetArmor(self.RENDER_TARGET_INDEX, armorVnum)

		# Hair
		if vItemHair:
			renderTarget.SetHair(self.RENDER_TARGET_INDEX, vItemHair)
		else:
			hairVnum = 0
			if player.GetItemIndex(item.COSTUME_SLOT_HAIR):
				hairVnum = player.GetItemIndex(item.COSTUME_SLOT_HAIR)
				item.SelectItem(hairVnum)

			if playerRace == vRace and hairVnum:
				renderTarget.SetHair(self.RENDER_TARGET_INDEX, item.GetValue(3))

		if app.ENABLE_EFFECT_SYSTEM:
			# Body Effect
			if vItemEffectBody:
				renderTarget.SetBodyEffect(self.RENDER_TARGET_INDEX, vItemEffectBody)
			else:
				if player.GetItemIndex(item.EQUIPMENT_BODY): 
					bodyEffectVnum = 0
					if player.GetItemIndex(item.COSTUME_SLOT_EFFECT_ARMOR):
						bodyEffectVnum = player.GetItemIndex(item.COSTUME_SLOT_EFFECT_ARMOR)
						item.SelectItem(bodyEffectVnum)

						if bodyEffectVnum and playerRace == vRace :
							renderTarget.SetBodyEffect(self.RENDER_TARGET_INDEX, item.GetValue(0))

			# Weapon Effect
			if player.GetItemIndex(item.EQUIPMENT_WEAPON): 
				playerWeaponSubType = 0
				weaponEffectVnum = 0
				if player.GetItemIndex(item.COSTUME_SLOT_EFFECT_WEAPON):
					weaponEffectVnum = player.GetItemIndex(item.COSTUME_SLOT_EFFECT_WEAPON)
					
					item.SelectItem(player.GetItemIndex(item.EQUIPMENT_WEAPON))
					playerWeaponSubType = item.GetItemSubType()

				if vItemEffectWeaponVnum:
					renderTarget.SetWeaponEffect(self.RENDER_TARGET_INDEX, vItemEffectWeaponVnum, playerWeaponSubType)
				else:
					if weaponEffectVnum and playerRace == vRace :
						renderTarget.SetWeaponEffect(self.RENDER_TARGET_INDEX, weaponEffectVnum, playerWeaponSubType)

	def Init(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/RenderTargetWindow.py")
		except:
			import exception
			exception.Abort("RenderTargetWindow.LoadDialog.LoadScript")

		try:
			self.board = self.GetChild("board")
			self.board.SetCloseEvent(self.Close)
			
			self.RenderTarget = self.GetChild("RenderTarget")

			self.buttons = {
				"MoveUp" : self.GetChild("MoveUp"),
				"MoveDown" : self.GetChild("MoveDown"),

				"RotateLeft" : self.GetChild("RotateLeft"),
				"RotateRight" : self.GetChild("RotateRight"),

				"ZoomIn" : self.GetChild("ZoomIn"),
				"ZoomOut" : self.GetChild("ZoomOut"),

				"Refresh" : self.GetChild("Refresh"),
				"DoEmotion" : self.GetChild("DoEmotion"),
			}

			self.buttons["MoveUp"].SetEvent(ui.__mem_func__(self.DownUp))
			self.buttons["MoveDown"].SetEvent(ui.__mem_func__(self.DownUp))

			self.buttons["RotateLeft"].SetEvent(ui.__mem_func__(self.RotationProgress))
			self.buttons["RotateRight"].SetEvent(ui.__mem_func__(self.RotationProgress))

			self.buttons["ZoomIn"].SetEvent(ui.__mem_func__(self.ZoomProgress))
			self.buttons["ZoomOut"].SetEvent(ui.__mem_func__(self.ZoomProgress))

			self.buttons["Refresh"].SetEvent(ui.__mem_func__(self.UpdateEquipment))
			self.buttons["DoEmotion"].SetEvent(ui.__mem_func__(self.DoEmotion))

			self.SetCenterPosition()

		except:
			import exception
			exception.Abort("RenderTargetWindow.LoadDialog.BindObject")

		renderTarget.SetBackground(self.RENDER_TARGET_INDEX, "d:/ymir work/ui/render_target.jpg")

	def BindInterface(self, interface):
		self.interface = interface

	def Destroy(self):
		self.Close()
		self.Initialize()

	def Close(self):
		self.Hide()

	def Open(self):
		self.Show()
		self.SetTop()
		renderTarget.SetAutoRotate(self.RENDER_TARGET_INDEX, False)

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def MINMAX(self, min, value, max):
		if value < min:
			return min
		elif value > max:
			return max
		else:
			return value

	def UpdateEquipment(self):
		renderTarget.RefreshRender(self.RENDER_TARGET_INDEX, 0)
		self.DisplayUser(player.GetRace())

	def OnUpdate(self):
		self.ZoomProgress()
		self.RotationProgress()
		self.DownUp()
		x, y = self.GetGlobalPosition()
		pos_x = self.MINMAX(0, x, self.max_pos_x)
		pos_y = self.MINMAX(0, y, self.max_pos_y)
		self.SetPosition(pos_x, pos_y)

		if self.refreshTime != 0 and app.GetTime() - self.refreshTime > 0.2:
			self.UpdateEquipment()
			self.refreshTime = 0

		if self.emotionTime != 0 and app.GetTime() - self.emotionTime > 5.0:
			self.UpdateEquipment()
			self.emotionTime = 0

	def RotationProgress(self):
		if self.buttons["RotateLeft"].IsDown():
			renderTarget.SetModelRotation(self.RENDER_TARGET_INDEX, -5)

		if self.buttons["RotateRight"].IsDown():
			renderTarget.SetModelRotation(self.RENDER_TARGET_INDEX, 5)

	def DownUp(self):
		if self.buttons["MoveUp"].IsDown():
			renderTarget.DownUp(self.RENDER_TARGET_INDEX, -5)

		if self.buttons["MoveDown"].IsDown():
			renderTarget.DownUp(self.RENDER_TARGET_INDEX, 5)

	def ZoomProgress(self):
		if self.buttons["ZoomIn"].IsDown():
			renderTarget.ZoomCamera(self.RENDER_TARGET_INDEX, 5)
		
		if self.buttons["ZoomOut"].IsDown():
			renderTarget.ZoomCamera(self.RENDER_TARGET_INDEX, -5)

	def DoEmotion(self):
		renderTarget.DoEmotion(self.RENDER_TARGET_INDEX)
		self.emotionTime = app.GetTime()

	def __ResetSettings(self):
		self.curRot = 0.0
		renderTarget.ResetSettings(self.RENDER_TARGET_INDEX)

	def AdjustPosition(self):
		if self.interface and self.interface.wndInventory and self.interface.wndInventory.GetGlobalPosition():
			x, y = self.interface.wndInventory.GetGlobalPosition()
			self.SetPosition(x - 210, y + 210)
