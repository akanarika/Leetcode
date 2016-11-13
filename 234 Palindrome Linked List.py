# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True
        
        p1 = head
        p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        s = []
        p3 = head
        while p3 != p1:
            s.append(p3.val)
            p3 = p3.next
        
        if p2:
            p1 = p1.next
        
        while s:
            u = s.pop()
            if u != p1.val:
                return False
            else:
                p1 = p1.next
        return True
            