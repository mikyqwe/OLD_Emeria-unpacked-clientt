import ui
import time
import constInfo
import chat
import uiToolTip
import item
import event
import net
import locale
import re
import wndMgr
import time

##
## Error Message Id's in use:
## 101f 
## 102f
## 102f
##

##
## TODO
##
ACHIEVEMENTSYSTEM_PATH = "locale/de/ui/achievementsystem/"

class Achievementsystem(ui.ScriptWindow):

	achievements = {}

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE
		if FALSE == self.isLoaded:
			self.__LoadScript()
		
	def __LoadScript(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, 'uiscript/achievementsystem.py')
		except:
			import exception
			exception.Abort('Achievementsystem.__LoadScript.LoadScriptFile')

		try:
			self.__LoadVariables()
		except:
			import exception
			exception.Abort('Achievementsystem.__LoadScript.LoadVariables')

		try:
			self.__LoadUi()
		except:
			import exception
			exception.Abort('Achievementsystem.__LoadScript.LoadUi')

		try:
			self.__LoadEvents()
		except:
			import exception
			exception.Abort('Achievementsystem.__LoadScript.LoadEvents')
		
		self.isLoaded = TRUE

	def __LoadVariables(self):
		self.ClearAchievements()
		self.SetDefaultPageVar()
		self.loadingBar = LoadingBar()
		self.achievementDialog = AchievementDialog()
		self.quest_cmd = ''
		self.qid = 0
		self.recent_task_done_tool_tip = uiToolTip.ToolTip(220)
		self.recent_task_done_tool_tip.Hide()

	def SetDefaultPageVar(self):
		self.page = {
				'current_page' : 0,
				'current_tab' : 0,

				'tasks' : { 
					'current_pos' : 0,
					'current_state' : 'all',
					# 'sort' : {
						# 'type' : {
							# 'text' : 1,
							# 'achievement_points' : 0
						# },
						# 'reverse' : 0
					# }
				},
				'overview' : {
					'categorys_progress' : {
							'current_tab': 0,
						},
					'recent_tasks_done' : {
							'current_tab': 0,
						},
				},
			}
			
	
	def ClearAchievements(self):
		self.achievements = {
			'categorys' : [
				{
					'title': "Übersicht",
					'statistic': {
						'current_achievement_points' : 0,
						'data' : [
							{
								'text' : 'gesamte Achievementpunkte',
								'value' : 0,
							},
							{
								'text' : 'erledigte Achievements',
								'value' : 0,
							},
							{
								'text' : 'ausstehende Achievements',
								'value' : 0,
							},
						],

					},
					'recent_tasks_done': [],
				},
			],
		}
		
	def __LoadUi(self):
		self.elements = {
			'titlebar' : self.GetChild("titlebar"),
			'pages' : {
				'overview_page' : self.GetChild('overview_page'),
				'tasks_page' : self.GetChild('tasks_page'),
			},
			'header': {
				'main_progressbar' : {
					'progressbar_full' : self.GetChild('eimg_main_progressbar_full'),
					'progressbar_completed' : self.GetChild('img_main_progressbar_completed'),
				},
				'category' : {
					'buttons' : [
						self.GetChild('btn_category_menue_content_0'),
						self.GetChild('btn_category_menue_content_1'),
						self.GetChild('btn_category_menue_content_2'),
						self.GetChild('btn_category_menue_content_3'),
						self.GetChild('btn_category_menue_content_4'),
						self.GetChild('btn_category_menue_content_5'),
					],
				},
				'navigation' : {
					'buttons' : {
						'arrow_left' : self.GetChild('btn_arrow_left'),
						'arrow_right' : self.GetChild('btn_arrow_right'),
					},
				},
			},
			
			'overview_page': {
				'recent_tasks_done' : {
					'buttons' : {
						'arrow_up' : self.GetChild('btn_arrow_up'),
						'arrow_down' : self.GetChild('btn_arrow_down'),
					},
					'content' : [
						self.GetChild('recent_tasks_done_content_0'),
						self.GetChild('recent_tasks_done_content_1'),
						self.GetChild('recent_tasks_done_content_2'),
						self.GetChild('recent_tasks_done_content_3'),
						self.GetChild('recent_tasks_done_content_4'),
						self.GetChild('recent_tasks_done_content_5'),
					],
					'title' : [
						self.GetChild('txt_recent_tasks_done_content_task_title_0'),
						self.GetChild('txt_recent_tasks_done_content_task_title_1'),
						self.GetChild('txt_recent_tasks_done_content_task_title_2'),
						self.GetChild('txt_recent_tasks_done_content_task_title_3'),
						self.GetChild('txt_recent_tasks_done_content_task_title_4'),
						self.GetChild('txt_recent_tasks_done_content_task_title_5'),
					],
					'value' : [
						self.GetChild('txt_recent_tasks_done_content_task_value_0'),
						self.GetChild('txt_recent_tasks_done_content_task_value_1'),
						self.GetChild('txt_recent_tasks_done_content_task_value_2'),
						self.GetChild('txt_recent_tasks_done_content_task_value_3'),
						self.GetChild('txt_recent_tasks_done_content_task_value_4'),
						self.GetChild('txt_recent_tasks_done_content_task_value_5'),
					],
					'image' : [
						self.GetChild('img_recent_tasks_done_title_0'),
						self.GetChild('img_recent_tasks_done_title_1'),
						self.GetChild('img_recent_tasks_done_title_2'),
						self.GetChild('img_recent_tasks_done_title_3'),
						self.GetChild('img_recent_tasks_done_title_4'),
						self.GetChild('img_recent_tasks_done_title_5'),
					],
				},
				'categorys_progress' : {
					'buttons' : {
						'arrow_up' : self.GetChild('btn_categorys_arrow_up'),
						'arrow_down' : self.GetChild('btn_categorys_arrow_down'),
					},
					'content' : [
						self.GetChild('categorys_progress_content_0'),
						self.GetChild('categorys_progress_content_1'),
						self.GetChild('categorys_progress_content_2'),
						self.GetChild('categorys_progress_content_3'),
						self.GetChild('categorys_progress_content_4'),
					],
					'title' : [
						self.GetChild('txt_categorys_progress_content_title_0'),
						self.GetChild('txt_categorys_progress_content_title_1'),
						self.GetChild('txt_categorys_progress_content_title_2'),
						self.GetChild('txt_categorys_progress_content_title_3'),
						self.GetChild('txt_categorys_progress_content_title_4'),
					],
					'progressbar_full' : [
						self.GetChild('eimg_categorys_progress_content_progressbar_full_0'),
						self.GetChild('eimg_categorys_progress_content_progressbar_full_1'),
						self.GetChild('eimg_categorys_progress_content_progressbar_full_2'),
						self.GetChild('eimg_categorys_progress_content_progressbar_full_3'),
						self.GetChild('eimg_categorys_progress_content_progressbar_full_4'),
					],
					'progressbar_completed' : [
						self.GetChild('img_categorys_progress_content_progressbar_full_completed_0'),
						self.GetChild('img_categorys_progress_content_progressbar_full_completed_1'),
						self.GetChild('img_categorys_progress_content_progressbar_full_completed_2'),
						self.GetChild('img_categorys_progress_content_progressbar_full_completed_3'),
						self.GetChild('img_categorys_progress_content_progressbar_full_completed_4'),
					],
				},
				'statistic' : {
					'title': [
						self.GetChild('txt_statistic_content_title_0'),
						self.GetChild('txt_statistic_content_title_1'),
						self.GetChild('txt_statistic_content_title_2'),
					],
					'value': [
						self.GetChild('txt_statistic_content_value_0'),
						self.GetChild('txt_statistic_content_value_1'),
						self.GetChild('txt_statistic_content_value_2'),
					],
				},
				'achievement_points' : {
					'value': self.GetChild('txt_statistic_content_achievementpoints_value'),
				},
			},
			'tasks_page': {
				'buttons' : {
						'state_all' : self.GetChild('btn_tasks_page_change_state_all'),
						'state_pending' : self.GetChild('btn_tasks_page_change_state_pending'),
						'state_done' : self.GetChild('btn_tasks_page_change_state_done'),
						# 'sort': {
							# 'text' : self.GetChild('btn_tasks_page_change_sort_type_text'),
							# 'achievement_points' : self.GetChild('btn_tasks_page_change_sort_type_achievement_points'),
							# 'order' : {
								# 'ascending' : self.GetChild('btn_tasks_page_change_sort_order_ascending'),
								# 'descending' : self.GetChild('btn_tasks_page_change_sort_order_descending'),
							# },
						# },
				},
				'scrollbar' : self.GetChild('scrollbar_tasks_page_content'), 
				'tasks' : {
					'content' : [
						self.GetChild('tasks_page_content_0'),
						self.GetChild('tasks_page_content_1'),
						self.GetChild('tasks_page_content_2'),
						self.GetChild('tasks_page_content_3'),
						self.GetChild('tasks_page_content_4'),
						self.GetChild('tasks_page_content_5'),
						self.GetChild('tasks_page_content_6'),
						self.GetChild('tasks_page_content_7'),
					],
					'title' : [
						self.GetChild('txt_tasks_page_content_progressbar_title_0'),
						self.GetChild('txt_tasks_page_content_progressbar_title_1'),
						self.GetChild('txt_tasks_page_content_progressbar_title_2'),
						self.GetChild('txt_tasks_page_content_progressbar_title_3'),
						self.GetChild('txt_tasks_page_content_progressbar_title_4'),
						self.GetChild('txt_tasks_page_content_progressbar_title_5'),
						self.GetChild('txt_tasks_page_content_progressbar_title_6'),
						self.GetChild('txt_tasks_page_content_progressbar_title_7'),
					],
					'value' : [
						self.GetChild('txt_tasks_page_content_progressbar_flag_value_0'),
						self.GetChild('txt_tasks_page_content_progressbar_flag_value_1'),
						self.GetChild('txt_tasks_page_content_progressbar_flag_value_2'),
						self.GetChild('txt_tasks_page_content_progressbar_flag_value_3'),
						self.GetChild('txt_tasks_page_content_progressbar_flag_value_4'),
						self.GetChild('txt_tasks_page_content_progressbar_flag_value_5'),
						self.GetChild('txt_tasks_page_content_progressbar_flag_value_6'),
						self.GetChild('txt_tasks_page_content_progressbar_flag_value_7'),
					],
					'progressbar_full' : [
						self.GetChild('eimg_tasks_page_content_progressbar_full_0'),
						self.GetChild('eimg_tasks_page_content_progressbar_full_1'),
						self.GetChild('eimg_tasks_page_content_progressbar_full_2'),
						self.GetChild('eimg_tasks_page_content_progressbar_full_3'),
						self.GetChild('eimg_tasks_page_content_progressbar_full_4'),
						self.GetChild('eimg_tasks_page_content_progressbar_full_5'),
						self.GetChild('eimg_tasks_page_content_progressbar_full_6'),
						self.GetChild('eimg_tasks_page_content_progressbar_full_7'),
					],
					'progressbar_completed' : [
						self.GetChild('img_tasks_page_content_progressbar_full_completed_0'),
						self.GetChild('img_tasks_page_content_progressbar_full_completed_1'),
						self.GetChild('img_tasks_page_content_progressbar_full_completed_2'),
						self.GetChild('img_tasks_page_content_progressbar_full_completed_3'),
						self.GetChild('img_tasks_page_content_progressbar_full_completed_4'),
						self.GetChild('img_tasks_page_content_progressbar_full_completed_5'),
						self.GetChild('img_tasks_page_content_progressbar_full_completed_6'),
						self.GetChild('img_tasks_page_content_progressbar_full_completed_7'),
					],
				},
			},
		}

	def __LoadEvents(self):
		self.elements['titlebar'].SetCloseEvent(ui.__mem_func__(self.Close))

		self.elements['header']['navigation']['buttons']['arrow_left'].SetEvent(self.ChangeCategoryTab, 'left')
		self.elements['header']['navigation']['buttons']['arrow_right'].SetEvent(self.ChangeCategoryTab, 'right')

		self.elements['overview_page']['categorys_progress']['buttons']['arrow_up'].SetEvent(self.ChangeCategorysProgressTab, 'up')
		self.elements['overview_page']['categorys_progress']['buttons']['arrow_down'].SetEvent(self.ChangeCategorysProgressTab, 'down')

		self.elements['overview_page']['recent_tasks_done']['buttons']['arrow_up'].SetEvent(self.ChangeRecentTasksDoneTab, 'up')
		self.elements['overview_page']['recent_tasks_done']['buttons']['arrow_down'].SetEvent(self.ChangeRecentTasksDoneTab, 'down')
		
		for i in xrange(len(self.elements['overview_page']['recent_tasks_done']['image'])):
			self.elements['overview_page']['recent_tasks_done']['image'][i].OnMouseOverIn = lambda arg = self, index = i: arg.OnMouseOverInRecentTasksDone(index)
			self.elements['overview_page']['recent_tasks_done']['image'][i].OnMouseOverOut  = lambda arg = self, index = i: arg.OnMouseOverOutRecentTasksDone(index)
			
		
		category_buttons = self.elements['header']['category']['buttons']
		for id in range(len(category_buttons)):
			category_buttons[id].SetEvent(self.ChangeCategoryPage, id)

		self.elements['tasks_page']['scrollbar'].SetScrollEvent(self.ScrollTasksPage)

		self.elements['tasks_page']['buttons']['state_all'].SetEvent(self.ChangeTasksState, 'all')
		self.elements['tasks_page']['buttons']['state_pending'].SetEvent(self.ChangeTasksState, 'pending')
		self.elements['tasks_page']['buttons']['state_done'].SetEvent(self.ChangeTasksState, 'done')
		
		# self.elements['tasks_page']['buttons']['sort']['text'].SetEvent(self.ChangeTasksSortType, 'text')
		# self.elements['tasks_page']['buttons']['sort']['achievement_points'].SetEvent(self.ChangeTasksSortType, 'achievement_points')
		# self.elements['tasks_page']['buttons']['sort']['order']['ascending'].SetEvent(self.ChangeTasksSortOrder, 'ascending')
		# self.elements['tasks_page']['buttons']['sort']['order']['descending'].SetEvent(self.ChangeTasksSortOrder, 'descending')

	## PROGRESSBAR FUNCTIONS START ##

	def SetPercentProgressbarMain(self, cur, max):
		if cur >= max:
			self.elements['header']['main_progressbar']['progressbar_full'].Hide()
			self.elements['header']['main_progressbar']['progressbar_completed'].Show()
		else:
			self.elements['header']['main_progressbar']['progressbar_completed'].Hide()
			self.elements['header']['main_progressbar']['progressbar_full'].SetPercentage(float(cur), float(max))
			self.elements['header']['main_progressbar']['progressbar_full'].Show()
			

	## PROGRESSBAR FUNCTIONS END ##

	## PAGES FUNCTIONS START ##

	def ShowOverviewPage(self):
		self.elements['pages']['tasks_page'].Hide()
		self.elements['pages']['overview_page'].Show()

	def ShowTasksPage(self):
		self.elements['pages']['overview_page'].Hide()
		self.elements['pages']['tasks_page'].Show()

	## PAGES FUNCTIONS END ##

	## CATEGORY FUNCTIONS START ##

	def SetTitleCategory(self, id, title):
		self.elements['header']['category']['buttons'][id].SetText(title)

	def ShowCategory(self, id):
		self.elements['header']['category']['buttons'][id].Show()

	def HideCategory(self, id):
		self.elements['header']['category']['buttons'][id].Hide()

	def HideAllCategorys(self):
		buttons = self.elements['header']['category']['buttons']
		for button in buttons:
			button.Hide()

	def SetAllCategorysUp(self):
		for button in self.elements['header']['category']['buttons']:
			button.SetUp()

	def SetCategoryDown(self, id):
		self.SetAllCategorysUp()
		self.elements['header']['category']['buttons'][id].Down()

	def ShowArrowLeftCategory(self):
		self.elements['header']['navigation']['buttons']['arrow_left'].Show()

	def HideArrowLeftCategory(self):
		self.elements['header']['navigation']['buttons']['arrow_left'].Hide()

	def ShowArrowRightCategory(self):
		self.elements['header']['navigation']['buttons']['arrow_right'].Show()

	def HideArrowRightCategory(self):
		self.elements['header']['navigation']['buttons']['arrow_right'].Hide()

	## CATEGORY FUNCTIONS END ##

	## RECENT_TASKS_DONE FUNCTIONS START ##
	def ShowRecentTaskDone(self, id):
		self.elements['overview_page']['recent_tasks_done']['content'][id].Show()

	def HideAllRecentTasksDone(self):
		contents = self.elements['overview_page']['recent_tasks_done']['content']
		for content in contents:
			content.Hide()

	def HideRecentTaskDone(self, id):
		self.elements['overview_page']['recent_tasks_done']['content'][id].Hide()

	def SetTitleRecentTaskDone(self, id, title):
		self.elements['overview_page']['recent_tasks_done']['title'][id].SetText(title[:10]+'...')
		# self.elements['overview_page']['recent_tasks_done']['image'][id].SetToolTipText(title)

	def SetValueRecentTaskDone(self, id, value):
		self.elements['overview_page']['recent_tasks_done']['value'][id].SetText('+%d' % value)

	def ShowArrowUpRecentTasksDone(self):
		self.elements['overview_page']['recent_tasks_done']['buttons']['arrow_up'].Show()

	def HideArrowUpRecentTasksDone(self):
		self.elements['overview_page']['recent_tasks_done']['buttons']['arrow_up'].Hide()

	def ShowArrowDownRecentTasksDone(self):
		self.elements['overview_page']['recent_tasks_done']['buttons']['arrow_down'].Show()

	def HideArrowDownRecentTasksDone(self):
		self.elements['overview_page']['recent_tasks_done']['buttons']['arrow_down'].Hide()

	## RECENT_TASKS_DONE FUNCTIONS END ##

	## CATEGORYS PROGRESS FUNCTIONS START ##
	def SetPercentCategoryProgress(self, id, cur, max):
		if cur >= max:
			self.elements['overview_page']['categorys_progress']['progressbar_full'][id].Hide()
			self.elements['overview_page']['categorys_progress']['progressbar_completed'][id].Show()
		else:
			self.elements['overview_page']['categorys_progress']['progressbar_completed'][id].Hide()
			self.elements['overview_page']['categorys_progress']['progressbar_full'][id].SetPercentage(float(cur), float(max))
			self.elements['overview_page']['categorys_progress']['progressbar_full'][id].Show()
	
	def SetTitleCategoryProgress(self, id, title):
		self.elements['overview_page']['categorys_progress']['title'][id].SetText(title)

	def ShowCategoryProgress(self, id):
		self.elements['overview_page']['categorys_progress']['content'][id].Show()

	def HideAllCategorysProgress(self):
		contents = self.elements['overview_page']['categorys_progress']['content']
		for content in contents:
			content.Hide()

	def HideCategoryProgress(self, id):
		self.elements['overview_page']['categorys_progress']['content'][id].Hide()

	def ShowArrowUpCategorysProgress(self):
		self.elements['overview_page']['categorys_progress']['buttons']['arrow_up'].Show()

	def HideArrowUpCategorysProgress(self):
		self.elements['overview_page']['categorys_progress']['buttons']['arrow_up'].Hide()

	def ShowArrowDownCategorysProgress(self):
		self.elements['overview_page']['categorys_progress']['buttons']['arrow_down'].Show()

	def HideArrowDownCategorysProgress(self):
		self.elements['overview_page']['categorys_progress']['buttons']['arrow_down'].Hide()

	## CATEGORYS PROGRESS FUNCTIONS END ##

	## STATISTIC FUNCTIONS START ##

	def SetTitleStatistic(self, id, title):
		self.elements['overview_page']['statistic']['title'][id].SetText(title)

	def SetValueStatistic(self, id, value):
		self.elements['overview_page']['statistic']['value'][id].SetText('%d' % value)

	def SetAchievementPoints(self, value):
		self.elements['overview_page']['achievement_points']['value'].SetText('%d' % value)

	## STATISTIC FUNCTIONS END ##

	## TASKS FUNCTIONS START ##
	def SetPercentTask(self, id, cur, max):
		if cur >= max:
			self.elements['tasks_page']['tasks']['progressbar_full'][id].Hide()
			self.elements['tasks_page']['tasks']['progressbar_completed'][id].Show()
		else:
			self.elements['tasks_page']['tasks']['progressbar_completed'][id].Hide()
			self.elements['tasks_page']['tasks']['progressbar_full'][id].SetPercentage(float(cur), float(max))
			self.elements['tasks_page']['tasks']['progressbar_full'][id].Show()
	
	def SetTitleTask(self, id, title):
		self.elements['tasks_page']['tasks']['title'][id].SetText(title)

	def SetValueTask(self, id, value):
		self.elements['tasks_page']['tasks']['value'][id].SetText(str(value))

	def ShowTask(self, id):
		self.elements['tasks_page']['tasks']['content'][id].Show()

	def HideAllTasks(self):
		contents = self.elements['tasks_page']['tasks']['content']
		for content in contents:
			content.Hide()

	def HideTask(self, id):
		self.elements['tasks_page']['tasks']['content'][id].Hide()

	def GetTasksScrollbarPos(self):
		return self.elements['tasks_page']['scrollbar'].GetPos()

	def ShowTasksScrollbar(self):
		self.elements['tasks_page']['scrollbar'].Show()

	def HideTasksScrollbar(self):
		self.elements['tasks_page']['scrollbar'].Hide()

	def SetTasksScrollbarPos(self, pos):
		self.elements['tasks_page']['scrollbar'].SetPos(pos)

	def SetTasksScrollbarMiddleBarSize(self, size):
		self.elements['tasks_page']['scrollbar'].SetMiddleBarSize(size)

	## available commands:
	## all
	## pending
	## done
	def SetTasksStateDown(self, state):
		self.elements['tasks_page']['buttons']['state_%s' % state].Down()

	def SetTasksStateUp(self, state):
		self.elements['tasks_page']['buttons']['state_%s' % state].SetUp()

	def SetAllTasksStatesUp(self):
		self.SetTasksStateUp('all')
		self.SetTasksStateUp('pending')
		self.SetTasksStateUp('done')

	## TASKS FUNCTIONS END ##

	## MAIN FUNCTIONS START ##

	## CHANGE TAB FUNCTIONS START ##
	def ChangeCategoryPage(self, page_id):
		self.page['current_id'] = page_id + self.page['current_tab']

		self.SetCategoryDown(page_id)

		self.RebuildMainWindow()

	def ChangeCategoryTab(self, direction):
		max_tab = len(self.achievements['categorys'])-6

		if direction == 'left' and self.page['current_tab'] > 0:
			self.page['current_tab'] -= 1
		elif direction == 'right' and self.page['current_tab'] < max_tab:
			self.page['current_tab'] += 1

		self.RebuildAllCategoryTitles()

	def ChangeCategorysProgressTab(self, direction):
		max_tab = len(self.achievements['categorys'])-6

		if direction == 'up' and self.page['overview']['categorys_progress']['current_tab'] > 0:
			self.page['overview']['categorys_progress']['current_tab'] -= 1
		elif direction == 'down' and self.page['overview']['categorys_progress']['current_tab'] < max_tab:
			self.page['overview']['categorys_progress']['current_tab'] += 1

		self.RebuildCategoryProgressContent()

	def ChangeRecentTasksDoneTab(self, direction):
		max_tab = len(self.achievements['categorys'][0]['recent_tasks_done'])-6

		if direction == 'up' and self.page['overview']['recent_tasks_done']['current_tab'] > 0:
			self.page['overview']['recent_tasks_done']['current_tab'] -= 1
		elif direction == 'down' and self.page['overview']['recent_tasks_done']['current_tab'] < max_tab:
			self.page['overview']['recent_tasks_done']['current_tab'] += 1

		self.RebuildRecentTasksDone()
		
	## CHANGE TAB FUNCTIONS END ##
	
	## CHANGE TASKS FUNCTIONS START ##

	def ChangeTasksState(self, state):
		self.page['tasks']['current_state'] = state
		self.SetTasksScrollbarPos(0)
		self.RebuildTasksPage()
		
	# def ChangeTasksSortType(self, type):
		# for self.page['tasks']['sort']['type'] in type:
			# self.page['tasks']['sort']['type'][type] = 0
			
		# self.page['tasks']['sort']['type'][type] = 1
		
		# self.RebuildTasksPage()
		
	# def ChangeTasksSortOrder(self, order):
		# if order == 'ascending':
			# self.page['tasks']['sort']['reverse'] = 0
		# elif order == 'descending':
			# self.page['tasks']['sort']['reverse'] = 1
		
		# self.RebuildTasksPage()

	## CHANGE TASKS FUNCTIONS END ##

	## SCROLL FUNCTIONS START ##

	def ScrollTasksPage(self):
		self.page['tasks']['current_pos'] = self.GetTasksScrollbarPos()
		self.RebuildTasksPage()

	## SCROLL FUNCTIONS END ##

	## REBUILD FUNCTIONS START ##

	def RebuildMainWindow(self):
		try:
			self.RebuildMainProgressbar()
		except:
			self.SendSystemChat('This should not happen. An error occured on rebuilding the main progressbar. Error(101f)')

		if self.page['current_id'] == 0:
			try:
				self.RebuildOverviewPageCompletely()
			except:
				self.SendSystemChat('This should not happen. An error occured on rebuilding the overview page by id. Error(102f)')
			self.ShowOverviewPage()
		else:
			try:
				self.SetTasksScrollbarPos(0) ## and RebuildTasksPage
			except:
				self.SendSystemChat('This should not happen. An error occured on rebuilding the tasks page by id. Error(103f)')
			self.ShowTasksPage()

	def RebuildAllCategoryTitles(self):

		start_index = self.page['current_tab']
		categorys_len = len(self.achievements['categorys'])

		if self.page['current_id'] >= start_index and self.page['current_id']-start_index <= 5:
			self.SetCategoryDown(self.page['current_id']-start_index)
		else:
			self.SetAllCategorysUp()

		self.HideAllCategorys()

		for i in xrange(min(6, categorys_len)):
			real_index = i + start_index
			self.SetTitleCategory(i, self.achievements['categorys'][real_index]['title'])
			self.ShowCategory(i)

		if start_index <= 0:
			 self.HideArrowLeftCategory()
			 self.ShowArrowRightCategory()
		elif start_index >= 1 and (start_index + 6) < categorys_len:
			self.ShowArrowLeftCategory()
			self.ShowArrowRightCategory()
		elif start_index >= 1 and (start_index + 6) >= categorys_len:
			self.ShowArrowLeftCategory()
			self.HideArrowRightCategory()

	def RebuildOverviewPageCompletely(self):
		self.RebuildCategoryProgressContent()
		self.RebuildRecentTasksDone()
		self.RebuildStatistic()

	def RebuildCategoryProgressContent(self):
		start_index = self.page['overview']['categorys_progress']['current_tab']
		achievements_len = len(self.achievements['categorys'])-1

		self.HideAllCategorysProgress()

		for i in xrange(min(5, achievements_len)):
			category = self.achievements['categorys'][i+1+start_index]
			mission_max = 0
			mission_min = 0
			for mission in category['missions']:
				if mission['percent']['min'] >= mission['percent']['max']:
					mission_min += 1
				mission_max += 1

			self.SetTitleCategoryProgress(i, category['title'])
			self.SetPercentCategoryProgress(i, mission_min, mission_max)
			self.ShowCategoryProgress(i)

		if start_index <= 0:
			 self.HideArrowUpCategorysProgress()
			 self.ShowArrowDownCategorysProgress()
		elif start_index >= 1 and (start_index + 5) < achievements_len:
			self.ShowArrowUpCategorysProgress()
			self.ShowArrowDownCategorysProgress()
		elif start_index >= 1 and (start_index + 5) >= achievements_len:
			self.ShowArrowUpCategorysProgress()
			self.HideArrowDownCategorysProgress()

	def RebuildRecentTasksDone(self):
		start_index = self.page['overview']['recent_tasks_done']['current_tab']
		recent_tasks_done = self.achievements['categorys'][0]['recent_tasks_done']
		recent_tasks_done_len = len(recent_tasks_done)

		self.HideAllRecentTasksDone()

		for i in xrange(min(6, recent_tasks_done_len)):
			recent_task = recent_tasks_done[i+start_index]
			self.SetTitleRecentTaskDone(i, recent_task['text'])
			self.SetValueRecentTaskDone(i, recent_task['achievement_points'])
			self.ShowRecentTaskDone(i)

		if start_index <= 0 and recent_tasks_done_len > 6:
			self.HideArrowUpRecentTasksDone()
			self.ShowArrowDownRecentTasksDone()
		elif start_index <= 0 and recent_tasks_done_len <= 6:
			self.HideArrowUpRecentTasksDone()
			self.HideArrowDownRecentTasksDone()
		elif start_index >= 1 and (start_index + 6) < recent_tasks_done_len:
			self.ShowArrowUpRecentTasksDone()
			self.ShowArrowDownRecentTasksDone()
		elif start_index >= 1 and (start_index + 6) >= recent_tasks_done_len:
			self.ShowArrowUpRecentTasksDone()
			self.HideArrowDownRecentTasksDone()

	def RebuildStatistic(self):
		missions_done = 0
		missions_pending = 0
		for i in range(len(self.achievements['categorys'])-1):
			category = self.achievements['categorys'][i+1]
			
			for mission in category['missions']:
				if mission['percent']['min'] >= mission['percent']['max']:
					missions_done += 1
				else:
					missions_pending += 1

		self.achievements['categorys'][0]['statistic']['data'][1]['value'] = missions_done
		self.achievements['categorys'][0]['statistic']['data'][2]['value'] = missions_pending

		statistic = self.achievements['categorys'][0]['statistic']

		for i in range(3):
			self.SetTitleStatistic(i, statistic['data'][i]['text'])
			self.SetValueStatistic(i, statistic['data'][i]['value'])
		self.SetAchievementPoints(statistic['current_achievement_points'])
			
	def RebuildTasksPage(self):
		current_page = self.page['current_id']
		current_state = self.page['tasks']['current_state']
		
		# sort_text = self.page['tasks']['sort']['type']['text']
		# sort_achievementpoints = self.page['tasks']['sort']['type']['achievement_points']
		# sort_reverse = self.page['tasks']['sort']['reverse']
		
		missions = self.achievements['categorys'][current_page]['missions']
		# if sort_text:
			# self.NaturalSort(missions, key=lambda x: x['text'], reverse=sort_reverse)
		# elif sort_achievementpoints:
			# missions.sort(key=lambda x: x['achievement_points'], reverse=sort_reverse)

		self.HideAllTasks()
		self.HideTasksScrollbar()

		self.SetAllTasksStatesUp()
		self.SetTasksStateDown(current_state)

		if current_state == 'pending':
			sorted_missions = []

			for i in xrange(len(missions)):
				mission = missions[i]
				if mission['percent']['min'] < mission['percent']['max']:
					sorted_missions.append(mission)

			missions = sorted_missions 

		elif current_state == 'done':
			sorted_missions = []

			for i in xrange(len(missions)):
				mission = missions[i]
				if mission['percent']['min'] >= mission['percent']['max']:
					sorted_missions.append(mission)

			missions = sorted_missions 

		missions_len = len(missions)
		start_index = int(self.page['tasks']['current_pos'] * (missions_len-8))

		for i in xrange(min(8, missions_len)):
			mission = missions[i+start_index]
			self.SetTitleTask(i, mission['text'])
			self.SetPercentTask(i, mission['percent']['min'], mission['percent']['max'])
			self.SetValueTask(i, mission['achievement_points'])
			self.ShowTask(i)

		if missions_len <= 8:## Set scrollbar middle Size, show or hide
			self.HideTasksScrollbar()
		else:
			self.SetTasksScrollbarMiddleBarSize(float(8)/float(len(missions)))
			self.ShowTasksScrollbar()

	def RebuildMainProgressbar(self):
		mission_min = 0
		mission_max = 0
		for i in range(len(self.achievements['categorys'])-1):
			category = self.achievements['categorys'][i+1]
			
			for mission in category['missions']:
				if mission['percent']['min'] >= mission['percent']['max']:
					mission_min += 1
				mission_max += 1

		self.SetPercentProgressbarMain(mission_min, mission_max)

	## REBUILD FUNCTIONS END ##
	
	## MOUSE OVER IN OUT FUNCTIONS START ##
	
	def OnMouseOverInRecentTasksDone(self, index):
		(x, y) = self.elements['overview_page']['recent_tasks_done']['image'][index].GetGlobalPosition()
		
		start_index = self.page['overview']['recent_tasks_done']['current_tab']
		recent_tasks_done = self.achievements['categorys'][0]['recent_tasks_done'][index+start_index]

		self.recent_task_done_tool_tip.ClearToolTip()
		self.recent_task_done_tool_tip.SetTitle(recent_tasks_done['text'])
		self.recent_task_done_tool_tip.SetToolTipPosition(x-10, y + 10)
		self.recent_task_done_tool_tip.ShowToolTip()
		
	def OnMouseOverOutRecentTasksDone(self, index):
		self.recent_task_done_tool_tip.HideToolTip()
	
	## MOUSE OVER IN OUT FUNCTIONS START ##

	## QUEST COMMANDS FUNCTIONS START ##
	
	def SetQid(self, qid):
		self.qid = qid
		
	def GetQuestCmd(self):
		net.SendQuestInputStringPacket(self.quest_cmd)
		self.quest_cmd = 'NULL#'

	def AddCategory(self, title):
		temp_category = { 'title' : title.replace('_', ' '),'missions' : [] }
		self.achievements['categorys'].append(temp_category)

	def UpdateStatisticAchievementpointsCurrent(self, points):
		self.achievements['categorys'][0]['statistic']['current_achievement_points'] = int(points)

	def UpdateStatisticAchievementpointsTotal(self, points):
		self.achievements['categorys'][0]['statistic']['data'][0]['value'] = int(points)
		
	def AddAchievementMission(self, category_id, actual, need, text, points):
		if actual > need:
			actual = need
		temp_mission = { 
			'text' : text.replace('_', ' '),
			'achievement_points' : points,
			'percent' : {
					'min': actual,
					'max': need,
			},
		}
		
		self.achievements['categorys'][category_id]['missions'].append(temp_mission)
		
	def UpdateAchievementMission(self, category_id, achievement_id, actual, need, text, points):
		# self.SendSystemChat('category_id: %d, achievement_id: %d , text: %s' % (category_id, achievement_id, text))
		if actual > need:
			actual = need
		if len(self.achievements['categorys']) > 1:
			temp_mission = { 
				'text' : text.replace('_', ' '),
				'achievement_points' : points,
				'percent' : {
						'min': actual,
						'max': need,
				},
			}
			
			self.achievements['categorys'][category_id]['missions'][achievement_id] = temp_mission
			
			if self.IsShow():
				if self.page['current_id'] != 0 and category_id == self.page['current_id']:
					self.RebuildTasksPage()
				elif self.page['current_id'] == 0:
					self.RebuildOverviewPageCompletely()
					
	def AddRecentTaskDone(self, category_id, achievement_id):
		try:
			achievement_mission = self.achievements['categorys'][category_id]['missions'][achievement_id]
			
			temp_mission = { 
				'text' : achievement_mission['text'],
				'achievement_points' : achievement_mission['achievement_points'],
			}
			
			# self.SendSystemChat('RECENT ADD: '+achievement_mission['text'])
			
			self.achievements['categorys'][0]['recent_tasks_done'].append(temp_mission)
		except:
			pass
		
	def UpdateRecentTaskDone(self, category_id, achievement_id):
		try:
			if len(self.achievements['categorys']) > 1:
				achievement_mission = self.achievements['categorys'][category_id]['missions'][achievement_id]
				
				temp_mission = { 
					'text' : achievement_mission['text'],
					'achievement_points' : achievement_mission['achievement_points'],
				}
				
				# self.SendSystemChat('RECENT UPDATE: '+achievement_mission['text'])
				
				self.achievements['categorys'][0]['recent_tasks_done'].insert(0, temp_mission) ## insert task
				# self.achievements['categorys'][0]['recent_tasks_done'].pop(len(self.achievements['categorys'][0]['recent_tasks_done'])-1) ## delete last task
				
				if self.IsShow() and self.page['current_id'] == 0:
					self.RebuildRecentTasksDone()
		except:
			pass
		
	## QUEST COMMANDS FUNCTIONS END ##
	
	## MAIN FUNCTIONS END ##

	def Command(self, received_cmd):
		received_cmd = received_cmd.split("/")
		cmd = received_cmd[0]
		param = received_cmd[1:]
		
		if cmd == 'OPEN':
			self.Open()

		elif cmd == 'SET_QID': ## param: qid
			self.SetQid(int(param[0]))
			
		elif cmd == 'GET_QUESTCMD':
			self.GetQuestCmd()
		
		elif cmd == 'SET_LOADINGBAR_PERCENT': ## param: percent
			self.loadingBar.SetPercent(int(param[0]))

		elif cmd == 'ADD_CATEGORY': ## param: category_name
			self.AddCategory(param[0])

		elif cmd == 'UPDATE_STATISTIC_ACHIEVEMENTPOINTS_CURRENT': ## param: points
			self.UpdateStatisticAchievementpointsCurrent(int(param[0]))

		elif cmd == 'UPDATE_STATISTIC_ACHIEVEMENTPOINTS_TOTAL': ## param: points
			self.UpdateStatisticAchievementpointsTotal(int(param[0]))
			
		elif cmd == 'ADD_ACHIEVEMENT_MISSION': ## param: category_id, actual, need, text, points
			self.AddAchievementMission(int(param[0]), int(param[1]), int(param[2]), param[3], int(param[4]))
			
		elif cmd == 'UPDATE_ACHIEVEMENT_MISSION': ## param: category_id, achievement_id, actual, need, text, points
			self.UpdateAchievementMission(int(param[0]), int(param[1]), int(param[2]), int(param[3]), param[4], int(param[5]))
			
		elif cmd == 'ADD_RECENT_TASK_DONE': ## param: category_id, achievement_id
			self.AddRecentTaskDone(int(param[0]), int(param[1]))
		
		elif cmd == 'UPDATE_RECENT_TASK_DONE': ## param: category_id, achievement_id
			self.UpdateRecentTaskDone(int(param[0]), int(param[1]))
			
		elif cmd == 'SHOW_ACHIEVEMENT_DONE':
			self.achievementDialog.Show(param[0])
			self.achievementDialog.SetTop()  
	
	def SendQuestCommand(self, cmd):
		self.quest_cmd = cmd
		# self.SendSystemChat('Sending command: %s to qid: %d ' % (cmd, self.qid))
		event.QuestButtonClick(self.qid)
			
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.ClearAchievements()
		self.SetDefaultPageVar()
		self.Hide()

	def OpenRequest(self):
		# self.SendSystemChat('OpenRequest Send')
		self.loadingBar.Open()
		
		if len(self.achievements['categorys']) <= 1:
			self.SendQuestCommand('OPEN#0') ## update request
		else:
			self.SendQuestCommand('OPEN#1')

	def Open(self):
		self.ChangeCategoryPage(0)
		self.RebuildAllCategoryTitles()
		self.SetTop()
		self.Show()
		
	def Close(self):
		self.Hide()

	def SendSystemChat(self, text):
		chat.AppendChat(chat.CHAT_TYPE_INFO, "<Achievementsystem>: " + str(text))

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE
		
	# def NaturalSort(self, list, key=lambda s:s, reverse=False):
		# def GetAlphanumKeyFunc(key):
			# convert = lambda text: int(text) if text.isdigit() else text 
			# return lambda s: [convert(c) for c in re.split('([0-9]+)', key(s))]
		# sort_key = GetAlphanumKeyFunc(key)
		# list.sort(key=sort_key, reverse=reverse)

class LoadingBar(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.isLoaded = FALSE

	def __LoadScript(self):
		## Load gui
		try: 
			self.BindObjects()
		except:
			import exception
			exception.Abort('achievementsystem.LoadingBar.__LoadScript.BindObjects')
			
		self.isLoaded = TRUE
		
	## Bind the objects in __LoadScript
	def BindObjects(self):
		global ACHIEVEMENTSYSTEM_PATH

		self.board = ui.ThinBoard()
		self.board.SetSize(260,30)
		self.board.SetCenterPosition()
		self.board.Show()

		self.progressBarActualFile = ui.AniImageBox()
		self.progressBarActualFile.SetParent(self.board)
		self.progressBarActualFile.AppendImage(ACHIEVEMENTSYSTEM_PATH + 'other/loading_bar.tga')
		self.progressBarActualFile.SetPosition(5, 8)
		self.progressBarActualFile.SetDelay(90)
		self.progressBarActualFile.SetPercentage(0, 100)
		self.progressBarActualFile.Show()

		self.lb_load = ui.TextLine()
		self.lb_load.SetParent(self.board)
		self.lb_load.SetPosition(10,9)
		self.lb_load.SetText('Laden')
		self.lb_load.Show()

		self.lb_percent = ui.TextLine()
		self.lb_percent.SetParent(self.board)
		self.lb_percent.SetPosition(225,9)
		self.lb_percent.SetText('0%')
		self.lb_percent.Show()

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	## Hide the Gui
	def Destroy(self):
		self.Hide()

	def SetPercent(self, percent):
		if percent >= 100:
			self.board.Hide()
		else:
			self.board.SetTop()
			self.board.Show()
			self.progressBarActualFile.SetPercentage(percent, 100)
			self.lb_percent.SetText(str(percent) +'%')
		
	## Open the gui
	def Open(self):
		if FALSE == self.isLoaded:
			self.__LoadScript()
		self.SetTop()
		self.Show()

	## Close the gui
	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

	def OnPressExitKey(self):
		self.Close()
		return TRUE
		
		

AchievementPoints = 0

class AchievementDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__Load()
		
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Destroy(self):
		self.Hide()
		return TRUE
		
	def __Load_LoadScript(self, fileName):
		try:
			pyScriptLoader = ui.PythonScriptLoader()
			pyScriptLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("AchievementDialog.__Load_LoadScript")

	def __Load_BindObject(self):
		try:
			self.AchievementText = self.GetChild("Achievement_Text")
			self.AchievementTextFiller = self.GetChild("Achievement_Filler")
			self.AchievementCountText = self.GetChild("Count_Achievement_Text")
			self.AchievementCountTextFiller = self.GetChild("Count_Filler")
			self.AchievementPointsText = self.GetChild("Achievement_Points_Text")
			self.AchievementInfoTextPage1 = self.GetChild("Achievement_Info_1")
			self.AchievementInfoTextPage2 = self.GetChild("Achievement_Info_2")
			self.AchievementInfoTextPage3 = self.GetChild("Achievement_Info_3")
		except:
			import exception
			exception.Abort("AchievementDialog.__Load_BindObject")

	def __Load(self):
		self.__Load_LoadScript("uiscript/achievementboard.py")
		self.__Load_BindObject()
		width = wndMgr.GetScreenWidth()
		height = wndMgr.GetScreenHeight()
	
	def Show(self, archivement):
		global AchievementPoints
		ui.ScriptWindow.Show(self)
		self.AchievementSetText(str(archivement))
		self.WarteSchleife = WaitingDialog()
		self.WarteSchleife.Open(3.0)
		self.WarteSchleife.SAFE_SetTimeOverEvent(self.ShowAchievementPoints)
		
	
	def AchievementSetText(self, archivement):
		global AchievementPoints
		self.AchievementTextFiller.SetText("Achievement erreicht:")
		if archivement.find("_") != -1:
			archivement = archivement.replace('_', ' ')
		if archivement.find("%") != -1:
			AchievementSplit = archivement.split("%")
			archivement = AchievementSplit[0]
			AchievementPoints = AchievementSplit[1]
		if archivement.find("#") != -1:
			Splittext = archivement.split("#")
			Achievement = Splittext[0]
			Count = Splittext[1]
			self.AchievementText.SetText(str(Achievement))
			self.AchievementCountTextFiller.SetText(str(Count))
		else:
			self.AchievementText.SetText(str(archivement))
			self.AchievementCountTextFiller.SetText("Herzlichen Glückwunsch.")
			self.AchievementCountText.SetText("")
		self.AchievementPointsText.SetText("")
		self.AchievementInfoTextPage1.SetText("")
		self.AchievementInfoTextPage2.SetText("")
		self.AchievementInfoTextPage3.SetText("")
	
	def ShowAchievementPoints(self):
		global AchievementPoints
		self.AchievementTextFiller.SetText("Deine Achievement-Punkte")
		self.AchievementText.SetText("")
		self.AchievementPointsText.SetText("steigen auf:")
		self.AchievementCountTextFiller.SetText("")
		self.AchievementCountText.SetText(str(AchievementPoints))
		self.WarteSchleife = WaitingDialog()
		self.WarteSchleife.Open(3.0)
		self.WarteSchleife.SAFE_SetTimeOverEvent(self.Information)
		
	def Information(self):
		self.AchievementTextFiller.SetText("")
		self.AchievementText.SetText("")
		self.AchievementPointsText.SetText("")
		self.AchievementCountTextFiller.SetText("")
		self.AchievementCountText.SetText("")
		self.AchievementInfoTextPage1.SetText("Du kannst deine Punkte")
		self.AchievementInfoTextPage2.SetText("im Achievement-Shop")
		self.AchievementInfoTextPage3.SetText("eintauschen.")
		self.WarteSchleife = WaitingDialog()
		self.WarteSchleife.Open(2.5)
		self.WarteSchleife.SAFE_SetTimeOverEvent(self.Close)
		
	def Close(self):
		self.Hide()
		return TRUE
		
	def OnPressEscapeKey(self):
		self.Hide()
		return TRUE

class WaitingDialog(ui.ScriptWindow):

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
			PythonScriptLoader.LoadScriptFile(self, "uiscript/WarteSchleife.py")

		except:
			import exception
			exception.Abort("WaitingDialog.LoadDialog.BindObject")

	def Open(self, waitTime):
		curTime = time.clock()
		self.endTime = curTime + waitTime

		self.Show()		

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

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
			return
		
	def OnPressExitKey(self):
		self.Close()
		return TRUE


wnd = Achievementsystem()
