import itertools

BLANK_BOARD = ['   ',
               '   ',
               '   ']

PLAYER_SIGILS = ['O', 'X']

def all_same_nonspace(items):
    if items[0] == ' ':
        return False
    else:
        return all(x==items[0] for x in items)

class Board(object):
    def __init__(self, grid = None):
        if grid is None:
            self.rows = [list(row) for row in BLANK_BOARD]
        else: 
            self.rows = [list(row) for row in grid]
    turns_left = property(lambda self: len(self.unplayed_spots))
    turn = property(lambda self: PLAYER_SIGILS[self.turns_left%2])

    @property
    def columns(self):
        return zip(*self.rows)

    # how does this work?
    @property
    def diags(self):
       return zip(*[(row[i],row[2-i]) for i, row in enumerate(self.rows)])

    @property
    def unplayed_spots(self):
        return [(r,c)
            for r in range(3) for c in range(3)
            if self.rows[r][c] not in PLAYER_SIGILS
        ]

    def __str__(self):
        template = (
                '     |     |     \n'
                '  {}  |  {}  |  {}  \n'
                '     |     |     \n'
                '-----------------\n'
                '     |     |     \n'
                '  {}  |  {}  |  {}  \n'
                '     |     |     \n'
                '-----------------\n'
                '     |     |     \n'
                '  {}  |  {}  |  {}  \n'
                '     |     |     \n')
        return template.format(*[c for row in self.rows for c in row])

    def check_victory(self):
        return any(all_same_nonspace(comb) for 
            comb in itertools.chain(self.rows, self.columns, self.diags))
    def check_tie(self):
        return self.turns_left == 0 and not self.check_victory()

    def place_char (self, row, col):
        if self.rows[row][col] != ' ':
            print 'Invalid move. A player has already marked that spot'
        else: 
            self.rows[row][col] = self.turn

    def find_diff(self, next_board):
        diff = [(r,c)
            for r in range(3) for c in range(3)
            if next_board.rows[r][c] != self.rows[r][c]
        ]
        assert len(diff) == 1
        return diff

    @property
    def possible_boards(self):
        empty_spots = self.unplayed_spots
        poss_boards = []
        for spot in empty_spots:
            new_board = Board(self.rows)
            new_board.place_char(spot[0],spot[1])
            poss_boards.append(new_board)
        return poss_boards
