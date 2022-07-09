# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the 
# island must be connected 4-directionally.



def maxAreaOfIsland(grid):
  m,n = len(grid), len(grid[0])

  def dfs(i, j):
    if 0 <= i < m and 0 <=j < n and grid[i][j]:
      grid[i][j] = 0
      return 1 + dfs(i-1, j) + dfs(i, j + 1) + dfs(i + 1,j) + dfs(i, j - 1)
    return 0

  areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
  return max(areas) if areas else 0
