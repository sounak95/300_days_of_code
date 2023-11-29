# https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1

# User function Template for python3

def printFirstNegativeInteger(A, N, K):
    q = []
    ans = []
    # process first K elements
    for i in range(K):
        if A[i] < 0:
            q.append(i)

    # sliding window
    for i in range(K, N):
        # print negative for the previous window
        if len(q) != 0:
            ans.append(A[q[0]])

            # removal
            if i - q[0] >= K:
                q.pop(0)
        # ans is 0 is no negative element is found
        else:
            ans.append(0)

        # addition
        if A[i] < 0:
            q.append(i)

    # check for the last window
    if len(q) != 0:
        ans.append(A[q[0]])
    else:
        # ans is 0 is no negative element is found
        ans.append(0)

    return ans


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())

        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends