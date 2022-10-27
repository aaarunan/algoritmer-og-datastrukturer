from dataclasses import dataclass
import tqdm

@dataclass
class Edge:
    start: int
    end: int
    weight: int


@dataclass
class Node:
    value: int
    edges: list[Edge]

    def append_edge(self, end: int, weight: int) -> None:
        self.edges.append(Edge(self.value, end, weight))


class Graph:
    def __init__(self, nodes: int, edges: list[Edge]) -> None:
        self.nodes = nodes
        self.edges = edges
        self.graph = [None] * self.nodes

    def add(self, start: int, end: int, weight: int) -> None:
        if self.graph[start] is not None:
            self.graph[start].append_edge(end, weight)
            return
        self.graph[start] = Node(start, [Edge(start, end, weight)])

    def dijikstras(self, start: int):
        distances = [[None, float("inf")]] * self.nodes
        distances[start] = ["start", 0]
        queue = PriorityQueue()
        queue.insert(self.graph[start].value, 0)

        visited = [False] * self.nodes
        pbar = tqdm.tqdm(total=self.nodes)
        print("Finding paths...")
        while queue.length != 0:
            index, distance = queue.peek()
            current_node = self.graph[index]

            if current_node is None:
                continue
            if visited[index]:
                continue
            pbar.update(1)
            visited[index] = True
            distances[current_node.value][1] = distance

            for edge in current_node.edges:
                if visited[edge.end]:
                    continue
                new_weight = distance + edge.weight
                if new_weight < distances[edge.end][1]:
                    queue.insert(edge.end, new_weight)
                    distances[edge.end] = [edge.start, new_weight]

        return distances

    def print_predecessors(self, distances):
        print("distance, path")
        for index, obj in enumerate(distances):
            print(index, "     ", end="")
            if obj[1] == float("inf"):
                print("unreachable")
                continue
            predecessor = obj[0]
            temp = []
            while predecessor != "start":
                temp.append(predecessor)
                predecessor = distances[predecessor][0]
            for predecessor in reversed(temp):
                print(
                    predecessor,
                    end="-->",
                )
            temp = []

            print(f" ({str(obj[1])})")

    def __repr__(self) -> str:
        return str(self.graph)


class PriorityQueue:

    distances = []
    length = 0
    indexes = []

    def swap(self, i, j):
        self.distances[i], self.distances[j] = self.distances[j], self.distances[i]
        self.indexes[i], self.indexes[j] = self.indexes[j], self.indexes[i]

    @staticmethod
    def left_child_index(i):
        return 2 * i + 1

    @staticmethod
    def right_child_index(i):
        return 2 * i + 2

    @staticmethod
    def parent_index(i):
        return (i - 1) // 2

    def insert(self, index, weight):
        self.distances.append(weight)
        self.indexes.append(index)
        self.length += 1
        self.heapify_up(self.length - 1)

    def change_priority(self, index, weight):
        self.distances[self.indexes[index]] = weight
        self.heapify_up(index)
        return

    def is_in_queue(self, index):
        if index < self.length and self.indexes[index] < self.length:
            print(1)
            return True
        return False

    def peek(self):
        # if self.length == 0:
        #    return None
        self.swap(0, self.length - 1)
        distance = self.distances.pop()
        peek = self.indexes.pop()
        self.length -= 1
        self.heapify_down(0)

        return [peek, distance]

    def heapify_up(self, i):
        while (self.parent_index(i) >= 0) and self.distances[
            self.parent_index(i)
        ] > self.distances[i]:
            self.swap(self.parent_index(i), i)
            i = self.parent_index(i)

    def heapify_down(self, i):
        left_child_index = self.left_child_index(i)
        while left_child_index < self.length:
            smallest_index = left_child_index
            right_child_index = self.right_child_index(i)
            if (
                right_child_index < self.length
                and self.distances[right_child_index] < self.distances[left_child_index]
            ):
                smallest_index = right_child_index
            if self.distances[i] < self.distances[smallest_index]:
                break
            self.swap(i, smallest_index)
            i = smallest_index
            left_child_index = self.left_child_index(i)


def main():
    graph = parse_from_file()
    distances = graph.dijikstras(1)
    graph.print_predecessors(distances)


def parse_from_file():
    print("parsing file...")
    with open("vg1.txt", "r", encoding="UTF-8") as file:
        lines = file.read().splitlines()
    args = lines[0].split()
    graph = Graph(int(args[0]), int(args[1]))
    for line in tqdm.tqdm(lines[1:]):
        values = line.split()
        graph.add(int(values[0]), int(values[1]), int(values[2]))
    return graph


if __name__ == "__main__":
    main()
