import socket, sys, board, minimax

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 1060

def recv_all(sock,length):
	data = ''
	while len(data) < length:
		#print length - len(data)
		more = sock.recv(length - len(data))
		if not more:
			raise EOFError('sock closed {l} bytes into a {l2}-byte message'.format(l=len(data), l2 = length))
		data += more
	return data

def end_game(board, turn):
	if board.check_victory():
		print 'player',turn,'won'
		return True
	elif board.check_tie():
		print 'tie'
		return True
	else:
		return False

s.connect((HOST,PORT))
board = board.Board()
turn = board.turn

while True:
	print board
	input_var = raw_input(board.turn + " Enter [row, col]: ")
	if board.place_char(*[int(x.strip()) for x in input_var.split(',')]):
		print board
		s.sendall(board.to_string())
		turn = board.turn
		reply = recv_all(s,9)
		board.from_string(reply)
		if end_game(board, turn):
			print board
			break
s.close()