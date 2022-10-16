def findLargestNumber(itemList, money):
    lst = [0 for j in range(len(itemList)+1)]
    matrix = [[0 for j in range(len(itemList)+1)] for i in range(money+1)]
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if itemList[j-1] <= money - matrix[i-1][j]:
                matrix[i][j] = matrix[i-1][j] + 1
                lst[j] = lst[j] * 10 + j
            else:
                matrix[i][j] = matrix[i-1][j]
    print(lst)
    return max(lst)
    


lst = [9,7,8,6,3,4,5,2,1] # 99999
num = findLargestNumber(lst, 5)
print(num)
lst = [9,7,2,2,3,4,5,3,3] # 99999
num = findLargestNumber(lst, 2)
print(num)
lst = [9,9,9,9,9,9,9,9,9] # 99999
num = findLargestNumber(lst, 5)
print(num)