class Solution:
    def getKthNum(self, lo, hi, k):
        result = []

        for i in range(lo, hi + 1):
            count, temp = 0, i

            while i != 1:
                if i % 2 == 0:
                    i = i//2
                else:
                    i = 3*i + 1
                count += 1
            result.append([temp, count])
        
        result.sort(key = lambda x:x[1])
        ans = result[k-1]

        return ans[0]


obj = Solution()
lo, hi, k = 12, 15, 2
ans = obj.getKthNum(lo, hi, k)
print(ans)
        