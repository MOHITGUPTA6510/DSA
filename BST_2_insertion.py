class BST_node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return BST_node(key)
    if root.val == key:
            return root
    if root.val < key:
            root.right = insert(root.right, key)
    else:
            root.left = insert(root.left, key)
    return root


def inorder (root):
    if root:
        inorder(root.left)
        print(root.val , end=" ")
        inorder(root.right)


r=BST_node(15)
a=[10,18,4,11,16,20,13]
b=len(a)
for i in range(0,b):
    r=insert(r,a[i])

inorder(r)
