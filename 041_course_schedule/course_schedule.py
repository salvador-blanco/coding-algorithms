#https://leetcode.com/problems/course-schedule/description/

from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list, indigree_list = self.generate_graph(numCourses, prerequisites)

        zero_indigree_que = deque([ node_indx for node_indx in range(numCourses) if indigree_list[node_indx] == 0])

        while zero_indigree_que:
            node_indx = zero_indigree_que.popleft()
            for dependent_course in adjacency_list[node_indx]:
                indigree_list[dependent_course] -= 1
                if indigree_list[dependent_course] == 0:
                    zero_indigree_que.append(dependent_course)
            numCourses -= 1

        return not numCourses

    def generate_graph(self, numCourses, prerequisites):
        adjacency_list =  [[] for _ in range(numCourses)]
        indigree_list =  [0 for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            adjacency_list[prerequisite].append(course)
            indigree_list[course] += 1
        return adjacency_list, indigree_list

def main():
    tester = Solution()

    numCourses = 7
    prerequisites = [[6,5],[6,2],[5,4],[4,3],[2,1],[1,0]]
    print(tester.canFinish(numCourses, prerequisites)) # Espected result = True

    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(tester.canFinish(numCourses, prerequisites)) # Espected result = False

if __name__ == '__main__':
    main()