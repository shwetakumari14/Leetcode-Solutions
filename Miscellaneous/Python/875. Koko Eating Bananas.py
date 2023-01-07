import math

class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left)//2

            hours_spent = 0

            for pile in piles:
                hours_spent += math.ceil(pile/mid)
            
            if hours_spent <= h:
                right = mid
            else:
                left = mid + 1
        
        return right

obj = Solution()
piles, h = [30, 11, 23, 4, 20], 5
ans = obj.minEatingSpeed(piles, h)
print(ans)