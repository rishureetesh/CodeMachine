def findLargestNumber(itemList, money):
    matrix = [[0 for j in range(len(itemList)+1)] for i in range(money+1)]
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if itemList[j-1] <= money - matrix[i-1][j]:
                matrix[i][j] = matrix[i-1][j] + 1
            else:
                matrix[i][j] = matrix[i-1][j]
    max = matrix[money][0]
    ind = 0
    for index in range(1, len(matrix[money])):
        if matrix[money][index] >= max:
            max = matrix[money][index]
            ind = index
    if max == 0:
        return -1
    dataReturn = 0
    for i in range(max):
        dataReturn = dataReturn * 10 + ind
    return dataReturn
    


lst = [9,7,8,6,3,4,5,2,1] # 99999
num = findLargestNumber(lst, 5)
print(num)
lst = [9,7,2,2,3,4,5,3,3] # 99999
num = findLargestNumber(lst, 2)
print(num)
lst = [9,9,9,9,9,9,9,9,9] # 99999
num = findLargestNumber(lst, 5)
print(num)