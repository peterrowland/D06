#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body

def load_words():
    fin = open('words.txt','r')
    words = fin.readlines()
    for i in range(len(words)):
        words[i].strip()

    return words

def avoids(word,forbid_ltrs):
    """ return True if word NOT forbidden"""
    for letter in word:
        if forbid_ltrs.find(letter) >= 0:
            return False
    return True
    ...

def avoids_count(words,ltrs):
    count = 0
    for word in words:
        count += avoids(word,ltrs)

    return count

def forbidden_prompt():
    """ print count of words NOT forbidden by input"""
    user_forbid_ltrs = input('Give me some forbidden letters: ')

    words = load_words()
    avoids_count = 0

    for word in words:
        avoids_count += avoids(word,user_forbid_ltrs)

    print ("{:,}".format(avoids_count) + " of " + "{:,}".format(len(words)) + " don't contain your letters")

def forbidden_param():
    """ return count of words NOT forbidden by param"""
    ...

def find_five():
    """ This takes a loooong time to run and I'm not sure I'm getting the right result.
    I need a way to store values after each test and reference. I think this is what dict is for?"""
    #load words
    words = load_words()

    # init variables
    letters = []
    summed = 0
    prev_remaining_words = 0
    highest = 0


    # test each letter
    for idx in range(ord('a'), ord('z')+1):
        remaining_words = avoids_count(words,chr(idx))

        # Finding highest value.
        if remaining_words > highest:
            letters.insert(0,(chr(idx)))
            highest = remaining_words
            continue

        else:
            for i in letters[:5]:
                if remaining_words > avoids_count(words,i):
                    letters.insert(letters.index(i), chr(idx))
                    break
                else:
                    continue

    for letter in letters[:5]:
        summed += avoids_count(words,letter)


    print(letters[:5])
    print(summed)



##############################################################################
def main():
    ...
    # Your final submission should only call five_five
    #forbidden_prompt()
    find_five()
if __name__ == '__main__':
    main()
