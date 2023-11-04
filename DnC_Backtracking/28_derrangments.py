
# https://www.geeksforgeeks.org/count-derangements-permutation-such-that-no-element-appears-in-its-original-position/


def solve(n):
    if n==1:
        return 0

    if n==2:
        return 1

    return (n-1) * (solve(n-1)+ solve(n-2))