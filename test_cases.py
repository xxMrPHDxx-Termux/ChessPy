from piece import Piece
from tile import Tile
from move import Move
from player import Player
from board import Board

b = Board()

def test_board_start():
    assert len(b.get_white_pieces()) == 16, \
        'Should have 16 white pieces'
    assert len(b.get_black_pieces()) == 16, \
        'Should have 16 black pieces'
    assert len(b.get_white_moves()) == 20, \
        'Should have 20 white moves'
    assert len(b.get_black_moves()) == 20, \
        'Should have 20 black moves'
    assert b.current_player.ally == 'W', \
        'Current player should be white'

def test_piece_compare():
    p1 = b[0].piece
    p2 = b[1].piece
    p3 = Piece('N', 'B', 1, True)
    assert p1 != p3, 'Should not equal'
    assert p2 == p3, 'Should be equal'
    assert p1 != p3, 'Should not equal'

def test_tile_compare():
    t1, t2 = b[0:2]
    t3 = Tile(1,Piece('N','B',1,True))
    assert t1 != t2, 'Should not equal'
    assert t2 == t3, 'Should be equal'
    assert t1 != t3, 'Should not equal'

def test_move_compare():
    p = b[1].piece
    m1 = [
        m
        for m in b.get_black_moves()
        if m.pos == 1 and m.dest == 16
    ]
    assert len(m1) == 1, \
        'Should only be 1 move found'
    m1 = m1[0]
    m2 = Move(b, p, 16)
    assert m1 == m2, 'Move __eq__ failed!'

def test_player_compare():
    p1 = b.white_player
    p2 = b.black_player
    p3 = Player('W', b)
    assert p1 != p2, 'Should not equal'
    assert p2 != p3, 'Should not equal'
    assert p1 == p3, 'Should be equal'

def test_board_compare():
    m = [
        m
        for m in b.current_player.moves
        if m.pos == 57 and m.dest == 40
    ]
    assert len(m) == 1, \
        'Should found 1 move only'
    b2 = m[0].execute()
    b3 = Board([
        -1,-2,-3,-4,-5,-3,-2,-1,
        *[-6 for _ in range(8)],
        *[0 for _ in range(24)],
         2, 0, 0, 0, 0, 0, 0, 0,
        *[ 6 for _ in range(8)],
         1, 0, 3, 4, 5, 3, 2, 1
    ],'B',{40:False})
    assert b != b2, 'Should not equal'
    assert b2 == b3, 'Should be equal'
    assert b != b3, 'Should not equal'

def test_move_execution():
    m = [
        m
        for m in b.current_player.moves
        if m.pos == 57 and m.dest == 40
    ]
    assert len(m) == 1, \
        'Should found 1 move only'
    m = m[0]
    b2 = m.execute()
    assert not b2[40].piece.fm, \
        'Should not be first move anymore'
