def minPathSum(grid):
    def minPath(grid, row, col, path_sum = 0):
        if row > len(grid)-1 or col > len(grid[0])-1:
            return float('inf')
        path_sum += grid[row][col]
        if row == len(grid)-1 and col == len(grid[0])-1:
            return path_sum
        return min(minPath(grid, row, col+1, path_sum),
        minPath(grid, row+1, col, path_sum))
    return minPath(grid, 0, 0)

def minPathSum1(grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

print(minPathSum([[1,2],[1,1]]))


