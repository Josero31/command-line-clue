#!/usr/bin/env python3
from pathlib import Path

base_dir = Path("game")
test_path = base_dir / "school" / "classrooms" / "art room"

rel_path = str(test_path.relative_to(base_dir))
print(f"Relative path: '{rel_path}'")
print(f"Expected key in dict: '{rel_path}'")

# Test with backslash (Windows)
rel_path_backslash = rel_path.replace("/", "\\")
print(f"With backslashes: '{rel_path_backslash}'")
