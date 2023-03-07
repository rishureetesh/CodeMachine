def sortedArray(array, index):
    if index == 0:
        return True
    if array[index] < array[index-1]:
        return False
    return sortedArray(array, index-1)

array = [1,2,3,4,5,6,7,9,8,10]
print(sortedArray(array, len(array)-1))