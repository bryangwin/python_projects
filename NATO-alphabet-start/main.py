import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

letter_dic = {row.letter:row.code for (index, row) in nato.iterrows()}



def gen_phonetic():
    word_to_code = input("Enter a word: ").upper()
    try:
        code_list = [letter_dic[letter] for letter in word_to_code]
    except KeyError:
        print("Sorry, letters only.")
        gen_phonetic()
    else:
        print(code_list)

gen_phonetic()