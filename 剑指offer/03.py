"""
找出数组中任意一个重复的数字。
这道题有多种解法：
首先最直接的方法，我们可以先对数组进行一次快排，排序完成后再从头开始往后判断是否重复。这种算法的时间复杂度是O(nlog(n))，空间复杂度是O(n)
如果为了更快，那就使用哈希表，时间复杂度是O(n), 空间复杂度是O(n)

但我们注意题的一个条件: 一个长度为n的数组，而所有数字都在0到n-1范围内，那么必定有至少一个数是重复的。
从我们最开始想到的对数组进行快排，说明一个有序的数组查找是最方便的。那根据题目的限定，数字的值一定不会超过数组的长度。
那么我们也可以用下标存储对应的数字，每个不重复的数字都能在对应的下标存储下，那么当一个数字对应的下标已经有值且与这个数相等，说明这个数就是重复数字
这也是一种排序思想，是桶排序的思想。这样我们使用的时间复杂度是O(n),但因为只对数组本身操作,空间复杂度变为了O(1)
"""


class Solution:
    def findRepeatNumber(self, nums):
        model = 'bucket'

        # 快排
        if model == 'quick':
            nums.sort()
            tem = nums[0]
            for n in nums[1:]:
                if tem == n:
                    return n
                tem = n

        # 哈希表
        elif model == 'hash':
            n_dict = dict()
            for n in nums:
                if n_dict.get(n):
                    return n
                n_dict[n] = True

        # 桶排序
        else:
            for i in range(len(nums)):
                while i != nums[i]:
                    if nums[i] == nums[nums[i]]:
                        return nums[i]
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]


if __name__ == '__main__':
    print(Solution().findRepeatNumber([2, 3, 4, 5, 1, 0, 5]))

