# Tic-Tac-Toe

A console-based Tic-Tac-Toe game in Python.

## Features

- **Two modes:** player vs player or player vs computer
- **Symbol choice:** X or O; press Enter for random selection
- **3×3 board:** enter a cell number from 1 to 9 to make a move
- **vs computer:** the computer plays by choosing a random free cell
- **Play again:** after each game you can start another round

## Requirements

- Python 3.6+

No external dependencies — only the standard library is used.

## Run

```bash
python tic_tac_toe.py
```

## How to play

1. Choose mode: `1` — two players, `2` — vs computer.
2. Enter player names (vs computer: only your name).
3. Choose symbol: `X`, `O`, or Enter for random.
4. Take turns entering a cell number (1–9). Cell layout:

   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```

5. The first to get three of their symbol in a row (horizontal, vertical, or diagonal) wins.
6. When asked "Play again?", type `y` or `n`.

## Project structure

```
tic-tac-toe/
├── tic_tac_toe.py   # main game code
└── README.md
```
License MIT
