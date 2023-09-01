'''
1
2*2
3*3*3
4*4*4*4
3*3*3
2*2
1
'''

n=4

# alternake way
for i in range(n):
    for j in range(i+1):
        if j<i:
            print(i+1, end='*')
        elif j==i:
            print(i+1, end='')
    print()

n=n-1
for i in range(n):
    for j in range(n-i):
        if j<n-i-1:
            print(n-i, end='*')
        else:
            print(n-i, end='')
    print()

# for i in range(n):
#     for j in range(2*i + 1):
#         if j%2==0:
#             print(i + 1, end='')
#         else:
#             print("*", end='')
#     print()
