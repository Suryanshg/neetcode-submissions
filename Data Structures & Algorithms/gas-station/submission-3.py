class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Why we do not need to go over the list to complete full circle. 
        Two reasons:
        1. We already checked that gas >= cost so atleast one solution exists
        2. The carry over of total from previous stations ensure that it will last for completing full circle.
        """

        if sum(gas) < sum(cost):
            return -1

        start = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i] # Calculate diff at every station
            if total < 0: # If diff goes negative, reset total and move start to the next pos
                total = 0
                start = i + 1
        
        return start

