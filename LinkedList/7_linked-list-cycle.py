# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp=head
        seen = set()
        while(temp!=None):

            # Cycle present
            if temp in seen:
                return True

            seen.add(temp)
            temp = temp.next

        return False

class Solution2(object):
    def hasCycle(self, head):
        fast = head
        slow = head
        while (fast != None):
            fast = fast.next

            if (fast != None):
                fast = fast.next
                slow = slow.next

            # check loop
            if slow == fast:
                return True

        return False
