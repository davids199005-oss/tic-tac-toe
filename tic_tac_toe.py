
import os
import random
import sys
import time

BOARD_SIZE = 3
CELLS_COUNT = BOARD_SIZE * BOARD_SIZE
SYMBOLS = ("X", "O")
COMPUTER_NAME = "Computer"

WIN_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def setup_game_mode():
    while True:
        choice = input(
            "Choose mode: 1 — play vs player, 2 — play vs computer: "
        ).strip()
        if choice == "1":
            return False
        if choice == "2":
            return True
        print("Enter 1 or 2.")


def setup_player_name(player_number):
    while True:
        name = input(f"Player {player_number}, enter your name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")


def setup_player_symbol(first_player_name):
    while True:
        choice = input(
            f"{first_player_name}, choose symbol (X or O), or Press Enter for random: "
        ).strip().upper()
        if choice in SYMBOLS:
            return choice
        if not choice or choice in ("R", "RANDOM"):
            symbol = random.choice(SYMBOLS)
            print(f"Symbol chosen: {symbol}.")
            return symbol
        print("Enter X, O, or press Enter for random.")


def setup_players(vs_computer):
    if vs_computer:
        print("Enter your name and choose your symbol.\n")
        name1 = setup_player_name(1)
        symbol1 = setup_player_symbol(name1)
        symbol2 = SYMBOLS[1] if symbol1 == SYMBOLS[0] else SYMBOLS[0]
        print(f"\n{name1} plays as {symbol1}, {COMPUTER_NAME} as {symbol2}.\n")
        return [(name1, symbol1), (COMPUTER_NAME, symbol2)]
    print("Enter names and choose symbols.\n")
    name1 = setup_player_name(1)
    symbol1 = setup_player_symbol(name1)
    symbol2 = SYMBOLS[1] if symbol1 == SYMBOLS[0] else SYMBOLS[0]
    name2 = setup_player_name(2)
    print(f"\n{name1} plays as {symbol1}, {name2} as {symbol2}.\n")
    return [(name1, symbol1), (name2, symbol2)]


def create_board():
    return [" "] * CELLS_COUNT


def display_board(board):
    print()
    for row in range(BOARD_SIZE):
        cells = []
        for col in range(BOARD_SIZE):
            index = row * BOARD_SIZE + col
            cell = board[index]
            cells.append(cell if cell != " " else str(index + 1))
        print(" | ".join(cells))
        if row < BOARD_SIZE - 1:
            print("-" * (BOARD_SIZE * 4 - 3))
    print()


def clear_console():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def setup_move(board, player_name, player_symbol):
    while True:
        try:
            raw = input(f"{player_name} ({player_symbol}), enter cell number (1-9): ").strip()
            if not raw:
                print("Enter a number from 1 to 9.")
                continue
            num = int(raw)
            if num < 1 or num > CELLS_COUNT:
                print(f"Number must be between 1 and {CELLS_COUNT}.")
                continue
            index = num - 1
            if board[index] != " ":
                print("That cell is already taken.")
                continue
            return index
        except ValueError:
            print("Enter a number from 1 to 9.")


def setup_available_moves(board):
    return [i for i in range(CELLS_COUNT) if board[i] == " "]


def setup_computer_move(board):
    moves = setup_available_moves(board)
    if not moves:
        raise RuntimeError("No available moves")
    return random.choice(moves)


def setup_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def setup_draw(board):
    if setup_winner(board) is not None:
        return False
    return " " not in board


def run_game(players, vs_computer):
    board = create_board()
    symbol_to_name = {symbol: name for name, symbol in players}
    current_index = 0

    while True:
        current_name, current_symbol = players[current_index]
        clear_console()
        display_board(board)

        if vs_computer and current_name == COMPUTER_NAME:
            print(f"{COMPUTER_NAME} is thinking...")
            time.sleep(0.8)
            index = setup_computer_move(board)
            print(f"{COMPUTER_NAME} chose cell {index + 1}.")
        else:
            index = setup_move(board, current_name, current_symbol)

        board[index] = current_symbol

        winner = setup_winner(board)
        if winner is not None:
            clear_console()
            display_board(board)
            print(f"{symbol_to_name[winner]} wins!")
            return

        if setup_draw(board):
            clear_console()
            display_board(board)
            print("It's a draw!")
            return

        current_index = 1 - current_index


def play_game():
    print("Welcome to Tic-Tac-Toe. Enter cell number (1-9) to move.\n")
    vs_computer = setup_game_mode()
    players = setup_players(vs_computer)
    while True:
        run_game(players, vs_computer)
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    play_game()
