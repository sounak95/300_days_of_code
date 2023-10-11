

def min_in_array(arr, n, i, mini):
    if i==n:
        return
    mini[0] =  min(arr[i], mini[0])
    min_in_array(arr, n, i+1, mini)

mini =  [float('inf')]
min_in_array([1,2,3,4,5, -99], 6, 0, mini)

print(mini[0])