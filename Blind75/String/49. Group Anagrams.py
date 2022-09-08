class Solution:
    def groupAnagrams(sefl, str):
        dict, ans = {}, []

        for word in str:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in dict:
                dict[sortedWord] = [word]
            else:
                dict[sortedWord].append(word)
        
        for values in dict.values():
            ans.append(values)

        return ans

obj = Solution()
str = ["eat","tea","tan","ate","nat","bat"]
ans = obj.groupAnagrams(str)
print(ans)