

def binary_serach(arr, s, e, target):
    if s>e:
        return -1

    mid=s+(e-s)//2

    if arr[mid]==target:
        return mid

    if target>arr[mid]:
        return binary_serach(arr, mid+1, e, target)
    else:
        return binary_serach(arr,s, mid-1, target)


l1=[1,2,3,4,5,6]
print(binary_serach(l1, 0, len(l1)-1,6 ))
