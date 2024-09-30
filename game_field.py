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


def put_mine():
    board = create_board()
    total_count = 0
    while total_count < 60:
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
                        board[random_row_number][s] = "mine"
    return board


def put_bush():
    board = put_mine()
    total_count = 0
    while total_count < 60:
        value = True
        while value:
            random_row_number = random.randint(0, 24)
            if random_row_number > 1:
                value = False
        for i in range(25):
            if i == random_row_number:
                random_col_number = 50
                count = 0
                while random_col_number > 47:
                    random_col_number = random.randint(1, 49)
                for k in range(random_col_number, random_col_number + 3):
                    if board[random_row_number][k] == "FREE" or "mine" \
                            and board[random_row_number + 1] == "FREE" or "mine":
                        count += 1
                        total_count += 1
                if count == 3:
                    total_count += 1
                    for s in range(random_col_number, random_col_number + 3):
                        board[random_row_number + 1][s] = "bush"
                        board[random_row_number][s] = "bush"
    return board
