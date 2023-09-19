


def WavePrint(m, n, arr):
    for j in range(n):
        if j%2==0:
            for i in range(m):
                print(arr[i][j], end=' ')
        else:
            for i in range(m-1,-1,-1):
                print(arr[i][j], end=' ')


# Driver Code
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]

WavePrint(5, 4, arr)