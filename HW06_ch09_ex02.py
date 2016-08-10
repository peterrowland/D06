#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def contains_e(text):
    return bool(text.lower().find('e') >= 0)

def list_not_e():

    with open('roster.txt','r') as f:
        names = f.readlines()
        total = len(names)
        not_e_names = []

        for name in names:
            #print(name.split()[0])
            if contains_e(name.split()[0]) != True:
                not_e_names.append(name.split()[0])

    with open('not_e_names.txt', 'w') as fout:
        fout.write('Number of names not containing e: ' + (str(len(not_e_names))) + '\n' )
        for i in not_e_names: fout.write(i + ' \n')
        fout.write('Percentage of names not containing e: ')
        fout.write("{:.2%}".format((len(not_e_names)/total)))


    # print("Number of names containing e:", str(len(e_names)))
    # for i in e_names: print (i)



##############################################################################
def main():
    list_not_e()

if __name__ == '__main__':
    main()


##############################################################################
def main():
    pass  # Call your function(s) here.

if __name__ == '__main__':
    main()
