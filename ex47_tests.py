from nose.tools import *
from ex43.NewGame import door1


def test_room():
	gold = door1("GoldRoom",
		"""This room has gold in it you can grab. There's a
		door to the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})

def test_room_paths():
	center = door1("Center", "Test room in the center.")
	north = door1("North", "Test room in the north.")
	south = door1("South", "Test room in the south.")

	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)

def test_map():
	start = door1("Start", "You can go west and down a hole.")
	west = door1("Trees", "There are trees here, you can go east.")
	down = door1("Dungeon", "It's dark down here, you can go up.")

	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})

	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)
