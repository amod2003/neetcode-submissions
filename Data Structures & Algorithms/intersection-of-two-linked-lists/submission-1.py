# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        slow=headA
        fast=headB
        while slow!=fast:
            slow=slow.next if slow else headB
            fast=fast.next if fast else headA
        return slow
            