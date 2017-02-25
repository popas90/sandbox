class Edge:

    def __init__(self, prop):
        self.v1 = prop[0]
        self.v2 = prop[1]
        self.cost = prop[2]

    def __str__(self):
        return str(self.v1) + " - " + str(self.v2) + ", " + str(self.cost)

    def __repr__(self):
        return self.__str__()


class UnionFind:

    def __init__(self, nodes):
        self._clusters = dict()
        for node in nodes:
            self._clusters[node] = node
        self._no_clusters = len(nodes)

    def find(self, node):
        return self._clusters[node]

    def union(self, n1, n2):
        # the nodes already are in the same cluster
        if self._clusters[n1] == self._clusters[n2]:
            return
        print("Union: " + str(n1) + ", " + str(n2))
        parent_n1 = self.find(n1)
        parent_n2 = self.find(n2)
        for node, parent in self._clusters.items():
            if self._clusters[node] == parent_n2:
                self._clusters[node] = parent_n1
                print("Updated " + str(node) + "  " + str(self._clusters[n1]))
        count = set()
        for _, cluster in self._clusters.items():
            count.add(cluster)
        self._no_clusters = len(count)

    def no_clusters(self):
        return self._no_clusters

    def clusters(self):
        return self._clusters

    def __str__(self):
        return "UnionFind: " + str(len(self._clusters)) + " nodes, " + \
            str(self._no_clusters) + " clusters"


def extract_nodes_from_edges(edges):
    nodes = set()
    for edge in edges:
        nodes.add(edge.v1)
        nodes.add(edge.v2)
    return nodes


def run_clustering(path, k):
    no_nodes, edges = read_graph(path)
    union_find = UnionFind(extract_nodes_from_edges(edges))
    # edges.sort(key=lambda e: e.cost, reverse=False)
    edges = sorted(edges, key=lambda m: (m.cost), reverse=False)
    idx = 0
    while union_find.no_clusters() > 4:
        union_find.union(edges[idx].v1, edges[idx].v2)
        # print(union_find.no_clusters())
        idx += 1
    # print(union_find.clusters())
    for edge in edges:
        if union_find.find(edge.v1) != union_find.find(edge.v2):
            print(union_find.find(edge.v1))
            print(union_find.find(edge.v2))
            print(edge)
            break


def read_graph(path):
    file_data = read_lines_from_file(path)
    no_nodes = int(file_data[0])
    del file_data[0]
    edges = []
    for line in file_data:
        edges.append(Edge(list(map(int, line.strip().split(' ')))))
    return no_nodes, edges


def read_lines_from_file(path):
    lst = []
    for line in open(path):
        lst.append(line.rstrip('\n'))
    return lst

if __name__ == "__main__":
    run_clustering("clustering1.txt", 4)

# ex1 106
