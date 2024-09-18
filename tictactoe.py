"""
Tic Tac Toe Player
"""
import copy
import math


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    count = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                count += 1
    if count % 2 == 0:
        print(O)
        return O
    else:
        print(X)
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                empty_actions.add((i, j))
    print(empty_actions)
    return empty_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    win_state = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    for row in win_state:
        if [X, X, X] == row:
            return X
        if [O, O, O] == row:
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for row in board:
        if None in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return 1 if winner(board) == X else 0 if winner(board) is None else -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    max_val = float('-inf')
    min_val = float('inf')
    if player(board) == X:
        return eval_max(board, max_val, min_val)[1]
    else:
        return eval_min(board, max_val, min_val)[1]


def eval_max(board, max_val, min_val):
    move = None
    if terminal(board):
        return [utility(board), None]
    value = float('-inf')
    for action in actions(board):
        move_value = eval_min(result(board, action), max_val, min_val)[0]
        max_val = max(value, move_value)
        if move_value > value:
            move = action
            value = move_value
        if max_val >= min_val:
            break
    return [value, move]


def eval_min(board, max_val, min_val):
    move = None
    if terminal(board):
        return [utility(board), None]
    value = float('inf')
    for action in actions(board):
        move_value = eval_max(result(board, action), max_val, min_val)[0]
        min_val = min(value, move_value)
        if move_value < value:
            value = move_value
            move = action
        if max_val >=  min_val:
            break
    return [value, move]


if __name__ == "__main__":
    entry = [
        [X, None, None],
        [None, O, None],
        [None, None, X]
    ]
    print(winner(entry))
    print(terminal(entry))
    print(actions(entry))
    print(player(entry))
