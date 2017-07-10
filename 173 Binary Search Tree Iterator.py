# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.p = []
        node = root
        while node:
            self.p.append(node)
            node = node.left
            

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.p
        

    def next(self):
        """
        :rtype: int
        """
        u = self.p.pop()
        node = u.right
        while node:
            self.p.append(node)
            node = node.left
        return u.val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())