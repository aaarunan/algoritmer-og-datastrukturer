import math
import random
from timeit import default_timer as timer


class Hashtable:
    collisions = []
    entries = 0

    def __init__(self, table_size) -> None:
        self.table_size = table_size
        self.table = [None] * table_size

    def put(self, key: str):
        hashcode = self.hash_prime(key)
        node = self.table[hashcode]
        self.entries += 1
        if node is None:
            self.table[hashcode] = LinkedNode(key)
        else:
            self.collisions.append(key)
            node.append_last(key)

    def int_put(self, key: int):
        hashcode = self.hash_multi(key)
        node = self.table[hashcode]
        self.entries += 1
        if node is None:
            self.table[hashcode] = LinkedNode(key)
        else:
            self.collisions.append(key)
            node.append_last(key)

    def get(self, key: str):
        hashcode = self.hash_prime(key)
        node = self.table[hashcode]
        if node is None:
            return None
        return node.get(key)

    def hash(self, value: str) -> int:
        hashcode = 0
        for index, char in enumerate(value):
            hashcode += int(char) * (index + 1)

        return hashcode % self.table_size

    def hash_prime(self, value: str):
        hashcode = 0
        for char in value:
            hashcode = hashcode * 31 + ord(char)
        return hashcode % self.table_size

    def hash_multi(self, value: int) -> int:
        A = value * (math.sqrt(5) - 1) / 2
        A -= int(A)
        return int(len(self.table) * abs(A))

    def loadfactor(self):
        return self.entries / self.table_size


class LinkedNode:
    value = None
    right = None

    def __init__(self, value) -> None:
        self.value = value

    def get_last(self):
        if self.right is None:
            return self

        return self.right.get_last()

    def append_last(self, value):
        last = self.get_last()
        if self.value is None:
            self.value = value
        else:
            new = LinkedNode(value)
            last.right = new

    def get(self, value):
        if self.value == value:
            return self.value
        if self.right is None:
            return None
        return self.right.get(value)


def main():
    table = Hashtable(137)
    with open("navn.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            if line[-1:] == "\n":
                line = line[0:-1]
                count += 1
            table.put(line)

    print("collisions: \n", table.collisions)
    print("amount col:", len(table.collisions))
    print("entries:   ", table.entries)
    print("lines:     ", count)
    print("table size:", table.table_size)
    print("loadfactor:", table.loadfactor())
    print("coll/perso:", len(table.collisions) / table.entries)

    print(table.get("Arunan Gnanasekaran"))


def main2():
    numbers = [random.randint(-1_000_000, 1_000_000) for _ in range(10_000_00)]
    table = Hashtable(10_000_019)
    print("Setup complete")
    start = timer()
    for number in numbers:
        table.int_put(number)
    print(timer() - start)
    print(len(table.collisions))
    answer = {}
    start = timer()
    for number in numbers:
        answer.update({number: number})
    print(timer() - start)


main()
main2()
