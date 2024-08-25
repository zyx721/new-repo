class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if data == self.data :
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    def in_order_traversal(self):
        elements =[]
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    def delete(self,val):
        if self.data>val:
            if self.left:
                self.left = self.left.delete(val)
        elif self.data<val:
            if self.right:
                self.right =self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data
    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data
    def calculate_sum(self,s=0):
        s+=self.data
        return self.left.calculate_sum() + self.right.calculate_sum()
    def post_order_traversal(self):
        elements=[]
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    def pre_order_traversal(self):
        elements=[self.data]
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()

        return elements

    def draw_tree(self, depth=0):
        if self.right:
            self.right.draw_tree(depth + 1)
        print("   " * depth + str(self.data))
        if self.left:
            self.left.draw_tree(depth + 1)
    def search(self,val):
        if self.data == val:
            return True
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        return False
def bulid_tree(elements):
    s = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        s.add_child(elements[i])
    return s

elements = [17,4,1,20,9,23,18,34]
tree = bulid_tree(elements)
tree.draw_tree()
print(tree.in_order_traversal())
print(tree.search(1))
print(tree.find_max())
print(tree.find_min())
print(tree.in_order_traversal())
print(tree.pre_order_traversal())
print(tree.post_order_traversal())
tree.delete(23)
tree.draw_tree()