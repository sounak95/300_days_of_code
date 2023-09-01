'''
1
1 2
1 . 3
1 . . 4
1 2 3 4 5
'''
n=5

for i in range(n):
    for j in range(i+1):
        if i==n-1 or j==0 or j==i:
            print(j+1, end=' ')
        else:
            print('.', end=' ')
    print()