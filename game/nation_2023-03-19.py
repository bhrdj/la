# nation kata idea 2023-02-11

# make a shooting star across the screen

import curses as c, sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stdout, **kwargs)

def main(my_screen):
    star = '*'
    hgt, wdt = my_screen.getmaxyx()
    yx = [hgt//2, 0] #wdt//2]
    akson = 'ກຂຄງຈສຊຍດຕຖທນບປຜຝພຟມຢຣລວຫອຮ'
    
    while True:
        my_screen.clear()
        try:
            my_screen.addstr(*yx, star)
        except Exception as err:
            sys.stdout.write('Cursor probably went off-screen')
            return None
        my_screen.refresh()
        k = my_screen.getkey()
        if k=='q': return None
        yx[1] = yx[1] + 1

c.wrapper(main)
