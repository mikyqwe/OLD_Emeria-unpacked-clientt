import ui
import grp
import localeInfo
## Ente ente ente ente
IMG_PATH = "d:/ymir work/ui/DropdownTree/"

class DropdownTreeMain(ui.BoardWithTitleBar):
	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.isLoaded = FALSE
		if FALSE == self.isLoaded:
			self.__LoadMe()

	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)
		
	def SetTextLineCube(self, text):
		self.textLineCube.SetText("[id:%s]"%text)
		
	def __LoadMe(self):
		self.SetSize(350, 2220+35+20)
		self.SetCenterPosition()
		self.AddFlag('movable')
		self.SetTitleName("Example Dropdown Tree by Ente")
		self.SetCloseEvent(self.Close)
		
		textLineCube = ui.TextLine()
		textLineCube.SetParent(self)
		textLineCube.SetPosition(215, 35)
		textLineCube.SetSize(100 -15 -15, 20)
		textLineCube.SetText('[]')
		textLineCube.Show()
		self.textLineCube = textLineCube

		listBoxCube = DropdownTree()
		listBoxCube.SetParent(self)
		listBoxCube.SetPosition(215,35+20)
		listBoxCube.SetSize(310, 200)
		listBoxCube.SetItemSize(310, 18)
		listBoxCube.SetViewItemCount(10)
		listBoxCube.Show()
		self.listBoxCube = listBoxCube

		scrollBarListBoxCube = ui.ScrollBar()
		scrollBarListBoxCube.SetParent(self)
		scrollBarListBoxCube.SetPosition(310+15,35+20)
		scrollBarListBoxCube.SetScrollBarSize(200)
		scrollBarListBoxCube.Show()
		self.scrollBarListBoxCube = scrollBarListBoxCube

		self.listBoxCube.SetScrollBar(self.scrollBarListBoxCube)

		listBoxCubeItems = [
			{ 
				'item' : self.CreateCubeMenuTab1Item("Oberkategorie 1", lambda arg = ("1"): self.SetTextLineCube(arg)), 
				'children' : (
					{
						'item' : self.CreateCubeMenuTab2Item("Unterkategorie 1 1", lambda arg = ("1 1"): self.SetTextLineCube(arg), 5),
						'children' : (
							{
								'item' : self.CreateCubeMenuTab3Item("Unterkategorie 1 1 1", lambda arg = ("1 1 1"): self.SetTextLineCube(arg), 10)
							},
							{
								'item' : self.CreateCubeMenuTab3Item("Unterkategorie 1 1 2", lambda arg = ("1 1 2"): self.SetTextLineCube(arg), 10)
							},
							{
								'item' : self.CreateCubeMenuTab3Item("Unterkategorie 1 1 3", lambda arg = ("1 1 3"): self.SetTextLineCube(arg), 10)
							},
							{
								'item' : self.CreateCubeMenuTab3Item("Unterkategorie 1 1 4", lambda arg = ("1 1 4"): self.SetTextLineCube(arg), 10)
							}
						)
					},
					{
						'item' : self.CreateCubeMenuTab2Item("Unterkategorie 1 2", lambda arg = ("1 2"): self.SetTextLineCube(arg), 5),
						'children' : (
							{
								'item' : self.CreateCubeMenuTab3Item("Unterkategorie 1 2 1", lambda arg = ("1 2 1"): self.SetTextLineCube(arg), 10)
							},
						)
					}
				)
			},
			{ 
				'item' : self.CreateCubeMenuTab1Item("Oberkategorie 2", lambda arg = ("2"): self.SetTextLineCube(arg)), 
				'children' : (
					{
						'item' : self.CreateCubeMenuTab3Item("Unterkategorie 2 1", lambda arg = ("2 1"): self.SetTextLineCube(arg), 10)
					},
					{
						'item' : self.CreateCubeMenuTab3Item("Unterkategorie 2 2", lambda arg = ("2 2"): self.SetTextLineCube(arg), 10)
					},
					{
						'item' : self.CreateCubeMenuTab3Item("Unterkategorie 2 3", lambda arg = ("2 3"): self.SetTextLineCube(arg), 10)
					},
					{
						'item' : self.CreateCubeMenuTab3Item("Unterkategorie 2 4", lambda arg = ("2 4"): self.SetTextLineCube(arg), 10)
					},
					{
						'item' : self.CreateCubeMenuTab3Item("Unterkategorie 2 5", lambda arg = ("2 5"): self.SetTextLineCube(arg), 10)
					},
					{
						'item' : self.CreateCubeMenuTab3Item("Unterkategorie 2 6", lambda arg = ("2 6"): self.SetTextLineCube(arg), 10)
					},
					{
						'item' : self.CreateCubeMenuTab3Item("Unterkategorie 2 7", lambda arg = ("2 7"): self.SetTextLineCube(arg), 10)
					},
					{
						'item' : self.CreateCubeMenuTab3Item("Unterkategorie 2 8", lambda arg = ("2 8"): self.SetTextLineCube(arg), 10)
					},
					{
						'item' : self.CreateCubeMenuTab3Item("Unterkategorie 2 9", lambda arg = ("2 9"): self.SetTextLineCube(arg), 10)
					},
					{
						'item' : self.CreateCubeMenuTab3Item("Unterkategorie 2 10", lambda arg = ("2 10"): self.SetTextLineCube(arg), 10)
					},
				)
			},
			{ 
				'item' : self.CreateListItem("Oberkategorie 3", lambda arg = ("3"): self.SetTextLineCube(arg)), 
				'children' : (
					{
						'item' : self.CreateSubListItem("Unterkategorie 3 1", lambda arg = ("3 1"): self.SetTextLineCube(arg), 10),
						'children' : (
							{
								'item' : self.CreateSubListItem("Unterkategorie 3 1 1", lambda arg = ("3 1 1"): self.SetTextLineCube(arg), 15),
								'children' : (
									{
										'item' : self.CreateLastListItem("Unterkategorie 3 1 1 1", lambda arg = ("3 1 1 1"): self.SetTextLineCube(arg), 20)
									},
									{
										'item' : self.CreateLastListItem("Unterkategorie 3 1 1 2", lambda arg = ("3 1 1 2"): self.SetTextLineCube(arg), 20)
									},
								)
							},
							{
								'item' : self.CreateSubListItem("Unterkategorie 3 2 1", lambda arg = ("3 2 1"): self.SetTextLineCube(arg), 15),
								'children' : (
									{
										'item' : self.CreateLastListItem("Unterkategorie 3 2 1 1", lambda arg = ("3 2 1 1"): self.SetTextLineCube(arg), 20)
									},
								)
							},
						)
					},
				)
			}
		]

		self.listBoxCube.AppendItemList(listBoxCubeItems)
		self.isLoaded = True

	def CreateCubeMenuTab1Item(self, text, event, offset = 0):
		listboxItem = CubeMenuTab1(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem

	def CreateCubeMenuTab2Item(self, text, event, offset = 0):
		listboxItem = CubeMenuTab2(text)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem

	def CreateCubeMenuTab3Item(self, text, event, offset = 0):
		listboxItem = CubeMenuTab3(text)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem

	def CreateListItem(self, text, event, offset = 0):
		listboxItem = ListItem(text)
		listboxItem.SetVisible(True)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem

	def CreateSubListItem(self, text, event, offset = 0):
		listboxItem = SubListItem(text)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem
	
	def CreateLastListItem(self, text, event, offset = 0):
		listboxItem = LastListItem(text)
		listboxItem.SetEvent(event)
		listboxItem.SetOffset(offset)
		return listboxItem

	def Open(self):
		self.Show()

	def Close(self):
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnPressExitKey(self):
		self.Close()
		return True

class DropdownTree(ui.Window):
	class Item(ui.Window):
		def __init__(self):
			ui.Window.__init__(self)
			self.id = -1
			self.parentId = -1
			self.offset = 0
			self.visible = False
			self.expanded = False
			self.event = None
			self.onCollapseEvent = None
			self.onExpandEvent = None
			
		def __del__(self):
			ui.Window.__del__(self)

		def SetParent(self, parent):
			ui.Window.SetParent(self, parent)
			self.parent=ui.proxy(parent)

		def SetSize(self, width, height):
			ui.Window.SetSize(self, width, height)

		def GetId(self):
			return self.id

		def SetId(self, id):
			self.id = id

		def GetParentId(self):
			return self.parentId

		def SetParentId(self, parentId):
			self.parentId = parentId
			
		def IsParent(self):
			return self.parentId == -1

		def SetVisible(self, visible):
			self.visible = visible
			
		def IsVisible(self):
			return self.visible
			
		def IsExpanded(self):
			return self.expanded
			
		def Expand(self):
			self.expanded = True
			if self.onExpandEvent:
				self.onExpandEvent()
			
		def Collapse(self):
			self.expanded = False
			if self.onCollapseEvent:
				self.onCollapseEvent()

		def SetOnExpandEvent(self, event):
			self.onExpandEvent = event

		def SetOnCollapseEvent(self, event):
			self.onCollapseEvent = event

		def SetOffset(self, offset):
			self.offset = offset

		def GetOffset(self):
			return self.offset

		def SetEvent(self, event):
			self.event = event

		def OnSelect(self):
			if self.event:
				self.event()
			self.parent.SelectItem(self)
		
		def OnSelect2(self):
			if self.event:
				self.event()
			#self.parent.SelectItem(self)
						
		def OnMouseLeftButtonDown(self):
			self.OnSelect()

	def __init__(self):
		ui.Window.__init__(self)
		self.__curItemId=0
		self.viewItemCount=12
		self.basePos=0
		self.itemHeight=16+7
		self.itemStep=20+7
		self.selItem=0
		self.itemList=[]
		self.onSelectItemEvent = lambda *arg: None
		self.itemWidth=140
		self.scrollBar=None
		self.__UpdateSize()
		self.LEN = 0
	def __del__(self):
		ui.Window.__del__(self)

	def __UpdateSize(self):
		height=self.itemStep*self.__GetViewItemCount()

		self.SetSize(self.itemWidth, height)

	def IsEmpty(self):
		if len(self.itemList)==0:
			return 1
		return 0

	def SetItemStep(self, itemStep):
		self.itemStep=itemStep
		self.__UpdateSize()

	def SetItemSize(self, itemWidth, itemHeight):
		self.itemWidth=itemWidth
		self.itemHeight=itemHeight
		self.__UpdateSize()
	
	def SetViewItemCount(self, viewItemCount):
		self.viewItemCount=viewItemCount
	
	def SetSelectEvent(self, event):
		self.onSelectItemEvent = event

	def SetBasePos(self, basePos):
		for oldItem in self.itemList:
			oldItem.Hide()

		self.basePos=basePos

		skipCount = basePos
		pos = basePos
		for lItem in self.itemList:
			if not lItem.IsVisible():
				continue
			
			if skipCount > 0:
				skipCount -= 1
				continue

			if pos >= (self.basePos+self.viewItemCount):
				break

			(x, y) = self.GetItemViewCoord(pos, lItem.GetWidth())
			lItem.SetPosition(x+lItem.GetOffset(), y)
			lItem.Show()
			pos+=1
		self.UpdateScrollbar()

	def GetItemIndex(self, argItem):
		return self.itemList.index(argItem)

	def GetSelectedItem(self):
		return self.selItem

	def SelectIndex(self, index):
		if index >= len(self.itemList) or index < 0:
			self.selItem = None
			return
		try:
			self.selItem=self.itemList[index]
		except:
			pass

	def ClearItem(self):
		self.selItem=None
		for lItem in self.itemList:
			lItem.Hide()

		self.itemList=[]
		self.__curItemId = 0

		if self.scrollBar:
			self.scrollBar.SetPos(0)
		self.SetBasePos(0)

	def SelectItem(self, selItem):
		self.selItem = selItem
		if selItem.IsExpanded():
			self.CloseTree(selItem, self.itemList)
		else:
			self.OpenTree(selItem, self.itemList)
		self.SetBasePos(self.basePos)

	def __AppendItem(self, newItem, parentId):
		curItemId = self.__curItemId
		self.__curItemId += 1
		
		newItem.SetParent(self)
		newItem.SetParentId(parentId)
		newItem.SetSize(self.itemWidth, self.itemHeight)
		newItem.SetId(curItemId)

		pos = self.__GetItemCount()
		self.itemList.append(newItem)

		if newItem.IsVisible() and self.__IsInViewRange(pos):
			(x, y)=self.GetItemViewCoord(pos, newItem.GetWidth())
			newItem.SetPosition(x, y)
			newItem.Show()
		else:
			newItem.Hide()

		self.UpdateScrollbar()

		return curItemId

	def AppendItemList(self, dict):
		self.__AppendItemList(-1, dict)
	
	def __AppendItemList(self, parentId, dict):
		for lItem in dict:
			if 'item' in lItem:
				id = self.__AppendItem(lItem['item'], parentId)
				if 'children' in lItem:
					self.__AppendItemList(id, lItem['children'])
				
	def SetScrollBar(self, scrollBar):
		scrollBar.SetScrollEvent(ui.__mem_func__(self.__OnScroll))
		self.scrollBar=scrollBar

	def __OnScroll(self):
		self.SetBasePos(int(self.scrollBar.GetPos()*self.__GetScrollLen()))

	def __GetScrollLen(self):
		scrollLen=self.__GetItemCount()-self.__GetViewItemCount()
		if scrollLen<0:
			return 0

		return scrollLen

	def __GetViewItemCount(self):
		return self.viewItemCount

	def __GetItemCount(self):
		return sum(1 for lItem in self.itemList if lItem.IsVisible())

	def GetItemViewCoord(self, pos, itemWidth):
		return (0, (pos-self.basePos)*self.itemStep)

	def __IsInViewRange(self, pos):
		if pos<self.basePos:
			return 0
		if pos>=self.basePos+self.viewItemCount:
			return 0
		return 1
	
	def UpdateScrollbar(self):
		if self.__GetViewItemCount() < self.__GetItemCount():
			self.scrollBar.SetMiddleBarSize(float(self.__GetViewItemCount())/self.__GetItemCount())
			self.scrollBar.Show()
		else:
			self.scrollBar.Hide()
		
	def CloseTree(self, curItem, list):
		curItem.Collapse()
		for listboxItem in list:
			if listboxItem.GetParentId() == curItem.GetId():
				listboxItem.SetVisible(False)
				self.CloseTree(listboxItem, list)
		self.SetBasePos(0)

		
	def OpenTree(self, curItem, list):
		#close all
		for item in range(self.LEN):
			for listboxItem in list:
				self.CloseTree(listboxItem, list)
		##
		curItem.Expand()
		for listboxItem in list:
			if listboxItem.GetParentId() == curItem.GetId():
				listboxItem.SetVisible(True)

		
	def SetLEN(self,var):
		self.LEN = var
		
class CubeMenuTab1(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,1)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(3,5)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_tab1_plus.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(3,5)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_tab1_minus.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)
		
		
class CubeMenuTab2(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab2.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,1)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(4,4)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_tab2_plus.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(4,4)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_tab2_minus.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)

class CubeMenuTab3(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		clearButton = ui.Button()
		clearButton.SetParent(self)
		clearButton.SetUpVisual(IMG_PATH +"cube_menu_tab3_default.sub")
		clearButton.SetOverVisual(IMG_PATH +"cube_menu_tab3_select.sub")
		clearButton.SetDownVisual(IMG_PATH +"cube_menu_tab3_select.sub")
		clearButton.SetText(text)
		clearButton.SetEvent(self.OnSelect2)
		clearButton.SetPosition(0,0)
		clearButton.Show()
		self.text = text
		self.clearButton = clearButton
		
	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def GetText(self):
		return self.text
		
	def __del__(self):
		DropdownTree.Item.__del__(self)

class ListItem(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetFontName(localeInfo.UI_DEF_FONT)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(self)
		iconExtendedImage.SetPosition(0,0)
		iconExtendedImage.LoadImage(IMG_PATH + "plus.tga")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(self)
		iconCollapsedImage.SetPosition(0,0)
		iconCollapsedImage.LoadImage(IMG_PATH + "minus.tga")
		iconCollapsedImage.Hide()

		textLine.SetText(text)
		textLine.Show()
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage
		self.text = text

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def __del__(self):
		DropdownTree.Item.__del__(self)

	def GetText(self):
		return self.text

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def OnMouseOverIn(self):
		self.overLine = True

	def OnMouseOverOut(self):
		self.overLine = False

	def OnRender(self):
		if self.overLine and self.parent.GetSelectedItem()!=self:
			x, y = self.GetGlobalPosition()
			grp.SetColor(grp.GenerateColor(0.0, 1.0, 1.0, 0.2))
			grp.RenderBar(x, y, self.GetWidth(), self.GetHeight())
		elif self.parent.GetSelectedItem()==self:
			x, y = self.GetGlobalPosition()
			grp.SetColor(grp.GenerateColor(0.0, 0.0, 0.7, 0.7))
			grp.RenderBar(x, y, self.GetWidth(), self.GetHeight())

class SubListItem(ListItem):
	def OnRender(self):
		if self.overLine and self.parent.GetSelectedItem()!=self:
			x, y = self.GetGlobalPosition()
			grp.SetColor(grp.GenerateColor(1.0, 0.0, 1.0, 0.2))
			grp.RenderBar(x, y, self.GetWidth(), self.GetHeight())
		elif self.parent.GetSelectedItem()==self:
			x, y = self.GetGlobalPosition()
			grp.SetColor(grp.GenerateColor(1.0, 0.0, 0.7, 0.7))
			grp.RenderBar(x, y, self.GetWidth(), self.GetHeight())

class LastListItem(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False
		textLine=ui.TextLine()
		textLine.SetParent(self)
		textLine.SetFontName(localeInfo.UI_DEF_FONT)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()

		textLine.SetText(text)
		textLine.Show()
		self.textLine = textLine
		self.text = text

	def __del__(self):
		DropdownTree.Item.__del__(self)

	def GetText(self):
		return self.text

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def OnMouseOverIn(self):
		self.overLine = True

	def OnMouseOverOut(self):
		self.overLine = False

	def OnRender(self):
		if self.overLine and self.parent.GetSelectedItem()!=self:
			x, y = self.GetGlobalPosition()
			grp.SetColor(grp.GenerateColor(1.0, 1.0, 1.0, 0.2))
			grp.RenderBar(x, y, self.GetWidth(), self.GetHeight())
		elif self.parent.GetSelectedItem()==self:
			x, y = self.GetGlobalPosition()
			grp.SetColor(grp.GenerateColor(0.0, 1.0, 0.7, 0.7))
			grp.RenderBar(x, y, self.GetWidth(), self.GetHeight())

class NewMenuTab1(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,5)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(3,5)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_all.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(3,5)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_all.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)

class NewMenuTab2(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,5)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(3,5)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_waffe.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(3,5)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_waffe.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)

class NewMenuTab3(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,5)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(3,4)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_ruestung.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(3,4)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_ruestung.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)

class NewMenuTab4(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,5)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(4,5)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_schmuck.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(4,5)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_schmuck.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)

class NewMenuTab5(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,5)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(3,4)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_kosi.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(3,4)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_kosi.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)

class NewMenuTab6(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,5)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(3,6)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_books.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(3,6)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_books.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)

class NewMenuTab7(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,5)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(4,3)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_potts.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(4,3)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_potts.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)

class NewMenuTab8(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,5)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(3,5)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_steine.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(3,5)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_steine.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)

class NewMenuTab9(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,5)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(3,5)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_mount.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(3,5)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_mount.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)

class NewMenuTab10(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,5)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(4,5)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_pet.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(4,5)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_pet.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)

class NewMenuTab11(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,5)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(3,4)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_upps.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(3,4)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_upps.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)
		
class NewMenuTab12(DropdownTree.Item):
	def __init__(self, text):
		DropdownTree.Item.__init__(self)
		self.overLine = False

		iconBackgroundImage = ui.ImageBox()
		iconBackgroundImage.SetParent(self)
		iconBackgroundImage.AddFlag("not_pick")
		iconBackgroundImage.SetPosition(0,0)
		iconBackgroundImage.LoadImage(IMG_PATH +"cube_menu_tab1.sub")
		iconBackgroundImage.Show()

		textLine=ui.TextLine()
		textLine.SetParent(iconBackgroundImage)
		textLine.SetPosition(0,5)
		textLine.SetWindowHorizontalAlignCenter()
		textLine.SetHorizontalAlignCenter()
		textLine.SetText(text)
		textLine.Show()

		iconExtendedImage = ui.ImageBox()
		iconExtendedImage.SetParent(iconBackgroundImage)
		iconExtendedImage.SetPosition(3,4)
		iconExtendedImage.LoadImage(IMG_PATH +"cube_menu_minime.sub")
		iconExtendedImage.Show()

		iconCollapsedImage = ui.ImageBox()
		iconCollapsedImage.SetParent(iconBackgroundImage)
		iconCollapsedImage.SetPosition(3,4)
		iconCollapsedImage.LoadImage(IMG_PATH +"cube_menu_minime.sub")
		iconCollapsedImage.Hide()

		self.iconBackgroundImage = iconBackgroundImage
		self.textLine = textLine
		self.iconExtendedImage = iconExtendedImage
		self.iconCollapsedImage = iconCollapsedImage

		self.SetOnExpandEvent(self.ExpandEvent)
		self.SetOnCollapseEvent(self.CollapseEvent)

	def SetSize(self, width, height):
		DropdownTree.Item.SetSize(self, width-self.GetOffset(), height)

	def CollapseEvent(self):
		self.iconCollapsedImage.Hide()
		self.iconExtendedImage.Show()

	def ExpandEvent(self):
		self.iconExtendedImage.Hide()
		self.iconCollapsedImage.Show()

	def GetText(self):
		return self.textLine.GetText()

	def __del__(self):
		DropdownTree.Item.__del__(self)