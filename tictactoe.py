"""
Tic Tac Toe Player
"""

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
    x_count=sum(row.count(X) for row in board)
    o_count=sum(row.count(O) for row in board)
    if x_count > o_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions=set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==None:
                possible_actions.add(i,j)
    
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j=action
    if board[i][j] is not EMPTY:
        raise Exception("invalid action")
    else:
        new_board=[row[:] for row in board]
        currentplayer=player(board)
    new_board[i][j]=currentplayer
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] is not None and row[0]==row[1]==row[2]:
            return row[0]
    for col in range(3):
        if board[0][col] is not None and board[0][col]==board[1][col]==board[2][col]:
            return board[0][col]
    if board[0][0] is not None and board[0][0]==board[1][1]==board[2][2]
     return board[0][0]
    if board[0][2] is not None and board[0][2]==board[1][1]==board[2][0]
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or not any( EMPTY in row for row in board)

    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win=winner(board)
    if win==X:
        return 1
    elif win==O:
        return -1
    else:
        return 0
    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current_player=player(board)
    if current_player==X:
        value,move=max_value(board)

    else:
        value,move=min_value(board)

def max_value(board):
    if terminal(board):
        return utility(board),None
    
    v=-math.inf
    best_action=None
    for action in actions(board):
        value,_=min_value(result(board,action))
        if value>v:
            v=value
            best_action=action  
    return v,best_action

def min_value(board):
    if terminal(board):
        return utility(board),None
    v=math.inf
    best_action=None
    for action in actions(board):
        value,_=max_value(result(board),action)
        if value<v:
            v=value
            best_action=action
    return value,best_action