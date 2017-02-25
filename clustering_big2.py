class UnionFind:

    def __init__(self, nodes):
        self._unodes = nodes
        self._labels = dict()
        self._clusters = dict()
        idx = 1
        # put each node in separate cluster
        for n in self._unodes:
            self._labels[idx] = [n]
            self._clusters[n] = idx
            idx += 1

    def no_clusters(self):
        return len(self._labels)

    def find(self, n):
        if n in self._clusters:
            return self._clusters[n]
        return 0

    def union(self, n1, n2):
        n1_label = self.find(n1)
        n2_label = self.find(n2)
        if n1_label == 0 or n2_label == 0 or n1_label == n2_label:
            return
        # print("Union: " + str(n1_label) + ", " + str(n2_label))
        # merge n2 with n1
        changes = self._labels[n2_label]
        self._labels[n1_label] += self._labels[n2_label]
        for n in changes:
            self._clusters[n] = n1_label
        del self._labels[n2_label]


def run_clustering(path):
    no_nodes, bits, nodes = read_graph(path)
    unodes = set(nodes)
    unodes_sorted = sorted(list(unodes))
    union_find = UnionFind(unodes_sorted)

    for n in unodes_sorted:
        # print(clusters[n])
        # compute all neighbors of n
        # for each neighbour, find in unodes
        # if found, cluster together
        neighbours = get_neighbours(n, 2)
        neighbours.remove(n)
        # find smallest parent
        for neighbour in list(neighbours):
            union_find.union(n, neighbour)

    print(union_find.no_clusters())


def get_neighbours(node, distance):
    if distance < 1:
        return set()
    neighbours = set()
    # print(distance)
    for idx, bit in enumerate(node):
        # Flip current bit and recursively call for new value
        current = list(node)
        current[idx] = toggle_bit(bit)
        tup = tuple(current)
        neighbours.add(tup)
        neighbours = neighbours.union(get_neighbours(tup, distance - 1))
    # print(neighbours)
    return neighbours


def toggle_bit(bit):
    if bit == 1:
        return 0
    return 1


def read_graph(path):
    file_data = read_lines_from_file(path)
    no_nodes, bits = tuple(map(int, file_data[0].split(' ')))
    del file_data[0]
    nodes = []
    for line in file_data:
        nodes.append(tuple(map(int, line.strip().split(' '))))
    return no_nodes, bits, nodes


def hamming_distance(n1, n2):
    distance = 0
    for bit1, bit2 in zip(n1, n2):
        if bit1 != bit2:
            distance = distance + 1
    return distance


def read_lines_from_file(path):
    lst = []
    for line in open(path):
        lst.append(line.rstrip('\n'))
    return lst

if __name__ == "__main__":
    run_clustering("clustering_big.txt")

# ex2 6118
