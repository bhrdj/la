# nation kata idea 2023-02-11

# make a shooting star across the screen

import curses as c, random, sys

def main(my_screen):
    hgt, wdt = my_screen.getmaxyx()
    yx = [hgt//2, wdt//2]
    c.curs_set(0)
    my_screen.clear()
    my_screen.refresh()
    my_screen.addstr(hgt//2, wdt//2, 'b')
    k = my_screen.getkey()
    if k=='q': return None 

c.wrapper(main)
