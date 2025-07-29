#Search in binary search tree

class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def insertion(root,key):
    if root is None:
        return node(key)
    if root.key == key:
        return root
    if root.key < key:
        root.right = insertion(root.right,key)
    else:
        root.left = insertion(root.left,key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

def search(root,key):
    if root is None:
        return root
    if root.key == key:
        return root
    elif root.key < key:
        return search(root.right,key)
    else:
        return search(root.left,key)

root=node(50)
for i in [30,70,20,40,60,80]:
    root=insertion(root,i)

print("found" if search(root,19) else "not found")
print("found" if search(root,80) else "not found")

