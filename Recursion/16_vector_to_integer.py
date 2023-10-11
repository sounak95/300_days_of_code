
def vector_to_integer(arr, n, i, num):
    if i==n:
        return num
    num=num*10+arr[i]

    return vector_to_integer(arr, n, i+1, num)

print(vector_to_integer([3,2,1,9,8],5,0, 0))