# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        phead = ListNode(None)
        qhead = ListNode(None)
        p = head
        q = head.next
        phead.next = p
        qhead.next = q
        while p.next.next and q.next.next:
            pt = p.next.next
            qt = q.next.next
            p.next = pt
            q.next = qt
            p = p.next
            q = q.next
        if p.next and p.next.next:
            p.next = p.next.next
            p = p.next
        if q.next and q.next.next:
            q.next = q.next.next
            q = q.next
        q.next = None
        p.next = qhead.next
        return phead.next