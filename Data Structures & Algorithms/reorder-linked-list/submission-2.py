# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        cur = slow.next
        slow.next = None
        prev = None

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur=next
        
        first,second = head,prev
        while second:
            next = first.next
            next_sec = second.next

            first.next = second
            second.next = next

            first = next
            second = next_sec




        