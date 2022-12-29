import heapq

class Solution:
    def minStoneSum(self, piles, k):
        heap = [-num for num in piles]
        heapq.heapify(heap)

        for _ in range(k):
            curr = - (heapq.heappop(heap))
            remove = curr // 2
            heapq.heappush(heap, -(curr - remove))
        
        return -sum(heap)
     

obj = Solution()
piles, k = [4,3,6,7], 3
ans = obj.minStoneSum(piles, k)
print(ans)
        