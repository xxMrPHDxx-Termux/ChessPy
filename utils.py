from move import Move

def valid(pos):
    return pos > 0 and pos < 64

def get_moves(b, p, d, o, loop=False):
    while True:
        t = b[d]
        if not t.empty():
            ap = t.piece
            if ap.ally != p.ally:
                yield Move(b, p, d, ap)
            if loop:
                return
        else:
            yield Move(b, p, d)
        if not valid(d+o) or \
            p.has_exclusion(d, o) or \
            not loop:
                return
        d += o

class List(list):
    def __getitem__(self, arg):
        if type(arg) == tuple:
            return [
                self[idx]
                for idx in arg
            ]
        return list.__getitem__(self, arg)
