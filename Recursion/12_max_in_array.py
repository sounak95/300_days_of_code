

def max_in_array(arr, n, i, maxi):
    if i==n:
        return
    maxi[0] =  max(arr[i], maxi[0])
    max_in_array(arr, n, i+1, maxi)

maxi =  [-float('inf')]
max_in_array([1,2,3,400,5, 99], 6, 0, maxi)

print(maxi[0])