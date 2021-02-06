"""
为了使拿到的牌总数最大，拿其实转换过来其实就是使剩下的牌最小，
拿其实就等于从头开始，让一个长度为n-k的窗口不断往后滑，求的最小和的窗口
"""


class Solution:
    def maxScore(self, cardPoints, k):
        length = len(cardPoints)
        _min = tem = sum(cardPoints[:length-k])
        for i in range(k):
            tem = tem - cardPoints[i] + cardPoints[length - k + i]
            _min = _min if _min < tem else tem
        return sum(cardPoints) - _min


if __name__ == '__main__':
    cardPoints = [1,79,80,1,1,1,200,1]
    k = 3
    print(Solution().maxScore(cardPoints, k))

