globalArray = []

def assembleArray(array, item):
    if len(array) == 0 or array[-1] <= item:
        array.append(item)
        return
    data = array[-1]
    array.pop()
    assembleArray(array, item)
    array.append(data)

def sortArray(array):
    if len(array) <= 1:
        return
    data = array[-1]
    array.pop()
    sortArray(array)
    assembleArray(array, data)
    return array

arrayElements = [9,8,9,0,6,5,8,3,2,1]
print(sortArray(arrayElements))