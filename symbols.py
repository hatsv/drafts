#!/usr/bin/env python

import curses
import random
import time

# Initialize curses
stdscr = curses.initscr()

# Turn off echoing of keypresses
curses.noecho()

# Turn off buffering of typed characters
curses.cbreak()

# Turn on the keypad for non-alphanumeric keys
stdscr.keypad(True)

# Turn on the cursor
curses.curs_set(0)

# Set the colors
curses.start_color()
curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

# Get the size of the screen
max_y, max_x = stdscr.getmaxyx()

# Set the starting positions and speeds of the stars
star_y1 = 0
star_x1 = random.randint(1, max_x-2)
star_speed1 = random.randint(1, 5)

star_y2 = 0
star_x2 = random.randint(1, max_x-2)
star_speed2 = random.randint(1, 5)

star_y3 = 0
star_x3 = random.randint(1, max_x-2)
star_speed3 = random.randint(1, 5)

# Loop while the program is running
while True:
    # Clear the screen
    stdscr.clear()

    # Move the symbols
    star_y1 += star_speed1
    star_y2 += star_speed2
    star_y3 += star_speed3

    # Reset the symbols if they fall off the bottom of the screen
    if star_y1 >= max_y-1:
        star_y1 = 0
        star_x1 = random.randint(1, max_x-2)
        star_speed1 = random.randint(1, 5)

    if star_y2 >= max_y-1:
        star_y2 = 0
        star_x2 = random.randint(1, max_x-2)
        star_speed2 = random.randint(1, 5)

    if star_y3 >= max_y-1:
        star_y3 = 0
        star_x3 = random.randint(1, max_x-2)
        star_speed3 = random.randint(1, 5)

    # Draw the stars
    stdscr.addstr(star_y1, star_x1, "*", curses.color_pair(1))
    stdscr.addstr(star_y2, star_x2, "*", curses.color_pair(1))
    stdscr.addstr(star_y3, star_x3, "*", curses.color_pair(1))

    # Refresh the screen
    stdscr.refresh()

    # Wait for a short time before updating the screen again
    time.sleep(0.05)

# End curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
