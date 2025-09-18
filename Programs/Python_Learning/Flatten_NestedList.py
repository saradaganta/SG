def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat

# Input list
nested_list = [4, 7, [6, 3, 2, [7, 9, 2], 4], 1, 3]

# Flattened result
flattened = flatten_list(nested_list)
print(flattened)
