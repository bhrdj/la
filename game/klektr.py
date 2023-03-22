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

def move(k, yx, hgt, wdt):
    if k=='KEY_UP':
        yx[0] = yx[0] - 1
    elif k=='KEY_DOWN':
        yx[0] = yx[0] + 1
    elif k=='KEY_LEFT':
        yx[1] = yx[1] - 1
    elif k=='KEY_RIGHT':
        yx[1] = yx[1] + 1
    if yx[0] >= hgt: yx[0] = 1
    elif yx[0] <= 0: yx[0] = hgt-1
    if yx[1] >= wdt: x[1] = 1
    elif yx[1] <= 0: yx[1] = wdt-1
    return yx

def get_yx_akson(akson, hgt, wdt):
    board0 = [[i,j] for i in range(2,hgt-1) for j in range(2,wdt-2)]
    yx_akson = {}
    for ak in akson:
        yx_akson[ak] = random.choice(board0)
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                remove_quietly(board0,(i,j))
    return yx_akson

def main(my_screen):
    c.curs_set(0)
    star = '*'
    akson = 'ກຂຄງຈສຊຍດຕຖທນບປຜຝພຟມຢຣລວຫອຮ'
    hgt, wdt = my_screen.getmaxyx()
    yx = [hgt//2, 0] #wdt//2]
    yx_akson = get_yx_akson(akson, hgt, wdt)

    hgt, wdt = my_screen.getmaxyx() # This should be checked and reset during each loop
    while True:
        my_screen.clear()

        if yx in yx_akson.values():
            my_screen.addstr(hgt//2, wdt//2, 'b')
            yx_akson.pop('key', None)
        for ak in yx_akson:
            my_screen.addstr(*yx_akson[ak], ak)
        try:
            my_screen.addstr(*yx, star)
        except Exception as err:
            sys.stdout.write('Cursor probably went off-screen')
            return None

        my_screen.refresh()
        k = my_screen.getkey()
        yx = move(k, yx, hgt, wdt)
        if k=='q': return None

c.wrapper(main)
