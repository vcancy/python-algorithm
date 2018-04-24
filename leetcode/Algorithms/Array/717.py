__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""

分析：遍历一遍数组内容，遇到1则前进两步（因为1开头一定是包含两个比特的），遇到0则前进一步。

遇到1则令结果变量为false，遇到0则令结果变量为true。

当遍历完时

如果最后走的一步恰好为遇到1时的两步，则返回为false，

如果最后走的一步是遇到0时的一步，则返回为true。


"""

class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        ret = None
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                ret = False
            else:
                i += 1
                ret = True

        return ret
