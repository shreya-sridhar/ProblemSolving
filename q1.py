# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Test Cases :

# only integers
# 1. [0,-1,0,3,12] -> [-1,3,12,0,0]         
# 2. [] -> []
# 3. [0,0,0] -> [0,0,0]
# 4. [1,-2,4] -> [1,-2,4]
# 5. [1,3,-5,0,0] -> [1,3,-5,0,0]
# 6. [0,0,1,-2,3] -> [1,-2,3,0,0]

# Algo :





# [0,-1,0,3,12]
# [-1,3,0,0,12]
# [-1,3,12,0,0]

def move_zeros_to_end(nums): 
    # Set zero index  = -1
    zero_index = -1
    # Start iteratiomg from 0 to n-1 
    for curr_index in range(0, len(nums)): #curr_index = 4
        if nums[curr_index] == 0 and zero_index == -1:
            zero_index = curr_index  #zero_index = 2
            # every time we see non zero we swap with zero index and increment 
        elif nums[curr_index] != 0 and zero_index >= 0:
            temp = nums[curr_index]
            nums[curr_index] = nums[zero_index]
            nums[zero_index] = temp #[-1,3,0,0,12]
            zero_index += 1 
    return nums 

print(move_zeros_to_end([0,-1,0,3,12]))
print(move_zeros_to_end([]))
print(move_zeros_to_end([0,0,0]))
print(move_zeros_to_end([1,-2,4]))
print(move_zeros_to_end([1,3,-5,0,0]))
print(move_zeros_to_end([0,0,1,-2,3]))



