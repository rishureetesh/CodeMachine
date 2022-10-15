from math import sqrt


def binary_search(list_elements, target, low=0, high=0):
    high = len(list_elements) - 1 if not high else high
    while low <= high:
        mid = low + (high-low)//2
        if list_elements[mid] == target:
            return mid
        elif list_elements[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def linear_seach(list_elements, target):
    for index, value in enumerate(list_elements):
        if value == target:
            return index
    return -1

def jump_search(list_elements, target):
    jump = int(sqrt(len(list_elements)))
    low = 0
    high = jump
    while list_elements[min(high, len(list_elements))-1] < target:
        low, high = high, high+jump
        if low >= len(list_elements):
            return -1
    for index in range(low, high):
        if list_elements[index] == target:
            return index
    return -1

def exponential_search(list_elements, target):
    if len(list_elements) == 0:
        return -1
    if list_elements[0] == target:
        return 0
    exp = 1
    while exp < len(list_elements) and list_elements[exp] <= target:
        exp *= 2
    return binary_search(list_elements, target, exp//2, min(exp, len(list_elements)-1))