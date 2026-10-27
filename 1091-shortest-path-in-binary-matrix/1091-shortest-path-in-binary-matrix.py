class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1

        q = deque([(0, 0, 1)])
        grid[0][0] = 1

        while q:
            r, c, d = q.popleft()
            if (r, c) == (n-1, n-1):
                return d

            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if 0 <= i < n and 0 <= j < n and grid[i][j] == 0:
                        grid[i][j] = 1
                        q.append((i, j, d+1))

        return -1
