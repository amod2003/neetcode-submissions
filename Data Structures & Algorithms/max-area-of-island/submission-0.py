from collections import defaultdict, deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        max_area=0
       
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    q=deque([(r,c)])
                    grid[r][c]=0
                    area=0

                    while q:
                        x,y=q.popleft()
                        area+=1
                        dire=[(1,0),(-1,0),(0,1),(0,-1)]
                        for dr,dc in dire:
                            nr=dr+x
                            nc=dc+y
                            if(0<=nr<row and 0<=nc<col and grid[nr][nc]==1):
                                grid[nr][nc]=0
                                q.append((nr,nc))
                            max_area=max(area,max_area)
        return max_area