#print("Welcome to the Band Name Generator")
#city =input("Which city do you grow up in?\n")
"""pet=input("What is the name of your pet?\nhe")
print("Your band name could be -" + city + " " + pet)
-------------------xxxxxxxxxxxxxxxxx--------------------------
print("Welcome to the Tip Calculator")
bill = float(input("What was your Total bill-"))
tip = int(input("What percentage tip would you lik to give? 10 12 15")) 
numOfPeople=int(input("How many people to split the bill-"))
payableAmount=tip/100 * bill + bill
print(payableAmount)
individualPay=payableAmount/numOfPeople
print("Each person will have to pay" +str(individualPay))

----------------------------xxxxxxxxxxx--------------------
print("Welcome to Pizza Deliveries")
size=input("What size pizza would you want? S M L\n")
pepporoni=input("Do you want to add pepporoni?Y or N:\n")
extra_cheese=input("Do you want extra cheese?Y or N:\n")


#selecting size of pizza and adding price 
bill = 0

if size=="S":
    bill+= 15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("You Typed the wrong input \n please select from S M L")

if pepporoni=="Y":
    bill+=5
else: bill+=5
print("Please type the right choice Y or N")

if extra_cheese=="Y":
    bill+=2
else: bill+=0
print("Please type the right choice Y or N")


print("Your final bill is :${bill}")

import random
#random_int=random.randint(1,10)
#print(random_int)

#randomfloatnumber=random.random()
#print(randomfloatnumber)

randonflnum=random.uniform(5,15)
print(randonflnum)

"""
"""
------------------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx--------------------------------------
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
--------------------------------------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-------------------------------------
"""
"""
student_score=[36,48,66,88,66,55,44,77,99,67,58]
heighest_score = 0
for score in student_score:
    if score > heighest_score:
        heighest_score=score
print(heighest_score)
---------------------------------x--------x-x-x---------------x-------------------------------x-------------------
"""
import random
print("The Password Generator")
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


req_letters=int(input("How many letters would you want in your password?\n"))
req_numbers=int(input("How many numbers do you want in your password?\n"))
req_symbols=int(input("How many symbols do you want in your password?\n"))

#Easy level

password=""

for char in range(0,req_letters):
    password +=random.choice(letters)
   

for char in range(0,req_numbers):
    password +=random.choice(numbers)
   

for char in range(0,req_symbols):
    password +=random.choice(symbols)
  
print(password)
