import random


def create_board():
    main_list = []
    for i in range(25):
        second_list = []
        for j in range(50):
            main_list.append(second_list)
            print(main_list)


create_board()


def put_mine():
    board = create_board()
    random_row_number = random.randint(1, 25)
    for i in range(25):
        random_col_number = 50
        if i == random_row_number:
            for j in range(50):
                while random_col_number > 47:
                    random_col_number = random.randint(1, 50)
                for s in range(random_col_number, random_col_number + 3):
                    board[random_row_number][s] = f"mine{s}"
