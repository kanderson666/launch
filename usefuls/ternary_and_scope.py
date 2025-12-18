# from https://github.com/The-SPOT-Hub/SPOT-Wiki/blob/main/LSBot_Exercises/Python/PY101/118.md
def destructive_even_numbers(num_lst):
    for i in range(len(num_lst)):
        num_lst[i] = [num for num in num_lst[i] if not num % 2]
        # in_lst = []
        # for num in num_lst[i]:
        #     if not num % 2:
        #         in_lst.append(num)
        # num_lst[i] = in_lst

def nondestructive_even_numbers(num_lst):
    return [[num for num in sublist if not num % 2] for sublist in num_lst]

    # fixed_lst = []
    # for i in range(len(num_lst)):
    #     fixed_lst.append([])
    #     for num in num_lst[i]:
    #         if not num % 2:
    #             fixed_lst[i].append(num)
    # return fixed_lst

numbers1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ids = [id(lst) for lst in numbers1]
ids2 = [[id(num) for num in sublist] for sublist in numbers1]
print(ids)
print(ids2)

destructive_even_numbers(numbers1)
print(numbers1)  # Output: [[2], [4, 6], [8]]

numbers2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nondestructive_even_numbers(numbers2))  # Output: [[2], [4, 6], [8]]
print(numbers2)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]