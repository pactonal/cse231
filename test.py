#!/usr/bin/env python3
from checkers import Piece
import examples,tools
from proj10 import apply_move,indexify

Piece.symbols = ['b', 'w']
Piece.symbols_king = ['B', 'W']

board = examples.board_figure1()
board.place(1,2,Piece('white'))
board.place(6,1,Piece('black'))
print("Figure 1 board:")
board.display()

errmsg = "Invalid move, please type 'hints' to get suggestions."

#row,col = indexify(moves[0][0])
#moves = tools.get_moves(board, row, col)
#print("MOVES:",moves)
print("trying white pawn to king-row move: ('b3','a2')")
apply_move(board,('b3','a2'))
row,col = indexify('a2')
piece = board.get(row,col)
assert piece.is_king()
print("Success: white pawn made into king\n")

print("trying black pawn to king-row move: ('g2','h3')")
apply_move(board,('g2','h3'))
row,col = indexify('h3')
piece = board.get(row,col)
assert piece.is_king()
print("Success: black pawn made into king\n")

board.display()
correct = False
print("trying illegal move: ('a5','c6')")
try:
    apply_move(board, ('a5','c6'))
except Exception as err:
    print("Correct Exception message: \"{:s}\"".format(errmsg))
    print("Your Exception message: \"{:s}\"".format(str(err)))
    assert str(err) == errmsg
    correct = True
if not correct:
    print("Failed to raise exception with correct error message")
    assert False
