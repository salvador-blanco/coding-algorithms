from typing import List
#https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

class Solution:
    def numOfMinutes(self, n: int, headID: int, managers: List[int], informTime: List[int]) -> int:
        
        adjacency_list = self.generate_graph( n, managers, informTime)
        max_time = self.dfs_calculate_time(adjacency_list, headID)

        return max_time

    def generate_graph(self, n, managers, informTime):
        adjacency_list =  [[] for _ in range(n)]
        for employee, manager in enumerate(managers):
            if manager != -1:
                adjacency_list[manager].append((employee, informTime[manager]))        
        return adjacency_list
    
    def dfs_calculate_time(self, adjacency_list, root):
        
        if not adjacency_list[root]:
            return 0
        
        max_time = 0
        for next_node, delay in adjacency_list[root]:
            path_time = delay + self.dfs_calculate_time(adjacency_list, next_node)
            max_time = max(max_time, path_time)
        return max_time

def main():
    tester = Solution()

    n = 1
    headID = 0
    manager = [-1]
    informTime = [0]
    print(tester.numOfMinutes(n,headID, manager, informTime)) #Expected output = 0

if __name__ == '__main__':
    main()