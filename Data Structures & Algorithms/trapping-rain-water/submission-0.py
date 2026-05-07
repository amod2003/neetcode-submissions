class Solution:
    def trap(self, height: List[int]) -> int:
        h=height
        n=len(h)
        leftMax=[0]*n
        rightMax=[0]*n
        leftMax[0]=h[0]
        for i in range(1,n):
            leftMax[i]=max(leftMax[i-1],h[i])
        rightMax[n-1]=h[n-1]
        for i in range(n-2,-1,-1):
            rightMax[i]=max(rightMax[i+1],h[i])
        res=0
        for i in range(n):
            res+=min(leftMax[i],rightMax[i])-h[i]
        return res