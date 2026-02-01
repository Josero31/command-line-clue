#!/usr/bin/env python3
"""
Test suite for the Mystery Game to verify that the murder location
is the only empty room in the game.
"""

import unittest
from clue import MysteryGame


class TestMysteryGame(unittest.TestCase):
    """Tests for the MysteryGame class."""

    def test_only_murder_location_is_empty(self):
        """
        Test that the murder location is the ONLY empty room in the game.
        All other rooms should have at least one person OR one object.
        """
        # Run the test multiple times to account for randomness
        for _ in range(10):
            game = MysteryGame()
            game.generate_mystery(num_suspects=6, num_weapons=6)
            
            # Count empty rooms
            empty_rooms = []
            non_empty_rooms = []
            
            for room, contents in game.room_contents.items():
                is_empty = (len(contents["people"]) == 0 and 
                           len(contents["objects"]) == 0)
                if is_empty:
                    empty_rooms.append(room)
                else:
                    non_empty_rooms.append(room)
            
            # Assert there is exactly one empty room
            self.assertEqual(len(empty_rooms), 1, 
                           f"Expected exactly 1 empty room, but found {len(empty_rooms)}: {empty_rooms}")
            
            # Assert that empty room is the murder location
            self.assertEqual(empty_rooms[0], game.murder_location,
                           f"Empty room {empty_rooms[0]} is not the murder location {game.murder_location}")
            
            # Assert all other rooms have at least one item
            for room in non_empty_rooms:
                contents = game.room_contents[room]
                has_items = len(contents["people"]) > 0 or len(contents["objects"]) > 0
                self.assertTrue(has_items, 
                              f"Room {room} should have at least one item but is empty")

    def test_only_murder_location_is_empty_small_game(self):
        """
        Test with a smaller game (3 suspects, 3 weapons) to ensure the fix
        works with different game configurations.
        """
        for _ in range(10):
            game = MysteryGame()
            game.generate_mystery(num_suspects=3, num_weapons=3)
            
            empty_rooms = [room for room, contents in game.room_contents.items()
                          if len(contents["people"]) == 0 and len(contents["objects"]) == 0]
            
            # Should have exactly one empty room
            self.assertEqual(len(empty_rooms), 1,
                           f"Expected exactly 1 empty room, but found {len(empty_rooms)}")
            
            # That room should be the murder location
            self.assertEqual(empty_rooms[0], game.murder_location,
                           f"The only empty room should be the murder location")

    def test_murder_location_has_no_items(self):
        """
        Test that the murder location itself contains no people or objects.
        """
        for _ in range(10):
            game = MysteryGame()
            game.generate_mystery(num_suspects=6, num_weapons=6)
            
            murder_contents = game.room_contents[game.murder_location]
            self.assertEqual(len(murder_contents["people"]), 0,
                           f"Murder location should have no people")
            self.assertEqual(len(murder_contents["objects"]), 0,
                           f"Murder location should have no objects")

    def test_guilty_suspect_not_in_any_room(self):
        """
        Test that the guilty suspect does not appear in any room.
        """
        for _ in range(10):
            game = MysteryGame()
            game.generate_mystery(num_suspects=6, num_weapons=6)
            
            for room, contents in game.room_contents.items():
                self.assertNotIn(game.guilty_suspect, contents["people"],
                               f"Guilty suspect {game.guilty_suspect} should not be in room {room}")

    def test_murder_weapon_not_in_any_room(self):
        """
        Test that the murder weapon does not appear in any room.
        """
        for _ in range(10):
            game = MysteryGame()
            game.generate_mystery(num_suspects=6, num_weapons=6)
            
            for room, contents in game.room_contents.items():
                self.assertNotIn(game.murder_weapon, contents["objects"],
                               f"Murder weapon {game.murder_weapon} should not be in room {room}")


if __name__ == "__main__":
    unittest.main()
