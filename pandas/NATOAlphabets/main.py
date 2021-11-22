import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate():
    user_input = input("Enter the word: ").upper()
    try:
        output = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("No numbers! Enter alphabets please")
        generate()
    else:
        print(f"Your phonetic alphabets are {output}")


generate()

