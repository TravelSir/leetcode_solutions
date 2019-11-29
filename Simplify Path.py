"""
解题思路:
简化绝对路径, ..返回上级, 这后进后出的模式, 不就是栈吗
遇到目录入栈，遇到..出栈
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        res = []
        for a in arr:
            if a == '..':
                try:
                    res.pop()
                except Exception:
                    pass
            elif a == '.':
                pass
            elif a:
                res.append(a)
        return '/' + '/'.join(res)


if __name__ == '__main__':
    sl = Solution()
    print(sl.simplifyPath("/a/./b/../../c/"))
