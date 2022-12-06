import heapq

class Solution:
    def minNoOfChairs(self, start, end):
        intervals, result = [], []

        for i in range(len(start)):
            intervals.append((start[i], end[i]))
        
        intervals.sort(key = lambda x : x[0])

        heapq.heappush(result, intervals[0][1])

        for i in intervals[1:]:
            if result[0] <= i[0]:
                heapq.heappop(result)
            
            heapq.heappush(result, i[1])

        return len(result)
                    

obj = Solution()
start, end = [1, 2, 6, 5, 3], [5, 5, 7, 6, 8]
ans = obj.minNoOfChairs(start, end)
print(ans)