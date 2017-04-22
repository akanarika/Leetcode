# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        root = None
        root = self.addToBST(root, nums)
        return root

    def addToBST(self, root, a):
        if not a:
            return
        n = len(a)
        mid = (n - 1) / 2
        root = TreeNode(a[mid])
        if mid != 0:
            root.left = self.addToBST(root.left, a[:mid])
        if mid != n - 1:
            root.right = self.addToBST(root.right, a[mid+1:])
        return root
