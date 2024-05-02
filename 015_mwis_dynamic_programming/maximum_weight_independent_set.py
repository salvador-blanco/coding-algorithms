import random

def main():
    test_set = [51, 38, 56, 5, 17, 58, 10, 52, 3, 36, 23, 44, 34, 54, 47, 16, 8, 35, 29, 55, 32, 43, 1, 30, 12, 27, 0, 7, 50, 49, 39, 33, 26, 2, 28, 22, 4, 48, 21, 31, 40, 20, 46, 19, 13, 45, 57, 42, 41, 25, 24, 15, 18, 6, 9, 37, 11, 14, 59, 53]
    
    print(f"Test set: {test_set}")
    mwis = mwis_brute_force(test_set)
    print(f"Brute force result:         {mwis}")
    
    mwis = mwis_dp(test_set)
    print(f"Dynamic programming result: {mwis}")

def mwis_brute_force(input_set):
    if len(input_set) == 3:
        return max([input_set[1]], [input_set[0], input_set[2]], key=sum)
    
    if len(input_set) <= 2:
        return [max(input_set)]
    
    return max(mwis_brute_force(input_set[:-2]) + [input_set[-1]],
                mwis_brute_force(input_set[:-3])  + [input_set[-2]], key=sum)

def mwis_dp(input_set, memory = None):

    if memory == None:
        memory = {}

    if len(input_set) in memory:
        return memory[len(input_set)]
    
    result = []
    if len(input_set) == 3:
        result = max([input_set[1]], [input_set[0], input_set[2]], key=sum)
    
    elif len(input_set) <= 2:
        result = [max(input_set)]
    
    else:
        result = max(mwis_dp(input_set[:-2], memory) + [input_set[-1]],
                mwis_dp(input_set[:-3], memory)  + [input_set[-2]], key = sum)
    
    memory[len(input_set)] = result
    return result

if __name__ == "__main__":
    main()