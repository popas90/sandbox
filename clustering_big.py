def run_clustering(path):
    no_nodes, bits, nodes = read_graph(path)
    unodes = set(nodes)
    unodes_sorted = sorted(list(unodes))
    clusters = dict()
    idx = 1
    # put each node in separate cluster
    for n in unodes_sorted:
        clusters[n] = idx
        idx += 1

    idx = 1
    for n in unodes_sorted:
        # print(clusters[n])
        # compute all neighbors of n
        # for each neighbour, find in unodes
        # if found, cluster together
        neighbours = get_neighbours(n, 2)
        # neighbours.remove(n)
        parent = clusters[n]
        # find smallest parent
        for neighbour in list(neighbours):
            if neighbour in clusters:
                if parent > clusters[neighbour]:
                    parent = clusters[neighbour]

        for neighbour in list(neighbours):
            if neighbour in clusters:
                clusters[neighbour] = parent

        # Check
        if parent > idx:
            print("Error: " + str(idx) + ", " + str(parent))
            break
        idx += 1

    idx = 1
    for n in unodes_sorted:
        # print(clusters[n])
        # compute all neighbors of n
        # for each neighbour, find in unodes
        # if found, cluster together
        neighbours = get_neighbours(n, 2)
        # neighbours.remove(n)
        parent = clusters[n]
        # find smallest parent
        for neighbour in list(neighbours):
            if neighbour in clusters:
                if parent > clusters[neighbour]:
                    parent = clusters[neighbour]

        for neighbour in list(neighbours):
            if neighbour in clusters:
                clusters[neighbour] = parent
        idx += 1

    idx = 1
    for n in unodes_sorted:
        # print(clusters[n])
        # compute all neighbors of n
        # for each neighbour, find in unodes
        # if found, cluster together
        neighbours = get_neighbours(n, 2)
        # neighbours.remove(n)
        parent = clusters[n]
        # find smallest parent
        for neighbour in list(neighbours):
            if neighbour in clusters:
                if parent > clusters[neighbour]:
                    parent = clusters[neighbour]

        for neighbour in list(neighbours):
            if neighbour in clusters:
                clusters[neighbour] = parent
        idx += 1

    unique = set(val for val in clusters.values())
    print(len(unique))

    idx = 1
    finish = False
    for n in unodes_sorted:
        neighbours = get_neighbours(n, 2)
        for neighbour in list(neighbours):
            if neighbour in clusters:
                if clusters[n] != clusters[neighbour]:
                    print("Error: " + str(idx))
                    finish = True
                    break
        if finish:
            break
        idx += 1


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

# ugly, but it works - see clustering_big2.py for more elegant solution
# ex2 6118
