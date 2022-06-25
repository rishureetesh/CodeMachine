# Recursion
def LCSRecursion(X, Y, n, m):
	if n == 0 or m == 0:
		return 0;
	if X[n - 1] == Y[m - 1]:
		return 1 + LCSRecursion(X, Y, n - 1, m - 1);
	else:
		return max(LCSRecursion(X, Y, n - 1, m), LCSRecursion(X, Y, n, m - 1))

# Memoization


def LCSMemoization(X, Y, n, m):
    table = [[0 for i in range(m+1)] for i in range(n+1)]
    if n == 0 or m == 0:
        table[n][m] = 0;
    if table[n][m] != -1:
        return table[n][m]
    if X[n - 1] == Y[m - 1]:
        table[n][m] = 1 + LCSMemoization(X, Y, n - 1, m - 1);
    else:
        table[n][m] = max(LCSMemoization(X, Y, n - 1, m), LCSMemoization(X, Y, n, m - 1))
    return table[n][m]

#Top Down
def LCSMTopDown(X, Y, n, m):
    table = [[0 for i in range(m+1)] for i in range(n+1)]
    for i in range(1, m+1):
        for j in range(1, m+1):
            if X[i - 1] == Y[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1];
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[n][m]


data = LCSMTopDown("abecd", "abyfc",5,5)
print(data)