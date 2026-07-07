# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        # can either make new one or just put them into list1

        # could be case where list1 is empty

        dummy = ListNode()
        tail = dummy
        while curr1 and curr2: # while these are not null
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        
        #case where one is empty
        if curr1:
            tail.next = curr1
        elif curr2:
            tail.next = curr2
        
        #ignore nummy head
        return dummy.next