alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #Alphabet duplicated - for shifting of letters at end of alphabet. 

from art import logo
print(logo)

def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if direction == "decrypt":
        shift_amount*=-1 # for decrypting
    for char in start_text: #encrypting starts from here
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result : {end_text}")

flag = False    
while not flag:
    direction = input(f"Type 'encode' to encrypt, to decode to 'decrypt'- ")
    text = input(f"Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26 #if shift number is greater than 26

    caesar(text,shift,direction)

    restart = input(" Type 'yes' if you want to go again. Otherwise type 'no'. \n ").lower()
    if restart == "no":
        flag = True
        print("Goodbye")

