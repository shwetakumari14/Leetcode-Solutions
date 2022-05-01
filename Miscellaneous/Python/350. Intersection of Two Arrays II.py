class Solution:
   def intersect(self, nums1, nums2):
        res = []
        count = {}

        for num in nums1:
            count[num] = count.get(num, 0) + 1

        for num in nums2:
            if num in count and count[num] > 0:
                res.append(num)
                count[num] -= 1

        return res

obj = Solution()
nums1, nums2 = [1, 2, 2, 1], [2, 2]
ans = obj.intersect(nums1, nums2)
print(ans)