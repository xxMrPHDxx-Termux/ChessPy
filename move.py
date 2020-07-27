class Move(object):
    def __init__(self, b, p, d, ap=None):
        self.__b = b
        self.__p = p
        self.__d = d
        self.__ap = ap
    @property
    def board(self): return self.__b
    @property
    def piece(self): return self.__p
    @property
    def dest(self): return self.__d
    @property
    def ap(self): return self.__ap
    @property
    def pos(self): return self.__p.pos
    def attack(self):
        return self.ap != None
    def execute(self):
        from board import Board
        config = [0 for i in range(64)]
        states = {}
        for p in self.__b.get_all_pieces():
            if p == self.ap:
                continue
            t = ' RNBQKP'.index(p.type)
            t *= 1 if p.is_white() else -1
            pos = self.dest \
                if p == self.piece \
                else p.pos
            config[pos] = t
            states[pos] = False \
                if p == self.piece \
                else p.fm
        return Board(
            config,
            'B' \
            if self.piece.ally == 'W' \
            else 'W',
            states
        )
    def __eq__(self, o):
        if not isinstance(o, Move):
            return False
        return all([
            self.piece == o.piece,
            self.ap == o.ap
        ])
    def __str__(self):
        pos, att = self.pos, self.attack()
        p,d,ap = self.__p, self.__d, self.__ap
        a, b = ('Attack', '=>') \
            if att \
            else ('', '->')
        c = f'{ap}{d}' if att else str(d)
        return a + \
            f'Move[{p}{pos}{b}{c}]'
