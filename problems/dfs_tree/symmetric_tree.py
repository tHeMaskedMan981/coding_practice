

# A node structure 
class Node: 
  
    # A utility function to create a new node 
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):

        h = self.height(root) 
        level_elements = []
        for i in range(1, h+1): 
            self.printGivenLevel(root, i) 
            num = len(level_elements)
            for i in range(0, int((num+1)/2)):
                if level_elements[i]!=level_elements[(num-1)-i]:
                    return False
            level_elements = []
        return True



    # Function to  print level order traversal of tree 
    def printLevelOrder(self,root): 
        pass
    
    # Print nodes at a given level 
    def printGivenLevel(self,root , level): 
        if root is None: 
            return
        if level == 1: 
            print(root.data)
        elif level > 1 : 
            self.printGivenLevel(root.left , level-1) 
            self.printGivenLevel(root.right , level-1) 
    
    def height(self,node): 
        if node is None: 
            return 0 
        else : 
            # Compute the height of each subtree  
            lheight = self.height(node.left) 
            rheight = self.height(node.right) 
    
            #Use the larger one 
            return max(lheight, rheight) + 1
    


# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
  
print ("Level order traversal of binary tree is -")
Solution().isSymmetric(root)
# printLevelOrder(root) 


