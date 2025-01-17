from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank, current_tank = 0, 0
        starting_station = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                starting_station = i + 1
                current_tank = 0

        return starting_station if total_tank >= 0 else -1
