

# A node structure 
class Node: 
  
    # A utility function to create a new node 
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None


class Solution(object):

    def isSymmetric(self, root):

        if root is None:
            return True
        
        return self.isMirror(root.left, root.right)

    def isMirror(self, root1, root2):

        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None:
            return False
        
        if root1.data != root2.data:
            return False
        
        return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)


# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.right = Node(6)

print ("Level order traversal of binary tree is -")
print(Solution().isSymmetric(root))