class Solution(object):
    def twoCitySchedCost(self, costs):
        costs.sort(key=lambda x: x[0] - x[1])  
        n = len(costs) // 2
        total = 0
        for i in range(n):
            total += costs[i][0]      # first half → A
        for i in range(n, len(costs)):
            total += costs[i][1]      # second half → B
        
        return total