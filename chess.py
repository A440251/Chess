#Chess, for learning purposes. By /u/A440251.
#TODO: figure out how to change the values of initial_board based on the
#      move that the user inputs. 


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
        rtn_dict[str(row_no+1)] = row_no
    return rtn_dict

the_dict = create_chess_notation_to_dict(initial_board)
print(the_dict)
print(the_dict['2'])
def move_piece(board):
    #TODO:
    #I definitely should be able to use enumerate() in some way to make all
    #these printing tasks easier.
    """Asks the user two different tiles (e4, c5, etc) and takes the first
    input as the initial board position and takes the second input as the final
    board position"""
    initial_square = input("From what square?")
    final_square = input("To what square?")
    initial_column = the_dict[initial_square[0]]
    print(initial_column, "initial_column")
    initial_row = the_dict[initial_square[1]]
    print(initial_row, "initial_row")
    final_column = the_dict[final_square[0]]
    print(final_column, "final_column")
    final_row = the_dict[final_square[1]]
    print(final_row, "final_row")
    starting_square = board[initial_column][initial_row]
    print(starting_square, "starting_square")
    ending_square = board[final_column][final_row]
    print(ending_square, "ending_square")
    new_board = starting_square.replace(starting_square, ' ')
    print(new_board, "new_board")
    #new_board = new_board.replace(new_board[final_column][final_row], starting_sqaure)
    #print(new_board, "new_board")
    

    return new_board


print(move_piece(initial_board))

