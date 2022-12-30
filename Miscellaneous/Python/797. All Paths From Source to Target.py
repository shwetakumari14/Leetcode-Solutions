class Solution:
    def allPathsSourceTarget(self, graph):
        target = len(graph)-1
        result = []

        def backtrack(currNode, path):
            if currNode == target:
                result.append(list(path))
                return 
            
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()


        path = [0]
        backtrack(0, path)

        return result

     

obj = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]
ans = obj.allPathsSourceTarget(graph)
print(ans)
        