import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.grafo = nx.Graph()
        self.situazioni = []
        self.nazioni = []
        self.result = {}
        self.idMap = {}


    def getGrafo(self, year):
        self.situazioni = DAO.getAllBeforYear(year)
        self.nazioni = DAO.getAllCountries()
        lista = DAO.getCountriesYear(year)
        for i in lista:
            self.grafo.add_node(i.CCode)
            self.idMap[i.CCode] = i.StateNme
        for row in self.situazioni:
            self.grafo.add_edge(row.state1no, row.state2no)


    def getNumNodes(self):
        return len(self.grafo.nodes)
    def getNumEdges(self):
        return len(self.grafo.edges)

    def getName(self, code):
        return self.idMap[code]


    def getConnessa(self):
        #count = 0
        # print(self.getNumNodes())
        # print(self.getNumEdges())

        # for i in self.grafo.nodes:
        #     print(i)
        for v in self.grafo.nodes:
            stato = ""
            confini = self.grafo.degree[v]
            for i in self.nazioni:
                if i.CCode == v:
                    stato = i.StateNme

            # if stato == "":
            #     stato = v
            self.result[stato] = confini
            # if confini != 0:
            #     count+=1
        ciao = nx.connected_components(self.grafo)
        return self.result, len(list(ciao))

    def getCompConnessa(self, v0):
        lista = []
        if v0 in self.grafo.nodes:
            connComp = nx.node_connected_component(self.grafo, v0)
            connComp.remove(v0)
            for i in connComp:
                for j in self.nazioni:
                    if i == j.CCode:
                        lista.append(j.StateNme)
        return lista
