class Solution:
    def findDuplicates(self, arr, n):
        dict = {}
        myset = set([])

        for i in range(n):
            if arr[i] not in dict:
                dict[arr[i]] = 1
            elif arr[i] in dict:
                dict[arr[i]] += 1
                myset.add(arr[i])

        if len(myset) == 0:
            myset.add(-1)
        
        myset = sorted(list(myset))
        return myset

obj = Solution()
arr, n = [13, 9, 25, 1, 1, 0, 22, 13, 22, 20, 3, 8, 11, 25, 10, 3, 15, 11, 19, 20, 2, 4, 25, 14, 23, 14], 26
ans = obj.findDuplicates(arr, n)
print(ans)