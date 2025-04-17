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
        n = int(f.readline().strip())

        # create a matrix that places inf at all points
        matrix = [[float('inf')] * n for _ in range(n)]
        for u in range(n):
            matrix[u][u] = 0.0 # set diagonal to 0 as the distance from a node to itself is 0
        for line in f: # for each connecting line we are given add it to the adjacency matrix
            print(line)
            parts = line.strip().split()
            if len(parts) != 3:
                continue  
            i, j, w = parts
            u, v = int(i) - 1, int(j) - 1
            weight = float(w)
            matrix[u][v] = weight # add it both from u -> v 
            matrix[v][u] = weight # and v -> u as this is an undirected graph
    
    return matrix


def prim_mst(adj_matrix):
    n = len(adj_matrix)
    ids  = list(range(1, n+1))
    keys = [float('inf')] * n
    parent = {i: None for i in ids}

    keys[0] = 0.0

    H = Heap() # create a heap based off of the adjacency matrix we are given
    H.heap_ini(keys, ids)

    mst = [] # initialize the mst so it can be added to later
    while H.heap:
        u = H.min_id()
        H.delete_min()

        # while the heap still has members in it get out the minimum and calculate its distance
        if parent[u] is not None:
            p = parent[u]
            w = adj_matrix[p-1][u-1]
            mst.append((p, u, w))

        # then check that this does not affect the minimum distance of any of the other connections
        # if it does then swap out its connection
        for v in ids:
            w_uv = adj_matrix[u-1][v-1]
            if w_uv < float('inf') and H.in_heap(v) and w_uv < H.key(v):
                parent[v] = u
                H.decrease_key(v, w_uv)

    return mst


mat = get_input_adjacency_matrix("graph") # create the adjacency matrix
mst_edges = prim_mst(mat) # create the mst from the adjacency matrix
print("Edges of MST in order:") 
for u, v, w in mst_edges: # output all the edges of the minimum spanning tree
    print(f"{u} -- {v}  (weight {w})")