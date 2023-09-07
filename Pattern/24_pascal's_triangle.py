'''
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1 
'''

n=7

for i in range(1,n+1):
    c=1
    for j in range(1, i+1):
        print(c, end=' ')
        c=c*(i-j)//j
    print()
