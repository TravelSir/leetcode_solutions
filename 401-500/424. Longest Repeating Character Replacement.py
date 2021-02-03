"""
寻找最长重复子串，其实就是从头开始遍历，以第一个元素为标准，遇到相同的继续，遇到不同的，根据k值，k>0则说明能变，则k-1,继续遍历下一个元素，
直到k=0且元素不等于头元素，这样就能找到从第一个元素开始的替换后的最长重复元素。以此类推，得出每个元素的最长，比较得出最长的，
那时间复杂度就在O(n*n)，这种暴力解法时间太长

然后思考优化的空间，当第一个元素和第二个元素相同时，那么其实第二个元素替换后的最长长度肯定是第一个元素替换后的最长元素-1，
因为他们可替换的k是一样的，那么我们每次计算的遍历就不用从头到尾遍历完，第二次遍历可以从上次遍历遇到的第一个不同元素开始算，这样能节约很多时间。
但即使这样，当连续当元素很少时一样很耗时。

我们重点审题，这里是寻找最长的重复子串，那么我们找到第一个长串后，之后找的串必须要大于第一个串才行，那么其实我们可以转化思想，不去计算每一次的子串大小，
而是用一个区间，也就是用一个滑动的窗口去向后不断包含更多的元素。因为我们要替换元素使子串为同样的元素，那么我们这个区间包含了多种元素，
那肯定其实某种数量最多的元素是主元素，其他元素作为替换元素。因为元素全为大写英文，那么就只有26种不同元素，
我们可以用一个哈希表来记录当前窗口的元素种类和个数, 当主元素外的其他元素总数=k时并且下一个元素不为主元素，那当前窗口就扩展到头了，记录当前区间长度
然后头元素和尾元素都向后移动一位，因为要找的子串必须要大于当前子串才有意义
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        cha_dict = {s[0]: 1}
        left = right = 0
        length = len(s)
        _max = 1
        while right < length - 1:
            if s[right + 1] in cha_dict:
                cha_dict[s[right + 1]] += 1
            else:
                cha_dict[s[right + 1]] = 1
            max_cha = self.get_max_char(cha_dict)
            _length = sum(cha_dict.values())
            if _length - cha_dict[max_cha] > k:
                _max = _length - 1
                cha_dict[s[left]] -= 1
                left += 1
                right += 1
            else:
                right += 1
        if _max == 1:
            _max = right - left + 1
        return _max

    @staticmethod
    def get_max_char(cha_dict):
        max_cha = ''
        max_num = 0
        for k, v in cha_dict.items():
            if v > max_num:
                max_cha = k
                max_num = v
        return max_cha


if __name__ == '__main__':
    s = 'ABAA'
    k = 0
    print(Solution().characterReplacement(s, k))
