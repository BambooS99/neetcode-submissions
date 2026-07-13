# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        stored = []

        while curr:
            stored.append(curr)
            curr = curr.next

        rm = len(stored) - n
        if rm == 0:
            return head.next

        stored[rm-1].next = stored[rm].next
        return head