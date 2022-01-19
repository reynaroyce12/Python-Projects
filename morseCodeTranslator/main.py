from morseCode import *


def encrypt_text(text):
    encrypted_text = ''
    for letter in text:
        if letter != ' ':
            encrypted_text += MORSE_CODE_DICT[letter] + ' '
        else:
            encrypted_text += ' '

    return encrypted_text


def decrypt_text(text):
    decrypted_text = ''
    text_list = text.split(' ')
    for item in text_list:
        if item != '':
            decrypted_text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(item)]
        else:
            decrypted_text += ' '
            continue
    return decrypted_text.lower()


print("-------MORSE CODE TRANSLATOR-------")
print("1. Encrypt a text")
print("2. Decrypt a text")
print("3. Exit")

should_continue = True
while should_continue:
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        text_to_encrypt = input("Enter the text to convert: ").upper()
        print(f"The encrypted text is - {encrypt_text(text_to_encrypt)}")
    elif choice == 2:
        text_to_decrypt = input("Enter the text to decrypt: ").upper()
        print(f"The decrypted text is - {decrypt_text(text_to_decrypt)}")
    elif choice == 3:
        should_continue = False
        exit()
    else:
        print("Enter a valid choice :)")
