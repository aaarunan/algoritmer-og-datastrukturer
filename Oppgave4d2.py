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
            if self.value < string:
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
        center_rate = 60
        while current_level:
            next_level = []
            for node in current_level:
                print(node.value.center(center_rate), end=" ")
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            print("\n")
            center_rate = center_rate >> 1
            current_level = next_level
            


def main():
    strings = ["hei", "du", "er", "stygg", "veldig", "moren", "din", "jf" " lasdkjf", "lsdkj" "dsljf", "lkfd", "øl"]
    root = Node(None)
    for string in strings:
        root.add_node(string)
    root.traverse_tree()


if __name__ == "__main__":
    main()
