

def check_sorted(arr, n, i):
    if i>=n:
        return True

    if arr[i]>arr[i-1]:
        return check_sorted(arr, n, i+1)
    else:
        return False

l1=[1,2,3,4,9,6]

print(check_sorted(l1,len(l1), 1))