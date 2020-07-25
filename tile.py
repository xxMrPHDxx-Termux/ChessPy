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
        return str(self.piece)
