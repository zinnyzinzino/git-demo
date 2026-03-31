# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class Slinkedlist:
#     def __init__(self):
#         self.head = None

#     def printlist(self):
#         printval = self.head
#         while printval:
#             print(printval.data)
#             printval = printval.next

#     def beginning(self, newdata):  # insert at the beginning
#         newnode = Node(newdata)
#         newnode.next = self.head
#         self.head = newnode 

#     def ending(self, moredata):  # insert at the end
#         endnode = Node(moredata)
#         if self.head is None:
#             self.head = endnode
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = endnode

#     def between(self, middle_node, plusdata):  # insert in the middle
#         if middle_node is None:
#             print("absent")
#             return
#         betweennode = Node(plusdata)
#         betweennode.next = middle_node.next
#         middle_node.next = betweennode

#     def insert(self, index, evenmoredata):
#         if index <= 0 or self.head is None:
#             self.beginning(evenmoredata)
#             return

#         new_node = Node(evenmoredata)
#         current = self.head
#         current_index = 0

#         while current.next is not None and current_index < index - 1:
#             current = current.next
#             current_index += 1

#         new_node.next = current.next
#         current.next = new_node

#     def find_min_max(self):
#         if self.head is None:
#             return None, None

#         cur = self.head
#         minv = cur.data
#         maxv = cur.data
#         cur = cur.next

#         while cur:
#             if cur.data < minv:
#                 minv = cur.data
#             if cur.data > maxv:
#                 maxv = cur.data
#             cur = cur.next

#         return minv, maxv

#     # remove in POSITIONS
#     def delete_beginning(self):
#         if self.head:
#             # remove first node by making head point to second
#             self.head = self.head.next

#     def delete_end(self):
#         if not self.head:
#             return
#         if not self.head.next:
#             # only one node
#             self.head = None
#             return
#         current = self.head
#         while current.next.next is not None:
#             current = current.next   
#         current.next = None

#     def delete_positon(self, index):
#         if index == 1:
#             self.delete_beginning()
#             return
#         current = self.head
#         count = 1
#         while current and count < index - 1:
#             current = current.next
#             count += 1
#         if current and current.next:
#             current.next = current.next.next
#     # remove a selected VALUE
#     def remove_node(self, removekey):
#         headvalue = self.head
#         if headvalue is not None:
#             if headvalue.data == removekey:
                
#                 self.head = headvalue.next
#                 headvalue = None
#                 return
#             prev = None
#             while headvalue is not None:
#                 if headvalue.data == removekey:
#                     break
#                 prev = headvalue
#                 headvalue = headvalue.next
#             if headvalue is None:
#                 return
#             prev.next = headvalue.next
#             headvalue = None


# list = Slinkedlist()
# list.head = Node("mon")
# e2 = Node("tue")
# e3 = Node("wed")

# list.head.next = e2
# e2.next = e3

# list.insert(4, "bigbong")
# list.remove_node("bigbong")
# list.between(list.head.next, "fri")
# list.beginning("sun")
# list.ending("thu")
# list.printlist()
# low, high = list.find_min_max()
# print("min:", low, "max:", high)




# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class Slinkedlist:
#     def __init__(self):
#         self.head = None
#     def addbeginning(self, data):
#        newnode = Node(data)
#        newnode.next = self.head
#        self.head = newnode
#     def addend(self,data):
#         newnode = Node(data)
#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = newnode
#     def addinpos(self,data,pos):
#         newnode = Node(data)
#         if self.head == None or pos == 0:
#             self.head = self.addbeginning(data)
#         curr = self.head
#         count = 0
#         while curr.next and count != pos-1:
#             curr = curr.next
#             count +=1
#         newnode.next = curr.next
#         curr.next = newnode
#     def deletebyvalue(self,data):
#         if self.head ==None:
#             return
#         if self.head.data == data:
#             self.head = self.head.next
#         curr = self.head
#         while curr.next and curr.next.data !=data:
#             curr = curr.next
#         if curr.next is None:
#             print('couldnt find')
#         curr.next = curr.next.next
#     def reverse(self):
#         curr = self.head
#         prev = None
#         while curr:
#             nxt = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nxt
#         self.head = prev
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end = "->")
#             temp = temp.next
#         print ("none")
#     def deletestart(self):
#         if self.head == None:
#             return
#         self.head = self.head.next
#     def deleteend(self):
#         if self.head is None:
#             return
#         if self.head.next is None:
#             self.head = None
#             return
        
#         curr = self.head
#         while curr.next.next:
#             curr = curr.next
#         curr.next = None
#     def deleteinpos(self,pos):
#         curr = self.head
#         count = 0 
#         while curr and pos !=count - 1:
#             curr = curr.next
#             count +=1
#         curr.next = curr.next.next
#     def detectcycle(self):
#         fast = self.head
#         slow = self.head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False
#     def findmid(self,head):
#         fast =head
#         slow = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow.data
#     def sortlist(self, head):
#         if head is None or head.next is None:
#             return head
#         slow = head
#         fast = head
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast=fast.next.next
#         mid=slow.next
#         slow.next = None
#         left = self.sortlist(head)
#         right = self.sortlist(mid)
#         return self.mergelist(left,right)
#     def mergelist(self,l1, l2):
#         dummy = Node(0)
#         tail = dummy
#         while l1 and l2:
#             if l1.data <=l2.data:
#                 tail.next = l1
#                 l1 = l1.next
#             else:
#                 tail.next = l2
#                 l2 = l2.next
#             tail = tail.next
#         tail.next = l1 if l1 else l2
#         return dummy.next
#     def findmindmax(self):
#         curr = self.head
#         minv = curr.data
#         maxv = curr.data
#         curr = curr.next
#         while curr:
#             if minv > curr.data:
#                 minv = curr.data
#             if maxv<curr.data:
#                 maxv=curr.data
#             curr = curr.next
#         return minv,maxv
            





class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            return

        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    def insert_at_end(self, data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = newnode
        newnode.prev = current

    def insert_at_pos(self, data, pos):
        newnode = node(data)
        if pos == 1:
            self.insert_at_beginning(data)
            return

        current = self.head
        cnt = 1
        while current and cnt != pos - 1:
            current = current.next
            cnt += 1

        newnode.next = current.next
        newnode.prev = current

        if current.next:
            current.next.prev = newnode
        current.next = newnode

    def delete_at_beginning(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if not self.head :
            return
        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next:
            current = current.next

        current.prev.next = None

    def delete_at_pos(self, pos):
        if not self.head:
            return
        if pos == 1:
            delete_at_beginning()
            return

        current = self.head
        cnt = 1
        while current and cnt != pos:
            current = current.next
            cnt += 1

        if current is None:
            print('position out of range')
            return

        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev


    def print_forward(self):
        current = self.head
        while current:
            print(current.data, end = '->')
            current = current.next
        print("None")