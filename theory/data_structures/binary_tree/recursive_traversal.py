class Node(object):
    def __init__(self, value):
        self.data = value
        self.left = None 
        self.right = None 


def pre_order_traversal(root):
    
    if root is None:
        return
    
    ans.append(root.data)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)

    pass
        
def post_order_traversal(root):
    
    if root is None:
        return
    
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    ans.append(root.data)

    pass
        
def in_order_traversal(root):

    if root is None:
        return

    in_order_traversal(root.left)
    ans.append(root.data)
    in_order_traversal(root.right)

    pass
        
# Tree defination
root = Node("F")
root.left = Node("B")
root.left.left = Node("A")
root.left.right = Node("D")
root.left.right.left = Node("C")
root.left.right.right = Node("E")

root.right = Node("G")
root.right.right = Node("I")
root.right.right.left = Node("H")

ans = []
in_order_traversal(root)
print("\nIn order traversal : ", ans)


ans = []
pre_order_traversal(root)
print("\nPre-order traversal : ", ans)

ans = []
post_order_traversal(root)
print("\nPost-order traversal : ", ans)
