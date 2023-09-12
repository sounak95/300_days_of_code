

def solve(arr):
    arr[0]=100

'''
array by default is passed by reference
'''
arr= [10,20,30]
solve(arr)
print(arr)


'''
array here is passed by value
'''
arr= [10,20,30]
solve(arr.copy())
print(arr)

