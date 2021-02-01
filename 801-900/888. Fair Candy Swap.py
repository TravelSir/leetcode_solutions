"""
首先想到的解法时间复杂度可能较高
1. 先算出两个人分别拥有的糖果总量。 O(m+n)
2. 将两个人的糖果进行排序。 O(m*log(m)+n*log(n))
3. 从头开始比较两人糖果差值使之等于两人糖果总量差值的一半 O(m+n)

但是其实我们可以用数学的解法来解这道题:
设 A,B糖果总量为sumA, sumB。 解集为{x, y}, x和y分别为A, B集合中的一个元素, 那么:
sumA - x + y = sumB - y + x
x = (sumA - sumB) / 2 + y
这就表示对于B集合中的任意一个y`来说，只要A中有满足(sumA-sumB)/2+y`的x`数的存在，那就表明这是一组有效解
那检测一个数存不存在，最快速的方法就是用哈希表了
那时间复杂度就为O(m+n) , 但需要一个额外空间O(n)
"""


class Solution:
    # def fairCandySwap(self, A, B):
    #     poor = (sum(A) - sum(B)) / 2
    #     A = sorted(A)
    #     B = sorted(B)
    #     i = j = 0
    #     while i < len(A):
    #         if A[i] - B[j] == poor:
    #             return [A[i], B[j]]
    #         elif A[i] - B[j] < poor:
    #             i += 1
    #         else:
    #             j += 1

    def fairCandySwap(self, A, B):
        poor = (sum(A) - sum(B)) // 2
        hash_a = set(A)  # 只检测存不存在，可用set来代替dict
        for b in B:
            if (poor + b) in hash_a:
                return [poor + b, b]


if __name__ == '__main__':
    a = [2]
    b = [1, 3]
    print(Solution().fairCandySwap(a, b))
