# https://leetcode.com/problems/min-cost-climbing-stairs/description/
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int], position = -1, memoization = None) -> int:

        if memoization == None:
            memoization = {}
            cost.append(0)

        if position > len(cost)-4:
            return cost[position]
        
        if position in memoization:
            return memoization[position]
        
        memoization[position] = cost[position] + \
            min(self.minCostClimbingStairs(cost, position+1, memoization),
                self.minCostClimbingStairs(cost, position+2, memoization))
        return memoization[position]
        
def main():
    tester = Solution()

    # Example 1:
    cost = [10,15,20] #Expected Output = 15
    print(tester.minCostClimbingStairs(cost))
    
    # Example 2:
    cost = [1,100,1,1,1,100,1,1,100,1] #Expected Output = 6
    print(tester.minCostClimbingStairs(cost))  


# class Solution:
#     def minCostClimbingStairsBF(self, cost: List[int], position = -1, curr_cost = 0) -> int:

#         if position > len(cost)-3:
#             return curr_cost

#         dist_one_step = self.minCostClimbingStairsBF(cost, position+1, curr_cost+cost[position+1])
#         dist_two_step = self.minCostClimbingStairsBF(cost, position+2, curr_cost+cost[position+2])
#         return min(dist_one_step, dist_two_step)

if __name__ == "__main__":
    main()


