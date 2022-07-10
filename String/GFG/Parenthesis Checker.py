class Solution:
    def repeatedChar(self, x):
        dict, stack = {"}":"{", "]":"[", ")":"("}, []

        for char in x:
            if char in dict.values():
                stack.append(char)
                continue
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False

        
        return stack == []

obj = Solution()
str = "{([])}"
ans = obj.repeatedChar(str)
print(ans)