class Solution:
    def validIPAddress(self, queryIP):
        if "." in queryIP:
            splitted = queryIP.split(".")
            if len(splitted) != 4:
                return "Neither"
            for part in splitted:
                if len(part) == 0 or (len(part) > 1 and part[0] == "0"):
                    return "Neither"
                if not part.isnumeric() or int(part) > 255:
                    return "Neither"
            return "IPv4"
        
        if ":" in queryIP:
            splitted = queryIP.split(":")
            if len(splitted) != 8:
                return "Neither"
            symbols = "0123456789abcdefABCDEF"
            for part in splitted:
                if len(part) == 0 or len(part) > 4:
                    return "Neither"
                for ele in part:
                    if ele not in symbols:
                        return "Neither"
            
            return "IPv6"


obj = Solution()
queryIP = "172.16.254.1"
ans = obj.validIPAddress(queryIP)
print(ans)