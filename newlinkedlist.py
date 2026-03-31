class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    def _insert_at_beginning_(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
    def printlist(self):
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.next
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev



