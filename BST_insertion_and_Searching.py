class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, value):
    if(root == None):
        return Node(value)
    if (root.data == value):
        return root 
    if (root.data > value):
        root.left = insert(root.left , value)
    else:
         root.right = insert(root.right , value)
    return root

def inorder(root):
    if(root != None):
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def search(root, value):
    if(root == None):
        print("Element not found")
        return
    if (root.data == value):
        print(f"Element {value} is found")
        return
    if (root.data > value):
        search(root.left , value)
    else:
         search(root.right , value)
    return

root = insert(None, 20)
root = insert(root,15)
root = insert(root,12)
root = insert(root,30)
root = insert(root,40)
root = insert(root,18)

print("inorder is :", end="")
inorder(root)
print()

search(root,30)
search(root, 20)
search(root,60)