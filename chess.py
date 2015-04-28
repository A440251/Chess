#Chess, for learning purposes. By /u/A440251.
#TODO: work on the king_in_check logic. After that, work on START_2P
#       ----> Learn how to deal with the out of range stuff. Filter that out
#             Also clean up the black_king_in_check() somewhat.
#             Do I really need to have seperate functions for black and white?
"""
Welcome to Chess!

Please input an answer:

An answer of "!STARTAI will play against the computer.
An answer of "!START2P will start a game for two players.
An answer of !QUIT" will quit the game.

"""

#White pieces are designated by lower case letters
#Black pieces are designated by upper case letters
initial_board =\
        [['R','N','B','Q','K','B','N','R'],
         ['P','P','P','P','P','P','P','P'],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         ['p','p','p','p','p','p','p','p'],
         ['r','n','b','q','k','b','n','r']]

pawn_check_board =\
        [['R','N','B','Q','K','B','N','R'],
         ['P','P','P','P','P','p','P','P'],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         ['p','p','p','p','p','p','p','p'],
         ['r','n','b','q','k','b','n','r']]

def create_chess_notation_to_dict(board):
    columns = "abcdefgh"
    rtn_dict = {}
    for column_no, column in enumerate(board):
        rtn_dict[columns[column_no]] = column_no
    for row_no, row in enumerate(board):
        rtn_dict[str(row_no+1)] = 7 - row_no
    return rtn_dict
the_dict = create_chess_notation_to_dict(initial_board)


def draw_board(board):
    for column_no, column in enumerate(board):
        print("|%s| %d"%("|".join(column), 8-column_no))
        #prints out each individiual square with the given piece, followed by
        #the row markers on the right.
    print(" a b c d e f g h ")





def move_piece(board):
    """Asks the user two different tiles (e4, c5, etc) and takes the first
    input as the initial board position and takes the second input as the final
    board position"""
    initial_square = input("From what square?")
    final_square = input("To what square?")
    
    #These assignments convert chess moves to list indexes
    initial_column = the_dict[initial_square[0]]
    initial_row = the_dict[initial_square[1]]
    final_column = the_dict[final_square[0]]
    final_row = the_dict[final_square[1]]

    #the string values for what is at the given board position
    starting_square = board[initial_row][initial_column]
    ending_square = board[final_row][final_column]

    #The logic that determines how a piece may move.
        

    #changing the value in the list that represents the board
    board[initial_row][initial_column] = ' '
    board[final_row][final_column] = starting_square

    draw_board(board)
    

    return board

def black_king_pos(board):
    """Determines the position of the black king and
    returns a tuple of the form (column_no, row_no)"""
    for column_no, column in enumerate(board):
        for row_no, row in enumerate(column):
            if column[row_no] == 'K':
                b_king_pos = (column_no, row_no)
                return b_king_pos
def white_king_pos(board):
    """Determines the position of the white king and
    returns a tuple of the form (column_no, row_no)"""
    for column_no, column in enumerate(board):
        for row_no, row in enumerate(column):
            if column[row_no] == 'k':
                w_king_pos = (column_no, row_no)
                return w_king_pos

def black_king_in_check(board):
    b_king_pos = black_king_pos(board)
    #The logic for the pawn checks
    if board[b_king_pos[0]+1][b_king_pos[1]-1] == "p" or\
       board[b_king_pos[0]+1][b_king_pos[1]+1] == "p":
           return True
    else:
        return False
    
            
def START_2P():
    """Starts a two-player game"""
    game_over = False
    whites_turn = True
    turn_number = 1
    draw_board(board)
    while not game_over:
        
        if whites_turn:
            if not white_king_in_check(board):
                turn_number += 1
                whites_turn = not whites_turn
        else:
            pass
def welcome():
    print(__doc__)

def main():
    done = False
    while not done:
        welcome()
        answer = input("What is your answer?\n...>")
        if answer.upper() == "!STARTAI":
            START_AI()
        if answer.upper() == "!START2P":
            START_2P()
        if answer.upper() == "!QUIT":
            break
    print("Thanks for playing Chess! Goodbye!")

"""
if __name__ == "__main__":
    main()
"""

def test_suite():
    print("draw the board")
    draw_board(initial_board)
    print("the black king starting position")
    _t1 = black_king_pos(initial_board)
    print(_t1)
    
    print("BKIC? should be true")
    _t2 = black_king_in_check(pawn_check_board)
    print(_t2)
    
    print("BKIC? should be false")
    _t3 = black_king_in_check(initial_board)
    print(_t3)

test_suite()
