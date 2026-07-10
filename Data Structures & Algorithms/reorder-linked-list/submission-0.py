# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tracked = []
        curr = head
        
        while curr:
            tracked.append(curr)
            curr = curr.next

        res = []
        l = 0
        r = len(tracked)-1
        while l < r:
            res.append(tracked[l])
            res.append(tracked[r])
            l += 1
            r -= 1
        if l == r:
            res.append(tracked[l])
            
        for i in range(len(res)-1):
            res[i].next = res[i+1] 
        res[-1].next = None       
        print(res)

        