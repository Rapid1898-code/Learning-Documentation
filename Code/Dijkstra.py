from collections import deque, namedtuple

Edge = namedtuple("Edge","start,end,cost")
def create_edge(start,end,cost):
    return Edge(start,end,cost)

class Graph:
    def __init__(self, edges):
        self.edges = [create_edge(*e) for e in edges]

    def vertices(self):
        return set(
            e.start for e in self.edges
        ).union(e.end for e in self.edges)

    def get_neighbour(self,v):      # nachbar für knoten v herausholen
        neighbours = []
        for e in self.edges:        # wie teuer von akt knoten zu nachbar knoten
            if e.start == v:
                neighbours.append((e.end,e.cost))
        return neighbours

    def dijkstra(self,source,destination):
        distances = {v: float("inf") for v in self.vertices()}
        prev_v = {v: None for v in self.vertices()}
        distances[source] = 0
        vertices = list(self.vertices())[:]
        while len(vertices) > 0:        # solange knoten vorhanden ist
            v = min(vertices,key=lambda u: distances[u])        # liste aller instanzen
            vertices.remove(v)
            if distances[v] == float("inf"):        # wenn graph nicht zusammenhängend ist (aus 2 unabhängigen teilen besteht)
                break
            for neighbour,cost in self.get_neighbour(v):
                path_cost = distances[v] + cost
                if path_cost < distances[neighbour]:
                    distances[neighbour] = path_cost
                    prev_v[neighbour] = v

        path = []
        curr_v = destination
        while prev_v[curr_v] is not None:
            path.insert(0,curr_v)
            curr_v = prev_v[curr_v]
        path.insert(0,curr_v)
        return path

if __name__ == "__main__":
    graph = Graph([
        ("a", "b", 2), ("a", "c", 4), ("b", "c", 5),
        ("b", "d", 4), ("b", "e", 9), ("c", "e", 1),
        ("d", "e", 2), ("c", "g", 2), ("c", "h", 7),
        ("g", "h", 3), ("g", "f", 1), ("h", "j", 5),
        ("g", "j", 8), ("f", "i", 2), ("i", "j", 6),
        ("g", "i", 6)
    ])

    print(graph.dijkstra("a","j"))