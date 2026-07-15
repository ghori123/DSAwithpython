class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def get_successor(root):
    root = root.right
    while(root != None and root.left != None):
        root = root.left
    return root

def deletion(root , value):
    if (root == None):
        return root
    if ( root.data > value):
        root.left = deletion(root.left, value)
    elif(root.data < value):
       root.right = deletion(root.right, value) 
    else:
        if(root.left == None):
            return root.right
        if(root.right == None):
            return root.left
        else:
            succ = get_successor(root)
            root.data =succ.data
            root.right= deletion(root.right,succ.data)
    return root
        

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

root = insert(None, 20)
root = insert(root,15)
root = insert(root,12)
root = insert(root,30)
root = insert(root,40)
root = insert(root,18)

print("inorder is :", end="")
inorder(root)
print()
deletion(root, 15)
inorder(root)
deletion(root, 12)
print()
inorder(root)
print()
deletion(root, 30)
inorder(root)