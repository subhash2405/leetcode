class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cash = sum(cost)
        fuel = sum(gas)

        if cash>fuel:
            return -1

        a,b = 0,0
        for i in range(len(gas)):
            a+=gas[i]-cost[i]
            if a<0:
                a = 0
                b = i+1
        return b