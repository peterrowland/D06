# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################################
# Imports


# Body

#plain version
def nested_sum(input_list):
    summed = 0
    for item in input_list:
        if type(item) == list:
            for i in item:
                summed += i
            #nested_sum(input_list.index(item))
        else:
            summed += item

    return summed

#recursive version? I only got part of this to work.
# def recursive():
#     if type(input) == list:
#         for item in input:
#             #print(input.index(item))
#             item_index = input.index(item)
#             #print(item_index)
#             nested_sum_recursive(item_index)
#         else:
#             return



##############################################################################
def main():
    pass

    print(nested_sum([1, 2,[3]]))
    #print(nested_sum([[1,2,5,6],[2,4,6]]))
    #print(nested_sum([[2,4,5],[[1],[2]]]))

if __name__ == '__main__':
    main()
