# tic-tac-toe-python

A two-player Tic Tac Toe game built in Python, playable in the terminal by two people sharing one computer.

This was my first milestone project while learning Python, and it brought together everything I'd learned up to this point — from the basics all the way through functions. I learned how to structure and write functions, how to integrate them with one another, and how to actually get them communicating correctly so they work together as one complete program, rather than as isolated pieces.

## Features

- Two players take turns choosing X or O
- The board is redisplayed after every move
- Input is validated — rejects non-numeric input, out-of-range positions, and already-taken spots
- Checks for a win across all 8 possible winning combinations (rows, columns, diagonals)
- Detects a tie when the board fills up with no winner

## How to run

python tic_tac_toe.py

Player 1 chooses X or O, Player 2 automatically gets the other symbol. Players then take turns entering a position (1-9, mapped to a numpad-style layout) to place their symbol.

## What I learned

- Writing and structuring functions, and getting them to work together as one complete program
- Input validation using nested loops
- How to reason about win conditions as a fixed set of index combinations rather than complex distance logic
- Debugging real issues as they came up, including off-by-one indexing errors and a Jupyter kernel-state bug where stale variables persisted between runs
- Using Git and GitHub to version and publish a project