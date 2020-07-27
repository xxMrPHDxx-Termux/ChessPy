from move import Move
from os import system

def valid(pos):
    return pos > 0 and pos < 64

def is_int(item):
    try:
        int(item)
        return True
    except:
        return False

def clear_screen():
    if system('cls') != 0:
        system('clear')

def get_moves(b, p, d, o, loop=False):
    while True:
        t = b[d]
        if not t.empty():
            ap = t.piece
            if ap.ally != p.ally \
                and p.type != 'P' \
                and abs(o)%8 != 0:
                yield Move(b, p, d, ap)
            if loop:
                return
        elif not (p.type == 'P' \
            and abs(o)%8 != 0):
            yield Move(b, p, d)
        if not valid(d+o) or \
            p.has_exclusion(d, o) or \
            not loop:
                return
        d += o

def create_move(b, f, t):
    m = [
        m
        for m in b.current_player.moves
        if m.pos == f and m.dest == t
    ]
    if len(m) != 1:
        print('Can\'t find that move!')
        return
    return m[0]

class List(list):
    def __getitem__(self, arg):
        if type(arg) == tuple:
            return [
                self[idx]
                for idx in arg
            ]
        return list.__getitem__(self, arg)
