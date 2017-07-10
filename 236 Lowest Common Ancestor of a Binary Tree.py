# Definition for a binary tree node.
import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        d = {}
        self.hasNode(root, p, q, d)
        s = collections.deque([root])
        res = None
        while s:
            u = s.popleft()
            if d[u] == 2:
                res = u
            s.extend(filter(None, [u.left, u.right]))
        return res
        
    def hasNode(self, node, p, q, d):
        if not node:
            return 0
        d[node] = self.hasNode(node.left, p, q, d) + self.hasNode(node.right, p, q, d) + int(node.val == p.val or node.val == q.val)
        return d[node]

s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.right = d
c.left = e
print s.lowestCommonAncestor(a, b, e).val
        