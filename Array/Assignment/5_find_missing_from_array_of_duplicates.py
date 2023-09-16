
'''
arr[1,3,5,3,4]
'''

def find_missing_num(arr):
    n=len(arr)
    for i in range(n):
        index = abs(arr[i])
        if arr[index-1]>0:
            arr[index-1]=-1*arr[index-1]

    for i in range(n):
        if arr[i]>0:
            print(i+1, end=' ')

find_missing_num([1,3,2,3,4])