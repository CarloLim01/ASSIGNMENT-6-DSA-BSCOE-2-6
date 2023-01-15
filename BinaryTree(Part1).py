# BINARY TREE (Part 1)

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
    
    # Defining Post Order Traversal Method 
    def post_order_traversal(self):
        elements = []
        
        # visit left tree
        if self.left:
            elements += self.left.post_order_traversal()
        
        # visit right tree
        if self.right:
            elements += self.right.post_order_traversal()
        
        # visit base node
        elements.append(self.data)

        return elements
    
    # Defining Pre Order Traversal Method
    def pre_order_traversal(self):
        elements = [self.data]
        
        # visit left tree
        if self.left:
            elements += self.left.pre_order_traversal()
        
        # visit right tree
        if self.right:
            elements += self.right.pre_order_traversal()

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
    
    # Calculating the Sum of All Elements
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
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
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    # Adding the Given Numbers
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("Input numbers:",numbers)
    print("Maximum Element:",numbers_tree.find_max())
    print("Minimum Element:",numbers_tree.find_min())
    print("Sum of All Elements:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
    
    # Adding My Full Name
    Name = ["A","L","B","E","R","T", "C","A","R","L","O", "L","I","M"]
    MyFullName = build_tree(Name)
    print("Input lName:",Name)
    print("Maximum Element:",MyFullName.find_max())
    print("Minimum Element:",MyFullName.find_min())
    print("In order traversal:", MyFullName.in_order_traversal())
    print("Pre order traversal:", MyFullName.pre_order_traversal())
    print("Post order traversal:", MyFullName.post_order_traversal())