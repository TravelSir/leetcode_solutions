"""
    解题思路：
    第一种方法是枚举法，但当图形排列是个高度递减当三角形时，最坏情况下的时间复杂度是O(n²)
    所以需要使用第二种方法使用双指针法，时间复杂度只有O(n)，头指针指向第一个数，尾指针指向最后一个数。
    由于计算面积是受长高影响。无论是移动头指针还是尾指针，长都相同都减1，而下次计算面积的高度一定是小于等于不动的指针高度的，
    所以需要保留高的指针，移动短的指针。
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lens = len(height)
        max_area = 0
        i = 0
        j = lens - 1
        while i != j:
            if height[i] < height[j]:
                area = height[i] * (j-i)
                i += 1
            else:
                area = height[j] * (j-i)
                j -= 1
            if max_area < area:
                max_area = area
        return max_area


if __name__ == '__main__':
    s = Solution()
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(s.maxArea(heights))
