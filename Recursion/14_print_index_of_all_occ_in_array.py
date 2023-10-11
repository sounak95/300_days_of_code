

def find(arr, n, i, target):
    if i==n:
        return

    if arr[i]==target:
        print(i)

    find(arr,n,i+1, target)

arr=[1,2,3,4,3,5,3]

find(arr, len(arr), 0, 3)
