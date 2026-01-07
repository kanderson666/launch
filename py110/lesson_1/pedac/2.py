"""
Leftover Blocks
You have a number of building blocks that can be used to build a valid structure. There are certain rules about what determines a valid structure:

The building blocks are cubes.
The structure is built in layers.
The top layer is a single block.
A block in an upper layer must be supported by four blocks in a lower layer.
A block in a lower layer can support more than one block in an upper layer.
You cannot leave gaps between blocks.

Write a program that, given the number of available blocks, 
calculates the number of blocks left over after building the tallest possible valid structure.

Make notes of your mental model for the problem, including:
inputs and outputs.
explicit and implicit rules.
Write a list of clarifying questions for anything that isn't clear.
"""
"""
1. Understand the Problem
Input:
    Integer- total number of building blocks 
Output:
    Integer- number of blocks left over (after building the tallest possible valid structure)
Rules:
    Exlicit:
        - Blocks are cubes
        - Top layer is single block
        - Need 4 blocks below block in upper
        - Lower block can have more than 1 block on top
        - No gaps between blocks
    Implicit:
        - Most efficient tower will have each row squared equal blocks on that row. ex. row 1 = 1 block, row 2 = 4 blocks
Questions:
    - 

2. Examples/test cases
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True

3. Data structure
-Integer 

4. Algorithm
- Ensure block number is above 0
- Check if new layer requires more blocks than we have
- If yes, return blocks we have
- If no, subtract blocks used for that layer, repeat

"""
def calculate_leftover_blocks(blocks_remaining): 
    if blocks_remaining < 1:
        return 0
    layer_num = 1
    while layer_num ** 2 <= blocks_remaining:
        blocks_remaining -= layer_num ** 2
        layer_num += 1
    return blocks_remaining


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True