#!/usr/bin/env python3
from clue import MysteryGame
import json

game = MysteryGame()
game.generate_mystery(3, 3)

print("=== GAME CONFIGURATION ===")
print(f"Suspects: {game.suspects}")
print(f"Weapons: {game.weapons}")
print(f"Guilty: {game.guilty_suspect}")
print(f"Murder weapon: {game.murder_weapon}")
print(f"Murder location: {game.murder_location}")
print(f"\nTotal rooms: {len(game.all_rooms)}")
print(f"Leaf rooms: {len(game._get_leaf_rooms())}")

print("\n=== ROOM CONTENTS ===")
for room, contents in sorted(game.room_contents.items()):
    people = contents.get("people", [])
    objects = contents.get("objects", [])
    if people or objects:
        print(f"{room}:")
        if people:
            print(f"  People: {people}")
        if objects:
            print(f"  Objects: {objects}")
