#!/usr/bin/env python

import curses
import random
import time
import shutil

# Initialize the screen
stdscr = curses.initscr()
curses.start_color()  # Enable color support
curses.curs_set(0)    # Hide the cursor

try:
    # Generate random positions for the dots
    num_symbols = 150
    width, height = shutil.get_terminal_size()
    positions = []
    for i in range(num_symbols):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        positions.append((x, y))

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Initialize the default color pair

    color_timer = time.time()  # Initialize the timer

    while True:
        # Randomly select a subset of positions to blink
        blink_positions = random.sample(positions, num_symbols // 3)

        # Change color every 10 seconds
        if time.time() - color_timer >= 10:
            curses.init_pair(1, random.randint(1, curses.COLORS - 1), curses.COLOR_BLACK)  # Change the color pair
            color_timer = time.time()

        # Display dots
        for x, y in positions:
            # Check if the position is in the blink set
            if (x, y) in blink_positions:
                # Toggle visibility between showing and hiding
                stdscr.addstr(y, x, " " if stdscr.inch(y, x) == ord(".") else ".", curses.color_pair(1))
            else:
                stdscr.addstr(y, x, ".", curses.color_pair(1))

        # Screen refresh
        stdscr.refresh()
 
        curses.napms(150)

except KeyboardInterrupt:
    pass
# This ensures that the terminal is left in a usable state even if the program terminates unexpectedly
finally:
    curses.endwin()

