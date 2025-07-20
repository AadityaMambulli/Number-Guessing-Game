# Number Guessing Game

import random

def play_game():
    main_num = random.randint(1, 100)
    attempts = 0
    Score = 0
    is_running = True

    print("********************************")
    print("Number----Guessing----------Game")
    print("********************************")
    print("The range of the Number is 1-100")
    print("********************************")

    try:
        while True:
            guess = int(input("Enter Your Guess: "))
            attempts += 1
            if guess < main_num:
                print(" Too Low!!")
            elif guess > main_num:
                print(" Too High!!")
            else:
                print("You Win!!")
                print(f"You Won the game in '{attempts}' attempts")
                score = attempts * 2
                print(f"score :- {score}")
                break
    except ValueError:
        print("Please Enter a Valid Number")

if __name__ == '__main__':
    while True:
        play_game()
        play_again = input("Do You Want to Play Again (yes/no):- ").lower()
        if play_again == "no":
            print("Thanks For Playing!!!!!")
        else:
            continue


