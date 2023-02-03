import ui
import net
import wndMgr
import dbg
import app
import event
import _weakref
import localeInfo as _localeInfo
import constInfo
localeInfo = _localeInfo.localeInfo()
import uiScriptLocale

class SelectEmpireWindow(ui.ScriptWindow):

	empireId = {
		0 : net.EMPIRE_A,
		1 : net.EMPIRE_B,
		2 : net.EMPIRE_C
	}

	def __init__(self, stream):
		ui.ScriptWindow.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_EMPIRE, self)
		self.stream=stream

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_EMPIRE, 0)
	def Close(self):
		self.ClearDictionary()
		self.exitButton = None
		self.KillFocus()
		self.Hide()

		app.HideCursor()
		event.Destroy()

	def Open(self):
		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("SelectEmpireWindow")
		self.Show()	

		if not self.__LoadScript("uiScript/intro_empire.py"):
			dbg.TraceError("SelectEmpireWindow.Open - __LoadScript Error")
			return
			
		app.ShowCursor()

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)	
		except:
			import exception
			exception.Abort("SelectEmpireWindow.__LoadScript.LoadObject")

		try:
			self.selectButtons = {
				0 : self.GetChild("ButtonSelectRedEmpire"),
				1 : self.GetChild("ButtonSelectYellowEmpire"),
				2 : self.GetChild("ButtonSelectBlueEmpire"),
			}
			self.exitButton = self.GetChild("ExitButton")
		except:
			import exception
			exception.Abort("SelectEmpireWindow.__LoadScript.BindObject")					

		self.exitButton.SetEvent(ui.__mem_func__(self.ClickExitButton))
		for id in range(len(self.selectButtons)):
			self.selectButtons[id].SetEvent(ui.__mem_func__(self.SelectEmpire), id)

		#if constInfo.ENABLE_INTRO_ANIMATION == 1:
			#self.CreateAnimateBackground()
			
		return 1

	def CreateAnimateBackground(self):
		self.AnimationImage = ui.AniImageBox()
		self.AnimationImage.SetParent(self.GetChild("video_layer"))
		self.AnimationImage.SetDelay(2)
		for x in xrange(89):
			self.AnimationImage.AppendImageScale("d:/ymir work/ui/intro/animation/empire/frame_%d.sub" % (x), float(wndMgr.GetScreenWidth()) / 1920.0, float(wndMgr.GetScreenHeight()) / 1080.0)
			self.AnimationImage.Show()
			
	def SelectEmpire(self, id):
		net.SendSelectEmpirePacket(self.empireId[id])
		self.stream.SetSelectCharacterPhase()

	def ClickExitButton(self):
		self.stream.SetLoginPhase()
		
	def OnPressEscapeKey(self):
		self.ClickExitButton()
		return TRUE

class ReselectEmpireWindow(SelectEmpireWindow):
	def SelectEmpire(self, id):
		net.SendSelectEmpirePacket(self.empireId[id])
		self.stream.SetCreateCharacterPhase()

	def ClickExitButton(self):
		self.stream.SetSelectCharacterPhase()
