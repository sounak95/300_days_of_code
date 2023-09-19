# https://practice.geeksforgeeks.org/problems/first-repeating-element4018/1

# User function Template for python3

class Solution:
    # Function to return the position of the first repeating element.
    def firstRepeated_bf(self ,arr, n):
        for i in range(n):
            for j in range(i+1, n):
                if arr[i]==arr[j]:
                    return arr[i]
        return -1

    def firstRepeated(self, arr, n):
        hash = {}

        for i in range(n):
            hash[arr[i]] = hash.get(arr[i], 0) + 1

        for i in range(n):
            if hash[arr[i]] > 1:
                return i + 1
        return -1


