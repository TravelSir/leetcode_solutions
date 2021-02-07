"""
非递减数列其实就是从小到大排列的有序数列。为了满足这一点且只能改变一个数，那么当遇到一个数小于前一个数时，有这么几种情况
ex: 当数组长度小于等于2时，肯定能满足条件
1. 当nums = [1, 3, 2, 4]时，2小于3，那这里当2就需要变成大于等于3且小于等于4的数字
2. 当nums = [1, 3, 2, 2]时，2小于3，但2无法满足小于等于2且大于等于3的条件，且因为2是小于等于后面的2的，那就找前置位的3使之满足大于等于1小于等于2，这种情况是存在的
那我们这里就需要比较四个数， a, b, c, d。当c>b时就要进行以上两步判断
"""


class Solution:
    def checkPossibility(self, nums):
        length = len(nums)
        if length <= 2:
            return True
        left = 0
        change = 1
        while left < length - 1:
            if nums[left] > nums[left+1]:
                if change == 0:
                    return False
                if left+1 == length-1:
                    return True
                if nums[left] > nums[left+2]:
                    if left-1 >= 0 and nums[left-1] > nums[left+1]:
                        return False
                change -= 1
            left += 1
        return True


if __name__ == '__main__':
    print(Solution().checkPossibility([1, 3, 2, 2]))

