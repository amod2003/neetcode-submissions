class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeTopen={")":"(","]":"[","}":"{"}

        for c in s:
            if c in closeTopen:
                if not stack or stack.pop()!=closeTopen[c]:
                    return False
            else:
                stack.append(c)
        return len(stack)==0