'''
.....*
....* *
...* * *
..* * * *
.* * * * *
* * * * * *
'''


n=6

for i in range(n):
    k=0
    for j in range(n-i-1):
        print(".", end='')
    for j in range(i+1):
        print("* ", end='')
    print()