def get_score(board, player):
	if board.check_victory():
		return 1 if board.turn == player else -1
	elif board.check_tie():
		return 0
	elif board.turn == player:
		poss_boards = board.possible_boards
		return max([get_score(b, player) for b in poss_boards])
	else:
		poss_boards = board.possible_boards
		return min([get_score(b, player) for b in poss_boards])

def get_move(board):
	poss_boards = board.possible_boards
	bestscore = None
	bestboard = None
	for b in poss_boards:
		score = get_score(b, b.turn)
		if bestscore == None or score > bestscore:
			bestscore = score
			bestboard = b
	return board.find_diff(b)[0]