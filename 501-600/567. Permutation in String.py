"""
解题思路:
因为都只有小写字母，那其实可以借鉴桶排序的思想，将字符串每一个字符分到26个桶中统计各自的次数
其次，第二个字符串的子串长度是等于第一个字符串的，所以我们可以用滑动窗口来滑动
从第一次滑动窗口开始，我们需要统计第一次滑动窗口里的字符到26个桶中的次数，
而第一个字符串的桶每个桶的值减去这26个桶对应的次数的非负差值之和为0，则为True，不为0则是滑动窗口一次需要滑动的距离
其中一个优化点是每次计算滑动窗口的桶次数时可以不重新统计，可以按照之前的桶计数和移动距离来做加减，减少计算
第二个优化点是把数组换成字典，这样会节省ord相减得下标的时间（懒所以没改）
"""


class Solution:

    @staticmethod
    def divide_bucket(s):
        res = [0 for i in range(26)]
        for c in s:
            res[ord(c) - ord('a')] += 1
        return res

    @staticmethod
    def calculate_dif(base, window):
        res = 0
        for i in range(26):
            tem = window[i] - base[i]
            if tem > 0:
                res += tem
        return res

    @staticmethod
    def calculate_window(s, window, left, right, step):
        for i in range(step):
            if right >= len(s):
                break
            window[ord(s[left]) - ord('a')] -= 1
            window[ord(s[right]) - ord('a')] += 1
            left += 1
            right += 1
        return window

    def checkInclusion1(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return False
        left = 0
        right = left + len1

        base_bucket = self.divide_bucket(s1)
        while right <= len2:
            # 优化点: 第一次window需要计算所有，但后面的桶计数只需要减去窗口移动距离前面的字符数，加上窗口移动距离后面的字符数即可
            window = self.divide_bucket(s2[left:right])
            res = self.calculate_dif(base_bucket, window)
            if res == 0:
                return True
            else:
                left += res
                right += res
        return False

    # 优化窗口计算
    def checkInclusion(self, s1, s2):
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2:
            return False
        left = 0
        right = left + len1

        base_bucket = self.divide_bucket(s1)
        window = self.divide_bucket(s2[left:right])
        while right <= len2:
            res = self.calculate_dif(base_bucket, window)
            if res == 0:
                return True
            else:
                window = self.calculate_window(s2, window, left, right, res)
                left += res
                right += res
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion2('abc', 'bbbca'))
