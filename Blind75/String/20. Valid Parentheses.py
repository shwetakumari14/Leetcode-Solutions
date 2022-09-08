class Solution:
    def validParentheses(sefl, str):
        dict, stack = {"}":"{", "]":"[", ")":"("}, []

        for char in str:
            if char in dict.values():
                stack.append(char)
                continue
            elif char in dict.keys():
                if stack == [] or dict[char] is not stack.pop():
                    return False
            else:
                return False

        return stack ==[]

obj = Solution()
str = "()[]{}"
ans = obj.validParentheses(str)
print(ans)