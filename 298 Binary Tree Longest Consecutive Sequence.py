# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        d = {root: 1, None: 0}
        s = [root]
        m = 1
        while s:
            u = s.pop()
            s.extend(filter(None, (u.left, u.right)))
            if u.left:
                d[u.left] = d[u] + 1 if u.left.val == u.val + 1 else 1
            if u.right:
                d[u.right] = d[u] + 1 if u.right.val == u.val + 1 else 1
            m = max(m, d[u.left], d[u.right])
            
        return m
        