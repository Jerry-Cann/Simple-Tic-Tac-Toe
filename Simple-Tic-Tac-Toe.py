def draw_board(coordinates_line):
    print("---------")
    print("|", coordinates_line[0], coordinates_line[1], coordinates_line[2], "|")
    print("|", coordinates_line[3], coordinates_line[4], coordinates_line[5], "|")
    print("|", coordinates_line[6], coordinates_line[7], coordinates_line[8], "|")
    print("---------")


def x_move(coordinates):
    global order_tracker
    coordinates = coordinates.split()
    if coordinates[0].isnumeric() and coordinates[1].isnumeric():
        coordinates = [int(coordinates[0]), int(coordinates[1])]
        if coordinates[0] > 3 or coordinates[1] > 3:
            print("Coordinates should be from 1 to 3!")
            x_move(input())
        elif board_state[(coordinates[1] - 1) + (coordinates[0] - 1) * 3] != "_":
            print("This cell is occupied! Choose another one!")
            x_move(input())
        else:
            board_state[(coordinates[1] - 1) + (coordinates[0] - 1) * 3] = "X"
            draw_board(board_state)
            order_tracker += 1
            gamestate_analyzer()
    else:
        print("You should enter numbers!")
        x_move(input())


def o_move(coordinates):
    global order_tracker
    coordinates = coordinates.split()
    if coordinates[0].isnumeric() and coordinates[1].isnumeric():
        coordinates = [int(coordinates[0]), int(coordinates[1])]
        if coordinates[0] > 3 or coordinates[1] > 3:
            print("Coordinates should be from 1 to 3!")
            o_move(input())
        elif board_state[(coordinates[1] - 1) + (coordinates[0] - 1) * 3] != "_":
            print("This cell is occupied! Choose another one!")
            o_move(input())
        else:
            board_state[(coordinates[1] - 1) + (coordinates[0] - 1) * 3] = "O"
            draw_board(board_state)
            order_tracker += 1
            gamestate_analyzer()
    else:
        print("You should enter numbers!")
        o_move(input())


def gamestate_analyzer():
    x_counter = 0
    o_counter = 0
    x_wins = False
    o_wins = False
    x_win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                          [0, 3, 6], [1, 4, 7], [2, 5, 8],
                          [0, 4, 8], [2, 4, 6]]
    o_win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                          [0, 3, 6], [1, 4, 7], [2, 5, 8],
                          [0, 4, 8], [2, 4, 6]]
    for i in range(0, 9):
        if board_state[i] == "X":
            x_counter += 1
        elif board_state[i] == "O":
            o_counter += 1
    for i in range(0, 8):
        if board_state[x_win_combinations[i][0]] == "X" and board_state[x_win_combinations[i][1]] == "X" and \
                board_state[x_win_combinations[i][2]] == "X":
            x_wins = True
        elif board_state[o_win_combinations[i][0]] == "O" and board_state[o_win_combinations[i][1]] == "O" and \
                board_state[o_win_combinations[i][2]] == "O":
            o_wins = True
    if x_wins:
        print("X wins")
    elif o_wins:
        print("O wins")
    elif x_counter + o_counter < 9:
        if order_tracker % 2 == 0:
            x_move(input())
        else:
            o_move(input())
    else:
        print("Draw")


board_state = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
order_tracker = 0
draw_board(board_state)
x_move(input())
