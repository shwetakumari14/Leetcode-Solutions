class Solution:
    def rotateString(self, s, goal):
        return len(s) == len(goal) and goal in s + s


obj = Solution()
s, goal = "abcde", "cdeab"
ans = obj.rotateString(s, goal)
print(ans)