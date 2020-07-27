from functools import reduce

import utils

class Piece(object):
    def __init__(self, t, a, p, fm=True):
        self._type = t
        self._ally = a
        self._pos = p
        self._fm = fm
    @property
    def type(self): return self._type
    @property
    def ally(self): return self._ally
    @property
    def pos(self): return self._pos
    @property
    def fm(self): return self._fm
    def is_white(self):
        return self.ally == 'W'
    def is_black(self):
        return self.ally == 'B'
    def calculate_moves(self, b):
        t, a = self.type, self.ally
        if not t in 'RNBQKP':
            return []
        p = self.pos
        d = -1 if a == 'W' else 1
        if   t in 'QK':
            offs = [-9,-8,-7,-1,1,7,8,9]
        elif t == 'R':
            offs = [-8,-1,1,8]
        elif t == 'B':
            offs = [-9,-7,7,9]
        elif t == 'N':
            offs = [-17,-15,-10,-6,6,10,15,17]
        else:
            offs = [i*d for i in [7,8,9,16]]
        moves = [
            list(utils.get_moves(
                b, 
                self, 
                p+o, 
                o,
                t in 'RBQ'
            ))
            for o in offs
            if utils.valid(p+o)
            and not self.has_exclusion(p, o)
        ]
        return reduce(
            lambda a, b: [*a, *b],
            moves,
            []
        )
    def has_exclusion(self, p, o):
        t, d = self.type, p+o
        c, cc = p%8, d%8
        if not t in 'RNBQKP':
            return False
        b = 1 if t == 'N' else 0
        return abs(cc-c) > b
    def __eq__(self, o):
        if not isinstance(o, Piece):
            return False
        return all([
            self.type == o.type,
            self.ally == o.ally,
            self.pos == o.pos,
            self.fm == o.fm
        ])
    def __str__(self):
        return (
            (lambda x: x.lower())
            if self.ally == 'W'
            else lambda x: x
        )(self.type)


