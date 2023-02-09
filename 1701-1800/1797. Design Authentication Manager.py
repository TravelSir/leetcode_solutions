"""
解题思路:
这题其实挺简单的，实例化对象的时候设置过期时间值，并初始化记录tokenId与过期时间的dict。
在每一次generate的时候，都设置tokenId的过期时间未当前时间+过期时间
在renew的时候，如果tokenId不存在或者已过期不处理，否则设置tokenId的过期时间未当前时间+过期时间

"""


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.token_dict = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token_dict[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token_dict and self.token_dict[tokenId] > currentTime:
            self.token_dict[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for t in self.token_dict:
            if self.token_dict[t] > currentTime:
                cnt += 1
        return cnt


if __name__ == '__main__':
    # Your AuthenticationManager object will be instantiated and called as such:
    obj = AuthenticationManager(5)
    obj.renew("aaa", 1)
    obj.generate("aaa", 2)
    print(obj.countUnexpiredTokens(6))
    obj.generate("bbb",7)
    obj.renew("aaa",8)
    obj.renew("bbb", 10)
    print(obj.countUnexpiredTokens(15))

