def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    d1 = 0
    d2 = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                d1 += arr[i][j]
            if i == (n-j-1):
                d2 += arr[i][j]
    return(abs(d1-d2))
