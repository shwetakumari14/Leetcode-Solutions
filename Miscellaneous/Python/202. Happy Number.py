class Solution:
   def happyNumber(self, n):
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True

obj = Solution()
n = 19
ans = obj.happyNumber(n)
print(ans)