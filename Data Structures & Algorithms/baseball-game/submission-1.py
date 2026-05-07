class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for i in range(len(operations)):
            if operations[i]=='D':
                score=ans[-1]*2
                ans.append(score)
            elif operations[i]=='C':
                ans.pop()
            elif operations[i]=='+':
                score=ans[-1]+ans[-2]
                ans.append(score)
            else:
                next_score = int(operations[i])
                ans.append(next_score)
        return sum(ans)
        