class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s,j=0,0
        ans=float("inf")
        n=len(nums)
        for i in range(n):
            s+=nums[i]
            while s >=target:
                ans=min(ans,i-j+1)
                s-=nums[j]
                j+=1
        return 0 if ans == float('inf') else ans
