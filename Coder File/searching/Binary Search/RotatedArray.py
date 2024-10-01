def RotatedArray(lst):
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

lst = [8,9,10,11,12,13,1,2,3,4,5,6,7]
index = RotatedArray(lst)
print(index)