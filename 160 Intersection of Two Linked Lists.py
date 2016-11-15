# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import gc

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        
        while p1 is not p2:
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next
            
        gc.collect()
        
        return p1
        