import background
import cfg
import constInfo
import ui

SKYBOX_INFO = [
	["Skybox #1", 		"d:/ymir work/environment/rain.msenv"],
	["Skybox #2", 		"d:/ymir work/environment/dark.msenv"],
	["Skybox #3", 		"d:/ymir work/environment/map_n_flame_01.msenv"],
	["Skybox #4", 		"d:/ymir work/environment/morgen.msenv"],
	["Skybox #5", 		"d:/ymir work/environment/abend.msenv"],
	["Skybox #6", 		"d:/ymir work/environment/baytestt.msenv"],
	["Skybox #7", 		"d:/ymir work/environment/test.msenv"],
	["Skybox #8", 		"d:/ymir work/environment/dawnmistwood.msenv"],
	["Skybox #9", 		"d:/ymir work/environment/mtthunder.msenv"],
	["Skybox #10", 		"d:/ymir work/environment/evening.msenv"],
	["Skybox #11", 		"d:/ymir work/environment/kfdungeonn1.msenv"],
	["Skybox #12", 		"d:/ymir work/environment/komnata.msenv"],
	["Skybox #13", 		"d:/ymir work/environment/paradies_hell.msenv"],
	["Skybox #14", 		"d:/ymir work/environment/piekielna_ruina.msenv"],
	["Skybox #15", 		"d:/ymir work/environment/plechito_scorpion_dungeon.msenv"],
	["Skybox #16", 		"d:/ymir work/environment/predawn.msenv"],
	["Skybox #17", 		"d:/ymir work/environment/pustynia.msenv"],
	["Skybox #18", 		"d:/ymir work/environment/rain.msenv"],
	["Skybox #19", 		"d:/ymir work/environment/asenis_fish.msenv"],
	["Skybox #20", 		"d:/ymir work/environment/asenis_gilldia.msenv"],
	["Skybox #21", 		"d:/ymir work/environment/asenis_legenda_forest.msenv"],
	["Skybox #22", 		"d:/ymir work/environment/asenis_m1.msenv"],
	["Skybox #23", 		"d:/ymir work/environment/asenis_mine.msenv"],
	["Skybox #24", 		"d:/ymir work/environment/asenis_ork.msenv"],
	["Skybox #25", 		"d:/ymir work/environment/asenis_recpak.msenv"],
	["Skybox #26", 		"d:/ymir work/environment/asenis_red_las.msenv"],
	["Skybox #27", 		"d:/ymir work/environment/magical_forest.msenv"],
	["Skybox #28", 		"d:/ymir work/environment/foggysunset_kf.msenv"],
	["Skybox #29", 		"d:/ymir work/environment/ice_gilldia.msenv"],
	["Skybox #30", 		"d:/ymir work/environment/kami-sama.msenv"],
	["Skybox # Day", 	"d:/ymir work/environment/metin2_map_blaues_reich_map_1.msenv"],
	["Skybox # Night", 	constInfo.ENVIRONMENT_NIGHT]
]

class SkyBoxChanger(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.LoadSkyBoxChanger()
		
	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)

	def LoadSkyBoxChanger(self):     
		self.SetSize(320, 620)
		self.Hide()
		self.AddFlag('movable')
		self.AddFlag("float")
		self.SetTitleName('Skybox-System')
		self.SetCenterPosition()
		self.SetCloseEvent(self.Close)
		self.LoadGUI()
		
	def LoadGUI(self):		
		self.X_START = 20
		self.Y_START = 50		
		self.typeButtonList, groupButtonDict = [], {}	
		for x in xrange(len(SKYBOX_INFO)):		
			groupButtonDict[x] = ui.Button()
			groupButtonDict[x].SetParent(self)
			groupButtonDict[x].SetPosition(self.X_START, self.Y_START)
			groupButtonDict[x].SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
			groupButtonDict[x].SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
			groupButtonDict[x].SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
			groupButtonDict[x].SetText(SKYBOX_INFO[x][0])
			groupButtonDict[x].SetEvent(self.ChangeSkyBox, x)
			groupButtonDict[x].Show()
			self.typeButtonList.append(groupButtonDict[x])
			
			if x % 2:
				self.X_START = 20
				self.Y_START += 30	
			else:	
				self.X_START = 180
				
		self.skyboxWindowButtonDefaultSkybox = ui.Button()
		self.skyboxWindowButtonDefaultSkybox.SetParent(self)
		self.skyboxWindowButtonDefaultSkybox.SetPosition(self.X_START, self.Y_START)
		self.skyboxWindowButtonDefaultSkybox.SetUpVisual("d:/ymir work/ui/public/Large_Button_01.sub")
		self.skyboxWindowButtonDefaultSkybox.SetOverVisual("d:/ymir work/ui/public/Large_Button_02.sub")
		self.skyboxWindowButtonDefaultSkybox.SetDownVisual("d:/ymir work/ui/public/Large_Button_03.sub")
		self.skyboxWindowButtonDefaultSkybox.SetText("Default Skybox")
		self.skyboxWindowButtonDefaultSkybox.SetEvent(self.UseDefaultSkybox)
		self.skyboxWindowButtonDefaultSkybox.Show()
	
		self.SetSize(290, self.Y_START + 70)		
		
	def UseDefaultSkybox(self):	
		background.SetEnvironmentData(0)	
		cfg.Set(cfg.SAVE_OPTION, "skybox_path", "")
		
	def ChangeSkyBox(self, index):
		background.RegisterEnvironmentData(1, SKYBOX_INFO[index][1]) 
		background.SetEnvironmentData(1)	
		cfg.Set(cfg.SAVE_OPTION, "skybox_path", SKYBOX_INFO[index][1])

	def Destroy(self):
		self.Hide()
		return TRUE
		
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE
		
