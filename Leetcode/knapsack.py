def knapsack(item, value, capacity, size):
    if not size or not capacity:
        return -1

    matrix = [[0 for i in range(capacity+1)] for i in range(len(item)+1)]

    for i in range(1, len(item)+1):
        for j in range(1, capacity+1):
            if item[i-1] <= j:
                matrix[i][j] = max(value[i-1] + matrix[i-1][j-item[i-1]], matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]
    for rows in matrix:
        print(rows)
    return matrix[-1][-1]

item = [1,2,3,4,5]
value = [5,6,2,9,5]
weight = 25
size = len(item)
data = knapsack(item, value, weight, size)
print(data)