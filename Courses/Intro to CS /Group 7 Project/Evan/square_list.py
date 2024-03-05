# Evan Johnson
# Evan-Johnson-WV
# 2/21/24
# The purpose of this code is to create a function that will take a list and return a list of the squared
# values of the list

def square_list(list_of_nums):
    """ This function will take a list and square all of the values in the list """

    # Setting a starting index to reference the positions of the numbers
    index = 0

    # Creating the function
    for number in list_of_nums:
        # Rewriting the numbers as their square
        list_of_nums[index] = number * number
        # Adding one to the index to pull all values of the list
        index += 1
    return list_of_nums
