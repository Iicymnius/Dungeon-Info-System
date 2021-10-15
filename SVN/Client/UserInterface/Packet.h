//find;

	HEADER_CG_SCRIPT_SELECT_ITEM = 114,

//add below;

#ifdef ENABLE_DUNGEON_INFO_SYSTEM
	HEADER_CG_TELEPORT = 122,//You may need to change the number 122 here.
#endif

//find again;

#pragma pack(pop)

//add above;

#ifdef ENABLE_DUNGEON_INFO_SYSTEM
typedef struct command_send_teleport
{
	BYTE	header;
	int		mapCoords[2];
}TPacketGCTeleport;
#endif