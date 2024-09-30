import random


def create_board():
    board = []
    spot = "FREE"
    for i in range(25):
        second_list = []
        for j in range(50):
            second_list.append(spot)
        board.append(second_list)
    return board


def put_man():
    board = create_board()
    for i in range(0, 5):
        for j in range(0, 2):
            if i < 3:
                board[i][j] = "body"
            else:
                board[i][j] = "leg"
    return board


def put_flag():
    board = put_man()
    for i in range(21, 25):
        for j in range(46, 50):
            if board[i][j] == board[21][46]:
                board[i][j] = "third flag"
            else:
                board[i][j] = "flag"
    return board


def put_mine():
    board = put_flag()
    total_count = 0
    while total_count < 20:
        random_row_number = random.randint(0, 24)
        for i in range(25):
            if i == random_row_number:
                random_col_number = 50
                count = 0
                while random_col_number > 47:
                    random_col_number = random.randint(1, 49)
                for k in range(random_col_number, random_col_number + 3):
                    if board[random_row_number][k] == "FREE":
                        count += 1
                if count == 3:
                    total_count += 1
                    for s in range(random_col_number, random_col_number + 3):
                        if random_col_number == s:
                            board[random_row_number][s] = "first mine"
                        else:
                            board[random_row_number][s] = "mine"

    return board

x = put_mine()
print(x)

def put_bush():
    board = put_mine()
    total_count = 0
    while total_count < 20:
        value = True
        while value:
            random_row_number = random.randint(0, 24)
            if random_row_number < 24:
                value = False
        for i in range(25):
            if i == random_row_number:
                random_col_number = 50
                count = 0
                while random_col_number > 47:
                    random_col_number = random.randint(1, 49)
                for k in range(random_col_number, random_col_number + 3):
                    if board[random_row_number][k] == "FREE" or "mine" and board[random_row_number + 1] == "FREE" or "mine":
                        count += 1
                        total_count += 1
                if count == 3:
                    total_count += 1
                    for s in range(random_col_number, random_col_number + 3):
                        if board[random_row_number + 1][s] == "mine":
                            board[random_row_number + 1][s] = "mine-bush"
                        else:
                            board[random_row_number + 1][s] = "bush"
                        if board[random_row_number][s] == "mine":
                            board[random_row_number][s] = "mine-bush"
                        else:
                            board[random_row_number][s] = "bush"
                        if s == random_col_number:
                            if "mine" in board[random_row_number][s]:
                                board[random_row_number][s] = "second mine_bush"
                            else:
                                board[random_row_number][s] = "second bush"
    return board


