"""
解题思路:
这题看上去很简单呀。就是不能出现连续的三个a或三个b
那首先判断a, b谁更多，多的如果是a 那就连续两个两个a出现，中间用一个b隔断，最大消耗a,最小消耗b
这里可以发现，b最少要有ceil(A/2) - 1个，最多有ceil(A/2)个，从最小到最多每多一个，那么相当于两个a两个a之间要多有一个是两个b隔开的。

这样我们就能得出, 两个a的次数为 A // 2， 一个a的次数为A % 2, 两个b出现的次数为 less_two = B - math.ceil(A/2) 如果less_two小于0就是没有应该为0,一个b出现的次数为B - less_two * 2 个
其实ceil(A/2) = A // 2 + A % 2, 因为A // 2 和 A % 2都要用，所以这里不用计算ceil(A/2), 直接把more_one和more_two加起来就可以了
最后循环组合一下就行了

"""


class Solution:

    def strWithout3a3b(self, A, B):
        if A < 3 and B < 3:
            return 'a' * A + 'b' * B
        if A >= B:
            less = 'b'
            more = 'a'
            more_two = A // 2
            more_one = A % 2
            less_two = B - (more_one + more_two)
            less_two = less_two if less_two > 0 else 0
            less_one = B - less_two * 2
        else:
            less = 'a'
            more = 'b'
            more_two = B // 2
            more_one = B % 2
            less_two = A - (more_one + more_two)
            less_two = less_two if less_two > 0 else 0
            less_one = A - less_two * 2

        res = []
        flag = 'more'
        while more_one + more_two + less_one + less_two:
            if flag == 'more':
                if more_two > 0:
                    res.append(more * 2)
                    more_two -= 1
                elif more_one > 0:
                    res.append(more)
                    more_one -= 1
                flag = 'less'
            else:
                if less_two > 0:
                    res.append(less * 2)
                    less_two -= 1
                elif less_one > 0:
                    res.append(less)
                    less_one -= 1
                flag = 'more'
        return ''.join(res)


if __name__ == '__main__':
    sl = Solution()
    while True:
        a = input('Input a...')
        if a == '-1':
            break
        b = input('Input b...')
        print(sl.strWithout3a3b(int(a), int(b)))
