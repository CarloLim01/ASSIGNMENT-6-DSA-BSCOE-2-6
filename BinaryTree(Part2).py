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
    
    # Defining a Delete Method
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

    # Defining a Search Method
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

# Defining a Build Tree as a Helper Method
def build_tree(elements):
    print("\n\tBuilding tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    # Adding the Given Numbers
    print("\nNUMBERS:")
    
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    # this should print [1, 4, 9, 17, 18, 23, 34]
    print("\tAfter deleting 20:", numbers_tree.in_order_traversal()) 
    
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    # this should print [1, 4, 17, 18, 20, 23, 34]
    print("\tAfter deleting 9:", numbers_tree.in_order_traversal())  

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    # this should print [1, 4, 9, 18, 20, 23, 34]
    print("\tAfter deleting 17:", numbers_tree.in_order_traversal())  
    
    # Adding My Full Name
    print("\n\nMY FULL NAME:")
    
    MyFullName = build_tree(["A","L","B","E","R","T", "C","A","R","L","O", "L","I","M"])
    MyFullName.delete("B")
    print("\tAfter deleting B:", MyFullName.in_order_traversal())
    
    MyFullName = build_tree(["A","L","B","E","R","T", "C","A","R","L","O", "L","I","M"])
    MyFullName.delete("C")
    print("\tAfter deleting C:", MyFullName.in_order_traversal())
    
    MyFullName = build_tree(["A","L","B","E","R","T", "C","A","R","L","O", "L","I","M"])
    MyFullName.delete("I")
    print("\tAfter deleting I:", MyFullName.in_order_traversal())
    