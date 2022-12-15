from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):

        n = len(nums)

        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        deq, maxIdx = deque(), 0

        def clearDequeue(i):
            if deq and deq[0] == i-k:
                deq.popleft()
            
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
        
        for i in range(k):
            clearDequeue(i)
            deq.append(i)

            if nums[i] > nums[maxIdx]:
                maxIdx = i
        output = [nums[maxIdx]]

        for i in range(k, n):
            clearDequeue(i)
            deq.append(i)
            output.append(nums[deq[0]])
        
        return output


obj = Solution()
nums, k = [1,3,-1,-3,5,3,6,7], 3
ans = obj.maxSlidingWindow(nums, k)
print(ans)
        