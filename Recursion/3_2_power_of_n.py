

def pow(n):
    #base case
    if n==0:
        return 1

    return 2*pow(n-1)

print(pow(6))