#Recursion
def subset_sum(lst, sum, target_sum, n):

    if target_sum == 0:
        return True
    
    if n==0:
        return False
    
    if lst[n-1] <= target_sum:
        return subset_sum(lst, sum+lst[n-1], target_sum-lst[n-1], n-1) or subset_sum(lst, sum, target_sum, n-1)
    elif lst[n-1] > target_sum:
        return subset_sum(lst, sum, target_sum, n-1)
    return False


#Memoization
lst_memo = [[False for i in range(21+1)] for i in range(6+1)]
def subset_sum_memoization(lst, sum, target_sum, n):

    if target_sum == 0:
        lst_memo[n][target_sum] = True
    
    if n==0:
        lst_memo[n][target_sum] = False
    
    if lst[n-1] <= target_sum:
        lst_memo[n][target_sum] = subset_sum(lst, sum+lst[n-1], target_sum-lst[n-1], n-1) or subset_sum(lst, sum, target_sum, n-1)
        return lst_memo[n][target_sum]
    elif lst[n-1] > target_sum:
        lst_memo[n][target_sum] = subset_sum(lst, sum, target_sum, n-1)
        return lst_memo[n][target_sum]


# Top Down
lst_top = [[False for i in range(43+1)] for i in range(6+1)]
def subset_sum_top_down(lst, sum, target_sum, n):

    for len in range(n+1):
        for col in range(target_sum+1):
            if col == 0:
                lst_top[len][col] = True
            
            elif lst[len-1] <= col:
                lst_top[len][col] = lst_top[len-1][col-lst[len-1]] or lst_top[len-1][col]
            elif lst[len-1] > col:
                lst_top[len][col] = lst_top[len-1][col]


data = subset_sum([1,2,3,4,5,6], 0, 21, 6)
print("Recursion : ",data)

data = subset_sum_memoization([1,2,3,4,5,6], 0, 21, 6)
print("Recursion Memoization : ",data)

subset_sum_top_down([1,2,3,4,5,6], 0, 43, 6)
print("Recursion Topdown : ",lst_top[6][43])