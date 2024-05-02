# n = 5: Number of items.
# W = 6: Maximum capacity of the knapsack.
# Items:
# Item 1: Value = 5, Weight = 3
# Item 1: Value = 5, Weight = 2
# Item 2: Value = 4, Weight = 1
# Item 3: Value = 2, Weight = 1
# Item 4: Value = 3, Weight = 2
# Expected profit = 4, 5, 5
# Expected weight = 1, 2, 3

def main():
    treasure = {0:(5,3), 1:(5,2), 2:(4,1), 3:(2,1), 4:(3,2)} # (Value, Weight)
    knapsack_capasity = 6
    loot(treasure, knapsack_capasity)

def loot(treasure, knapsack_capasity, total_loot = [0]):
    if knapsack_capasity <=0 or len(treasure) == 0:
        return total_loot
    key, (value, weight) = treasure.popitem()
    return max(loot(treasure, knapsack_capasity),
               loot(treasure, knapsack_capasity-weight, total_loot.append(value)), key=sum)

if __name__ == "__main__":
    main()