"""
这道题考查的是二进制数的位运算: 与(&),或(|),异或(^),右移(>>),左移(<<)
计算一个二进制中1的个数，我们可以通过将这个数与1进行与操作，判断这个数的最后一位是否为1，
如果是正数，我们再将这个数右移，继续计算，直到这个数变为0
但是如果是负数，-1右移后还是-1，就会导致最后一位一直是1。
所以为了避免死循环，我们才用左移的方式。先判断n与1，然后将1左移一位，再判断n与1。这样需要循环32次判断完

还有一种更巧妙的方法:
假设数字最后一位为1 0000 1111 当我们把数字-1: 0000 1110
假设数字最后一位为0 0000 1110 当我们把数字-1: 0000 1101
我们会发现最右边的1左边的数没有变，而右边包括自身的数都与原来相反。那我们把减1前后的数进行与操作。就会发现左边的数不变，右边全为0了
那一个数字中有多少个1，那我们就可以进行n&(n-1)操作n次，不用循环32次判断
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return self.amazing(n)

    @staticmethod
    def normal(n: int) -> int:
        flag = 1
        total = 0
        for i in range(32):
            if n & flag:
                total += 1
            flag <<= 1
        return total

    @staticmethod
    def amazing(n: int) -> int:
        total = 0
        while n:
            n = n & (n-1)
            total += 1
        return total




