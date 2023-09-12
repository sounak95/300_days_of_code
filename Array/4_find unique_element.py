

def get_unique(arr):
    ans=0
    for ele in arr:
        ans=ans^ele
    return ans

arr=[2,10,11,10,2,13,15,13,15]

print(get_unique(arr))
