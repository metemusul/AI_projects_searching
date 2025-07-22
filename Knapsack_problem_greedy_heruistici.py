items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50
items.sort(key=lambda x: x[0]/x[1], reverse=True)

total_value = 0
for value, weight in items:
    if capacity >= weight:
        capacity -= weight
        total_value += value
