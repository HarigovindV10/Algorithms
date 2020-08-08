import math


class DijkstraShortestPathAlgorithm:
    """
        Dijkstra's shortest path algorithm

        Implementation of Dijkstra's shortest path algorithm to find the shortest distance

        Attributes:
            graph (list(list)) : adjacency matrix of the graph
    """
    graph = [[]]

    def __init__(self, graph):
        self.graph = graph

    def get_all_nodes(self, source, dist):
        all_nodes = {}
        for vertex in self.graph:
            vertex_index = self.graph.index(vertex)
            if vertex_index != source:
                dist.append(math.inf)
            all_nodes[str(vertex_index)] = vertex_index
        return all_nodes

    def compute_minimum_distance(self, source):
        visited = set()
        dist = []
        dist.append(0)

        all_nodes = self.get_all_nodes(source, dist)

        while len(all_nodes) > 0:

            min_list = []
            for index, distances in enumerate(dist):
                if index in visited:
                    continue
                min_list.append(distances)

            min_value = min(min_list)
            shortest_dist_index = 0

            for indexes, distances in enumerate(dist):
                if distances == min_value and indexes not in visited:
                    shortest_dist_index = indexes

            vertex = self.graph[shortest_dist_index]
            all_nodes.pop(str(shortest_dist_index))
            visited.add(shortest_dist_index)

            for index, _ in enumerate(vertex):
                if str(index) not in all_nodes:
                    continue
                computed_dist = dist[shortest_dist_index] + self.graph[shortest_dist_index][index]
                if dist[shortest_dist_index] < computed_dist < dist[index]:
                    dist[index] = computed_dist

        return dist


def main():

    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
             [4, 0, 8, 0, 0, 0, 0, 11, 0],
             [0, 8, 0, 7, 0, 4, 0, 0, 2],
             [0, 0, 7, 0, 9, 14, 0, 0, 0],
             [0, 0, 0, 9, 0, 10, 0, 0, 0],
             [0, 0, 4, 14, 10, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 1, 6],
             [8, 11, 0, 0, 0, 0, 1, 0, 7],
             [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    obj = DijkstraShortestPathAlgorithm(graph)

    dist = obj.compute_minimum_distance(0)

    print(dist)


if __name__ == "__main__":
    main()
