class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost = sum(gas), sum(cost)
        
        # If the total fuel is less than the total cost, it's impossible to complete the circuit
        if total_gas < total_cost:
            return -1
        
        start, tank = 0, 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            
            # If tank goes negative, reset start to next station and tank to 0
            if tank < 0:
                start = i + 1
                tank = 0
                
        return start
        

        
