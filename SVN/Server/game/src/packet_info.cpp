//find;

	Set(HEADER_CG_STATE_CHECKER, sizeof(BYTE), "ServerStateCheck", false);

//add below;

#ifdef ENABLE_DUNGEON_INFO_SYSTEM
	Set(HEADER_CG_TELEPORT, sizeof(TPacketGCTeleport), "TPacketGCTeleport", false);
#endif