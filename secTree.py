
# По уровням слева направо вывод
class Tree:
    def __init__(self, letter:str, left = None, right = None) -> None:
        self.letter = letter
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(Tree.letter)
    

def print_ordered(tree:Tree):
    letters_dict = {}
    def print_tree(tree:Tree=tree, level:int = 0):
        if tree == None: return
        if letters_dict.get(level) == None: letters_dict[level] = tree.letter
        else: letters_dict[level] += tree.letter
        level += 1
        print_tree(tree.left, level)
        print_tree(tree.right, level)
    print_tree()
    print(''.join(list(letters_dict.values())))


tree = Tree('A', Tree("B", Tree("D"), Tree("E")), Tree("C", None, Tree("F")))

print_ordered(tree)

    
