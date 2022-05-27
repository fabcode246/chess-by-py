import random

cb = []

black = 200
white = 100

pieces = {}

piece_types = {
        10: 'pawn',
        20: 'bishop',
        30: 'knight',
        40: 'rook',
        50: 'queen',
        60: 'king'
    }

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


def valid_moves(piece):
    valid_moves = []
    pos = pieces[piece]
    string = str(piece)
    clr = int(string[0]) * 100
    typ = int(string[1]) * 10
    ind = int(string[2])
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
        for sign in (1, -1):
            for i in range(row_pos):
                if sign == 1:
                    val = pos + ((i+1) * 7) * sign
                    if val >= 1 and val <= 64:
                        valid_moves.append(val)
                else:
                    val = (pos + ((i+1) * 9) * sign)
                    if val >= 1 and val <= 64:
                        valid_moves.append(val)
            for i in range(7-row_pos):
                if sign == -1:
                    val = (pos + ((i+1) * 7) * sign)
                    if val >= 1 and val <= 64:
                        valid_moves.append(val)
                else:
                    val pos + ((i+1) * 9) * sign)
                    if val >= 1 and val <= 64:
                        valid_moves.append(val)

    if typ == 30:
        for i in (-17, 17, -15, 15, -10, 10, -6, 6):
            val = pos+i
            if val >= 1 and val <= 64:
                valid_moves.append(val)

    if typ == 40:
        row_pos = (pos%8) - 1
        col_pos = int((pos-1) / 8)
        for i range(row_pos):
            pass
