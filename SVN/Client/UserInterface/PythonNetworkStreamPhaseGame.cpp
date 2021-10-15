//add to bottom;

#ifdef ENABLE_DUNGEON_INFO_SYSTEM
bool CPythonNetworkStream::DungeonTeleport(DWORD coordX, DWORD coordY)
{
	if (!__CanActMainInstance())
		return true;

	TPacketGCTeleport p;
	p.header = HEADER_CG_TELEPORT;
	p.mapCoords[0] = coordX;
	p.mapCoords[1] = coordY;
	if (!Send(sizeof(TPacketGCTeleport), &p))
	{
		Tracen("DungeonTeleport Error");
		return false;
	}

	return SendSequence();
}
#endif