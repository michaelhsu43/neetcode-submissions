class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        drc = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r, c, visited, pos):
            print(pos)
            if pos == len(word) :
                print("HI")
                return True
            for d in drc:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < m  and 0 <= nc < n and visited[nr][nc] == 0 and board[nr][nc] == word[pos]:
                    print("nr: ", nr, "nc: ", nc)
                    visited[nr][nc] = 1
                    if dfs(nr, nc, visited, pos + 1):
                        return True
                    visited[nr][nc] = 0
                

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    visited = [[0] * n for _ in range(m)]
                    visited[r][c] = 1
                    
                    if dfs(r, c, visited, 1):
                        return True
                
        
        return False