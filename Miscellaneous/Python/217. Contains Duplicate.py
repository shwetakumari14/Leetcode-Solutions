class Solution:
    def containsDuplicate(self, arr):
        dict = {}
        for num in arr:
            if num not in dict.keys():
                dict[num] = 1
            else:
                return True
        return False

obj = Solution()
arr = [1, 2, 3, 1]
ans = obj.containsDuplicate(arr)
print(ans)