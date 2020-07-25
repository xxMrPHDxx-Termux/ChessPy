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
    def __str__(self):
        return (
            (lambda x: x.lower())
            if self.ally == 'W'
            else lambda x: x
        )(self.type)

class Tile(object):
    def __init__(self, pos, piece=None):
        self._pos = pos
        self._piece = piece
    @property
    def pos(self): return self._pos
    @property
    def piece(self): return self._piece
    def empty(self):
        return self.piece == None
    def occupied(self):
        return not self.empty()
    def __str__(self):
        if self.empty():
            return '-'
        #print(self.piece)
        return str(self.piece)

class Board(object):
    DEFAULT = [
        -1,-2,-3,-4,-5,-3,-2,-1,
        -6,-6,-6,-6,-6,-6,-6,-6,
        *[0 for _ in range(32)],
         6, 6, 6, 6, 6, 6, 6, 6,
         1, 2, 3, 4, 5, 3, 2, 1
    ]
    def __init__(
            self, 
            cfg=DEFAULT,
            move_maker='W'):
        self.__tiles = [
            (
                lambda x: Tile(
                    i,
                    None
                    if x == 0
                    else Piece(
                        'RNBQKP'[abs(int(x))-1],
                        'WB'[
                            0 
                            if int(x) > 0
                            else 1
                        ],
                        i,
                        True
                    )
                )
            )(
                cfg[i]
                if i < len(cfg)
                else 0
            )
            for i in range(64)
        ]
        def __cp(a, b):
            (
                a[1] 
                if b.is_white() 
                else a[0]
            ).append(b)
            return a
        self.__wp, self.__bp = reduce(
            __cp,
            [
                t.piece
                for t in self.tiles
                if t.occupied()
            ],
            ([],[])
        )
    @property
    def tiles(self): return self.__tiles
    def get_white_pieces(self):
        return self.__wp
    def get_black_pieces(self):
        return self.__bp
    def __getitem__(self, arg):
        if type(arg) == tuple:
            r, c = arg
            return self.tiles[r*8+c]
        return self.tiles[arg]
    def __str__(self):
        return '\n'.join([
            ' '.join([
                f'{t}'
                for t in self.tiles[_*8:(_+1)*8]
            ]) for _ in range(8)
        ])

if __name__ == '__main__':
    b = Board()
    print(b.get_white_pieces())
    print(b.get_black_pieces())
