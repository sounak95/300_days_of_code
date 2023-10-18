

def last_occ(arr, index, target):
    if index<0:
        return -1
    if arr[index] == target:
        return index
    else:
        return last_occ(arr, index-1, target)

arr = [1,2,3,3,4,4,5]
print(last_occ(arr, len(arr)-1, 4))
