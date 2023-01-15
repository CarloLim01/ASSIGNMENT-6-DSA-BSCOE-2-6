# BINARY TREE (Part 2)

# Defining Binary Search Node Class
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    # Defining In Order Traversal Method
    def in_order_traversal(self):
        elements = []
        
        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # Finding the Maximum Element
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # Finding the Minimum Element 
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()