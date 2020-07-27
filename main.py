from board import Board
from utils import *

if __name__ == '__main__':
    b = Board()
    print(b)

    while True:
        try:
            cmd, *args = input('>> ') \
                    .lower().split()
        except:
            exit()
        if cmd in ['h', 'help']:
            print(open(
                'help.txt',
                'r',
                encoding='UTF-8'
            ).read())
        if cmd in ['cls', 'clear']:
            clear_screen()
        if cmd in ['q', 'quit']:
            break
        if cmd in ['m', 'move'] \
            and len(args) == 2 \
            and all([ 
                is_int(i) for i in args
            ]):
            move = create_move(b, *[
                int(arg)
                for arg in args
            ])
            if move != None:
                b = move.execute()
                clear_screen()
                print(b)
