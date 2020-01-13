"""
解题思路:
这题我们可以使用哈希表的方式，第一次循环将数组的值和对应的下标建立映射。因为可能存在重复值，所以哈希表所对应的下标值用数组存储
第二次循环，判断是否存在target - s[n] 的值存在与hash表中，如果存在即返回两个值所对应的下标.
这里需要注意，有可能target - s[n] = s[n]，那么就需要判断s[n]所对应的下标是否有两个，没有两个则无法成立
这样时间复杂度为O(2n), 空间复杂度为O(n)
"""


class Solution:
    def twoSum(self, nums, target):
        tem = dict()
        for i, n in enumerate(nums):
            if n in tem:
                tem[n].append(i)
            else:
                tem[n] = [i]
        for n in nums:
            m = target - n
            if m in tem:
                if m == n:
                    if len(tem[n]) > 1:
                        return [tem[n][0], tem[n][1]]
                else:
                    return [tem[n][0], tem[m][0]]


if __name__ == '__main__':
    nums = [3, 3]
    target = 6
    print(Solution().twoSum(nums, target))
