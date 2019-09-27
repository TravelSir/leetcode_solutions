"""
解题思路:
要求解最小船数，就得使每艘船尽量满载
由于一艘船可坐两人，在不超重的情况下那最重的人和最轻的人在一起是最好的
如果超重，则最重的人单独坐一艘，然后再让剩下最重的和最轻的，依次类推。

所以首先应该对people列表倒序排序,然后一个left指针指向最重和一个right指针指向最轻
当left=right时，这个人单独坐一艘，当left>right时，代表所有人已经被分配，结束循环
"""


class Solution:
    def numRescueBoats(self, people, limit):
        lens = len(people)
        if lens < 2:
            return lens
        people = sorted(people, reverse=True)
        left = 0
        right = lens - 1
        sum = 0
        while left <= right:
            if left == right:
                sum += 1
                break
            if people[left] + people[right] <= limit:
               left += 1
               right -= 1
            else:
                left += 1
            sum += 1
        return sum


if __name__ == '__main__':
    sl = Solution()
    print(sl.numRescueBoats([3, 1, 7], 7))
