#Recursion
def ZeroOneKnapsack(weight, value, capacity, n):
    if not capacity or not n:
        return 0
    
    if weight[n-1] <= capacity:
        return max(value[n-1]+ZeroOneKnapsack(weight, value, capacity-weight[n-1], n-1), ZeroOneKnapsack(weight, value, capacity, n-1))
    elif weight[n-1] > capacity:
        return ZeroOneKnapsack(weight, value, capacity, n-1)

lst = [[-1 for data in range(0,8)] for x in range(5)]
lst_new = [[-1 for data in range(0,8)] for x in range(5)]
#With Memoization
def ZeroOneKnapsackMemoization(weight, value, capacity, n):
    if not capacity or not n:
        return 0
    
    if lst[n][capacity] != -1:
        return lst[n][capacity]
    
    if weight[n-1] <= capacity:
        lst[n][capacity]=max(value[n-1]+ZeroOneKnapsackMemoization(weight, value, capacity-weight[n-1], n-1), ZeroOneKnapsackMemoization(weight, value, capacity, n-1))
        return lst[n][capacity]
    elif weight[n-1] > capacity:
        lst[n][capacity]=ZeroOneKnapsackMemoization(weight, value, capacity, n-1)
        return lst[n][capacity]


#With Top Down Approach
def ZeroOneKnapsackTopDown(weight, value, capacity, n):
    for len in range(n+1):
        for col in range(capacity+1):
            if not len or not col:
                lst_new[len][col] = 0
            elif weight[len-1] <= col:
                lst_new[len][col]=max(value[len-1]+lst_new[len-1][col-weight[len-1]], lst_new[len-1][col])
            elif weight[len-1] > col:
                lst_new[len][col]=lst_new[len-1][col]


print("Recursion : ",ZeroOneKnapsack([1,2,3,4],[4,3,5,10], 7, 4))
ZeroOneKnapsackMemoization([1,2,3,4],[4,3,5,10], 7, 4)
print("Memoization : ", lst[4][7])
ZeroOneKnapsackTopDown([1,2,3,4],[4,3,5,10], 7, 4)
print("Top Down : ",lst_new[4][7])