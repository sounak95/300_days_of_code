'''
. . . . 1
. . . 1 2 1
. . 1 2 3 2 1
. 1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''

n=5

for i in range(n):
    for j in range(n-i-1):
        print(".", end=' ')
    k=0
    for j in range(i+1):
        print(j+1, end=' ')
        k=j

    for j in range(k,0,-1):
        print(j, end=' ')

    print()
