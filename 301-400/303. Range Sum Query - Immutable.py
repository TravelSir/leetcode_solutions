"""
解题思路:
首先数组不可变，且方法会多次调用
那其实计算过一次后我们可以保存下来供下次调用快速返回
那这就是典型的动态规划中备忘录的用法了
我们只需要记下从0到n-1之间所有的总和，就可以求出任意i到j的总和
例如: nums = [-2, 0, 3, -5, 2, -1]
记录对应和: result = [-2, -2, 1, -4, -2, -3]
那么从索引3到5: sumRange(3, 5) = result[5] - result[2] = -4 = -5 + 2 + -1这里减的是result[2]而不是result[3]是因为要包含索引3的值

"""


class NumArray:

    def __init__(self, nums):
        tem = 0
        self.result = []
        for i in nums:
            tem += i
            self.result.append(tem)

    def sumRange(self, i, j):
        return self.result[j] - (self.result[i-1] if i else 0)


if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    param_1 = obj.sumRange(0, 2)
    print(param_1)
