

def solve(n, k):
    if n==1:
        return k
    if n==2:
        return k+k*k(k-1)

    return (k-1)* (solve(n-1, k)+ solve(n-2, k))