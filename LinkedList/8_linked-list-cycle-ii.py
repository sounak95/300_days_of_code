# https://leetcode.com/problems/linked-list-cycle-ii/description/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head

        while(fast!=None):
            fast = fast.next
            if(fast!=None):
                fast = fast.next
                slow=slow.next

            if slow==fast:
                break

        if fast==None:
            return None

        slow=head

        while(fast!=slow):
            fast = fast.next
            slow=slow.next

        return slow # return fast

