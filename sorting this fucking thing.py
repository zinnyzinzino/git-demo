class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def sort_lists(head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        l1 = sort_lists(head)
        l2 = sort_lists(mid)
        return mergelists (l1, l2)
        
        
def mergelists(l1, l2):
        dummy = Node(0)
        tail = dummy
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next