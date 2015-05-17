# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
    	l = ListNode(None)
    	head = l
    	carry = 0
    	e1 = l1
    	e2 = l2
    	while e1!=None or e2!=None or carry!=0:
    		v1 = e1.val if e1!=None else 0
    		v2 = e2.val if e2!=None else 0
    		d = v1+v2+carry
    		a = divmod(d,10)
    		carry = a[0]
    		l.next = ListNode(a[1])
    		l = l.next
    		e1 = e1.next if e1!=None else None
    		e2 = e2.next if e2!=None else None
    	return head.next