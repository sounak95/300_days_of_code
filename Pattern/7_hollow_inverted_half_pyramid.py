'''
* * * * *
*     *
*   *
* *
*
'''

n= 5

for i in range(n):
    for j in range(n - i):
        if i==0  or j==0 or j==n-i-1:
            print("* ", end='')
        else:
            print("  ", end='')
    print()

print()
# Alternate way
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        if i==n-1 or j==0 or j==i :
            print('* ', end='')
        else:
            print("  ", end='')
    print()
