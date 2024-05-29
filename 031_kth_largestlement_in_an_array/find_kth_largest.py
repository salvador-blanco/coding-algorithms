import random

class Solution(object):
    def findKthLargest(self, input_array,  k = 0, segment_start = None, segment_end = None):
        if segment_start == None:
            segment_start, segment_end = 0, len(input_array)-1
            k = k-1
    
        pivot =  random.randint(segment_start, segment_end)
        pivot_value = input_array[pivot]
        
        i, m = segment_start, segment_start
        l = segment_end
        
        input_array[pivot], input_array[segment_end] = input_array[segment_end], input_array[pivot]

        while m <= l:
            if input_array[m] > pivot_value: 
                input_array[i], input_array[m] = input_array[m], input_array[i]
                i+=1
                m+=1
            elif input_array[m] == pivot_value:
                m+=1

            else:
                input_array[m], input_array[l] = input_array[l], input_array[m]
                l -= 1

        if i<=k<m:
            return pivot_value
        elif i  < k:
            return self.findKthLargest(input_array, k, m, segment_end)
        elif i  > k:
            return self.findKthLargest(input_array, k, segment_start, i-1)
        

def main():
    tester = Solution()
    print(tester.findKthLargest([3,2,3,1,2,4,5,5,6],4))
    print(tester.findKthLargest([1, 2, 3, 4, -5, 1, 1, 1, 1, 1, 1, 1, 1, -1, -2, -3, -4], 1))


if __name__ == "__main__":
    main()