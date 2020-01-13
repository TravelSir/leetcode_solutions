"""
解题思路:
这题看上去就是盛最多水容器的升级版，也可以用双指针标记左右两柱
首先我们先分析，第一根柱子为左柱，第二根柱子为右柱
1. 首先当右柱大于等于左柱时，这时无论此右柱后面还有多少右柱，都不会影响到当前水槽存储的水量了
2. 在计算水量时，需要减去中间的柱子的体积
3. 当没有右柱大于左柱时，那就相当于我们左柱时最高柱，那么此时我们可以从右边开始重复逻辑，将右边第一根柱为左柱，右柱左边第二根柱为右柱
4. 当计算完一个坑的水量后，右柱就变为了下一个坑的左柱
那么这样最好情况是最后一根柱子为最高柱，时间复杂度为O(n),最差情况第一根柱子为最高柱，时间复杂度为O(2n)
"""


class Solution:
    def trap(self, height):
        # 找出第一根柱子
        left = -1
        lens = len(height)
        for i in range(lens):
            if height[i] != 0:
                left = i
                break
        # 无柱子直接返回
        if left == -1:
            return 0

        sum = 0
        flag = False
        while left < lens - 1:
            right = left + 1
            tem = 0
            while right < lens:
                if height[left] <= height[right]:
                    _sum = height[left] * (right - left - 1) - tem
                    sum += _sum
                    left = right
                    break
                tem += height[right]
                right += 1

                # 此时左柱为最高柱
                if right == lens:
                    flag = True
            if flag:
                break

        if flag:
            _left = lens - 1
            while _left > left + 1:
                _right = _left - 1
                tem = 0
                while _right >= left:
                    if height[_left] <= height[_right]:
                        _sum = height[_left] * (_left - _right - 1) - tem
                        sum += _sum
                        _left = _right
                        break
                    tem += height[_right]
                    _right -= 1

        return sum


if __name__ == '__main__':
    height = [4,2,3]
    print(Solution().trap(height))
