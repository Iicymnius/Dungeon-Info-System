//add;

#ifdef ENABLE_DUNGEON_INFO_SYSTEM
#include "dungeon_info.h"
#endif

//find;

	if (g_noticeBattleZone)

//add above;

#ifdef ENABLE_DUNGEON_INFO_SYSTEM
	DungeonInfo::instance().Update(ch);
#endif