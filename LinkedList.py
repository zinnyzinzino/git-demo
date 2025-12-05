class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Slinkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        printval = self.head
        while printval:
            print(printval.data)
            printval = printval.next

    def beginning(self, newdata):  # insert at the beginning
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

    def ending(self, moredata):  # insert at the end
        endnode = Node(moredata)
        if self.head is None:
            self.head = endnode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = endnode

    def between(self, middle_node, plusdata):  # insert in the middle
        if middle_node is None:
            print("absent")
            return
        betweennode = Node(plusdata)
        betweennode.next = middle_node.next
        middle_node.next = betweennode

    def insert(self, index, evenmoredata):
        if index <= 0 or self.head is None:
            self.beginning(evenmoredata)
            return

        new_node = Node(evenmoredata)
        current = self.head
        current_index = 0

        while current.next is not None and current_index < index - 1:
            current = current.next
            current_index += 1

        new_node.next = current.next
        current.next = new_node

    def find_min_max(self):
        if self.head is None:
            return None, None

        cur = self.head
        minv = cur.data
        maxv = cur.data
        cur = cur.next

        while cur:
            if cur.data < minv:
                minv = cur.data
            if cur.data > maxv:
                maxv = cur.data
            cur = cur.next

        return minv, maxv

    # remove in POSITIONS
    def delete_beginning(self):
        if self.head:
            # remove first node by making head point to second
            self.head = self.head.next

    def delete_end(self):
        if not self.head:
            return
        if not self.head.next:
            # only one node
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_positon(self, index):
        if index == 1:
            self.delete_beginning()
            return
        current = self.head
        count = 1
        while current and count < index - 1:
            current = current.next
            count += 1
        if current and current.next:
            current.next = current.next.next

    # remove a selected VALUE
    def remove_node(self, removekey):
        headvalue = self.head
        if headvalue is not None:
            if headvalue.data == removekey:
                
                self.head = headvalue.next
                headvalue = None
                return
            prev = None
            while headvalue is not None:
                if headvalue.data == removekey:
                    break
                prev = headvalue
                headvalue = headvalue.next
            if headvalue is None:
                return
            prev.next = headvalue.next
            headvalue = None


list = Slinkedlist()
list.head = Node("mon")
e2 = Node("tue")
e3 = Node("wed")

list.head.next = e2
e2.next = e3

list.insert(4, "bigbong")
list.remove_node("bigbong")
list.between(list.head.next, "fri")
list.beginning("sun")
list.ending("thu")
list.printlist()
low, high = list.find_min_max()
print("min:", low, "max:", high)