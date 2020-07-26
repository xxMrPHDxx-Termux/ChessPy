from error import *

class Player(object):
    def __init__(self, a, b):
        self.__a = a
        self.__p = b.get_white_pieces() \
                if a == 'W' \
                else b.get_black_pieces()
        self.__m = b.get_white_moves() \
                if a == 'W' \
                else b.get_black_moves()
        self.__k = [
            p
            for p in self.pieces
            if p.type == 'K'
        ]
        if len(self.king) == 0:
            raise NoKingFound(self.ally)
        elif len(self.king) > 1:
            raise TooManyKing(self.ally)
        self.__k = self.king[0]
    @property
    def ally(self): return self.__a
    @property
    def pieces(self): return self.__p
    @property
    def moves(self): return self.__m
    @property
    def king(self): return self.__k
    def __str__(self):
        return (
            'White'
            if self.ally == 'W'
            else 'Black'
        ) + 'Player[Pieces={},Moves={}]'.format(
            len(self.pieces),
            len(self.moves)
        )
