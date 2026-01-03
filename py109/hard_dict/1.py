# Problem 1: Merge nested inventory dictionaries
# ---------------------------------------------
# Write a function merge_inventories(inv1, inv2) that:
# - Takes two dictionaries inv1 and inv2.
# - Each has category names as keys (e.g. "fruits") and values that are
#   dictionaries of item: quantity pairs.
# - Return a NEW dictionary.
# Rules:
# - For each category:
#   - If the category exists in both inv1 and inv2, merge their inner
#     dictionaries by summing quantities of matching items.
#   - If an item appears in only one inventory, just include it with its quantity.
# - Categories that appear in only one inventory should also appear in the result.

def merge_inventories(inv1, inv2):
    # your code here
    pass


# Test cases
inv_a = {
    "fruits": {"apple": 10, "banana": 5},
    "drinks": {"water": 20}
}

inv_b = {
    "fruits": {"banana": 3, "orange": 7},
    "snacks": {"chips": 15}
}

result = merge_inventories(inv_a, inv_b)
print(result)
# Expected (order may differ):
# {
#   "fruits": {"apple": 10, "banana": 8, "orange": 7},
#   "drinks": {"water": 20},
#   "snacks": {"chips": 15}
# }
