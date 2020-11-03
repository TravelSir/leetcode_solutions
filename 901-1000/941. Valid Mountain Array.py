"""
解题思路:
山脉数组其实就是前面是一个无重复的增序数组，后面是一个无重复的减序数组。
这题一看就只需要遍历一次就行了。需要注意的点是
1.无重复，那么前后元素的数值不能相等
2.增序数组和减序数组的交接点不能在左右边界处，即和第一个数比较时，第二个数必定大于第一个数，最后一个数和倒数第二个数比较时，最后一个数必定小于倒数第二个数
3.在1和2判断之后，那么其实我们就只需要确定在第一个凸点，也就是第一个大于后一个数的地方标记，这个时候所有的数都应该是减序的
"""


class Solution:
    def validMountainArray(self, A):
        length = len(A)
        if length < 3:
            return False
        if (A[0] > A[1]) or (A[-2] < A[-1]):
            return False
        down = False
        for i in range(1, length-1):
            if A[i] == A[i+1]:
                return False
            elif A[i] > A[i+1]:
                down = True
            else:
                if down:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().validMountainArray([0,3,2,1]))
