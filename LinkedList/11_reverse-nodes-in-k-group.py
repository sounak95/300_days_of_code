# https://leetcode.com/problems/reverse-nodes-in-k-group/


# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def getLength(self, head):
        len = 0
        temp = head
        while (temp != None):
            len += 1
            temp = temp.next

        return len

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head

        if head.next == None:
            return head

        prev = None
        curr = head
        next = curr.next
        pos = 0
        len = self.getLength(head)

        # don't reverse if length is less than k
        if len < k:
            return head

        # solve one case
        while (pos < k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            pos += 1

        recAns = None
        if next != None:
            recAns = self.reverseKGroup(next, k)
            head.next = recAns

        return prev