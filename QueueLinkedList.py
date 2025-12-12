class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.front:           
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        removed = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed

    def peek(self):
        return None if not self.front else self.front.data

    def is_empty(self):
        return self.front is None

    def show(self):
        temp = self.front
        out = []
        while temp:
            out.append(temp.data)
            temp = temp.next
        return out
   
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")

print(q.show())        
print(q.dequeue())     
print(q.show())        