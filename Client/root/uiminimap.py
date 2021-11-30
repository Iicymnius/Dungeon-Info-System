#find;

class MiniMap(ui.ScriptWindow):

#find in function;

	def __init__(self):

#change;

	def __init__(self, interface):

#find in same function;

		self.canSeeInfo = True

#add below;

		self.interface = interface

#find again;

		self.serverInfo = None

#add below;

		self.interface = None

#find again;

		self.AtlasShowButton = 0

#add below;

		if app.ENABLE_DUNGEON_INFO_SYSTEM:
			self.dungeonInfoButton = 0

#find again;

			self.serverInfo = self.GetChild("ServerInfo")

#add below;

			if app.ENABLE_DUNGEON_INFO_SYSTEM:
				self.dungeonInfoButton = self.GetChild("l_button")

#find again;

		self.MiniMapShowButton.SetEvent(ui.__mem_func__(self.ShowMiniMap))

#add below;

		if app.ENABLE_DUNGEON_INFO_SYSTEM:
			self.dungeonInfoButton.SetEvent(ui.__mem_func__(self.DungeonInfo))

#find again;

	def ShowAtlas(self):
		if not miniMap.IsAtlas():
			return
		if not self.AtlasWindow.IsShow():
			self.AtlasWindow.Show()

#add below;

	if app.ENABLE_DUNGEON_INFO_SYSTEM:
		def DungeonInfo(self):
			if self.interface:
				self.interface.ShowDungeonInfoInterface()
