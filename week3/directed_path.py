import requests
import sys
sys.setrecursionlimit(10000)

class DirectedGraph():

    def __init__(self):
        self.graph = {}
        self.checked = []

    def add_edge(self, nodeA , nodeB): #nodeA = Jeni, nodeB = Kiro
        if nodeA in self.graph:
            if nodeB not in self.graph[nodeA]:
                self.graph[nodeA].append(nodeB)
                if nodeB not in self.graph:
                    self.graph[nodeB] = []
                    self.checked.append(nodeB)
        else:
            self.graph[nodeA] = [nodeB]
            self.checked.append(nodeA)
            if nodeB not in self.graph:
                self.graph[nodeB] = []
                self.checked.append(nodeB)

    def get_neighbors_for(self, node):
        return self.graph[node]


    def path_between(self, nodeA, nodeB): #nodeA = Jeni, nodeB = Kiro
        list_of_results = []
        if nodeB in self.graph[nodeA] not in self.checked:
            return True
        elif self.graph[nodeA] is None:
            return False
        else:
            for node in self.graph[nodeA]:
                if self.path_between(node, nodeB) is True:
                    list_of_results.append(self.path_between(node, nodeB))
        for result in list_of_results:
            if result is True:
                return True

    
