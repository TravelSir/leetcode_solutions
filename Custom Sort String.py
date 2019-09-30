"""
解题思路:
字符串S相当于给小写字母重新进行了ascll编值
我们可以用一个字典来重新存储规则, key就是小写字母，而value就是他们在字符串中的位置+1，而没有的字母自动就是0
然后快排就行了

but 针对还有一种更快的办法，桶排序
桶排序就是利用了函数的映射关系，这里的桶数就是字符串S的长度，且桶内的映射是一一对应的关系，所以桶内都不动对入桶的字母再排序，这里只需要计数就行了
而题目不要求其他字母排序，那不入桶的字母直接放入一个列表中即可
"""


# 快排
# class Solution:
#     rule = dict()
#
#     def customSortString(self, S, T):
#         self.rule = self.make_num_dict(S)
#         t_list = list(T)
#         self.quick_sort(t_list, 0, len(t_list) - 1)
#         return ''.join(t_list)
#
#     @staticmethod
#     def make_num_dict(s):
#         res = dict()
#         for i, v in enumerate(s):
#             res[v] = i+1
#         return res
#
#     def compare_letters(self, a, b):
#         return (self.rule.get(a) or 0) >= (self.rule.get(b) or 0)
#
#     def quick_sort(self, s, l, r):
#         i = l
#         j = r
#         flag = 'right'
#         if i < j:
#             tem = s[l]
#             while i < j:
#                 if flag == 'right':
#                     if self.compare_letters(tem, s[j]):
#                         s[i] = s[j]
#                         flag = 'left'
#                         i += 1
#                     else:
#                         j -= 1
#                 else:
#                     if self.compare_letters(s[i], tem):
#                         s[j] = s[i]
#                         flag = 'right'
#                         j -= 1
#                     else:
#                         i += 1
#             s[i] = tem
#             self.quick_sort(s, l, i-1)
#             self.quick_sort(s, j+1, r)


# 桶排序
class Solution:
    def customSortString(self, S, T):
        # 因为python3.5以上的字典是有序的，这里就用字典做桶
        # 如果是python3.5以下,则bucket = [ 0 for i in S]
        # 且需要定义一个字典{ v: i for i,v in enumerate(S)}来建立bucket[i] 与S中字母的顺序关系
        bucket = {s: 0 for s in S}
        others = []
        for t in T:
            if t in bucket:
                bucket[t] += 1
            else:
                others.append(t)
        for k, v in bucket.items():
            for i in range(v):
                others.append(k)
        return ''.join(others)


if __name__ == '__main__':
    sl = Solution()
    s = 'bcd'
    t = 'abcd'
    print(sl.customSortString(s, t))
