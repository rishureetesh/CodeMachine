# Top Down
lst_top = [[0 for i in range(6+1)] for i in range(6+1)]
def countOfSubsetSum(lst, sum, target_sum, n):

    for len in range(n+1):
        for col in range(target_sum+1):
            if col == 0:
                lst_top[len][col] = 1
            
            elif lst[len-1] <= col:
                lst_top[len][col] = lst_top[len-1][col-lst[len-1]] + lst_top[len-1][col]
            elif lst[len-1] > col:
                lst_top[len][col] = lst_top[len-1][col]

countOfSubsetSum([1,2,3,4,5,6], 0, 6, 6)
print("Recursion Topdown : ",lst_top[6][6])