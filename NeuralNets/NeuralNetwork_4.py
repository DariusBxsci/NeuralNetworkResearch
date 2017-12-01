class Node:
    leftChild = None
    rightChild = None
    op = ""

    def __init__(self, o = 0, left = None, right = None):
        self.op = o
        self.leftChild = left
        self.rightChild = right
        return

    def eval(self):
        if self.op.isdigit():
            return self.op
        elif self.leftChild == None or self.rightChild == None:
            return self.op
        else:
            return str(eval(self.leftChild.eval() + self.op + self.rightChild.eval()))

node = Node("*", Node("-",Node("3"),Node("4")), Node("/",Node("4"),Node("2"))) #print result of (3 - 4) * (4 / 2)

print node.eval();
