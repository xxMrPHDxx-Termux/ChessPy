from functools import reduce

from piece import Piece
from tile import Tile

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
        self.__wm, self.__bm = [], []
        def __cp(a, b):
            (
                a[1] 
                if b.is_white() 
                else a[0]
            ).append(b)
            [
                (
                    self.__wm \
                    if b.is_white() \
                    else self.__bm
                ).append(move)
                for move in b.calculate_moves(
                    self
                )
            ]
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
    def get_all_pieces(self):
        return [*self.__wp, *self.__bp]
    def get_white_moves(self):
        return self.__wm
    def get_black_moves(self):
        return self.__bm
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
