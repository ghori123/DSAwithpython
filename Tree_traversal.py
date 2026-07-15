class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def preorder(root):
    if (root != None):
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
    else:
        return
    
    
def inorder(root):
    if (root != None):
        inorder(root.left)
        print(root.data, end= " ")
        inorder(root.right)
    else:
        return
    

def postorder (root):
    if (root != None):
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = " ")
    else:
        return


root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(8)
print(" preorder is :", end="")
preorder(root)
print()
print(" inorder is :", end="")
inorder(root)
print()
print("postorder is :", end="")
postorder(root)