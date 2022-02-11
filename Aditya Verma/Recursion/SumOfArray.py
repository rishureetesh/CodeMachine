def sumOfArray(array, index):
    if not array:
        return -1
    if index==0:
        return array[index]
    return array[index] + sumOfArray(array, index-1)

array = [3,4,5,6,7,8]
print(sumOfArray(array,len(array)-1))