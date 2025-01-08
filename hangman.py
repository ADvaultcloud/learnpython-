import random
stages= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print(" Welcome to the Game : HANGMAN ")
word_list=["python","linux","aws","docker","kubernetes","jenkins","ansible"]
lives=6
your_word=random.choice(word_list)
placeholder=""
word_length=len(your_word)
for letter in range(word_length):
    placeholder += "_ "
print(placeholder)    

game_over=False
correct_letters=[]
while not game_over:
    guess=input("Guess a letter-").lower()
    print(guess)

    display=""
    for letter in your_word:
        if letter==guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
               display += letter
        else:
            display += "_ " 
       
    print(display)
    if guess not in your_word:
        lives -= 1
        if lives==0:
            game_over=True
            print("You loose")

    if "_" not in display:
        game_over=True
        print("You Win")
    print(stages[lives])