

class Solution:
    def __init__(self, grid,M,N):
        self.grid = grid
        # 当前区域的人数
        self.cnt = 0
        # 保存所有区域中的人数，返回其长度，及其最大值
        self.dp = []
        self.M = M
        self.N = N

    def dfs(self, i, j):
        if 0 <= i < self.M and 0 <= j < self.N:
            if self.grid[i][j] == 1:
                self.cnt += 1
                # 经过的点就置0
                self.grid[i][j] = 0
                # (i-1,j-1) (i-1,j) (i-1,j+1)
                # (i,j-1)   (i,j)   (i,j+1)
                # (i+1,j-1) (i+1,j) (i+1,j+1)
                # 8个方向搜索
                self.dfs(i - 1, j)
                self.dfs(i + 1, j)
                self.dfs(i, j - 1)
                self.dfs(i, j + 1)
                # self.dfs(i - 1, j - 1)
                # self.dfs(i + 1, j + 1)
                # self.dfs(i + 1, j - 1)
                # self.dfs(i - 1, j + 1)

    def solve(self):
        for i in range(M):
            for j in range(N):
                if self.grid[i][j] == 1:
                    # 每找到一个新区域就清0，因为被搜索过的1都置0了，所以新区还是1
                    self.cnt = 0
                    self.dfs(i, j)
                    if self.cnt > 0:
                        self.dp.append(self.cnt)

        return len(self.dp), max(self.dp)

if __name__ == '__main__':
    grid =  [[1,0,0,1,1],
             [1,0,0,1,1],
             [0,0,1,0,0],
             [0,0,1,0,0],
             [0,0,1,0,0]]

    M = N = 5
    result = Solution(grid,M,N)
    a,b = result.solve()
    print(a,b)