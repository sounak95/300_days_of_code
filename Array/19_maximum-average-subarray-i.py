# https://leetcode.com/problems/maximum-average-subarray-i/


class Solution(object):
    '''
    Time complexity: o(n2)
    '''
    def findMaxAverage_bf(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum= -float('inf')
        j=k-1
        i=0
        while(j<len(nums)):
            sum=0
            for y in range(i, j+1):
                sum+=nums[y]
            if sum>max_sum:
                max_sum=sum
            i+=1
            j+=1
        max_avg = max_sum/float(k)

        return max_avg
    '''
    Sliding window
    '''
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i=0
        j=k-1
        sum=0
        for y in range(i, j+1):
            sum+=nums[y]
        max_sum= sum
        j+=1
        while(j<len(nums)):
            sum-=nums[i]
            sum+=nums[j]
            i+=1
            j+=1
            if sum>max_sum:
                max_sum=sum
        return max_sum/k


l1= [1,12,-5,-6,50,3]
k=4
s=Solution()
print(s.findMaxAverage_bf(l1,k))
