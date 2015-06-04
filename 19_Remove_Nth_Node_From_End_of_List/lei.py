# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        a = b = head
        for i in xrange(n):
            b = b.next
        if b == None:
            return head.next
        while b.next:
            a = a.next
            b = b.next
        a.next = a.next.next
        return head