def get_score(board, player):
	if board.check_victory():
		return 1 if board.turn == player else -1
	elif board.check_tie():
		return 0
	elif board.turn == player:
		poss_boards = board.possible_boards
		return max([get_score(b, b.turn) for b in poss_boards])
	else:
		poss_boards = board.possible_boards
		return min([get_score(b, b.turn) for b in poss_boards])

def get_move(board):
	print 'ORIGINAL BOARD\n', board
	print "_______________________________________\n\n"
	print 'BOARD OPTIONS\n'
	poss_boards = board.possible_boards
	bestscore = None
	bestboard = None
	for b in poss_boards:
		score = get_score(b, board.turn)
		print 'SCORE OF BOARD IS ', score,'\n', b
		if bestscore == None or score > bestscore:
			bestscore = score
			bestboard = b
	print "_______________________________________\n\n"
	print 'BEST BOARD\n',bestboard
	print 'BEST BOARD SCORE = ',bestscore
	return board.find_diff(bestboard)[0]