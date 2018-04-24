__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""

分析(DFS)：首先找到目标点，然后从目标点发散开[上下左右四个方向]。

然后当我们到达新的方向之后怎么办？继续DFS，那就是递归咯。

递归边界条件：数组是不越界，对应值为1，之前没有找到过这个点

用一个set保存已经递归过的点,下次遇到直接跳过

"""

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen = set() # 保存已经探查过的点
        mx = 0

        def dfs(grid, i, j):
            '''
            递归完成四个方向搜索
            '''
            area = 0
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1 and (i, j) not in seen:# 边界条件
                seen.add((i, j))
                area = 1 + dfs(grid, i - 1, j) + dfs(grid, i + 1, j) + dfs(grid, i, j - 1) + dfs(grid, i, j + 1)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    mx = max(mx, dfs(grid, i, j))

        return mx
