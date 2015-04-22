#Chess, for learning purposes. By /u/A440251.
#TODO: work on the king_in_check logic. After that, work on START_2P
"""
Welcome to Chess!

Please input an answer:

An answer of "!STARTAI will play against the computer.
An answer of "!START2P will start a game for two players.
An answer of !QUIT" will quit the game.

"""
initial_board = [['R','N','B','Q','K','B','N','R'],
         ['P','P','P','P','P','P','P','P'],
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

def king_in_check(board):
    for column_no, column in enumerate(board):
        for row_no, row in enumerate(column):
            if column[row_no] == 'K':
                print(column_no, row_no)
            elif column[row_no] == 'k':
                print(column_no, row_no)
def START_2P():
    game_over = False
    whites_turn = True
    turn_number = 1
    draw_board(board)
    while not game_over:
        
        if whites_turn:
            if not king_in_check(board):
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
    draw_board(initial_board)
    king_in_check(initial_board)

test_suite()
