import terminal
import random

def possible_boards(current_board):
	empty_spots = current_board.unplayed_spots
	poss_boards = []
	for spot in empty_spots:
		new_board = terminal.Board(current_board.rows)
		new_board.place_char(spot[0],spot[1])
		poss_boards.append(new_board)
	return poss_boards

def final_boards(current_board):
	fin_boards = []
	if current_board.check_victory():
		turn = current_board.turn
		fin_boards.append((current_board,turn))
		return fin_boards
	elif current_board.turns_left == 0:
		fin_boards.append((current_board,'tie'))
		return fin_boards
	else:
		poss_boards = possible_boards(current_board)
		for board in poss_boards:
			fin_boards = fin_boards + final_boards(board)
	return fin_boards

def calc_util(end_states, player):
	outcomes = [end[1] for end in end_states]
	util = 0
	for result in outcomes:
		if result == 'tie':
			pass
		elif result == player:
			util += 1
		else: 
			util -= 1
	return util

def best_move(board):
	poss_boards = possible_boards(board)
	board_utils = []
	for board in poss_boards:
		ends = final_boards(board)
		util = calc_util(ends, board.turn)
		board_utils.append((board,util))
	best_next = best_move_helper(board_utils)
	row, col = best_next.find_diff(board)[0]
	return (row,col)

def best_move_helper(pairs):
	best = pairs[0][0]
	for pair in pairs:
		if pair[1] > best[1]:
			best = pair[0]
	return best

def random_move(board):
	empty_spots = board.unplayed_spots
	return empty_spots[random.randint(0,len(empty_spots))]

def play_game(num_humans):
    if num_humans == 1:
        while (True): 
            turn = my_board.turn
            print my_board
            if turn == 'O':
                #r,c = best_move(my_board)
                r,c = random_move(my_board)
                my_board.place_char(r,c)
            else: 
                input_var = raw_input(turn + " Enter [row, col]: ")
                my_board.place_char(*[int(x.strip()) for x in input_var.split(',')])
            if my_board.check_victory():
            	print my_board
            	print "player " + turn + " has won!"
            	break

if __name__ == '__main__':
    my_board = terminal.Board()
    play_game(1)
