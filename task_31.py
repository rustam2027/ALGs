class Solution:
    def longestCycle(self, edges) -> int:
        reversed_graph = {}
        for i, j in enumerate(edges):
            if j != -1:
                if j in reversed_graph:
                    reversed_graph[j].append(i)
                else:
                    reversed_graph[j] = [i]

        visited = []

        def dfs(vert, graph, time, time_arr):
            visited.append(vert)
            if vert in graph:
                for next_vert in graph[vert]:
                    if next_vert in visited:
                        continue
                    else:
                        time = dfs(next_vert, graph, time, time_arr)
            time_arr.append((vert, time))
            time += 1
            return time

        time_arr = []
        time = 0
        for i in range(len(edges)):
            if i not in visited:
                time = dfs(i, reversed_graph, time, time_arr)

        time_arr.sort(key=lambda x: x[1], reverse=True)

        all_visited = []

        def new_dfs(vert, graph):
            visited.append(vert)
            next_vert = graph[vert]
            if next_vert == -1 or next_vert in visited or next_vert in all_visited:
                return None
            new_dfs(next_vert, graph)

        visited = []
        max_len = -1
        for i in time_arr:
            vert, _ = i
            if vert in all_visited:
                continue

            new_dfs(vert, edges)
            if len(visited) > max_len and len(visited) > 1:
                max_len = len(visited)
            all_visited += visited
            visited = []

        return max_len
