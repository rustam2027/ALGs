class Solution:
    def longestCycle(self, edges) -> int:
        reversed_graph = {}
        for i, j in enumerate(edges):
            if j != -1:
                if j in reversed_graph:
                    reversed_graph[j].append(i)
                else:
                    reversed_graph[j] = [i]

        visited = [False] * len(edges)

        def dfs(vert, graph, time, time_arr):
            visited[vert] = True
            if vert in graph:
                for next_vert in graph[vert]:
                    if visited[next_vert]:
                        continue
                    time = dfs(next_vert, graph, time, time_arr)
            time_arr.append((vert, time))
            time += 1
            return time

        time_arr = []
        time = 0
        for i in range(len(edges)):
            if not visited[i]:
                time = dfs(i, reversed_graph, time, time_arr)

        time_arr.sort(key=lambda x: x[1], reverse=True)

        all_visited = [0] * len(edges)

        def new_dfs(vert, graph, color):
            all_visited[vert] = color
            colors[color] += 1
            next_vert = graph[vert]
            if next_vert == -1 or all_visited[next_vert]:
                return None
            new_dfs(next_vert, graph, color)

        colors = [0]
        color = 1
        for i in time_arr:
            vert, _ = i
            if all_visited[vert]:
                continue
            colors.append(0)
            new_dfs(vert, edges, color)
            color += 1
        ans = max(colors)
        if ans == 1:
            return -1
        return ans


A = Solution()
print(A.longestCycle([3,3,4,2,3]))

# https://leetcode.com/problems/longest-cycle-in-a-graph/submissions/955225751/
