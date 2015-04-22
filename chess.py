
def draw_board(board):
    #I need a better way of drawing the board. This is a lot of unecessary
    #typing, I feel.
    print("-----------------")
    print(("|%s|%s|%s|%s|%s|%s|%s|%s|  8") %
          (board[0][0], board[0][1], board[0][2],board[0][3], board[0][4],
           board[0][5],board[0][6], board[0][7]))
    print("-----------------")
    print(("|%s|%s|%s|%s|%s|%s|%s|%s|  7") %
          (board[1][0], board[1][1], board[1][2],board[1][3], board[1][4],
           board[1][5],board[1][6], board[1][7]))
    print("-----------------")
    print(("|%s|%s|%s|%s|%s|%s|%s|%s|  6") %
          (board[2][0], board[2][1], board[2][2],board[2][3], board[2][4],
           board[2][5],board[2][6], board[2][7]))
    print("-----------------")
    print(("|%s|%s|%s|%s|%s|%s|%s|%s|  5") %
          (board[3][0], board[3][1], board[3][2],board[3][3], board[3][4],
           board[3][5],board[3][6], board[3][7]))
    print("-----------------")
    print(("|%s|%s|%s|%s|%s|%s|%s|%s|  4") %
          (board[4][0], board[4][1], board[4][2],board[4][3], board[4][4],
           board[4][5],board[4][6], board[4][7]))
    print("-----------------")
    print(("|%s|%s|%s|%s|%s|%s|%s|%s|  3") %
          (board[5][0], board[5][1], board[5][2],board[5][3], board[5][4],
           board[5][5],board[5][6], board[5][7]))
    print("-----------------")
    print(("|%s|%s|%s|%s|%s|%s|%s|%s|  2") %
          (board[6][0], board[6][1], board[6][2],board[6][3], board[6][4],
           board[6][5],board[6][6], board[6][7]))
    print("-----------------")
    print(("|%s|%s|%s|%s|%s|%s|%s|%s|  1") %
          (board[7][0], board[7][1], board[7][2],board[7][3], board[7][4],
           board[7][5],board[7][6], board[7][7]))
    print("-----------------")
    print(" a b c d e f g h ")

chess_notation_to_list = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7}
def move_piece(board):
    """Takes as input two different tiles (e4, c5, etc) and takes the first
    input as the initial board position and takes the second input as the final
    board position"""
    initial_square = input("From what square?")
    final_square = input("To what square?")
    initial_index_one = chess_notation_to_list[initial_square[0]]
    initial_index_two = chess_notation_to_list[initial_square[1]]
    final_index_one = chess_notation_to_list[final_square[0]]
    final_index_two = chess_notation_to_list[final_square[1]]
    return (initial_index_one, initial_index_two,
            final_index_one, final_index_two)
#My tests:
initial_board = [['R','N','B','Q','K','B','N','R'],
         ['P','P','P','P','P','P','P','P'],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         ['p','p','p','p','p','p','p','p'],
         ['r','n','b','q','k','b','n','r']]
draw_board(initial_board)
print(move_piece(initial_board))

