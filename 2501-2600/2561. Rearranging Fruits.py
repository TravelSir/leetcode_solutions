"""
解题思路:
这里我们可以先将两个数组快速排序，然后使用双指针的方法来遍历两个数组。
当两个头指针指向的元素相等时，我们可以直接跳过这两个元素。
如果不相等，我们则需将小的那个元素交换给另外一个数组，然后判断小树的那个指针下一个数是否等于该数。
若不等于则说明无法使两个数组相等，返回-1。
如果等于，则将该数的值加到总成本数组中，并将指针向后移动。
最后计算总成本时，其实只需要取数组前面一半的值计算即可，且这里需要判断若单个值大于数组中最小值的两倍，其实可以通过最小值交换的方式两次交换减少成本
"""
from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        basket1.sort()
        basket2.sort()

        i, j = 0, 0
        cost_list = []
        min_cost = min(basket1[0], basket2[0]) if basket1 and basket2 else 0
        total_cost = 0

        while i < len(basket1) or j < len(basket2):
            if j < len(basket2) and i < len(basket1) and basket1[i] == basket2[j]:
                i += 1
                j += 1
            elif j >= len(basket2) or (i < len(basket1) and basket1[i] < basket2[j]):
                if (i + 1 >= len(basket1)) or (basket1[i + 1] != basket1[i]):
                    return -1
                cost_list.append(basket1[i])
                i += 2
            elif i >= len(basket1) or (j < len(basket2) and basket1[i] > basket2[j]):
                if (j + 1 >= len(basket2)) or (basket2[j + 1] != basket2[j]):
                    return -1
                cost_list.append(basket2[j])
                j += 2
            else:
                return -1

        for cost in range(len(cost_list) // 2):
            if cost_list[cost] > 2 * min_cost:
                total_cost += min_cost * 2
            else:
                total_cost += cost_list[cost]

        return total_cost



if __name__ == '__main__':
    print(Solution().minCost([4,2,2,2], [1, 4, 1, 2]))  # Example usage
    print(Solution().minCost([2, 3, 4, 1, 3, 3], [3, 2, 1, 2, 2, 5]))  # Example usage
    print(Solution().minCost([4,4,4,4,3], [5,5,5,5,3]))  # Example usage
    print(Solution().minCost([84,80,43,8,80,88,43,14,100,88], [32,32,42,68,68,100,42,84,14,8]))  # Example usage