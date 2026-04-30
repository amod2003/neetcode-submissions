class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=float('inf')
        l=0
        for right in range(k-1,len(nums)):
            ans=min(nums[right]-nums[l],ans)
            l+=1
        return ans