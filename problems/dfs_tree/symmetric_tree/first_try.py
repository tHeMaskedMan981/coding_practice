

# A node structure 
class Node: 
  
    # A utility function to create a new node 
    def __init__(self, key): 
        self.data = key  
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.level_elements = []

    def isSymmetric(self, root):

        h = self.height(root) 
        
        for i in range(1, h+1): 
            self.printGivenLevel(root, i) 
            num = len(self.level_elements)
            print(self.level_elements)
            for i in range(0, int((num+1)/2)):
                if self.level_elements[i]!=self.level_elements[(num-1)-i]:
                    return False
            self.level_elements = []
        return True


    
    # Print nodes at a given level 
    def printGivenLevel(self,root , level): 
        if root is None: 
            self.level_elements.append('null')
            return
        if level == 1: 
            # print(root.data)
            self.level_elements.append(root.data)
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
root.right.right = Node(6)

print ("Level order traversal of binary tree is -")
Solution().isSymmetric(root)
# printLevelOrder(root) 


