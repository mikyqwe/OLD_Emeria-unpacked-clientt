import ui
import net
import background
import uiPhaseCurtain
import constInfo
#import snd
import time
import chat

#starttime = time.strftime("%H")
whitelist = ["metin2_map_b11",
			"metin2_map_c11",
			"metin2_map_a11"]

class uiRainSystem(ui.AniImageBox):
	def __init__(self):
		ui.AniImageBox.__init__(self)

	def __del__(self):
		ui.AniImageBox.__del__(self)

	def Show(self):
		ui.AniImageBox.Show(self)
	
	def LoadWindow(self):
		
		import time
		
		timeHour = time.strftime("%H")
		timeMinute = time.strftime("%M")
		timeSecond = time.strftime("%S")
		
		intMin = int(timeMinute)
		
		# set timestamp
		if intMin < 30:
			timeStamp = timeHour + "00"
		else:
			timeStamp = timeHour + "30"
			
		# variable skybox checkup
		if constInfo.ENVIRONMENT_CYCLE_ID != timeStamp:
			# update variable to current timestamp
			constInfo.ENVIRONMENT_CYCLE_ID = timeStamp
		
		else:
			# current skybox already set
			return

		self.curtain = uiPhaseCurtain.PhaseCurtain()
		self.curtain.speed = 200
		self.curtain.Hide()

		if background.GetCurrentMapName() in whitelist:
			self.__SkyboxUpdate(timeStamp)
					
		return

	def __SkyboxUpdate(self, arg):
	
		# arg = str(arg)

		envSelect = constInfo.ENVIRONMENT_CYCLE + arg + ".msenv"
		
		# chat.AppendChat(chat.CHAT_TYPE_INFO, "RAIN SYSTEM CYCLE: " + envSelect)

		background.RegisterEnvironmentData(int(arg), envSelect)
		background.SetEnvironmentData(int(arg))
		self.curtain.FadeIn()
		
		