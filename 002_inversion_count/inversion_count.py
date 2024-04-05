def get_inversion_count(input_array: list[int]) -> list[int]:
    sorted_array = 0
    if len(input_array) > 1:
        inversion_count = 0
        segment_a, segment_b = divide_array(input_array)    
        
        segment_a, inversion_count_a = get_inversion_count(segment_a)
        segment_b, inversion_count_b = get_inversion_count(segment_b)
        
        sorted_array, inversion_count_tp = merge_arrays(segment_a, segment_b)

        inversion_count += inversion_count_a+inversion_count_b + inversion_count_tp
        return sorted_array, inversion_count
    else:
        return input_array, 0


def merge_arrays(segment_a, segment_b):
    sorted_array = []
    inversion_count = 0
    while segment_a and segment_b:

        if segment_a[0] <= segment_b[0]:
            sorted_array.append(segment_a.pop(0))

        elif segment_a[0] > segment_b[0]:
            sorted_array.append(segment_b.pop(0))
            inversion_count += len(segment_a)

    return sorted_array + segment_a + segment_b, inversion_count

def divide_array(input_array : list[int]) -> list[int]:
    midpoint = len(input_array)//2
    segment_a = input_array[:midpoint]
    segment_b = input_array[midpoint:]
    return segment_a, segment_b

def main():
    test_array = [1,5,2, 8,3,4]
    _, inversion_count = get_inversion_count(test_array)
    print(test_array)
    print(inversion_count)

    print()

    test_array = [5, 4, 3, 2, 1]
    _, inversion_count = get_inversion_count(test_array)
    print(test_array)
    print(inversion_count)

if __name__ == "__main__":
    main()