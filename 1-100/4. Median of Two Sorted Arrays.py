"""
解题思路:
首先这是两个有序数组, 且要求时间复杂度为O(log(m+n))，那么肯定就要用到二分查找的思想
首先寻找两个数组共同的中位数，那么其实就是寻找nums1数组中的某个点m，和nums2数组中的某个点n
使nums1和nums2以m，n为中点的左子组的长度之和等于他们右子组的长度之和。
left                        |     right
nums1[0], ..., nums1[m-1]   |   nums1[m], ...
nums2[0], ..., nums2[n-1]   |   nums2[n], ...

这样需要满足 max(left) <= min(right)
也就是nums1[m-1] <= nums2[n], 且nums2[n-1] <= nums1[m]

如果nums1[m] < nums2[n-1], 说明m需要减小，n需要增大
如果nums2[n] < nums1[m-1], 说明n需要减小，m需要增大

那如果两个条件同时存在，那m, n如何变化呢
其实我们只需要比较nums1[m-1]和nums2[n-1]中谁更大就行
比如nums1[m-1] >= nums[n-1], 因为nums1[m] >= nums1[m-1], 所以nums1[m]必定大于nums[n-1]。所以这时只需判断nums2[n]与num1[m-1]即可

假设第一次n, m都是两数组的中点
假设nums2[n] < nums2[m-1]了, 那么n的取值范围就应该在0到n-1之间了，二分法的话也就是nums2就得向左移动了n/2，
那m要对应向右移动n/2，而m右区间的总长度为m，如果nums2的长度是nums1的长度的两倍以上，这样nums1就会不够而越界。
所以我们二分选择的应该是短的那个数组，然后再让长的数组配合移动，这样才不会越界
而且我们需要一个取值范围来记录短数组下次移动的区间中点是什么。
比如[begin: end], 初始begin = 0, end = n, i = (end - begin + 1) // 2
当nums2[n] < nums2[m-1]时，end = i-1
当nums1[m] < nums2[n-1]时，begin = i+1
i = (end - begin + 1) // 2
直到begin > end为止。

但是这其中会有特殊情况，
当n为0时，这就表示短数组全在右区间
当n等于数组长度-1时，这就表示短数组全在左区间
所以这个时候中位数就在长数组内来确定了

所以由此可见时间复杂度应该为log(min(m,n))
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) < len(nums2):
            mi = nums1
            ma = nums2
        else:
            mi = nums2
            ma = nums1
        leni = len(mi)
        lena = len(ma)
        # 分割的两边区间长度
        mid = (leni + lena + 1) // 2

        begin, end = 0, leni
        while begin <= end:
            left = (end + begin) // 2
            right = mid - left
            if left > 0 and mi[left - 1] > ma[right]:
                # left需要减小
                end = left - 1

            elif left < leni and ma[right - 1] > mi[left]:
                # left需要增大
                begin = left + 1
            else:
                if left == 0:
                    # 说明小数组全在左区间
                    max_left = ma[right - 1]
                elif right == 0:
                    # 当数组长度相等时大数组全在左区间
                    max_left = mi[left - 1]
                else:
                    max_left = max(ma[right - 1], mi[left - 1])

                if (leni + lena) % 2:
                    return max_left

                if left == leni:
                    # 说明小数组全在右区间
                    min_right = ma[right]
                elif right == lena:
                    # 当数组长度相等时大数组全在右区间
                    min_right = mi[left]
                else:
                    min_right = min(ma[right], mi[left])

                return (max_left + min_right) / 2


if __name__ == '__main__':
    nums1 = [3, 4]
    nums2 = [1, 2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
