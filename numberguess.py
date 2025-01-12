from random import randint
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5

def check_answer(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
        print("TOO High")
        return turns -1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns -1
    else:
        print(f"You got it ! The answer was{actual_answer}")    


def set_difficulty():
    level=input("Set a Difficulty: type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    print("Welcome to the Number Guessing Game")
    print("I am thinking of number  between '1' to '100' ")
    answer = randint(1 , 100)
    print(f"The correct answer is {answer} ")

    turns = set_difficulty()
  

    guess=0
    while guess != answer:
        print(f"You have {turns} attempts reamining to guess the number ")
        guess = int(input("Make a Guess:"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, You Loose")
            return
        elif guess != answer:
            print("Guess Again") 

game()