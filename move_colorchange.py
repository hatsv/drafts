#!/usr/bin/env python

import curses
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

# Initialize curses
stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()
for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, -1)  # Different text colors with a default background

curses.curs_set(0)  # Hide the cursor

try:
    while True:
        stdscr.clear()

        # Calculate the screen dimensions
        screen_height, screen_width = stdscr.getmaxyx()

        # Calculate pic position
        pic_height = len(pic.splitlines())
        pic_width = max(len(line) for line in pic.splitlines())

        # Calculate the expanded gap size
        expansion_factor = 1
        expanded_gap_size = (screen_width - pic_width) // (2 * expansion_factor)

        # Calculate time-based position
        t = time.time()
        offset = int(t * 10) % (2 * expanded_gap_size)
        if offset >= expanded_gap_size:
            offset = 2 * expanded_gap_size - offset

        pic_x = expanded_gap_size + offset
        pic_y = (screen_height - pic_height) // 2  # Center the picture vertically

        # Choose a color for the text symbols in the picture
        color_index = int(t) % curses.COLORS + 1

        # Print picture with the selected text color and a black background
        for i, line in enumerate(pic.splitlines()):
            if 0 <= pic_x <= screen_width - len(line):
                stdscr.addstr(pic_y + i, pic_x, line, curses.color_pair(color_index))

        stdscr.refresh()

        # Sleep for a short duration to control the color cycling
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

# Clean up and exit curses
curses.endwin()

