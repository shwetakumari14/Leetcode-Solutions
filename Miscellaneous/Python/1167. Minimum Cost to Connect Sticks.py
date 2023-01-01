import heapq

class Solution:
    def connectSticks(self, sticks):
        result = 0
        heapq.heapify(sticks)

        while len(sticks) > 1:
            num1, num2 =  heapq.heappop(sticks), heapq.heappop(sticks)
            result += num1 +  num2
            heapq.heappush(sticks,  num1 +  num2)
        

        return result

     

obj = Solution()
sticks = [1,8,3,5]
ans = obj.connectSticks(sticks)
print(ans)
        