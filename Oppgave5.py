from threading import activeCount


class Hashtable:
    table_size = 137
    table = [None] * table_size
    collisions = []
    entries = 0

    def put(self, key: str):
        hashcode = self.hash(key)
        node = self.table[hashcode]
        self.entries += 1
        if node is None:
            self.table[hashcode] = LinkedNode(key)
        else:
            self.collisions.append(key)
            node.appendLast(key)

    def get(self, key: str):
        hashcode = self.hash(key)
        node = self.table[hashcode]
        if node is None:
            return None
        return node.getNode(key)

    def hash(self, value: str):
        hashcode = 0
        for index, char in enumerate(value):
            hashcode = ord(char) * (index + 1)
        return hashcode % self.table_size

    def loadfactor(self):
        return self.entries / self.table_size


class LinkedNode:
    value = None
    right = None

    def __init__(self, value) -> None:
        self.value = value

    def getLast(self):
        if self.right is None:
            return self

        return self.right.getLast()

    def appendLast(self, value):
        last = self.getLast()
        if self.value is None:
            self.value = value
        else:
            new = LinkedNode(value)
            last.right = new

    def getNode(self, value):
        if self.value == value:
            return self.value
        if self.right is None:
            return None
        print(self.value)
        return self.right.getNode(value)


def main():
    table = Hashtable()
    with open("navn.txt", "r", encoding="UTF-8") as f:
        lines = f.readlines()
        lastLine = None
        for line in lines:
            if lastLine is None:
                lastLine = line
            table.put(line)
            line = f.readline()

    print("collisions: \n", table.collisions)
    print("amount col:", len(table.collisions))
    print("entries:   ", table.entries)
    print("table size:", table.table_size)
    print("loadfactor:", table.loadfactor())


    
    print(table.get("Arunan Gnanasekaran\n"))


main()
