# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.sort(head)
        
    def sort(self, head):
        if not head or not head.next:
            return head
        if not head.next.next:
            if head.val > head.next.val:
                c = head.next
                c.next = head
                head.next = None
                head = c
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        c = slow.next
        slow.next = None
        return self.merge(self.sort(head), self.sort(c))
        
    def merge(self, a, b):
        p = ListNode(None)
        head = p
        pa = a
        pb = b
        while pa and pb:
            if pa.val < pb.val:
                c = pa
                pa = pa.next
            else:
                c = pb
                pb = pb.next
            p.next = c
            p = p.next
        p.next = pa or pb
        return head.next
                
            