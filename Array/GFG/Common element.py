class Solution:
    def commonElements(self, arr1, arr2, arr3, n1, n2, n3):
        dict1, dict2, dict3, ans = {}, {}, {}, []
        
        for num in arr1:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1

        for num in arr2:
            if num not in dict2:
                dict2[num] = 1
            else:
                dict2[num] += 1
        
        for num in arr3:
            if num not in dict3:
                dict3[num] = 1
            else:
                dict3[num] += 1
        
        for num in arr3:
            if num in dict1 and dict1[num] > 0 and num in dict2 and dict2[num] > 0 and num in dict3 and dict3[num] > 0:
                ans.append(num)
                dict3[num] -= 1
                dict3[num] -= 1
                dict3[num] -= 1

        
        return ans

obj = Solution()
arr1, arr2, arr3, n1, n2, n3 = [1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120], 6, 5, 8
ans = obj.commonElements(arr1, arr2, arr3, n1, n2, n3)
print(ans)