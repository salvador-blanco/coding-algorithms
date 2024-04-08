import random

def quick_sort(input_array, low, max):
    print()
    print(f"low: {low} max: {max}")
    print(input_array)
    print(f"input array {input_array[low:max]}")
    array_len = len(input_array[low:max])

    if array_len <= 1:
        return input_array[low:max]
    
    pivot = random.randint(low, max)
    print(f"Pivot: {input_array[pivot]}")
    input_array[max-1], input_array[pivot] = input_array[pivot], input_array[max-1]
    print(f"pivot moved {input_array[low:max]}")
    pivot = max-1
    print(f"Pivot: {input_array[pivot]}")


    i, j = 0, 0

    for j in range(low,max-1):
        if input_array[j] < input_array[pivot]:
            input_array[j], input_array[i] = input_array[i], input_array[j]
            i+=1
    input_array[pivot], input_array[i] = input_array[i], input_array[pivot]
    pivot = i

    print(f"sorted array: {input_array[low:max]}")
    print(f"next itter 1: {input_array[low:pivot]}")
    print(f"next iiter p: {input_array[pivot]}")
    print(f"next itter 2: {input_array[pivot+1:max]}")

    return quick_sort(input_array, low, pivot)  + [input_array[pivot]] + quick_sort(input_array, pivot+1, max)

def main():
    test_array = [50, 16, 87, 51, 79, 23]#, 61, 77, 5, 48, 40, 11, 42, 63, 7, 1, 55, 99, 64]
    
    print(f"Test array: {test_array}")
    sorted_array = quick_sort(test_array, 0, len(test_array))
    print(f"Sorted array: {sorted_array}")

if __name__ == "__main__":
    main()