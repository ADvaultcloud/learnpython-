"""
#function parameters and arguments
def life_in_weeks(age):
    years_reamining = 90 - age
    weeks_reamining = years_reamining * 52
    print(f"You have {weeks_reamining} weeks left.")
life_in_weeks(12) 
#True love score
def calculate_love_score(name1,name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()
    
    t=lower_names.count("t")
    r=lower_names.count("r")
    u=lower_names.count("u")
    e=lower_names.count("e")
    first_digit=t+r+u+e
    
    l=lower_names.count("l")
    o=lower_names.count("o")
    v=lower_names.count("v")
    e=lower_names.count("e")
    last_digit=l+o+v+e

    score=int(str(first_digit) + str(last_digit))
    
    print(score)    
    
   """
should_continue=True
 
while should_continue:
    alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    choice=input('Type "encode" to encrypt the content, Type "decode" to decrypt the content \n').lower()
    text=input("Type your message \n").lower()
    shift=int(input("Type your shift number \n"))
    
    restart=input("Type 'yes' if you want continue decoding,or else type'no' \n").lower()
    if restart=="no":
        should_continue=False
        print("Goodbye")    


    if choice=="encode":
        def encrypt(given_text,shift_number):
            cipher_text=""
            for letter in given_text:
                shifted_position = alphabets.index(letter) + shift_number
                shifted_position %= len(alphabets)
                cipher_text += alphabets[shifted_position]

            print(f"Your encoded message is {cipher_text} ")
        encrypt(given_text=text,shift_number=shift)
    elif choice=="decode":
        def decrypt(given_text,shift_number):
            output_text=""
            for letter in given_text:
                shifted_position = alphabets.index(letter) - shift_number
                shifted_position %= len(alphabets)
                output_text += alphabets[shifted_position]
            print(f"Your decrypted message is {output_text} ")    
        decrypt(given_text=text,shift_number=shift)    
    else:
        print("wrong input!!! Type encode / decode")



"""

def ceasar():
    def decrypt(given_text,shift_number,encode_or_decode):
    output_text=""
    for letter in given_text:
        if letter not in alphabets:
            output_text += letter
        else:    
            if encode_or_decode == "decode":
                shift_number *=  -1
            shifted_position = alphabets.index(letter) - shift_number
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
    print(f"Your decrypted message is {output_text} ")    
ceasar(given_text=text,shift_number=shift,encode_or_decode=choice)    
"""
