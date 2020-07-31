import collections
# Iterative Python program for level order traversal and dfs traversal of Binary Tree 
  
# A node structure 
class Node: 
  
    # A utility function to create a new node 
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None
  
def inOrder(root):
    stack = [root]
    visited = set()
    while stack:
        
        node = stack.pop()
        
        if node is None:
            continue
        
        if node in visited:
            print(node.data)
            continue
        
        visited.add(node)
        
        stack.append(node.right)
        stack.append(node)
        stack.append(node.left)

def preOrder(root):
    stack = [root]
    visited = set()
    while stack:
        
        node = stack.pop()
        
        if node is None:
            continue
        
        if node in visited:
            print(node.data)
            continue
        
        visited.add(node)
        
        stack.append(node.right)
        stack.append(node.left)
        stack.append(node)

def postOrder(root):

    stack = [root]
    visited = set()
    while stack:
        
        node = stack.pop()
        
        if node is None:
            continue
        
        if node in visited:
            print(node.data)
            continue
        
        visited.add(node)

        stack.append(node)
        stack.append(node.right)
        stack.append(node.left)


def printLevelOrder(root):

    q = collections.deque()
    q.append((root,1))

    while q : 
        
        node, l = q.popleft()
        
        if node is None:
            continue

        print(node.data, l)

        q.append((node.left, l+1))
        q.append((node.right, l+1))
        
        

# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print ("\n\nLevel order traversal of binary tree is -")
printLevelOrder(root) 
print ("\n\nIn order traversal of binary tree is -")
inOrder(root)
print ("\n\nPre order traversal of binary tree is -")
preOrder(root)
print ("\n\nPost order traversal of binary tree is -")
postOrder(root)  

