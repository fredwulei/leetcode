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
            return
        
        def merge(l1, l2):
            # print l1.val, l2.val
            s = h = ListNode(-1)
            while l1 and l2:
                if l1.val < l2.val:
                    h.next = l1
                    l1 = l1.next
                else:
                    h.next = l2
                    l2 = l2.next
                h = h.next
            if not l1:
                h.next = l2
            else:
                h.next = l1
            return s.next
        
        while len(lists) >= 2:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            l = merge(l1, l2)
            lists.append(l)
        return lists[0]
        