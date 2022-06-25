"""
Sort an array of 0s, 1s and 2s

Problem Statement: Given an array consisting of only 0s, 1s and 2s.
Write a program to in-place sort the array without using inbuilt sort functions.
( Expected: Single pass-O(N) and constant space)

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]

Input: nums = [0]
Input: nums = [0]

"""

"""
Approach 1: 
Count number of 0s, 1s and 2s
Re-write the array according to that

Approach 2:
using 3 pointer approach
use mid approach and play along it

"""


def take_input():
    return [2,0,2,1,1,0]

def sort_array_012(input_array):
    if not input_array:
        return print_output(output=[])
    
    array_len = len(input_array)

    end_pointer = array_len -1
    initial_pointer = 0
    mid_pointer = 0
    
    while mid_pointer <= end_pointer:
        if input_array[mid_pointer] == 0:
            input_array[initial_pointer], input_array[mid_pointer] = input_array[mid_pointer], input_array[initial_pointer]
            initial_pointer += 1
            mid_pointer += 1
        
        elif input_array[mid_pointer] == 1:
            mid_pointer += 1
        
        elif input_array[mid_pointer] == 2:
            input_array[end_pointer], input_array[mid_pointer] = input_array[mid_pointer], input_array[end_pointer]
            end_pointer -= 1

    return print_output(output=input_array)

def print_output(*args, **kwargs):
    print(f"Output received {args, kwargs}")

input = take_input()
sort_array_012(input)