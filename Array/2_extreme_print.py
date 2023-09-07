arr = [10,20,30,40,50, 60]
arr = [10,20,30,40,50,]
left=0
right = len(arr)-1

while(left<=right):
    if left==right:
        print(arr[left])
    else:
        print(arr[left], end=' ')
        print(arr[right], end=' ')
    left+=1
    right-=1

