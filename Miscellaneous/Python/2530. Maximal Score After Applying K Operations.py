import heapq, math

class Solution:
    def maxKelements(self, nums, k):
        heap, result = [-num for num in nums], 0
        heapq.heapify(heap)

        for _ in range(k):
            curr = -heapq.heappop(heap)
            result += curr
            remove = math.ceil(curr/3)
            heapq.heappush(heap, -remove)
        
        return result


obj = Solution()
nums, k = [1,10,3,3,3], 3
ans = obj.maxKelements(nums, k)
print(ans)