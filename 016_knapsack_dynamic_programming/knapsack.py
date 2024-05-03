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
    treasure = {0:(5,3), 1:(5,2), 2:(4,1), 3:(2,1), 4:(3,2)} # (Value, Weight)
    knapsack_capasity = 6
    total_loot = loot(treasure, knapsack_capasity) # line 15
    print(total_loot)

def loot(treasure, knapsack_capasity, total_loot = []):

    
    temporal_treasure = treasure.copy()
    key, (value, weight) = temporal_treasure.popitem()

    if len(temporal_treasure) < 1:
        if knapsack_capasity >= weight:
            return max(total_loot, total_loot + [value])
        else:
            return [0]

    #include the item
    loot_no_item = loot(temporal_treasure, knapsack_capasity)
    #don't include the item
    if knapsack_capasity >= weight:
        loot_with_item = loot(temporal_treasure, knapsack_capasity-weight, total_loot + [value])
    else:
        loot_with_item = loot_no_item
    return max(loot_no_item, loot_with_item, key=sum)#

if __name__ == "__main__":
    main() # line 28