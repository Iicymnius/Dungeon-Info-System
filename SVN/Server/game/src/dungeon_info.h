#include "../../common/service.h"
#ifdef ENABLE_DUNGEON_INFO_SYSTEM
#ifndef __INC_METIN_II_GAME_DUNGEON_INFO_H__
#define __INC_METIN_II_GAME_DUNGEON_INFO_H__
#pragma once

class DungeonInfo : public singleton<DungeonInfo>
{
	public:
		DungeonInfo();
		~DungeonInfo();
	
	bool    IsValidTeleportLocation(int x, int y) const;
	void	Update(LPCHARACTER ch);
};
#endif
#endif