# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        i,j=0,len(arr)-1
        res=0
        while i<j:
            res=max(res,arr[i]+arr[j])
            i+=1
            j-=1
        return res
