"""
解题思路:
因为复制只能复制全部，但每一次复制可以粘贴多次，所以结果应该是
1*(a+1)*(b+1)*(c+1) ... 这样的，a,b,c代表第一次,第二次，第三次粘贴的次数
所以当我们对总数做因数分解，比如总数为30
30 = 3 * 2 * 5
那么分解后对项数就是需要copy的次数3，每次需要paste的次数就是3-1,2-1,5-1
这里其实copy的次数跟paste需要减的次数相同,结果其实就是3+2+5=10，也由此可以得出完全分解才是使用次数最少的
操作的顺序可以随机,但结果一样
这个例子按3*2*5操作就是：
1. 复制   -- 1
2-3. 粘贴2次 -- 3
4. 复制   -- 3
5. 粘贴1次 -- 6
6. 复制   -- 6
7-10. 粘贴4次  -- 30

"""


class Solution:
    def minSteps(self, n: int) -> int:
        num_list = []
        if n < 2:
            return 0
        i = 2
        while i <= n:
            if n % i:
                i += 1
                continue
            n = n // i
            num_list.append(i)
        res = 0
        for n in num_list:
            res += n
        return res


if __name__ == '__main__':
    sl = Solution()
    print(sl.minSteps(6))
