class Solution:
    def powerOfFou1(self, n):
        if n == 1:
            return True
        
        if n < 4 or n % 4:
            return False

        val = 1
        
        while val < n:
            val *= 4
            if val == n:
                return True
        
        return False
    
    def powerOfFour2(self, n):
        if n < 1:
            return False
        
        while n % 4 == 0:
            n /= 4
        
        return n == 1
    
    def powerOfFour3(self, n):
        val = 1

        while val < n:
            val <<= 2
        
        return val == n

obj = Solution()
ans = obj.powerOfFour3(16)
print(ans)