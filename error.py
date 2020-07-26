class NoKingFound(Exception):
    def __init__(self, ally):
        Exception.__init__(''.join([
            'No king found for ',
            'White' \
            if ally == 'W' \
            else 'Black',
            ' Player!'
        ]))

class TooManyKing(Exception):
    def __init__(self, ally):
        Exception.__init__(''.join([
            'Too many ',
            'king found for ',
            'White' \
            if ally == 'W' \
            else 'Black',
            ' Player!'
        ]))
