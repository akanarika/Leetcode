# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        head = lists[0]
        
        while len(lists) > 1:
            a = lists.pop()
            b = lists.pop()
            head = self.merge2Lists(a, b)
            lists.insert(0, head)
            
        return head
        
    def merge2Lists(self, a, b):
        head = p = ListNode(0)
        p1 = a
        p2 = b
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
            p.next = None
        p.next = p1 or p2
        return head.next
        
            