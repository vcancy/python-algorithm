__author__ = "vcancy"

#/usr/bin/python
#-*-coding:utf-8-*-
"""
分析：
记录两个值：
r：到目前位置最大的利润，默认0
lower：到目前位置最小的股票价格，默认第一个
遍历数据，当前价格-lower和r比较取最大利润，lower和当前价格比较取最小价格
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        r = 0
        lower = prices[0]
        for i in range(1, len(prices)):
            r = max(prices[i] - lower, r)
            lower = min(prices[i], lower)
        return r
