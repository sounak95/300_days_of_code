'''
                     pow(2, 6)
                     /     \
                    /       \
                2 * pow(2, 5)  = 2 * 32 = 64
                     /     \
                    /       \
                2 * pow(2, 4)  = 2 * 16 = 32
                     /     \
                    /       \
                2 * pow(2, 3)  = 2 * 8  = 16
                     /     \
                    /       \
                2 * pow(2, 2)  = 2 * 4  = 8
                     /     \
                    /       \
                2 * pow(2, 1)  = 2 * 2  = 4
                     /     \
                    /       \
                2 * pow(2, 0)  = 2 * 1  = 2
                            |
                            |
                         return 1 (base case)

'''

def pow(n):
    #base case
    if n==0:
        return 1

    return 2*pow(n-1)

print(pow(6))