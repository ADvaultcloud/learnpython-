
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

#password=""

"""for char in range(0,req_letters):
    password +=random.choice(letters)
   

for char in range(0,req_numbers):
    password +=random.choice(numbers)
   

for char in range(0,req_symbols):
    password +=random.choice(symbols)
  
print(password)
"""
#hard level
password_list=[]
for char in range(0,req_letters):
    password_list.append(random.choice(letters))
   
for char in range(0,req_numbers):
    password_list.append(random.choice(numbers))
   
for char in range(0,req_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
print(password_list)


pwd ="".join(password_list)#concatinate every element in list and makes a string
print(pwd)
#print("your password is -{pwd}")
print(f"Your password is -{pwd} ")
"""
password=""
for char in password_list:
    password += char
print(f"Your password is - {password}")
    
"""
