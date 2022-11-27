class Solution:
    def decodeString(self, str):
        num, stack, i = 0, [""], 0

        while i < len(str):
            if str[i].isdigit():
                num = num*10 + int(str[i])
            elif str[i] == "[":
                stack.append(num)
                num = 0
                stack.append("")
            elif str[i] == "]":
                str1 = stack.pop()
                cnt = stack.pop()
                str2 = stack.pop()
                stack.append(str2 + str1*cnt)
            else:
                stack[-1] += str[i]
            
            i += 1
        
        return "".join(stack)


obj = Solution()
str = "3[a2[c]]"
ans = obj.decodeString(str)
print(ans)
        