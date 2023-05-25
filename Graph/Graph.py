class Graph():
    Nodes = [chr]
    weights = {}

    def addNode(self, A :chr):
        self.Nodes.append(A)

    def addWeight(self, A: chr,B: chr,i: int):
        self.weights[(A,B)] = i
