import collections

class Solution:
    def powerOfTwo(self, n):
        char = collections.Counter(str(n))
        return any(char == collections.Counter(str(1 << i)) for i in range(30))


obj = Solution()
ans = obj.powerOfTwo(46)
print(ans)