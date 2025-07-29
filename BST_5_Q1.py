#insert a node program
class node():
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def insert(root,key):
    if root is None:
        return node(key)
    if key < root.key:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

root=node(10)
for i in [20,70,10,3,6,30,28]:
    root=insert(root,i)

inorder(root)

    
