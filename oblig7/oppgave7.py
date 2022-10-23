from collections import defaultdict
from dataclasses import dataclass
from dis import dis
from math import dist
import tqdm

@dataclass
class Edge:
    start: int
    end: int
    weight: int

@dataclass
class Node:
    value : int
    edges : list[Edge]

    def append_edge(self,end: int, weight: int) -> None:
        self.edges.append(Edge(self.value, end, weight))


class Graph:
    def __init__(self, nodes: int, edges : list[Edge]) -> None:
        self.nodes = nodes
        self.edges = edges
        self.graph = [None] * self.nodes
    

    def add(self, start: int, end: int, weight: int) -> None:
        if start is None:
            raise None
        if self.graph[start] is not None:
            self.graph[start].append_edge(end, weight)
            return
        self.graph[start] = Node(start, [Edge(start, end,weight)])
    
        

    def dijikstras(self, start: int):
        distances = [[None,float("inf")]] * self.nodes
        distances[start] = ["start", 0]

        temp = [float("inf")] * self.nodes
        temp[start] = 0

        queue = PriorityQueue(self.graph[:], temp)
        visited = set()
        pbar = tqdm.tqdm(total=self.nodes)
        pbar.display()
        while not queue.is_empty(): 
            current_node, distance = queue.peek()
            if current_node.value in visited:
               continue
            pbar.update(1)
            visited.add(current_node.value)
            distances[current_node.value][1] = distance
            for edge in current_node.edges:
                if edge.end in visited:
                    continue
                new_weight = distance + edge.weight
                if new_weight < distances[edge.end][1]:
                    queue.insert(self.graph[edge.end], new_weight)
                    distances[edge.end] = [edge.start, new_weight]
        print(distances)
        pbar.close()
        #self.print_predecessors(distances, start)
        
    def print_predecessors(self, distances, start):
        print("distance, path")
        for obj in distances:
            print(obj[0], "     ", end="")
            if (obj[1] == float("inf")):
                print("inf")
                continue
            if obj[1] is None:
                print("start")
            predecessor = obj[0]
            while predecessor != "start":
                print(predecessor, end="-->")
                predecessor = distances[predecessor][0]

            print("start")

    def __repr__(self) -> str:
        return str(self.graph)

class PriorityQueue:

    def __init__(self, nodes, distances) -> None:
        self.distances = distances
        self.nodes = nodes
        print(len(distances))
        self.heapify(len(nodes))

    def swap(self, i, j):
        self.distances[i], self.distances[j] = self.distances[j], self.distances[i]
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def is_empty(self):
        if len(self.nodes) == 0:
           return True 

        return False

    def heapify(self, end):
        if end != 0:
            for i in range((end // 2) - 1, -1, -1):
                self.heapify_util(i, end)

    def heapify_util(self, i, end: Node):
        smallest = i

        left = 2 * i + 1
        right = 2 * i + 2

        if left < end and self.distances[left] < self.distances[i]:
            smallest = left

        if right < end and self.distances[right] < self.distances[i]:
            smallest = right

        if smallest != i:
            self.swap(smallest, i)

        if right < end and self.distances[left] < self.distances[i]:
            self.swap(left, i)

    def insert(self, node, weight):
        if node is None:
            return
        self.nodes.append(node)
        self.distances.append(weight)
        self.heapify(len(self.nodes))
    
        
    def peek(self):
        if len(self.nodes) == 0:
            return None

        peek = self.nodes.pop(0)
        distance = self.distances.pop(0)
        self.heapify(len(self.nodes))
        return [peek, distance]

    def __repr__(self) -> str:
        return str(self.nodes)


def main():
    graph = parse_from_file()
    graph.dijikstras(1)
    return

def parse_from_file():
    with open("vg4.txt", "r", encoding="UTF-8") as file:
        lines = file.read().splitlines()
    args = lines[0].split()
    graph = Graph(int(args[0]), int(args[1]))
    for line in lines[1:]:
        values = line.split()
        graph.add(int(values[0]), int(values[1]), int(values[2]))
    return graph

if __name__ == "__main__":
    main()
