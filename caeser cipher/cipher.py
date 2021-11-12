from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter) + shift
            new_letter = alphabet[position % len(alphabet)]
            cipher_text += new_letter
        else:
            cipher_text += letter

    print(f"The encoded string is {cipher_text}")


def decode(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter) - shift
            new_letter = alphabet[position % len(alphabet)]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The decoded string is {cipher_text}")


user_choice = True
while user_choice:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == 'encode':
        encrypt(text, shift)
    else:
        decode(text, shift)

    choice = input("Print yes to continue and no to exit \n").lower()
    if choice == 'no':
        user_choice = False
        print("--------Bye Bye-------")
