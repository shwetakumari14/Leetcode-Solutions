import heapq

class Solution:
    def getOrder(self, tasks):
        result, heap, i = [], [], 0

        tasks = sorted([t[0], t[1], i] for i, t in enumerate(tasks))
        currTime = tasks[0][0]

        while len(result) < len(tasks):
            while i < len(tasks) and (tasks[i][0] <= currTime):
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            
            if heap:
                timeDiff, originalIndex = heapq.heappop(heap)
                currTime += timeDiff
                result.append(originalIndex)
            elif i < len(tasks):
                currTime = tasks[i][0]
        

        return result
     

obj = Solution()
tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
ans = obj.getOrder(tasks)
print(ans)
        