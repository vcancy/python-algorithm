__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""

假设当前层为[1,2,1]。 然后我们拷贝成两个复制副本a,b，

将0分别添加到a的开头和b的结尾; 

那么我们有[0,1,2,1]和[1,2,1,0]。 

然后，我们可以执行按对应元素相加操作，我们将有[1,3,3,1]。 

这是来自帕斯卡三角形的定义。

"""

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row
