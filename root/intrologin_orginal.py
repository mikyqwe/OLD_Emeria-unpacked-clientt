import dbg
import app
import net
import ui
import ime
import snd
import wndMgr
import musicInfo
import serverInfo
import systemSetting
import ServerStateChecker
import localeInfo as _localeInfo
localeInfo = _localeInfo.localeInfo()
import constInfo
import uiCommon
import time
import serverCommandParser
import ime
import uiScriptLocale
import os
import uiGuild

RUNUP_MATRIX_AUTH = FALSE
NEWCIBN_PASSPOD_AUTH = FALSE

LOGIN_DELAY_SEC = 0.0
SKIP_LOGIN_PHASE = FALSE
SKIP_LOGIN_PHASE_SUPPORT_CHANNEL = FALSE
FULL_BACK_IMAGE = FALSE

PASSPOD_MSG_DICT = {}

VIRTUAL_KEYBOARD_NUM_KEYS = 46
VIRTUAL_KEYBOARD_RAND_KEY = TRUE

def Suffle(src):
	if VIRTUAL_KEYBOARD_RAND_KEY:
		items = [item for item in src]

		itemCount = len(items)
		for oldPos in xrange(itemCount):
			newPos = app.GetRandom(0, itemCount-1)
			items[newPos], items[oldPos] = items[oldPos], items[newPos]

		return "".join(items)
	else:
		return src

if localeInfo.IsNEWCIBN() or localeInfo.IsCIBN10():
	LOGIN_DELAY_SEC = 60.0
	FULL_BACK_IMAGE = TRUE
	NEWCIBN_PASSPOD_AUTH = TRUE
	PASSPOD_MSG_DICT = {
		"PASERR1"	: localeInfo.LOGIN_FAILURE_PASERR1,
		"PASERR2"	: localeInfo.LOGIN_FAILURE_PASERR2,
		"PASERR3"	: localeInfo.LOGIN_FAILURE_PASERR3,
		"PASERR4"	: localeInfo.LOGIN_FAILURE_PASERR4,
		"PASERR5"	: localeInfo.LOGIN_FAILURE_PASERR5,
	}

elif localeInfo.IsYMIR() or localeInfo.IsCHEONMA():
	FULL_BACK_IMAGE = TRUE

elif localeInfo.IsHONGKONG():
	FULL_BACK_IMAGE = TRUE
	RUNUP_MATRIX_AUTH = TRUE 
	PASSPOD_MSG_DICT = {
		"NOTELE"	: localeInfo.LOGIN_FAILURE_NOTELEBLOCK,
	}

elif localeInfo.IsJAPAN():
	FULL_BACK_IMAGE = TRUE
	
elif localeInfo.IsBRAZIL():
	LOGIN_DELAY_SEC = 60.0

def IsFullBackImage():
	global FULL_BACK_IMAGE
	return FULL_BACK_IMAGE

def IsLoginDelay():
	global LOGIN_DELAY_SEC
	if LOGIN_DELAY_SEC > 0.0:
		return TRUE
	else:
		return FALSE

def IsRunupMatrixAuth():
	global RUNUP_MATRIX_AUTH
	return RUNUP_MATRIX_AUTH	

def IsNEWCIBNPassPodAuth():
	global NEWCIBN_PASSPOD_AUTH
	return NEWCIBN_PASSPOD_AUTH

def GetLoginDelay():
	global LOGIN_DELAY_SEC
	return LOGIN_DELAY_SEC

app.SetGuildMarkPath("test")

class ConnectingDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__LoadDialog()
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __LoadDialog(self):
		try:
			PythonScriptLoader = ui.PythonScriptLoader()
			PythonScriptLoader.LoadScriptFile(self, "UIScript/ConnectingDialog.py")

			self.board = self.GetChild("board")
			self.message = self.GetChild("message")
			self.countdownMessage = self.GetChild("countdown_message")

		except:
			import exception
			exception.Abort("ConnectingDialog.LoadDialog.BindObject")

	def Open(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime

		self.Lock()
		self.SetCenterPosition()
		self.SetTop()
		self.Show()		

	def Close(self):
		self.Unlock()
		self.Hide()

	def Destroy(self):
		self.Hide()
		self.ClearDictionary()

	def SetText(self, text):
		self.message.SetText(text)

	def SetCountDownMessage(self, waitTime):
		self.countdownMessage.SetText("%.0f%s" % (waitTime, localeInfo.SECOND))

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)

	def OnUpdate(self):
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			self.SetCountDownMessage(self.endTime - time.clock())

	def OnPressExitKey(self):
		#self.eventExit()
		return TRUE

class LoginWindow(ui.ScriptWindow):

	config = {
		"name" : "Elendosfiles",
		"accountFile" : "elendosfiles.accounts",
		"ip" : "193.135.10.41",
		"auth" : 11212,
		"channel" : [13101, 14070, 15070, 16070, 17070],
		"url" : {
			"forgot" : "https://elendos.shop/",
			"vote" : "https://elendos.shop/",
			"forum" : "xxxxxxxxx",
			"register" : "https://elendos.shop/",
		},
	}

	values = {
        "accounts" : {
            0 : {"id" : "", "pw" : "",},
            1 : {"id" : "", "pw" : "",},
            2 : {"id" : "", "pw" : "",},
            3 : {"id" : "", "pw" : "",},
        },
	}

	IS_TEST = net.IsTest()

	def __init__(self, stream):
		print "NEW LOGIN WINDOW  ----------------------------------------------------------------------------"
		ui.ScriptWindow.__init__(self)
		net.SetPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(self)

		self.matrixInputChanceCount = 0
		self.lastLoginTime = 0
		self.inputDialog = None
		self.connectingDialog = None
		self.stream=stream
		self.isNowCountDown=FALSE
		self.isStartError=FALSE

		self.xServerBoard = 0
		self.yServerBoard = 0
		
		self.loadingImage = None

		self.virtualKeyboard = None
		self.virtualKeyboardMode = "ALPHABET"
		self.virtualKeyboardIsUpper = FALSE
		
	def __del__(self):
		net.ClearPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(0)
		ui.ScriptWindow.__del__(self)
		print "---------------------------------------------------------------------------- DELETE LOGIN WINDOW"

	def Open(self):
		ServerStateChecker.Create(self)

		print "LOGIN WINDOW OPEN ----------------------------------------------------------------------------"

		self.loginFailureMsgDict={

			"ALREADY"	: localeInfo.LOGIN_FAILURE_ALREAY,
			"NOID"		: localeInfo.LOGIN_FAILURE_NOT_EXIST_ID,
			"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"FULL"		: localeInfo.LOGIN_FAILURE_TOO_MANY_USER,
			"SHUTDOWN"	: localeInfo.LOGIN_FAILURE_SHUTDOWN,
			"REPAIR"	: localeInfo.LOGIN_FAILURE_REPAIR_ID,
			"BLOCK"		: localeInfo.LOGIN_FAILURE_BLOCK_ID,
			"WRONGMAT"	: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER_TRIPLE,
			"BESAMEKEY"	: localeInfo.LOGIN_FAILURE_BE_SAME_KEY,
			"NOTAVAIL"	: localeInfo.LOGIN_FAILURE_NOT_AVAIL,
			"NOBILL"	: localeInfo.LOGIN_FAILURE_NOBILL,
			"BLKLOGIN"	: localeInfo.LOGIN_FAILURE_BLOCK_LOGIN,
			"WEBBLK"	: localeInfo.LOGIN_FAILURE_WEB_BLOCK,
			"BADSCLID"	: localeInfo.LOGIN_FAILURE_WRONG_SOCIALID,
			"AGELIMIT"	: localeInfo.LOGIN_FAILURE_SHUTDOWN_TIME,
		}

		self.loginFailureFuncDict = {
			"WRONGPWD"	: self.__DisconnectAndInputPassword,
			"QUIT"		: app.Exit,
		}

		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("LoginWindow")

		if not self.__LoadScript("poccix_login_ui.py"):
			dbg.TraceError("LoginWindow.Open - __LoadScript Error")
			return

		self.__loadConfigs()
	
		if musicInfo.loginMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("BGM/"+musicInfo.loginMusic)

		snd.SetSoundVolume(systemSetting.GetSoundVolume())

		# pevent key "[" "]"
		ime.AddExceptKey(91)
		ime.AddExceptKey(93)
			
		self.Show()
		app.ShowCursor()
		

	def Close(self):

		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None

		ServerStateChecker.Initialize(self)

		print "---------------------------------------------------------------------------- CLOSE LOGIN WINDOW "
		if musicInfo.loginMusic != "" and musicInfo.selectMusic != "":
			snd.FadeOutMusic("BGM/"+musicInfo.loginMusic)

		self.editLines["id"].SetTabEvent(0)
		self.editLines["id"].SetReturnEvent(0)
		self.editLines["pw"].SetReturnEvent(0)
		self.editLines["pw"].SetTabEvent(0)
		self.editLines["pin"].SetReturnEvent(0)
		self.editLines["pin"].SetTabEvent(0)

		self.connectBoard = None
		self.loginBoard = None
		self.editLines["id"] = None
		self.editLines["pw"] = None
		self.editLines["pin"] = None
		self.inputDialog = None
		self.connectingDialog = None
		self.loadingImage = None

		self.serverBoard				= None
		self.serverList					= None
		self.channelList				= None

		self.KillFocus()
		self.Hide()

		self.stream.popupWindow.Close()
		self.loginFailureFuncDict=None

		ime.ClearExceptKey()

		app.HideCursor()

	def __SaveChannelInfo(self):
		try:
			file=open("channel.inf", "w")
			file.write("%d %d %d" % (self.__GetServerID(), self.__GetChannelID(), self.__GetRegionID()))
		except:
			print "LoginWindow.__SaveChannelInfo - SaveError"

	def __LoadChannelInfo(self):
		try:
			file=open("channel.inf")
			lines=file.readlines()
			
			if len(lines)>0:
				tokens=lines[0].split()

				selServerID=int(tokens[0])
				selChannelID=int(tokens[1])
				
				if len(tokens) == 3:
					regionID = int(tokens[2])

				return regionID, selServerID, selChannelID

		except:
			print "LoginWindow.__LoadChannelInfo - OpenError"
			return -1, -1, -1

	def __ExitGame(self):
		app.Exit()

	def SetIDEditLineFocus(self):
		if self.editLines["id"] != None:
			self.editLines["id"].SetFocus()

	def SetPasswordEditLineFocus(self):
		if localeInfo.IsEUROPE():
			if self.editLines["id"] != None: #0000862: [M2EU] �α���â �˾� ����: ����� ���� None ������
				self.editLines["id"].SetText("")
				self.editLines["id"].SetFocus() #0000685: [M2EU] ���̵�/��й�ȣ ���� ���� ���� ����: ������ ���̵�� ��Ŀ���� ���� �����

			if self.editLines["pw"] != None: #0000862: [M2EU] �α���â �˾� ����: ����� ���� None ������
				self.editLines["pw"].SetText("")
		else:
			if self.editLines["pw"] != None:
				self.editLines["pw"].SetFocus()								

	def SetPinEditLineFocus(self):
		if self.editLines["pin"] != None:
			self.editLines["pin"].SetFocus()
			
	def OnEndCountDown(self):
		self.isNowCountDown = FALSE
		if localeInfo.IsBRAZIL():
			self.timeOutMsg = TRUE
		else:
			self.timeOutMsg = FALSE
		self.OnConnectFailure()

	def OnConnectFailure(self):

		if self.isNowCountDown:
			return

		snd.PlaySound("sound/ui/loginfail.wav")

		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None
		self.PopupNotifyMessage(localeInfo.LOGIN_CONNECT_FAILURE, self.SetPasswordEditLineFocus)

	def OnHandShake(self):
		if not IsLoginDelay():
			snd.PlaySound("sound/ui/loginok.wav")
			self.PopupDisplayMessage(localeInfo.LOGIN_CONNECT_SUCCESS)

	def OnLoginStart(self):
		if not IsLoginDelay():
			self.PopupDisplayMessage(localeInfo.LOGIN_PROCESSING)
			
		if constInfo.LOADED_RESOURCES == 0:
			net.LoadResourcesInCache()
			constInfo.LOADED_RESOURCES = 1

	def OnLoginFailure(self, error):
		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None

		try:
			loginFailureMsg = self.loginFailureMsgDict[error]
		except KeyError:
			if PASSPOD_MSG_DICT:
				try:
					loginFailureMsg = PASSPOD_MSG_DICT[error]
				except KeyError:
					loginFailureMsg = localeInfo.LOGIN_FAILURE_UNKNOWN + error
			else:
				loginFailureMsg = localeInfo.LOGIN_FAILURE_UNKNOWN  + error

		loginFailureFunc=self.loginFailureFuncDict.get(error, self.SetPasswordEditLineFocus)
		self.PopupNotifyMessage(loginFailureMsg, loginFailureFunc)

		snd.PlaySound("sound/ui/loginfail.wav")

	def __DisconnectAndInputID(self):
		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None

		self.SetIDEditLineFocus()
		net.Disconnect()

	def __DisconnectAndInputPassword(self):
		if self.connectingDialog:
			self.connectingDialog.Close()
		self.connectingDialog = None

		self.SetPasswordEditLineFocus()
		net.Disconnect()

	def __LoadScript(self, fileName):
		import dbg
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.LoadObject")
		try:
			self.editLines = {
				"id" : self.GetChild("edit_username"),
				"pw" : self.GetChild("edit_password"),
				"pin" : self.GetChild("edit_pin"),
			}

			self.accountBtn = {
				0 : self.GetChild("btn_account_01"),
				1 : self.GetChild("btn_account_02"),
				2 : self.GetChild("btn_account_03"),
				3 : self.GetChild("btn_account_04"),
			}

			self.deleteBtn = {
				0 : self.GetChild("btn_delete_01"),
				1 : self.GetChild("btn_delete_02"),
				2 : self.GetChild("btn_delete_03"),
				3 : self.GetChild("btn_delete_04"),
			}

			self.channelBtn = {
				0 : self.GetChild("btn_channel_01"),
				1 : self.GetChild("btn_channel_02"),
				2 : self.GetChild("btn_channel_03"),
				#3 : self.GetChild("btn_channel_04"),
				#4 : self.GetChild("btn_channel_05"),
			}

			self.channelLabel = {
				0 : self.GetChild("label_channel_01"),
				1 : self.GetChild("label_channel_02"),
				2 : self.GetChild("label_channel_03"),
				#3 : self.GetChild("label_channel_04"),
				#4 : self.GetChild("label_channel_05"),
			}

			self.accountLabel = {
				0 : self.GetChild("label_account_01"),
				1 : self.GetChild("label_account_02"),
				2 : self.GetChild("label_account_03"),
				3 : self.GetChild("label_account_04"),
			}

			self.btn_forgot = self.GetChild("btn_forgot")
			self.btn_save = self.GetChild("btn_save")
			self.btn_register = self.GetChild("btn_register")
			self.btn_forum = self.GetChild("btn_forum")
			self.btn_vote = self.GetChild("btn_vote")
			self.btn_login = self.GetChild("btn_login")
			self.btn_close = self.GetChild("btn_close")
			
			line = "2"
			try:
				file = open("lang.cfg", "r")
				line = file.readlines()[0]
				file.close()
			except:
				file = open("lang.cfg", "w")
				file.write("2")
				file.close()
				
			
			constInfo.SEL_LANG = int(line)
			
			self.lang_de = self.GetChild("lang_de")
			self.lang_cz = self.GetChild("lang_cz")
			self.lang_en = self.GetChild("lang_en")
			self.lang_es = self.GetChild("lang_es")
			self.lang_gl = self.GetChild("lang_gl")
			self.lang_hu = self.GetChild("lang_hu")
			self.lang_it = self.GetChild("lang_it")
			self.lang_pl = self.GetChild("lang_pl")
			self.lang_pt = self.GetChild("lang_pt")
			self.lang_tr = self.GetChild("lang_tr")
			self.lang_ro = self.GetChild("lang_ro")
			
			
			self.lang_de.SetEvent(ui.__mem_func__(self.setLanguage), 1) 
			self.lang_cz.SetEvent(ui.__mem_func__(self.setLanguage), 0)
			self.lang_en.SetEvent(ui.__mem_func__(self.setLanguage), 2)
			self.lang_es.SetEvent(ui.__mem_func__(self.setLanguage), 3)
			self.lang_gl.SetEvent(ui.__mem_func__(self.setLanguage), 4)
			self.lang_hu.SetEvent(ui.__mem_func__(self.setLanguage), 5)
			self.lang_it.SetEvent(ui.__mem_func__(self.setLanguage), 6)
			self.lang_pl.SetEvent(ui.__mem_func__(self.setLanguage), 7)
			self.lang_pt.SetEvent(ui.__mem_func__(self.setLanguage), 8)
			self.lang_tr.SetEvent(ui.__mem_func__(self.setLanguage), 10)
			self.lang_ro.SetEvent(ui.__mem_func__(self.setLanguage), 9)

		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.BindObject")

		return 1

	def setLanguage(self, id):
		file = open("locale.cfg", "w")
		if id == 0:
			file.write("10002 1250 cz")
		elif id == 1:
			file.write("10002 1252 de")
		elif id == 2:
			file.write("10002 1252 en")
		elif id == 3:
			file.write("10002 1252 es")
		elif id == 4:
			file.write("10002 1253 gr")
		elif id == 5:
			file.write("10002 1250 hu")
		elif id == 6:
			file.write("10002 1252 it")
		elif id == 7:
			file.write("10002 1250 pl")
		elif id == 8:
			file.write("10002 1252 pt")
		elif id == 9:
			file.write("10002 1250 ro")
		elif id == 10:
			file.write("10002 1254 tr")
		file.close()
		file = open("lang.cfg", "w")
		file.write(str(id))
		file.close()
		dbg.LogBox("The laguage of client was changed!\nPlease restart the Elendosfiles Client.")
		app.Exit()

	def __loadConfigs(self):
		self.btn_close.SetEvent(ui.__mem_func__(self.__OnClickExitButton))
		self.btn_login.SetEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.btn_save.SetEvent(ui.__mem_func__(self.saveAccount))
		self.btn_forgot.SetEvent(ui.__mem_func__(self.openUrl), self.config["url"]["forgot"])
		self.btn_vote.SetEvent(ui.__mem_func__(self.openUrl), self.config["url"]["vote"])
		self.btn_forum.SetEvent(ui.__mem_func__(self.openUrl), self.config["url"]["forum"])
		self.btn_register.SetEvent(ui.__mem_func__(self.openUrl), self.config["url"]["register"])
		self.editLines["id"].SetFocus()
		self.editLines["id"].SetReturnEvent(ui.__mem_func__(self.editLines["pw"].SetFocus))
		self.editLines["id"].SetTabEvent(ui.__mem_func__(self.editLines["pw"].SetFocus))
		self.editLines["pw"].SetReturnEvent(ui.__mem_func__(self.editLines["pin"].SetFocus))
		self.editLines["pw"].SetTabEvent(ui.__mem_func__(self.editLines["pin"].SetFocus))
		self.editLines["pin"].SetReturnEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.editLines["pin"].SetTabEvent(ui.__mem_func__(self.editLines["id"].SetFocus))
		for delId in range(len(self.deleteBtn)):
			self.deleteBtn[delId].SetEvent(ui.__mem_func__(self.deleteAccount), delId)
		for accId in range(len(self.accountBtn)):
			self.accountBtn[accId].SetEvent(ui.__mem_func__(self.selectAccount), accId)
		for chId in range(len(self.channelBtn)):
			self.channelBtn[chId].SetEvent(ui.__mem_func__(self.selectChannel), chId)
		
		self.selectChannel(0)
		self.loadAccounts()

	def openUrl(self, url):
		import os
		os.startfile(url)

	def deleteAccount(self, idx):
		self.values["accounts"][idx] = {"id" : "", "pw" : "", "pin" : ""}
		self.saveAccountFile()
		
	def selectAccount(self, idx):
		self.editLines["id"].SetText(self.values["accounts"][idx]["id"])
		self.editLines["pw"].SetText(self.values["accounts"][idx]["pw"])
		self.editLines["pin"].SetText(self.values["accounts"][idx]["pin"])
		self.__OnClickLoginButton()

	def saveAccount(self):
		saved = False
		for accId in self.values["accounts"]:
			if self.values["accounts"][accId]["id"] == "":
				self.values["accounts"][accId] = {"id" : self.editLines["id"].GetText(), "pw" : self.editLines["pw"].GetText(), "pin" : self.editLines["pin"].GetText()}
				saved = True
				break
		if saved:
			self.saveAccountFile()
		else:
			self.PopupNotifyMessage("No available slot.")

	def saveAccountFile(self):
		with open(self.config["accountFile"], "w") as keyfile:
			for accId in self.values["accounts"]:
				keyfile.write("{}#{}#{}\n".format(self.values["accounts"][accId]["id"], self.values["accounts"][accId]["pw"], self.values["accounts"][accId]["pin"]))
		self.loadAccounts()

	def loadAccounts(self):
		with open(self.config["accountFile"]) as keyfile:
			accounts = [x.split('#') for x in [l.replace('\n','') for l in keyfile.readlines()]]
			for accId in range(len(accounts)):
				self.values["accounts"][accId] = {"id" : accounts[accId][0], "pw" : accounts[accId][1], "pin" : accounts[accId][2],}
				if(accounts[accId][0] == ""):
					accounts[accId][0] = "Slot"
				self.accountLabel[accId].SetText("#{} - {}".format(str(accId + 1), accounts[accId][0]))

	def selectChannel(self, idx):
		for btn in range(len(self.channelBtn)):
			self.channelBtn[btn].SetUp()
			self.channelLabel[btn].SetText("Channel {}".format(str(btn + 1)))
		self.channelBtn[idx].Down()
		self.channelLabel[idx].SetText("Channel {}".format(str(idx + 1)))

		self.stream.SetConnectInfo(self.config["ip"], self.config["channel"][idx], self.config["ip"], self.config["auth"])
		net.SetMarkServer(self.config["ip"], self.config["channel"][0])
		net.SetServerInfo("{} - Channel {}".format(self.config["name"], str(idx + 1)))


	def __VirtualKeyboard_SetKeys(self, keyCodes):
		uiDefFontBackup = localeInfo.UI_DEF_FONT
		localeInfo.UI_DEF_FONT = localeInfo.UI_DEF_FONT_LARGE

		keyIndex = 1
		for keyCode in keyCodes:					
			key = self.GetChild2("key_%d" % keyIndex)
			if key:
				key.SetEvent(lambda x=keyCode: self.__VirtualKeyboard_PressKey(x))
				key.SetText(keyCode)
				key.ButtonText.SetFontColor(0, 0, 0)
				keyIndex += 1
			
		for keyIndex in xrange(keyIndex, VIRTUAL_KEYBOARD_NUM_KEYS+1):
			key = self.GetChild2("key_%d" % keyIndex)
			if key:
				key.SetEvent(lambda x=' ': self.__VirtualKeyboard_PressKey(x))
				key.SetText(' ')
		
		localeInfo.UI_DEF_FONT = uiDefFontBackup

	def __VirtualKeyboard_PressKey(self, code):
		ime.PasteString(code)
		
		#if self.virtualKeyboardMode == "ALPHABET" and self.virtualKeyboardIsUpper:
		#	self.__VirtualKeyboard_SetLowerMode()
			
	def __VirtualKeyboard_PressBackspace(self):
		ime.PasteBackspace()
		
	def __VirtualKeyboard_PressReturn(self):
		ime.PasteReturn()		

	def __VirtualKeyboard_SetUpperMode(self):
		self.virtualKeyboardIsUpper = TRUE
		
		if self.virtualKeyboardMode == "ALPHABET":
			self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_ALPHABET_UPPERS)
		elif self.virtualKeyboardMode == "NUMBER":
			if localeInfo.IsBRAZIL():
				self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_SYMBOLS_BR)
			else:	
				self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_SYMBOLS)
		else:
			self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_NUMBERS)
			
	def __VirtualKeyboard_SetLowerMode(self):
		self.virtualKeyboardIsUpper = FALSE
		
		if self.virtualKeyboardMode == "ALPHABET":
			self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_ALPHABET_LOWERS)
		elif self.virtualKeyboardMode == "NUMBER":
			self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_NUMBERS)			
		else:
			if localeInfo.IsBRAZIL():
				self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_SYMBOLS_BR)
			else:	
				self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_SYMBOLS)
			
	def __VirtualKeyboard_SetAlphabetMode(self):
		self.virtualKeyboardIsUpper = FALSE
		self.virtualKeyboardMode = "ALPHABET"		
		self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_ALPHABET_LOWERS)	

	def __VirtualKeyboard_SetNumberMode(self):			
		self.virtualKeyboardIsUpper = FALSE
		self.virtualKeyboardMode = "NUMBER"
		self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_NUMBERS)
					
	def __VirtualKeyboard_SetSymbolMode(self):		
		self.virtualKeyboardIsUpper = FALSE
		self.virtualKeyboardMode = "SYMBOL"
		if localeInfo.IsBRAZIL():
			self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_SYMBOLS_BR)
		else:	
			self.__VirtualKeyboard_SetKeys(self.VIRTUAL_KEY_SYMBOLS)
				
	def Connect(self, id, pwd, pin):

		if constInfo.SEQUENCE_PACKET_ENABLE:
			net.SetPacketSequenceMode()

		if IsLoginDelay():
			loginDelay = GetLoginDelay()
			self.connectingDialog = ConnectingDialog()
			self.connectingDialog.Open(loginDelay)
			self.connectingDialog.SAFE_SetTimeOverEvent(self.OnEndCountDown)
			self.connectingDialog.SAFE_SetExitEvent(self.OnPressExitKey)
			self.isNowCountDown = TRUE

		else:
			self.stream.popupWindow.Close()
			self.stream.popupWindow.Open(localeInfo.LOGIN_CONNETING, self.SetPasswordEditLineFocus, localeInfo.UI_CANCEL)
            
		if not constInfo.loadedShinings:
			import shinings
			shinings.LoadEffectTable()
			constInfo.loadedShinings = TRUE
		
		self.stream.SetLoginInfo(id, pwd, pin)
		self.stream.Connect()

	def __OnClickExitButton(self):
		self.stream.SetPhaseWindow(0)

	def __SetServerInfo(self, name):
		net.SetServerInfo(name.strip())
		self.serverInfo.SetText(name)
				
	def PopupDisplayMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg)

	def PopupNotifyMessage(self, msg, func=0):
		if not func:
			func=self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def __OnCloseInputDialog(self):
		if self.inputDialog:
			self.inputDialog.Close()
		self.inputDialog = None
		return TRUE

	def OnPressExitKey(self):
		self.stream.popupWindow.Close()
		self.stream.SetPhaseWindow(0)
		return TRUE

	def OnExit(self):
		self.stream.popupWindow.Close()

	def OnUpdate(self):
		ServerStateChecker.Update()

	def EmptyFunc(self):
		pass

	def __ServerBoard_OnKeyUp(self, key):
		if self.serverBoard.IsShow():
			if app.DIK_RETURN==key:
				self.__OnClickSelectServerButton()
		return TRUE

	def __GetRegionID(self):
		return 0

	def __GetServerID(self):
		return self.serverList.GetSelectedItem()

	def __GetChannelID(self):
		return self.channelList.GetSelectedItem()

	# SEVER_LIST_BUG_FIX
	def __ServerIDToServerIndex(self, regionID, targetServerID):
		try:
			regionDict = serverInfo.REGION_DICT[regionID]
		except KeyError:
			return -1

		retServerIndex = 0
		for eachServerID, regionDataDict in regionDict.items():
			if eachServerID == targetServerID:
				return retServerIndex

			retServerIndex += 1		
		
		return -1

	def __ChannelIDToChannelIndex(self, channelID):
		return channelID - 1
	# END_OF_SEVER_LIST_BUG_FIX

	def __OnSelectRegionGroup(self):
		self.__RefreshServerList()

	def __OnSelectSettlementArea(self):
		# SEVER_LIST_BUG_FIX
		regionID = self.__GetRegionID()
		serverID = self.serverListOnRegionBoard.GetSelectedItem()

		serverIndex = self.__ServerIDToServerIndex(regionID, serverID)
		self.serverList.SelectItem(serverIndex)
		# END_OF_SEVER_LIST_BUG_FIX
		
		self.__OnSelectServer()

	def __RefreshServerList(self):
		regionID = self.__GetRegionID()
		
		if not serverInfo.REGION_DICT.has_key(regionID):
			return

		self.serverList.ClearItem()

		regionDict = serverInfo.REGION_DICT[regionID]

		# SEVER_LIST_BUG_FIX
		visible_index = 1
		for id, regionDataDict in regionDict.items():
			name = regionDataDict.get("name", "noname")
			if localeInfo.IsBRAZIL() or localeInfo.IsCANADA():
				self.serverList.InsertItem(id, "%s" % (name))
			else:
				if localeInfo.IsCIBN10():			
					if name[0] == "#":
						self.serverList.InsertItem(-1, "  %s" % (name[1:]))
					else:
						self.serverList.InsertItem(id, "  %s" % (name))
						visible_index += 1
				else:
					try:
						server_id = serverInfo.SERVER_ID_DICT[id]
					except:
						server_id = visible_index

					self.serverList.InsertItem(id, "  %02d. %s" % (int(server_id), name))
					
					visible_index += 1
		
		# END_OF_SEVER_LIST_BUG_FIX

	def __OnSelectServer(self):
		self.__OnCloseInputDialog()
		self.__RequestServerStateList()
		self.__RefreshServerStateList()

	def __RequestServerStateList(self):
		regionID = self.__GetRegionID()
		serverID = self.__GetServerID()

		try:
			channelDict = serverInfo.REGION_DICT[regionID][serverID]["channel"]
		except:
			print " __RequestServerStateList - serverInfo.REGION_DICT(%d, %d)" % (regionID, serverID)
			return

		ServerStateChecker.Initialize();
		for id, channelDataDict in channelDict.items():
			key=channelDataDict["key"]
			ip=channelDataDict["ip"]
			udp_port=channelDataDict["udp_port"]
			ServerStateChecker.AddChannel(key, ip, udp_port)

		ServerStateChecker.Request()

	def __RefreshServerStateList(self):

		regionID = self.__GetRegionID()
		serverID = self.__GetServerID()
		bakChannelID = self.channelList.GetSelectedItem()

		self.channelList.ClearItem()

		try:
			channelDict = serverInfo.REGION_DICT[regionID][serverID]["channel"]
		except:
			print " __RequestServerStateList - serverInfo.REGION_DICT(%d, %d)" % (regionID, serverID)
			return

		for channelID, channelDataDict in channelDict.items():
			channelName = channelDataDict["name"]
			channelState = channelDataDict["state"]
			self.channelList.InsertItem(channelID, " %s %s" % (channelName, channelState))

		self.channelList.SelectItem(bakChannelID-1)

	def __GetChannelName(self, regionID, selServerID, selChannelID):
		try:
			return serverInfo.REGION_DICT[regionID][selServerID]["channel"][selChannelID]["name"]
		except KeyError:
			if 9==selChannelID:
				return localeInfo.CHANNEL_PVP
			else:
				return localeInfo.CHANNEL_NORMAL % (selChannelID)

	def NotifyChannelState(self, addrKey, state):
		try:
			stateName=serverInfo.STATE_DICT[state]
		except:
			stateName=serverInfo.STATE_NONE

		regionID=self.__GetRegionID()
		serverID=self.__GetServerID()
		channelID=addrKey%10

		try:
			serverInfo.REGION_DICT[regionID][serverID]["channel"][channelID]["state"] = stateName
			self.__RefreshServerStateList()

		except:
			import exception
			exception.Abort(localeInfo.CHANNEL_NOT_FIND_INFO)

	def __OnClickExitServerButton(self):
		print "exit server"
		self.__OpenLoginBoard()			

		if IsFullBackImage():
			self.GetChild("bg1").Hide()
			self.GetChild("bg2").Show()
			

	def __OnClickSelectRegionButton(self):
		regionID = self.__GetRegionID()
		serverID = self.__GetServerID()

		if (not serverInfo.REGION_DICT.has_key(regionID)):
			self.PopupNotifyMessage(localeInfo.CHANNEL_SELECT_REGION)
			return

		if (not serverInfo.REGION_DICT[regionID].has_key(serverID)):
			self.PopupNotifyMessage(localeInfo.CHANNEL_SELECT_SERVER)
			return		

		self.__SaveChannelInfo()

		self.serverExitButton.SetEvent(ui.__mem_func__(self.__OnClickExitServerButton))
		self.serverExitButton.SetText(localeInfo.UI_CLOSE)

		self.__RefreshServerList()
		self.__OpenServerBoard()

	def __OnClickSelectServerButton(self):
		if IsFullBackImage():
			self.GetChild("bg1").Hide()
			self.GetChild("bg2").Show()

		regionID = self.__GetRegionID()
		serverID = self.__GetServerID()
		channelID = self.__GetChannelID()

		if (not serverInfo.REGION_DICT.has_key(regionID)):
			self.PopupNotifyMessage(localeInfo.CHANNEL_SELECT_REGION)
			return

		if (not serverInfo.REGION_DICT[regionID].has_key(serverID)):
			self.PopupNotifyMessage(localeInfo.CHANNEL_SELECT_SERVER)
			return

		try:
			channelDict = serverInfo.REGION_DICT[regionID][serverID]["channel"]
		except KeyError:
			return

		try:
			state = channelDict[channelID]["state"]
		except KeyError:
			self.PopupNotifyMessage(localeInfo.CHANNEL_SELECT_CHANNEL)
			return

		# ���°� FULL �� ������ ���� ����
		if state == serverInfo.STATE_DICT[3]: 
			self.PopupNotifyMessage(localeInfo.CHANNEL_NOTIFY_FULL)
			return

		self.__SaveChannelInfo()

		try:
			serverName = serverInfo.REGION_DICT[regionID][serverID]["name"]
			channelName = serverInfo.REGION_DICT[regionID][serverID]["channel"][channelID]["name"]
			addrKey = serverInfo.REGION_DICT[regionID][serverID]["channel"][channelID]["key"]
			
			if "õ�� ����" == serverName:			
				app.ForceSetLocale("ymir", "locale/ymir")
			elif "�赵 ����" == serverName:			
				app.ForceSetLocale("we_korea", "locale/we_korea")				
				
		except:
			print " ERROR __OnClickSelectServerButton(%d, %d, %d)" % (regionID, serverID, channelID)
			serverName = localeInfo.CHANNEL_EMPTY_SERVER
			channelName = localeInfo.CHANNEL_NORMAL % channelID

		self.__SetServerInfo("%s, %s " % (serverName, channelName))

		try:
			ip = serverInfo.REGION_DICT[regionID][serverID]["channel"][channelID]["ip"]
			tcp_port = serverInfo.REGION_DICT[regionID][serverID]["channel"][channelID]["tcp_port"]
		except:
			import exception
			exception.Abort("LoginWindow.__OnClickSelectServerButton - ���� ���� ����")

		try:
			account_ip = serverInfo.REGION_AUTH_SERVER_DICT[regionID][serverID]["ip"]
			account_port = serverInfo.REGION_AUTH_SERVER_DICT[regionID][serverID]["port"]
		except:
			account_ip = 0
			account_port = 0

		try:
			markKey = regionID*1000 + serverID*10
			markAddrValue=serverInfo.MARKADDR_DICT[markKey]
			net.SetMarkServer(markAddrValue["ip"], markAddrValue["tcp_port"])
			app.SetGuildMarkPath(markAddrValue["mark"])
			# GUILD_SYMBOL
			app.SetGuildSymbolPath(markAddrValue["symbol_path"])
			# END_OF_GUILD_SYMBOL

		except:
			import exception
			exception.Abort("LoginWindow.__OnClickSelectServerButton - ��ũ ���� ����")


		if app.USE_OPENID and not app.OPENID_TEST :
			## 2012.07.19 OpenID : ����
			# ä�� ���� ȭ�鿡�� "Ȯ��"(SelectServerButton) �� ��������,
			# �α��� ȭ������ �Ѿ�� �ʰ� �ٷ� ������ OpenID ����Ű�� �������� ����
			self.stream.SetConnectInfo(ip, tcp_port, account_ip, account_port)
			self.Connect(0, 0)
		else :
			self.stream.SetConnectInfo(ip, tcp_port, account_ip, account_port)
			self.__OpenLoginBoard()
		

	def __OnClickSelectConnectButton(self):
		if IsFullBackImage():
			self.GetChild("bg1").Show()
			self.GetChild("bg2").Hide()
		self.__RefreshServerList()
		self.__OpenServerBoard()

	def __OnClickLoginButton(self):
		id = self.editLines["id"].GetText()
		pwd = self.editLines["pw"].GetText()
		pin = self.editLines["pin"].GetText()		

		if len(id)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_ID, self.SetIDEditLineFocus)
			return

		if len(pwd)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PASSWORD, self.SetPasswordEditLineFocus)
			return
			
		if len(pin)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PIN, self.SetPinEditLineFocus)
			return

		self.Connect(id, pwd, pin)
	
	def SameLogin_OpenUI(self):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(localeInfo.LOGIN_FAILURE_SAMELOGIN, 0, localeInfo.UI_OK)
        
	def BINARY_SetGuildBuildingList(self, obj):
		uiGuild.BUILDING_DATA_LIST = obj
        