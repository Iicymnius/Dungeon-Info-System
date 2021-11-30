#find;

				## AtlasShowButton

#add above;

				# if app.ENABLE_DUNGEON_INFO_SYSTEM:
				{
					"name" : "l_button",
					"type" : "button",
					"x" : REAL_WIDTH-BOARD_WIDTH,
					"y" : 84,
					"default_image" : ROOT + "dungeon/1.png",
					"over_image" : ROOT + "dungeon/2.png",
					"down_image" : ROOT + "dungeon/3.png",
					"tooltip_text" : localeInfo.MINIMAP_DUNGEON_INFO,
				},