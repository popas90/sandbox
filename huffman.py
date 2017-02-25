from heapq import heapify, heappush, heappop


class Tree:

    def __init__(self, left, right):
        self._left = left
        self._right = right

    def get_data(self):
        return self._left.get_data() + self._right.get_data()

    def get_max_depth(self):
        left_depth = self._left.get_max_depth()
        right_depth = self._right.get_max_depth()
        if left_depth > right_depth:
            return left_depth + 1
        return right_depth + 1

    def get_min_depth(self):
        left_depth = self._left.get_min_depth()
        right_depth = self._right.get_min_depth()
        if left_depth < right_depth:
            return left_depth + 1
        return right_depth + 1

    def __eq__(self, other):
        return self.get_data() == other.get_data()

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.get_data() < other.get_data()

    def __le__(self, other):
        return self.get_data() <= other.get_data()

    def __gt__(self, other):
        return self.get_data() > other.get_data()

    def __ge__(self, other):
        return self.get_data() >= other.get_data()

    def __repr__(self):
        return "Tree: " + str(self.get_data())


class Leaf:

    def __init__(self, data):
        self._data = data

    def get_data(self):
        return self._data

    def get_max_depth(self):
        return 0

    def get_min_depth(self):
        return 0

    def __eq__(self, other):
        return self.get_data() == other.get_data()

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.get_data() < other.get_data()

    def __le__(self, other):
        return self.get_data() <= other.get_data()

    def __gt__(self, other):
        return self.get_data() > other.get_data()

    def __ge__(self, other):
        return self.get_data() >= other.get_data()

    def __repr__(self):
        return "Leaf: " + str(self.get_data())


def run_huffman(path):
    _, weights = read_huffman(path)
    heapify(weights)
    while len(weights) > 1:
        first = heappop(weights)
        second = heappop(weights)
        new_tree = Tree(first, second)
        heappush(weights, new_tree)
    assert len(weights) == 1
    print(weights[0])
    print(weights[0].get_max_depth())
    print(weights[0].get_min_depth())


def read_huffman(path):
    file_data = read_lines_from_file(path)
    no_symbols = int(file_data[0])
    del file_data[0]
    weights = []
    for line in file_data:
        weights.append(Leaf(int(line.strip())))
    return no_symbols, weights


def read_lines_from_file(path):
    lst = []
    for line in open(path):
        lst.append(line.rstrip('\n'))
    return lst

if __name__ == "__main__":
    run_huffman("huffman.txt")

# ex1 19
# ex2 9
