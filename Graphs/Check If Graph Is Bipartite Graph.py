import queue


class Solution:
    def checkBipartite(self, vertices, adj):
        col, queue = [-1]*vertices, []

        for i in range(vertices):
            if col[i] == -1:
                queue.append([i, 0])
                col[i] = 0

                while queue:
                    p = queue.pop(0)
                    v, c = p[0], p[1]

                    for j in adj[v]:
                        if col[j] == c:
                            return False
                        
                        if col[j] == -1:
                            if c == 1:
                                col[j] = 0
                            else:
                                col[j] = 1
                            queue.append([j, col[j]])

        
        return True

obj = Solution()
vertices, adj = 4, []
adj.append([1,3])
adj.append([0,2])
adj.append([1,3])
adj.append([0,2])
ans = obj.checkBipartite(vertices, adj)

print(ans)


