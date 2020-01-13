"""
解题思路:
一道看上去十分简单的题，从第一位开始，每次循环数组去看所有字符串是否有该字符就行了，但时间复杂度最坏在O(n*m), n是数组长度，m是单个字符串的长度
其实，我们转变一下思路，我们可以把第一个字符串当做初始前缀，去和第二个字符串比较出相同前缀，这样我们的循环需要n次，但m却大大减小了
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        mod = strs[0]
        for i in strs[1:]:
            tem = ""
            for j in range(min(len(mod), len(i))):
                if mod[j] != i[j]:
                    break
                tem += mod[j]
            mod = tem
            if not mod:
                break
        return mod
