'''
*
*1*
*121*
*12321*
*1234321*
*12321*
*121*
*1*
*
'''
num=9
n=num//2


for i in range(n+1):
    print('*', end='')
    num=0
    for j in range(i):
        # if j!=0 and j!=i:
        #     print(num, end='')
        # else:
        num=j+1
        print(num, end='')
    num-=1
    for j in range(num, 0,-1):
        print(j, end='')
    if i>0:
        print('*', end='')
    print()

for i in range(n-1,-1,-1):
    print('*', end='')
    num=0
    for j in range(i):
        num=j+1
        print(num, end='')
    num-=1
    for j in range(num, 0,-1):
        print(j, end='')
    if i>0:
        print('*', end='')
    print()

