# deletion in BST

# making a tree
class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

#for checking/printing the output
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)

#fir instering node and maintaning its structure

def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root

#find inorder seccessor
def get_successor(curr):
    curr = curr.right
    while curr.left:
        curr = curr.left
    return curr

# for deleting the node
def delete_node(root,key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_node(root.left ,key)
    elif key> root.val:
        root.right = delete_node(root.right,key)
    else:


        # for no child node
        if root.left is None and root.right is None:
            return None

        #for one child
        elif root.left is None :
            return root.right
        elif root.right is None:
            return root.left


        # for too child node

        else:
            successor = get_successor(root)
            root.val = successor.val
            root.right = delete_node(root.right,successor.val)
    return root

#making binary search tree
root = None
for i in [50,30,70,20,40,60,80]:
    root=insert(root,i)

inorder(root)
print("\n")
root =delete_node(root,80)
print("\n")
inorder(root)
