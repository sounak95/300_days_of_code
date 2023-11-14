# https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1




class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None



class Solution:

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

    def addOne(self,head):
        #Returns new head of linked List.

        # reverse list
        head = self.reverseList(head)

        # add one
        carry=1
        temp = head
        while(temp.next!=None):
            sum = temp.data + carry
            digit = sum % 10
            carry = sum//10
            temp.data = digit
            if carry==0:
                break
            temp=temp.next

        # process the last node
        if carry!=0:
            sum = temp.data + carry
            digit = sum % 10
            carry = sum // 10
            temp.data = digit

            if carry!=0:
                node = Node(carry)
                temp.next = node

        head = self.reverseList(head)
        return head
