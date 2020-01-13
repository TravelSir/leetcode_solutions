"""
解题思路:
很久以前被这道题困扰住，用了三层循环，想尽办法优化每次循环，还是超时
最近又开始看这道题，突然就有了灵感。
两数相加，结果要为0，那么肯定是一正一负或两个0
那三数相加，排除0的情况，肯定有一个正数或一个负数，那我们只需要以所有正数或所有负数为基数，
假设我们设基数为负数，那么我们可以先对数组进行排序，设置正负指针，也就是左指针从基数右边第一个负数开始，右指针从右边正数开始，
计算三数之和
1. 如果大于0，说明正数过大，右指针左移
2. 如果小于0，说明负数过大，左指针右移
3. 等于0，则记录结果，左指针右移，右指针左移，寻找下一个解

优化步骤:
1. 长度小于3则不用判断，直接返回空数组
2. 在计算三数之和第3步时，左指针右移时判断移动后的数字是否和当前数字相等，相等则跳过相同数字到下一位置，右指针同理

"""


class Solution:

    def threeSum(self, nums):
        lens = len(nums)
        res = []
        if lens < 3:
            return res
        nums.sort()
        i = 0
        tem = None
        while i < lens:
            if nums[i] > 0:
                break
            if nums[i] == tem:
                tem = nums[i]
                i += 1
                continue
            left = i + 1
            right = lens - 1
            t_left = t_right = None
            flag = False
            while left < right:
                if nums[left] == t_left:
                    t_left = nums[left]
                    left += 1
                    flag = True
                if nums[right] == t_right:
                    t_right = nums[right]
                    right -= 1
                    flag = True
                if flag:
                    flag = False
                    continue
                _sum = nums[i] + nums[left] + nums[right]

                if _sum > 0:
                    t_right = nums[right]
                    right -= 1
                elif _sum < 0:
                    t_left = nums[left]
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    t_left = nums[left]
                    t_right = nums[right]
                    right -= 1
                    left += 1
            tem = nums[i]
            i += 1

        return res


if __name__ == '__main__':
    s = Solution()
    num_list = [[1,-1,-1,0],[-2,0,0,2,2], [-1,0,1,2,-1,-4]]
    for i in num_list:
        print(s.threeSum(i))
