__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""

分析：复制矩阵，遍历矩阵中的每个元素，找到元素周围存在的元素(注意数组越界),

赋值到复制矩阵对应位置

"""

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        x_len = len(M)
        y_len = len(M[0]) if M else 0

        res = [[0] * y_len for _ in M] # 复制矩阵
        for i in range(x_len):
            for j in range(y_len):
                neighbor = [
                    M[_x][_y]
                    for _x in (i - 1, i, i + 1)
                    for _y in (j - 1, j, j + 1)
                    if 0 <= _x < x_len and 0 <= _y < y_len # 判断边界
                ]
                res[i][j] = sum(neighbor) // len(neighbor)
        return res
