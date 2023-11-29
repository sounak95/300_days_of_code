# https://practice.geeksforgeeks.org/problems/interleave-the-first-half-of-the-queue-with-second-half/1


from typing import List


class Solution:
    def rearrangeQueue(self, N: int, q: List[int]) -> List[int]:
        second=[]
        # push the first half of the queue into second
        for i in range(N//2):
            second.append(q.pop(0))

        #merge both the halfs
        for i in range(N//2):
            q.append(second.pop(0))
            q.append(q.pop(0))

        return q

# code here


# {
# Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())

        q = IntArray().Input(N)

        obj = Solution()
        res = obj.rearrangeQueue(N, q)

        IntArray().Print(res)

# } Driver Code Ends