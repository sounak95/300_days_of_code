

arr=[1,2,3,4]
n=len(arr)

#doublet
for i in range(n):
    for j in range(n):
        print(arr[i], arr[j])

#triplet
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(arr[i], arr[j], arr[k])