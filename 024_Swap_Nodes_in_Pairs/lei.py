# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        if head.next == None:
            return head
        
        dummy = ListNode(-1)
        now = dummy
        
        while head and head.next:
            # print head.val
            odd = head
            even = head.next
            now.next = even
            odd.next = even.next
            even.next = odd
            now = odd
            head = odd.next
        return dummy.next