# creating a BST(binary search tree)

class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    def __str__(self):
        return f"{self.key} , {self.left} , {self.right}"

    
root =  node(5)



print(root)
