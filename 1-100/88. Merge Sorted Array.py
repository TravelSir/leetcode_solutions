"""
解题思路:
题目的意思是把第二个增序数组合并只第一个增序数组中，仍然要保持增序。这题要求原地操作，且时间复杂度为O(m+n)
那么我们需要依次遍历nums1和nums2的数组，判断并将nums2的数插入nums1中，
根据数组的插入特性，我们知道，插入一个数，需要将插入位置后的数全部向后移动一位，那这样时间复杂度就会为O(m*n)，这显然很慢
那其实在我们把数全往后移时就已经遍历了它们，那其实假设我们第一个数开始就要后移，我们用一个中间数tem来表示nums1中需要后移的第一位数。
如果nums2中的数大于等于tem，那就代表这个数不需要后移，那如果num2的数小于tem，代表这个数开始要后移，
那这个数后面的那个数就是就变成了tem。继续与nums2比较

"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        tem = nums1[0]
        left = 0
        right = 0

        while left < m + n and right < n:
            if right == n:
                nums1[left], tem = tem, nums1[left]
            elif left - right >= m:
                nums1[left] = nums2[right]
                right += 1
            else:
                if tem < nums2[right]:
                    nums1[left] = tem
                    tem = nums1[left+1]
                else:
                    tem = nums1[left]
                    nums1[left] = nums2[right]
                    right += 1
            left += 1


if __name__ == '__main__':
    num1 = [5, 8, 0, 0, 0]
    nums2 = [1, 5, 6]
    Solution().merge(num1, 2, nums2, 3)
    print(num1)

