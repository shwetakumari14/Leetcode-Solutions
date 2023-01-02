class Solution:
    def reverseWords(self, s):

        def reverseComplete(low, high):
            while(low < high):
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1
        
        reverseComplete(0, len(s)-1)
        left = 0

        for idx, char in enumerate(s):
            if char == " ":
                reverseComplete(left, idx-1)
                left = idx + 1
        reverseComplete(left, len(s)-1)

        return s

     

obj = Solution()
s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
ans = obj.reverseWords(s)
print(ans)
        