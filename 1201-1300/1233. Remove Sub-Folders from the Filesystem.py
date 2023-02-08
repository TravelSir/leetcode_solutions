"""
解题思路:
这道题最简单的方式就是将数组排序后遍历判断, 因为排序后公共前缀是相同的。
所以a目录开头的一定会排在b目录前。所以排序后的第一个目录肯定不是子文件夹。
那么依次判断，若第二个字符串的前缀等于第一个字符串，那么说明第二个字符串为子文件夹，可以直接排除
若不等，则说明第二个文件夹也不为子文件夹
唯一的小坑是判断前缀想等后要判断子文件夹的下一个字符是否为/,因为有a, ab这种名称
"""
from typing import List


class Trie:
    def __init__(self, val):
        self.child = dict()
        self.ref = -1


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0]]
        for i in range(1, len(folder)):
            if len(folder[i]) <= len(result[-1]):
                result.append(folder[i])
                continue
            if not (result[-1] == folder[i][:len(result[-1])] and folder[i][len(result[-1])] == '/'):
                result.append(folder[i])
        return result


if __name__ == '__main__':
    print(Solution().removeSubfolders(folder=["/a/b/c","/a/b/ca","/a/b/d"]))