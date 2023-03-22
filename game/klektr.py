# nation kata idea 2023-02-11

# make a shooting star across the screen

import curses as c, random, sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stdout, **kwargs)

def remove_quietly(lst,element):
    try:
        lst.remove(element)
    except:
        pass

def move(k, yx):
    if k=='KEY_UP':
        yx[0] = yx[0] - 1    
    elif k=='KEY_DOWN':
        yx[0] = yx[0] + 1    
    elif k=='KEY_LEFT':
        yx[1] = yx[1] - 1
    elif k=='KEY_RIGHT':
        yx[1] = yx[1] + 1    
    return yx

def main(my_screen):
    star = '*'
    hgt, wdt = my_screen.getmaxyx()
    yx = [hgt//2, 0] #wdt//2]
    akson = 'ກຂຄງຈສຊຍດຕຖທນບປຜຝພຟມຢຣລວຫອຮ'
    yx_akson = {}
    board0 = [(i,j) for i in range(2,hgt-1) for j in range(2,wdt-2)]
    for ak in akson:
        yx_akson[ak] = random.choice(board0)
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                remove_quietly(board0,(i,j))
    
    c.curs_set(0)
    while True:
        my_screen.clear()
        for ak in yx_akson:
            my_screen.addstr(*yx_akson[ak], ak)
        try:
            my_screen.addstr(*yx, star)   
        except Exception as err:
            sys.stdout.write('Cursor probably went off-screen')
            return None
        my_screen.refresh()
        k = my_screen.getkey()
        yx = move(k, yx)
        if k=='q': return None
        
c.wrapper(main)
