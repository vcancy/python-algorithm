__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""

分析：每一方向由左上到右下的对角线上具有相同元素即是i行j列元素对应的i+1行j+1列相等。

"""

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
