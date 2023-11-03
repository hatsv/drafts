#!/usr/bin/env python

import curses
import random
import shutil
import time  # Import the time module

def get_terminal_size():
    try:
        columns, lines = shutil.get_terminal_size()
    except:
        lines, columns = 25, 80  # Default size
    return columns, lines

# Initialize the screen
stdscr = curses.initscr()
# Do not display cursor
curses.curs_set(0)

# Initialize color pairs
curses.start_color()
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

# Get terminal size
term_width, term_height = get_terminal_size()

planet_x, planet_y, planet_dir = 0, 2, 1

planet = r"""
                     .--------------.
                .---'  X        .    `---.
             .-'    .    X  .         .   `-.
          .-'     @@@@@@       .             `-.
        .'@@   @@@@@@@@@@@       @@@@@@@   .    `.
      .'@@@  @@@@@@@@@@@@@@     @@@@@@@@@         `.
     /@@@  X @@@@@@@@@@@@@@     @@@@@@@@@     X     \
    /        @@@@@@@@@@@@@@  @   @@@@@@@@@ @@     .  \
   /@  X      @@@@@@@@@@@   .  @@  @@@@@@@@@@@     @@ \
  /@@@      .   @@@@@@ X       @  @@@@@@@@@@@@@ X @@@@ \
 /@@@@@                  X .      @@@@@@@@@@@@@@  @@@@@ \
 |@@@@@    X    `.-./  .        .  @@@@@@@@@@@@@   @@@  |
/ @@@@@        --`-'       X        @@@@@@@@@@@ @@@    . \
|@ @@@@ .  X  X    `    @            @@      . @@@@@@    |
|   @@                         X    @@   .     @@@@@@    |
|  .     @   @ @       X              @@   X   @@@@@@.   |
\     @    @       @       .-.       @@@@       @@@      /
 |  @    @  @              `-'     . @@@@     .    .    |
 \ .  X       @  @@@@  .              @@  .           . /
  \      @@@    @@@@@@       .                   X     /
   \    @@@@@   @@\@@    /        X          .        /
    \ X  @@@       \ \  /  __        .   .     .--.  /
     \      .     . \.-.---                   `--'  /
      `.             `-'      .                   .'
        `.    X     / | `           X     .     .'
          `-.      /  |        X             .-'
             `-.          .         .     .-'
                `---.        .       .---'
                     `--------------'
"""

# Function to check if a position is empty
def is_position_empty(x, y):
    return stdscr.inch(y, x) == ord(' ')

# Function to draw the planet picture
def draw_planet(x, y, text):
    for i, line in enumerate(text.split("\n")):
        for j, char in enumerate(line):
            if 0 <= x + j < term_width and 0 <= y + i < term_height:
                stdscr.addch(y + i, x + j, char, curses.color_pair(4) | curses.A_BOLD)

try:
    while True:
        # Clear the screen
        stdscr.clear()

        # Move the planet picture
        planet_x += planet_dir

        # If the planet reaches the right border, change its direction to move left
        if planet_x + len(planet.split("\n")[0]) >= term_width - 1:
            planet_dir = -1

        # If the planet reaches the left border, change its direction to move right
        if planet_x <= 0:
            planet_dir = 1

        # Display the planet picture
        draw_planet(planet_x, planet_y, planet)

        # Refresh the screen
        stdscr.refresh()

        # Introduce a delay to slow down the movement
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    curses.endwin()

