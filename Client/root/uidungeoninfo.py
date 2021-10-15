import app
import ui
import uiToolTip
import grp
import item
import player
import constInfo
import localeInfo
import uiScriptLocale
import uiCommon
import net
import renderTarget
import nonplayer
import constInfo
import chat

class DungeonInfo(ui.ScriptWindow):
	TOOLTIP_NORMAL_COLOR = grp.GenerateColor(0.9490, 0.9058, 0.7568, 1.0)
	TOOLTIP_SPECIAL_COLOR = grp.GenerateColor(1.0, 0.7843, 0.0, 1.0)
	MIN_SCROLLBAR_LIST = 10

	AFFECT_DICT = {
		item.APPLY_MAX_HP : localeInfo.TOOLTIP_MAX_HP,
		item.APPLY_MAX_SP : localeInfo.TOOLTIP_MAX_SP,
		item.APPLY_CON : localeInfo.TOOLTIP_CON,
		item.APPLY_INT : localeInfo.TOOLTIP_INT,
		item.APPLY_STR : localeInfo.TOOLTIP_STR,
		item.APPLY_DEX : localeInfo.TOOLTIP_DEX,
		item.APPLY_ATT_SPEED : localeInfo.TOOLTIP_ATT_SPEED,
		item.APPLY_MOV_SPEED : localeInfo.TOOLTIP_MOV_SPEED,
		item.APPLY_CAST_SPEED : localeInfo.TOOLTIP_CAST_SPEED,
		item.APPLY_HP_REGEN : localeInfo.TOOLTIP_HP_REGEN,
		item.APPLY_SP_REGEN : localeInfo.TOOLTIP_SP_REGEN,
		item.APPLY_POISON_PCT : localeInfo.TOOLTIP_APPLY_POISON_PCT,
		item.APPLY_STUN_PCT : localeInfo.TOOLTIP_APPLY_STUN_PCT,
		item.APPLY_SLOW_PCT : localeInfo.TOOLTIP_APPLY_SLOW_PCT,
		item.APPLY_CRITICAL_PCT : localeInfo.TOOLTIP_APPLY_CRITICAL_PCT,
		item.APPLY_PENETRATE_PCT : localeInfo.TOOLTIP_APPLY_PENETRATE_PCT,

		item.APPLY_ATTBONUS_WARRIOR : localeInfo.TOOLTIP_APPLY_ATTBONUS_WARRIOR,
		item.APPLY_ATTBONUS_ASSASSIN : localeInfo.TOOLTIP_APPLY_ATTBONUS_ASSASSIN,
		item.APPLY_ATTBONUS_SURA : localeInfo.TOOLTIP_APPLY_ATTBONUS_SURA,
		item.APPLY_ATTBONUS_SHAMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_SHAMAN,
		item.APPLY_ATTBONUS_MONSTER : localeInfo.TOOLTIP_APPLY_ATTBONUS_MONSTER,

		item.APPLY_ATTBONUS_HUMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_HUMAN,
		item.APPLY_ATTBONUS_ANIMAL : localeInfo.TOOLTIP_APPLY_ATTBONUS_ANIMAL,
		item.APPLY_ATTBONUS_ORC : localeInfo.TOOLTIP_APPLY_ATTBONUS_ORC,
		item.APPLY_ATTBONUS_MILGYO : localeInfo.TOOLTIP_APPLY_ATTBONUS_MILGYO,
		item.APPLY_ATTBONUS_UNDEAD : localeInfo.TOOLTIP_APPLY_ATTBONUS_UNDEAD,
		item.APPLY_ATTBONUS_DEVIL : localeInfo.TOOLTIP_APPLY_ATTBONUS_DEVIL,
		item.APPLY_STEAL_HP : localeInfo.TOOLTIP_APPLY_STEAL_HP,
		item.APPLY_STEAL_SP : localeInfo.TOOLTIP_APPLY_STEAL_SP,
		item.APPLY_MANA_BURN_PCT : localeInfo.TOOLTIP_APPLY_MANA_BURN_PCT,
		item.APPLY_DAMAGE_SP_RECOVER : localeInfo.TOOLTIP_APPLY_DAMAGE_SP_RECOVER,
		item.APPLY_BLOCK : localeInfo.TOOLTIP_APPLY_BLOCK,
		item.APPLY_DODGE : localeInfo.TOOLTIP_APPLY_DODGE,
		item.APPLY_RESIST_SWORD : localeInfo.TOOLTIP_APPLY_RESIST_SWORD,
		item.APPLY_RESIST_TWOHAND : localeInfo.TOOLTIP_APPLY_RESIST_TWOHAND,
		item.APPLY_RESIST_DAGGER : localeInfo.TOOLTIP_APPLY_RESIST_DAGGER,
		item.APPLY_RESIST_BELL : localeInfo.TOOLTIP_APPLY_RESIST_BELL,
		item.APPLY_RESIST_FAN : localeInfo.TOOLTIP_APPLY_RESIST_FAN,
		item.APPLY_RESIST_BOW : localeInfo.TOOLTIP_RESIST_BOW,
		item.APPLY_RESIST_FIRE : localeInfo.TOOLTIP_RESIST_FIRE,
		item.APPLY_RESIST_ELEC : localeInfo.TOOLTIP_RESIST_ELEC,
		item.APPLY_RESIST_MAGIC : localeInfo.TOOLTIP_RESIST_MAGIC,
		item.APPLY_RESIST_WIND : localeInfo.TOOLTIP_APPLY_RESIST_WIND,
		item.APPLY_REFLECT_MELEE : localeInfo.TOOLTIP_APPLY_REFLECT_MELEE,
		item.APPLY_REFLECT_CURSE : localeInfo.TOOLTIP_APPLY_REFLECT_CURSE,
		item.APPLY_POISON_REDUCE : localeInfo.TOOLTIP_APPLY_POISON_REDUCE,
		item.APPLY_KILL_SP_RECOVER : localeInfo.TOOLTIP_APPLY_KILL_SP_RECOVER,
		item.APPLY_EXP_DOUBLE_BONUS : localeInfo.TOOLTIP_APPLY_EXP_DOUBLE_BONUS,
		item.APPLY_GOLD_DOUBLE_BONUS : localeInfo.TOOLTIP_APPLY_GOLD_DOUBLE_BONUS,
		item.APPLY_ITEM_DROP_BONUS : localeInfo.TOOLTIP_APPLY_ITEM_DROP_BONUS,
		item.APPLY_POTION_BONUS : localeInfo.TOOLTIP_APPLY_POTION_BONUS,
		item.APPLY_KILL_HP_RECOVER : localeInfo.TOOLTIP_APPLY_KILL_HP_RECOVER,
		item.APPLY_IMMUNE_STUN : localeInfo.TOOLTIP_APPLY_IMMUNE_STUN,
		item.APPLY_IMMUNE_SLOW : localeInfo.TOOLTIP_APPLY_IMMUNE_SLOW,
		item.APPLY_IMMUNE_FALL : localeInfo.TOOLTIP_APPLY_IMMUNE_FALL,
		item.APPLY_BOW_DISTANCE : localeInfo.TOOLTIP_BOW_DISTANCE,
		item.APPLY_DEF_GRADE_BONUS : localeInfo.TOOLTIP_DEF_GRADE,
		item.APPLY_ATT_GRADE_BONUS : localeInfo.TOOLTIP_ATT_GRADE,
		item.APPLY_MAGIC_ATT_GRADE : localeInfo.TOOLTIP_MAGIC_ATT_GRADE,
		item.APPLY_MAGIC_DEF_GRADE : localeInfo.TOOLTIP_MAGIC_DEF_GRADE,
		item.APPLY_MAX_STAMINA : localeInfo.TOOLTIP_MAX_STAMINA,
		item.APPLY_MALL_ATTBONUS : localeInfo.TOOLTIP_MALL_ATTBONUS,
		item.APPLY_MALL_DEFBONUS : localeInfo.TOOLTIP_MALL_DEFBONUS,
		item.APPLY_MALL_EXPBONUS : localeInfo.TOOLTIP_MALL_EXPBONUS,
		item.APPLY_MALL_ITEMBONUS : localeInfo.TOOLTIP_MALL_ITEMBONUS,
		item.APPLY_MALL_GOLDBONUS : localeInfo.TOOLTIP_MALL_GOLDBONUS,
		item.APPLY_SKILL_DAMAGE_BONUS : localeInfo.TOOLTIP_SKILL_DAMAGE_BONUS,
		item.APPLY_NORMAL_HIT_DAMAGE_BONUS : localeInfo.TOOLTIP_NORMAL_HIT_DAMAGE_BONUS,
		item.APPLY_SKILL_DEFEND_BONUS : localeInfo.TOOLTIP_SKILL_DEFEND_BONUS,
		item.APPLY_NORMAL_HIT_DEFEND_BONUS : localeInfo.TOOLTIP_NORMAL_HIT_DEFEND_BONUS,
		item.APPLY_RESIST_WARRIOR : localeInfo.TOOLTIP_APPLY_RESIST_WARRIOR,
		item.APPLY_RESIST_ASSASSIN : localeInfo.TOOLTIP_APPLY_RESIST_ASSASSIN,
		item.APPLY_RESIST_SURA : localeInfo.TOOLTIP_APPLY_RESIST_SURA,
		item.APPLY_RESIST_SHAMAN : localeInfo.TOOLTIP_APPLY_RESIST_SHAMAN,
		item.APPLY_MAX_HP_PCT : localeInfo.TOOLTIP_APPLY_MAX_HP_PCT,
		item.APPLY_MAX_SP_PCT : localeInfo.TOOLTIP_APPLY_MAX_SP_PCT,
		item.APPLY_ENERGY : localeInfo.TOOLTIP_ENERGY,
		item.APPLY_COSTUME_ATTR_BONUS : localeInfo.TOOLTIP_COSTUME_ATTR_BONUS,

		item.APPLY_MAGIC_ATTBONUS_PER : localeInfo.TOOLTIP_MAGIC_ATTBONUS_PER,
		item.APPLY_MELEE_MAGIC_ATTBONUS_PER : localeInfo.TOOLTIP_MELEE_MAGIC_ATTBONUS_PER,
		item.APPLY_RESIST_ICE : localeInfo.TOOLTIP_RESIST_ICE,
		item.APPLY_RESIST_EARTH : localeInfo.TOOLTIP_RESIST_EARTH,
		item.APPLY_RESIST_DARK : localeInfo.TOOLTIP_RESIST_DARK,
		item.APPLY_ANTI_CRITICAL_PCT : localeInfo.TOOLTIP_ANTI_CRITICAL_PCT,
		item.APPLY_ANTI_PENETRATE_PCT : localeInfo.TOOLTIP_ANTI_PENETRATE_PCT,
	}
	if app.ENABLE_WOLFMAN_CHARACTER:
		AFFECT_DICT.update({
			item.APPLY_BLEEDING_PCT : localeInfo.TOOLTIP_APPLY_BLEEDING_PCT,
			item.APPLY_BLEEDING_REDUCE : localeInfo.TOOLTIP_APPLY_BLEEDING_REDUCE,
			item.APPLY_ATTBONUS_WOLFMAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_WOLFMAN,
			item.APPLY_RESIST_CLAW : localeInfo.TOOLTIP_APPLY_RESIST_CLAW,
			item.APPLY_RESIST_WOLFMAN : localeInfo.TOOLTIP_APPLY_RESIST_WOLFMAN,
		})

	if app.ENABLE_MAGIC_REDUCTION_SYSTEM:
		AFFECT_DICT.update({
			item.APPLY_RESIST_MAGIC_REDUCTION : localeInfo.TOOLTIP_RESIST_MAGIC_REDUCTION,
		})

	if app.ENABLE_NEW_ATTRIBUTE_TYPES:
		AFFECT_DICT.update({
			item.APPLY_ATTBONUS_STONE : localeInfo.TOOLTIP_ATTBONUS_STONE,
			item.APPLY_ATTBONUS_BOSS : localeInfo.TOOLTIP_ATTBONUS_BOSS,
			item.APPLY_ATTBONUS_ELEMENTS : localeInfo.TOOLTIP_ATTBONUS_ELEMENTS,
			item.APPLY_ENCHANT_ELEMENTS : localeInfo.TOOLTIP_ENCHANT_ELEMENTS,
			item.APPLY_ATTBONUS_CHARACTERS : localeInfo.TOOLTIP_ATTBONUS_CHARACTERS,
			item.APPLY_ENCHANT_CHARACTERS : localeInfo.TOOLTIP_ENCHANT_CHARACTERS,
			item.APPLY_ATTBONUS_RAZADOR : localeInfo.TOOLTIP_ATTBONUS_RAZADOR,
			item.APPLY_ATTBONUS_NEMERE : localeInfo.TOOLTIP_ATTBONUS_NEMERE,
			item.APPLY_ATTBONUS_LUCIFER : localeInfo.TOOLTIP_ATTBONUS_LUCIFER,
			item.APPLY_ATTBONUS_BLUE_DRAGON : localeInfo.TOOLTIP_ATTBONUS_BLUE_DRAGON,
			item.APPLY_ATTBONUS_RED_DRAGON : localeInfo.TOOLTIP_ATTBONUS_RED_DRAGON,
			item.APPLY_ATTBONUS_AZRAEL : localeInfo.TOOLTIP_ATTBONUS_AZRAEL,

		})

	#ENABLE_PENDANT_SYSTEM
	AFFECT_DICT.update({
		item.APPLY_ENCHANT_ELECT : localeInfo.TOOLTIP_APPLY_ENCHANT_ELECT,
		item.APPLY_ENCHANT_FIRE : localeInfo.TOOLTIP_APPLY_ENCHANT_FIRE,
		item.APPLY_ENCHANT_ICE : localeInfo.TOOLTIP_APPLY_ENCHANT_ICE,
		item.APPLY_ENCHANT_WIND : localeInfo.TOOLTIP_APPLY_ENCHANT_WIND,
		item.APPLY_ENCHANT_EARTH : localeInfo.TOOLTIP_APPLY_ENCHANT_EARTH,
		item.APPLY_ENCHANT_DARK : localeInfo.TOOLTIP_APPLY_ENCHANT_DARK,

		item.APPLY_RESIST_HUMAN : localeInfo.TOOLTIP_APPLY_RESIST_HUMAN,
		item.APPLY_ATTBONUS_SWORD : localeInfo.TOOLTIP_APPLY_ATTBONUS_SWORD,
		item.APPLY_ATTBONUS_TWOHAND: localeInfo.TOOLTIP_APPLY_ATTBONUS_TWOHAND,
		item.APPLY_ATTBONUS_DAGGER : localeInfo.TOOLTIP_APPLY_ATTBONUS_DAGGER,
		item.APPLY_ATTBONUS_BELL : localeInfo.TOOLTIP_APPLY_ATTBONUS_BELL,
		item.APPLY_ATTBONUS_FAN : localeInfo.TOOLTIP_APPLY_ATTBONUS_FAN,
		item.APPLY_ATTBONUS_BOW : localeInfo.TOOLTIP_APPLY_ATTBONUS_BOW,
		item.APPLY_ATTBONUS_CZ : localeInfo.TOOLTIP_APPLY_ATTBONUS_CZ,
		item.APPLY_ATTBONUS_DESERT : localeInfo.TOOLTIP_APPLY_ATTBONUS_DESERT,
		item.APPLY_ATTBONUS_INSECT : localeInfo.TOOLTIP_APPLY_ATTBONUS_INSECT,
		item.APPLY_ATTBONUS_CLAW : localeInfo.TOOLTIP_APPLY_ATTBONUS_CLAW,
	})

	DUNGEON_TYPE = {
		0 : localeInfo.DUNGEON_INFO_TYPE0,
		1 : localeInfo.DUNGEON_INFO_TYPE1,
		2 : localeInfo.DUNGEON_INFO_TYPE2
	}

	DUNGEON_ORGANIZATION = {
		0 : localeInfo.DUNGEON_INFO_ORGANIZATION0,
		1 : localeInfo.DUNGEON_INFO_ORGANIZATION1,
		2 : localeInfo.DUNGEON_INFO_ORGANIZATION2
	}

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.dungeonIndex = 0
		self.dungeonButton = {}
		self.dungeonImage = {}
		self.dungeonImageIcon = {}
		self.dungeonName = {}
		self.dungeonAvailable = {}
		self.questionDialog = None
		self.renderModelPreview = None
		self.isAlreadyLoaded = False

	def __del__(self):
		ui.ScriptWindow.__del__(self)

		self.dungeonIndex = 0
		self.dungeonButton = {}
		self.dungeonImage = {}
		self.dungeonImageIcon = {}
		self.dungeonName = {}
		self.dungeonAvailable = {}
		self.questionDialog = None
		self.renderModelPreview = None
		self.isAlreadyLoaded = False

	def LoadDialog(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/dungeoninfowindow.py")
		except:
			import exception
			exception.Abort("DungeonInfo.LoadDialog.LoadScript")

		try:
			self.dungeonBoard = self.GetChild("DungeonBoard")
			self.dungeonBoardTitleBar = self.GetChild("DungeonBoardTitleBar")

			self.dungeonButtonBoard = self.GetChild("DungeonButtonBoard")
			self.dungeonButtonThinBoard = self.GetChild("DungeonButtonThinBoard")

			self.dungeonInfoItem = self.GetChild("DungeonInfoItem")
			self.dungeonInfoItemSlot = self.GetChild("DungeonInfoItemSlot")

			self.dungeonScrollBar = self.GetChild("ScrollBar")
			self.dungeonInfoBoard = self.GetChild("DungeonInfoBoard")

			self.dungeonInfoName = self.GetChild("DungeonInfoName")
			self.dungeonInfoType = self.GetChild("DungeonInfoType")
			self.dungeonInfoOrganization = self.GetChild("DungeonInfoOrganization")
			self.dungeonInfoLevelLimit = self.GetChild("DungeonInfoLevelLimit")
			self.dungeonInfoPartyMembers = self.GetChild("DungeonInfoPartyMembers")
			self.dungeonInfoCooldown = self.GetChild("DungeonInfoCooldown")
			self.dungeonInfoDuration = self.GetChild("DungeonInfoDuration")
			self.dungeonInfoEntrance = self.GetChild("DungeonInfoEntrance")
			self.dungeonInfoStrengthBonus = self.GetChild("DungeonInfoStrengthBonus")
			self.dungeonInfoResistanceBonus = self.GetChild("DungeonInfoResistanceBonus")

			self.dungeonInfoTeleportButton = self.GetChild("DungeonInfoTeleportButton")
			self.closeDungeonBoard = self.GetChild("CloseDungeonBoard")

			self.dungeonRenderTarget = self.GetChild("DungeonInfoRender")
			self.dungeonRenderTarget.SetEvent(ui.__mem_func__(self.OnPressedInfoButton))

		except:
			import exception
			exception.Abort("DungeonInfo.LoadDialog.GetChild")

		self.dungeonBoardTitleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.closeDungeonBoard.SetEvent(ui.__mem_func__(self.Close))
		self.dungeonInfoTeleportButton.SetEvent(self.TeleportDungeon)

		self.toolTip = uiToolTip.ToolTip()

		self.LoadDungeonButtons()
		self.LoadDungeonInfoBoard(self.dungeonIndex)

		self.isAlreadyLoaded = True

	def OnPressedInfoButton(self):
		if self.renderModelPreview:
			self.OnRenderBossClose()
		elif int(constInfo.dungeonInfo[self.dungeonIndex]['boss_vnum']) != 0:
			self.OnRenderBoss(int(constInfo.dungeonInfo[self.dungeonIndex]['boss_vnum']))

	def OnRenderBoss(self, model):
		if model == 2493:
			return
		RENDER_TARGET_INDEX = 12

		self.renderModelPreview = ui.ThinBoardDungeon()
		self.renderModelPreview.SetParent(self)
		self.renderModelPreview.SetSize(190+10, 280+30)
		self.renderModelPreview.SetPosition(537, 431 / 6)
		self.renderModelPreview.Show()

		self.modelPreviewTarget = ui.RenderTarget()
		self.modelPreviewTarget.SetParent(self.renderModelPreview)
		self.modelPreviewTarget.SetSize(190, 280)
		self.modelPreviewTarget.SetPosition(5, 22)
		self.modelPreviewTarget.SetRenderTarget(RENDER_TARGET_INDEX)
		self.modelPreviewTarget.Show()

		self.modelPreviewTargetText = ui.TextLine()
		self.modelPreviewTargetText.SetParent(self.renderModelPreview)
		self.modelPreviewTargetText.SetPackedFontColor(0xffFFB96D)
		self.modelPreviewTargetText.SetPosition(0, 5)
		self.modelPreviewTargetText.SetText(nonplayer.GetMonsterName(int(constInfo.dungeonInfo[self.dungeonIndex]['boss_vnum'])))
		self.modelPreviewTargetText.SetOutline()
		self.modelPreviewTargetText.SetFeather(False)
		self.modelPreviewTargetText.SetWindowHorizontalAlignCenter()
		self.modelPreviewTargetText.SetHorizontalAlignCenter()
		self.modelPreviewTargetText.Show()
		renderTarget.SetBackground(RENDER_TARGET_INDEX, "d:/ymir work/ui/game/myshop_deco/model_view_bg.sub")
		renderTarget.SetVisibility(RENDER_TARGET_INDEX, True)
		renderTarget.SelectModel(RENDER_TARGET_INDEX, model)
		if model == 1093:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.6, 0.6, 0.6)
		elif model == 694:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.7, 0.7, 0.7)
		elif model == 2092:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.2, 0.2, 0.2)
		elif model == 2598:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.5, 0.5, 0.5)
		elif model == 6091:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.5, 0.5, 0.5)
		elif model == 6191:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.5, 0.5, 0.5)
		elif model == 4103:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.5, 0.5, 0.5)

	def OnChangeRenderBoss(self, vnum):
		if vnum == 2493:
			self.modelPreviewTargetText.SetText(nonplayer.GetMonsterName(vnum))
			return
		RENDER_TARGET_INDEX = 12
		renderTarget.SelectModel(RENDER_TARGET_INDEX, vnum)
		if vnum == 1093:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.6, 0.6, 0.6)
		elif vnum == 694:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.7, 0.7, 0.7)
		elif vnum == 2092:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.2, 0.2, 0.2)
		elif vnum == 2598:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.5, 0.5, 0.5)
		elif vnum == 6091:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.5, 0.5, 0.5)
		elif vnum == 6191:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.5, 0.5, 0.5)
		elif model == 4103:
			renderTarget.SetScale(RENDER_TARGET_INDEX, 0.5, 0.5, 0.5)
		self.modelPreviewTargetText.SetText(nonplayer.GetMonsterName(vnum))
		
	def OnRenderBossClose(self):
		RENDER_TARGET_INDEX = 12

		if self.renderModelPreview:
			self.renderModelPreview.Hide()
			self.modelPreviewTargetText.Hide()

			self.renderModelPreview = None
			self.modelPreviewTargetText = None

			renderTarget.SetVisibility(RENDER_TARGET_INDEX, False)
			
	def Close(self):
		if self.toolTip:
			self.toolTip = None

		self.isAlreadyLoaded = False
		
		self.OnRenderBossClose()
		
		self.Hide()

	def GetAffectString(self, affectType):
		if 0 == affectType:
			return None

		try:
			bonus = self.AFFECT_DICT[affectType](affectType)
			bonus = bonus.replace('%', '').replace('+', '')
			result = ''.join([i for i in bonus if not i.isdigit()])
			return result
		except TypeError:
			return "UNKNOWN_VALUE[%s] %s" % (affectType, affectType)
		except KeyError:
			return "UNKNOWN_TYPE[%s] %s" % (affectType, affectType)
		
	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Open(self):
		if not self.isAlreadyLoaded:
			self.LoadDialog()

		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def LoadDungeonButtons(self):
		if not constInfo.dungeonInfo:
			return

		for index in xrange(min(self.MIN_SCROLLBAR_LIST, len(constInfo.dungeonInfo))):
			self.AppendDungeonButton(
				index,\
				self.dungeonButtonBoard,\
				3, 3 + (38 * index)
			)

		if len(constInfo.dungeonInfo) <= self.MIN_SCROLLBAR_LIST:
			self.dungeonScrollBar.SetMiddleBarSize(float(len(constInfo.dungeonInfo)) / float(len(constInfo.dungeonInfo)))
			self.dungeonScrollBar.Show()
		else:
			self.dungeonScrollBar.SetMiddleBarSize(float(self.MIN_SCROLLBAR_LIST) / float(len(constInfo.dungeonInfo)))
			self.dungeonScrollBar.Show()

		self.dungeonScrollBar.SetScrollEvent(self.OnScroll)

	def OnScroll(self):
		button_count = len(self.dungeonButton)
		pos = int(self.dungeonScrollBar.GetPos() * (len(constInfo.dungeonInfo) - button_count))

		self.dungeonButton = {}
		self.dungeonImage = {}
		self.dungeonImageIcon = {}
		self.dungeonName = {}
		self.dungeonAvailable = {}

		for idx in xrange(min(self.MIN_SCROLLBAR_LIST, button_count)):
			realPos = idx + pos

			self.AppendDungeonButton(
				realPos,\
				self.dungeonButtonBoard,\
				3, 3 + (38 * idx)
			)

			if realPos != self.dungeonIndex:
				self.dungeonButton[realPos].SetUpVisual("d:/ymir work/ui/game/mailbox/post_default.sub")
				self.dungeonButton[realPos].SetOverVisual("d:/ymir work/ui/game/mailbox/post_over.sub")
				self.dungeonButton[realPos].SetDownVisual("d:/ymir work/ui/game/mailbox/post_select.sub")

	def AppendDungeonButton(self, index, parent, x, y):
		self.dungeonButton[index] = ui.Button()
		self.dungeonButton[index].SetParent(parent)
		self.dungeonButton[index].SetUpVisual("d:/ymir work/ui/game/mailbox/post_select.sub")
		self.dungeonButton[index].SetOverVisual("d:/ymir work/ui/game/mailbox/post_select.sub")
		self.dungeonButton[index].SetDownVisual("d:/ymir work/ui/game/mailbox/post_select.sub")
		self.dungeonButton[index].SetPosition(x, y)
		self.dungeonButton[index].SetEvent(lambda: self.LoadDungeonInfoBoard(index))
		self.dungeonButton[index].Show()

		self.dungeonImage[index] = ui.ImageBox()
		self.dungeonImage[index].SetParent(self.dungeonButton[index])
		self.dungeonImage[index].LoadImage("d:/ymir work/ui/game/mailbox/mailbox_icon_empty.sub")
		self.dungeonImage[index].SetPosition(1, 2)
		self.dungeonImage[index].Show()

		self.dungeonImageIcon[index] = ui.Button()
		self.dungeonImageIcon[index].SetParent(self.dungeonImage[index])

		mapIndex = constInfo.dungeonInfo[index]['map_index']
		self.dungeonImageIcon[index].SetUpVisual("d:/ymir work/ui/game/dungeon_info/icons/%d.tga" % mapIndex)
		self.dungeonImageIcon[index].SetOverVisual("d:/ymir work/ui/game/dungeon_info/icons/%d.tga" % mapIndex)
		self.dungeonImageIcon[index].SetDownVisual("d:/ymir work/ui/game/dungeon_info/icons/%d.tga" % mapIndex)
		self.dungeonImageIcon[index].SetEvent(lambda: self.LoadDungeonInfoBoard(index))

		self.dungeonImageIcon[index].SetPosition(0, 0)
		self.dungeonImageIcon[index].Show()

		self.dungeonName[index] = ui.TextLine()
		self.dungeonName[index].SetParent(self.dungeonButton[index])
		self.dungeonName[index].SetPosition(40, 10)
		self.dungeonName[index].SetText("%s" % constInfo.dungeonInfo[index]['map'])
		self.dungeonName[index].Show()

		self.dungeonAvailable[index] = ui.TextLine()
		self.dungeonAvailable[index].SetParent(self.dungeonButton[index])
		self.dungeonAvailable[index].SetPosition(200, 10)
		self.dungeonAvailable[index].SetText(localeInfo.DUNGEON_INFO_UNAVAILABLE)
		self.dungeonAvailable[index].Show()

		self.dungeonAvailable[index].SetText("data_loading")
	def LoadDungeonInfoBoard(self, index):
		self.dungeonIndex = index

		mapIndex = constInfo.dungeonInfo[self.dungeonIndex]['map_index']
		if (self.dungeonIndex == 0):
			self.dungeonInfoBoard.LoadImage("d:/ymir work/ui/game/dungeon_info/background/66.tga")
		else:
			self.dungeonInfoBoard.LoadImage("d:/ymir work/ui/game/dungeon_info/background/%d.tga" % int(mapIndex))

		self.dungeonButton[self.dungeonIndex].SetUpVisual("d:/ymir work/ui/game/mailbox/post_select.sub")
		self.dungeonButton[self.dungeonIndex].SetOverVisual("d:/ymir work/ui/game/mailbox/post_select.sub")
		self.dungeonButton[self.dungeonIndex].SetDownVisual("d:/ymir work/ui/game/mailbox/post_select.sub")

		pos = int(self.dungeonScrollBar.GetPos() * (len(constInfo.dungeonInfo) - len(self.dungeonButton)))
		for idx in xrange(len(self.dungeonButton)):
			realPos = idx + pos
			if realPos != self.dungeonIndex:
				self.dungeonButton[realPos].SetUpVisual("d:/ymir work/ui/game/mailbox/post_default.sub")
				self.dungeonButton[realPos].SetOverVisual("d:/ymir work/ui/game/mailbox/post_over.sub")
				self.dungeonButton[realPos].SetDownVisual("d:/ymir work/ui/game/mailbox/post_select.sub")

		dungeonMap = str(constInfo.dungeonInfo[self.dungeonIndex]['map'])
		dungeonType = constInfo.dungeonInfo[self.dungeonIndex]['type']
		dungeonOrganization = constInfo.dungeonInfo[self.dungeonIndex]['organization']
		dungeonLevelMin = constInfo.dungeonInfo[self.dungeonIndex]['min_level']
		dungeonLevelMax = constInfo.dungeonInfo[self.dungeonIndex]['max_level']
		dungeonPartyMembers = constInfo.dungeonInfo[self.dungeonIndex]['party_members']
		dungeonCooldown = constInfo.dungeonInfo[self.dungeonIndex]['cooldown']
		dungeonDuration = constInfo.dungeonInfo[self.dungeonIndex]['duration']
		dungeonEntranceMap = str(constInfo.dungeonInfo[self.dungeonIndex]['entrance_map'])
		dungeonStrengthBonus = self.GetAffectString(constInfo.dungeonInfo[self.dungeonIndex]['strength_bonus'])
		dungeonResistanceBonus = self.GetAffectString(constInfo.dungeonInfo[self.dungeonIndex]['resistance_bonus'])
		dungeonItemVnum = int(constInfo.dungeonInfo[self.dungeonIndex]['item_vnum'])

		self.dungeonInfoName.SetText("%s" % dungeonMap)
		self.dungeonInfoType.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_TYPE, self.DUNGEON_TYPE[dungeonType]))
		self.dungeonInfoOrganization.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_ORGANIZATION, self.DUNGEON_ORGANIZATION[dungeonOrganization]))
		self.dungeonInfoLevelLimit.SetText("%s : %d - %d" % (uiScriptLocale.DUNGEON_INFO_LEVEL_LIMIT, dungeonLevelMin, dungeonLevelMax))
		self.dungeonInfoPartyMembers.SetText("%s : %d" % (uiScriptLocale.DUNGEON_INFO_PARTY_MEMBERS, dungeonPartyMembers))
		self.dungeonInfoCooldown.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_COOLDOWN, self.FormatTime(dungeonCooldown)))
		self.dungeonInfoDuration.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_DURATION, self.FormatTime(dungeonDuration)))
		self.dungeonInfoEntrance.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_ENTRANCE, dungeonEntranceMap))
		self.dungeonInfoStrengthBonus.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_STRENGTH, dungeonStrengthBonus))
		self.dungeonInfoResistanceBonus.SetText("%s : %s" % (uiScriptLocale.DUNGEON_INFO_RESISTANCE, dungeonResistanceBonus))

		if dungeonItemVnum > 0:
			self.dungeonInfoItemSlot.LoadImage("icon/item/%d.tga" % dungeonItemVnum)
		else:
			self.dungeonInfoItemSlot.LoadImage("d:/ymir work/ui/pet/skill_button/skill_enable_button.sub")

		if self.renderModelPreview:
			self.OnChangeRenderBoss(int(constInfo.dungeonInfo[self.dungeonIndex]['boss_vnum']))
	def FormatTime(self, seconds):
		if seconds == 0:
			return localeInfo.DUNGEON_INFO_NONE

		m, s = divmod(seconds, 60)
		h, m = divmod(m, 60)

		return "%d:%02d:%02d" % (h, m, s)

	def SecondToHM(time):
		second = int(time % 60)
		minute = int((time / 60) % 60)
		hour = int((time / 60) / 60) % 24

		if hour <= 0:
			return "Soðuma: 00:%d:%02d" % (minute, second)
		else:
			return "Soðuma: 0%d:%02d:%02d" % (hour, minute,second)

	def TeleportDungeon(self):
		if player.GetStatus(player.LEVEL) < constInfo.dungeonInfo[self.dungeonIndex]['min_level']:
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DUNGEON_INFO_LEVEL_ERROR)
			return
		self.questionDialog = uiCommon.QuestionDialog()
		self.questionDialog.Open()
		self.questionDialog.SetText(localeInfo.DUNGEON_INFO_TELEPORT % str(constInfo.dungeonInfo[self.dungeonIndex]['map']))
		self.questionDialog.SetAcceptText(localeInfo.UI_ACCEPT)
		self.questionDialog.SetCancelText(localeInfo.UI_DENY)
		self.questionDialog.SetAcceptEvent(lambda arg = True: self.AnswerTeleport(arg))
		self.questionDialog.SetCancelEvent(lambda arg = False: self.AnswerTeleport(arg))
		self.questionDialog.SetTop()

	def AnswerTeleport(self, answer):
		if not self.questionDialog:
			return

		if answer == True:
			import event

			dungeonMapCoordX = int(constInfo.dungeonInfo[self.dungeonIndex]['map_coord_x'])
			dungeonMapCoordY = int(constInfo.dungeonInfo[self.dungeonIndex]['map_coord_y'])

			net.DungeonTeleport(dungeonMapCoordX, dungeonMapCoordY)

		self.questionDialog.Close()
		self.questionDialog = None

	def OnUpdate(self):
		pos = int(self.dungeonScrollBar.GetPos() * (len(constInfo.dungeonInfo) - len(self.dungeonButton)))

		for idx in xrange(min(self.MIN_SCROLLBAR_LIST, len(self.dungeonButton))):
			realPos = idx + pos
			format_time = constInfo.dungeonInfo[realPos]['cooldown']-app.GetGlobalTimeStamp()
	
			if player.GetStatus(player.LEVEL) >= constInfo.dungeonInfo[realPos]['min_level']:
				self.dungeonAvailable[realPos].SetText(localeInfo.DUNGEON_INFO_AVAILABLE)
				self.dungeonAvailable[realPos].SetPosition(200, 10)
				if (format_time < 0):
					self.dungeonAvailable[realPos].SetText(localeInfo.DUNGEON_INFO_AVAILABLE)
					self.dungeonAvailable[realPos].SetPosition(200, 10)
				else:
					self.dungeonAvailable[realPos].SetText("|cffc9c89a%s|r" % SecondToHM(format_time))
					self.dungeonAvailable[realPos].SetPosition(200-8, 10)
			elif player.GetStatus(player.LEVEL) <= constInfo.dungeonInfo[realPos]['min_level']:
				self.dungeonAvailable[realPos].SetText(localeInfo.DUNGEON_INFO_UNAVAILABLE)
				self.dungeonAvailable[realPos].SetPosition(200, 10)

			
		if self.toolTip:
			if self.dungeonInfoItemSlot.IsIn():
				self.toolTip.ClearToolTip()

				dungeonItemVnum = constInfo.dungeonInfo[self.dungeonIndex]['item_vnum']
				if dungeonItemVnum > 0:
					item.SelectItem(dungeonItemVnum)

					self.toolTip.AppendTextLine(item.GetItemName(), self.TOOLTIP_SPECIAL_COLOR)
					self.toolTip.AppendDescription(item.GetItemDescription(), 26)

					self.toolTip.AlignHorizonalCenter()
					self.toolTip.ShowToolTip()

			else:
				self.toolTip.HideToolTip()

