#Chess, for learning purposes. By /u/A440251.
#TODO: start adding rules for how a piece is allowed to move.


initial_board = [['R','N','B','Q','K','B','N','R'],
         ['P','P','P','P','P','P','P','P'],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         ['p','p','p','p','p','p','p','p'],
         ['r','n','b','q','k','b','n','r']]

def draw_board(board):
    #A great way to think about printing the board.
    #I'm going to comment this code to confirm I actually know what it does
    #instead of blindly copy and pasting.
    for column_no, column in enumerate(board):
        #enumerate is a great way to count indexes. Based on the size of the
        #board, column_no counts the columns and column is the representation
        #of what is in board[column_no]
        #https://docs.python.org/3/library/functions.html#enumerate
        print("|%s| %d"%("|".join(column), 8-column_no))
        #prints out each individiual square with the given piece, followed by
        #the row markers on the right.
    print(" a b c d e f g h ")
        #This marks the columns
    #Also, this looks better than what was submitted before. I don't think that
    #there is a need to add the other dashes.

draw_board(initial_board)

def create_chess_notation_to_dict(board):
    #Let's apply the same concept to this chess_notation_to_list dict.
    columns = "abcdefgh"
    rtn_dict = {}
    for column_no, column in enumerate(board):
        rtn_dict[columns[column_no]] = column_no
    for row_no, row in enumerate(board):
        rtn_dict[str(row_no+1)] = 7 - row_no
    return rtn_dict

the_dict = create_chess_notation_to_dict(initial_board)

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

    #changing the value in the list that represents the board
    board[initial_row][initial_column] = ' '
    board[final_row][final_column] = starting_square

    draw_board(board)
    

    return board


move_piece(initial_board)
