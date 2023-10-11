
def doubleArr(arr, n, i):
    if i==n:
        return
    arr[i] = 2*arr[i]
    doubleArr(arr, n, i+1)

arr=[1,2,3,4,5]
doubleArr(arr,len(arr), 0)

print(arr)