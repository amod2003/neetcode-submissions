class Solution:
    def maxDifference(self, s: str) -> int:
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        odd=[]
        even=[]

        for f in freq.values():
            if f%2==1:
                odd.append(f)
            else:
                even.append(f)
        return max(odd) - min(even)