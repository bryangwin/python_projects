
import pandas

words = pandas.read_csv("nato_phonetic_alphabet.csv")

words_dic = {row.letter: row.code for (index, row) in words.iterrows()}

user_word = input("Type a word: ").upper()

codes = [words_dic[letter] for letter in list(user_word)]

print(codes)
