
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
    
    def add_child(self, data):
        if data == self.data:
            return 
        
        if data < self.data:
            #Add left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data) 
        else:
            #Add right 
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_tranversal(self):

         # left - node - right 
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_tranversal()
        # visit node
        elements.append(self.data)
        # visit right

        if self.right:
            elements += self.right.in_order_tranversal()

        return elements
    
    def post_order_traversal(self):
        # left - right - node
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)

        return elements
    def pre_order_traversal(self):
        # node - left - right 
        
        elements = []

        elements.append(self.data)

        # or elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements


    def search(self, val):
        if self.data == val: 
            return True 
        
        if val < self.data:
            # Val might be in left subtree
            if self.left:
                return self.left.search(val) 
            else:
                return False 
        if val > self.data:
            # Val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):

        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
        #solution
        # if self.left is None:
        #     return self.data
        # return self.left.find_min()
    
    def find_max(self):

        if self.right:
            return self.right.find_max()
        else: 
            return self.data
    
    def calculate_sum(self):
        sum = self.data

        if self.left:
            sum += self.left.calculate_sum()
        
        if self.right:
            sum += self.right.calculate_sum()

        return sum

        # solution
        # left_sum = self.left.calculate_sum() if self.left else 0
        # right_sum = self.right.calculate_sum() if self.right else 0
        # return self.data + left_sum + right_sum
    
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    n = [17, 3, 5, 20, 9, 23, 18, 34, 18, 4, 40]
    n_tree = build_tree(n)
    in_order = n_tree.in_order_tranversal()
    post_order = n_tree.post_order_traversal()
    pre_order = n_tree.pre_order_traversal()

    min = n_tree.find_min()
    max = n_tree.find_max()

    print("\nIn order: ")
    print(in_order)

    print("\nPost order: ")
    print(post_order)

    print("\nPre order: ")
    print(pre_order)

    print("Min node: ", min)
    print("Max node: ", max)

    sum = n_tree.calculate_sum()
    print("Sum of the numbers: ", sum)




