from collections import defaultdict
from dataclasses import dataclass
from math import dist

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
        if self.graph[start] is not None:
            self.graph[start].append_edge(end, weight)
            return
        self.graph[start] = Node(start, [Edge(start, end,weight)])

    def dijikstras(self, start: int):
        distances = [float("inf")] * self.nodes
        distances[start] = 0
        predecessors = [None] * self.nodes
        queue = PriorityQueue()
        queue.insert(self.graph[start], 0)
        visited = set()
        for node in self.graph:
            if node == None:
                continue
            if node.value != start:
                queue.insert(node, float("inf"))
        
        while not queue.is_empty(): 
            current_node, distance = queue.peek()
            if current_node.value in visited:
               continue
            visited.add(current_node.value)
            for edge in current_node.edges:
                if edge.end not in visited:
                    new_weight = distance + edge.weight
                    queue.insert(, new_weight)
            distances[current_node.value] = distance
            predecessors[current_node.value] = current_node
        
        print(distances)
            
                   

    def __repr__(self) -> str:
        return str(self.graph)

class PriorityQueue:
    distances = []
    nodes = []

    def swap(self, i, j):
        self.distances[i], self.distances[j] = self.distances[j], self.distances[i]
        self.nodes[i], self.nodes[j] = self.nodes[j], self.nodes[i]

    def is_empty(self):
        if len(self.nodes) == 0:
           return True 

        return False
    
    def update_node(self, node, weight):
        self.distances[self.nodes[node].value] = weight
        self.heapify(0, len(self.nodes))
    
    def get_distance(self, node):
        print(self.nodes)
        print(node)
        return self.distances[self.nodes[node].value]

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


def main():
    graph = parse_from_file()
    print(graph.dijikstras(1))
    return

def parse_from_file():
    with open("vg1.txt", "r", encoding="UTF-8") as file:
        lines = file.read().splitlines()
    args = lines[0].split()
    graph = Graph(int(args[0]), int(args[1]))
    for line in lines[1:]:
        values = line.split()
        graph.add(int(values[0]), int(values[1]), int(values[2]))
    return graph

if __name__ == "__main__":
    main()
