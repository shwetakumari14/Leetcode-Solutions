class Solution:
    def canTransform(self, start, end):

        if len(start) != len(end):
            return False

        if start.replace("X", "") != end.replace("X", ""):
            return False
        
        n = len(start)

        Lstart = [i for i in range(n) if start[i] == "L"]
        Lend = [i for i in range(n) if end[i] == "L"]

        Rstart = [i for i in range(n) if start[i] == "R"]
        Rend = [i for i in range(n) if end[i] == "R"]

        for i, j in zip(Lstart, Lend):
            if i < j:
                return False
        
        for i, j in zip(Rstart, Rend):
            if i > j:
                return False

       
        return True

obj = Solution()
start, end = "RXXLRXRXL",  "XRLXXRRLX"
ans = obj.canTransform(start, end)
print(ans)
        