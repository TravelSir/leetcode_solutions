"""
解题思路:
超简单的因式分解，
只需要将n，um先除以2除到不能整除，然后再除以3，以此类推，直到整除结果为1或除数超过了5，最后判断整除结果是否为1即可
"""


class Solution:
    def isUgly(self, num):
        factor = [2, 3, 5]
        i = 0
        while num != 1:
            if i >= len(factor):
                break
            if num < factor[i]:
                break
            if num % factor[i] == 0:
                num /= factor[i]
            else:
                i += 1
        if num == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    sl = Solution()
    print(sl.isUgly(8))
