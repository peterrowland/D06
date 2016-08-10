#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write additional function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports

# Body
def is_abecedarian(word):
    word = word.lower()
    last_letter = 'a'
    true_bit = True
    for letter in word:
        if ord(letter) >= ord(last_letter):
            last_letter = letter
        else:
            true_bit = False
            break

    return true_bit

def count_abecedarian():
    fin = open('words.txt','r')
    words = fin.readlines()
    abec_words = []

    for i in range(len(words)):
        words[i] = words[i].strip()
        if is_abecedarian(words[i]):
            abec_words.append(words[i])

    print("There are", "{0}".format(len(abec_words)), end=' ')
    print("(.2%)".format( len(abec_words) / len(words)), "abecedarian words.")




    # while fin.readline():
    #     if is_abecedarian()




##############################################################################
def main():
    pass  # Call your function(s) here.
    count_abecedarian()
if __name__ == '__main__':
    main()
