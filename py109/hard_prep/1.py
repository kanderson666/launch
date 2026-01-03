def mystery(a_list): 
    result = [] 
    for idx, value in enumerate(a_list): 
        if value % 2 == 0: 
            result.append(value * 2) 
        else: result.insert(0, value - idx) 
    return result

nums = [3, 4, 5, 6, 7] # 3, 8, 3, 12, 3
                        # 3, 3, 3, 8, 12
print(mystery(nums)) 
print(nums)

# Questions:  
# a) What exactly gets printed?  
# b) Does `mystery` modify the original list `nums`? Explain why or why not.  
# c) In plain English, describe what `mystery` does.
