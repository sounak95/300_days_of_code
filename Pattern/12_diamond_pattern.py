'''
...*
..* *
.* * *
* * * *
* * * *
.* * *
..* *
...*
'''

num=8

n=num//2

for i in range(n):
    k=0
    for j in range(n-i-1):
        print(".", end='')
    for j in range(i+1):
        print("* ", end='')
    print()

for i in range(n-1,-1,-1):
    k=0
    for j in range(n-i-1):
        print(".", end='')
    for j in range(i+1):
        print("* ", end='')
    print()

# for i in range(n):
#     k=0
#     for j in range(i):
#         print(".", end='')
#     for j in range(n-i):
#         print("* ", end='')
#
#     print()