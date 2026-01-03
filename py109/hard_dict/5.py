# Problem 5: Apply a discount to a nested catalog dictionary
# ----------------------------------------------------------
# You have a nested dictionary `catalog`:
# - Top-level keys: category names (e.g. "books", "electronics").
# - Values: dictionaries where:
#     - Keys: item names.
#     - Values: dictionaries with at least a "price" key (float).
#
# Write a function apply_discount(catalog, category_name, discount_percent) that:
# - Returns a NEW catalog (do NOT mutate the original).
# - Only for the given `category_name`:
#     - Reduce each item's "price" by `discount_percent` percent.
#       Example: 10% discount on price 100.0 -> 90.0
# - All other categories should remain unchanged.
# - Assume discount_percent is between 0 and 100.

def apply_discount(catalog, category_name, discount_percent):
    # your code here
    pass


# Test cases
catalog1 = {
    "books": {
        "Book A": {"price": 20.0, "author": "Author A"},
        "Book B": {"price": 30.0, "author": "Author B"},
    },
    "electronics": {
        "Phone": {"price": 500.0, "brand": "BrandX"},
        "Laptop": {"price": 1000.0, "brand": "BrandY"},
    }
}

discounted = apply_discount(catalog1, "books", 10)
print(discounted)
# Expected:
# - In "books", prices should be 18.0 and 27.0 (10% off).
# - In "electronics", prices should remain 500.0 and 1000.0.
# - Original catalog1 should be unchanged.

print(catalog1)  # to check it wasn't modified
