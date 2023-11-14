# https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1


'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''


class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):

        fast = head
        slow = head

        while (fast != None):
            fast = fast.next
            if (fast != None):
                fast = fast.next
                slow = slow.next

            if slow == fast:
                break

        if fast == None:
            return None

        slow = head

        while (fast != slow):
            fast = fast.next
            slow = slow.next

        # fetch the starting point of loop
        startingPoint = slow

        temp = startingPoint

        while(temp.next!=startingPoint):
            temp = temp.next

        temp.next = None
