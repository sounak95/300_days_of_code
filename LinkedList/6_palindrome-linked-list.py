# https://leetcode.com/problems/palindrome-linked-list/description/

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

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = head
        fast = head

        while (fast.next != None):
            fast = fast.next
            if (fast.next != None):
                fast = fast.next
                # main yaha keh skta hu k fast ne 2 step chal liye h
                # ab slow ko bhi chalwao ek step
                slow = slow.next

        return slow

    def compareList(self, head1, head2):

        while(head1!=None and head2!=None):
            if head1.val!=head2.val:
                return False
            else:
                head1=head1.next
                head2=head2.next

        return True

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # break into 2 havles
        midNode = self.middleNode(head)
        head2 = midNode.next
        midNode.next = None

        # reverse second half
        head2 = self.reverseList(head2)

        # compare both list
        ans = self.compareList(head, head2)
        return ans