import socket, sys, board, minimax, select


def recv_all(sock,length):
	data = ''
	while len(data) < length:
		#print length - len(data)
		more = sock.recv(length - len(data))
		if not more:
			raise EOFError('sock closed {l} bytes into a {l2}-byte message'.format(l=len(data), l2 = length))
		data += more
	return data

def end_game(board):
	if board.check_victory():
		return True
	elif board.check_tie():
		return True
	else:
		return False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 1060
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(5)
input = [s,sys.stdin]

while True:
	inputready, outputready, exceptready = select.select(input,[],[])
	for sock in inputready:
		if sock == s:
			sc, sockname = s.accept()
			message = recv_all(sc,9)
			new_board = board.Board()
			new_board.from_string(message)
			r,c = minimax.get_move(new_board)
			new_board.place_char(r,c)
			sc.sendall(new_board.to_string())
			input.append(sc)
		elif sock == sys.stdin:
			junk = sys.stdin.readline()
			break
		else:
			message = recv_all(sock,9)
			if message:
				new_board = board.Board()
				new_board.from_string(message)
				if end_game(new_board):
					sock.sendall(message)
					sock.close()
					input.remove(sock)
				else:
					r,c = minimax.get_move(new_board)
					new_board.place_char(r,c)
					sock.sendall(new_board.to_string())
					if end_game(new_board):
						sock.close()
						input.remove(sock)
			else:
				sock.close()
				input.remove(sock)

s.close()
