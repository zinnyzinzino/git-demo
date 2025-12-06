class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.size = 0
    def isEmpty(self):
        return self.size == 0
    def isFull(self):
        return self.size == self.capacity
    def enqueue(self, item):
        if self.isFull():
            print('full')
            return
        self.arr[self.size] = item
        self.size +=1
    def dequeue (self):
        if self.isEmpty():
            print('empty')
            return
        for i in range(1,self.size):
            self.arr[i-1] = self.arr[i]
            self.size -=1
    def getFront(self):
        if self.isEmpty():
            print("empty")
            return -1
        return self.arr[0]
    def getRear(self):
        if self.isEmpty():
            print('fuck you')
            return -1
        return self.arr[self.size - 1]
if __name__=="__main__":
 q = MyQueue(3)
 q.enqueue(3)
 q.enqueue(20)
 q.enqueue(30)
 print("front:", q.getFront())
 q.dequeue()
 print("front", q.getFront())
 print("rear", q.getRear())
 q.enqueue(40)
