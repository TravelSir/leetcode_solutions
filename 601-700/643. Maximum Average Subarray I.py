"""
这题很简单，从头开始遍历的，长度为k的滑动窗口一直往后滑动，不断比较总数就行了，最后再由最大总数求的平均数。时间复杂度为O(n)
"""


class Solution:
    def findMaxAverage(self, nums, k):
        left = 0
        length = len(nums)
        _max = sum(nums[left:left+k])
        tem = _max
        left += 1
        while left + k <= length:
            tem = tem - nums[left-1] + nums[left+k-1]
            _max = _max if _max > tem else tem
            left += 1
        return _max / k


if __name__ == '__main__':
    nums = [0,4,0,3,2]
    k = 1
    print(Solution().findMaxAverage(nums, k))

