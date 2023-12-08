from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printBFS(root):
    if root == None:
        return []
    result = []
    queue = deque([root])
    while len(queue) > 0:
        current = queue.pop()
        result.append(current.val)

        if current.left:
            queue.appendleft(current.left)
        if current.right:
            queue.appendleft(current.right)

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

searched = printBFS(a)
for item in searched:
    print(item)
