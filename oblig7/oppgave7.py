from collections import defaultdict
import random


class PriorityQueue:
    queue = []

    def __init__(self) -> None:
        pass

    def swap(self, i, j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

    def heapify(self, end):
        if end != 0:
            for i in range((end // 2) - 1, -1, -1):
                self.heapify_util(i, end)

    def heapify_util(self, i, end):
        largest = i

        left = 2 * i + 1
        right = 2 * i + 2

        if left < end and self.queue[left] > self.queue[i]:
            largest = left

        if right < end and self.queue[right] > self.queue[i]:
            largest = right

        if largest != i:
            self.swap(largest, i)

        if right < end and self.queue[left] > self.queue[i]:
            self.swap(left, i)

    def insert(self, num):
        self.queue.append(num)
        self.heapify(len(self.queue))

    def peek(self):
        if len(self.queue) == 0:
            return None

        peek = self.queue.pop(0)
        self.heapify(len(self.queue))
        return peek


class Graph:
    def __init__(self, nodes: int) -> None:
        self.nodes = nodes
        self.graph = defaultdict(set)

    def add(self, start: int, end: int) -> None:
        self.graph[start].add(end)

    def dijikstras(self):
        return


def main():

    return


if __name__ == "__main__":
    main()


def test_peek():

    nums = random.sample(range(-100000, 100000), 5000)
    queue = PriorityQueue()

    for num in nums:
        queue.insert(num)

    peek = queue.peek()
    result = []
    while peek:
        result.append(peek)
        peek = queue.peek()

    assertion = result[:]
    assertion.sort()
    assert result == assertion[::-1]
