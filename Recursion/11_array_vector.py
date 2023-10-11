
# push even elements to vector

def solve(arr, n, i, vector):
    if i==n:
        return
    if arr[i]%2==0:
        vector.append(arr[i])
    solve(arr, n, i+1, vector)

vector=[]
solve([1,2,3,4,5], 5, 0, vector)
print(vector)