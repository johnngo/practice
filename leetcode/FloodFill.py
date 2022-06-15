##BFS/DFS
##Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr =1 , sc = 1, color = 2
##Output [[2,2,2],[2,2,0],[2,0,1]]

def floodFill(image,sr, sc, color):
  xlen = len(image)
  ylen = len(image[0])
  ori = image[sr][sc]

  def dfs(x,y):
    if 0 <=x<xlen and 0<=y<ylen and image[x][y] == ori:
      image[x][y] = color
      dfs(x-1, y)
      dfs(x+1, y)
      dfs(x, y-1)
      dfs(x, y+1)
    
    if ori !=color:
      dfs(sr,sc)
    return image

def floodFill(image, sr, sc , color):
  r, c = len(image), len(image[0])
  ori = image[sr][sc]
  def dfs(i, j):
    if i < 0 or i>=r or j < 0 or j >=c:
      return
    if image[i][j] == color or image[i][j] != ori:
      return
    image[i][j] = color
    dfs(i+1, j)
    dfs(i-1, j)
    dfs(i, j+1)
    dfs(i, j-1)
  dfs(sr,sc)
  return image

  
