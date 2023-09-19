
'''
arr[1,3,5,3,4]

'''


'''
Positioning technique
Time complexity: o(n)
Space complexity: o(1)
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

# find_missing_num([1,3,2,3,4])
'''
Sorting plus swapping

'''
def find_missing_num_sort_swap(arr):
    i=0
    while(i<len(arr)):
        index=arr[i]-1
        if arr[index]!=arr[i]:
            arr[index], arr[i]= arr[i], arr[index]
        else:
            i+=1
    print(arr)
    for i,ele in enumerate(arr):
        index=i+1
        if index!=ele:
            print(index, end=' ')

find_missing_num_sort_swap([1,3,5,3,4])
# find_missing_num_sort_swap([5,3,3,3,1])
