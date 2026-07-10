class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        ther=len(nums)//3
        res=[]
        for k,v in freq.items():
            if v>ther:
                res.append(k)
        return res
        