# https://leetcode.com/problems/find-pivot-index/

class Solution(object):
    '''
    Time Complexity: o(n2)
    Space complexity: o(1)
    '''

    def pivotIndex_bf(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        for i in range(n):
            l_sum=0
            for j in range(i):
                l_sum+=nums[j]
            r_sum=0
            for j in range(i+1,n):
                r_sum+=nums[j]

            if l_sum==r_sum:
                return i
        return -1

    '''
    Optimal Solution
    Time Complexity: o(n)
    Space complexity: o(n)
    '''
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        l_sum=[0]*n
        r_sum=[0]*n

        for i in range(1,n):
            l_sum[i]=l_sum[i-1]+ nums[i-1]

        for i in range(n-2,-1,-1):
            r_sum[i]=r_sum[i+1]+ nums[i+1]

        for i in range(n):
            if l_sum[i]==r_sum[i]:
                return i

        print(l_sum, r_sum)
        return -1

s=Solution()
print(s.pivotIndex([1,7,3,6,5,6]))

