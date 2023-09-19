# https://practice.geeksforgeeks.org/problems/common-elements1132/1


# User function Template for python3



class Solution:
    def commonElements(self, A, B, C, n1, n2, n3):
        set_ans = set()
        i = 0
        j = 0
        k = 0
        while (i < n1 and j < n2 and k < n3):
            if A[i] == B[j] and B[j] == C[k]:
                set_ans.add(A[i])
                i += 1
                j += 1
                k += 1
            elif A[i] < B[j]:
                i += 1
            elif B[j] < C[k]:
                j += 1
            else:
                k += 1

        ans = []
        for ele in set_ans:
            ans.append(ele)

        return sorted(ans)




