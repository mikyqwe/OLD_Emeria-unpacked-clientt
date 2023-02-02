######################################## AICI INCEPE TREABA ######################################## ORA: 21:36
import app, net, ui, snd, wndMgr, dbg, os
import musicInfo, systemSetting
import localeInfo, constInfo, uiScriptLocale, uicommon
import ime
import serverInfo
import serverCommandParser
import time
import ServerStateChecker
import serverlogindata
import uiCommon
from _weakref import proxy

ENABLE_BACKGROUND_ANIMATION = 1

class LoginWindow(ui.ScriptWindow):
	def __init__(self, stream):
		ui.ScriptWindow.__init__(self)
		
		net.SetPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(self)

		self.AccountManagerData	= [
								["", "", ""],
								["", "", ""],
								["", "", ""],
								["", "", ""],
							  	]

		self.stream = stream
		self.isDown = False
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
		net.ClearPhaseWindow(net.PHASE_WINDOW_LOGIN, self)
		net.SetAccountConnectorHandler(0)

	def LoadAccountData(self):
		with open('account.cfg', 'r') as content_file:
			encContent = content_file.read()
			content = app.DecryptByHWID(encContent)
			
			if ';' in content:
				accounts = content.split(';')
				for idx, account in enumerate(accounts):
					if ':#:' in account:
						data = account.split(':#:')
						self.AccountManagerData[idx][0] = data[0]
						self.AccountManagerData[idx][1] = data[1]
						self.AccountManagerData[idx][2] = data[2]
						
						#dbg.TraceError("ID: %s || PW: %s || PIN: %s" % (data[0], data[1], data[2]))
		
		
		for idx, account in enumerate(self.AccountManagerData):
			if account[0] != "":
				self.GetChild("account_text_%d" % idx).SetText(account[0])
				self.GetChild("f%d_save_button" % (int(idx)+1)).Hide()
				self.GetChild("account_text_%d" % idx).SetPackedFontColor(0xffbeaa87)
			else:
				self.GetChild("f%d_login_button" % (int(idx)+1)).Hide()
				self.GetChild("f%d_delete_button" % (int(idx)+1)).Hide()
				

	def SaveAccountData(self):
		with open('account.cfg', 'w+') as content_file:
			data = self.AccountManagerData[0][0] + ':#:' + self.AccountManagerData[0][1] + ':#:' + self.AccountManagerData[0][2] + ';'
			data += self.AccountManagerData[1][0] + ':#:' + self.AccountManagerData[1][1] + ':#:' + self.AccountManagerData[1][2] + ';'
			data += self.AccountManagerData[2][0] + ':#:' + self.AccountManagerData[2][1] + ':#:' + self.AccountManagerData[2][2] + ';'
			data += self.AccountManagerData[3][0] + ':#:' + self.AccountManagerData[3][1] + ':#:' + self.AccountManagerData[3][2] + ';'
			
			encData = app.EncryptByHWID(data)
			content_file.write(encData)

	def Open(self):
		ServerStateChecker.Create(self)
		self.__RefreshServerStateList()
		ServerStateChecker.Request()

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
			"WRONGPWD"	: localeInfo.LOGIN_FAILURE_WRONG_PASSWORD,
			"WRONGMAT"	: localeInfo.LOGIN_FAILURE_WRONG_MATRIX_CARD_NUMBER,
			"QUIT"		: app.Exit,
		}
		
		self.LANG_BUTTON_MAX = 11
		self.langDict = {
			0 : {"ask_text" : "Do you want to change the Language to Czech?", "localestring" : "10002 1250 cz"},
			1 : {"ask_text" : "Do you want to change the Language to Deutsch?", "localestring" : "10002 1252 de"},
			2 : {"ask_text" : "Do you want to change the Language to English?", "localestring" : "10002 1252 en"},
			3 : {"ask_text" : "Do you want to change the Language to Espana?", "localestring" : "10002 1252 es"},
			4 : {"ask_text" : "Do you want to change the Language to Francais?", "localestring" : "10002 1253 gr"},
			5 : {"ask_text" : "Do you want to change the Language to Hungary?", "localestring" : "10002 1250 hu"},
			6 : {"ask_text" : "Do you want to change the Language to Italian?", "localestring" : "10002 1252 it"},
			7 : {"ask_text" : "Do you want to change the Language to Poland?", "localestring" : "10002 1250 pl"},
			8 : {"ask_text" : "Do you want to change the Language to Portuguese?", "localestring" : "10002 1252 pt"},
			9 : {"ask_text" : "Do you want to change the Language to Romanian?", "localestring" : "10002 1250 ro"},
			10 : {"ask_text" : "Do you want to change the Language to Turk?", "localestring" : "10002 1254 tr"},
		}
		
		
		self.SetSize(wndMgr.GetScreenWidth(), wndMgr.GetScreenHeight())
		self.SetWindowName("LoginWindow")
		self.__BuildKeyDict()

		self.__LoadScript("UIScript/loginwindow.py")
		# if not self.__LoadScript(uiScriptLocale.LOCALE_UISCRIPT_PATH + "LoginWindow.py"):
			# dbg.TraceError("LoginWindow.Open - __LoadScript Error")
			# return
		
		if musicInfo.loginMusic != "":
			snd.SetMusicVolume(systemSetting.GetMusicVolume())
			snd.FadeInMusic("BGM/" + musicInfo.loginMusic)

		snd.SetSoundVolume(systemSetting.GetSoundVolume())

		ime.AddExceptKey(91)
		ime.AddExceptKey(93)
		self.SetChannel(0)

		if not os.path.exists('account.cfg'):
			self.SaveAccountData()
		
		self.LoadAccountData()
		
		self.Show()
		app.ShowCursor()	

	def Close(self):
		self.serverList					= None
		self.channelList				= None
		self.onPressKeyDict 			= None

		self.AccountManagerData	= None

		if musicInfo.loginMusic != "" and musicInfo.selectMusic != "":
			snd.FadeOutMusic("BGM/"+musicInfo.loginMusic)
	
		if self.stream.popupWindow:
			self.stream.popupWindow.Close()
	
		self.Hide()
		app.HideCursor()
		ime.ClearExceptKey()

	def __BuildKeyDict(self):
		onPressKeyDict = {}

		onPressKeyDict[app.DIK_F1]	= lambda : self.loginWithHotkey(1)
		onPressKeyDict[app.DIK_F2]	= lambda : self.loginWithHotkey(2)
		onPressKeyDict[app.DIK_F3]	= lambda : self.loginWithHotkey(3)
		onPressKeyDict[app.DIK_F4]	= lambda : self.loginWithHotkey(4)

		self.onPressKeyDict = onPressKeyDict

	def OnKeyDown(self, key):
		try:
			self.onPressKeyDict[key]()
		except KeyError:
			pass
		except:
			raise

		return TRUE

	def OnConnectFailure(self):
		snd.PlaySound("sound/ui/loginfail.wav")
		self.PopupNotifyMessage(localeInfo.LOGIN_CONNECT_FAILURE, self.EmptyFunc)

	def OnHandShake(self):
		if constInfo.LOADED_RESOURCES == 0:
			net.LoadResourcesInCache()
			constInfo.LOADED_RESOURCES = 1
		snd.PlaySound("sound/ui/loginok.wav")
		self.PopupDisplayMessage(localeInfo.LOGIN_CONNECT_SUCCESS)

	def OnLoginStart(self):
		self.PopupDisplayMessage(localeInfo.LOGIN_PROCESSING)
		if constInfo.LOADED_RESOURCES == 0:
			net.LoadResourcesInCache()
			constInfo.LOADED_RESOURCES = 1

	def OnLoginFailure(self, error):
		ServerStateChecker.Request()
		try:
			loginFailureMsg = self.loginFailureMsgDict[error]
		except KeyError:
		
			loginFailureMsg = localeInfo.LOGIN_FAILURE_UNKNOWN  + error

		loginFailureFunc = self.loginFailureFuncDict.get(error, self.EmptyFunc)

		self.PopupNotifyMessage(loginFailureMsg, loginFailureFunc)

		snd.PlaySound("sound/ui/loginfail.wav")

	def __LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.LoadObject")

		try:
			self.idEditLine			= self.GetChild("id")
			self.pwdEditLine		= self.GetChild("pwd")
			self.pinEditLine		= self.GetChild("pin")

			self.loginButton		= self.GetChild("login_button")
			self.exitButton			= self.GetChild("exit_button")

			for i in xrange(0, self.LANG_BUTTON_MAX):
				self.GetChild("lang_button_%d" % i).SetEvent(ui.__mem_func__(self.AskLanguage), i)
			
			self.channelButton = {
				0 : self.GetChild("select_btn_ch1"),
				1 : self.GetChild("select_btn_ch2"),
				2 : self.GetChild("select_btn_ch3"),
				3 : self.GetChild("select_btn_ch4")
			}

		except:
			import exception
			exception.Abort("LoginWindow.__LoadScript.BindObject")
			
				
		for (channelID, channelButtons) in self.channelButton.items():
				channelButtons.SetEvent(ui.__mem_func__(self.SetChannel), channelID)
		
		self.loginButton.SetEvent(ui.__mem_func__(self.__OnClickLoginButton))
		self.exitButton.SetEvent(ui.__mem_func__(self.OnPressExitKey))

		self.GetChild("forgot_pw_button").SetEvent(ui.__mem_func__(self.GoForgotPassword))
		self.GetChild("sign_in_button").SetEvent(ui.__mem_func__(self.GoRegister))
		
		self.idEditLine.SetTabEvent(lambda arg = 2 : self.OnSetFocus(arg))
		self.pwdEditLine.SetTabEvent(lambda arg = 3 : self.OnSetFocus(arg))
		self.pinEditLine.SetTabEvent(lambda arg = 1 : self.OnSetFocus(arg))
		self.idEditLine.SetSelectEvent(lambda arg = 1 : self.OnSetFocus(arg))
		self.pwdEditLine.SetSelectEvent(lambda arg = 2 : self.OnSetFocus(arg))
		self.pinEditLine.SetSelectEvent(lambda arg = 3 : self.OnSetFocus(arg))
		self.idEditLine.SetReturnEvent(lambda arg = 2 : self.OnSetFocus(arg))
		self.pwdEditLine.SetReturnEvent(lambda arg = 3 : self.OnSetFocus(arg))
		self.pinEditLine.SetReturnEvent(ui.__mem_func__(self.__OnClickLoginButton))
		
		self.GetChild("id_focus_background").Hide()
		self.GetChild("pw_focus_background").Hide()
		self.GetChild("pin_focus_background").Hide()
		self.OnSetFocus(1)
		

		#self.saveButton.SetEvent(ui.__mem_func__(self.__OnClickAccountSave))

		self.GetChild("f1_save_button").SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountSave)(0))
		self.GetChild("f2_save_button").SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountSave)(1))
		self.GetChild("f3_save_button").SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountSave)(2))
		self.GetChild("f4_save_button").SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountSave)(3))
		
		self.GetChild("f1_login_button").SetEvent(lambda:ui.__mem_func__(self.loginWithHotkey)(1))
		self.GetChild("f2_login_button").SetEvent(lambda:ui.__mem_func__(self.loginWithHotkey)(2))
		self.GetChild("f3_login_button").SetEvent(lambda:ui.__mem_func__(self.loginWithHotkey)(3))
		self.GetChild("f4_login_button").SetEvent(lambda:ui.__mem_func__(self.loginWithHotkey)(4))
		
		self.GetChild("f1_delete_button").SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountErase)(0))
		self.GetChild("f2_delete_button").SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountErase)(1))
		self.GetChild("f3_delete_button").SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountErase)(2))
		self.GetChild("f4_delete_button").SetEvent(lambda:ui.__mem_func__(self.__OnClickAccountErase)(3))

		self.GetChild("ch1_online").Hide()
		self.GetChild("ch2_online").Hide()
		self.GetChild("ch3_online").Hide()
		self.GetChild("ch4_online").Hide()
		
		self.GetChild("animation_button").SetEvent(ui.__mem_func__(self.OnClickAnimationButton))
		
		#for i in range(len(self.AccountManager)):
			#self.AccountManager[i][1].Hide()
		
		lang = "2"
		try:
			file = open("lang.cfg", "r")
			lang = file.readlines()[0]
			file.close()
		except:
			file = open("lang.cfg", "w")
			file.write("2")
			file.close()

		constInfo.SEL_LANG = int(lang)
		
		ani = "1"
		try:
			file = open("intro.cfg", "r")
			ani = file.readlines()[0]
			file.close()
		except:
			file = open("intro.cfg", "w")
			file.write("1")
			file.close()
			
		constInfo.ENABLE_INTRO_ANIMATION = int(ani)
	
		if constInfo.ENABLE_INTRO_ANIMATION == 1:
			self.GetChild("animation_button").SetText("Hide Animation")
			self.CreateAnimateBackground()
			
	def CreateAnimateBackground(self):
		self.AnimationImage = ui.AniImageBox()
		self.AnimationImage.SetParent(self.GetChild("video_layer"))
		self.AnimationImage.SetDelay(2)
		for x in xrange(131):
			self.AnimationImage.AppendImageScale("d:/ymir work/ui/intro/animation/login/frame_%d.sub" % (x), float(wndMgr.GetScreenWidth()) / 1920.0, float(wndMgr.GetScreenHeight()) / 1080.0)
			self.AnimationImage.Show()
			
	def OnSetFocus(self, arg):
		self.GetChild("id_focus_background").Hide()
		self.GetChild("pw_focus_background").Hide()
		self.GetChild("pin_focus_background").Hide()
		if arg == 1:
			self.pinEditLine.KillFocus()
			self.idEditLine.SetFocus()
			self.GetChild("id_focus_background").Show()
		if arg == 2:
			self.idEditLine.KillFocus()
			self.pwdEditLine.SetFocus()
			self.GetChild("pw_focus_background").Show()
		if arg == 3:
			self.pwdEditLine.KillFocus()
			self.pinEditLine.SetFocus()
			self.GetChild("pin_focus_background").Show()
	
	def OnUpdate(self):
		ServerStateChecker.Update()
		
	def SetChannel(self, ch):
		for key, button in self.channelButton.items():
			button.SetUp()

		serverIP = serverlogindata.SRV1["host"]
			
		self.channelButton[ch].Down()
		self.stream.SetConnectInfo(serverIP, self.ChannelPort(ch, 0), serverIP, self.ChannelPort("LOGIN"))

		net.SetMarkServer(serverIP, self.ChannelPort("LOGO"))
		app.SetGuildMarkPath("10.tga")
		app.SetGuildSymbolPath("10")
		net.SetServerInfo(self.ChannelPort(ch, 2))
		
	def ChannelPort(self, ch, value=0):
		channel = {
			0	:	serverlogindata.SRV_LIST[0][0][3][0][2],
			1	:	serverlogindata.SRV_LIST[0][0][3][1][2],
			2	:	serverlogindata.SRV_LIST[0][0][3][2][2],
			3	:	serverlogindata.SRV_LIST[0][0][3][3][2],
		}
		
		if ch == "LOGIN":
			return serverlogindata.SRV_LIST[0][0][1]
		elif ch == "LOGO":
			return channel[0]
		elif value == 2:
			return serverlogindata.SRV_LIST[0][0][0] + ", CH%s" % (ch+1)
		else:
			return channel[ch]


	def Connect(self, id, pwd, pin):
		if constInfo.SEQUENCE_PACKET_ENABLE:
			net.SetPacketSequenceMode()
			
		constInfo.LastAccount = id.lower()

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(localeInfo.LOGIN_CONNETING, self.EmptyFunc, localeInfo.UI_CANCEL)

		self.stream.SetLoginInfo(id, pwd, pin)
		self.stream.Connect()
		
	def PopupDisplayMessage(self, msg):
		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg)

	def PopupNotifyMessage(self, msg, func=0):
		if not func:
			func = self.EmptyFunc

		self.stream.popupWindow.Close()
		self.stream.popupWindow.Open(msg, func, localeInfo.UI_OK)

	def OnPressExitKey(self):
		if self.stream.popupWindow:
			self.stream.popupWindow.Close()
		self.stream.SetPhaseWindow(0)
		return TRUE

	def __GetRegionID(self):
		return 0

	def __GetServerID(self):
		return 0

	def __GetChannelID(self):
		return self.channelList.GetSelectedItem()

## SERVER STATE CHECKER

	def NotifyChannelState(self, key, state):
		serverlogindata.SERVER_STATE_TABLE[key] = state
		
		serverIndex = self.__GetServerID()
		if (key / 10) == serverIndex:
			try:
				stateName = serverlogindata.STATE_DICT[state]
				stateNameText = serverlogindata.STATE_DICT[state]
			except:
				stateName = serverlogindata.STATE_NONE
				stateNameText = serverlogindata.STATE_TEXT_NONE

			channelIndex = key % 10
			channelName = serverlogindata.SRV_LIST[0][serverIndex][3][channelIndex][0]

			if state >= 1:
				self.GetChild("ch%d_online" % (int(channelIndex)+1)).Show()
				self.GetChild("ch%d_offline" % (int(channelIndex)+1)).Hide()
			else:
				self.GetChild("ch%d_online" % (int(channelIndex)+1)).Hide()
				self.GetChild("ch%d_offline" % (int(channelIndex)+1)).Show()

	def __RequestServerStateList(self):
		serverIndex = self.__GetServerID()
		channelData = None

		try:
			channelData = serverlogindata.SRV_LIST[0][serverIndex][3]
		except:
			print "LoginWindow::__RequestServerStateList"
			return

		ServerStateChecker.Request()

	def __RefreshServerStateList(self):
		serverIndex = self.__GetServerID()
		channelData = None

		try:
			channelData = serverlogindata.SRV_LIST[0][0][3]
		except:
			print "LoginWindow::__RefreshServerStateList"
			return
			
		for index, channel in enumerate(channelData):
			ServerStateChecker.AddChannel(index, channel[1], channel[2])
			stateName = serverlogindata.STATE_NONE

			print "LoginWindow::__RefreshServerStateList(): key %d, channelName %s, stateName %s" % (index + 1, channel[0], stateName)

## ACCSAVE System ##
	def __OnClickAccountSave(self, idx):
		if self.AccountManagerData[idx][0] == "":
			id = self.idEditLine.GetText()
			pwd = self.pwdEditLine.GetText()
			pin = self.pinEditLine.GetText()
			
			if id == "" or pwd == "" or pin == "":
				return

			self.AccountManagerData[idx][0] = id
			self.AccountManagerData[idx][1] = pwd
			self.AccountManagerData[idx][2] = pin
			self.SaveAccountData()
			self.GetChild("account_text_%d" % idx).SetText(id)
			self.GetChild("f%d_save_button" % (int(idx)+1)).Hide()
			self.GetChild("f%d_login_button" % (int(idx)+1)).Show()
			self.GetChild("f%d_delete_button" % (int(idx)+1)).Show()
			self.GetChild("account_text_%d" % idx).SetPackedFontColor(0xffbeaa87)
			#self.AccountManager[i][0].SetFontColor(201.0 / 255.0, 104.0 / 255.0, 32.0 / 255.0)

	def __OnClickAccountErase(self, idx):
		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.SetText("Do you want to delete the entry?") #translateme
		self.questionDialog.SetAcceptEvent(lambda arg=idx: self.OnDelAccAcceptEvent(arg))
		self.questionDialog.SetCancelEvent(ui.__mem_func__(self.OnDelAccQuestionCancel))
		self.questionDialog.Open()
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(1)
		
	def OnDelAccAcceptEvent(self, idx):
		self.OnCloseQuestionDialog()
		self.AccountManagerData[idx][0] = ""
		self.AccountManagerData[idx][1] = ""
		self.AccountManagerData[idx][2] = ""
		
		self.GetChild("account_text_%d" % idx).SetText("Free Slot")
		self.GetChild("f%d_save_button" % (int(idx)+1)).Show()
		self.GetChild("f%d_login_button" % (int(idx)+1)).Hide()
		self.GetChild("f%d_delete_button" % (int(idx)+1)).Hide()
		self.GetChild("account_text_%d" % idx).SetPackedFontColor(0xff727272)
		#self.GetChild("account_text_%d" % i).SetFontColor(121.0, 0.0,0.0)
		#self.GetChild("account_text_%d" % i).Hide()
		self.SaveAccountData()
		
	def OnDelAccQuestionCancel(self):
		self.OnCloseQuestionDialog()
		
	def OnCloseQuestionDialog(self):
		if not self.questionDialog:
			return
		
		self.questionDialog.Close()
		self.questionDialog = None
		constInfo.SET_ITEM_QUESTION_DIALOG_STATUS(0)
#####################

## BUTTONS ##

	def GoForgotPassword(self):
		import os
		os.system('@echo off && explorer "https://elendos.shop/password/recover"')
		return TRUE

	def GoRegister(self):
		import os
		os.system('@echo off && explorer "https://elendos.shop/register"')
		return TRUE

	def OnClickAnimationButton(self):
		if constInfo.ENABLE_INTRO_ANIMATION == 0:
			file = open("intro.cfg", "w")
			file.write("1")
			file.close()
		if constInfo.ENABLE_INTRO_ANIMATION == 1:
			file = open("intro.cfg", "w")
			file.write("0")
			file.close()
		os.system('start Elendos.exe')
		app.Exit()

############################

## Change Language

	def AskLanguage(self, lang_id):
		self.question = uicommon.QuestionDialog()
		self.question.SetText(self.langDict[lang_id]["ask_text"])
		self.question.SetAcceptEvent(lambda lang_id=lang_id, flag=True: self.AnswerLanguage(lang_id, flag))
		self.question.SetCancelEvent(lambda lang_id=lang_id, flag=False: self.AnswerLanguage(lang_id, flag))
		self.question.Open()
	
	def AnswerLanguage(self, lang_id, flag):
		if flag:
			self.popup = uicommon.PopupDialog()
			self.popup.SetText("Restart the Elendosfiles client!")
			self.popup.SetAcceptEvent(lambda lang_id=lang_id: self.SetLanguage(lang_id))
			self.popup.Open()

		self.question.Close()

	def SetLanguage(self, lang_id):
		file = open("locale.cfg", "w")
 		file.write(self.langDict[lang_id]["localestring"]) 
		file.close()
		file = open("lang.cfg", "w")
		file.write(str(lang_id))
		file.close()
		os.system('start Elendos.exe')
		app.Exit()

############################

	def EmptyFunc(self):
		pass

	def __OnClickLoginButton(self):
		id = self.idEditLine.GetText()
		pwd = self.pwdEditLine.GetText()
		pin = self.pinEditLine.GetText()

		if len(id)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_ID, self.EmptyFunc)
			return

		if len(pwd)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PASSWORD, self.EmptyFunc)
			return

		if len(pin)==0:
			self.PopupNotifyMessage(localeInfo.LOGIN_INPUT_PIN, self.EmptyFunc)
			return
	
		self.Connect(id, pwd, pin)

	def loginWithHotkey(self, arg):
		self.Connect(self.AccountManagerData[arg-1][0], self.AccountManagerData[arg-1][1], self.AccountManagerData[arg-1][2])
