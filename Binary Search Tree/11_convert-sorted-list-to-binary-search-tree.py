# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/submissions/


class ListNode(object):

  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


# Definition for a binary tree node.
class TreeNode(object):

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution(object):

  def helper(self, head_ref, n):
    if head_ref[0] is None or n <= 0:
      return None

    leftSubtree = self.helper(head_ref, n // 2)
    root = head_ref[0]
    root.left = leftSubtree
    head_ref[0] = head_ref[0].next

    rightSubtree = self.helper(head_ref, n - (n // 2) - 1)

    root.right = rightSubtree

    return root

  def getLength(self, head):
    count = 0
    temp = head
    while (temp):
      count += 1
      temp = temp.next

    return count

  def sortedListToBST(self, head):
    """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """

    head_ref = [head]
    length = self.getLength(head)
    return self.helper(head_ref, length)
