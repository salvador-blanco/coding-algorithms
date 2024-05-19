def main():
    nums = [3,3]
    target = 6

    print(two_sum(nums, target))

def two_sum(nums, target):
    complement_has = {}
    for i, num in enumerate(nums):
        if num in complement_has:
            return sorted([i, complement_has[num]])
        else:
            complement = target-num
            complement_has[complement] = i


if __name__ == "__main__":
    main()