#!/usr/bin/python3

# Author: Edwin Trinh
# GitHub username: trinhed
# Date: 2/19/2024
# Description: Program that calculates the square of a value

def square_list(num_list):
    """Method to get the value of a list of numbers and square the values"""
    squared_list = [] # Initialize an empty list for squared values

    for value in num_list: # Get the value of each index
        squared_value = value ** 2 # Square the original list value
        squared_list.append(squared_value) # Append new squared values to squared list
    # print(squared_list)
    num_list[:] = squared_list # Replace values or original list with squared list

# num_list = [7, -3, 12, 9]
# square_list(num_list)
# print(num_list)  # This should print [49, 9, 144, 81]