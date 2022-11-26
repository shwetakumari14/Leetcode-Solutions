class Solution:
    def __init__(self):
        self.msg_dict = {}

    def rateLimiter(self, timeStamp, message):
        if message not in self.msg_dict:
            self.msg_dict[message] = timeStamp
            return True
        
        if timeStamp - self.msg_dict[message] >= 10:
            self.msg_dict[message] = timeStamp
            return True
        else:
            return False

obj = Solution()
timeStamp, message = 1, "foo"
ans = obj.rateLimiter(timeStamp, message)
print(ans)
        