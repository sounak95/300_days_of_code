
'''
[60, 10, 20, 30, 40, 50]
'''
arr=[10,20,30,40,50,60]

n=len(arr)

temp=arr[n-1]

for i in range(n-1,0,-1):
    arr[i]=arr[i-1]

arr[0]=temp

print(arr)


'''
TODO
right shift
shift k

'''