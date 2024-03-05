# Evan Johnson
# Evan-Johnson-WV
# 2/21/24
# This code will be able to take an inputted list and reverse the order of the values

def reverse_list(num_list):
    copied_list = list(num_list)
    index_back = len(num_list) - 1

    for index, num in enumerate(num_list):
        num_list[index] = copied_list[index_back]
        index_back -= 1
