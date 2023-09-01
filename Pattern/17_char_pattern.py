'''
A
ABA
ABCBA
ABCDCBA
ABCDEDCBA
ABCDEFEDCBA
'''
n=6

for i in range(n):
    for j in range(i+1):
        ch= chr(ord('A') + j)
        print(ch, end='')

    #alternate way
    # for j in range(i,0,-1):
    #     # print(j-1, end='')
    #     print(chr (ord('A') + j-1), end='')
    for char in range(ord(ch) - 1, ord('A') - 1, -1):
        print(chr(char), end='')
    print()