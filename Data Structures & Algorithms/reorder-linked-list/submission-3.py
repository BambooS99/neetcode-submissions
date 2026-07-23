# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        stored = []

        while curr:
            stored.append(curr)
            curr = curr.next

        l = 0
        r = len(stored)-1
        res = []

        while l < r:
            res.append(stored[l])
            res.append(stored[r])
            l += 1
            r -= 1

        if l == r:
            res.append(stored[l])

        for i in range(len(res)-1):
            res[i].next = res[i+1]
            res[-1].next = None    
        
