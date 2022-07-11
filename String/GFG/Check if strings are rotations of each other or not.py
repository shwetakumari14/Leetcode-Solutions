class Solution:
    def checkIfStringIsRotationOfEachOther(self, s1, s2):

        for i in range(len(s1)):
          temp = s1[i:]+s1[:i]
          if temp == s2:
              return 1

        return 0

obj = Solution()
s1, s2 = "geeksforgeeks", "forgeeksgeeks"
ans = obj.checkIfStringIsRotationOfEachOther(s1, s2)
print(ans)