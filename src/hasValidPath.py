class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        
        visited = set()
        
        def dfs(r: int, c:int, balance: int) -> bool:
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1
            
            if balance < 0:
                return False
            
            passos_restantes = (m - 1 - r) + (n - 1 - c)
            if balance > passos_restantes:
                return False
            
            if r == m - 1 and c == n - 1:
                return balance == 0
            
            estado = (r, c, balance)
            if estado in visited:
                return False
            
            visited.add(estado)
            
            if c + 1 < n and dfs(r, c + 1, balance):
                return True
            
            if r + 1 < m and dfs(r + 1, c, balance):
                return True
            
            return False
        return dfs(0, 0, 0)