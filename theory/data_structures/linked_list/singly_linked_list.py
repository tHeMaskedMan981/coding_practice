# A simple Python program for traversal of a linked list 
  
# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # This function prints contents of linked list 
    # starting from head 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print (temp.data) 
            temp = temp.next
    

    def insert_in_start(self, node):
        node.next = self.head
        self.head = node
    

    def insert_in_order(self, node):

        if self.head is None:
            self.head = node
            return 

        if node.data < self.head.data:
            self.insert_in_start(node)
            return

        temp = self.head
        while (temp):

            if temp.next is None:
                temp.next = node
                break

            if node.data > temp.data and node.data < temp.next.data:
                node.next = temp.next
                temp.next = node
                break
            temp = temp.next


    def insert_at_end(self, node):
        temp = self.head
        while(temp):
            # print(temp.data)
            if temp.next is None:
                temp.next = node
                break
            temp = temp.next


    def delete_node(self, node):
        temp = self.head
        while (temp):

            if temp.next.data == node.data:
                temp.next = temp.next.next
                break
            temp = temp.next


# Code execution starts here 
# if __name__=='__main__': 
  
# Start with the empty list 
llist = LinkedList() 

llist.head = Node(10) 
node2 = Node(20) 
node3 = Node(30) 

llist.head.next = node2 # Link first node with second 
node2.next = node3 # Link second node with the third node 

llist.printList() 

print("\n\ninserting in start - 6") 
node4 = Node(6)
# print(fourth)

llist.insert_in_start(node4)
llist.printList()

print("\n\ninserting in end - 40")
node5 = Node(40)

llist.insert_at_end(node5)
llist.printList()

print("\n\ninserting numbers everywhere according to increasing order - ")

node6 = Node(25)
llist.insert_in_order(node6)
# llist.printList()

llist.insert_in_order(Node(35))
llist.insert_in_order(Node(45))
llist.insert_in_order(Node(15))
llist.insert_in_order(Node(3))
llist.insert_in_order(Node(50))
llist.printList()

print("\n\ndeleting node : 25 ")

llist.delete_node(Node(25))
llist.printList()