class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks):
        remainingCapcity = [cap - rock for cap, rock in zip(capacity, rocks)]
        remainingCapcity.sort()
        fullBags = 0

        for cap in remainingCapcity:
            if additionalRocks >= cap:
                additionalRocks -= cap
                fullBags += 1
            else:
                break
        
        return fullBags
     

obj = Solution()
capacity, rocks, additionalRocks = [2,3,4,5], [1,2,4,4], 2
ans = obj.maximumBags(capacity, rocks, additionalRocks)
print(ans)
        