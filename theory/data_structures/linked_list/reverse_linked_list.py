class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverse(head):

    pre = None
    while head:
        # print(head.val)
        head.next, pre, head = pre, head, head.next
    return pre

def printlist(h):
    i=0
    while h:
        print("index ",i, " : ", h.val)
        h = h.next
        i+=1

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

printlist(head)
newhead = reverse(head)
printlist(newhead)
