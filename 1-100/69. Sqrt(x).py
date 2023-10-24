"""
给定一个数，返回他的算术平方根的整数部分。
最暴力的方式就是从1*1一直算到n*n，当n*n大于x时，返回n-1。
但是这样的时间复杂度为O(根号x)，所以我们可以使用二分法查找来进行优化。
二分法查找的时间复杂度为O(logn)。由于我们要找的是整数部分，所以最后需判断mid*mid，大于则返回mid-1。
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x
        while left < right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        mid = min(left, right)
        if mid * mid > x:
            return mid - 1
        return mid


if __name__ == '__main__':
    print(Solution().mySqrt(144))
