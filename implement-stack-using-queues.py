from queue import Queue
class MyStack(object):

    def __init__(self):
        self.queue = Queue()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.put(x)
        for i in range(self.queue.qsize()-1):
            self.queue.put(self.queue.get())
        

    def pop(self):
        """
        :rtype: int
        """
        if(self.queue.empty()):
            return None
        return self.queue.get()

    def top(self):
        """
        :rtype: int
        """
        if(self.queue.empty()):
            return None
        topEle = self.queue.get()
        self.queue.put(topEle)
        for i in range(self.queue.qsize()-1):
            self.queue.put(self.queue.get())
        return topEle
    def empty(self):
        """
        :rtype: bool
        """
        return self.queue.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
