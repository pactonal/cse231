#!/usr/bin/env python3
###############################################################################
#
#
#
#
#
#
###############################################################################
import tools
import gameai as ai
from checkers import Piece
from checkers import Board
import string

"""
    Write something about this program here.
"""


def indexify(position):
    """
    Write something about this function here.
    """
    ix = string.ascii_lowercase.find(position[0])
    iy = int(position[1:]) - 1

    return (ix, iy)


def deindexify(row, col):
    """
    Write something about this function here.
    """
    files = []
    for let in string.ascii_lowercase:
        files.append(let)
    cfile = files[row]
    rank = col + 1
    return (cfile + str(rank))


def initialize(board):
    """
    This function puts white and black pieces according to the checkers
    game positions. The black pieces will be on the top three rows and
    the white pieces will be on the bottom three rows (for an 8x8 board).
    The first row for the black pieces will be placed as a2, a4, a6, ...
    etc. and the next rows will be b1, b3, b5, ... etc. For the white
    rows, the placement patterns will be opposite of those of blacks.
    This must work for any even length board size.
    """

    row = col = board.get_length()
    initrows = (row // 2) - 1
    for r in range(row - 1, row - (initrows + 1), -1):
        for c in range(0 if r % 2 == 1 else 1, col, 2):
            board.place(r, c, Piece('white'))
    for r in range(0, initrows):
        for c in range(0 if r % 2 == 1 else 1, col, 2):
            board.place(r, c, Piece())


def count_pieces(board):
    """
    Write something about this function here.
    """
    wp = Piece('white')
    bp = Piece()
    wk = Piece('white', True)
    bk = Piece(is_king=True)
    white = 0
    black = 0
    for r in range(8):
        for c in range(8):
            if not board.is_free(r, c):
                if (str(board.get(r, c)) is str(wp) or
                        str(board.get(r, c)) is str(wk)):
                    white += 1
                elif (str(board.get(r, c)) is str(bp) or
                        str(board.get(r, c)) is str(bk)):
                    black += 1

    return (black, white)


def get_all_moves(board, color, is_sorted=False):
    """
    Write something about this function here.
    """
    moves = []
    piece = Piece(color)
    pieceK = Piece(color, True)
    for r in range(8):
        for c in range(8):
            if not board.is_free(r, c):
                if str(board.get(r, c)) is str(piece):
                    valid = tools.get_moves(board, r, c, True)
                    for move in valid:
                        tup = (deindexify(r, c), move)
                        moves.append(tup)
                elif str(board.get(r, c)) is str(pieceK):
                    valid = tools.get_moves(board, r, c, True)
                    for move in valid:
                        tup = (deindexify(r, c), move)
                        moves.append(tup)

    if is_sorted:
        moves.sort()

    return moves


def sort_captures(all_captures, is_sorted=False):
    '''If is_sorted flag is True then the final list will be sorted by the length
    of each sub-list and the sub-lists with the same length will be sorted
    again with respect to the first item in corresponding the sub-list,
    alphabetically.'''

    return sorted(all_captures, key=lambda x: (-len(x), x[0])) if is_sorted \
        else all_captures


def get_all_captures(board, color, is_sorted=False):
    """
    Write something about this function here.
    """
    captures = []
    piece = Piece(color)
    pieceK = Piece(color, True)
    for r in range(8):
        for c in range(8):
            if not board.is_free(r, c):
                if str(board.get(r, c)) is str(piece):
                    valid = tools.get_captures(board, r, c, True)
                    for lst in valid:
                        captures.append(lst)
                elif str(board.get(r, c)) is str(pieceK):
                    valid = tools.get_captures(board, r, c, True)
                    for lst in valid:
                        captures.append(lst)
    if is_sorted:
        sort_captures(captures, True)
    return captures


def apply_move(board, move):
    """
    Write something about this function here.

    Raise this exception below:
        raise RuntimeError("Invalid move, please type" \
                         + " \'hints\' to get suggestions.")
    If,
        a. there is no move from move[0], i.e. use tools.get_moves() function
           to get all the moves from move[0]
        b. the destination position move[1] is not in the moves list found
            from tools.get_moves() function.
    """
    wp = Piece('white')
    bp = Piece()
    wk = Piece('white', True)
    bk = Piece('black', True)
    loc = indexify(move[0])
    if str(board.get(loc[0], loc[1])) is str(wp):
        if move not in get_all_moves(board, 'white', True):
            raise RuntimeError(move_error)
        else:
            oldloc = loc
            newloc = indexify(move[1])
            if newloc[0] == 0:
                board.place(newloc[0], newloc[1], Piece('white', True))
                board.remove(oldloc[0], oldloc[1])
            else:
                board.place(newloc[0], newloc[1], Piece('white'))
                board.remove(oldloc[0], oldloc[1])
            board.remove(oldloc[0], oldloc[1])

    elif str(board.get(loc[0], loc[1])) is str(bp):
        if move not in get_all_moves(board, 'black', True):
            raise RuntimeError(move_error)
        else:
            oldloc = loc
            newloc = indexify(move[1])
            if newloc[0] == 7:
                board.place(newloc[0], newloc[1], Piece(is_king=True))
                board.remove(oldloc[0], oldloc[1])
            else:
                board.place(newloc[0], newloc[1], Piece())
                board.remove(oldloc[0], oldloc[1])

    elif str(board.get(loc[0], loc[1])) is str(wk):
        if move not in get_all_moves(board, 'white', True):
            raise RuntimeError(move_error)
        else:
            oldloc = loc
            newloc = indexify(move[1])
            board.place(newloc[0], newloc[1], Piece('white', True))
            board.remove(oldloc[0], oldloc[1])

    elif str(board.get(loc[0], loc[1])) is str(bk):
        if move not in get_all_moves(board, 'black', True):
            raise RuntimeError(move_error)
        else:
            oldloc = loc
            newloc = indexify(move[1])
            board.place(newloc[0], newloc[1], Piece(is_king=True))
            board.remove(oldloc[0], oldloc[1])
    else:
        raise RuntimeError(move_error)


def apply_capture(board, capture_path):
    """
    Write something about this function here.

    Raise this exception below:
        raise RuntimeError("Invalid jump/capture, please type" \
                         + " \'hints\' to get suggestions.")
    If,
        a. there is no jump found from any position in capture_path, i.e. use
            tools.get_jumps() function to get all the jumps from a certain
            position in capture_path
        b. the destination position from a jump is not in the jumps list found
            from tools.get_jumps() function.
    """
    wp = Piece('white')
    bp = Piece()
    wk = Piece('white', True)
    bk = Piece('black', True)
    loc = indexify(capture_path[0])
    if str(board.get(loc[0], loc[1])) is str(wp):
        for idx in range(0, len(capture_path) - 1):
            oldloc = indexify(capture_path[idx])
            if capture_path[idx + 1] in tools.get_jumps(board,
                                                        oldloc[0],
                                                        oldloc[1]):
                newloc = indexify(capture_path[idx + 1])
                caploc = ((oldloc[0] + newloc[0]) // 2,
                          (oldloc[1] + newloc[1]) // 2)

                if newloc[0] == 0:
                    board.place(newloc[0], newloc[1], Piece('white', True))
                    board.remove(oldloc[0], oldloc[1])
                    board.remove(caploc[0], caploc[1])
                else:
                    board.place(newloc[0], newloc[1], Piece('white'))
                    board.remove(oldloc[0], oldloc[1])
                    board.remove(caploc[0], caploc[1])

    elif str(board.get(loc[0], loc[1])) is str(bp):
        for idx in range(0, len(capture_path) - 1):
            oldloc = indexify(capture_path[idx])
            if capture_path[idx + 1] in tools.get_jumps(board,
                                                        oldloc[0],
                                                        oldloc[1]):
                newloc = indexify(capture_path[idx + 1])
                caploc = ((oldloc[0] + newloc[0]) // 2,
                          (oldloc[1] + newloc[1]) // 2)

                if newloc[0] == 7:
                    board.place(newloc[0], newloc[1], Piece(is_king=True))
                    board.remove(oldloc[0], oldloc[1])
                    board.remove(caploc[0], caploc[1])
                else:
                    board.place(newloc[0], newloc[1], Piece())
                    board.remove(oldloc[0], oldloc[1])
                    board.remove(caploc[0], caploc[1])

    elif str(board.get(loc[0], loc[1])) is str(wk):
        for idx in range(0, len(capture_path) - 1):
            oldloc = indexify(capture_path[idx])
            if capture_path[idx + 1] in tools.get_jumps(board,
                                                        oldloc[0],
                                                        oldloc[1]):
                newloc = indexify(capture_path[idx + 1])
                caploc = ((oldloc[0] + newloc[0]) // 2,
                          (oldloc[1] + newloc[1]) // 2)

                board.place(newloc[0], newloc[1], Piece('white', True))
                board.remove(oldloc[0], oldloc[1])
                board.remove(caploc[0], caploc[1])

    elif str(board.get(loc[0], loc[1])) is str(bk):
        for idx in range(0, len(capture_path) - 1):
            oldloc = indexify(capture_path[idx])
            if capture_path[idx + 1] in tools.get_jumps(board,
                                                        oldloc[0],
                                                        oldloc[1]):
                newloc = indexify(capture_path[idx + 1])
                caploc = ((oldloc[0] + newloc[0]) // 2,
                          (oldloc[1] + newloc[1]) // 2)

                board.place(newloc[0], newloc[1], Piece(is_king=True))
                board.remove(oldloc[0], oldloc[1])
                board.remove(caploc[0], caploc[1])

    else:
        raise RuntimeError(jump_error)


def get_hints(board, color, is_sorted=False):
    """
    Write something about this function here.
    """
    moves = get_all_moves(board, color, True)
    captures = get_all_captures(board, color, True)
    if len(captures) > 0:
        hint = ([], captures)
    elif len(moves) == 0 and len(captures) == 0:
        hint = ([], [])
    else:
        hint = (moves, captures)

    return hint


def get_winner(board, is_sorted=False):
    """
    Write something about this function here.
    """
    if len(get_hints(board, 'white', True)) == 0:
        return 'black'
    elif len(get_hints(board, 'black', True)) == 0:
        return 'white'
    elif count_pieces(board)[0] > count_pieces(board)[1]:
        return 'black'
    elif count_pieces(board)[0] < count_pieces(board)[1]:
        return 'white'
    else:
        return 'draw'


def is_game_finished(board, is_sorted=False):
    """
    Write something about this function here.
    """
    if ((len(get_hints(board, 'white')[0]) == 0 and
         len(get_hints(board, 'white')[1]) == 0) or
        (len(get_hints(board, 'black')[0]) == 0 and
         len(get_hints(board, 'black')[1]) == 0)):
            return True
    else:
        return False


# Some error messages to save lines.
move_error = "Invalid move, please type \'hints\' to get suggestions."
hasjump_error = "You have jumps, please type \'hints\' to get suggestions."
jump_error = "Invalid jump/capture, please type \'hints\' to get suggestions."
hint_error = "Invalid hint number."
cmd_error = "Invalid command."


def game_play_human():
    """
    This is the main mechanism of the human vs. human game play.
    Use this function to write the game_play_ai() function.
    """
    # UNCOMMENT THESE TWO LINES TO TEST ON MIMIR SUBMISSION
    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']

    prompt = "[{:s}'s turn] :> "
    print(tools.banner)

    # Choose the color here
    (my_color, opponent_color) = tools.choose_color()

    # Take a board of size 8x8
    board = Board(8)
    initialize(board)

    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'black' else opponent_color
    print("Black always plays first.\n")

    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)

            print("Current board:")
            board.display(piece_count)

            # Get the command from user using input
            command = input(prompt.format(turn)).strip().lower()

            # Now decide on different commands
            if command == 'pass':
                break
            elif command == 'exit':
                break
            elif command == 'hints':
                (moves, captures) = get_hints(board, turn, True)
                if moves:
                    print("You have moves:")
                    for i, move in enumerate(moves):
                        print("\t{:d}: {:s} --> {:s}"
                              .format(i + 1, move[0], move[1]))
                if captures:
                    print("You have captures:")
                    for i, path in enumerate(captures):
                        print("\t{:d}: {:s}".format(i + 1, str(path)))
            else:
                command = [s.strip().lower() for s in command.split()]
                (moves, captures) = get_hints(board, turn, True)
                action = None
                if command and command[0] == 'move' and len(command) == 3:
                    if not captures:
                        action = (command[1], command[2])
                        if action in moves:
                            apply_move(board, action)
                        else:
                            raise RuntimeError(move_error)
                    else:
                        raise RuntimeError(hasjump_error)
                elif command and command[0] == 'jump' and len(command) >= 3:
                    action = command[1:]
                    if action in captures:
                        apply_capture(board, action)
                    else:
                        raise RuntimeError(jump_error)
                elif command and command[0] == 'apply' and len(command) == 2:
                    id_hint = int(command[1])
                    if moves and (1 <= id_hint <= len(moves)):
                        action = moves[id_hint - 1]
                        apply_move(board, action)
                    elif captures and (1 <= id_hint <= len(captures)):
                        action = captures[id_hint - 1]
                        apply_capture(board, action)
                    else:
                        raise ValueError(hint_error)
                else:
                    raise RuntimeError(cmd_error + tools.usage)
                print("\t{:s} played {:s}.".format(turn, str(action)))
                turn = my_color if turn == opponent_color else opponent_color
        except Exception as err:
            print("Error:", err)

    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)
    if command != 'pass':
        winner = get_winner(board)
        if winner != 'draw':
            diff = abs(piece_count[0] - piece_count[1])
            print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
        else:
            print("This game ends in a draw.")
    else:
        winner = opponent_color if turn == my_color else my_color
        print("{:s} gave up! {:s} is the winner!! yay!!!".format(turn, winner))
    # --- end of game play human ---


def game_play_ai():
    """
    This is the main mechanism of the human vs. ai game play. You need to
    implement this function by taking helps from the game_play_human()
    function.

    For a given board situation/state, you can call the ai function to get
    the next best move, like this:

        move = ai.get_next_move(board, turn)

    where the turn variable is a color 'black' or 'white', also you need to
    import ai module as 'import gameai as ai' at the beginning of the file.
    This function will be very similar to game_play_human().
    """

    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']

    prompt = "[{:s}'s turn] :> "
    print(tools.banner)

    # Choose the color here
    (my_color, opponent_color) = tools.choose_color()

    # Take a board of size 8x8
    board = Board(8)
    initialize(board)

    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'black' else opponent_color
    print("Black always plays first.\n")

    # loop until the game is finished
    while not is_game_finished(board):
        try:
            if turn == opponent_color:
                piece_count = count_pieces(board)
                print("Current board:")
                board.display(piece_count)

                move = ai.get_next_move(board, turn)
                if type(move) is tuple:
                    apply_move(board, move)
                elif type(move) is list:
                    apply_capture(board, move)
                print("\t{:s} played {:s}.".format(turn, str(move)))
                piece_count = count_pieces(board)
                turn = my_color

            elif turn == my_color:
                piece_count = count_pieces(board)
                print("Current board:")
                board.display(piece_count)
                # Get the command from user using input
                command = input(prompt.format(turn)).strip().lower()

                # Now decide on different commands
                if command == 'pass':
                    break
                elif command == 'exit':
                    break
                elif command == 'hints':
                    (moves, captures) = get_hints(board, turn, True)
                    if moves:
                        print("You have moves:")
                        for i, move in enumerate(moves):
                            print("\t{:d}: {:s} --> {:s}"
                                  .format(i + 1, move[0], move[1]))
                    if captures:
                        print("You have captures:")
                        for i, path in enumerate(captures):
                            print("\t{:d}: {:s}".format(i + 1, str(path)))
                else:
                    command = [s.strip().lower() for s in command.split()]
                    (moves, captures) = get_hints(board, turn, True)
                    action = None
                    if command and command[0] == 'move' and len(command) == 3:
                        if not captures:
                            action = (command[1], command[2])
                            if action in moves:
                                apply_move(board, action)
                            else:
                                raise RuntimeError(move_error)
                        else:
                            raise RuntimeError(hasjump_error)
                    elif (command and command[0] == 'jump' and
                          len(command) >= 3):
                        action = command[1:]
                        if action in captures:
                            apply_capture(board, action)
                        else:
                            raise RuntimeError(jump_error)
                    elif (command and command[0] == 'apply' and
                          len(command) == 2):
                        id_hint = int(command[1])
                        if moves and (1 <= id_hint <= len(moves)):
                            action = moves[id_hint - 1]
                            apply_move(board, action)
                        elif captures and (1 <= id_hint <= len(captures)):
                            action = captures[id_hint - 1]
                            apply_capture(board, action)
                        else:
                            raise ValueError(hint_error)
                    else:
                        raise RuntimeError(cmd_error + tools.usage)
                    print("\t{:s} played {:s}.".format(turn, str(action)))
                    turn = opponent_color
        except Exception as err:
            print("Error:", err)

    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)
    if command != 'pass':
        winner = get_winner(board)
        if winner != 'draw':
            diff = abs(piece_count[0] - piece_count[1])
            print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
        else:
            print("This game ends in a draw.")
    else:
        winner = opponent_color if turn == my_color else my_color
        print("{:s} gave up! {:s} is the winner!! yay!!!".format(turn, winner))
    # --- end of game play ai ---


def main():
    # game_play_human()
    game_play_ai()


# main function, the program's entry point
if __name__ == "__main__":
    main()
