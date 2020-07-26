from board import Board

if __name__ == '__main__':
    b = Board()
    print(b)
    #print(b.get_white_pieces())
    #print(b.get_black_pieces())
    print('White', len(b.get_white_moves()))
    print('Black', len(b.get_black_moves()))
