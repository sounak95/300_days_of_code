
def find(arr, n, i, target):
    if i==n:
        return

    if arr[i]==target:
        print(i)

    find(arr,n,i+1, target)

arr="babbar"

find(arr, len(arr), 0, 'a')