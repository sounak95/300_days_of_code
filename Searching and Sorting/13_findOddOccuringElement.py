

def find_odd_occuring_ele(nums):
    n= len(nums)
    s=0
    e=n-1
    mid=s+(e-s)//2
    while(s<=e):
        # single element
        if s==e:
            return s
        if mid%2!=0:
            if mid-1>=0 and nums[mid]==nums[mid-1]:
                # goto right
                s=mid+1
            else:
                # goto left
                e=mid-1
        elif mid%2==0:
            if mid+1<n and nums[mid]==nums[mid+1]:
                #goto right
                s=mid+2
            else:
                #goto left
                e=mid

        mid=s+(e-s)//2

    return -1

nums= [7,10,10,2,2,3,3,5,5,6,6,7,7]
# nums= [10]
print(nums[find_odd_occuring_ele(nums)])