class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.root = self.createTree(0, len(nums)-1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.updateTree(i, val, self.root)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumTree(i, j, self.root)
        
    def createTree(self, s, e):
        if s > e:
            return None
        if s == e:
            new_node = TreeNode(s, e)
            new_node.range_sum = self.nums[s]
            return new_node
        m = s + (e - s) / 2
        new_root = TreeNode(s, e)
        new_root.left = self.createTree(s, m)
        new_root.right = self.createTree(m+1, e)
        new_root.range_sum = new_root.left.range_sum + new_root.right.range_sum
        return new_root
        
    def updateTree(self, i, val, root):
        if not root:
            return 0
        if root.s == root.e == i:
            old_val = root.range_sum
            root.range_sum = val
            return val - old_val
        m = (root.s + root.e) / 2
        if i > m:
            offset = self.updateTree(i, val, root.right)
        else:
            offset = self.updateTree(i, val, root.left)
        root.range_sum += offset
        return offset
        
    def sumTree(self, i, j, root):
        if not root:
            return 0
        if root.s == i and root.e == j:
            return root.range_sum
        m = (root.s + root.e) / 2
        if i > m:
            return self.sumTree(i, j, root.right)
        if j <= m:
            return self.sumTree(i, j, root.left)
        return self.sumTree(i, m, root.left) + self.sumTree(m+1, j, root.right)
        
class TreeNode(object):
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.range_sum = 0
        self.left = None
        self.right = None
        
'''
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = [0]
        for i in range(len(nums)):
            if i == 0:
                self.sums.append(nums[0])
            else:
                self.sums.append(self.sums[i] + nums[i])
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        old_val = self.nums[i]
        self.nums[i] = val
        for j in range(i, len(self.nums)):
            self.sums[j+1] += val - old_val
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1] - self.sums[i]
'''

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)