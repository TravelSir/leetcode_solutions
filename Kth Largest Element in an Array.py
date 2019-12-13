"""
解题思路:
最简单的方法是排序,
    nums.sort(reverse=True)
    return nums[k-1]
但时间复杂度是O(n*log(n))

其实我们要确定第k个最大数，其实只需要每次判断与最大k个数的比较，每次只记录下最大的k个数
如果当前数小于k个数中的最小数，就继续循环
若果当前数大于k个数中的最小数，则相当于把这个数插入进这k个数中，再把最小数丢出k个数
我们这里的实现思路是用小顶堆，
这样的时间复杂度是O(n*log(k))
"""


class Solution:
    def findKthLargest(self, nums, k):
        heap = nums[:1]
        for i in nums[1:]:
            if len(heap) == k:
                if i < heap[0]:
                    continue
                heap[0] = heap[-1]
                heap = heap[:-1]
                if k > 1:
                    self.down(heap)
            heap.append(i)
            self.up(heap)
        return heap[0]

    def up(self, heap):
        child = len(heap) - 1
        parent = (child - 1) // 2
        tem = heap[child]
        while child > 0 and tem < heap[parent]:
            heap[child] = heap[parent]
            child = parent
            parent = (child - 1) // 2
        heap[child] = tem

    def down(self, heap):
        parent = 0
        child = parent * 2 + 1
        lens = len(heap)
        tem = heap[parent]
        while child < lens:
            if child + 1 < lens and heap[child] > heap[child + 1]:
                child += 1
            if heap[child] < tem:
                heap[parent] = heap[child]
                parent = child
                child = parent * 2 + 1
            else:
                break
        heap[parent] = tem


if __name__ == '__main__':
    nums = [3,2,3,1,2,4,5,5,6]
    k = 1
    print(Solution().findKthLargest(nums, k))
