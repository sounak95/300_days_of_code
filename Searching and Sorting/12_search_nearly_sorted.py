

def search_nearly_sorted(arr, target):
    n= len(arr)
    s=0
    e= n-1

    mid = s+(e-s)//2

    while(s<=e):
        if (mid-1>=0 and arr[mid-1]==target):
            return mid-1
        elif arr[mid]==target:
            return mid
        elif (mid+1)<n  and arr[mid+1]==target:
            return mid+1

        if target>arr[mid]:
            s=mid+2
        elif target<arr[mid]:
            e=mid-2

        mid=s+(e-s)//2

    return -1

l1=[20,10,30,50,40,70,60]
print(search_nearly_sorted(l1,50))

