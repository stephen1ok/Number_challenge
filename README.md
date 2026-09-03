

## NUMBER CHALLENGE GAME

It is a Python command-line game where you try to guess a secret number chosen by the computer.

## HOW TO PLAY THE GAME 

1. Run the script : python Number_Challenge_Game.py
2. choose a difficulty : easy,medium, or hard.
3. guess a number between 1 and 50.
4. after each guess, the game tell you if it was too high or too low.
5. keep guessing untill you either:
6. type quit at any time to exit the game immediately.
7. after a round ends, you'll be asked if you want to play again.

## Difficulty levels

## difficulty        :     attemps
### easy              :     10
### medium            :    5
###  Hard             :   3


# 

- **Input validation** — rejects non-numeric guesses and asks again instead of crashing.
- **Quit anytime** — typing `quit` during a guess ends the game right away.
- **Replay loop** — play multiple rounds without restarting the script.
- **Clear feedback** — every guess gets a "too high," "too low," or "correct" response.
- **Attempt tracking** — shows how many attempts are left, and how many were used on a win.

## Concepts Practiced

- `if`, `elif`, `else` for decision-making
- Comparison operators (`==`, `<`, `>`)
- Logical checks with `.isdigit()` and `.lower()`
- `while` loops with `break`, `continue`, and `return`
- Functions and return values for controlling program flow

