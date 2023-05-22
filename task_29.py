class Solution:
    def isBipartite(self, graph) -> bool:
        visited = [-1] * len(graph)

        def search(vert, graph) -> bool:
            for to in graph[vert]:
                if visited[to] == visited[vert]:
                    return False
                if visited[to] == -1:
                    visited[to] = not visited[vert]
                    if not search(to, graph):
                        return False
            return True

        for vert in range(len(graph)):
            if visited[vert] == -1:
                visited[vert] = 0
                if not search(vert, graph):
                    return False

        return True

# https://leetcode.com/problems/is-graph-bipartite/submissions/954878077/
