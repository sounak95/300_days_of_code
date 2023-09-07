'''

'''

n=5

for i in range(n):
    cond = i
    space_count = 2*(n-i-1)
    for j in range(2*n):
        if j<=cond:
            print('*', end=' ')
        elif space_count>0:
            print('.', end=' ')
            space_count-=1
        else:
            print('*', end=' ')

    print()
for i in range(n-1,0,-1):
    cond = i
    space_count = 2*(n-i-1)
    for j in range(2*n):
        if j<=cond:
            print('*', end=' ')
        elif space_count>0:
            print('.', end=' ')
            space_count-=1
        else:
            print('*', end=' ')

    print()
