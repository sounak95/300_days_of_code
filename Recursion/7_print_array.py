
def printArray(arr, n, index):
    if index==n:
        return
    print(arr[index])
    printArray(arr, n, index+1)


printArray([1,2,3,4,5], 5, 0)