# return true/false
# return valid index or -1

def search_in_array(arr, n, target, i):
    if i==n:
        return False
    if arr[i] ==target:
        return True
    return search_in_array(arr, n, target, i+1)

def search_in_array_index(arr, n, target, i):
    if i==n:
        return -1
    if arr[i] ==target:
        return i
    return search_in_array_index(arr, n, target, i+1)

print(search_in_array([1,2,3,4,5], 5, 3, 0))

print(search_in_array_index([1,2,3,4,5], 5, 3, 0))