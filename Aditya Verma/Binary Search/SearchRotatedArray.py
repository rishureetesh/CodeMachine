def SearchRotatedArray(lst):
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = low + (high-low)//2
        if lst[mid] < lst[mid-1] and lst[mid] < lst[mid+1]:
            return mid
        elif lst[mid] > lst[low]:
            low = mid+1
        else:
            high = mid -1
    return 0

def BinarySearch(lst, low, high, target):
    while low <= high:
        mid = low + (high-low)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid+1
        else:
            high = mid -1
    return -1

lst = [8,9,10,11,12,13,1,2,3,4,5,6,7]
target = 12
index = SearchRotatedArray(lst)
ind = -1
if lst[len(lst)-1] >= target:
    ind = BinarySearch(lst, index, len(lst)-1, target)
else:
    ind = BinarySearch(lst, 0, index-1, target)

if ind == -1:
    print("Element not found!!!")
else:
    print(f"Found at index : {ind}")