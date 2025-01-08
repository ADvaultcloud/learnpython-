import random
print("Stone paper Scissor game")
print(" Lets start the Game..... ")
rock='''

_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)


'''

paper='''
_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissor='''
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
user_choice=int(input("What do you choose?Type 0 for rock,1 for paper,2 for scissor"))
if user_choice == 0:
    print("rock is what you choose",rock)
elif user_choice == 1:
    print("paper is what you choose",paper)
elif user_choice == 2:
    print("scissor is what you choose",scissor)
else:
    print("You choose the wrong input. You loose")

computers_choice=random.randint(0,2)
print("computer chooses ",computers_choice)
if computers_choice == 0:
    print("computer choice is",rock)
elif computers_choice == 1:
    print("computer choice is paper",paper)
elif computers_choice == 2:
    print("computer choice is scissor",scissor)

result=""
if computers_choice == user_choice:
    print("Its a Draw")
elif computers_choice == 2 and user_choice == 1:
    print("You Lose")
elif computers_choice == 2 and user_choice == 0:
    print("You Win")
elif computers_choice == 1 and user_choice == 0:
    print("You lose")   
elif computers_choice == 1 and user_choice == 2:
    print("You win")
elif computers_choice == 0 and user_choice == 1:
    print("You win")
elif computers_choice == 0 and user_choice == 2:
    print("You Lose")           