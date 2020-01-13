"""
解题思路:
这题要求我们不能使用其他库，就是要我们手动实现大数据的计算
而大数据计算的意义在于，当一个整型变量的值超过了2的32次方，这时候我们就没法声明一个超大数，所以我们可以用字符串来表示一个超大数，然后进行计算
从我们从小到大的手写算乘法的经验来：
首先我们以第一个数为基准，那么将第二个数拆成个，十，百，千，万形式的乘数，与第一个数每一位相乘，十位补一个0，百位补两个0。
其实这是根据乘法 a*(b+c) = a*b + a*c，比如计算 3 * 33 = 3 * 30 + 3 * 3 = 3*3*10 + 3*3
我们就只需要计算出3*3，然后根据位数补0就行，然后把所有得出的结果每位相加，有上一位的进1则加1，结果有1进1。
这样把问题拆成子问题最后结果相加的模式像极了动态规划, 而这样我们只需要计算9种组合,只是每种结果后面需要补0,
将计算结果备忘录起来，这样能减少很多次的计算
"""


class Solution:

    def add(self, num1, num2, zero):
        num2 = ['0']*zero + num2
        len1 = len(num1)
        len2 = len(num2)
        _max = max(len1, len2)

        i = 0
        _sum = []
        # 是否需要进位
        up = False
        while i < _max:
            tem = 0
            if i < len1:
                tem += int(num1[i])
            if i < len2:
                tem += int(num2[i])
            if up:
                tem += 1
            _tem = tem - 10
            if _tem >= 0:
                up = 1
                _sum.append(str(_tem))
            else:
                up = 0
                _sum.append(str(tem))
            i += 1
        if up:
            _sum.append('1')
        return _sum

    def multiply(self, num1: str, num2: str) -> str:
        # 基于第一个数的本次计算结果的备忘录
        note = {'0': '0'}
        zero = 0
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        if num1 == '0':
            return '0'
        num2 = num2[::-1]
        num1 = num1[::-1]
        _sum = []
        for i in range(len(num1)):
            tem = []
            up = 0
            if num1[i] not in note:
                for j in range(len(num2)):
                    res = int(num1[i]) * int(num2[j]) + up
                    tem.append(res % 10)
                    up = res // 10
                if up:
                    tem.append(str(up))
                note[num1[i]] = tem
            if note[num1[i]] != '0':
                _sum = self.add(_sum, note[num1[i]], zero)
            zero += 1
        return ''.join(_sum[::-1])


if __name__ == '__main__':
    sl = Solution()
    print(sl.multiply('2', '6'))

