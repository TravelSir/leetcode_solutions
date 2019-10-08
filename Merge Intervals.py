"""
解题思路:
判断区间是否重合其实就是两个区间同时满足一个区间的右边界大于等于另一个区间的左边界
那么我们可以先进行排序，将左边界顺序排序后只需要O(n)的时间就可以合并完成,为更快时间,新建列表存储合并结果
"""


class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            if right < intervals[i][0]:
                res.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
            elif right < intervals[i][1]:
                right = intervals[i][1]
        res.append([left, right])
        return res

# 笨办法，未排序两层循环
# class Solution:
#     def merge(self, intervals):
#         i = 0
#         flag = True
#         while i < len(intervals) - 1:
#             for j in range(i+1, len(intervals)):
#                 a = intervals[i]
#                 b = intervals[j]
#                 res = self.merge_two_intervals(a, b)
#                 if res:
#                     intervals[i] = res
#                     intervals.pop(j)
#                     flag = False
#                     break
#                 else:
#                     flag = True
#                     j += 1
#             if flag:
#                 i += 1
#         return intervals
#
#     @staticmethod
#     def merge_two_intervals(a, b):
#         if a[1] >= b[0] and a[0] <= b[1]:
#             if a[1] < b[1]:
#                 a[1] = b[1]
#             if a[0] > b[0]:
#                 a[0] = b[0]
#             return a
#         if b[1] >= a[0] and b[0] <= a[1]:
#             if b[1] < a[1]:
#                 b[1] = a[1]
#             if b[0] > a[0]:
#                 b[0] = a[0]
#             return b
#         return False


if __name__ == '__main__':
    intervals = [[1, 4], [0, 4]]
    sl = Solution()
    print(sl.merge(intervals))
