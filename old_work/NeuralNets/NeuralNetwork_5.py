import NeuralNetwork_4 as net

def parseSymbol(symbol): #turn logical symbol into numbers
    if symbol == "True":
        return "1"
    elif symbol == "False":
        return "0"
    return symbol

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
                return str(eval(parseSymbol(self.leftChild.eval()) + " " + self.op + " " + parseSymbol(self.rightChild.eval())))
            else:
                return str(eval(self.op + " " + parseSymbol(self.leftChild.eval())))

#These trees are outlined in manuscript.pdf, section 2.2

#Evaluate by how many years a person is older than a second person
ageTree = ["*", ["-",["16"],["14"]], ["True"]]
ageTree = net.BuildTree(ageTree);
print "The first person is " + str(ageTree.eval()) + " years older than the second"

ageTree = ["*", ["-",["15"],["20"]], ["False"]]
ageTree = net.BuildTree(ageTree);
print "The first person is " + str(ageTree.eval()) + " years older than the second"
