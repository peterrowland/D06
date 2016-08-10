#!/usr/bin/env python3
# D06ex03.py

##############################################################################
# Imports


# Body

def contains_e(text):
    return bool(text.lower().find('e') >= 0)
    # if text.find('e') > 0:
    # if text.lower().find('e') >= 0:
    #     return text

def list_e_names():

    with open('roster.txt','r') as f:
        names = f.readlines()
        e_names = []

        for name in names:
            #print(name.split()[0])
            if contains_e(name.split()[0]) == True:
                e_names.append(name.split()[0])

        print("Number of names containing e:", str(len(e_names)))
        for i in e_names: print (i)



##############################################################################
def main():
    list_e_names()

if __name__ == '__main__':
    main()
