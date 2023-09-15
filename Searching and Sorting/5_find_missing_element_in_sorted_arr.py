
l1=[1,2,3,4,6,7,8,9]

def find_missing_element(arr,n):
    s=0
    e=n-1
    mid = s+(e-s)//2
    ans=-1
    while(s<=e):
        if arr[mid]-mid==1:
            s=mid+1
        else:
            ans=mid
            e=mid-1
        mid=s+(e-s)//2

    return ans+1

print(find_missing_element(l1, len(l1)))
