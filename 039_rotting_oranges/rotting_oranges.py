from typing import List
from collections import deque

class Solution:
    def __init__(self) -> None:
        self._directions = [(0,1),
                            (1,0),
                            (0,-1),
                            (-1,0)]

    def orangesRotting(self, grid: List[List[int]]) -> int:
        len_y = len(grid)
        len_x = len(grid[0])
        
        inital_queue, good_oranges = self._count_oranges(grid, len_y, len_x)
        time, all_rotted = self._dfs(grid, inital_queue, good_oranges, len_y, len_x)

        return time if all_rotted else -1


    def _dfs(self, grid, next_to_rot, good_oranges, len_y, len_x):
        time = 0

        while next_to_rot:
            for _ in range(len(next_to_rot)):
                y, x = next_to_rot.popleft()
                grid[y][x] = 0
                for y_dir,x_dir in self._directions:
                    y_new, x_new = y + y_dir, x + x_dir
                    if 0<=y_new<len_y and 0<=x_new<len_x and grid[y_new][x_new] == 1:
                        grid[y_new][x_new] = 0
                        good_oranges -= 1
                        next_to_rot.append((y_new, x_new))
            if next_to_rot:
                time +=1
        return time, not good_oranges

    def _count_oranges(self, grid: List[List[int]], len_y: int, len_x: int):
        rotted_oranges = deque()
        good_oranges = 0
        for y in range(len_y):
            for x in range(len_x):
                if grid[y][x] == 2:
                    rotted_oranges.append((y,x))
                elif grid[y][x] == 1:
                    good_oranges += 1
        return rotted_oranges, good_oranges

def main():
    tester = Solution()
    grid_1 = get_grid_1()
    grid_2 = get_grid_2()
    grid_3 = get_grid_3()
    
    print(tester.orangesRotting(grid_1))
    print(tester.orangesRotting(grid_2))
    print(tester.orangesRotting(grid_3))

def get_grid_1(): # Expected output 4
    return [[2,1,1],
            [1,1,0],
            [0,1,1]]

def get_grid_2(): # Expected output -1
    return [[2,1,1],
            [0,1,1],
            [1,0,1]]
    
def get_grid_3(): # Expected output 0
    return [[0,2]]

if __name__ == "__main__":
    main()