class Solution:
    def minJumps(self, arr, n):
        if len(arr) == 1:
            return 0
        if arr[0] == 0:
            return -1

        jumps, maxLen, steps = 1, arr[0], arr[0]

        for i in range(1, n):
            if i == n-1:
                return jumps
            
            maxLen = max(maxLen, arr[i]+i)
            steps -= 1
            if steps == 0:
                jumps += 1
                if i > maxLen:
                    return -1
                steps = maxLen - i

        return jumps

obj = Solution()
arr, n = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1], 10
ans = obj.minJumps(arr, n)
print(ans)