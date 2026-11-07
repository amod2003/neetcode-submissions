class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        cnt=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1':
                    cnt+=1
                    q=deque([(r,c)])
                    grid[r][c]='0'
                    while q:
                        x,y=q.popleft()
                        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                        for dr,dc in directions:
                            nr=x+dr
                            nc=y+dc
                            if (0<=nr<row and 0<=nc<col and grid[nr][nc]=="1"):
                        
                        
                                grid[nr][nc]='0'
                                q.append((nr,nc))
        return cnt

        