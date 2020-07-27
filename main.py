from board import Board

if __name__ == '__main__':
    b = Board()
    print(b)
    #print(b.get_white_pieces())
    #print(b.get_black_pieces())
    print(b.white_player)
    print(b.black_player)

    from random import random
    from math import floor
    for i in range(3):
        ms = b.current_player.moves
        m = ms[floor(random() * len(ms))]
        b = m.execute()
        print('Executing', m)
        print(b)
