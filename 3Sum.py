


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lens = len(nums)
        if lens < 3:
            return []
        res = []
        filter = []
        for i in range(lens-2):
            a = nums[i]
            for j in range(i+1, lens-1):
                b = nums[j]
                for k in range(j+1, lens):
                    c = nums[k]
                    if (a, b) in filter or (a, c) in filter or (b, c) in filter:
                        break
                    if a + b + c == 0:
                        filter.append((a, c))
                        filter.append((c, a))
                        filter.append((a, b))
                        filter.append((b, a))
                        filter.append((b, c))
                        filter.append((c, b))
                        res.append([a, b, c])
                        break

        return res


if __name__ == '__main__':
    s = Solution()
    num_list = [3,0,-2,-1,1,2]
    print(s.threeSum(num_list))
