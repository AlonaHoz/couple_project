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
    used_col_num = []
    for i in range(25):
        random_row_number = random.randint(0, 24)
        if i == random_row_number:
            random_col_number = 50
            count = 0
            while random_col_number > 47 and count == 3:
                random_col_number = random.randint(1, 50)
                for k in range(random_col_number, random_col_number + 3):
                    if board[random_row_number][k] == "FREE":
                        count += 1
            for s in range(random_col_number, random_col_number + 3):
                board[random_row_number][s] = f"mine{s}"
    return board


p = put_mine()
print(p)
