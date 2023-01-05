from collections import Counter
import math

class Solution:
    def minimumRounds(self, tasks):
        tasksCount, result = Counter(tasks), 0

        for _, val in tasksCount.items():
            if val < 2:
                return -1
            result += math.ceil(val/3)
        
        return result


obj = Solution()
tasks = [2,2,3,3,2,4,4,4,4,4]
ans = obj.minimumRounds(tasks)
print(ans)