import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.grafo = nx.Graph()
        self.situazioni = []
        self.nazioni = []
        self.result = {}


    def getGrafo(self, year):
        self.situazioni = DAO.getAllBeforYear(year)
        self.nazioni = DAO.getAllCountries()
        for i in self.nazioni:
            self.grafo.add_node(i.StateAbb)
        for row in self.situazioni:
            self.grafo.add_edge(row.state1ab, row.state2ab)

    def getNumNodes(self):
        return len(self.grafo.nodes)
    def getNumEdges(self):
        return len(self.grafo.edges)


    def getConnessa(self):
        for v in self.grafo.nodes:
            stato = ""
            confini = self.grafo.degree[v]
            for i in self.nazioni:
                if i.StateAbb == v:
                    stato = i.StateNme

            if stato == "":
                stato = v
            self.result[stato] = confini
        return self.result, nx.number_connected_components(self.grafo)

    def getCompConnessa(self, v0):
        lista = []
        connComp = nx.node_connected_component(self.grafo, v0)
        connComp.remove(v0)
        for i in connComp:
            for j in self.nazioni:
                if i == j.StateAbb:
                    lista.append(j.StateNme)
        return lista