"""
解题思路:
首先这题的要求是在原地修改且不改变顺序，且返回新长度，那对于数组来说移除元素其实就本质上是交换元素，将需要移除的元素和不需要移除的元素有序地交换到数组末尾
那这个时候我们就可以使用双指针的方式，左指针从0开始，右指针从1开始，左指针判断指向的元素是否需要移除，如不需要移除，则两个指针都往后移。
如左指针指向的元素需要移除，那么就要把该元素后的第一个非移除元素补上来，那么就要开始判断右指针指向的元素是否也需要移除，直到右指针指向一个非移除元素，再交换左右指针的值后，再继续以上步骤。
而要计算交换后的有效元素的新长度，那么就需要确定交换完后左指针指向的是最后一个非移除元素还是一个移除元素。这个其实可以判断。
当需要交换时，右指针指向了最后一个元素且最后一个元素也为移除元素时，那么右指针就移不动了，左指针指向排序后的第一个移除元素，长度就为左指针大小
当右指针指向了最后一个元素且元素不为移除元素时，交换后，左指针会右移，这时候循环结束，左指针依旧指向排序后的第一个移除元素
第三种情况是数组完全没有非移除元素，那么左指针肯定指向的是一个非移除元素，这个时候长度就为左指针大小加1
"""


class Solution:
    def removeElement(self, nums, val):
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return 0 if val == nums[0] else 1

        left = 0
        right = 1
        while right < length:
            if nums[left] == val:
                while right < length:
                    if nums[right] == val:
                        right += 1
                    else:
                        nums[left] = nums[right]
                        nums[right] = val
                        left += 1
                        right += 1
                        break
            else:
                left += 1
                right += 1
        return left + (0 if nums[left] == val else 1)

    # LeetCode上的一个更简介的解法是: 定义一个没有移除值的最终数组为nums[0...i], 然后遍历数组去维护定义。也是双指针，但不是左右指针的概念，而是两个指针指向两个数组开头，而只是这两个数组恰好重合了。
    # 从这个解法我学到了一个小技巧就是: 当你要做遍历比较的时候，要得到满足条件长度时，初始化i为-1开始计算，在满足条件时，先加i，再交换值，这样能保证i一定为满足条件数-1。
    def removeElementEasy(self, nums, val):
        length = len(nums)
        i = -1
        j = 0
        while j <= length - 1:
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1
