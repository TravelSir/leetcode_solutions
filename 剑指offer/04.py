"""
n*m的二维数组满足所有行和列都是递增，那么对于目标值来说
1. 当目标值大于第一行的第x个数也就是x列的数时，那么目标值肯定不在大于x列的所有列中，因为x列到第n列的所有数都会大于x列的第一行的数，也就是左上角的数，
所以目标数肯定就在第1列到第x-1列的矩阵中。
2. 当目标值小于第y行的最后一列的数时，那说明目标值在第y行到最后一行之间，因为如果目标值大于y行最后一列数，这个数时右下角的数，它是大于所有左上区域的数的
3. 那综合上述两条，我们可以首先从第一行开始，确定右边界，然后再根据右边界找出上边界。
"""


class Solution:
    def findNumberIn2DArray(self, matrix, target):
        if not matrix:
            return False

        m = len(matrix)  # 总行数
        n = len(matrix[0])  # 总列数

        row = 0  # 边界行数
        col = n  # 边界列数
        while True:
            flag = False
            i = -1
            for i in range(col):
                if matrix[row][i] == target:
                    return True
                elif matrix[row][i] > target:
                    flag = True
                    break
            if i == -1:
                return False
            col = i - 1 if flag else i  # 通过遍历第一行确定右边界

            flag = False
            j = -1
            for j in range(row, m):
                if matrix[j][col] == target:
                    return True
                elif matrix[j][col] > target:
                    flag = True
                    break
            if j == -1 or flag is False:
                return False
            row = j  # 通过遍历最后一列确定上边界


if __name__ == '__main__':
    arra = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    target = 20
    print(Solution().findNumberIn2DArray(arra, target))
