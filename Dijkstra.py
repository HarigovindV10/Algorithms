import math


class Dijkstra:

    Graph = [[]]

    def __init__(self, Graph):
        self.Graph = Graph

    def ComputeMinimumDistance(self, source):
        S = set()
        visited = [False for _ in range(len(self.Graph))]
        Q = {}
        dist = []
        dist.append(0)

        for vertex in self.Graph:

            v = self.Graph.index(vertex)
            if v != source:
                dist.append(math.inf)
            Q[str(v)] = v

        while(len(Q) > 0):

            minList = []
            for x in range(0, len(dist)):
                if(x in S):
                    continue
                minList.append(dist[x])

            minValue = min(minList)
            i = 0

            for y in range(0, len(dist)):
                if dist[y] == minValue and y not in S:
                    i = y

            #i = dist.index(min(minList))
            v = self.Graph[i]
            Q.pop(str(i))
            S.add(i)

            for u in range(0, len(v)):
                if str(u) not in Q:
                    continue
                alt = dist[i] + self.Graph[i][u]
                if(alt < dist[u] and alt > dist[i]):
                    dist[u] = alt

        print(Q)
        print(S)
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

    graphBrilliant = [[0, 3, 0, 0, 7, 0, 5, 0, 0],
                      [3, 0, 7, 0, 1, 0, 0, 0, 0],
                      [0, 7, 0, 1, 2, 2, 0, 0, 0],
                      [0, 0, 1, 0, 0, 3, 0, 0, 5],
                      [7, 1, 2, 0, 0, 1, 3, 3, 0],
                      [0, 0, 2, 3, 1, 0, 0, 3, 2],
                      [5, 0, 0, 0, 3, 0, 0, 2, 0],
                      [0, 0, 0, 0, 3, 3, 2, 0, 4],
                      [0, 0, 0, 5, 0, 2, 0, 4, 0]]

    obj = Dijkstra(graph)

    dist = obj.ComputeMinimumDistance(0)

    print(dist)


if __name__ == "__main__":
    main()
