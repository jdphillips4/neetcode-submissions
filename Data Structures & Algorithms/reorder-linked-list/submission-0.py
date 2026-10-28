# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, n-1, 1, n-2, 2, n-3, ...]

        # dont move 123... move around the other ones
        # singly linked... next of 0 to last, next of 1 to 2nd last...

        # find middle of list
        # reverse second half
        # merge them alternatively

        # use slow and fast ptr to find middle of list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is end of first half (or middle but same for this)
        
        second = slow.next # head of 2nd half of list
        slow.next = None #split list
        prev = None

        # reverse 2nd half:
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge both lists
        first = head
        second = prev #start of 2nd is where left off
        while second:# second is shorter
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1 
            first = tmp1
            second = tmp2



# failed unoptimal: 
        # curr = 0
        # curr_next = 1 = curr.next
        # new_next = n-1 = iterate to end
        # new_next.next = curr_next = 1
        # curr = curr_next


        # this would iterate to the end n/2 times with the end becoming shorter and shorter
        # curr = head

        # while curr:
        #     curr_next = curr.next
            
        #     # iterate to end
        #     new_next = curr_next
        #     while new_next.next:
        #         # if not new_next.next:
        #         #     break
        #         new_next = new_next.next
        #     # new_next is now last element
        #     new_next.next = curr_next #set its next to curr_next
        #     curr = curr_next



