def merge_sort(input_array: list[int]) -> list[int]:
    if len(input_array) > 1:
        segment_a, segment_b = divide_array(input_array)    
        
        segment_a = merge_sort(segment_a)
        segment_b = merge_sort(segment_b)
        
        sorted_array = merge_arrays(segment_a, segment_b)

        return sorted_array
    else:
        return input_array


def merge_arrays(segment_a, segment_b):
    sorted_array = []
    while segment_a and segment_b:

        if segment_a[0] <= segment_b[0]:
            sorted_array.append(segment_a.pop(0))

        elif segment_a[0] > segment_b[0]:
            sorted_array.append(segment_b.pop(0))

    return sorted_array + segment_a + segment_b

def divide_array(input_array : list[int]) -> list[int]:
    midpoint = len(input_array)//2
    segment_a = input_array[:midpoint]
    segment_b = input_array[midpoint:]
    return segment_a, segment_b

def main():
    test_array = [50, 16, 87, 51, 79, 23, 61, 77, 5, 48, 40, 11, 42, 63, 7, 1, 1, 55, 99, 64]
    sorted_array = merge_sort(test_array)
    print(f"Test array: {test_array}")
    print(f"Test array: {sorted_array}")

if __name__ == "__main__":
    main()