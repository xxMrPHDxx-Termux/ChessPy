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
    def __str__(self):
        pos, att = self.pos, self.attack()
        p,d,ap = self.__p, self.__d, self.__ap
        a, b = ('Attack', '=>') \
            if att \
            else ('', '->')
        c = f'{ap}{d}' if att else str(d)
        return a + \
            f'Move[{p}{pos}{b}{c}'
