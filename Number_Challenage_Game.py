

import random

def choose_difficulty():
    while True:
       choose = input ("enter easy, medium or hard:") 

       if choose == "easy":
          attempts = 10
          break
       elif choose == "medium":
           attempts = 5
           break
       elif choose == "hard":
           attempts = 3
           break
       else:
          print ("try again")
    
    return attempts                # it tells you how many attempts you have based on the difficulty level

def play_game():
    attempts = choose_difficulty()
    number = random.randint(1, 50)
    attempts_used = 0

    while attempts_used < attempts:
        guess = input("Guess a number (1, 50), type 'quit' to exit: ")
        
        if guess.lower() == "quit":
            print("Thanks for playing! Goodbye.")
            return "quit"                 # it tells you to quit

        if not guess.isdigit():
            print("Enter a valid number")
            continue

        guess = int(guess)
        attempts_used += 1

        if guess == number:
            print(f"Correct! you used {attempts_used} attempts")
            break
                              
        elif guess < number :     
            print("Too low")
        else:
            print("Too high")
        
        remaining = attempts - attempts_used
        if remaining == 0:
            print(f"No more attempts! the number was {number}")
        else:
            print(f"Attempts left: {remaining}")

def main():
    keep_playing = True
    
    while keep_playing:
        result = play_game()
        if result == "quit":
            keep_playing = False        # it tells you to quit the game
            continue
        again = input("play again? (yes/no): ")   
        if again.lower() not in ["yes", "y"]:
            keep_playing = False
            
    print("Game over.")
    
main()