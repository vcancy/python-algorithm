__author__ = "vcancy"

#/usr/bin/python
#-*-coding:utf-8-*-

"""
分析：
从最低位+1，当加后值>10,上一位继续+1，若<10则返回，最后需要检测是否有最高位需要进位的情况
"""
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            a,b=divmod(digits[i]+1,10)
            if a==0:
                digits[i]=b
                return digits
            else:
                digits[i]=b
        if digits[0] ==0:#最高位待进位
            r = [0]*(len(digits)+1)
            r[0] =1
            return r
        return   digits