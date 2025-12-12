class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
class Slinkedlist:
    def __init__(self):
        self.head = None
    def beginning(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode
    def insert_at_position(self, index, moredata):
        if index <=0 or self.head is None:
            self.beginning(moredata)
            return
        newnewnode = Node(moredata)
        current = self.head
        current_index = 0
        while current.next and current_index < index - 1:
            current = current.next
            current_index +=1
        newnewnode.next = current.next
        current.next = newnewnode