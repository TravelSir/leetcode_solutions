"""
解题思路:
动态规划
假设 cost = [1, 2, 3, 4, 5]
虽然出发点不确定，但是终点是确定的,可以想象成下楼梯
f(1) = f(2) = 0
那么顶阶之前肯定是4，5阶，假设之前在第4阶，那肯定花费是到第4阶时的最小花费加上第4阶，第5阶也是如此
那f(n) = min(f(n-2) + cost(n-2), f(n-1) + cost(n-1))
f(3) = min(f(1) + 1, f(2) + 2) = 1
f(4) = min(f(2) + 2, f(3) + 3) = 2
f(5) = min(f(3) + 3, f(4) + 4) = 4
f(6) = min(f(4) + 4, f(5) + 5) = 6
那其实登顶就是走2 4,总花费6
其实我们从下往上我们只需要记录中间两个值就行了
"""


class Solution:
    def minCostClimbingStairs(self, cost):
        lens = len(cost)
        left = right = 0
        for i in range(2, lens + 1):
            tem = right
            right = min(left + cost[i-2], right + cost[i-1])
            left = tem
        return right


if __name__ == '__main__':
    sl = Solution()
    print(sl.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
