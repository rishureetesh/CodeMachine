def knapSack(W, wt, val, n):
   # code here
   lst_un = [[0 for j in range(W+1)]for i in range(len(wt)+1)]
   for row in range(1,len(lst_un)):
      for col in range(1, len(lst_un[0])):
          if wt[row-1] <= col:
             lst_un[row][col] = max(val[row-1]+lst_un[row][col-wt[row-1]],lst_un[row-1][col])
          elif wt[row-1] > col:
             lst_un[row][col] = lst_un[row-1][col]
 
   return lst_un[-1][-1]


W = 8
val = [10, 40, 50, 70]
wt  = [1, 3, 4, 5]

data = knapSack( W, wt, val, len(wt))
print(data)