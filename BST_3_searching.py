class node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def search(root,key):
    if root is None or root.val == key:
        return root

    if root.val < key :
        return search(root.right, key)


    else:
        return search(root.left, key)

root =node(50)
root.left = node(30)
root.right = node(70)
root.left.left = node(20)
root.left.right = node(40)
root.right.left = node(60)
root.right.right = node(80)

print("found" if search(root,19) else "Not found")
print("found" if search(root,80) else "Not found")
