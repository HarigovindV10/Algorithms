import math


class dijkstra:

    graph = [[]]

    def __init__(self, graph):
        self.graph = graph

    def compute_minimum_distance(self, source):
        visited = set()
        all_nodes = {}
        dist = []
        dist.append(0)

        for vertex in self.graph:

            v = self.graph.index(vertex)
            if v != source:
                dist.append(math.inf)
            all_nodes[str(v)] = v

        while len(all_nodes) > 0:

            min_list = []
            for index, distances in enumerate(dist):
                if index in visited:
                    continue
                min_list.append(distances)

            min_value = min(min_list)
            shortest_distance_index = 0

            for indexes, distances in enumerate(dist):
                if distances == min_value and indexes not in visited:
                    shortest_distance_index = indexes

            vertex = self.graph[shortest_distance_index]
            all_nodes.pop(str(shortest_distance_index))
            visited.add(shortest_distance_index)

            for index, node in enumerate(vertex):
                if str(index) not in all_nodes:
                    continue
                computed_distance = dist[shortest_distance_index] + self.graph[shortest_distance_index][index]
                if(dist[shortest_distance_index] < computed_distance < dist[index]):
                    dist[index] = computed_distance

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

    obj = dijkstra(graph)

    dist = obj.compute_minimum_distance(0)

    print(dist)


if __name__ == "__main__":
    main()
