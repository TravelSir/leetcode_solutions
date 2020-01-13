"""
解题思路:
判断不含有重复字符的最长字串，那么我们就需要存储字串来进行比较。这样在自身上面有区间的操作可以用到双指针，滑动窗口算法
最开始左右指针都指向第一位。右指针每次向右移动一位，判断右指针所指向的字符是否在之前的字串中存在
如果接下来的字符不存在于字串中，那么这个字符就加入字串，右指针继续右移
如果接下来的字符存在于字串中，那就记录下当前字串的长度，与最大字串长度比较取最大。而左指针就指向找到的字符的位置的后一位，右指针继续移动
当循环完成后，需要最终判断一下最后的字串是否为最长字串
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 1
        lens = len(s)
        if lens < 2:
            return lens
        max_num = 1
        while right < lens:
            index = s[left:right].find(s[right])
            if index == -1:
                right += 1
            else:
                poor = right - left
                if max_num < poor:
                    max_num = poor
                left += index + 1
                right += 1
        poor = right - left
        if max_num < poor:
            max_num = poor
        return max_num


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
