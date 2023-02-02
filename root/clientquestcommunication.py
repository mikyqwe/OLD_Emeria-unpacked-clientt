import net
import event
import chat

class ClientQuestCommunication(object):
	def __init__(self):
		self.__chat_debug = 0
		self.__arg_seperator = ','
		self.__space_replacer = '#'
		
		self.__tmp_command = ''
		
		self.__quest_cmd = ''
		self.__quest_id = 0
		
		self.__commands = {
			'SET_QUEST_ID' : self.__SetQuestId,
			'GET_QUEST_CMD' : self.__GetQuestCmd,
		}
		
	def ClearTmpCommand(self):
		self.__tmp_command = ''
		
	def EnableChatDebug(self):
		self.__chat_debug = 1
		
	def SetArgSeperator(self, seperator):
		self.__arg_seperator = seperator
		
	def SetSpaceReplace(self, replacer):
		self.__space_replacer = replacer
		
	def AddCommand(self, cmd, event):
		self.__commands[cmd] = event
			
	def AddCommandDict(self, cmds):
		self.__commands.update(cmds)
		
	def __SetQuestId(self, quest_id):
		self.__quest_id = int(quest_id)
		
	def __GetQuestCmd(self):
		if self.__chat_debug:
			chat.AppendChat(chat.CHAT_TYPE_INFO, 'DEBUG: SEND COMMAND TO QUEST %d -> %s'%(self.__quest_id, self.__quest_cmd))
			
		net.SendQuestInputStringPacket(self.__quest_cmd)
		self.__quest_cmd = ''
		
	def SendQuestCommand(self, cmd):
		if self.__chat_debug:
			chat.AppendChat(chat.CHAT_TYPE_INFO, 'DEBUG: SEND CLICK TO QUEST %d'%self.__quest_id)
			
		self.__quest_cmd = cmd
		event.QuestButtonClick(self.__quest_id)
		
	def ReceiveQuestCommand(self, quest_command):
		if self.__chat_debug:
			chat.AppendChat(chat.CHAT_TYPE_INFO, 'DEBUG: RECEIVE COMMAND %s'%quest_command)
			
		self.__tmp_command += quest_command

		close_pos = self.__tmp_command.find(')')

		if close_pos != -1:
			open_pos = self.__tmp_command.find('(')
			
			command = self.__tmp_command[:open_pos]
			args = self.__tmp_command[open_pos+1:close_pos].replace(self.__space_replacer,' ').split(self.__arg_seperator)
			
			if self.__chat_debug:
				chat.AppendChat(chat.CHAT_TYPE_INFO, 'DEBUG: TRY TO RUN %s'%self.__tmp_command)
				
			self.__tmp_command = ''
			
			if command in self.__commands:
				if args[0]:
					self.__commands[command](*args)
				else:
					self.__commands[command]()
			else:
				if self.__chat_debug:
					chat.AppendChat(chat.CHAT_TYPE_INFO, 'DEBUG: COMMAND %s IS NOT FOUND IN COMMAND LIST'%command)
				print('ClientQuestCommunication() command %s is not found in command list'%command)
		