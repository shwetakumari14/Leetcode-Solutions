class Solution:
    def twoSum(self, arr, target):
        dict = {}

        for i in range(len(arr)):
            if target - arr[i] in dict:
                return [dict[target - arr[i]], i]
            else:
                dict[arr[i]] = i
        return []
    
obj = Solution()
arr, target = [2,7,11,15], 9
ans = obj.twoSum(arr, target)
print(ans)