# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = head
        vals = []

        while cur is not None:
            vals.append(cur.val)
            cur = cur.next

        vals.pop(len(vals) - n)

        if not vals:
            return None

        res = ListNode(vals[0])
        cur = res

        for i in range(1, len(vals)):
            cur.next = ListNode(vals[i])
            cur = cur.next

        return res