import random


# Lab 6 - Tic Tac Toe
def initialize():
    global board
    for i in range(3):
        board.append([" ", " ", " "])

    for i in range(9):
        squares_available.append(int(i + 1))

def play_game(board):
    x_o = 0

    input_times = 0
    while input_times < 9:
        if x_o == 1:
            print("COMPUTER TURN ")
            improved_random_move(board, "X")
            # make_random_move(board, "X")
            # print(squares_available)

            # Player 2 replaced by computer
            # x_number = input("Now Placing X: Which Square?")
            # while not valid_square(int(x_number)):
            #     x_number = input("Invalid Square Try Again!")
            # put_in_board(board, "X", square_num(int(x_number)))

        if x_o == 0:
            o_number = input("USER TURN (O): Which Square?")
            while not valid_square(int(o_number)):
                o_number = input("Invalid Square Try Again!")

            put_in_board(board, "O", square_num(int(o_number)))
            # print(squares_available)

        # Switching marks each time
        if x_o == 0:
            x_o = 1
        else:
            x_o = 0

        if is_win(board, "X"):
            print("X has won")
            input_times = 9

        if is_win(board, "O"):
            print("O has won")
            input_times = 9

        input_times += 1

        show_board(board)


def show_board(board):
    print("Current Board:")
    for i in range(3):
        print(str(board[i][0]), "|", str(board[i][1]), "|", str(board[i][2]))
        if i !=2:
            print("----------")


def valid_square(num):
    if num in squares_available:
        squares_available.sort()
        squares_available.remove(num)
        return True
    elif num > 9 or num < 1:
        return False
    else:
        return False


def square_num(square_number):
    row = (square_number - 1) // 3
    col = (square_number - 1) - (3 * ((square_number - 1) // 3))

    return [row, col]


def make_random_move(board, mark):
    choice = random.randrange(0, len(squares_available))
    number1 = squares_available[choice]
    squares_available.remove(number1)

    put_in_board(board, mark, square_num(number1))

# Part A
def improved_random_move(board, mark):
    # place a mark in every available spot and see if it wins. If not then make random move
    winning_move = False
    # squares_available_replica = squares_available

    for i in range(len(squares_available)):
        number = squares_available[i]
        squares_available.remove(number)
        put_in_board(board, mark, square_num(number))
        if is_win(board, mark):
            winning_move = True
            break
        else:
            board[square_num(number)[0]][square_num(number)[1]] = " "
            squares_available.append(number)
            squares_available.sort()

    if not winning_move:
        make_random_move(board, mark)


# Putting in the board
def put_in_board(board, mark, square_num):
    # Mark, "X" or "O"
    board[square_num[0]][square_num[1]] = mark


# Code to check if someone has won
def is_win(board, mark):
    # Checking Rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True

        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True

        # check diagonals top left to bottom right
        if board[0][0] == board[1][1] == board[2][2] == mark:
            return True

        # check diagonal top right to bottom left
        if board[0][2] == board[1][1] == board[2][0] == mark:
            return True


if __name__ == "__main__":
    board = []
    squares_available = []
    initialize()
    show_board(board)

    play_game(board)

    # Part 1 - User vs User

