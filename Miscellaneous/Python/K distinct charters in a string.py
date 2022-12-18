class Solution:
    def longestKSubString(self, s,  k):
        window = set()

        end, begin, low, high = 0, 0, 0, 0

        freq = [0]*128

        while high < len(s):

            window.add(s[high])
            freq[ord(s[high])] += 1

            while len(window) > k:
                freq[ord(s[low])] -= 1
                if freq[ord(s[low])] == 0:
                    window.remove(s[low])
                low += 1
            
            if end - begin < high - low:
                end = high
                begin = low
            high += 1
        
        return s[begin: end+1]

     

obj = Solution()
s, k = "abcbdbdbbdcdabd", 2
ans = obj.longestKSubString(s,  k)
print(ans)
        