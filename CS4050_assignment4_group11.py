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

def get_input_adjacency_matrix(file_path):
    with open(file_path, 'r') as f:
        # Number of vertices
        n = int(f.readline().strip())
        
        # Initialize n×n matrix with infinities, and 0 on the diagonal
        matrix = [[float('inf')] * n for _ in range(n)]
        for u in range(n):
            matrix[u][u] = 0.0
        
        # Read edges
        for line in f:
            parts = line.strip().split()
            if len(parts) != 3:
                continue  # skip empty or malformed lines
            i, j, w = parts
            u, v = int(i) - 1, int(j) - 1
            weight = float(w)
            matrix[u][v] = weight
            matrix[v][u] = weight  # undirected
    
    return matrix


def prim_mst(adj_matrix):
    n = len(adj_matrix)
    ids  = list(range(1, n+1))
    keys = [float('inf')] * n
    parent = {i: None for i in ids}

    keys[0] = 0.0

    H = Heap()
    H.heap_ini(keys, ids)

    mst = []
    while H.heap:
        u = H.min_id()
        H.delete_min()

        if parent[u] is not None:
            p = parent[u]
            w = adj_matrix[p-1][u-1]
            mst.append((p, u, w))

        for v in ids:
            w_uv = adj_matrix[u-1][v-1]
            if w_uv < float('inf') and H.in_heap(v) and w_uv < H.key(v):
                parent[v] = u
                H.decrease_key(v, w_uv)

    return mst

mat = get_input_adjacency_matrix("graph")
mst_edges = prim_mst(mat)
print("Edges of MST in order:")
for u, v, w in mst_edges:
    print(f"{u} -- {v}  (weight {w})")