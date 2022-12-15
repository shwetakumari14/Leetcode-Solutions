class Solution:
    def leastInterval(self, tasks, n):
        frequency = [0]*26

        for task in tasks:
            frequency[ord(task) - ord('A')] += 1
        
        frequency.sort()
        
        max_freq = frequency.pop()
        ideal_time = (max_freq - 1)*n

        while frequency and ideal_time > 0:
            ideal_time -= min(max_freq - 1, frequency.pop())
        
        ideal_time = max(0, ideal_time)

        return len(tasks) + ideal_time

obj = Solution()
tasks, n = ["A","A","A","A","A","A","B","C","D","E","F","G"], 2
ans = obj.leastInterval(tasks, n)
print(ans)
        