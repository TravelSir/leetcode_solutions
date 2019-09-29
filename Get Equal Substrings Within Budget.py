"""
解题思路:
题的意思是两个字符串相等，只能进行同一位置上的字符串替换操作，求的也是替换过后相同位置连续不断的字符相同的最大长度
首先 我们可以算出每个位置替换所需的开销
例如: p = [1,3,5,2,0,7]
然后为了不超过最大开销，我们其实求的就是 连续开销和 小于 最大开销 的最大长度
如:maxCost = 7, 符合条件的有[1,3] [5,2,0] [0,7],最长长度应该是[5,2,0]长度为3
这里遍历最长长度第一种是使用两个for循环，但时间为O(n2)
所以要使用双指针,一个标记起点，一个标记结尾。结尾不断向后，直到总和大于总开销，起点指针再往后移保证总和小于总开销
这种方式也叫滑动窗口法,只需要O(n)的时间
"""


class Solution:
    def equalSubstring(self, s, t, maxCost):
        poor_list = self.get_poor_list(s, t)
        left = 0
        right = 0
        max_num = 0
        cost = 0
        while right <= len(poor_list):
            if len(poor_list) - left < max_num:
                break
            if cost <= maxCost:
                if right == len(poor_list):
                    if max_num < right - left:
                        max_num = right - left
                else:
                    cost += poor_list[right]
                right += 1
            else:
                if max_num < right - left - 1:
                    max_num = right - left - 1
                while cost > maxCost:
                    cost -= poor_list[left]
                    left += 1
        return max_num

    @staticmethod
    def get_poor_list(s, t):
        return [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]


if __name__ == '__main__':
    sl = Solution()
    print(sl.equalSubstring("krpgjbjjznpzdfy", "nxargkbydxmsgby", 14))
    print(sl.equalSubstring("abcd" ,"cdef" ,1))
