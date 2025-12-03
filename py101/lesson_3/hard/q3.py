def mess_with_vars_a(one, two, three):
    one = two
    two = three
    three = one

def mess_with_vars_b(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

def mess_with_vars_c(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars_a(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

mess_with_vars_b(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

mess_with_vars_c(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")