
class Tree:
    def __init__(self, cargo, left=None, right=None) -> None:
        self.cargo = cargo
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return str(self.cargo)
    

def total(tree:Tree):
    if tree == None: return 0
    return total(tree.left) + total(tree.right) + tree.cargo

def print_tree(tree:Tree, level=0):
    if tree == None: return
    print_tree(tree.left, level+1)
    print(' ' * level + str(tree.cargo))
    print_tree(tree.right, level+1)

print(Tree(5, left=4, right=10))

tree = Tree(1, Tree(5, Tree(5), Tree(14)), Tree(10, Tree(12), Tree(15)))
print(total(tree))

print(print_tree(tree))






























# class Tree:
#     def __init__(self, cargo, left=None, right=None):
#         self.cargo = cargo
#         self.left = left
#         self.right = right
    
#     def __str__(self) -> str:
#         return str(self.cargo)
        
# def total(tree:Tree) -> int:
#     if tree == None: return 0
#     return total(tree.left) + total(tree.right) + tree.cargo



# if __name__ == "__main__":
#     left = Tree(2)
#     right = Tree(3)
#     tree = Tree(1, left, right)
#     print(total(tree))
