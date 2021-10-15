//add;

#ifdef ENABLE_DUNGEON_INFO_SYSTEM
#include "dungeon_info.h"
#endif

//find;

int CInputMain::Analyze(LPDESC d, BYTE bHeader, const char* c_pData)

//add above;

#ifdef ENABLE_DUNGEON_INFO_SYSTEM
void CInputMain::DungeonTeleport(LPCHARACTER ch, const char* c_pData)
{
	if (!ch->GetDesc())
		return;

	TPacketGCTeleport* p = (TPacketGCTeleport*)c_pData;
	ch->WarpSet(p->mapCoords[0] * 100, p->mapCoords[1] * 100);
}
#endif

//find again;

	case HEADER_CG_DRAGON_SOUL_REFINE:
	[
		...
	]

//add below;

#ifdef ENABLE_DUNGEON_INFO_SYSTEM
	case HEADER_CG_TELEPORT:
		DungeonTeleport(ch, c_pData);
		break;
#endif