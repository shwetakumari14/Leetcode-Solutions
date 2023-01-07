class Solution:
    def canCompleteCircuit(self, gas, cost):
        tank_cost, curr_cost, start_station = 0, 0, 0

        for i in range(len(gas)):
            tank_cost += gas[i] - cost[i]
            curr_cost += gas[i] - cost[i]

            if curr_cost < 0:
                curr_cost = 0
                start_station = i + 1
        
        if tank_cost < 0 :
            return -1
        return start_station


obj = Solution()
gas, cost = [1,2,3,4,5],  [3,4,5,1,2]
ans = obj.canCompleteCircuit(gas, cost)
print(ans)