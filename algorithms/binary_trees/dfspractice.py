from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printDFS(root):
    if root == None:
        return []
    result = []
    stack = deque([root])

    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

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

sortedArr = printDFS(a)
print(sortedArr)