


def binary_search(arr,n, target):
    start=0
    end=n-1
    mid=(start+end)//2

    while(start<=end):
        if arr[mid]==target:
            return mid
        if target>arr[mid]:
            # goto right
            start=mid+1
        elif target<arr[mid]:
            #goto left
            end=mid-1

        mid = (start+ end)//2

    return -1
arr=[10,20,30,40,50,60,70,80,90]

print(binary_search(arr, len(arr),90 ))

