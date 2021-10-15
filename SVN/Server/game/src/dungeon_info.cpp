#include "../../common/service.h"
#ifdef ENABLE_DUNGEON_INFO_SYSTEM
#include "stdafx.h"
#include "constants.h"
#include "utils.h"
#include "desc.h"
#include "char.h"
#include "db.h"
#include "config.h"
#include "dungeon_info.h"
#include "affect.h"
#include "item.h"
#include "questmanager.h"
#include <boost/algorithm/string.hpp>

struct DungeonInfoTable {
	int type; // Dungeon type [ 0 (Unkown), 1 (Private), 2 (Global) ] Bizdeki dungeonlar bireysel oldu�u i�in 1 kullan�caks�n 1. veriyi
	int organization; // Dungeon organization [ 0 (None), 1 (Party), 2 (Guild) ] Bizdeki dungeonlar bireysel oldu�u i�in 0 kullan�caks�n 2. veriyi
	int min_level;  // Dungeon level limit [ min_level ] Burada zindan�n alt level limitini yaz�caks�n 3. veriye
	int party_members;  // Dungeon party members [ max_members (0) Unlimited ] Burada dungeona grubunla girebilecek max ki�i say�s�n� yaz�caks�n. 4. veriye
	int map_index;  // Dungeon map index // Dungeonun map indexini yaz�caks�n 5. veriye
	char map_name[64]; // Map Name // Zindan�n ismini yaz�caks�n 6. veriye
	char map_entrance[64]; // Map Name Entrance // Zindan�n giri� haritas�n�n ismini yaz�caks�n 7. veriye
	int map_coords[2]; // Map Coords (X,Y) // ���nlan tu�una bas�nca hangi koordinata ���nlans�n onu yaz�cak�n 8. veriye
	int cooldown;  // [ 0 (None) ] | Ex: 60 * 60 * 3 = 3 hours // So�uma s�resini yaz�caks�n 9. veriye saniye cinsi
	int duration;  // [ 0 (None) ] | Ex: 60 * 60 * 3 = 3 hours // Dungeonda en fazla ne kadar durabilir onun s�resini yaz�caks�n 10. veriye saniye cinsi
	int max_level; // Dungeon level min [ max_level ] //  Burada zindan�n �st level limitini yaz�caks�n 11. veriye
	int strength_bonus;  // Strength bonus id against dungeon monsters // Hangi bonus bu dungeon canavarlar�na kar�� g��l� bunun lenght.h 'taki kar��l��� 12. veriye 
	int resistance_bonus; // Resistance bonus id against dungeon monsters  // Hangi bonus bu dungeon canavarlar�na kar�� dayan�kl� bunun lenght.h 'taki kar��l��� 13. veriye
	int item_vnum;  // Required dungeon item // Dungeona girmek i�in gerekli e�yay� yazacaks�n 14. veriye
	int boss_vnum; // Boss Vnum // dungeonun bossu hangisiyse vnumunu yaz�caks�n 15. veriye
};

DungeonInfoTable dungeonTable[8] = { // Buradaki rakam� ka� tane dungeon girersen o say�y� yaz�caks�n.

	{1, 0, 40, 8 , 66, "�eytan Kulesi", "Hwang Tap�na��" , {5906, 1108}, 0, 3600 , 105, 22, 89, 0, 1093}, // Dungeon 0
	{1, 0, 55, 8 , 364, "Ork Zindan�", "Seungryong Vadisi" , {3352, 7549}, 900, 3600 , 75, 19, 88, 828, 694}, // Dungeon 1
	{1, 0, 55, 8 , 362, "�r�mcek Barones", "�r�mcek Zindan� 3.Kat" , {692, 6110}, 900, 3600 , 75, 116, 38, 30325, 2092}, // Dungeon 2
	{1, 0, 75, 8 , 79, "Mavi Ejderha", "S�rg�n Zindan� 2.Kat" , {1817, 12207}, 900, 3600 , 105, 105, 36, 30179, 2493}, // Dungeon 3
	{1, 0, 75, 8 , 216, "�eytan Katakombu", "Hwang Tap�na��" , {5919, 996}, 900, 3600 , 105, 22, 89, 30319, 2598}, // Dungeon 4
	{1, 0, 90, 8 , 351, "Razad�r", "Doyyumhwan" , {5998, 7075}, 900, 3600 , 105, 100, 35, 817, 6091}, // Dungeon 5
	{1, 0, 90, 8 , 352, "Nemere", "Sohan Da��" , {4324, 1648}, 900, 3600 , 105, 101, 87, 818, 6191}, // Dungeon 6
	{1, 0, 75, 8 , 55, "Paskalya Ma�aras�", "K�z�l Orman" , {11171, 535}, 0, 2400 , 105, 119, 120, 30787, 4103}, // Dungeon 6

};

DungeonInfo::DungeonInfo()
{
}

DungeonInfo::~DungeonInfo()
{
}

bool DungeonInfo::IsValidTeleportLocation(int x, int y) const
{
	for (const auto& entry : dungeonTable)
	{
		if (entry.map_coords[0] == x && entry.map_coords[1] == y)
			return true;
	}
	return false;
}

void DungeonInfo::Update(LPCHARACTER ch)
{
	if (ch == NULL)
		return;

	if (!ch->IsPC())
		return;

	if (sizeof(dungeonTable) == 0)
		return;

	ch->ChatPacket(CHAT_TYPE_COMMAND, "CleanDungeonInfo");
	int size = *(&dungeonTable + 1) - dungeonTable;
	for (int i = 0; i <= size - 1; i++)
	{
		std::string mapName(dungeonTable[i].map_name);
		boost::algorithm::replace_all(mapName, " ", "_");

		std::string mapEntrance(dungeonTable[i].map_entrance);
		boost::algorithm::replace_all(mapEntrance, " ", "_");

		ch->ChatPacket(CHAT_TYPE_COMMAND, "UpdateDungeonInfo %d %d %d %d %d %s %s %d %d %d %d %d %d %d %d %d %d %d %d",
			dungeonTable[i].type,
			dungeonTable[i].organization,
			dungeonTable[i].min_level,
			dungeonTable[i].party_members,
			dungeonTable[i].map_index,
			mapName.c_str(),
			mapEntrance.c_str(),
			dungeonTable[i].map_coords[0],
			dungeonTable[i].map_coords[1],
			dungeonTable[i].cooldown,
			dungeonTable[i].duration,
			dungeonTable[i].max_level,
			dungeonTable[i].strength_bonus,
			dungeonTable[i].resistance_bonus,
			dungeonTable[i].item_vnum,
			dungeonTable[i].boss_vnum
		);
	}
}
#endif