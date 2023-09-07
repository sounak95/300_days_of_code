'''
1
2*3
4*5*6
7*8*9*10
7*8*9*10
4*5*6
2*3
1
'''
num=8
n=num//2

num=1
for i in range(n):
    for j in range(i+1):
        if j==i:
            print(num, end='')
        else:
            print(num, end='*')
        num+=1
    print()

# num=1
# for i in range(n-1,-1,-1):
#     for j in range(i+1):
#         if j==i:
#             print(num, end='')
#         else:
#             print(num, end='*')
#         num+=1
#     print()

start = num - n
for i in range(n):

    k=start
    for j in range(n-i):
        if j==n-i-1:
            print(k, end='')
        else:
            print(k, end='*')
        k+=1
    start = start-(n - i-1)
    print()
