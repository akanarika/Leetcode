# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        p = head
        new_head = RandomListNode(p.label)
        q = new_head
        d = {}
        d[head] = new_head
        while p.next:
            q.next = RandomListNode(p.next.label)
            p = p.next
            q = q.next
            d[p] = q
            
        p = head
        q = new_head
        while p:
            if p.random:
                q.random = RandomListNode(d[p.random].label)
            p = p.next
            q = q.next
        
        return new_head