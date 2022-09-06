def checkNumber(array,item,index):
    if index >= len(array):
        return -1
    if array[index] == item:
        return index
    else:
        return checkNumber(array,item,index+1)

array = [2,3,1,3,7,5,8,9]
data = checkNumber(array,10,0)
print(data)