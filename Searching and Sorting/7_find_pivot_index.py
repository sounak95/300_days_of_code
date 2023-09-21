l1= [12,14,16,18,4,6,8]

def find_pivot_index(arr):
    s=0
    e=len(arr)
    mid=s+(e-s)//2

    while(s<=e):
        if s==e: # if array contains single element
            return s
        if arr[mid]<arr[mid-1]:
            return mid-1
        elif arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]<arr[s]:
            e=mid-1
        else:
            s=mid+1
        mid=s+(e-s)//2
    return -1

print(find_pivot_index(l1))