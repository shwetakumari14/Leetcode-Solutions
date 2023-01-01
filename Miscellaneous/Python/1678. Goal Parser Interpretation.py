class Solution:
    def interpret(self, command):
        result = ""

        for i in range(len(command)):
            if command[i] == "G":
                result += "G"
            elif command[i] == "(" and command[i+1] == ")":
                result += "o"
                i += 1
            elif command[i] == "(" and command[i+1] == "a":
                result += "al"
                i += 2
        
        return result

     

obj = Solution()
command = "G()(al)"
ans = obj.interpret(command)
print(ans)
        