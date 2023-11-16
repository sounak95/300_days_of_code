# https://practice.geeksforgeeks.org/problems/help-classmates--141631/1

#User function Template for python3

# next smaller elelemnt
class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        st=[-1]
        ans = [-1] * n
        for i in range(n-1, -1, -1):
            while(st[-1]>=arr[i]):
                st.pop()

            ans[i] = st[-1]
            st.append(arr[i])

        return ans

# prev smaller elelemnt

class Solution:
    def prev_smaller_element(self, arr, n):
        # Your code goes here
        # Return the list
        st=[-1]
        ans = [-1] * n
        for i in range(n):
            while(st[-1]>=arr[i]):
                st.pop()

            ans[i] = st[-1]
            st.append(arr[i])

        return ans

