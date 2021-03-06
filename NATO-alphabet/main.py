import pandas

# TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_data = {row.letter: row.code for (index, row) in data.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def get_input():
    user_input = input("Enter word: ")
    user_input = user_input.upper()
    try:
        answer = [new_data[ans] for ans in user_input]
    except KeyError:
        print("Please enter letter from the alphabet!!")
        get_input()
    else:
        print(answer)


get_input()
