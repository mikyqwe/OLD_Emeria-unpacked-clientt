import ui
import net
import constInfo
import chat
import dbg
import app
import background
class ChannelBoard(ui.BoardWithTitleBar):
	LastContactTimeStamp = int(app.GetTime())
	
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		
		self.SetSize(150, 210)
		self.SetCenterPosition()
		self.AddFlag("movable")
		self.AddFlag("float")
		self.SetTitleName("Change Channel")
		self.SetCloseEvent(self.__clo__)
		self.Hide()

		pos = [[30,40],[30,70],[30,100],[30,130],[30,160]]
		constInfo.lastChange = 0
		self.time = 0
		self.Buttons = {}
		for line in xrange(4):
			self.Buttons["Btn"+str(line)] = ui.Button()
			self.Buttons["Btn"+str(line)].SetParent(self)
			self.Buttons["Btn"+str(line)].SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			self.Buttons["Btn"+str(line)].SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
			self.Buttons["Btn"+str(line)].SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
			self.Buttons["Btn"+str(line)].SetText("Channel "+str(line+1))
			self.Buttons["Btn"+str(line)].SetPosition(pos[line][0],pos[line][1])
			self.Buttons["Btn"+str(line)].Show()
		self.Buttons["Btn0"].SetEvent(lambda: self.ChangeChannel(1))
		self.Buttons["Btn1"].SetEvent(lambda: self.ChangeChannel(2))
		self.Buttons["Btn2"].SetEvent(lambda: self.ChangeChannel(3))
		self.Buttons["Btn3"].SetEvent(lambda: self.ChangeChannel(4))
			
	def ChangeChannel(self, channel):
		net.SendChatPacket("/channel "+str(channel))
		net.SetServerInfo("Elendosfiles - CH" + str(channel)) 
		'''
		if str(channel) == net.GetServerInfo().split("CH")[1]:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "You are already active in this channel.")
			return
		else:
			
			constInfo.newchannel = int(channel)
			constInfo.OnChangeChannel = 1
			self.__clo__()
			net.LogOutGame()
		'''
			
	def __del__(self):
		self.Hide()
		ui.BoardWithTitleBar.__del__(self)
	def OnPressEscapeKey(self):
		self.Hide()
	def __clo__(self):
		self.Hide()
	def _Open(self):
		if self.IsShow():
			self.Hide()
		else:
			self.Show()
	
	def Destroy(self):
		self.__del__()
		return TRUE
chChanger = ChannelBoard()
chChanger.Hide()