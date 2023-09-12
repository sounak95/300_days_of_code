'''
Ways to solve this
1.counting
2.2 pointer
3.sort
'''
arr=[0,1,0,1,1,0,0,0,0]

c_0=0
c_1=1
for ele in arr:
    if ele==0:
        c_0+=1
    elif ele==1:
        c_1+=1

for i in range(len(arr)):
    if i<c_0:
        arr[i]=0
    else:
        arr[i]=1

print(arr)
