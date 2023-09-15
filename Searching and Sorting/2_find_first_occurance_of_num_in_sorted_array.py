

'''
Time omplexity: log(n)
'''

arr=[10,30,30,30,30,40,50]

def find_first_occurance(arr,n, target):
    start=0
    end=n-1
    mid=(start+end)//2
    ans=-1
    while(start<=end):
        if arr[mid]==target:
            ans=mid
            # goto left
            end=mid-1
        elif target>arr[mid]:
            # goto right
            start=mid+1
        elif target<arr[mid]:
            #goto left
            end=mid-1

        mid = (start+ end)//2

    return ans

print(find_first_occurance(arr, len(arr), 30))