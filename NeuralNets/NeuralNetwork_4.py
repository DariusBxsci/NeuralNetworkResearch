#This code defines neural networks as an abstract syntax tree

class Node:
    leftChild = None
    rightChild = None
    op = ""

    def __init__(self):
        return

    def __init__(self, o = 0, left = None, right = None):
        self.op = o
        self.leftChild = left
        self.rightChild = right
        return

    def eval(self): #evaluate the tree by moving down the nodes and evaluating whenever there is a literal expression
        if self.rightChild == None and self.leftChild == None:
            return self.op
        else:
            if not self.rightChild == None:
                return str(eval(self.leftChild.eval() + " " + self.op + " " + self.rightChild.eval()))
            else:
                return str(eval(self.op + " " + self.leftChild.eval()))

def BuildTree(lst): #helper function to create a full syntax tree from a list using Node objects
    source = Node()
    source.op = lst[0]

    if len(lst) == 2 and len(lst[1]) > 1:
        source.leftChild = BuildTree(lst[1])
        source.rightChild = None
        return source
    elif len(lst) == 2 and len(lst[1]) == 1:
        source.leftChild = Node(lst[1][0],None,None)
        source.rightChild = None
        return source

    if len(lst[1]) == 1:
        source.leftChild = Node(lst[1][0],None,None)
    else:
        source.leftChild = BuildTree(lst[1])

    if len(lst[2]) == 1:
        source.rightChild = Node(lst[2][0],None,None)
    else:
        source.rightChild = BuildTree(lst[2])

    return source



#simple arithmetic:
arithmeticTree = ["*", ["-",["3"],["5"]], ["/",["4"],["2"]]] #outputs -4
arithmeticTree = BuildTree(arithmeticTree);
print arithmeticTree.eval();

#simple logic:
logicalTree = ["not",["and", ["or",["True"],["False"]], ["and",["False"],["True"]]]] #outputs True
logicalTree = BuildTree(logicalTree);
print logicalTree.eval();
