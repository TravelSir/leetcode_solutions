"""
解题思路: 用两个栈实现一个队列
首先清楚栈和队列的定义:
栈: 先进后出，从尾部出
队列: 先进先出，从头部出

那栈和队列写入是一样的顺序，但读取是相反的顺序。
假设 stackA = [1,2,3], 出的顺序只能是3 2 1, 我们可以用stackB来依次接受stackA的数据，那stackB=[3,2,1]，出的顺序就变成了123
那么 stackA就是一个写入数据的栈，stackB就是一个读取数据的栈，当读取stackB为空时，需要一次性将stackA的数据导过来
"""


class CQueue:

    def __init__(self):
        self.read_stack = list()
        self.write_stack = list()

    def appendTail(self, value: int) -> None:
        self.write_stack.append(value)

    def deleteHead(self) -> int:
        if not self.read_stack:
            while self.write_stack:
                self.read_stack.append(self.write_stack.pop())
        if self.read_stack:
            return self.read_stack.pop()
        return -1


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()

