"""
解题思路:
要求时间复杂度O(log(n))就是要求用二分法嘛
首先是一个升序数组以某一点被旋转了，其实这一点就是新数组的第一位数。
当我们取数组中间数时，需要判断中数和头数的大小
1. 如果中数>头数，说明头数到中数是一个完全有序的区间，这个时候再判断target和中数的大小
    - 若target > 中数， 说明target 在右区间
    - 若target < 中数， 需要继续判断target与头数的大小
        - 若target > 头数，target 在左区间
        - 若target < 头数，target 在右区间
        - 相等则返回
    - 相等则返回
2. 如果中数<头数，说明中数到尾数是一个完全有序的区间
    - 若target < 中数， 说明target在左区间
    - 若target > 中数， 需要继续判断target与尾数的大小
        - 若target > 尾数， target 在左区间
        - 若target < 尾数， target 在右区间
        - 相等返回
    - 相等返回

"""


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (tail + head) // 2
            if target == nums[mid]:
                return mid
            if nums[mid] >= nums[head]:
                if target > nums[mid]:
                    head = mid + 1
                elif target == nums[head]:
                    return head
                elif target > nums[head]:
                    tail = mid - 1
                else:
                    head = mid + 1
            else:
                if target < nums[mid]:
                    tail = mid - 1
                elif target == nums[tail]:
                    return tail
                elif target > nums[tail]:
                    tail = mid - 1
                else:
                    head = mid + 1
        return -1


if __name__ == '__main__':
    nums = [1,3]
    target = 3
    print(Solution().search(nums, target))
