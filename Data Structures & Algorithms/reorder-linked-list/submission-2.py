# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        checker = []

        while curr:
            checker.append(curr)
            curr = curr.next
        
        res = []
        l,r = 0, len(checker)-1

        while l < r:
            res.append(checker[l])
            res.append(checker[r])
            l+=1
            r-=1
        if l == r:
            res.append(checker[l])
        
        for i in range(len(res)-1):
            res[i].next = res[i+1]
            res[-1].next = None