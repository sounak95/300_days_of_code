'''
. . . . . *
. . . . *   *
. . . *       *
. . *           *
. *               *
* * * * * * * * * * *
'''

n=6

for i in range(n):
    k=0
    for j in range(2*n-1):
        if j<n-i-1:
            print(".", end=' ')
        elif k<(2*i+1):
            if k==0 or k==2*i or i==n-1:
                print("*", end=' ')
            else:
                print(" ", end=' ')
            k+=1
        else:
            print(" ", end=' ')
    print()