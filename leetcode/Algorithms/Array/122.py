__author__ = "vcancy"


# /usr/bin/python
# -*-coding:utf-8-*-

"""
这一题不再限制买卖的次数,只要价格比前一天高就可以前一天买入、后一天卖出了。
"""
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                max_profit += prices[i] - prices[i - 1]

        return max_profit
