class Node:
    """
    This is one of the nodes in a binary tree
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# A function to do the traversal


def printDFS(root):
    """This function does a depth first search"""
    if (root == None):
        return []
    result = []
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)
        print(f"current value is {current.val}\n")
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)    
    return result

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

printDFS(a)
