import random

def quick_sort(input_array, segment_start, segment_end):

    array_len = len(input_array[segment_start:segment_end])

    if array_len <= 1:
        return input_array[segment_start:segment_end]
    
    pivot = random.randint(segment_start, segment_end-1)
    input_array[segment_end-1], input_array[pivot] = input_array[pivot], input_array[segment_end-1]
    pivot = segment_end-1


    partition_index = segment_start

    for j in range(segment_start,segment_end-1):
        if input_array[j] < input_array[pivot]:
            input_array[j], input_array[partition_index] = input_array[partition_index], input_array[j]
            partition_index+=1
    input_array[pivot], input_array[partition_index] = input_array[partition_index], input_array[pivot]
    pivot = partition_index

    quick_sort(input_array, segment_start, pivot)
    quick_sort(input_array, pivot+1, segment_end)
    return input_array

def main():
    test_array = [50, 16, 87, 51, 79, 23, 61, 77, 5, 48, 40, 11, 42, 63, 7, 1, 55, 99, 64]
    
    print(f"Test array: {test_array}")
    sorted_array = quick_sort(test_array, 0, len(test_array))
    print(f"Sorted array: {sorted_array}")

if __name__ == "__main__":
    main()