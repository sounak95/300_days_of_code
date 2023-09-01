'''
1 2 3 4 5
2 . . 5
3 . 5
4 5
5
'''
n=5

for i in range(n-1,-1,-1):
    k = n - i;
    for j in range(i+1):
        if i==n-1 or j==0 or j==i:
            print(k, end=' ')
        else:
            print('.', end=' ')
        k=k+1
    print()