"""
P:
    - Make a smart function that creates only numerical palindromes without having to test if its a palindrome, up to a defined number (limit)
    - Input:
        - Integer (limit)
    - Output:
        - List of integers (list of palindromes)
    - Rules:
        - No checking if is a palindrome
        - At least 2 digits
E:
    - 11 , 22, 33, 44, 55, ... 99
    - 101, 111, 121, 131, 141, 151 ... 191
    - 202, 212, 222, 232 ... 292
    - ... 989, 999
    - 1001, 1111, 1221, 1331, ... 1991
    - 2002, 2112, 2222, ... 2992
    - ... 9009, ... 9889, 9999
    - 10001, 10101, 10201, 10301, ... 10901
    - 11011, 11111, 11211, 11311
D:
    - 1 counter for 2 digits
    - 2 counters for 3 or 4 digits
    - 3 counters for 5 or 6 digits

    - Input: Integer (limit)
    - Output: List of integers (list of palindromes)
A:
    - Outer counter, inner counter, outer counter   1|0|1
    - outer, inner, inner, outer                   10|01
    - outerr, outer, inner, outer, outerr          21|0|12
    -                                             210|012
    -                                             321|0|123
    -                                            3210|0123
"""
import pdb
from os import system

DIGIT_LIMIT = 3     # 1 = 1,000      2 = 100,000  3 = 10,000,000
LAST_NUM = 10**DIGIT_LIMIT

def palindrome(result):
    for num in range(LAST_NUM):
        if num == 0:
            continue
        num = str(num)
        num_string = num + num[::-1]
        result.append(num_string)
        if all_nines(num_string):
            special(result, int(num))

def all_nines(num_string):
    for num in num_string:
        if num != '9':
            return False
    return True

def special(result, size):
    for num in range(10**(len(str(size)) - 1), size + 1):
        if num == 0:
            continue
        num = str(num)
        for add in range(10):
            add = str(add)
            num_string = num + add + num[::-1]
            result.append(num_string)

def check(result):
    checks = ['99', '999', '9999', '99999', '999999', '9999999', '99999999' '999999999']
    result.append("Done")

    system("clear")
    # print(result)
    print(result[-2])

    for idx, n in enumerate(result):
        for check in checks:
            if n == check:
                print(idx, n)
                print(idx + 1, result[idx + 1])
def main():
    result = []
    palindrome(result)
        
    check(result)

if __name__ == "__main__":
    main()

# LOOP_LIMIT = 2
# # include_first_counter = False
# include_first_counter = True

# def loop(result, num_string, num_of_loops):
#     global include_first_counter
#     # if len(result) > 2000:
#     #     return
        
#     if num_of_loops < LOOP_LIMIT:
#         num_of_loops += 1

#         for num in range(100):
#             if num == 0:
#                 num_string += '00'
#             elif num < 10:
#                 num_string = num_string[:-1] + str(num)
#             else:
#                 num_string = num_string[:-2] + str(num)
            
#             loop(result, num_string, num_of_loops)

#     else:
#         # switch = all_nines(num_string)
#         num_string = num_string.lstrip('0')
#         if not num_string:
#             for num in range(1, 10):
#                 result.append(str(num) * 2)
#             temp_string = ""
        
#         elif include_first_counter:
#             for num in range(10):
#                 num = str(num)
#                 temp_string = num_string
#                 temp_string = temp_string + num + temp_string[::-1]
#                 result.append(temp_string)
#                 if all_nines(num_string):
#                     include_first_counter = flip(include_first_counter)
#         else:
#             temp_string = num_string
#             temp_string = temp_string + temp_string[::-1]
#             result.append(temp_string)
#             if all_nines(num_string):
#                 include_first_counter = flip(include_first_counter)
#                 loop(result, num_string, num_of_loops)

        

# def all_nines(num_string):
#     # pdb.set_trace()
#     if not num_string:
#         return False
#     for num in num_string:
#         if num != '9':
#             return False
#     return True

# def flip(include_first_counter):
#     if include_first_counter:
#         return False
#     return True

# checks = ['99', '999', '9999', '99999', '999999', '9999999', '99999999' '999999999']
# result = []
# num_string = ""
# loop(result, num_string, 0)
# system("clear")
# # print(result[:500])
# for idx, n in enumerate(result):
#     for check in checks:
#         if n == check:
#             print(idx, n)
#             print(idx + 1, result[idx + 1])


# def loop(result, num_string, num_of_loops):
#     global include_first_counter
#     if len(result) > 200:
#         return
        
#     if num_of_loops != LOOP_LIMIT:
#         num_of_loops += 1

#         for num in range(100):
#             num = str(num)

#             if num == '0':
#                 num_string += num
#             else:
#                 num_string = num_string[:-1] + num
#             loop(result, num_string, num_of_loops)

#     else:
#         num_string = num_string.lstrip('0')
#         if not num_string:
#             return

#         if include_first_counter:
#             for num in range(10):
#                 num = str(num)
#                 temp_string = num_string
#                 temp_string = temp_string + num + temp_string[::-1]
#                 result.append(temp_string)
#         else:
#             temp_string = num_string
#             temp_string = temp_string + temp_string[::-1]
#             result.append(temp_string)

#         if all_nines(num_string):
#             include_first_counter = flip(include_first_counter)

# def all_nines(num_string):
#     if not num_string:
#         return False
#     for num in num_string:
#         if num != '9':
#             return False
#     return True

# def flip(include_first_counter):
#     if include_first_counter:
#         return False
#     return True

# def last_call(num_string, single):
    

# do_once = [True for _ in range(LOOP_LIMIT)]

# result = [""]
# loop(result, "", 0)
# system("clear")
# for res in result:
#     print(res)
# print(result)

# SINGLE = 1
# DOUBLE = 0

# def palindrome(limit):
#     result = []
#     num = ""
#     single = True
#     for three in range(10):
#         three = str(three)
#         for two in range(10):
#             two = str(two)
#             for one in range(10):
#                 one = str(one)

#                 if single:
#                     num = three + two + one + two + three
#                 else:
#                     num = three + two + one + one + two + three

#                 num = num.strip('0')
#                 if len(num) < 2:
#                     continue
#                 else:
#                     result.append(num)
#                 if len(result) == limit:
#                     return result
#     return result
# print(palindrome(5020))


    # for ten in range(10):
    #     ten = str(ten)
    #     for nine in range(10):
    #         nine = str(nine)
    #         for eight in range(10):
    #             eight = str(eight)
    #             for seven in range(10):
    #                 seven = str(seven)
    #                 for six in range(10):
    #                     six = str(six)
    #                     for five in range(10):
    #                         five = str(five)
    #                         for four in range(10):
    #                             four = str(four)
    #                             for three in range(10):
    #                                 three = str(three)
    #                                 for two in range(10):
    #                                     two = str(two)
    #                                     for one in range(10):
    #                                         one = str(one)
    #                                         # num = ten + nine + eight + seven + six + five + four + three + two + one + one + two + three + four + five + six + seven + eight + nine + ten
    #                                         num = ten + nine + eight + seven + six + five + four + three + two + one + two + three + four + five + six + seven + eight + nine + ten
    #                                         result.append(num.strip('0'))
    #                                         if len(result) == limit:
    #                                             return result[-5::]

