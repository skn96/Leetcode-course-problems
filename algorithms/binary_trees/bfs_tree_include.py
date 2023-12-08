from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def checkBFS(root, target):
    if root == None:
        return False

    queue = deque([root])
    while len(queue) > 0:
        current = queue.pop()
        #print(current.val)
        if current.val == target:
            return True

        if current.left:
            queue.appendleft(current.left)
        if current.right:
            queue.appendleft(current.right)

    return False


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

isTarget = checkBFS(a, "m")
if isTarget:
    print("The requested target is found \n")
else:
    print("Target not found\n")