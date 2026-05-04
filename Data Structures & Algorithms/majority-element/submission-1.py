class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        ther=len(nums)//2
        for num in nums:
            freq[num]=freq.get(num,0)+1
            if freq[num]>ther:
                return num
        return -1