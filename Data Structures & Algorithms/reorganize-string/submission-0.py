import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq=Counter(s)
        heap=[(-cnt,ch)for ch,cnt in freq.items()]
        heapq.heapify(heap)
        prev=(0,'')
        res=[]
        
        while heap:
            cnt,ch=heapq.heappop(heap)
            res.append(ch)
            cnt+=1
            if prev[0]<0:
                heapq.heappush(heap,prev)
            prev=(cnt,ch)
        return "" if prev[0] < 0 else "".join(res)

        