"""
解题思路:
这题考察的是大数的计算，由于Python的int类型范围很大，自带大数计算，所以可以直接用。
但是我们还是要理解其实现原理。大数的计算我们使用字符串或者数组来存储计算。
打印到n位数那么我们只需要申请一个长度为n的数组，初始化全为0，然后从数组末尾开始做+1计算，满10进1
那如何判断到最大位，我们这里就用一个数来记录标识满10进1的位数最大数x，当x>n即代表结束,但由于进位操作，例如9999到10000会有四次进位循环多出

所以我们可以用另一种思路: 生存的列表其实就是n位的0-9的全排列。全排列用递归实现，依次增加每一位，直到总长度=n返回，这里需要把结果为0的排列剔除
"""
from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        # return self.big_add(n)
        # result = []
        # num_list = []
        # _, result = self.permutation(num_list, result, n)
        # return result[1:]
        return self.python(n)

    @staticmethod
    def big_add(n: int) -> List[int]:
        result = []

        num_list = ['0'] * n
        x = 1
        while x <= n:
            inc = 1
            for i in range(1, x+1):
                if int(num_list[-i]) + inc >= 10:
                    num_list[-i] = '0'
                else:
                    num_list[-i] = str(int(num_list[-i]) + inc)
                    inc = 0
            if inc == 1:
                x += 1
                if x <= n:
                    num_list[-x] = '1'
                    result.append(int(''.join(num_list)))
            else:
                result.append(int(''.join(num_list)))
        return result

    def permutation(self, num_list: List[str], result: List[int], n: int) -> (List[str], List[int]):
        for i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            num_list.append(i)
            if len(num_list) == n:
                _num = int(''.join(num_list))
                result.append(_num)
                num_list.pop()
            else:
                num_list, result = self.permutation(num_list, result, n)
                num_list.pop()
        return num_list, result

    @staticmethod
    def python(n: int) -> List[int]:
        return [i for i in range(1, pow(10, n))]


if __name__ == '__main__':
    print(Solution().printNumbers(0))
