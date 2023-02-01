"""
解题思路:
很简单的一题，遍历一次key，建立字母映射哈希表。再根据哈希表替换message解密。
注意一下空格过滤，和判断一下映射关系是否已建立完善
"""


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_dict = dict()
        begin = _index = ord('a')
        for s in key:
            if s != ' ' and s not in key_dict:
                key_dict[s] = chr(_index)
                _index += 1
            if _index - begin == 32:
                break
        return ''.join([key_dict[s] if key_dict.get(s) else s for s in message])
