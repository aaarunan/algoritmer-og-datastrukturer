from collections import defaultdict


def parse_file(file: str):
    with open(file, "r", encoding="UTF-8") as file:
        lines = file.read().splitlines()

    args = str.split(lines[0])
    graph = Graph(int(args[0]))

    for line in lines[1:]:
        nodes = str.split(line)
        graph.add(int(nodes[0]), int(nodes[1]))

    return graph


def main():
    files = ["ø6g1", "ø6g5", "ø6g6", "ø6g2"]

    for file in files:
        print(f"\nThis is graph '{file}'")
        graph = parse_file(file + ".txt")

        print("Graph:")
        print(graph, end="\n\n")

        graph.print_strongly_connected_components()


class Graph:
    def __init__(self, nodes: int) -> None:
        self.nodes = nodes
        self.graph = defaultdict(set)

    def add(self, start: int, end: int) -> None:
        self.graph[start].add(end)

    def reverse(self):
        reverse = Graph(self.nodes)

        for node in self.graph:
            for neighbor in self.graph[node]:
                reverse.add(neighbor, node)
        return reverse

    def dfs_traversal(self, node, visited, order):
        visited[node] = True
        for i in self.graph[node]:
            if not visited[i]:
                self.dfs_traversal(i, visited, order)
        order.append(node)

    def strongly_connected_components(self):
        order, components = [], []
        visited = [False] * self.nodes

        for node in range(self.nodes):
            if not visited[node]:
                self.dfs_traversal(node, visited, order)

        reverse = self.reverse()
        visited = [False] * self.nodes

        for node in order[::-1]:
            if not visited[node]:
                result = []
                reverse.dfs_traversal(node, visited, result)
                components.append(result)

        return components

    def print_strongly_connected_components(self):
        comps = self.strongly_connected_components()
        print(f"There are {len(comps)} strongly connected components:")

        for comp in comps:
            end = " --> "
            for node in comp:
                if node == comp[len(comp) - 1]:
                    end = ""
                print(node, end=end)
            print()

    def __repr__(self) -> str:
        string = ""
        for node in self.graph:
            string += f"{str(node)} --> {str(self.graph[node])} \n"
        return string


if __name__ == "__main__":
    main()
