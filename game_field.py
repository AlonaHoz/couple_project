def create_board():
    main_list = []
    for i in range(25):
        second_list = []
        for j in range(50):
            main_list.append(second_list)
            print(*main_list)


