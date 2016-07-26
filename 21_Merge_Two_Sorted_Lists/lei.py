# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(None)
        head = res
        while l1 != None or l2 != None:
            if l1 == None:
                res.next = ListNode(l2.val)
                l2 = l2.next
                
            elif l2 == None:
                res.next = ListNode(l1.val)
                l1 = l1.next
                
            else:
                v1 = l1.val
                v2 = l2.val
                print v1, v2
                if v1 < v2:
                    res.next = ListNode(v1)
                    l1 = l1.next
                else:
                    res.next = ListNode(v2)
                    l2 = l2.next
            res = res.next
        return head.next