import random
# n = 5: Number of items.
# W = 6: Maximum capacity of the knapsack.
# Items:
# Item 0: Value = 5, Weight = 3
# Item 1: Value = 5, Weight = 2
# Item 2: Value = 4, Weight = 1
# Item 3: Value = 2, Weight = 1
# Item 4: Value = 3, Weight = 2
# Expected profit = 4, 5, 5
# Expected weight = 1, 2, 3
#treasure = {0:(5,3), 1:(5,2), 2:(4,1), 3:(2,1), 4:(3,2)} # (Value, Weight)


# n = 2: Number of items.
# W = 6: Maximum capacity of the knapsack.
# Items:
# Item 0: Value = 2, Weight = 5
# Item 1: Value = 3, Weight = 5

# Expected profit = 3
# Expected weight = 5
#treasure = {0:(2,5), 1:(3,5)} # (Value, Weight)

def main():
    treasure = {i: (random.randint(1, 5), random.randint(1, 3)) for i in range(35)}
    knapsack_capasity = 10
    total_loot = loot(treasure, knapsack_capasity) # line 15
    print(total_loot)

def loot(treasure, knapsack_capasity, total_loot = None):

    if total_loot == None:
        total_loot = []

    if not treasure:
        return total_loot
    
    temporal_treasure = treasure.copy()
    key, (value, weight) = temporal_treasure.popitem()

    #include the item
    loot_excluding = loot(temporal_treasure, knapsack_capasity)
    
    #don't include the item
    if knapsack_capasity >= weight:
        loot_including = loot(temporal_treasure, knapsack_capasity-weight, total_loot + [value])
    else:
        loot_including = loot_excluding
    return max(loot_excluding, loot_including, key=sum)

if __name__ == "__main__":
    main() # line 28
