import curses
import time

x = "Editable String"
y = "2nd Editable String"

stdscr = curses.initscr()
stdscr.addstr(x + '\n')
stdscr.addstr(y + '\n')
stdscr.refresh()
time.sleep(3)

stdscr.erase()
stdscr.addstr("")
stdscr.addstr("")
stdscr.refresh()
time.sleep(3)

curses.endwin()
