import collections 

class Solution:
    def validPath(self, n, edges, source, destination):
        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        seen = [False]*n
        seen[source] = True
        queue = collections.deque([source])

        while queue:
            cur_node = queue.popleft()
            if cur_node == destination:
                return True

            for next_node in graph[cur_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)
        
        return False
       

obj = Solution()
n, edges, source, destination = 6, [[0,1],[1,2],[2,0]], 0, 2
ans = obj.validPath(n, edges, source, destination)
print(ans)