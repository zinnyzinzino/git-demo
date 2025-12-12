class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    @staticmethod
    def printlist(head):
     current = head
     while current:
        print(current.data, end = "->")
        current = current.next



    @staticmethod
    def findlowest(head):
        minvalue = head.data
        currentnode = head.next
        while currentnode:
            if currentnode.data < minvalue:
                minvalue = currentnode.data
            currentnode = currentnode.next
        return minvalue
    
node1 = Node(7)
node2 = Node(9)
node3 = Node(15)
node4 = Node(6)
node5 = Node(0)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print (f"lowest value: {Node.findlowest(node1)}")
print(Node.printlist(head=node1))