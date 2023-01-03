import math

class Solution:
    def bulbSwitch(self, x):

        return int(math.sqrt(x))

obj = Solution()
x = 10
ans = obj.bulbSwitch(x)
print(ans)