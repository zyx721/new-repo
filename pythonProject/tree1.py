class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    def getlevel(self):
        level = 0
        p = self.parent
        while p:
            p=p.parent
            level+=1
        return level
    def print_tree(self):
        space = ' '*self.getlevel()*3
        prefix = space+ '|__'if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children :
                child.print_tree()

def build_product_tree():
    root = TreeNode('Nilupul')
    ch1 = TreeNode('Chinmay')
    ch2 = TreeNode('Gels')
    ch11 = TreeNode('Vishwa')
    ch12 = TreeNode('Amir')
    ch111 = TreeNode('Dhaval')
    ch112 = TreeNode('Abhijit')
    ch21 = TreeNode('Peter')
    ch22 = TreeNode('Waqas')

    ch1.add_child(ch11)
    ch1.add_child(ch12)
    ch11.add_child(ch111)
    ch11.add_child(ch112)
    ch2.add_child(ch21)
    ch2.add_child(ch22)
    root.add_child(ch1)
    root.add_child(ch2)
    return root
if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()