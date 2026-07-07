# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        # next should point to prev
        while curr: 
            temp = curr.next # save next one
            curr.next = prev

            prev = curr
            curr = temp
        return prev
