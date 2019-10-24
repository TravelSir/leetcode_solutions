"""
解题思路:
股票要赚钱肯定要低买高卖
那么从第1天开始，如果第二天比第一天高，那就可以第一天买，第二天卖；但是如果第二天比第一天低，那就说明第一天不能买，
因为就算第三天，第四天都比第一天高，但是中间的差值都不会比第二天到第三天，第四天大，所以想要赚最多，从第一天到第n天都是在找寻最低的价格
所以此题使用动态规划的思想，tem为购买的价格，初始等于第一天，往后遍历时遇到低于tem的，tem就变为改天的价格，遍历n次，比较找出tem小于n天时的价格差就是最大利润
时间复杂度为O(n)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_num = 0
        if len(prices) < 2:
            return max_num
        tem = prices[0]
        for i in prices[1:]:
            if tem >= i:
                tem = i
            else:
                max_num = max(max_num, i - tem)

        return max_num

