def subsetsum(lst, target):
    mat = [[False for i in range(target+1)] for j in range(len(lst)+1)]

    for i in range(len(lst)+1):
        mat[i][0] = True
    
    for row in range(1, len(lst)+1):
        for col in range(target+1):
            if lst[row-1] <= col:
                mat[row][col] = mat[row-1][col-lst[row-1]] or mat[row-1][col]
            else:
                mat[row][col] = mat[row-1][col]
    return mat[-1][-1]

lst = [3,5,2,8,4,9,6]
target = 38
data = subsetsum(lst, target)
print(data)