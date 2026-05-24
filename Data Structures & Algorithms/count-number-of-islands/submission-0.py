class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        count = 0
        drc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(r, c, visited):
            for d in drc:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1' and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    dfs(nr, nc, visited)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and visited[r][c] == 0:
                    count += 1
                    dfs(r, c, visited)
            
        return count