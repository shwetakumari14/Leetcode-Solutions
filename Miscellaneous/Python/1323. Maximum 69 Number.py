class Solution:
    def maximum69Number(self, num):
        result = [int(x) for x in str(num)]

        for i in range(len(result)):
            if result[i] == 6:
                result[i] = 9
                break
        
        return int("".join(map(str, result)))


obj = Solution()
num = 9669
ans = obj.maximum69Number(9669)
print(ans)