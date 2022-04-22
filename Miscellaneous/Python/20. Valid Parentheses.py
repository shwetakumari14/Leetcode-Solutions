class Solution:
    def isValid(self, str):
        stack = []

        for i in range(len(str)):
            if str[i] == "(" or str[i] == "[" or str[i] == "{":
                stack.append(str[i])
                continue
            else:
                temp = stack.pop()
                if str[i] == ")" and (temp != "("):
                    return False
                elif str[i] == "]" and (temp!= "["):
                    return False
                elif str[i] == "}" and (temp != "{"):
                    return False
        
        if len(stack) == 0:
            return True
        return False

    def isValid2(self, str):
        stack = []
        dict = {")":"(", "}":"{","]":"["}

        for char in str:
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
ans = obj.isValid2("(([]{}))")
print(ans)
                    