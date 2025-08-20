# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        p = head
        while p!= None:
            p = p.next # p: pointer
            count += 1
        if count % 2 == 0:
            count = count/2
        else:
            count = (count-1)/2

        for i in range(int(count)):
            head = head.next
        return head

        
            

