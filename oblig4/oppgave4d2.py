from dataclasses import dataclass


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

    def add_node(self, string: str):
        if self.value is None:
            self.value = string
        else:
            if string < self.value:
                if self.left:
                    self.left.add_node(string)
                else:
                    self.left = Node(string)
            else:
                if self.right:
                    self.right.add_node(string)
                else:
                    self.right = Node(string)

    def traverse_tree(self):
        current_level = [self]
        center_rate = 64
        while current_level:
            next_level = []
            if all(node is None for node in current_level):
                break
            for node in current_level:
                if node is None:
                    value = "*"
                    next_level.append(None)
                    next_level.append(None)
                else:
                    value = node.value
                    next_level.append(node.left)
                    next_level.append(node.right)
                print(value.center(center_rate), end="")
            center_rate >>= 1
            current_level = next_level
            print("\n")
            


def main():
    
    root = Node(None)
    while True:
        root.add_node(input("Type a word: "))
        print(root.traverse_tree())


if __name__ == "__main__":
    main()
