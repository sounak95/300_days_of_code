# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution(object):

    def prev_smaller_element(self, arr, n):
        # Your code goes here
        # Return the list
        st=[-1]
        ans = [-1] * n
        for i in range(n):
            while(st[-1]!=-1 and arr[st[-1]]>=arr[i]):
                st.pop()

            ans[i] = st[-1]
            st.append(i)

        return ans

    def next_smaller_element(self, arr, n):
        # Your code goes here
        # Return the list
        st = [-1]
        ans = [-1] * n
        for i in range(n-1, -1, -1):
            while (st[-1] != -1 and arr[st[-1]] >= arr[i]):
                st.pop()

            ans[i] = st[-1]
            st.append(i)

        return ans

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        next = self.next_smaller_element(heights, len(heights))
        prev = self.prev_smaller_element(heights, len(heights))

        for i in range(len(next)):
            if next[i]==-1:
                next[i] = len(heights)

        max_area = float('-inf')
        for i in range(len(heights)):
            height = heights[i]
            length = next[i]-prev[i]-1
            area = height*length
            max_area = max(area, max_area)

        return max_area