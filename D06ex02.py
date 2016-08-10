#!/usr/bin/env python3
# D06ex02.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
import random as random

# Body

def write_random():
    fout = open('random-numbers', 'w')

    for i in range(10):
        fout.write(str(random.randint(1,100)))
        fout.write('\n')
        
    fout.close()


##############################################################################
def main():

    write_random()

if __name__ == '__main__':
    main()
