import sys
sys.setrecursionlimit(500)
import pdb

def main():
    height = [99, 84, 7, 10, 19, 76, 12, 5, 25, 30, 23, 50, 44, 87, 95, 40, 60, 30, 1, 58]
    print(f"Result: {calc_max_area_bf(height)}, expected result: 1102")

    height = [99, 84, 7, 10, 19, 76, 12, 5, 25, 30, 23, 50, 44, 87, 95, 40, 60, 30, 1, 58]
    print(f"Result: {calc_max_area(height)}, expected result: 1102")

def calc_max_area(height):

    i, j = 0, len(height)-1
    min_heigh = min (height[i],height[j])
    max_area = min_heigh*(j-i)
                
    while(j-i>1):

        if height[i]<height[j]:   
            i+=1
        else:
            j-=1
            
        if height[i]>min_heigh or height[j]>min_heigh:
            min_heigh = min(height[i], height[j])
            max_area = max(max_area,min_heigh*(j-i))

    return max_area


     



def calc_max_area_bf(height, max_area = None):

    if max_area == None:
        max_area = 0

    curr_area = (len(height)-1)*min(height[0],height[-1]) 
    if len(height) == 2:
        return max(curr_area, max_area)
      
    return max(calc_max_area_bf(height[1:], max_area), calc_max_area_bf(height[:-1], max_area), curr_area)

if __name__ == "__main__":
    main()