
morse_code_alphabet = {"A": ".-",
     "B": "-...",
     "C": "-.-.",
     "D": "-..",
     "E": ".",
     "F": "..-.",
     "G": "--.",
     "H": "....",
     "I": "..",
     "J": ".---",
     "K": "-.-",
     "L": ".-..",
     "M": "--",
     "N": "-.",
     "O": "---",
     "P": ".--.",
     "Q": "--.-",
     "R": ".-.",
     "S": "...",
     "T": "-",
     "U": "..-",
     "W": ".--",
     "X": "-..-",
     "Y": "-.--",
     "Z": "--.."}
english_unicode = characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

latin_word = input("Write your text here to convert morse code. (Only use latin alphabet!)\n").upper()
splitted_list = [*latin_word]
sentence = ""
dont_start = 0

for letter in splitted_list:
     if letter in  english_unicode:
          pass
     elif letter not in english_unicode: 
          dont_start = 1
if dont_start == 0:
     for x in splitted_list:
          sentence = sentence + morse_code_alphabet[x]
     print(sentence)
else:
     raise UnicodeError("There is a letter in your sentence that is not in english alphabet. Please start the code again.")