# https://leetcode.com/problems/reverse-linked-list/description/


# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr=head
        prev=None
        while(curr!=None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr= next

        return prev


class Solution2(object):

    def helper(self, prev, curr):
        # base case
        if curr==None:
            return prev
        # 1 case hum solve krenge
        next = curr.next
        curr.next = prev
        prev= curr
        curr = next

        # baaaki kon sambhalega - recursion
        return self.helper(prev, curr)


    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        return self.helper(prev, curr)
