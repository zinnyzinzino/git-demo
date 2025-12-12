# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next= None
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_tail(self, data):
#         new = node(data)
#         if self.head is None:
#             self.head = new
#             return

#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = new

#     def reverse(self):
#         prev = None
#         curr = self.head

#         while curr:
#             nxt = curr.next      # store next node
#             curr.next = prev     # reverse pointer
#             prev = curr          # move prev
#             curr = nxt           # move curr

#         self.head = prev

#     def display(self):
#         curr = self.head
#         while curr:
#             print(curr.data, end=" -> ")
#             curr = curr.next
#         print("None")



# # Create list
# sll = SinglyLinkedList()

# sll.insert_tail(10)
# sll.insert_tail(20)
# sll.insert_tail(30)
# sll.insert_tail(40)

# print("Original list:")
# sll.display()
# # Output: 10 -> 20 -> 30 -> 40 -> None

# # Reverse it
# sll.reverse()

# print("Reversed list:")
# sll.display()
# # Output: 40 -> 30 -> 20 -> 10 -> None




# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
# def detect_cycle(head):
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         if slow ==fast:
#             return True
#     return False




# def merge_lists(l1, l2):
#     dummy = node(0)
#     tail = dummy
#     while l1 and l2:
#         if l1.data <= l2.data:
#             tail.next = l1
#             l1 = l1.next
#         else:
#             tail.next = l2
#             l2 = l2.next
#         tail= tail.next
#     tail.next = l1 or l2
#     return dummy.next

# def sort_list(head):
#     if not head or head.next:
#         return head
#     slow, fast = head.next, head.next.next
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     mid = slow.next
#     slow.next = None
#     l1 = sort_list(head)
#     l2 = sort_list(mid)
#     return merge_lists(l1, l2)

# def remove_duplicate(head):
#     current = head
#     while current:
#         if current.next == current.next.next:
#             current.next = current.next.next
#         else:
#             current = current.next
#     return head

# def find_middle(head):
#     slow = fast= head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     return slow.data

# def nth_from_node(head,n):
#     first = second = head
#     for _ in range(n):
#         first = first.next
#     while first:
#         first = first.next
#         second = second.next
#     return second.data

# def is_palindrome(head):
#     vals = []
#     current = head
#     while current:
#         vals.append(current.data)
#         current = current.next
#     return vals == vals[::-1]



# class Node:
#     def __init__(self,data=None):
#         self.data = data
#         self.next = None
    
# class Linkedlist:
#     def __init__(self, head=None):
#         self.head = head
#     def beginning(self,data):
#         newnode = Node(data)
#         newnode.next = self.head
#         self.head = newnode

#     def insert_in_pos(self, data, index):
#         if index == 0 or self.head is None:
#             self.beginning(data)
#             return
#         newernode = Node(data)
#         current = self.head
#         current_index = 0
#         while current.next and current_index < index - 1:
#             current = current.next
#             current_index +=1
#         newernode.next = current.next
#         current.next = newernode
#         if current_index != index - 1:
#          print("Index out of range")
#          return


#     def delete_by_value(self,value):
#         if self.head == None:
#          return
#         if self.head.data == value:
#             self.head = self.head.next
#             return
#         curr = self.head
#         while curr.next and curr.next.data !=value:
#             curr = curr.next
#         if curr.next is None:
#             print("not ofund")
#             return
#         curr.next = curr.next.next        
#     def reverse(self):
#         prev = None
#         current = self.head
#         while current:
#             nxt = current.next
#             current.next = prev
#             prev = current
#             current = nxt
#         self.head = prev
#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end = "->")
#             temp = temp.next
#         print ("none")


# train = Linkedlist()
# train.insert_in_pos('Engine', 0)
# train.insert_in_pos('Carriage1', 1)
# train.insert_in_pos('Carriage2', 2)
# train.display()
# train.reverse()
# train.display()


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class CustomerQueue:
#     def __init__(self):
#         self.head = None

#     def enqueue_vip(self, customer):
#         new_node = Node(customer)
#         new_node.next = self.head
#         self.head = new_node

#     def enqueue_regular(self, customer):
#         new_node = Node(customer)
#         if not self.head:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=' -> ')
#             temp = temp.next
#         print('None')


# # Example usage
# queue = CustomerQueue()
# queue.enqueue_regular('Alice')
# queue.enqueue_vip('VIP Bob')
# queue.enqueue_regular('Charlie')
# queue.display()



# class Node:
#     def __init__(self, data= None):
#         self.data = data
#         self.next = None
#         self.prev = None
# class DoublyLinkedList:
#     def __init__(self, head):
#         self.head = head
#     def insert_end(self, data):
#         newnode = Node(data)
#         if not self.head:
#             self.head = newnode
#             return
#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = newnode
#         newnode.prev = curr
#     def delete(self,val):
#         curr = self.head
#         while curr:
#             if curr.data == val:
#                 if curr.prev:
#                     curr.prev.next = curr.next
#                 if curr.next:
#                     curr.next.prev = curr.prev
#                 if curr == self.head:
#                     self.head = curr.next
#                 return
#             curr = curr.next
#     def traverse_forward(self):
#         curr = self.head
#         while curr:
#             print(curr.data, end = "<->")
#             curr = curr.next
#         print('none')
#     def traverse_Backward(self):
#         curr = self.head
#         while curr and curr.next:
#             curr = curr.next
#         while curr:
#             print(curr.data, end = "<->")
#             curr = curr.prev
#         print ('none')

# class node:
#     def __init__(self, data = None):
#         self.data = data
#         self.next = None
# class browserhistory:
#     def __init__(self,head,current):
#         self.head = head
#         self.current = current
#     def visit(self, url):
#         newnode = node(url)
#         if not self.head:
#             self.head = newnode
#         else:
#             self.current.next = newnode
#         self.current = newnode
#     def back(self):
#         if self.head == self.current:
#             return "can't goback"
#         temp = self.head
#         while temp.next != self.current:
#             temp = temp.next
#         self.current = temp
#         return self.current.data
#     def forward(self):
#         if self.current and self.current.next:
#             self.current = self.current.next
#             return self.current.data
#         return None
#     def show_history(self):
#         temp = self.head
#         history = []
#         while temp:
#             history.append(temp.data)
#             temp = temp.next
#         return history

# class Node:
#     def __init__(self, data = None):
#         self.data = data
#         self.next = None
# class taskscheduler:
#     def __init__(self, head):
#         self.head = head
#     def add_task(self,data):
#         newnode = Node(data)
#         if not self.head:
#             self.head = newnode
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = newnode
#     def rotate(self):
#         if not self.head or not self.head.next:
#             return
#         first = self.head
#         self.head = self.head.next
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = first
#         first.next = None
#     def remove_task(self,task):
#         temp = self.head
#         prev = None
#         while temp:
#             if temp.data == task:
#                 if prev:
#                     prev.next = temp.next
#                 else:
#                     self.head = temp.next
#                 return
#             prev = temp
#             temp = temp.next
#     def showtasks(self):
#         tasks = []
#         temp = self.head
#         while temp:
#             tasks.append(temp.data)
#             temp = temp.next
#         return tasks



# class Customer:
#     def __init__(self, ID, name, email):
#         self.id = ID
#         self.name=name
#         self.email=email
#     def __str__(self):
#         return f"employee {self.id}, {self.name}, {self.email}"

# class Node:
#     def __init__(self, data=None):
#         self.data=data
#         self.next=None

# class Slinkedlist:
#     def __init__(self):
#         self.head=None
#     def insertbeginning(self,ID):
#         newnode = Node(ID)
#         newnode.next = self.head
#         self.head = newnode 
#     def insertatend(self, ID):
#         newnoder = Node(ID)
#         if self.head is None:
#             self.head = newnoder
#         curr = self.head
#         while curr.next:
#             curr = curr.next
#         curr.next = newnoder
    
#     def deletebyid(self, id):
#         curr = self.head
#         prev = None
#         while curr:
#             if curr.data ==id:
#                 if prev:
#                     prev.next = curr.next
#                 else:
#                     self.head = curr.next
#                 return
#             prev = curr
#             curr = curr.next
     
#     def searchbyid(self,id):
#         curr = self.head
#         while curr:
#             if curr.data == id:
#                 return curr.data
#             curr = curr.next
#         return None
#     def display(self):
#         curr = self.head
#         if curr is None:
#             print("no customers")
#             return
#         while curr:
#             print(curr.data, end = "->")
#             curr = curr.next

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("nono")
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             return None
#     def is_empty(self):
#         return len(self.items) == 0
#     def display(self):
#         print(self.items)

# def evaluate_postfix(expr):
#     stack = Stack()
#     tokens = expr.split()
#     for token in tokens:
#         if token.isdigit():
#             stack.push(int(token))
#         else:
#             right = stack.pop()
#             left = stack.pop()
#             if token == "+":
#               stack.push(left + right)
#             elif token == "-":
#               stack.push(left - right)
#             elif token == "*":
#                 stack.push(left * right)
#             elif token == "/":
#                 stack.push(left/right)
#             else:
#                 raise ValueError("unknown oprator")
#     return stack.pop()

# class Customer:
#     def __init__(self, id, name, service_type):
#         self.id = id
#         self.name = name
#         self.service_type = service_type
#     def __str__(self):
#         return f"customer: {self.id}, {self.name}, {self.service_type}"
    
# class Queue:
#     def __init__(self):
#         self.items = []
#     def enqueue(self,item):
#         self.items.append(item)
#     def dequeue(self):
#         if self.isempty():
#             return "not found"
#         else:
#             return self.items.pop(0)
#     def peek(self):
#         return self.items[0] if not self.isempty() else "queue is empty"
#     def isempty(self):
#         return len(self.items) == 0
#     def size(self):
#         return len(self.items)
#     def search(self, target_id):
#         for i,customer in enumerate(len(self.items)):
#             if customer.id == target_id:
#                 return i
#         return -1
#     def display(self):
#         if self.isempty():
#             print("queue is empty")
#         else:
#             for item in self.items:
#                 print(item)

# class Node:
#     def __init__(self,song_name):
#         self.song = song_name
#         self.prev = None
#         self.next = None
# class Doublylinkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def insert_at_end(self, song_name):
#         newnode = Node(song_name)
#         if self.head is None:
#             self.head = self.tail = newnode
#             return
#         self.tail.next = newnode
#         newnode.prev = self.tail
#         self.tail = newnode
#     def delete(self,song_name):
#         curr = self.head
#         while curr:
#             if curr.song == song_name:
#                 if curr == self.head:
#                     self.head = curr.next
#                     if self.head:
#                         self.head.prev = None
#                     else:
#                         self.tail = None
#                 elif curr == self.tail:
#                     self.tail = curr.prev
#                     self.tail.next = None
#                 else:
#                     curr.prev.next = curr.next
#                     curr.next.prev = curr.prev
#                 return
#             curr = curr.next
#     def traverse_forward(self):
#         curr = self.head
#         while curr:
#             print(curr.song, end = "->")
#             curr = curr.next
#         print ("none")
#     def traverse_backward(self):
#         curr = self.tail
#         while curr:
#             print(curr.song, end = "->")
#             curr = curr.prev
#         print('None')
#     def find(self,song_name):
#         curr = self.head
#         while curr:
#             if curr.song == song_name:
#                 return curr
#             curr = curr.next
#         return None
# playlist = Doublylinkedlist()

# playlist.insert_at_end(" A")
# playlist.insert_at_end(" B")
# playlist.insert_at_end(" C")
# playlist.insert_at_end(" D")
# playlist.insert_at_end(" E")

# print("Forward traversal:")
# playlist.traverse_forward()

# print("\nBackward traversal:")
# playlist.traverse_backward()

# print("\nSearching for  C:")
# found = playlist.find(" C")
# print(found.song if found else "Not found")

# print("\nDeleting  B...")
# playlist.delete(" B")

# print("Forward after delete:")
# playlist.traverse_forward()
    
 
class Book:
    def __init__(self, isbn, title, author, price):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.isbn} - {self.title} by {self.author} (${self.price})"


class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


class BookBST:
    def __init__(self):
        self.root = None

 
    def insert(self, book):
        self.root = self._insert(self.root, book)

    def _insert(self, root, book):
        if root is None:
            return Node(book)
        if book.isbn < root.book.isbn:
            root.left = self._insert(root.left, book)
        else:
            root.right = self._insert(root.right, book)
        return root

    
    def search(self, isbn):
        return self._search(self.root, isbn)

    def _search(self, root, isbn):
        if root is None:
            return None
        if isbn == root.book.isbn:
            return root.book
        elif isbn < root.book.isbn:
            return self._search(root.left, isbn)
        else:
            return self._search(root.right, isbn)

    
    def delete(self, isbn):
        self.root = self._delete(self.root, isbn)

    def _delete(self, root, isbn):
        if root is None:
            return None

        if isbn < root.book.isbn:
            root.left = self._delete(root.left, isbn)

        elif isbn > root.book.isbn:
            root.right = self._delete(root.right, isbn)

        else:
       
            if root.left is None and root.right is None:
                return None
         
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            successor = self._min_value_node(root.right)
            root.book = successor.book
            root.right = self._delete(root.right, successor.book.isbn)

        return root

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        self._inorder(self.root)
        print()

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(root.book)
            self._inorder(root.right)

    def count_nodes(self):
        return self._count(self.root)

    def _count(self, root):
        if root is None:
            return 0
        return 1 + self._count(root.left) + self._count(root.right)
