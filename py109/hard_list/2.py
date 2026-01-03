# Problem 2: Merge overlapping intervals
# --------------------------------------
# You are given a list of intervals, where each interval is a list [start, end].
# Example: [[1, 3], [2, 6], [8, 10], [9, 12]]
#
# Write a function merge_intervals(intervals) that:
# - Returns a NEW list of intervals where all overlapping intervals
#   have been merged.
# - Intervals are inclusive: [1, 3] and [3, 5] should be merged to [1, 5].
# - The result should be sorted by start value.
#
# Example:
# [[1, 3], [2, 6], [8, 10], [9, 12]]
# -> [[1, 6], [8, 12]]

def merge_intervals(intervals):
    def sort_input(input_lst):
        result = []
        for lst in input_lst:
            result.append(lst.copy())
        result.sort()
        return result

    if not intervals:
        return intervals

    sorted_intervals = sort_input(intervals)

    result = []
    used = False

    for interval_lst in sorted_intervals:
        for result_lst in result:
            result_lower = result_lst[0]
            result_upper = result_lst[1]
            interval_lower = interval_lst[0]
            interval_upper = interval_lst[1]
            
            if interval_lower <= result_upper and interval_upper > result_upper:
                result_lst[1] = interval_upper
                used = True
                break
            elif interval_lower >= result_lower and interval_upper <= result_upper:
                used = True
                break
        if not used:
            result.append(interval_lst.copy())
        used = False
    return result

# Test cases
# test = [[1, 3], [2, 6]]
# print(merge_intervals(test))

intervals2 = [[1, 4], [4, 5]]
print(merge_intervals(intervals2))
# Expected: [[1, 5]]

intervals1 = [[1, 3], [2, 6], [8, 10], [9, 12]]
print(merge_intervals(intervals1))
# Expected: [[1, 6], [8, 12]]

intervals3 = [[5, 7], [1, 2], [3, 4]]
print(merge_intervals(intervals3))
# Expected: [[1, 2], [3, 4], [5, 7]]

intervals4 = []
print(merge_intervals(intervals4))
# Expected: []
