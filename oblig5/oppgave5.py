import math
import tqdm
import random
from timeit import default_timer as timer


class Hashtable:
    collisions = 0
    entries = 0

    def __init__(self, table_size) -> None:
        self.table_size = table_size
        self.table_size = self.nearestPrime()
        self.table = [None] * table_size
        self.PRIME = table_size

    def put(self, key: str):
        hashcode = self.hash(key)
        node = self.table[hashcode]
        self.entries += 1
        if node is None:
            self.table[hashcode] = LinkedNode(key)
        else:
            self.collisions += 1
            node.append(key)

    def __getitem__(self, key: str):
        hashcode = self.hash(key)
        node = self.table[hashcode]
        if node is None:
            return None
        return node.find(key)

    def hash(self, value: str) -> int:
        hashcode = 0
        for index, char in enumerate(value):
            hashcode += ord(char) * (index + 1)
        return hashcode % self.table_size

    def hash_multi(self, value: int) -> int:
        A = value * (math.sqrt(5) - 1) / 2
        A -= int(A)
        return int(self.table_size * abs(A))

    def nearestPrime(self):
        table_size = self.table_size
        if (table_size & 1) != 1:
            table_size -= 1
        for l in range((table_size), 1, -2):
            flag = True
            for i in range(2, int(l**0.5) + 1):
                if l % i == 0:
                    flag = False
                    break
            if flag:
                return l
        return 3
    
    def h2(self, value):
        return (value % (self.PRIME-1))+1

    def double_hash_put(self, value):
        h1 = self.hash_multi(value)
        if self.table[h1] is None:
            self.entries += 1
            self.table[h1] = value
            return
        if self.table[h1] == value:
            self.collisions += 1
            return

        h2 = self.h2(value)
        index = h1
        while True:
            self.collisions += 1
            index = (index + h2) % self.table_size
            if self.table[index] == value:
                self.collisions += 1
                return
            if self.table[index] is None:
                self.table[index] = value
                self.entries += 1
                return

    @property
    def loadfactor(self):
        return self.entries / self.table_size

    @property
    def collisions_per_entry(self):
        return self.collisions / self.entries


class LinkedNode:
    value = None
    right = None

    def __init__(self, value) -> None:
        self.value = value

    def append(self, value):
        last = self
        new = LinkedNode(value)
        new.right = last.right
        last.right = new

    def find(self, value):
        if self.value == value:
            return self.value
        if self.right is None:
            return None
        return self.right.find(value)

    def print_nodes(self):
        output = ""
        node = self
        while node is not None:
            output += "-->" + node.value
            node = node.right
        print(output)


def print_results(table: Hashtable):
    for node in table.table:
        if node is None:
            continue
        if node.right is None:
            continue
        node.print_nodes()

    print("\namount of collisions:  ", table.collisions)
    print("entries:               ", table.entries)
    print("loadfactor:            ", table.loadfactor)
    print("collsions/person:      ", table.collisions_per_entry)
    print("\nget:                   ", table["Arunan Gnanasekaran"], "\n")


def del1():
    table = Hashtable(130)
    with open("navn.txt", "r", encoding="UTF-8") as f:
        lines = f.read().splitlines()
    for line in lines:
        table.put(line)
    print_results(table)


def del2():
    print("Creating list")
    numbers = [random.randint(0, 100_100_000) for _ in range(10_000_000)]
    table1 = Hashtable(11_000_000)
    print("Finished...")

    print("Testing... this might take a while")
    start = timer()
    for number in numbers:
        table1.double_hash_put(number)
    end = timer()- start

    print("Time on my hashset    ", end)
    print("Collisions            ", table1.collisions)
    print("Loadfactor            ", table1.loadfactor)
    print("Collisions per entry  ", table1.collisions_per_entry)

    python_dict = {}
    start = timer()

    for number in numbers:
        python_dict[number] = number
    print("Python dictionary time", timer() - start)



if __name__ == '__main__':
    del1()
    del2()


def test_get_all():
    table = Hashtable(137)
    with open("navn.txt", "r", encoding="UTF-8") as f:
        lines = f.read().splitlines()
    for line in lines:
        table.put(line)
    for line in lines:
        assert table[line] is not None
