def printArray(arr, n, index):
    if index==n:
        return

    printArray(arr, n, index+1)
    print(arr[index])


printArray([1,2,3,4,5], 5, 0)