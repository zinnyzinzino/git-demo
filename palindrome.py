class node:
 def __init__(self, data = None):
  self.data = data
  self.next = None


def is_palindrome(head):
 vals = []
 current = head
 while current:
  vals.append(current.data)
  current = current.next
 return vals == vals[::-1]
