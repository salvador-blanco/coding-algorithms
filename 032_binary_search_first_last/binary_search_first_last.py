import math
class Solution(object):
    
    def searchRange(self, nums, target):

        if not nums:
            return [-1,-1]
        
        if len(nums) == 1:
            return [0,0] if target == nums[0] else [-1,-1]
            
        first_position = self.get_segment_start(nums, target)
        if first_position == None:
            return [-1,-1]

        last_position = self.get_segment_end(nums, target, first_position)
        return [first_position, last_position]
            
            
    def get_segment_start(self, nums, target, segment_start = None, segment_end = None, first_position = None):

        if segment_start == None and segment_end == None:
            segment_start,  segment_end = 0, len(nums) - 1
            first_position = None

        pivot = int(( segment_end + segment_start)/2)

        if nums[pivot] > target and segment_end != segment_start:
            if pivot-1 <0:
                return None
            return self.get_segment_start(nums, target, segment_start, pivot-1, first_position)
    
        elif nums[pivot] < target and segment_end != segment_start:
            return self.get_segment_start(nums, target, pivot+1, segment_end, first_position)

        elif nums[pivot] == target:
            if pivot-1 <0 or nums[pivot-1] != target:
                return pivot
            return self.get_segment_start(nums, target, segment_start, pivot-1, first_position)        
        
        return None

    def get_segment_end(self, nums, target, segment_start = None, segment_end = None, last_position = None):

        if segment_end == None:
            segment_end = len(nums) - 1

        pivot = math.ceil(( segment_end + segment_start)/2)

        if nums[pivot] > target and segment_end != segment_start: 
            return self.get_segment_end(nums, target, segment_start, pivot-1)
    
        elif nums[pivot] < target and segment_end != segment_start:
            return self.get_segment_end(nums, target, pivot+1, segment_end)

        elif nums[pivot] == target:
            if pivot+1 > len(nums)-1 or nums[pivot+1] != target:
                return pivot
            return self.get_segment_end(nums, target, pivot, segment_end)

        return None
        
def main():
    tester = Solution()
    print(tester.searchRange([5,7,8,8,8,10],8))
    print(tester.searchRange([5,7,7,8,8,10],6))
    
    print(tester.searchRange([],0))
    print(tester.searchRange([2,2],2))

if __name__ == "__main__":
    main()