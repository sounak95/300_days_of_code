# https://leetcode.com/problems/middle-of-the-linked-list/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = head
        fast = head

        while (fast != None):
            fast = fast.next
            if (fast != None):
                fast = fast.next
                # main yaha keh skta hu k fast ne 2 step chal liye h
                # ab slow ko bhi chalwao ek step
                slow = slow.next

        return slow