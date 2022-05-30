import random

class Chess:
    def __init__(self):
        self.cb = []

        self.black = 200
        self.white = 100

        self.pieces = {}

        self.piece_types = {
            10: 'pawn',
            20: 'bishop',
            30: 'knight',
            40: 'rook',
            50: 'queen',
            60: 'king'
        }

    def make_pieces(self):
        for clr in (100,200)):
            for t in piece_types:
                row = 0
                if clr == 100:
                    row = 8*7
                if t == 10:
                    for i in range(1, 9):
                        if clr == 100:
                            pieces[clr+t+i] = 8*6 + i
                        if clr == 200:
                            pieces[clr+t+i] = i+8
                
                if t == 20:
                    for i in (3,6):
                        pieces[clr+t+(i/3)] = row + i
                if t == 30:
                    for k, v in enumerate([2, 7]):
                        pieces[clr+t+(k+1)] = v + row
                if t == 40:
                    for k, v in enumerate([1, 8]):
                        pieces[clr+t+(k+1)] = v + row
                if t == 50:
                    pieces[clr+t+1] = row+4
                if t == 60:
                    pieces[clr+t+1] = row+5

    def valid_moves(self, piece):
        valid_moves = []
    pos = pieces[piece]
    string = str(piece)
    clr = int(string[0]) * 100
    typ = int(string[1]) * 10
    if typ == 10:
        sign = 1 if clr is 200 else -1
        check = ind
        check += 8*6 if clr == 100 else 8
        if pieces[piece] = check:
           valid_moves.append((pos+16) * sign) 
        val = (pos+8) * sign
        if val >= 1 and val <= 64:
            valid_moves.append(val)

    if typ == 20:
        row_pos = (pos % 8) - 1
        for i in range(row_pos):
            val = pos + (7*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
        for i in range(row_pos):
            val = pos + (-9*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
        for i in range(7-row_pos):
            val = pos + (9*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
        for i in range(7-row_pos):
            val = pos + (-7*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)

    if typ == 30:
        for i in (-17, 17, -15, 15, -10, 10, -6, 6):
            val = pos+i
            if val >= 1 and val <= 64:
                valid_moves.append(val)

    if typ == 40:
        row_pos = (pos%8) - 1
        col_pos = int((pos-1) / 8)
        for i in range(row_pos):
            valid_moves.append(pos - (i+1))
        for i in range(7-row_pos):
            valid_moves.append(pos - ((i+1) * -1))
        for i in range(col_pos):
            valid_moves.append(pos - (((i+1) * 8) * -1))
        for i in range(7-col_pos):
            valid_moves.append(pos - ((i+1) * 8))

    if typ == 50:
        
        row_pos = (pos%8) - 1
        col_pos = int((pos-1) / 8)

        #bishop like moves
        for i in range(row_pos):
            val = pos + (7*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
        for i in range(row_pos):
            val = pos + (-9*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
        for i in range(7-row_pos):
            val = pos + (9*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)
        for i in range(7-row_pos):
            val = pos + (-7*i)
            if val <= 64 and val >= 1:
                valid_moves.append(val)

        # rook like moves
        for i in range(row_pos):
            valid_moves.append(pos + (i+1))
        for i in range(7-row_pos):
            valid_moves.append(pos + ((i+1) * -1))
        for i in range(col_pos):
            valid_moves.append(pos + (((i+1) * 8) * -1))
        for i in range(7-col_pos):
            valid_moves.append(pos + ((i+1) * 8))

    if typ == 60:
        for i in (-9, -8, -7, -1, 1, 7, 8, 9):
            val = pos + i
            if val <= 64 and val >= 1:
                valid_moves.append(val)
    
    return valid_moves