"""
Kadane’s Algorithm : Maximum Subarray Sum in an Array
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and return its sum and print the subarray.

Example 1:

Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 

Output: 6 

Explanation: [4,-1,2,1] has the largest sum = 6. 

Examples 2: 

Input: arr = [1] 

Output: 1 

Explanation: Array has only one element and which is giving positive sum of 1. 

"""
def take_input():
    return [-2,1,-3,4,-1,2,1,-5,4]

def kadanes_algorithm(input_array):
    if not input_array:
        return dump_output(output="Array Empty!")
    curr_max = 0
    overall_max = 0
    start_point = -1
    end_point = -1
    for index, items in enumerate(input_array):
        curr_max += items

        if curr_max > overall_max:
            overall_max = curr_max
            end_point = index
        
        if curr_max <= 0:
            curr_max = 0
            start_point = index + 1
    return dump_output(output=overall_max, end_point=end_point, start_point=start_point)

def dump_output(**output):
    print(f"Output received : {output}")


input = take_input()
kadanes_algorithm(input)