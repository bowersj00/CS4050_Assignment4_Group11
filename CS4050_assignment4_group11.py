class Heap:
    def __init__(self):
        self.heap = dict()

    def heap_ini(self, keys, n):
        self.heap = dict(zip(n, keys))

    def in_heap(self, id):
        return id in self.heap

    def min_key(self):
        return self.heap[min(self.heap, key=self.heap.get)]

    def min_id(self):
        return min(self.heap, key=self.heap.get)

    def key(self, id):
        return self.heap[id]

    def delete_min(self):
        self.heap.pop(self.min_id())

    def decrease_key(self, id, new_key):
        if (new_key > self.heap[id]):
            self.heap[id] = new_key
