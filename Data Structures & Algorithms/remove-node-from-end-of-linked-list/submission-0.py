# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # from end, so n=1 removes last, n= 2 removes 2nd to last

        # linked list, so dont know length
        # given n tho, can have 2 ptrs where one trails behind
        # need to use dummy node before list to make adjustments
        # then return dummy.next
        dummy = ListNode(0,head)
        l = dummy
        r = head

        # give r a head start of length n
        while n>0:
            r = r.next # if n is 1, r is r.next
            n -= 1

        while r:
            l = l.next
            r = r.next
        
        # beacause of dummy node, l is before one to remove
        l.next = l.next.next 

        
        return dummy.next

        