from board import Board

def strs(arr):
    return [str(i) for i in arr]

if __name__ == '__main__':
    b = Board()
    print(b)
    #print(b.get_white_pieces())
    #print(b.get_black_pieces())
    print(strs(b.get_white_moves()))
    print(strs(b.get_black_moves()))
