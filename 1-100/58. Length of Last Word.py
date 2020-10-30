"""
解题思路:
这题唯一需要注意的是末尾的空格
"""


class Solution:
    def lengthOfLastWord(self, s):
        length = 0
        flag = False
        for i in s:
            if i == ' ':
                flag = True
            else:
                if flag:
                    length = 0
                    flag = False
                length += 1
        return length


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("  w "))
