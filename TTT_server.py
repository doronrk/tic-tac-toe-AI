import socket, sys, board, minimax, threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 1060

game_list = []

class Game(object):
	def __init__(self, s, b):
		self.sock = s
		self.board = b


def recv_all(sock,length):
	data = ''
	while len(data) < length:
		#print length - len(data)
		more = sock.recv(length - len(data))
		if not more:
			raise EOFError('sock closed {l} bytes into a {l2}-byte message'.format(l=len(data), l2 = length))
		data += more
	return data

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)


def end_game(board):
	if board.check_victory():
		return True
	elif board.check_tie():
		return True
	else:
		return False

def search_clients():
	while True:
		sc, sockname = s.accept()
		message = recv_all(sc,9)
		new_board = board.Board()
		new_board.from_string(message)
		new_game = Game(sc, new_board)
		game_list.append(new_game)

t = threading.Thread(target=search_clients)
t.daemon = True
t.start()

while True:
	for game in game_list:
		current_board = game.board
		current_socket = game.sock
		if end_game(current_board):
			current_socket.sendall(current_board.to_string())
			current_socket.close()
			game_list.remove(game)
		else:
			r,c = minimax.get_move(current_board)
			current_board.place_char(r,c)
			current_socket.sendall(current_board.to_string())
			if end_game(current_board):
				current_socket.close()
				game_list.remove(game)
			else:
				new = recv_all(current_socket, 9)
				current_board.from_string(new)

sc.close()
