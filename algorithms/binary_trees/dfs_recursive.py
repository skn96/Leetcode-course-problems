class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printDFS(root):
    if root == None:
        return []
    result = []
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return result

def printDFS_recursive(root):
    if (root == None):
        return []
    leftValues = printDFS_recursive(root.left)
    rightValues = printDFS_recursive(root.right)
    return [root.val] + rightValues + leftValues



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

searched = printDFS(a)
searched2 = printDFS_recursive(a)
for item in searched:
    print(item)

print("\n")

for item in searched2: 
    print(item)