import sys
# Top Down
lst_top = [[False for i in range(10+1)] for i in range(3+1)]
def minimumSubsetSumDifference(lst, sum, target_sum, n):

    for len in range(n+1):
        for col in range(target_sum+1):
            if col == 0:
                lst_top[len][col] = True
            
            elif lst[len-1] <= col:
                lst_top[len][col] = lst_top[len-1][col-lst[len-1]] or lst_top[len-1][col]
            elif lst[len-1] > col:
                lst_top[len][col] = lst_top[len-1][col]

minimumSubsetSumDifference([1,2,7], 0, 10, 3)

minData = sys.maxsize
for items in range(0,len(lst_top[3])//2):
    if lst_top[3][items]:
        minData = min(minData, 10-(2 * items))

print("Recursion Topdown : ",minData)