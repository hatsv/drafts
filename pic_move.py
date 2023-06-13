#!/usr/bin/env python

import time
import shutil

pic = r"""
  /\ ___ /\
 (  o   o  ) 
  \  >#<  /
  /       \  
 /         \       ^
|           |     //
 \         /    //
  ///  ///   --
"""

while True:
    # Clear
    print("\033c", end="")

    # Get screen width
    screen_width = shutil.get_terminal_size().columns

    # Calculate picture position
    pic_width = max(len(line) for line in pic.splitlines())

    # Calculate the expanded gap size
    expansion_factor = 2  # Adjust this value to control the expansion
    expanded_gap_size = (screen_width - pic_width) // (2 * expansion_factor)

    # Calculate time-based position
    t = time.time()
    offset = int(t * 10) % (2 * expanded_gap_size)
    if offset >= expanded_gap_size:
        offset = 2 * expanded_gap_size - offset

    pic_x = expanded_gap_size + offset

    # Print picture
    for line in pic.splitlines():
        if 0 <= pic_x <= screen_width - len(line):
            print(" " * pic_x + line)

    # Time before updating the screen
    time.sleep(0.1)
