
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
                return self.left
            
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self 

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
    
    def find_max(self):

        if self.right:
            return self.right.find_max()
        else: 
            return self.data
    
    

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    """
    Exercise => https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/9_Binary_Tree_2/9_binary_tree_part_2_exercise.md
    """
    
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_tranversal()) # this should print [1, 4, 9, 17, 18, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ",numbers_tree.in_order_tranversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ",numbers_tree.in_order_tranversal())  # this should print [1, 4, 9, 18, 20, 23, 34]