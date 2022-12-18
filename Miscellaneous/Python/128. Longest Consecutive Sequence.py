class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longestSeq = 0

        for num in nums:
            if num - 1 not in numSet:
                currNum = num
                currSeq = 1

                while currNum + 1 in numSet:
                    currNum += 1
                    currSeq += 1
                
                longestSeq = max(longestSeq, currSeq)
        
        return longestSeq

     

obj = Solution()
nums = [100,4,200,1,3,2]
ans = obj.longestConsecutive(nums)
print(ans)
        