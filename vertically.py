#!/usr/bin/env python

import curses
import shutil
import time

def get_terminal_size():
    try:
        columns, lines = shutil.get_terminal_size()
    except:
        lines, columns = 25, 80  # Default size
    return columns, lines

def initialize_screen():
    stdscr = curses.initscr()
    curses.curs_set(0)
    return stdscr

def cleanup(stdscr):
    curses.endwin()
    exit(0)

stdscr = initialize_screen()
curses.start_color()
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)

term_width, term_height = get_terminal_size()

computers_x, computers_y, computers_dir = 0, 2, 1
computers_dir = -1  # Change initial direction to move the computers up

computers = r"""
                                                           
   _______________                        |*\_/*|________ 
  |  ___________  |     .-.     .-.      ||_/-\_|______  | 
  | |           | |    .****. .****.     | |           | | 
  | |   0   0   | |    .*****.*****.     | |   0   0   | | 
  | |     -     | |     .*********.      | |     -     | | 
  | |   \___/   | |      .*******.       | |   \___/   | | 
  | |___     ___| |       .*****.        | |___________| | 
  |_____|\_/|_____|        .***.         |_______________| 
    _|__|/ \|_|_.............*.............._|________|_  
   / ********** \                          / ********** \  
 /  ************  \                      /  ************  \ 
                                                            
"""

def is_position_empty(x, y):
    return stdscr.inch(y, x) == ord(' ')

def draw_computers(x, y, text):
    for i, line in enumerate(text.split("\n")):
        for j, char in enumerate(line):
            if 0 <= x + j < term_width and 0 <= y + i < term_height:
                stdscr.addch(y + i, x + j, char, curses.color_pair(4) | curses.A_BOLD)

try:
    while True:
        new_term_width, new_term_height = get_terminal_size()
        if new_term_width != term_width or new_term_height != term_height:
            term_width, term_height = new_term_width, new_term_height
            stdscr.clear()

        computers_y += computers_dir

        if computers_y + len(computers.split("\n")) >= term_height - 1:
            computers_dir = -1

        if computers_y <= 0:
            computers_dir = 1

        draw_computers(computers_x, computers_y, computers)

        stdscr.refresh()
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    cleanup(stdscr)

