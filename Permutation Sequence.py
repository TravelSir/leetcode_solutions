"""
解题思路:
可以看出排列组合的规律是从小到大，
当n=1时，有1种排列，
当n=2时，有2种排列，
当n=3时，有6种排列，
其实n=3时，可以拆分成第一位数和 后两位数，后两位数的排列组合为n=2时的两种，那第一位数可以是三个数种的任意一个，所以总的排列数就是2*3=6
所以我们可以知道，当k<=2时，第一位数没有变，那我们就可以确定第一个数是最小数，那就对剩下的后两位数分析，如果k=1那就确定第二位数是最小数，否则则是第二小数
当2<k<=4时，可以确定第一位数是第二小数，再对后两数分析，如果k=3那第位数就是剩下数里的最小数
所以以此举例n=4,k=9时，我们对k进行判断k如果是在1*2*3到1*2*3*4之间的话，那说明k至少改变了4位，如果k在1*2*3到1*2*3*2之间，说明第一位肯定是2，未确定是数位[1,3,4]
那k=k-6=3，那么k是在1*2 到1*2*3之间，说明k改变了3位，且k在1*2到1*2*2之间，那第二位就是3, 剩余未排列[1,4]
k = k-3 = 1，那么说明最后两位k未改变, 那么第三第四位就是1 4


"""
import math


class Solution:
    def getPermutation(self, n, k):
        l = [str(i) for i in range(1, n+1)]
        res = []
        # 找到k的临界值
        tem = 1
        i = 1
        while i < 10:
            tem *= i
            if k <= tem:
                break
            i += 1
        # 未改变位数直接先存入
        if n > i:
            res.extend(l[: n - i])
            l = l[n - i:]

        while k > 0:
            if tem == k:
                res.extend(l[::-1])
                return ''.join(res)
            tem //= i
            i -= 1
            j = k // tem
            first = math.ceil(k / tem) - 1
            res.append(l[first])
            l.pop(first)
            k -= tem*j
        if l:
            res.extend(l[::-1])

        return ''.join(res)


if __name__ == '__main__':
    print(Solution().getPermutation(4, 9))
