import minimax, board

my_board = board.Board()

my_board.place_char(0,2)
my_board.place_char(0,0)
my_board.place_char(2,2)
my_board.place_char(0,1)
my_board.place_char(1,0)
my_board.place_char(1,2)


board1 = board.Board(my_board.rows)
board2 = board.Board(my_board.rows)
board3 = board.Board(my_board.rows)

board1.place_char(1,1)
board2.place_char(2,1)
board3.place_char(2,0)

board4 = board.Board(board1.rows)
board4.place_char(2,1)

minimax.get_move(my_board)

def one_player():
	my_board = board.Board()
	while (True): 
	    turn = my_board.turn
	    print my_board
	    if turn == 'O':
	        r,c = minimax.get_move(my_board)
	        my_board.place_char(r,c)
	    else: 
	        input_var = raw_input(turn + " Enter [row, col]: ")
	        my_board.place_char(*[int(x.strip()) for x in input_var.split(',')])
	    if my_board.check_victory():
	    	print my_board
	    	print "player " + turn + " has won!"
	    	break
	    elif my_board.check_tie():
	    	print my_board
	    	print "tie"
	    	break

def two_player():
    my_board = board.Board()
    while (True):
        turn = my_board.turn
        print my_board
        input_var = raw_input(turn + " Enter [row, col]: ")
        my_board.place_char(*[int(x.strip()) for x in input_var.split(',')])
        if my_board.check_victory():
            print my_board
            print "player " + turn + " has won!"
            break
        elif my_board.check_tie():
            print my_board
            print "tie"
            break

# one_player()