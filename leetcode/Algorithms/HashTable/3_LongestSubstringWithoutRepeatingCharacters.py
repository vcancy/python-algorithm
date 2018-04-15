__author__ = "vcancy"

#/usr/bin/python
#-*-coding:utf-8-*-

"""
定义一个窗口[ i, j ]，判断下一个字符是否在窗口里，如果不在，加进去；
如果在，左窗口向右缩减到不包含该重复项，右窗口加一。判断最大值得出结果。
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = j = 0
        slid = set()
        while i < len(s) and j < len(s):
            if s[j] not in slid:
                slid.add(s[j])
                j += 1
                count = max(len(slid), count)
            else:
                slid.remove(s[i])
                i += 1

        return count